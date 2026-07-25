#!/usr/bin/env python
"""Upload a video to YouTube with no browser, through YouTube Data API v3.

Facts this tool is built around (all from Google's own documentation):

  * Service accounts cannot upload to YouTube - the API answers NoLinkedYouTubeAccount.
    So every channel needs exactly ONE human "allow" click, once, ever. After that the
    stored refresh token lets this run unattended forever.
  * An OAuth app left in "Testing" publishing status is issued refresh tokens that expire
    after 7 days. Publish the app to production or unattended posting dies every week.
  * Until the Google Cloud project passes the YouTube API compliance audit, EVERY video
    uploaded through the API is locked to private and cannot be unlocked by hand. A
    successful upload is not the same thing as a published video.
  * videos.insert costs one of 100 uploads per day, separate from the 10,000-unit daily
    quota for everything else.

Safety rails, on by design:

  * Secrets are read through autopilot_log.keystore and never printed or logged.
  * A posting gate file (posting-gate.json) must explicitly say youtube is allowed before
    this tool will request anything other than privacyStatus=private. It fails closed:
    a missing, unreadable or malformed gate means "private only".

Output is deliberately ASCII-only so that Windows consoles cannot mangle it.

Commands
  where                                 print which keystore and gate file are in use
  auth-url                              print the consent URL (open it in the right browser)
  auth       --shelf NAME               run the local loopback flow, save the refresh token
  exchange   --shelf NAME --code CODE   save a refresh token from a hand-pasted code
  whoami     --shelf NAME               print the channel a stored token belongs to
  upload     --shelf NAME --file PATH --title T [--desc D] [--tags a,b]
             [--privacy private|unlisted|public] [--publish-at 2026-07-26T09:00:00Z]
             [--category 22] [--dry-run]

"shelf" is just the nickname you give one channel, so several channels can live side by
side: --shelf main, --shelf cooking, --shelf en.
"""

import argparse
import json
import os
import sys
import urllib.parse

import requests

from . import keystore

SCOPES = ("https://www.googleapis.com/auth/youtube.upload "
          "https://www.googleapis.com/auth/youtube.readonly")
REDIRECT = "http://localhost:8765/"
TOKEN_URL = "https://oauth2.googleapis.com/token"
AUTH_URL = "https://accounts.google.com/o/oauth2/v2/auth"
UPLOAD_URL = "https://www.googleapis.com/upload/youtube/v3/videos"
API_URL = "https://www.googleapis.com/youtube/v3"

TIMEOUT = 60

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass


def die(msg):
    sys.stderr.write("ERROR: %s\n" % msg)
    sys.exit(1)


# ---------------------------------------------------------------- credentials

def client_creds():
    creds = keystore.get("youtube-api")
    if not creds or not creds.get("CLIENT_ID") or not creds.get("CLIENT_SECRET"):
        die("no OAuth client stored yet (%s).\n"
            "Create a Google Cloud project, enable YouTube Data API v3, make an OAuth client of\n"
            "type 'Desktop app', then store it:\n"
            "  python -m autopilot_log.youtube set-client --client-id ... --client-secret ...\n"
            "See README, section 'Get a key'." % keystore.describe())
    return creds["CLIENT_ID"], creds["CLIENT_SECRET"]


# ---------------------------------------------------------------- posting gate

def gate_path():
    return os.environ.get("AUTOPILOT_LOG_GATE") or os.path.join(os.getcwd(), "posting-gate.json")


def gate_allows_public():
    """True only when the gate file explicitly opens YouTube. Fails closed."""
    try:
        with open(gate_path(), "r", encoding="utf-8") as fh:
            cfg = json.load(fh)
    except Exception:
        return False
    ch = (cfg.get("channels") or {}).get("youtube") or {}
    return ch.get("allowed") is True


# ---------------------------------------------------------------- oauth

def consent_url(client_id):
    q = {
        "client_id": client_id,
        "redirect_uri": REDIRECT,
        "response_type": "code",
        "scope": SCOPES,
        "access_type": "offline",
        "prompt": "consent",
        "include_granted_scopes": "true",
    }
    return AUTH_URL + "?" + urllib.parse.urlencode(q)


def exchange_code(client_id, client_secret, code):
    r = requests.post(TOKEN_URL, timeout=TIMEOUT, data={
        "code": code,
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": REDIRECT,
        "grant_type": "authorization_code",
    })
    if r.status_code != 200:
        die("token exchange failed %s: %s" % (r.status_code, r.text[:500]))
    tok = r.json()
    if not tok.get("refresh_token"):
        die("no refresh_token was returned. The consent must use prompt=consent and\n"
            "access_type=offline, and the OAuth app must not be in 'Testing' status.")
    return tok


def access_token(shelf):
    cid, csec = client_creds()
    rt = keystore.get("youtube-token-" + shelf, "REFRESH_TOKEN")
    if not rt:
        die("no refresh token for shelf '%s'. Run:\n"
            "  python -m autopilot_log.youtube auth --shelf %s" % (shelf, shelf))
    r = requests.post(TOKEN_URL, timeout=TIMEOUT, data={
        "refresh_token": rt,
        "client_id": cid,
        "client_secret": csec,
        "grant_type": "refresh_token",
    })
    if r.status_code != 200:
        die("refresh failed %s: %s\n"
            "If this says invalid_grant, the OAuth app is most likely still in 'Testing'\n"
            "status - those refresh tokens die after 7 days. Publish the app to production."
            % (r.status_code, r.text[:400]))
    return r.json()["access_token"]


def channel_of(tok):
    r = requests.get(API_URL + "/channels", timeout=TIMEOUT,
                     params={"part": "snippet", "mine": "true"},
                     headers={"Authorization": "Bearer " + tok})
    if r.status_code != 200:
        die("channels.list failed %s: %s" % (r.status_code, r.text[:400]))
    items = r.json().get("items") or []
    if not items:
        die("this Google account has no YouTube channel yet. Create the channel first.")
    return {"id": items[0]["id"], "title": items[0]["snippet"]["title"]}


def save_token(shelf, tok):
    ch = channel_of(tok["access_token"])
    keystore.put("youtube-token-" + shelf, {
        "REFRESH_TOKEN": tok["refresh_token"],
        "CHANNEL_ID": ch["id"],
        "CHANNEL_TITLE": ch["title"],
    }, "YouTube channel token for shelf '%s'" % shelf)
    print("saved: shelf=%s channel=%s (%s)" % (shelf, ch["title"], ch["id"]))


def loopback_code(url):
    """Serve http://localhost:8765/ once and return the ?code= Google redirects back with."""
    from http.server import BaseHTTPRequestHandler, HTTPServer
    box = {}

    class H(BaseHTTPRequestHandler):
        def do_GET(self):
            q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            box["code"] = (q.get("code") or [None])[0]
            box["error"] = (q.get("error") or [None])[0]
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            msg = "OK - you can close this tab." if box["code"] else "FAILED: %s" % box["error"]
            self.wfile.write(("<html><body style='font:28px sans-serif;padding:40px'>%s</body></html>"
                              % msg).encode("utf-8"))

        def log_message(self, *a):
            pass

    srv = HTTPServer(("127.0.0.1", 8765), H)
    print("open this URL in a browser that is signed in to the target channel:")
    print("")
    print(url)
    print("")
    print("waiting for the allow click on http://localhost:8765/ ...")
    srv.handle_request()
    srv.server_close()
    if not box.get("code"):
        die("consent was not granted: %s" % box.get("error"))
    return box["code"]


# ---------------------------------------------------------------- upload

def upload(shelf, path, title, desc, tags, privacy, publish_at, category, dry):
    if not os.path.isfile(path):
        die("no such file: %s" % path)
    size = os.path.getsize(path)

    if privacy != "private" or publish_at:
        if not gate_allows_public():
            die("the posting gate is CLOSED for youtube (%s).\n"
                "Only privacyStatus=private is allowed until the gate says\n"
                '  {"channels": {"youtube": {"allowed": true}}}\n'
                "Refusing." % gate_path())

    body = {
        "snippet": {
            "title": title[:100],
            "description": (desc or "")[:5000],
            "tags": tags or [],
            "categoryId": str(category),
        },
        "status": {
            "privacyStatus": privacy,
            "selfDeclaredMadeForKids": False,
        },
    }
    if publish_at:
        body["status"]["publishAt"] = publish_at
        body["status"]["privacyStatus"] = "private"  # the API requires this when scheduling

    if dry:
        print("DRY RUN - would upload %s (%d bytes) as:" % (path, size))
        print(json.dumps(body, ensure_ascii=False, indent=2))
        return

    tok = access_token(shelf)

    r = requests.post(UPLOAD_URL, timeout=TIMEOUT,
                      params={"uploadType": "resumable", "part": "snippet,status"},
                      headers={
                          "Authorization": "Bearer " + tok,
                          "Content-Type": "application/json; charset=UTF-8",
                          "X-Upload-Content-Length": str(size),
                          "X-Upload-Content-Type": "video/*",
                      },
                      data=json.dumps(body).encode("utf-8"))
    if r.status_code not in (200, 201):
        die("resumable init failed %s: %s" % (r.status_code, r.text[:600]))
    session = r.headers.get("Location")
    if not session:
        die("resumable init returned no Location header")

    with open(path, "rb") as fh:
        r2 = requests.put(session, data=fh, timeout=None,
                          headers={"Content-Type": "video/*", "Content-Length": str(size)})
    if r2.status_code not in (200, 201):
        die("upload failed %s: %s" % (r2.status_code, r2.text[:600]))

    v = r2.json()
    vid = v.get("id")
    got = (v.get("status") or {}).get("privacyStatus")
    print("uploaded: id=%s privacyStatus=%s url=https://youtu.be/%s" % (vid, got, vid))
    if got == "private" and privacy != "private":
        print("WARNING: asked for '%s' but YouTube forced 'private'. That is the unaudited-project\n"
              "lock - the video CANNOT be unlocked by hand. Pass the API compliance audit first."
              % privacy)


# ---------------------------------------------------------------- main

def main(argv=None):
    ap = argparse.ArgumentParser(prog="autopilot_log.youtube")
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("where")
    sub.add_parser("auth-url")

    s = sub.add_parser("set-client")
    s.add_argument("--client-id", required=True)
    s.add_argument("--client-secret", required=True)

    for name in ("auth", "whoami"):
        s = sub.add_parser(name)
        s.add_argument("--shelf", required=True)

    s = sub.add_parser("exchange")
    s.add_argument("--shelf", required=True)
    s.add_argument("--code", required=True)

    s = sub.add_parser("upload")
    s.add_argument("--shelf", required=True)
    s.add_argument("--file", required=True)
    s.add_argument("--title", required=True)
    s.add_argument("--desc", default="")
    s.add_argument("--tags", default="")
    s.add_argument("--privacy", default="private", choices=["private", "unlisted", "public"])
    s.add_argument("--publish-at", default="")
    s.add_argument("--category", default="22")
    s.add_argument("--dry-run", action="store_true")

    a = ap.parse_args(argv)

    if a.cmd == "where":
        print(keystore.describe())
        print("gate=%s allows_public=%s" % (gate_path(), gate_allows_public()))
    elif a.cmd == "set-client":
        keystore.put("youtube-api",
                     {"CLIENT_ID": a.client_id, "CLIENT_SECRET": a.client_secret},
                     "YouTube Data API v3 OAuth desktop client")
        print("saved: client id ending '%s', secret ending '%s' -> %s"
              % (a.client_id[-4:], a.client_secret[-4:], keystore.describe()))
    elif a.cmd == "auth-url":
        cid, _ = client_creds()
        print(consent_url(cid))
    elif a.cmd == "auth":
        cid, csec = client_creds()
        code = loopback_code(consent_url(cid))
        save_token(a.shelf, exchange_code(cid, csec, code))
    elif a.cmd == "exchange":
        cid, csec = client_creds()
        save_token(a.shelf, exchange_code(cid, csec, a.code))
    elif a.cmd == "whoami":
        ch = channel_of(access_token(a.shelf))
        print("shelf=%s channel=%s (%s)" % (a.shelf, ch["title"], ch["id"]))
    elif a.cmd == "upload":
        upload(a.shelf, a.file, a.title, a.desc,
               [t.strip() for t in a.tags.split(",") if t.strip()],
               a.privacy, a.publish_at, a.category, a.dry_run)


if __name__ == "__main__":
    main()
