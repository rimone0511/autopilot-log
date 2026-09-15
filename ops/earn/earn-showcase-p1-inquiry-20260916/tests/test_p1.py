#!/usr/bin/env python3
"""Stdlib tests for the P1 inquiry intake showcase. No network. No secrets."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from p1_inquiry.duplicates import compare_pair, find_duplicate_hits
from p1_inquiry.io_util import load_records
from p1_inquiry.pipeline import run_pipeline
from p1_inquiry.validate import validate_record


def fixture_by_id() -> dict:
    records = load_records(ROOT / "fixtures" / "inquiries.csv")
    return {row["inquiry_id"]: row for row in records}


class FailClosedTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.rows = load_records(ROOT / "fixtures" / "inquiries.csv")
        cls.by_id = {row["inquiry_id"]: row for row in cls.rows}
        cls.result = run_pipeline(cls.rows)
        cls.queue = {row["inquiry_id"]: row["queue"] for row in cls.result["records"]}
        cls.reasons = {row["inquiry_id"]: row["reasons"] for row in cls.result["records"]}

    def test_fixture_has_twenty(self) -> None:
        self.assertEqual(len(self.rows), 20)
        json_rows = load_records(ROOT / "fixtures" / "inquiries.json")
        self.assertEqual(len(json_rows), 20)
        self.assertEqual(
            [row["inquiry_id"] for row in self.rows],
            [row["inquiry_id"] for row in json_rows],
        )

    def test_expected_queues(self) -> None:
        expected = json.loads((ROOT / "fixtures" / "expected" / "queues.json").read_text(encoding="utf-8"))
        actual_ready = [row["inquiry_id"] for row in self.result["ready_for_review"]]
        actual_hold = [row["inquiry_id"] for row in self.result["needs_human"]]
        self.assertEqual(actual_ready, expected["ready_for_review_ids"])
        self.assertEqual(actual_hold, expected["needs_human_ids"])
        self.assertEqual(self.result["summary"]["sent"], 0)
        self.assertEqual(self.result["summary"]["published"], 0)
        self.assertEqual(self.result["summary"]["secrets_used"], 0)

    def test_json_and_csv_same_queues(self) -> None:
        csv_result = self.result
        json_result = run_pipeline(load_records(ROOT / "fixtures" / "inquiries.json"))
        self.assertEqual(
            [row["inquiry_id"] for row in csv_result["ready_for_review"]],
            [row["inquiry_id"] for row in json_result["ready_for_review"]],
        )
        self.assertEqual(
            [row["reasons"] for row in csv_result["records"]],
            [row["reasons"] for row in json_result["records"]],
        )

    def test_ambiguous_goes_to_human(self) -> None:
        self.assertIn("AMBIGUOUS_SIMILARITY", self.reasons["INQ-S0-015"])
        self.assertIn("AMBIGUOUS_IDENTITY", self.reasons["INQ-S0-018"])
        self.assertEqual(self.queue["INQ-S0-015"], "needs_human")
        self.assertEqual(self.queue["INQ-S0-018"], "needs_human")

    def test_exact_duplicates(self) -> None:
        self.assertIn("EXACT_EMAIL_DUPLICATE", self.reasons["INQ-S0-003"])
        self.assertIn("EXACT_PHONE_DUPLICATE", self.reasons["INQ-S0-005"])
        self.assertIn("EXACT_EMAIL_DUPLICATE", self.reasons["INQ-S0-020"])

    def test_validation_reasons(self) -> None:
        self.assertIn("MISSING_CONTACT", self.reasons["INQ-S0-006"])
        self.assertIn("INVALID_EMAIL", self.reasons["INQ-S0-007"])
        self.assertIn("MISSING_BODY", self.reasons["INQ-S0-008"])
        self.assertIn("FUTURE_RECEIVED_AT", self.reasons["INQ-S0-009"])
        self.assertIn("RISK_KEYWORD", self.reasons["INQ-S0-010"])
        self.assertTrue(
            "BODY_TOO_SHORT" in self.reasons["INQ-S0-011"]
            or "UNCLEAR_INTENT" in self.reasons["INQ-S0-011"]
        )
        self.assertIn("RISK_KEYWORD", self.reasons["INQ-S0-012"])
        self.assertIn("UNKNOWN_CHANNEL", self.reasons["INQ-S0-013"])
        self.assertIn("MISSING_NAME", self.reasons["INQ-S0-014"])

    def test_empty_input_is_fail_closed(self) -> None:
        result = run_pipeline([])
        self.assertEqual(result["ready_for_review"], [])
        self.assertEqual(result["needs_human"], [])
        self.assertEqual(result["summary"]["sent"], 0)

    def test_broken_record_never_ready(self) -> None:
        broken = {
            "inquiry_id": "X",
            "received_at": "not-a-date",
            "channel": "carrier-pigeon",
            "name": "",
            "email": "bad",
            "phone": "1",
            "company": "",
            "subject": "",
            "body": "",
        }
        reasons = validate_record(broken)
        self.assertTrue(reasons)
        result = run_pipeline([broken])
        self.assertEqual(result["ready_for_review"], [])
        self.assertEqual(result["needs_human"][0]["queue"], "needs_human")

    def test_no_send_flags(self) -> None:
        for row in self.result["records"]:
            self.assertFalse(row["sent"])
            self.assertFalse(row["published"])
        for draft in self.result["reply_drafts"]:
            self.assertEqual(draft["send_status"], "not_sent")
            self.assertFalse(draft["auto_send"])
            self.assertTrue(draft["synthetic"])
            self.assertIn("SAMPLE", draft["label"])

    def test_drafts_only_for_ready(self) -> None:
        ready_ids = {row["inquiry_id"] for row in self.result["ready_for_review"]}
        draft_ids = {row["inquiry_id"] for row in self.result["reply_drafts"]}
        self.assertEqual(ready_ids, draft_ids)

    def test_pair_helpers(self) -> None:
        hits = find_duplicate_hits(self.by_id["INQ-S0-003"], [self.by_id["INQ-S0-001"]])
        self.assertTrue(hits)
        reasons = compare_pair(self.by_id["INQ-S0-018"], self.by_id["INQ-S0-017"])
        self.assertIn("AMBIGUOUS_IDENTITY", reasons)

    def test_no_secret_markers_in_fixtures(self) -> None:
        text = (ROOT / "fixtures" / "inquiries.csv").read_text(encoding="utf-8").lower()
        for banned in ("api_key", "bearer ", "sk-", "aws_secret", "password="):
            self.assertNotIn(banned, text)

    def test_n8n_export_has_no_credentials(self) -> None:
        workflow = json.loads((ROOT / "n8n" / "inquiry_intake_p1.json").read_text(encoding="utf-8"))
        self.assertFalse(workflow.get("active"))
        for node in workflow["nodes"]:
            self.assertNotIn("credentials", node)
            self.assertNotIn("httpRequest", node.get("type", ""))


if __name__ == "__main__":
    unittest.main()
