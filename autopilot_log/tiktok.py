#!/usr/bin/env python
"""Upload a video to TikTok with no browser, through the Content Posting API.

Facts this tool is built around (all from TikTok's own documentation):

  * Direct posts from an unaudited client are restricted to SELF_ONLY. Posting accounts
    must be private, and each client can serve at most five users in a 24-hour period.
  * TikTok rotates refresh tokens when they are used. The newly returned refresh token
    must be saved before its access token is used or the stored credential can go stale.
  * TikTok has two different doors: video.upload sends a video to the creator's inbox for
    a final human tap, while video.publish can post directly after the required audit.
  * post_mode must be explicit. MEDIA_UPLOAD means inbox delivery; DIRECT_POST means a
    direct post.

Safety rails, on by design:

  * Secrets are read through autopilot_log.keystore and never printed or logged.
  * A posting gate must explicitly allow TikTok before this tool accepts a direct-post
    privacy level other than SELF_ONLY. Missing, unreadable, malformed, or merely truthy
    values all fail closed.
  * Inbox upload does not need the gate because the creator makes the final post in the
    TikTok app.
  * Every real direct post queries creator_info first and refuses a privacy level that
    TikTok does not list for that creator.

Output is deliberately ASCII-only so that Windows consoles cannot mangle it.

Commands
  where
  auth-url  --shelf NAME [--scopes S]
  auth      --shelf NAME
  exchange  --shelf NAME --code CODE
  whoami    --shelf NAME
  upload    --shelf NAME --file PATH [--title T] [--dry-run]
  publish   --shelf NAME --file PATH --title T [--privacy P]
            [--disable-comment] [--disable-duet] [--disable-stitch]
            [--brand-content] [--brand-organic] [--aigc] [--cover-ms N] [--dry-run]
  status    --shelf NAME --publish-id ID
"""

import argparse
import base64
import hashlib
import json
import os
import secrets
import sys
import time
import urllib.parse

import requests

from . import keystore

AUTH_URL = "https://www.tiktok.com/v2/auth/authorize/"
TOKEN_URL = "https://open.tiktokapis.com/v2/oauth/token/"
API_URL = "https://open.tiktokapis.com/v2"
CREATOR_INFO_URL = API_URL + "/post/publish/creator_info/query/"
DIRECT_INIT_URL = API_URL + "/post/publish/video/init/"
INBOX_INIT_URL = API_URL + "/post/publish/inbox/video/init/"
STATUS_URL = API_URL + "/post/publish/status/fetch/"

REDIRECT = "http://127.0.0.1:8766/"
SCOPES_DEFAULT = "user.info.basic,video.upload"
SCOPES_AUDITED = "user.info.basic,video.publish,video.upload"

CHUNK_MIN = 5 * 1024 * 1024
CHUNK_MAX = 64 * 1024 * 1024
TIMEOUT = 120

PRIVACY_LEVELS = (
    "SELF_ONLY",
    "MUTUAL_FOLLOW_FRIENDS",
    "FOLLOWER_OF_CREATOR",
    "PUBLIC_TO_EVERYONE",
)

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except Exception:
        pass


def die(msg):
    sys.stderr.write("ERROR: %s\n" % msg)
    sys.exit(1)


# ---------------------------------------------------------------- credentials

def client_creds():
    creds = keystore.get("tiktok-api")
    if not creds or not creds.get("CLIENT_KEY") or not creds.get("CLIENT_SECRET"):
        die("no TikTok API client stored yet (%s).\n"
            "Store CLIENT_KEY and CLIENT_SECRET in service 'tiktok-api' using the\n"
            "configured keystore. Never put the client secret on a command line."
            % keystore.describe())
    return creds["CLIENT_KEY"], creds["CLIENT_SECRET"]


# ---------------------------------------------------------------- posting gate

def gate_path():
    return os.environ.get("AUTOPILOT_LOG_GATE") or os.path.join(
        os.getcwd(), "posting-gate.json")


def gate_allows_public():
    """True only when the gate file explicitly opens TikTok. Fail closed."""
    try:
        with open(gate_path(), "r", encoding="utf-8") as fh:
            cfg = json.load(fh)
    except Exception:
        return False
    if not isinstance(cfg, dict):
        return False
    channels = cfg.get("channels")
    if not isinstance(channels, dict):
        return False
    channel = channels.get("tiktok")
    if not isinstance(channel, dict):
        return False
    return channel.get("allowed") is True


def check_privacy(privacy):
    if privacy not in PRIVACY_LEVELS:
        die("unknown privacy level %r (allowed: %s)"
            % (privacy, ", ".join(PRIVACY_LEVELS)))
    if privacy != "SELF_ONLY" and not gate_allows_public():
        die("the posting gate is CLOSED for tiktok (%s).\n"
            "Only privacy_level=SELF_ONLY is allowed until the gate says\n"
            '  {"channels": {"tiktok": {"allowed": true}}}\n'
            "Refusing." % gate_path())
    return privacy


# ---------------------------------------------------------------- oauth

def pkce_pair():
    verifier = base64.urlsafe_b64encode(secrets.token_bytes(48)).decode().rstrip("=")
    challenge = hashlib.sha256(verifier.encode()).hexdigest()
    return verifier, challenge


def consent_url(client_key, scopes, challenge=None, state=None):
    query = {
        "client_key": client_key,
        "scope": scopes,
        "response_type": "code",
        "redirect_uri": REDIRECT,
    }
    if challenge:
        query["code_challenge"] = challenge
        query["code_challenge_method"] = "S256"
    if state:
        query["state"] = state
    return AUTH_URL + "?" + urllib.parse.urlencode(query)


def token_call(payload):
    response = requests.post(
        TOKEN_URL,
        data=payload,
        timeout=TIMEOUT,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    try:
        body = response.json()
    except Exception:
        die("token endpoint returned non-JSON (HTTP %s)" % response.status_code)
    if response.status_code != 200 or body.get("error"):
        die("token exchange failed (HTTP %s, error=%s)"
            % (response.status_code, body.get("error")))
    return body


def save_token(shelf, body, display_name=None):
    refresh_token = body.get("refresh_token")
    if not refresh_token:
        die("TikTok returned no refresh_token")
    current = keystore.get("tiktok-token-" + shelf) or {}
    pairs = {
        "REFRESH_TOKEN": refresh_token,
        "OPEN_ID": body.get("open_id") or current.get("OPEN_ID", ""),
        "DISPLAY_NAME": (
            display_name if display_name is not None
            else current.get("DISPLAY_NAME", "")
        ),
    }
    keystore.put(
        "tiktok-token-" + shelf,
        pairs,
        "TikTok account token for shelf '%s'" % shelf,
    )


def exchange_code(shelf, code, verifier=None):
    key, secret = client_creds()
    payload = {
        "client_key": key,
        "client_secret": secret,
        "code": code,
        "grant_type": "authorization_code",
        "redirect_uri": REDIRECT,
    }
    if verifier:
        payload["code_verifier"] = verifier
    body = token_call(payload)
    save_token(shelf, body)
    print("saved: shelf=%s TikTok token stored" % shelf)


def access_token(shelf):
    """Refresh, save the rotated refresh token, then return the access token."""
    service = "tiktok-token-" + shelf
    saved = keystore.get(service)
    if not saved or not saved.get("REFRESH_TOKEN"):
        die("no refresh token for shelf '%s'. Run:\n"
            "  python -m autopilot_log.tiktok auth --shelf %s" % (shelf, shelf))
    key, secret = client_creds()
    body = token_call({
        "client_key": key,
        "client_secret": secret,
        "grant_type": "refresh_token",
        "refresh_token": saved["REFRESH_TOKEN"],
    })
    save_token(shelf, body)
    return body["access_token"]


def loopback_code(url):
    """Serve the loopback redirect once and return its code."""
    from http.server import BaseHTTPRequestHandler, HTTPServer

    received = {}

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            query = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            received["code"] = (query.get("code") or [None])[0]
            received["error"] = (query.get("error") or [None])[0]
            received["state"] = (query.get("state") or [None])[0]
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            message = "OK. Close this tab." if received["code"] else "Authorization failed."
            self.wfile.write(message.encode("utf-8"))

        def log_message(self, *args):
            pass

    server = HTTPServer(("127.0.0.1", 8766), Handler)
    print("open this URL in a browser signed in to the target TikTok account:")
    print("")
    print(url)
    print("")
    print("waiting for the allow click on %s ..." % REDIRECT)
    server.handle_request()
    server.server_close()
    if not received.get("code"):
        die("consent was not granted: %s" % received.get("error"))
    return received


# ---------------------------------------------------------------- API and upload

def api_post(url, token, payload):
    response = requests.post(
        url,
        headers={
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json; charset=UTF-8",
        },
        data=json.dumps(payload),
        timeout=TIMEOUT,
    )
    try:
        body = response.json()
    except Exception:
        die("TikTok API returned non-JSON (HTTP %s)" % response.status_code)
    error = body.get("error") or {}
    if response.status_code != 200 or error.get("code") not in (None, "", "ok"):
        die("TikTok API request failed (HTTP %s, code=%s)"
            % (response.status_code, error.get("code")))
    return body


def chunk_plan(size):
    """Return TikTok's chunk size and count for a file size."""
    if size < 1:
        die("video file is empty")
    if size <= CHUNK_MAX:
        return size, 1
    count = (size + CHUNK_MAX - 1) // CHUNK_MAX
    if count > 1000:
        die("file too large for TikTok's 1000-chunk limit (%d bytes)" % size)
    chunk = size // count
    if chunk < CHUNK_MIN:
        die("computed chunk %d is below TikTok's 5MB minimum" % chunk)
    return chunk, count


def source_info(path):
    if not os.path.isfile(path):
        die("no such file: %s" % path)
    size = os.path.getsize(path)
    chunk, count = chunk_plan(size)
    return {
        "source": "FILE_UPLOAD",
        "video_size": size,
        "chunk_size": chunk,
        "total_chunk_count": count,
    }, size, chunk, count


def put_chunks(upload_url, path, size, chunk, count):
    with open(path, "rb") as fh:
        for index in range(count):
            start = index * chunk
            end = size - 1 if index == count - 1 else start + chunk - 1
            fh.seek(start)
            data = fh.read(end - start + 1)
            response = requests.put(
                upload_url,
                data=data,
                timeout=TIMEOUT,
                headers={
                    "Content-Type": "video/mp4",
                    "Content-Length": str(len(data)),
                    "Content-Range": "bytes %d-%d/%d" % (start, end, size),
                },
            )
            if response.status_code not in (200, 201, 206):
                die("chunk %d/%d rejected (HTTP %s)"
                    % (index + 1, count, response.status_code))


def creator_info(token):
    return (api_post(CREATOR_INFO_URL, token, {}).get("data") or {})


def upload(shelf, path, title, dry_run):
    source, size, chunk, count = source_info(path)
    payload = {
        "post_mode": "MEDIA_UPLOAD",
        "media_type": "VIDEO",
        "source_info": source,
    }
    output = {
        "endpoint": INBOX_INIT_URL,
        "payload": payload,
        "title_note": title or "",
        "note": "inbox upload; the creator makes the final post in the TikTok app",
    }
    if dry_run:
        print(json.dumps(output, indent=2, ensure_ascii=True))
        return
    token = access_token(shelf)
    body = api_post(INBOX_INIT_URL, token, payload)
    data = body.get("data") or {}
    if not data.get("upload_url"):
        die("inbox init returned no upload_url")
    put_chunks(data["upload_url"], path, size, chunk, count)
    print("inbox publish_id=%s (finish the post in the TikTok app)"
          % data.get("publish_id"))


def publish(shelf, path, title, privacy, disable_comment, disable_duet,
            disable_stitch, brand_content, brand_organic, aigc, cover_ms,
            dry_run):
    privacy = check_privacy(privacy)
    source, size, chunk, count = source_info(path)
    post_info = {
        "title": title,
        "privacy_level": privacy,
        "disable_comment": bool(disable_comment),
        "disable_duet": bool(disable_duet),
        "disable_stitch": bool(disable_stitch),
        "is_aigc": bool(aigc),
        "brand_content_toggle": bool(brand_content),
        "brand_organic_toggle": bool(brand_organic),
    }
    if cover_ms is not None:
        post_info["video_cover_timestamp_ms"] = cover_ms
    payload = {
        "post_mode": "DIRECT_POST",
        "media_type": "VIDEO",
        "post_info": post_info,
        "source_info": source,
    }
    if dry_run:
        print(json.dumps({
            "endpoint": DIRECT_INIT_URL,
            "gate_open": gate_allows_public(),
            "payload": payload,
        }, indent=2, ensure_ascii=True))
        return

    token = access_token(shelf)
    info = creator_info(token)
    allowed = info.get("privacy_level_options")
    if not isinstance(allowed, list) or privacy not in allowed:
        shown = ", ".join(allowed) if isinstance(allowed, list) else "(none returned)"
        die("TikTok does not currently allow privacy_level=%s for this creator.\n"
            "Allowed: %s" % (privacy, shown))
    body = api_post(DIRECT_INIT_URL, token, payload)
    data = body.get("data") or {}
    if not data.get("upload_url"):
        die("direct init returned no upload_url")
    put_chunks(data["upload_url"], path, size, chunk, count)
    print("direct publish_id=%s privacy=%s" % (data.get("publish_id"), privacy))


def whoami(shelf):
    token = access_token(shelf)
    info = creator_info(token)
    nickname = info.get("creator_nickname") or ""
    keystore.put(
        "tiktok-token-" + shelf,
        {"DISPLAY_NAME": nickname},
        "TikTok account token for shelf '%s'" % shelf,
    )
    print("nickname=%s" % nickname)
    print("privacy_level_options=%s"
          % ",".join(info.get("privacy_level_options") or []))


def status(shelf, publish_id):
    token = access_token(shelf)
    body = api_post(STATUS_URL, token, {"publish_id": publish_id})
    print(json.dumps(body.get("data") or {}, indent=2, ensure_ascii=True))


# ---------------------------------------------------------------- main

def main(argv=None):
    parser = argparse.ArgumentParser(prog="autopilot_log.tiktok")
    commands = parser.add_subparsers(dest="cmd", required=True)

    commands.add_parser("where")

    command = commands.add_parser("auth-url")
    command.add_argument("--shelf", required=True)
    command.add_argument("--scopes", default=SCOPES_DEFAULT)

    command = commands.add_parser("auth")
    command.add_argument("--shelf", required=True)

    command = commands.add_parser("exchange")
    command.add_argument("--shelf", required=True)
    command.add_argument("--code", required=True)

    command = commands.add_parser("whoami")
    command.add_argument("--shelf", required=True)

    command = commands.add_parser("upload")
    command.add_argument("--shelf", required=True)
    command.add_argument("--file", required=True)
    command.add_argument("--title", default="")
    command.add_argument("--dry-run", action="store_true")

    command = commands.add_parser("publish")
    command.add_argument("--shelf", required=True)
    command.add_argument("--file", required=True)
    command.add_argument("--title", required=True)
    command.add_argument("--privacy", default="SELF_ONLY", choices=PRIVACY_LEVELS)
    command.add_argument("--disable-comment", action="store_true")
    command.add_argument("--disable-duet", action="store_true")
    command.add_argument("--disable-stitch", action="store_true")
    command.add_argument("--brand-content", action="store_true")
    command.add_argument("--brand-organic", action="store_true")
    command.add_argument("--aigc", action="store_true")
    command.add_argument("--cover-ms", type=int)
    command.add_argument("--dry-run", action="store_true")

    command = commands.add_parser("status")
    command.add_argument("--shelf", required=True)
    command.add_argument("--publish-id", required=True)

    args = parser.parse_args(argv)

    if args.cmd == "where":
        print(keystore.describe())
        print("gate=%s allows_public=%s"
              % (gate_path(), gate_allows_public()))
    elif args.cmd == "auth-url":
        key, _secret = client_creds()
        print(consent_url(key, args.scopes))
    elif args.cmd == "auth":
        key, _secret = client_creds()
        verifier, challenge = pkce_pair()
        state = secrets.token_urlsafe(12)
        received = loopback_code(consent_url(key, SCOPES_DEFAULT, challenge, state))
        if received.get("state") != state:
            die("state mismatch; refusing the authorization code")
        exchange_code(args.shelf, received["code"], verifier)
    elif args.cmd == "exchange":
        exchange_code(args.shelf, args.code)
    elif args.cmd == "whoami":
        whoami(args.shelf)
    elif args.cmd == "upload":
        upload(args.shelf, args.file, args.title, args.dry_run)
    elif args.cmd == "publish":
        if args.cover_ms is not None and args.cover_ms < 0:
            die("--cover-ms must be zero or greater")
        publish(
            args.shelf,
            args.file,
            args.title,
            args.privacy,
            args.disable_comment,
            args.disable_duet,
            args.disable_stitch,
            args.brand_content,
            args.brand_organic,
            args.aigc,
            args.cover_ms,
            args.dry_run,
        )
    elif args.cmd == "status":
        status(args.shelf, args.publish_id)


if __name__ == "__main__":
    main()
