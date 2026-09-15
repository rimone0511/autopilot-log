"""CSV/JSON loaders. Local files only."""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

REQUIRED_COLUMNS = (
    "inquiry_id",
    "received_at",
    "channel",
    "name",
    "email",
    "phone",
    "company",
    "subject",
    "body",
)


def load_records(path: Path) -> list[dict[str, Any]]:
    suffix = path.suffix.lower()
    if suffix == ".csv":
        return load_csv(path)
    if suffix == ".json":
        return load_json(path)
    raise ValueError(f"unsupported input type: {suffix or path.name}")


def load_csv(path: Path) -> list[dict[str, Any]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            return []
        missing = [col for col in REQUIRED_COLUMNS if col not in reader.fieldnames]
        if missing:
            raise ValueError(f"CSV missing columns: {', '.join(missing)}")
        return [_clean_row(row) for row in reader]


def load_json(path: Path) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, dict) and "inquiries" in payload:
        rows = payload["inquiries"]
    else:
        rows = payload
    if not isinstance(rows, list):
        raise ValueError("JSON must be a list or an object with inquiries[]")
    return [_clean_row(row) for row in rows]


def _clean_row(row: dict[str, Any]) -> dict[str, Any]:
    return {key: ("" if row.get(key) is None else str(row.get(key)).strip()) for key in REQUIRED_COLUMNS}


def write_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key, "") for key in fieldnames})
