#!/usr/bin/env python3
"""P1 inquiry intake runner. Local files only. No network. No secrets."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from p1_inquiry.io_util import load_records, write_csv, write_json
from p1_inquiry.pipeline import SHOWCASE_GENERATED_AT, run_pipeline
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

GENERATED_OUTPUT_FILES = (
    "summary.json",
    "records.json",
    "reply_drafts.SAMPLE.json",
    "hold_queue.csv",
    "needs_human.csv",
    "ready_for_review.csv",
    "report.html",
    "FACTS_STAMP.txt",
)

SHOWCASE_INPUTS = frozenset(
    {
        (ROOT / "fixtures" / "inquiries.csv").resolve(),
        (ROOT / "fixtures" / "inquiries.json").resolve(),
    }
)


def parse_generated_at(value: str) -> datetime:
    raw = value.strip()
    if raw.endswith("Z"):
        raw = raw[:-1] + "+00:00"
    try:
        parsed = datetime.fromisoformat(raw)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(
            f"invalid --generated-at {value!r}; use ISO-8601"
        ) from exc
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc).replace(microsecond=0)


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
        "--generated-at",
        type=parse_generated_at,
        default=SHOWCASE_GENERATED_AT,
        help="timestamp written to summary.generated_at_utc (default: showcase clock)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help=(
            "regenerate into a temp dir and compare committed output/ files; "
            "bundled showcase fixtures only; does not rewrite output/"
        ),
    )
    return parser.parse_args(argv)


def is_showcase_input(path: Path) -> bool:
    try:
        return path.resolve() in SHOWCASE_INPUTS
    except OSError:
        return False


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


def check_committed_outputs(input_path: Path, generated_at: datetime) -> int:
    if not is_showcase_input(input_path):
        sys.stderr.write(
            "CHECK FAILED: --check accepts only bundled showcase fixtures "
            "(fixtures/inquiries.csv or fixtures/inquiries.json).\n"
        )
        sys.stderr.write(f"got: {input_path}\n")
        return 1

    records = load_records(input_path)
    result = run_pipeline(
        records,
        generated_at=generated_at,
        showcase_fixture=True,
    )
    committed_dir = ROOT / "output"
    mismatches: list[str] = []
    with TemporaryDirectory(prefix="p1-check-") as tmp:
        tmp_dir = Path(tmp)
        write_outputs(tmp_dir, result)
        for name in GENERATED_OUTPUT_FILES:
            committed = committed_dir / name
            actual = tmp_dir / name
            if not committed.is_file():
                mismatches.append(f"missing committed {name}")
                continue
            if not actual.is_file():
                mismatches.append(f"missing generated {name}")
                continue
            if committed.read_bytes() != actual.read_bytes():
                mismatches.append(name)

    if mismatches:
        sys.stderr.write(
            "CHECK FAILED: committed output/ drifted from temp regeneration\n"
        )
        sys.stderr.write("mismatched: " + ", ".join(mismatches) + "\n")
        return 1

    expected_path = ROOT / "fixtures" / "expected" / "queues.json"
    actual_queues = expected_payload(result)
    expected = json.loads(expected_path.read_text(encoding="utf-8"))
    if actual_queues != expected:
        sys.stderr.write("CHECK FAILED: output queues drifted from fixtures/expected/queues.json\n")
        sys.stderr.write(
            json.dumps({"expected": expected, "actual": actual_queues}, ensure_ascii=False, indent=2)
            + "\n"
        )
        return 1

    print("CHECK OK: committed outputs match temp regeneration; queues match fixtures/expected/queues.json")
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.check:
        return check_committed_outputs(args.input, args.generated_at)

    showcase = is_showcase_input(args.input)
    records = load_records(args.input)
    result = run_pipeline(
        records,
        generated_at=args.generated_at,
        showcase_fixture=showcase,
    )
    write_outputs(args.out, result)
    print(f"wrote {args.out}")
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
