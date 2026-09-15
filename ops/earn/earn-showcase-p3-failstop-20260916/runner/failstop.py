#!/usr/bin/env python3
"""P3 fail-stop / double-registration guard (synthetic showcase).

Reads a ledger + a synthetic event log. When a write would duplicate,
collide, fail validation, or lack an event envelope (actor on approve,
event ID, timezone-aware time, unique event ID), it STOPS and surfaces
needs_human. A timeout is never treated as approve.

No network. No secrets. No outbound send.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from copy import deepcopy
from datetime import datetime
from pathlib import Path

TICKET = "EARN-SHOWCASE-P3-20260916"
PACK = "earn-showcase-p3-failstop-20260916"
DEFAULT_AS_OF = "2026-09-16T12:00:00Z"

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[A-Za-z]{2,}$")
OCCURRED_AT_RE = re.compile(
    r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})$"
)
REQUIRED_RECORD_FIELDS = ("record_id", "kind", "display_name", "email")
ALLOWED_KINDS = frozenset({"customer"})
WRITE_DECISIONS = frozenset({"approve"})
STOP_DECISIONS = {
    "timeout": "timeout_not_approve",
    "reject": "rejected",
    "rejected": "rejected",
    "missing": "decision_missing",
    "": "decision_missing",
}

REASON_JA = {
    "duplicate_registration": "同じ登録キーまたは同じ顧客が台帳に既にあります。二重登録になるため書き込みを止めました。",
    "idempotency_conflict": "同じ登録キーなのに中身が違います。衝突として止めました。",
    "id_collision": "同じ顧客IDなのに中身が違います。衝突として止めました。",
    "invalid_payload": "必須項目の欠落または形式不正です。台帳には書いていません。",
    "timeout_not_approve": "待ち時間が切れました。タイムアウトは承認ではありません。台帳には書いていません。",
    "rejected": "人が却下しました。台帳には書いていません。",
    "decision_missing": "判定が空です。空の判定は承認ではありません。",
    "unknown_decision": "判定が approve / reject / timeout 以外です。承認として扱いません。",
    "unknown_hold_target": "保留中の書き込みが見つかりません。勝手には書きません。",
    "unknown_event_type": "未知のイベント種別です。書き込みしていません。",
    "missing_event_id": "イベントIDが空です。監査できないため書き込みを止めました。",
    "duplicate_event_id": "同じイベントIDが既に使われています。再利用は書き込みません。",
    "missing_occurred_at": "時刻が空です。監査できないため書き込みを止めました。",
    "invalid_occurred_at": "時刻の形式が不正か、タイムゾーンがありません。書き込みを止めました。",
    "missing_actor": "approve なのに actor が空です。人が承認した記録にならないため書き込みを止めました。",
}

REASON_EN = {
    "duplicate_registration": "This registration key or customer is already in the ledger. Write stopped to avoid a duplicate.",
    "idempotency_conflict": "Same registration key, different payload. Treated as a conflict; not written.",
    "id_collision": "Same customer id, different payload. Treated as a collision; not written.",
    "invalid_payload": "Missing or invalid required fields. Not written.",
    "timeout_not_approve": "The wait expired. Timeout is not approve. Not written.",
    "rejected": "A person rejected the write. Not written.",
    "decision_missing": "The decision is empty. An empty decision is not approve.",
    "unknown_decision": "Decision is not approve / reject / timeout. Not treated as approve.",
    "unknown_hold_target": "No matching held write. Nothing was written.",
    "unknown_event_type": "Unknown event type. Nothing was written.",
    "missing_event_id": "Event ID is empty. Not written; the row would not be auditable.",
    "duplicate_event_id": "This event ID was already used. Reuse is not written.",
    "missing_occurred_at": "Event time is empty. Not written; the row would not be auditable.",
    "invalid_occurred_at": "Event time is malformed or missing a timezone. Not written.",
    "missing_actor": "Approve without an actor. Not treated as a human approval. Not written.",
}


def require_text(value):
    if not isinstance(value, str):
        return ""
    return value.strip()


def parse_occurred_at(value):
    text = require_text(value)
    if not text or not OCCURRED_AT_RE.match(text):
        return None
    iso = text[:-1] + "+00:00" if text.endswith("Z") else text
    try:
        parsed = datetime.fromisoformat(iso)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        return None
    return parsed


def payload_hash(record):
    identity = {
        "display_name": str(record.get("display_name") or ""),
        "email": str(record.get("email") or ""),
        "kind": str(record.get("kind") or ""),
        "record_id": str(record.get("record_id") or ""),
    }
    blob = json.dumps(identity, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
    return "sha256:" + hashlib.sha256(blob.encode("utf-8")).hexdigest()


def validate_record(record, idempotency_key):
    errors = []
    if not isinstance(record, dict):
        return ["record-not-object"]
    if not str(idempotency_key or "").strip():
        errors.append("idempotency_key-empty")
    for field in REQUIRED_RECORD_FIELDS:
        value = record.get(field)
        if not isinstance(value, str) or not value.strip():
            errors.append("missing-" + field)
    kind = str(record.get("kind") or "").strip()
    if kind and kind not in ALLOWED_KINDS:
        errors.append("kind-not-allowed")
    email = str(record.get("email") or "").strip()
    if email and not EMAIL_RE.match(email):
        errors.append("email-malformed")
    return errors


def _copy_record(record, extra):
    row = {
        "record_id": record["record_id"],
        "kind": record["kind"],
        "display_name": record["display_name"],
        "email": record["email"],
    }
    if record.get("source"):
        row["source"] = record["source"]
    row.update(extra)
    return row


def _needs_human(event, reason, extra=None):
    item = {
        "event_id": event.get("event_id"),
        "status": "needs_human",
        "reason": reason,
        "written": False,
        "message_ja": REASON_JA[reason],
        "message_en": REASON_EN[reason],
    }
    if extra:
        item.update(extra)
    return item


class Guard:
    def __init__(self, ledger):
        self.ledger = deepcopy(ledger)
        self.ledger.setdefault("records", [])
        self.ledger["synthetic"] = True
        self.by_key = {}
        self.by_id = {}
        for row in self.ledger["records"]:
            row = self._index_existing(row)
        self.holds = {}
        self.seen_event_ids = set()
        self.needs_human = []
        self.trace = []

    def _index_existing(self, row):
        if "payload_hash" not in row:
            row["payload_hash"] = payload_hash(row)
        key = row.get("idempotency_key")
        if key:
            self.by_key[key] = row
        rid = row.get("record_id")
        if rid:
            self.by_id[rid] = row
        return row

    def process_events(self, events):
        for event in events:
            self.process_event(event)
        return self.result()

    def process_event(self, event):
        envelope_reason = self._envelope_reason(event)
        if envelope_reason:
            outcome = self._stop(event, envelope_reason)
        else:
            event_type = str(event.get("event_type") or "")
            if event_type == "write_attempt":
                outcome = self._write_attempt(event)
            elif event_type == "human_decision":
                outcome = self._human_decision(event)
            else:
                outcome = _needs_human(event, "unknown_event_type")
                self.needs_human.append(outcome)
        self.trace.append(self._trace_row(event, outcome))
        return outcome

    def _envelope_reason(self, event):
        event_id = require_text(event.get("event_id"))
        if not event_id:
            return "missing_event_id"
        if event_id in self.seen_event_ids:
            return "duplicate_event_id"
        self.seen_event_ids.add(event_id)
        occurred_raw = event.get("occurred_at")
        if not require_text(occurred_raw):
            return "missing_occurred_at"
        if parse_occurred_at(occurred_raw) is None:
            return "invalid_occurred_at"
        return None

    def _write_attempt(self, event, from_hold=False):
        record = event.get("record") or {}
        key = str(event.get("idempotency_key") or "").strip()
        errors = validate_record(record, key)
        extra = {
            "record_id": record.get("record_id") if isinstance(record, dict) else None,
            "idempotency_key": key or None,
            "validation_errors": errors,
        }
        if errors:
            return self._stop(event, "invalid_payload", extra)

        digest = payload_hash(record)
        extra["payload_hash"] = digest

        existing_key = self.by_key.get(key)
        if existing_key:
            if existing_key.get("payload_hash") != digest:
                extra["existing_record_id"] = existing_key.get("record_id")
                return self._stop(event, "idempotency_conflict", extra)
            extra["existing_record_id"] = existing_key.get("record_id")
            return self._stop(event, "duplicate_registration", extra)

        existing_id = self.by_id.get(record["record_id"])
        if existing_id:
            extra["existing_record_id"] = existing_id.get("record_id")
            if existing_id.get("payload_hash") != digest:
                return self._stop(event, "id_collision", extra)
            extra["idempotency_key_existing"] = existing_id.get("idempotency_key")
            return self._stop(event, "duplicate_registration", extra)

        hold = bool(event.get("hold_for_human")) and not from_hold
        if hold:
            event_id = require_text(event.get("event_id"))
            hold_row = {
                "status": "held",
                "written": False,
                "event_id": event_id,
                "record_id": record["record_id"],
                "idempotency_key": key,
                "payload_hash": digest,
                "message_ja": "人の判定待ちです。この時点では台帳に書いていません。",
                "message_en": "Waiting for a human decision. Not written yet.",
            }
            self.holds[event_id] = {
                "event": deepcopy(event),
                "record": deepcopy(record),
                "idempotency_key": key,
                "payload_hash": digest,
            }
            return hold_row

        written = self._commit(event, record, key, digest)
        return {
            "status": "written",
            "written": True,
            "event_id": written["source_event_id"],
            "record_id": written["record_id"],
            "idempotency_key": key,
            "payload_hash": digest,
        }

    def _human_decision(self, event):
        target = event.get("target_event_id")
        raw = event.get("decision")
        decision = "" if raw is None else str(raw).strip().lower()
        extra = {
            "target_event_id": target,
            "decision": decision or None,
            "actor": event.get("actor"),
        }
        held = self.holds.pop(target, None) if target else None
        if held is None:
            return self._stop(event, "unknown_hold_target", extra)

        if decision in WRITE_DECISIONS:
            if not require_text(event.get("actor")):
                extra["held_event_id"] = held["event"].get("event_id")
                extra["record_id"] = held["record"].get("record_id")
                extra["idempotency_key"] = held["idempotency_key"]
                return self._stop(event, "missing_actor", extra)
            write_event = deepcopy(held["event"])
            write_event["event_id"] = require_text(event.get("event_id"))
            write_event["occurred_at"] = require_text(event.get("occurred_at"))
            write_event["hold_for_human"] = False
            write_event["approved_from_event_id"] = held["event"].get("event_id")
            outcome = self._write_attempt(write_event, from_hold=True)
            outcome["target_event_id"] = target
            outcome["decision"] = decision
            outcome["held_event_id"] = held["event"].get("event_id")
            if outcome.get("status") == "needs_human":
                return outcome
            return outcome

        if decision in STOP_DECISIONS:
            extra["held_event_id"] = held["event"].get("event_id")
            extra["record_id"] = held["record"].get("record_id")
            extra["idempotency_key"] = held["idempotency_key"]
            return self._stop(event, STOP_DECISIONS[decision], extra)

        extra["held_event_id"] = held["event"].get("event_id")
        extra["record_id"] = held["record"].get("record_id")
        return self._stop(event, "unknown_decision", extra)

    def _stop(self, event, reason, extra=None):
        item = _needs_human(event, reason, extra)
        self.needs_human.append(item)
        return item

    def _commit(self, event, record, key, digest):
        event_id = require_text(event.get("event_id"))
        occurred_at = require_text(event.get("occurred_at"))
        if not event_id or parse_occurred_at(occurred_at) is None:
            raise RuntimeError(
                "fail-closed: refusing ledger write without event_id and timezone-aware occurred_at"
            )
        row = _copy_record(
            record,
            {
                "idempotency_key": key,
                "payload_hash": digest,
                "written_at": occurred_at,
                "source_event_id": event_id,
            },
        )
        if event.get("approved_from_event_id"):
            row["approved_from_event_id"] = event["approved_from_event_id"]
        self.ledger["records"].append(row)
        self.by_key[key] = row
        self.by_id[row["record_id"]] = row
        return row

    def _trace_row(self, event, outcome):
        return {
            "event_id": event.get("event_id"),
            "event_type": event.get("event_type"),
            "occurred_at": event.get("occurred_at"),
            "status": outcome.get("status"),
            "reason": outcome.get("reason"),
            "written": bool(outcome.get("written")),
            "record_id": outcome.get("record_id"),
            "decision": outcome.get("decision"),
            "target_event_id": outcome.get("target_event_id") or event.get("target_event_id"),
        }

    def result(self, as_of=DEFAULT_AS_OF):
        self.ledger["as_of"] = as_of
        self.ledger["ticket"] = TICKET
        self.ledger["note_ja"] = "合成台帳の after。書けた行だけ。顧客実績ではない。"
        self.ledger["note_en"] = "Synthetic ledger after a guarded run. Written rows only. Not a client case."
        open_holds = []
        for event_id, held in self.holds.items():
            open_holds.append(
                {
                    "event_id": event_id,
                    "record_id": held["record"].get("record_id"),
                    "idempotency_key": held["idempotency_key"],
                    "status": "held",
                    "written": False,
                }
            )
        written_ids = [
            row["event_id"] for row in self.trace if row.get("status") == "written"
        ]
        return {
            "meta": {
                "ticket": TICKET,
                "pack": PACK,
                "synthetic": True,
                "as_of": as_of,
                "note_ja": "合成イベントログの見本。顧客実績・時短・売上・精度の証拠ではない。",
                "note_en": "Synthetic event-log sample. Not evidence of clients, time saved, revenue, or accuracy.",
                "timeout_is_approve": False,
            },
            "ledger": self.ledger,
            "holds_open": open_holds,
            "needs_human": self.needs_human,
            "trace": self.trace,
            "summary": {
                "ledger_count_after": len(self.ledger["records"]),
                "written_event_ids": written_ids,
                "needs_human_count": len(self.needs_human),
                "open_hold_count": len(open_holds),
                "timeout_wrote": False,
            },
        }


def load_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def load_jsonl(path):
    events = []
    with open(path, encoding="utf-8") as fh:
        for line_no, raw in enumerate(fh, 1):
            line = raw.strip()
            if not line:
                continue
            try:
                events.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise SystemExit("invalid JSONL at %s:%s: %s" % (path, line_no, exc))
    return events


def dump_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
        fh.write("\n")


def run(ledger_path, events_path, out_dir=None, as_of=DEFAULT_AS_OF):
    ledger = load_json(ledger_path)
    events = load_jsonl(events_path)
    result = Guard(ledger).process_events(events)
    result["meta"]["as_of"] = as_of
    result["ledger"]["as_of"] = as_of
    if out_dir is not None:
        out = Path(out_dir)
        dump_json(out / "after-ledger.json", result["ledger"])
        dump_json(out / "after-needs-human.json", result["needs_human"])
        dump_json(out / "after-trace.json", result["trace"])
        dump_json(out / "after-result.json", result)
        dump_json(out / "summary.json", result["summary"])
    return result


def build_parser():
    parser = argparse.ArgumentParser(
        description="P3 fail-stop / double-registration guard (synthetic)."
    )
    parser.add_argument("--ledger", required=True, help="Path to ledger JSON")
    parser.add_argument("--events", required=True, help="Path to synthetic events JSONL")
    parser.add_argument("--out-dir", help="Write after-*.json here")
    parser.add_argument("--as-of", default=DEFAULT_AS_OF)
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    result = run(args.ledger, args.events, args.out_dir, args.as_of)
    summary = result["summary"]
    print(
        json.dumps(
            {
                "ticket": TICKET,
                "synthetic": True,
                "timeout_is_approve": False,
                "ledger_count_after": summary["ledger_count_after"],
                "written_event_ids": summary["written_event_ids"],
                "needs_human_count": summary["needs_human_count"],
                "needs_human_reasons": [
                    {"event_id": item["event_id"], "reason": item["reason"]}
                    for item in result["needs_human"]
                ],
                "open_hold_count": summary["open_hold_count"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
