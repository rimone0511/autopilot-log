#!/usr/bin/env python3
"""P3 fail-stop showcase: duplicate / invalid writes stop; timeout is not approve."""

from __future__ import annotations

import json
import os
import re
import sys
import tempfile
import unittest

PACK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(PACK, "runner"))

import failstop  # noqa: E402

SECRET_RE = re.compile(
    r"sk-[A-Za-z0-9]{20,}|xoxb-[0-9A-Za-z-]+|xoxp-[0-9A-Za-z-]+|"
    r"AIza[0-9A-Za-z_-]{20,}|BEGIN [A-Z ]*PRIVATE|aws_secret_access_key|"
    r"ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}",
    re.I,
)


def pack_file(*parts):
    return os.path.join(PACK, *parts)


def load_expected():
    with open(pack_file("fixtures", "expected-summary.json"), encoding="utf-8") as fh:
        return json.load(fh)


def seed_ledger():
    return failstop.load_json(pack_file("fixtures", "ledger-seed.json"))


def showcase_result():
    return failstop.run(
        pack_file("fixtures", "ledger-seed.json"),
        pack_file("fixtures", "events.jsonl"),
        out_dir=None,
    )


class ShowcaseLogTest(unittest.TestCase):
    def setUp(self):
        self.expected = load_expected()
        self.result = showcase_result()

    def test_after_ledger_ids(self):
        ids = [row["record_id"] for row in self.result["ledger"]["records"]]
        self.assertEqual(ids, self.expected["ledger_record_ids_after"])

    def test_written_event_ids(self):
        self.assertEqual(
            self.result["summary"]["written_event_ids"],
            self.expected["written_event_ids"],
        )

    def test_needs_human_catalog(self):
        got = {item["event_id"]: item["reason"] for item in self.result["needs_human"]}
        self.assertEqual(got, self.expected["needs_human"])
        for item in self.result["needs_human"]:
            self.assertFalse(item["written"])
            self.assertEqual(item["status"], "needs_human")
            self.assertTrue(item["message_ja"])

    def test_timeout_does_not_write_client_d(self):
        ids = [row["record_id"] for row in self.result["ledger"]["records"]]
        self.assertNotIn("cust-1004", ids)
        timeout = next(
            item for item in self.result["needs_human"] if item["event_id"] == "evt-07"
        )
        self.assertEqual(timeout["reason"], "timeout_not_approve")
        self.assertFalse(self.result["meta"]["timeout_is_approve"])
        self.assertFalse(self.result["summary"]["timeout_wrote"])

    def test_reject_does_not_write_client_f(self):
        ids = [row["record_id"] for row in self.result["ledger"]["records"]]
        self.assertNotIn("cust-1006", ids)

    def test_invalid_never_enters_ledger(self):
        ids = [row["record_id"] for row in self.result["ledger"]["records"]]
        for rid in self.expected["not_written_record_ids"]:
            self.assertNotIn(rid, ids)

    def test_approve_writes_client_e_only_after_decision(self):
        ids = [row["record_id"] for row in self.result["ledger"]["records"]]
        self.assertIn("cust-1005", ids)
        row = next(r for r in self.result["ledger"]["records"] if r["record_id"] == "cust-1005")
        self.assertEqual(row["source_event_id"], "evt-09")
        self.assertEqual(row["approved_from_event_id"], "evt-08")

    def test_no_open_holds_after_showcase_log(self):
        self.assertEqual(self.result["holds_open"], [])

    def test_seed_count_was_two(self):
        self.assertEqual(
            [row["record_id"] for row in seed_ledger()["records"]],
            self.expected["ledger_record_ids_before"],
        )


class GuardUnitTest(unittest.TestCase):
    def fresh(self):
        return failstop.Guard(seed_ledger())

    def write(self, event_id, record_id, email, key=None, hold=False, name=None):
        return {
            "event_id": event_id,
            "occurred_at": "2026-09-16T01:00:00Z",
            "event_type": "write_attempt",
            "hold_for_human": hold,
            "idempotency_key": key or ("reg:studio-a:" + record_id),
            "record": {
                "record_id": record_id,
                "kind": "customer",
                "display_name": name or record_id,
                "email": email,
                "source": "test",
            },
        }

    def decide(self, event_id, target, decision):
        return {
            "event_id": event_id,
            "occurred_at": "2026-09-16T01:01:00Z",
            "event_type": "human_decision",
            "target_event_id": target,
            "decision": decision,
            "actor": "example-operator",
        }

    def test_idempotency_conflict(self):
        guard = self.fresh()
        event = self.write(
            "u-01",
            "cust-1001",
            "other-a@example.invalid",
            key="reg:studio-a:cust-1001",
            name="別人",
        )
        outcome = guard.process_event(event)
        self.assertEqual(outcome["reason"], "idempotency_conflict")
        self.assertFalse(outcome["written"])

    def test_empty_decision_is_not_approve(self):
        guard = self.fresh()
        guard.process_event(
            self.write("u-02", "cust-2001", "hold@example.invalid", hold=True)
        )
        outcome = guard.process_event(self.decide("u-03", "u-02", ""))
        self.assertEqual(outcome["reason"], "decision_missing")
        ids = [row["record_id"] for row in guard.ledger["records"]]
        self.assertNotIn("cust-2001", ids)

    def test_missing_decision_key_is_not_approve(self):
        guard = self.fresh()
        guard.process_event(
            self.write("u-04", "cust-2002", "hold2@example.invalid", hold=True)
        )
        outcome = guard.process_event(
            {
                "event_id": "u-05",
                "occurred_at": "2026-09-16T01:01:00Z",
                "event_type": "human_decision",
                "target_event_id": "u-04",
                "actor": "example-operator",
            }
        )
        self.assertEqual(outcome["reason"], "decision_missing")

    def test_unknown_decision_is_not_approve(self):
        guard = self.fresh()
        guard.process_event(
            self.write("u-06", "cust-2003", "hold3@example.invalid", hold=True)
        )
        outcome = guard.process_event(self.decide("u-07", "u-06", "maybe-later"))
        self.assertEqual(outcome["reason"], "unknown_decision")
        ids = [row["record_id"] for row in guard.ledger["records"]]
        self.assertNotIn("cust-2003", ids)

    def test_unknown_hold_target(self):
        guard = self.fresh()
        outcome = guard.process_event(self.decide("u-08", "does-not-exist", "approve"))
        self.assertEqual(outcome["reason"], "unknown_hold_target")

    def test_malformed_email_stops(self):
        guard = self.fresh()
        outcome = guard.process_event(
            self.write("u-09", "cust-2004", "not-an-email")
        )
        self.assertEqual(outcome["reason"], "invalid_payload")
        self.assertIn("email-malformed", outcome["validation_errors"])

    def test_unknown_event_type_stops(self):
        guard = self.fresh()
        outcome = guard.process_event(
            {
                "event_id": "u-10",
                "occurred_at": "2026-09-16T01:00:00Z",
                "event_type": "send_email_now",
            }
        )
        self.assertEqual(outcome["reason"], "unknown_event_type")

    def test_approve_rechecks_duplicate(self):
        guard = self.fresh()
        first = self.write("u-11", "cust-2005", "race@example.invalid", hold=True)
        race = self.write(
            "u-12",
            "cust-2005",
            "race@example.invalid",
            key="reg:studio-a:cust-2005-race",
        )
        guard.process_event(first)
        written = guard.process_event(race)
        self.assertEqual(written["status"], "written")
        outcome = guard.process_event(self.decide("u-13", "u-11", "approve"))
        self.assertEqual(outcome["status"], "needs_human")
        self.assertEqual(outcome["reason"], "duplicate_registration")
        ids = [row["record_id"] for row in guard.ledger["records"]]
        self.assertEqual(ids.count("cust-2005"), 1)

    def test_actorless_approve_does_not_write(self):
        guard = self.fresh()
        guard.process_event(
            self.write("u-a1", "cust-3101", "hold-a@example.invalid", hold=True)
        )
        outcome = guard.process_event(
            {
                "event_id": "u-a2",
                "occurred_at": "2026-09-16T01:01:00Z",
                "event_type": "human_decision",
                "target_event_id": "u-a1",
                "decision": "approve",
            }
        )
        self.assertEqual(outcome["status"], "needs_human")
        self.assertEqual(outcome["reason"], "missing_actor")
        self.assertFalse(outcome["written"])
        ids = [row["record_id"] for row in guard.ledger["records"]]
        self.assertNotIn("cust-3101", ids)

        guard2 = self.fresh()
        guard2.process_event(
            self.write("u-a3", "cust-3102", "hold-b@example.invalid", hold=True)
        )
        blank = self.decide("u-a4", "u-a3", "approve")
        blank["actor"] = "   "
        outcome2 = guard2.process_event(blank)
        self.assertEqual(outcome2["reason"], "missing_actor")
        self.assertFalse(outcome2["written"])
        ids2 = [row["record_id"] for row in guard2.ledger["records"]]
        self.assertNotIn("cust-3102", ids2)

    def test_missing_event_id_does_not_write(self):
        guard = self.fresh()
        event = self.write("will-drop", "cust-3201", "noid@example.invalid")
        del event["event_id"]
        outcome = guard.process_event(event)
        self.assertEqual(outcome["reason"], "missing_event_id")
        self.assertFalse(outcome["written"])
        self.assertNotEqual(outcome["status"], "written")
        ids = [row["record_id"] for row in guard.ledger["records"]]
        self.assertNotIn("cust-3201", ids)
        self.assertTrue(all(row.get("source_event_id") for row in guard.ledger["records"]))

        empty = self.write("   ", "cust-3201b", "empty-id@example.invalid")
        outcome_empty = guard.process_event(empty)
        self.assertEqual(outcome_empty["reason"], "missing_event_id")
        self.assertFalse(outcome_empty["written"])
        self.assertNotIn(
            "cust-3201b", [row["record_id"] for row in guard.ledger["records"]]
        )

    def test_missing_occurred_at_does_not_write(self):
        guard = self.fresh()
        event = self.write("u-t1", "cust-3202", "notime@example.invalid")
        del event["occurred_at"]
        outcome = guard.process_event(event)
        self.assertEqual(outcome["reason"], "missing_occurred_at")
        self.assertFalse(outcome["written"])
        self.assertNotIn(
            "cust-3202", [row["record_id"] for row in guard.ledger["records"]]
        )
        for row in guard.ledger["records"]:
            if row.get("source_event_id") == "u-t1":
                self.fail("missing occurred_at must not produce a ledger row")

        naive = self.write("u-t2", "cust-3203", "naive@example.invalid")
        naive["occurred_at"] = "2026-09-16T01:00:00"
        outcome_naive = guard.process_event(naive)
        self.assertEqual(outcome_naive["reason"], "invalid_occurred_at")
        self.assertFalse(outcome_naive["written"])
        self.assertNotIn(
            "cust-3203", [row["record_id"] for row in guard.ledger["records"]]
        )

    def test_duplicate_event_id_does_not_write(self):
        guard = self.fresh()
        first = self.write(
            "dup-id",
            "cust-3301",
            "one@example.invalid",
            key="reg:studio-a:cust-3301",
        )
        second = self.write(
            "dup-id",
            "cust-3302",
            "two@example.invalid",
            key="reg:studio-a:cust-3302",
        )
        outcome_first = guard.process_event(first)
        self.assertEqual(outcome_first["status"], "written")
        outcome_second = guard.process_event(second)
        self.assertEqual(outcome_second["status"], "needs_human")
        self.assertEqual(outcome_second["reason"], "duplicate_event_id")
        self.assertFalse(outcome_second["written"])
        ids = [row["record_id"] for row in guard.ledger["records"]]
        self.assertIn("cust-3301", ids)
        self.assertNotIn("cust-3302", ids)
        source_ids = [row["source_event_id"] for row in guard.ledger["records"]]
        self.assertEqual(source_ids.count("dup-id"), 1)


class CliAndPackTest(unittest.TestCase):
    def test_cli_writes_after_files(self):
        tmp = tempfile.mkdtemp(prefix="p3-failstop-")
        code = failstop.main(
            [
                "--ledger",
                pack_file("fixtures", "ledger-seed.json"),
                "--events",
                pack_file("fixtures", "events.jsonl"),
                "--out-dir",
                tmp,
            ]
        )
        self.assertEqual(code, 0)
        after = failstop.load_json(os.path.join(tmp, "after-ledger.json"))
        self.assertEqual(len(after["records"]), 4)

    def test_n8n_stub_is_inactive_and_has_no_creds(self):
        path = pack_file("n8n", "p3-failstop-double-reg.workflow.json")
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
        self.assertFalse(data.get("active"))
        blob = json.dumps(data)
        self.assertNotRegex(blob, SECRET_RE)
        self.assertNotIn("credentials", blob)
        types = {node.get("type") for node in data.get("nodes", [])}
        self.assertIn("n8n-nodes-base.manualTrigger", types)
        self.assertNotIn("n8n-nodes-base.webhook", types)
        self.assertTrue(
            types.isdisjoint(
                {
                    "n8n-nodes-base.emailSend",
                    "n8n-nodes-base.gmail",
                    "n8n-nodes-base.slack",
                }
            )
        )
        for marker in (
            "missing_actor",
            "missing_event_id",
            "missing_occurred_at",
            "duplicate_event_id",
        ):
            self.assertIn(marker, blob)

    def test_pack_text_has_no_secrets_or_live_mail(self):
        skip_ext = {".pyc"}
        for root, _dirs, files in os.walk(PACK):
            if "__pycache__" in root:
                continue
            for name in files:
                if os.path.splitext(name)[1] in skip_ext:
                    continue
                if name == "test_failstop.py":
                    continue
                path = os.path.join(root, name)
                with open(path, encoding="utf-8") as fh:
                    text = fh.read()
                self.assertNotRegex(text, SECRET_RE, path)
                self.assertNotIn("@gmail.com", text)
                self.assertNotIn("https://hooks.slack.com", text)

    def test_committed_examples_match_runner(self):
        result = showcase_result()
        example_ledger = failstop.load_json(pack_file("examples", "after-ledger.json"))
        example_human = failstop.load_json(pack_file("examples", "after-needs-human.json"))
        self.assertEqual(
            [row["record_id"] for row in example_ledger["records"]],
            [row["record_id"] for row in result["ledger"]["records"]],
        )
        self.assertEqual(
            [item["reason"] for item in example_human],
            [item["reason"] for item in result["needs_human"]],
        )


if __name__ == "__main__":
    unittest.main()
