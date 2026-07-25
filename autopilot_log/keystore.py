"""Where secrets live.

Autopilot Log never puts a credential in the repository, in a log line, or on the
terminal. It reads and writes them through one of three interchangeable backends,
chosen with the ``AUTOPILOT_LOG_KEYSTORE`` environment variable:

    file    (default)  ~/.autopilot-log/keys.json, created with owner-only permissions
    env                read-only, from AUTOPILOT_LOG_<SERVICE>_<FIELD> variables
    dpapi              Windows only: a PowerShell shelf encrypted with DPAPI CurrentUser

A "service" is a named bag of fields, for example::

    youtube-api            CLIENT_ID, CLIENT_SECRET          (one per Google Cloud project)
    youtube-token-main     REFRESH_TOKEN, CHANNEL_ID, ...    (one per YouTube channel)

Only ``get`` ever returns a raw value, and callers pass it straight to the Google
token endpoint. Nothing here prints a secret.
"""

import json
import os
import stat
import subprocess
import sys

DEFAULT_DIR = os.path.join(os.path.expanduser("~"), ".autopilot-log")
DEFAULT_FILE = os.path.join(DEFAULT_DIR, "keys.json")


def _backend():
    return (os.environ.get("AUTOPILOT_LOG_KEYSTORE") or "file").strip().lower()


# ---------------------------------------------------------------- file backend

def _file_path():
    return os.environ.get("AUTOPILOT_LOG_KEYFILE") or DEFAULT_FILE


def _file_load():
    path = _file_path()
    if not os.path.isfile(path):
        return {}
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def _file_save(data):
    path = _file_path()
    parent = os.path.dirname(path)
    if parent and not os.path.isdir(parent):
        os.makedirs(parent, exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2, sort_keys=True)
    os.replace(tmp, path)
    # Best effort on POSIX; Windows ACLs already restrict the user profile directory.
    try:
        os.chmod(path, stat.S_IRUSR | stat.S_IWUSR)
    except OSError:
        pass


# ---------------------------------------------------------------- env backend

def _env_key(service, field):
    safe = "".join(c if c.isalnum() else "_" for c in service).upper()
    return "AUTOPILOT_LOG_%s_%s" % (safe, field.upper())


# ---------------------------------------------------------------- dpapi backend

def _dpapi_script():
    path = os.environ.get("AUTOPILOT_LOG_DPAPI_SHELF")
    if not path:
        raise KeyStoreError(
            "AUTOPILOT_LOG_KEYSTORE=dpapi needs AUTOPILOT_LOG_DPAPI_SHELF to point at the "
            "PowerShell shelf script (see README, 'Bring your own keystore')."
        )
    return path


def _dpapi_run(args):
    cmd = ["powershell", "-NoProfile", "-File", _dpapi_script()] + args
    p = subprocess.run(cmd, capture_output=True, text=True)
    return p.returncode, p.stdout.strip(), p.stderr.strip()


# ---------------------------------------------------------------- public API

class KeyStoreError(Exception):
    pass


def get(service, field=None):
    """Return one field, or every field of ``service`` as a dict. None when absent."""
    kind = _backend()

    if kind == "env":
        if field:
            return os.environ.get(_env_key(service, field))
        prefix = _env_key(service, "")
        out = {k[len(prefix):]: v for k, v in os.environ.items() if k.startswith(prefix)}
        return out or None

    if kind == "dpapi":
        args = ["-Get", service] + (["-Field", field] if field else [])
        rc, out, _err = _dpapi_run(args)
        if rc != 0 or not out:
            return None
        return out if field else json.loads(out)

    data = _file_load().get(service)
    if data is None:
        return None
    return data.get(field) if field else data


def put(service, pairs, note=""):
    """Create or update ``service``. Existing fields that are not named are kept."""
    kind = _backend()

    if kind == "env":
        raise KeyStoreError(
            "the 'env' keystore is read-only. Set AUTOPILOT_LOG_KEYSTORE=file (or dpapi) "
            "to save the refresh token, or copy the printed variable names into your secret manager."
        )

    if kind == "dpapi":
        items = "; ".join("%s='%s'" % (k, str(v).replace("'", "''")) for k, v in pairs.items())
        rc, _out, err = _dpapi_run(["-Set", service, "-Pairs", "@{ %s }" % items, "-Note", note])
        if rc != 0:
            raise KeyStoreError("shelf write failed for %s: %s" % (service, err[:300]))
        return

    data = _file_load()
    entry = data.get(service) or {}
    entry.update({k: str(v) for k, v in pairs.items()})
    if note:
        entry["_note"] = note
    data[service] = entry
    _file_save(data)


def describe():
    """One line for --where, with no secret in it."""
    kind = _backend()
    if kind == "env":
        return "keystore=env (read-only, AUTOPILOT_LOG_<SERVICE>_<FIELD>)"
    if kind == "dpapi":
        return "keystore=dpapi shelf=%s" % _dpapi_script()
    return "keystore=file path=%s" % _file_path()


def redact(value):
    """A safe way to show that a value exists: only its last 4 characters."""
    if not value:
        return "(empty)"
    value = str(value)
    return "*" * max(0, len(value) - 4) + value[-4:]


if __name__ == "__main__":  # `python -m autopilot_log.keystore` prints the location only
    sys.stdout.write(describe() + "\n")
