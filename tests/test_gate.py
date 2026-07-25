"""The posting gate must fail closed.

The whole safety story of this tool rests on one claim: it cannot publish by accident.
These tests are that claim, written down so it stays true.

    python -m pytest tests           (or: python tests/test_gate.py)
"""

import json
import os
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def run(args, keyfile, gate):
    env = dict(os.environ)
    env["AUTOPILOT_LOG_KEYSTORE"] = "file"
    env["AUTOPILOT_LOG_KEYFILE"] = keyfile
    env["AUTOPILOT_LOG_GATE"] = gate
    return subprocess.run([sys.executable, "-m", "autopilot_log.youtube"] + args,
                          cwd=ROOT, env=env, capture_output=True, text=True)


class GateTest(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.mkdtemp(prefix="autopilot-log-test-")
        self.keyfile = os.path.join(self.dir, "keys.json")
        self.gate = os.path.join(self.dir, "posting-gate.json")
        self.video = os.path.join(self.dir, "clip.mp4")
        with open(self.video, "wb") as fh:
            fh.write(b"not really a video")
        r = run(["set-client", "--client-id", "fake-id", "--client-secret", "fake-secret"],
                self.keyfile, self.gate)
        self.assertEqual(r.returncode, 0, r.stderr)

    def write_gate(self, text):
        with open(self.gate, "w", encoding="utf-8") as fh:
            fh.write(text)

    def upload(self, privacy):
        return run(["upload", "--shelf", "t", "--file", self.video,
                    "--title", "T", "--privacy", privacy, "--dry-run"],
                   self.keyfile, self.gate)

    def test_private_is_allowed_without_any_gate(self):
        r = self.upload("private")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn('"privacyStatus": "private"', r.stdout)

    def test_missing_gate_refuses_public(self):
        r = self.upload("public")
        self.assertEqual(r.returncode, 1)
        self.assertIn("gate is CLOSED", r.stderr)

    def test_closed_gate_refuses_public(self):
        self.write_gate(json.dumps({"channels": {"youtube": {"allowed": False}}}))
        self.assertEqual(self.upload("public").returncode, 1)

    def test_malformed_gate_refuses_public(self):
        self.write_gate("this is not json {{{")
        r = self.upload("public")
        self.assertEqual(r.returncode, 1, "a broken gate must fail closed, not open")

    def test_truthy_but_not_true_refuses_public(self):
        # "true" the string, or 1, must not be mistaken for the boolean.
        self.write_gate(json.dumps({"channels": {"youtube": {"allowed": "true"}}}))
        self.assertEqual(self.upload("public").returncode, 1)

    def test_open_gate_allows_public(self):
        self.write_gate(json.dumps({"channels": {"youtube": {"allowed": True}}}))
        r = self.upload("public")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn('"privacyStatus": "public"', r.stdout)

    def test_scheduled_publish_needs_the_gate(self):
        r = run(["upload", "--shelf", "t", "--file", self.video, "--title", "T",
                 "--publish-at", "2026-12-31T00:00:00Z", "--dry-run"],
                self.keyfile, self.gate)
        self.assertEqual(r.returncode, 1, "scheduling is publishing, so it needs the gate too")


class KeystoreTest(unittest.TestCase):
    def test_no_secret_is_echoed_when_storing_a_client(self):
        d = tempfile.mkdtemp(prefix="autopilot-log-test-")
        keyfile = os.path.join(d, "keys.json")
        secret = "GOCSPX-super-secret-value"
        r = run(["set-client", "--client-id", "abc-id", "--client-secret", secret],
                keyfile, os.path.join(d, "gate.json"))
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertNotIn(secret, r.stdout + r.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
