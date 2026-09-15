#!/usr/bin/env python3
"""Stdlib tests for the P1 inquiry intake showcase. No network. No secrets."""

from __future__ import annotations

import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from p1_inquiry.duplicates import compare_pair, duplicate_inquiry_ids, find_duplicate_hits
from p1_inquiry.io_util import REQUIRED_COLUMNS, load_records, write_csv, write_json
from p1_inquiry.pipeline import SHOWCASE_GENERATED_AT, run_pipeline
from p1_inquiry.validate import validate_record
from run import GENERATED_OUTPUT_FILES, main as run_main


def fixture_by_id() -> dict:
    records = load_records(ROOT / "fixtures" / "inquiries.csv")
    return {row["inquiry_id"]: row for row in records}


def valid_row(**overrides: str) -> dict[str, str]:
    row = {
        "inquiry_id": "INQ-OK-001",
        "received_at": "2026-09-10T09:15:00+09:00",
        "channel": "form",
        "name": "山田サンプル",
        "email": "yamada.sample@example.com",
        "phone": "0300001001",
        "company": "株式会社サンプル南",
        "subject": "料金の見積もり希望",
        "body": "ホームページのミニ導入について料金の見積もりが欲しいです。対象は問い合わせ整理の範囲です。",
    }
    row.update(overrides)
    return row


def write_temp_input(rows: list[dict], suffix: str) -> Path:
    tmp = Path(tempfile.mkdtemp(prefix="p1-dup-"))
    if suffix == ".csv":
        path = tmp / "dup.csv"
        write_csv(path, rows, list(REQUIRED_COLUMNS))
    elif suffix == ".json":
        path = tmp / "dup.json"
        write_json(path, rows)
    else:
        raise ValueError(suffix)
    return path


def assert_duplicate_id_hold(test: unittest.TestCase, result: dict, inquiry_id: str) -> None:
    held = [row for row in result["needs_human"] if row["inquiry_id"] == inquiry_id]
    ready = [row for row in result["ready_for_review"] if row["inquiry_id"] == inquiry_id]
    test.assertEqual(len(held), 2)
    test.assertEqual(ready, [])
    for row in held:
        test.assertEqual(row["queue"], "needs_human")
        test.assertIn("DUPLICATE_INQUIRY_ID", row["reasons"])


class FailClosedTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.rows = load_records(ROOT / "fixtures" / "inquiries.csv")
        cls.by_id = {row["inquiry_id"]: row for row in cls.rows}
        cls.result = run_pipeline(cls.rows, showcase_fixture=True)
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
        self.assertTrue(self.result["summary"]["synthetic"])
        self.assertEqual(self.result["summary"]["generated_at_utc"], "2026-09-16T12:00:00+00:00")

    def test_json_and_csv_same_queues(self) -> None:
        csv_result = self.result
        json_result = run_pipeline(
            load_records(ROOT / "fixtures" / "inquiries.json"),
            showcase_fixture=True,
        )
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
        js = (ROOT / "n8n" / "process.js").read_text(encoding="utf-8")
        self.assertIn("DUPLICATE_INQUIRY_ID", js)
        validate_node = next(node for node in workflow["nodes"] if node["name"] == "Validate and hold")
        self.assertIn("DUPLICATE_INQUIRY_ID", validate_node["parameters"]["jsCode"])


class DuplicateInquiryIdTests(unittest.TestCase):
    def test_counts_nonempty_ids_across_batch(self) -> None:
        rows = [
            valid_row(inquiry_id="DUP-ID", email="one@example.com"),
            valid_row(
                inquiry_id="DUP-ID",
                email="two@example.com",
                phone="0300002002",
                subject="納品日の確認",
                body="納品予定日を教えてください。注文番号は SAMPLE-DUP です。",
            ),
            valid_row(inquiry_id="UNIQUE-ID", email="three@example.com", phone="0300003003"),
        ]
        self.assertEqual(duplicate_inquiry_ids(rows), {"DUP-ID"})

    def test_empty_ids_are_missing_not_duplicate(self) -> None:
        rows = [valid_row(inquiry_id=""), valid_row(inquiry_id="", email="other@example.com")]
        self.assertEqual(duplicate_inquiry_ids(rows), set())
        result = run_pipeline(rows)
        for row in result["records"]:
            self.assertIn("MISSING_INQUIRY_ID", row["reasons"])
            self.assertNotIn("DUPLICATE_INQUIRY_ID", row["reasons"])

    def test_duplicate_inquiry_id_csv_path(self) -> None:
        rows = [
            valid_row(
                inquiry_id="DUP-ID",
                email="alpha.dup@example.com",
                phone="0300001111",
                subject="料金の見積もり希望",
                body="ホームページのミニ導入について料金の見積もりが欲しいです。対象は問い合わせ整理の範囲です。",
            ),
            valid_row(
                inquiry_id="DUP-ID",
                name="佐藤デモ",
                email="beta.dup@example.com",
                phone="0300002222",
                company="デモ商事",
                subject="納品日の確認",
                body="納品予定日を教えてください。注文番号は SAMPLE-002 です。別件の本文です。",
            ),
        ]
        path = write_temp_input(rows, ".csv")
        loaded = load_records(path)
        self.assertEqual([row["inquiry_id"] for row in loaded], ["DUP-ID", "DUP-ID"])
        result = run_pipeline(loaded)
        assert_duplicate_id_hold(self, result, "DUP-ID")

    def test_duplicate_inquiry_id_json_path(self) -> None:
        rows = [
            valid_row(
                inquiry_id="DUP-ID",
                email="alpha.dup@example.com",
                phone="0300001111",
                subject="料金の見積もり希望",
                body="ホームページのミニ導入について料金の見積もりが欲しいです。対象は問い合わせ整理の範囲です。",
            ),
            valid_row(
                inquiry_id="DUP-ID",
                name="佐藤デモ",
                email="beta.dup@example.com",
                phone="0300002222",
                company="デモ商事",
                subject="納品日の確認",
                body="納品予定日を教えてください。注文番号は SAMPLE-002 です。別件の本文です。",
            ),
        ]
        path = write_temp_input(rows, ".json")
        loaded = load_records(path)
        self.assertEqual([row["inquiry_id"] for row in loaded], ["DUP-ID", "DUP-ID"])
        result = run_pipeline(loaded)
        assert_duplicate_id_hold(self, result, "DUP-ID")


class CheckAndProvenanceTests(unittest.TestCase):
    def test_check_compares_committed_outputs_without_dirtying(self) -> None:
        output_dir = ROOT / "output"
        before = {name: (output_dir / name).read_bytes() for name in GENERATED_OUTPUT_FILES}
        stdout = io.StringIO()
        stderr = io.StringIO()
        with redirect_stdout(stdout), redirect_stderr(stderr):
            rc = run_main(["--check"])
        self.assertEqual(rc, 0, msg=stderr.getvalue())
        self.assertIn("CHECK OK", stdout.getvalue())
        after = {name: (output_dir / name).read_bytes() for name in GENERATED_OUTPUT_FILES}
        self.assertEqual(before, after)

    def test_check_json_fixture_is_allowed(self) -> None:
        stdout = io.StringIO()
        stderr = io.StringIO()
        with redirect_stdout(stdout), redirect_stderr(stderr):
            rc = run_main(["--check", "--input", str(ROOT / "fixtures" / "inquiries.json")])
        self.assertEqual(rc, 0, msg=stderr.getvalue())

    def test_check_rejects_non_showcase_input(self) -> None:
        path = write_temp_input([valid_row()], ".csv")
        stdout = io.StringIO()
        stderr = io.StringIO()
        with redirect_stdout(stdout), redirect_stderr(stderr):
            rc = run_main(["--check", "--input", str(path)])
        self.assertEqual(rc, 1)
        self.assertIn("bundled showcase fixtures", stderr.getvalue())

    def test_non_showcase_input_does_not_claim_secrets(self) -> None:
        result = run_pipeline([valid_row()], showcase_fixture=False)
        self.assertFalse(result["summary"]["synthetic"])
        self.assertIsNone(result["summary"]["secrets_used"])
        self.assertEqual(result["summary"]["dataset"], "external-input-not-asserted")
        self.assertFalse(result["records"][0]["synthetic"])
        self.assertIn("not asserted", result["summary"]["disclaimer"])

    def test_generated_at_cli_override(self) -> None:
        out = Path(tempfile.mkdtemp(prefix="p1-out-"))
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            rc = run_main(
                [
                    "--input",
                    str(ROOT / "fixtures" / "inquiries.csv"),
                    "--out",
                    str(out),
                    "--generated-at",
                    "2020-01-02T03:04:05+00:00",
                ]
            )
        self.assertEqual(rc, 0)
        summary = json.loads((out / "summary.json").read_text(encoding="utf-8"))
        self.assertEqual(summary["generated_at_utc"], "2020-01-02T03:04:05+00:00")
        self.assertTrue(summary["synthetic"])
        self.assertEqual(summary["secrets_used"], 0)
        self.assertEqual(SHOWCASE_GENERATED_AT.isoformat(), "2026-09-16T12:00:00+00:00")


if __name__ == "__main__":
    unittest.main()
