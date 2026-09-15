#!/usr/bin/env python3
"""P1 inquiry intake runner. Local files only. No network. No secrets."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from p1_inquiry.io_util import load_records, write_csv, write_json
from p1_inquiry.pipeline import run_pipeline
from p1_inquiry.report import render_facts_stamp, render_html

CSV_FIELDS = [
    "inquiry_id",
    "received_at",
    "channel",
    "name",
    "email",
    "phone",
    "company",
    "subject",
    "queue",
    "severity",
    "decision",
    "reason_text",
    "duplicate_of",
    "sent",
    "published",
]


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Synthetic P1 inquiry intake. Validates, finds duplicates, writes hold lists."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=ROOT / "fixtures" / "inquiries.csv",
        help="CSV or JSON fixture",
    )
    parser.add_argument("--out", type=Path, default=ROOT / "output", help="output directory")
    parser.add_argument(
        "--check",
        action="store_true",
        help="compare queues with fixtures/expected and exit non-zero on drift",
    )
    return parser.parse_args(argv)


def write_outputs(out_dir: Path, result: dict) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    write_json(out_dir / "summary.json", result["summary"])
    write_json(out_dir / "records.json", result["records"])
    write_json(out_dir / "reply_drafts.SAMPLE.json", result["reply_drafts"])
    write_csv(out_dir / "hold_queue.csv", result["hold_queue"], CSV_FIELDS)
    write_csv(out_dir / "needs_human.csv", result["needs_human"], CSV_FIELDS)
    write_csv(out_dir / "ready_for_review.csv", result["ready_for_review"], CSV_FIELDS)
    (out_dir / "report.html").write_text(render_html(result), encoding="utf-8")
    (out_dir / "FACTS_STAMP.txt").write_text(render_facts_stamp(result), encoding="utf-8")


def expected_payload(result: dict) -> dict:
    return {
        "ready_for_review_ids": [row["inquiry_id"] for row in result["ready_for_review"]],
        "needs_human_ids": [row["inquiry_id"] for row in result["needs_human"]],
        "sent": 0,
        "published": 0,
        "secrets_used": 0,
    }


def check_expected(result: dict) -> int:
    expected_path = ROOT / "fixtures" / "expected" / "queues.json"
    actual = expected_payload(result)
    expected = json.loads(expected_path.read_text(encoding="utf-8"))
    if actual != expected:
        sys.stderr.write("CHECK FAILED: output queues drifted from fixtures/expected/queues.json\n")
        sys.stderr.write(json.dumps({"expected": expected, "actual": actual}, ensure_ascii=False, indent=2) + "\n")
        return 1
    print("CHECK OK: queues match fixtures/expected/queues.json")
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    records = load_records(args.input)
    result = run_pipeline(records)
    write_outputs(args.out, result)
    print(f"wrote {args.out}")
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))
    if args.check:
        return check_expected(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
