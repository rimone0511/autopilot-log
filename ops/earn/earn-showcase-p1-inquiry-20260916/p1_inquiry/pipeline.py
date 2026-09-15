"""Intake pipeline: validate → duplicate check → hold queues. No send/publish."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from . import DATASET, TICKET, __version__
from .drafts import draft_for
from .duplicates import find_duplicate_hits
from .validate import AS_OF, validate_record

QUEUE_READY = "ready_for_review"
QUEUE_HOLD = "needs_human"
SEVERITY_BLOCK = "BLOCK"
SEVERITY_REVIEW = "REVIEW"


def _sort_key(record: dict) -> tuple:
    return (record.get("received_at") or "", record.get("inquiry_id") or "")


def classify_record(record: dict, prior_ok: list[dict]) -> dict[str, Any]:
    validation = validate_record(record)
    hits = find_duplicate_hits(record, prior_ok)
    dup_reasons = []
    for hit in hits:
        dup_reasons.extend(hit["reasons"])
    # unique preserve
    seen = set()
    reasons = []
    for reason in list(validation) + dup_reasons:
        if reason not in seen:
            seen.add(reason)
            reasons.append(reason)

    if reasons:
        queue = QUEUE_HOLD
        severity = SEVERITY_BLOCK
        decision = "fail_closed"
    else:
        queue = QUEUE_READY
        severity = SEVERITY_REVIEW
        reasons = ["VALID_UNIQUE"]
        decision = "human_review_required"

    return {
        "inquiry_id": record.get("inquiry_id") or "",
        "received_at": record.get("received_at") or "",
        "channel": record.get("channel") or "",
        "name": record.get("name") or "",
        "email": record.get("email") or "",
        "phone": record.get("phone") or "",
        "company": record.get("company") or "",
        "subject": record.get("subject") or "",
        "body": record.get("body") or "",
        "queue": queue,
        "severity": severity,
        "decision": decision,
        "reasons": reasons,
        "reason_text": ";".join(reasons),
        "duplicate_hits": hits,
        "duplicate_of": ",".join(hit["other_id"] for hit in hits),
        "sent": False,
        "published": False,
        "synthetic": True,
    }


def run_pipeline(records: list[dict[str, Any]]) -> dict[str, Any]:
    ordered = sorted(records, key=_sort_key)
    results: list[dict[str, Any]] = []
    accepted_for_matching: list[dict] = []

    for record in ordered:
        item = classify_record(record, accepted_for_matching)
        results.append(item)
        # Only structurally usable rows become prior identity references.
        # Invalid contact data must not create a "clean" identity, but a
        # validated unique row is remembered even after later duplicates.
        if item["queue"] == QUEUE_READY:
            accepted_for_matching.append(record)
        elif any(
            reason.startswith("EXACT_") or reason == "NEAR_DUPLICATE"
            for reason in item["reasons"]
        ):
            # Remember the first raw row of a cluster via already-accepted peers.
            pass
        else:
            # Fail-closed rows with a usable identity still participate as
            # prior records so a later copy is also held.
            if not any(
                r in item["reasons"]
                for r in ("MISSING_CONTACT", "INVALID_EMAIL", "INVALID_PHONE", "MISSING_INQUIRY_ID")
            ):
                accepted_for_matching.append(record)

    results_by_id = sorted(results, key=lambda row: row["inquiry_id"])
    ready = [row for row in results_by_id if row["queue"] == QUEUE_READY]
    hold = [row for row in results_by_id if row["queue"] == QUEUE_HOLD]
    drafts = [draft_for(row, row["reasons"]) for row in ready]

    summary = {
        "ticket": TICKET,
        "dataset": DATASET,
        "runner_version": __version__,
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "input_count": len(results),
        "ready_for_review": len(ready),
        "needs_human": len(hold),
        "sent": 0,
        "published": 0,
        "secrets_used": 0,
        "as_of_utc": AS_OF.replace(microsecond=0).isoformat(),
        "auto_applied": False,
        "disclaimer": (
            "Counts describe this synthetic fixture run only. "
            "They are not a customer KPI, time-saved rate, or sales result."
        ),
    }
    return {
        "summary": summary,
        "records": results_by_id,
        "ready_for_review": ready,
        "needs_human": hold,
        "hold_queue": results_by_id,
        "reply_drafts": drafts,
    }
