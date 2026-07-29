"""Offline safety tests for the TikTok Content Posting API module.

    python -m pytest tests
    python tests/test_tiktok_gate.py
"""

import argparse
import json
import os
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from autopilot_log import tiktok


def run(args, keyfile, gate):
    env = dict(os.environ)
    env["AUTOPILOT_LOG_KEYSTORE"] = "file"
    env["AUTOPILOT_LOG_KEYFILE"] = keyfile
    env["AUTOPILOT_LOG_GATE"] = gate
    return subprocess.run(
        [sys.executable, "-m", "autopilot_log.tiktok"] + args,
        cwd=ROOT,
        env=env,
        capture_output=True,
        text=True,
    )


class TikTokGateTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="autopilot-log-tiktok-test-")
        self.keyfile = os.path.join(self.temp.name, "keys.json")
        self.gate = os.path.join(self.temp.name, "posting-gate.json")
        self.video = os.path.join(self.temp.name, "clip.mp4")
        with open(self.video, "wb") as fh:
            fh.write(b"not really a video")

    def tearDown(self):
        self.temp.cleanup()

    def write_gate(self, value):
        with open(self.gate, "w", encoding="utf-8") as fh:
            if isinstance(value, str):
                fh.write(value)
            else:
                json.dump(value, fh)

    def publish(self, privacy="PUBLIC_TO_EVERYONE", extra=None):
        args = [
            "publish",
            "--shelf", "test",
            "--file", self.video,
            "--title", "Test",
            "--privacy", privacy,
            "--dry-run",
        ]
        if extra:
            args.extend(extra)
        return run(args, self.keyfile, self.gate)

    def test_missing_gate_refuses_public(self):
        result = self.publish()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("gate is CLOSED", result.stderr)

    def test_malformed_gate_refuses_public(self):
        self.write_gate("{ not json")
        self.assertNotEqual(self.publish().returncode, 0)

    def test_string_true_refuses_public(self):
        self.write_gate({"channels": {"tiktok": {"allowed": "true"}}})
        self.assertNotEqual(self.publish().returncode, 0)

    def test_number_one_refuses_public(self):
        self.write_gate({"channels": {"tiktok": {"allowed": 1}}})
        self.assertNotEqual(self.publish().returncode, 0)

    def test_boolean_true_allows_public_dry_run(self):
        self.write_gate({"channels": {"tiktok": {"allowed": True}}})
        result = self.publish()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('"privacy_level": "PUBLIC_TO_EVERYONE"', result.stdout)

    def test_self_only_is_allowed_with_closed_gate(self):
        result = self.publish("SELF_ONLY")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('"privacy_level": "SELF_ONLY"', result.stdout)

    def test_inbox_dry_run_needs_no_gate(self):
        result = run([
            "upload",
            "--shelf", "test",
            "--file", self.video,
            "--title", "Test",
            "--dry-run",
        ], self.keyfile, self.gate)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('"post_mode": "MEDIA_UPLOAD"', result.stdout)

    def test_direct_metadata_fields_are_always_present(self):
        result = self.publish("SELF_ONLY", [
            "--aigc",
            "--brand-content",
            "--brand-organic",
        ])
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('"is_aigc": true', result.stdout)
        self.assertIn('"brand_content_toggle": true', result.stdout)
        self.assertIn('"brand_organic_toggle": true', result.stdout)


class TikTokChunkTest(unittest.TestCase):
    def test_files_below_five_mb_use_one_chunk(self):
        size = tiktok.CHUNK_MIN - 1
        self.assertEqual(tiktok.chunk_plan(size), (size, 1))

    def test_five_mb_uses_one_chunk(self):
        self.assertEqual(
            tiktok.chunk_plan(tiktok.CHUNK_MIN),
            (tiktok.CHUNK_MIN, 1),
        )

    def test_sixty_four_mb_uses_one_chunk(self):
        self.assertEqual(
            tiktok.chunk_plan(tiktok.CHUNK_MAX),
            (tiktok.CHUNK_MAX, 1),
        )

    def test_over_sixty_four_mb_splits(self):
        size = tiktok.CHUNK_MAX + 1
        chunk, count = tiktok.chunk_plan(size)
        self.assertEqual(count, 2)
        self.assertGreaterEqual(chunk, tiktok.CHUNK_MIN)
        self.assertLessEqual(chunk, tiktok.CHUNK_MAX)
        self.assertLessEqual(chunk * count, size)
        self.assertGreater(chunk * (count + 1), size)


class TikTokSourceSafetyTest(unittest.TestCase):
    def test_source_has_no_browser_driving_framework_names(self):
        with open(tiktok.__file__, "r", encoding="utf-8") as fh:
            source = fh.read().lower()
        banned = (
            "sele" + "nium",
            "play" + "wright",
            "web" + "driver",
            "pup" + "peteer",
        )
        for name in banned:
            self.assertNotIn(name, source)

    def test_cli_has_no_secret_argument(self):
        original = argparse.ArgumentParser.add_argument
        option_strings = []

        def record(parser, *args, **kwargs):
            option_strings.extend(
                item for item in args
                if isinstance(item, str) and item.startswith("-")
            )
            return original(parser, *args, **kwargs)

        argparse.ArgumentParser.add_argument = record
        try:
            with self.assertRaises(SystemExit) as stopped:
                tiktok.main(["--help"])
            self.assertEqual(stopped.exception.code, 0)
        finally:
            argparse.ArgumentParser.add_argument = original

        joined = " ".join(option_strings).lower()
        self.assertNotIn("secret", joined)
        self.assertNotIn("client-key", joined)
        self.assertNotIn("refresh-token", joined)
        self.assertNotIn("access-token", joined)


if __name__ == "__main__":
    unittest.main(verbosity=2)
