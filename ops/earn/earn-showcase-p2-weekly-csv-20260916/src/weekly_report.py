#!/usr/bin/env python3
"""P2 synthetic weekly ops report with row-level evidence.

Every summary line lists the source row_ids (and CSV line links) that produced it.
Invalid / out-of-week / colliding rows are excluded from totals (fail closed).

This is a local sample engine. It does not send mail, post, or call paid APIs.
Amounts are fictional stationery-shop figures, not seller revenue.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

try:
    from zoneinfo import ZoneInfo
except ImportError:  # pragma: no cover
    ZoneInfo = None  # type: ignore


PACK_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = PACK_ROOT / "fixtures" / "inbound-ops-synthetic-w37.csv"
DEFAULT_OUT = PACK_ROOT / "out"
DEFAULT_WEEK = "2026-W37"
DEFAULT_TZ_NAME = "Asia/Tokyo"
DEFAULT_GENERATED_AT = "2026-09-16T12:00:00+09:00"
DEFAULT_DATASET = "ハーバー文具（合成）"
SOURCE_REL = "fixtures/inbound-ops-synthetic-w37.csv"
TZ_ALIASES = {
    "jst": "Asia/Tokyo",
    "asia/tokyo": "Asia/Tokyo",
    "utc": "UTC",
    "gmt": "UTC",
    "z": "UTC",
}

ALLOWED_CHANNELS = ("store", "web", "phone", "wholesale")
ALLOWED_SKUS = ("NB-A5", "PEN-BK", "CLIP-20")
ALLOWED_STATUSES = ("fulfilled", "cancelled", "hold")

CHANNEL_LABEL_JA = {
    "store": "店頭",
    "web": "Web",
    "phone": "電話",
    "wholesale": "卸",
}
SKU_LABEL_JA = {
    "NB-A5": "A5ノート",
    "PEN-BK": "黒ボールペン",
    "CLIP-20": "ダブルクリップ（20個入）",
}

WEEK_RE = re.compile(r"^(\d{4})-W(\d{2})$")
SECRET_RE = re.compile(
    r"(api[_-]?key\s*[:=]|client_secret|BEGIN (RSA |OPENSSH )?PRIVATE KEY|bearer\s+[a-z0-9]|sk-[a-z0-9]{8,}|xox[baprs]-)",
    re.I,
)


def jst():
    tz, _ = resolve_timezone(DEFAULT_TZ_NAME)
    return tz


def resolve_timezone(name: str) -> Tuple[object, str]:
    """Return (tzinfo, recorded IANA name). Unknown names fail closed."""
    raw = (name or "").strip()
    if not raw:
        raise ValueError("timezone must be non-empty")
    iana = TZ_ALIASES.get(raw.lower(), raw)
    if ZoneInfo is not None:
        try:
            return ZoneInfo(iana), iana
        except Exception as exc:
            raise ValueError(f"unknown timezone: {name}") from exc
    if iana == "Asia/Tokyo":
        return timezone(timedelta(hours=9), name="JST"), "Asia/Tokyo"
    if iana == "UTC":
        return timezone.utc, "UTC"
    raise ValueError(f"unknown timezone: {name}")


def source_rel_for(input_path: Path, pack_root: Path = PACK_ROOT) -> str:
    """Leak-free source label for the file that was actually read.

    Pack-internal paths stay pack-relative (so the default fixture keeps
    `fixtures/inbound-ops-synthetic-w37.csv`). Paths outside the pack use
    the basename only — parent directories are never written into output.
    """
    resolved = input_path.expanduser().resolve()
    try:
        rel = resolved.relative_to(pack_root.resolve())
    except ValueError:
        name = resolved.name
        if not name or name in {".", ".."}:
            raise ValueError("input path has no usable filename")
        return name
    posix = rel.as_posix()
    if not posix or posix == ".":
        raise ValueError("input path has no usable filename")
    return posix


def evidence_href(source_rel: str, source_line: int) -> str:
    return f"../{source_rel}#L{source_line}"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def parse_week_bounds(week: str, tz) -> Tuple[datetime, datetime]:
    m = WEEK_RE.match(week)
    if not m:
        raise ValueError("week must look like YYYY-Www, e.g. 2026-W37")
    year, iso_week = int(m.group(1)), int(m.group(2))
    if iso_week < 1 or iso_week > 53:
        raise ValueError("iso week out of range")
    start_d = datetime.fromisocalendar(year, iso_week, 1).date()
    start = datetime(start_d.year, start_d.month, start_d.day, tzinfo=tz)
    end = start + timedelta(days=7)
    return start, end


def parse_dt(raw: str, tz) -> Optional[datetime]:
    text = (raw or "").strip()
    if not text:
        return None
    try:
        dt = datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=tz)
    return dt.astimezone(tz)


def parse_int(raw: str) -> Tuple[Optional[int], Optional[str]]:
    text = (raw or "").strip()
    if text == "":
        return None, "missing_number"
    try:
        value = int(text, 10)
    except ValueError:
        return None, "not_integer"
    return value, None


@dataclass
class SourceRow:
    source_line: int
    row_id: str
    occurred_at_raw: str
    channel: str
    sku: str
    qty_raw: str
    unit_amount_raw: str
    status: str
    note: str

    def fixture_link(self, source_rel: str) -> str:
        return evidence_href(source_rel, self.source_line)


@dataclass
class ClassifiedRow:
    source: SourceRow
    bucket: str
    reasons: Tuple[str, ...]
    occurred_at: Optional[datetime]
    qty: Optional[int]
    unit_amount_jpy: Optional[int]
    line_amount_jpy: Optional[int]

    @property
    def row_id(self) -> str:
        return self.source.row_id

    @property
    def source_line(self) -> int:
        return self.source.source_line


@dataclass
class SummaryLine:
    line_id: str
    section: str
    label: str
    predicate: str
    row_count: int
    qty: int
    synthetic_jpy: int
    row_ids: List[str]
    source_lines: List[int]

    def evidence_cell(self, source_rel: str) -> str:
        if not self.row_ids:
            return "（該当なし）"
        parts = []
        for rid, line in zip(self.row_ids, self.source_lines):
            parts.append(f"[{rid}]({evidence_href(source_rel, line)})")
        return ", ".join(parts)


@dataclass
class Report:
    week: str
    week_start: datetime
    week_end_exclusive: datetime
    timezone_name: str
    dataset_label: str
    input_path: Path
    source_rel: str
    input_sha256: str
    generated_at: str
    rows: List[ClassifiedRow]
    lines: List[SummaryLine]
    banner: str = (
        "SYNTHETIC / 合成データ。販売者の売上・顧客実績・時短・精度の証拠ではない。"
        "自主制作サンプル。"
    )


def load_csv(path: Path) -> List[SourceRow]:
    required = [
        "row_id",
        "occurred_at",
        "channel",
        "sku",
        "qty",
        "unit_amount_jpy",
        "status",
        "note",
    ]
    rows: List[SourceRow] = []
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames is None:
            raise ValueError("CSV has no header")
        missing = [c for c in required if c not in reader.fieldnames]
        if missing:
            raise ValueError("CSV missing columns: " + ", ".join(missing))
        for i, rec in enumerate(reader, start=2):
            rows.append(
                SourceRow(
                    source_line=i,
                    row_id=(rec.get("row_id") or "").strip(),
                    occurred_at_raw=(rec.get("occurred_at") or "").strip(),
                    channel=(rec.get("channel") or "").strip(),
                    sku=(rec.get("sku") or "").strip(),
                    qty_raw=(rec.get("qty") or "").strip(),
                    unit_amount_raw=(rec.get("unit_amount_jpy") or "").strip(),
                    status=(rec.get("status") or "").strip(),
                    note=(rec.get("note") or "").strip(),
                )
            )
    return rows


def classify_rows(
    sources: Sequence[SourceRow],
    week_start: datetime,
    week_end_exclusive: datetime,
    tz,
) -> List[ClassifiedRow]:
    id_counts: Dict[str, int] = {}
    for src in sources:
        if src.row_id:
            id_counts[src.row_id] = id_counts.get(src.row_id, 0) + 1

    classified: List[ClassifiedRow] = []
    for src in sources:
        reasons: List[str] = []
        if not src.row_id:
            reasons.append("missing_row_id")
        elif id_counts.get(src.row_id, 0) > 1:
            reasons.append("id_collision")

        occurred_at = parse_dt(src.occurred_at_raw, tz)
        if occurred_at is None:
            reasons.append("missing_or_bad_occurred_at")
        elif occurred_at < week_start or occurred_at >= week_end_exclusive:
            reasons.append("out_of_week")

        if src.channel not in ALLOWED_CHANNELS:
            reasons.append("unknown_channel")
        if not src.sku:
            reasons.append("missing_sku")
        elif src.sku not in ALLOWED_SKUS:
            reasons.append("unknown_sku")
        if src.status not in ALLOWED_STATUSES:
            reasons.append("unknown_status")

        qty, qty_err = parse_int(src.qty_raw)
        if qty_err:
            reasons.append("bad_qty")
        elif qty is not None and qty < 0:
            reasons.append("negative_qty")
        elif qty == 0:
            reasons.append("zero_qty")

        amount, amount_err = parse_int(src.unit_amount_raw)
        if amount_err:
            reasons.append("bad_unit_amount")
        elif amount is not None and amount < 0:
            reasons.append("negative_unit_amount")

        line_amount = None
        if qty is not None and amount is not None and qty > 0 and amount >= 0:
            line_amount = qty * amount

        if reasons:
            bucket = "exception"
        else:
            bucket = src.status

        classified.append(
            ClassifiedRow(
                source=src,
                bucket=bucket,
                reasons=tuple(reasons),
                occurred_at=occurred_at,
                qty=qty,
                unit_amount_jpy=amount,
                line_amount_jpy=line_amount,
            )
        )
    return classified


def _agg(rows: Sequence[ClassifiedRow]) -> Tuple[int, int, int, List[str], List[int]]:
    ordered = sorted(rows, key=lambda r: (r.source_line, r.row_id))
    ids = [r.row_id for r in ordered]
    lines = [r.source_line for r in ordered]
    qty = sum(r.qty or 0 for r in ordered)
    jpy = sum(r.line_amount_jpy or 0 for r in ordered)
    return len(ordered), qty, jpy, ids, lines


def build_lines(rows: Sequence[ClassifiedRow]) -> List[SummaryLine]:
    fulfilled = [r for r in rows if r.bucket == "fulfilled"]
    cancelled = [r for r in rows if r.bucket == "cancelled"]
    hold = [r for r in rows if r.bucket == "hold"]
    exceptions = [r for r in rows if r.bucket == "exception"]

    out: List[SummaryLine] = []

    def add(line_id: str, section: str, label: str, predicate: str, group: Sequence[ClassifiedRow]) -> None:
        count, qty, jpy, ids, lines = _agg(group)
        out.append(
            SummaryLine(
                line_id=line_id,
                section=section,
                label=label,
                predicate=predicate,
                row_count=count,
                qty=qty,
                synthetic_jpy=jpy,
                row_ids=ids,
                source_lines=lines,
            )
        )

    add("L01", "totals", "確定件数（fulfilled）", "bucket==fulfilled", fulfilled)
    add("L02", "totals", "確定数量合計", "bucket==fulfilled", fulfilled)
    add("L03", "totals", "確定・合成金額(円)", "bucket==fulfilled", fulfilled)

    n = 4
    for channel in ALLOWED_CHANNELS:
        group = [r for r in fulfilled if r.source.channel == channel]
        add(
            f"L{n:02d}",
            "channel",
            f"チャネル {CHANNEL_LABEL_JA[channel]}（{channel}）",
            f"bucket==fulfilled AND channel=={channel}",
            group,
        )
        n += 1
    for sku in ALLOWED_SKUS:
        group = [r for r in fulfilled if r.source.sku == sku]
        add(
            f"L{n:02d}",
            "sku",
            f"SKU {sku} / {SKU_LABEL_JA[sku]}",
            f"bucket==fulfilled AND sku=={sku}",
            group,
        )
        n += 1

    add("L11", "cancelled", "キャンセル件数（確定合計に含めない）", "bucket==cancelled", cancelled)
    add("L12", "cancelled", "キャンセル・合成金額(円)（確定合計に含めない）", "bucket==cancelled", cancelled)
    add("L13", "hold", "確認待ち件数（確定合計に含めない）", "bucket==hold", hold)
    add("L14", "hold", "確認待ち・合成金額(円)（確定合計に含めない）", "bucket==hold", hold)
    add("L15", "exception", "除外件数（失敗は成功に混ぜない）", "bucket==exception", exceptions)
    return out


def build_report(
    input_path: Path,
    week: str = DEFAULT_WEEK,
    timezone_name: str = DEFAULT_TZ_NAME,
    generated_at: str = DEFAULT_GENERATED_AT,
    dataset_label: str = DEFAULT_DATASET,
) -> Report:
    if not input_path.is_file():
        raise FileNotFoundError(f"input not found: {input_path}")
    tz, recorded_tz = resolve_timezone(timezone_name)
    week_start, week_end = parse_week_bounds(week, tz)
    sources = load_csv(input_path)
    rows = classify_rows(sources, week_start, week_end, tz)
    lines = build_lines(rows)
    return Report(
        week=week,
        week_start=week_start,
        week_end_exclusive=week_end,
        timezone_name=recorded_tz,
        dataset_label=dataset_label,
        input_path=input_path,
        source_rel=source_rel_for(input_path),
        input_sha256=sha256_file(input_path),
        generated_at=generated_at,
        rows=rows,
        lines=lines,
    )


def lineage_errors(report: Report) -> List[str]:
    """Every summary line must be a closed world over source rows."""
    errors: List[str] = []
    by_id_line: Dict[Tuple[str, int], ClassifiedRow] = {}
    for row in report.rows:
        key = (row.row_id, row.source_line)
        if key in by_id_line:
            errors.append(f"internal duplicate key {key}")
        by_id_line[key] = row

    for line in report.lines:
        if len(line.row_ids) != len(line.source_lines):
            errors.append(f"{line.line_id} row_ids/source_lines length mismatch")
        if line.row_count != len(line.row_ids):
            errors.append(f"{line.line_id} row_count {line.row_count} != {len(line.row_ids)}")
        for rid, src_line in zip(line.row_ids, line.source_lines):
            row = by_id_line.get((rid, src_line))
            if row is None:
                errors.append(f"{line.line_id} evidence ({rid}, L{src_line}) not in source")
                continue
            if not _row_matches_predicate(row, line.predicate):
                errors.append(
                    f"{line.line_id} evidence {rid} does not match {line.predicate}"
                )

        expected = [r for r in report.rows if _row_matches_predicate(r, line.predicate)]
        expected_keys = {(r.row_id, r.source_line) for r in expected}
        actual_keys = set(zip(line.row_ids, line.source_lines))
        missing = expected_keys - actual_keys
        extra = actual_keys - expected_keys
        if missing:
            errors.append(f"{line.line_id} missing source rows: {sorted(missing)}")
        if extra:
            errors.append(f"{line.line_id} extra evidence: {sorted(extra)}")

        recomputed_qty = sum((by_id_line[k].qty or 0) for k in actual_keys)
        recomputed_jpy = sum((by_id_line[k].line_amount_jpy or 0) for k in actual_keys)
        if line.qty != recomputed_qty:
            errors.append(f"{line.line_id} qty {line.qty} != evidence {recomputed_qty}")
        if line.synthetic_jpy != recomputed_jpy:
            errors.append(f"{line.line_id} jpy {line.synthetic_jpy} != evidence {recomputed_jpy}")

    fulfilled_ids = {r.row_id for r in report.rows if r.bucket == "fulfilled"}
    exception_lines = {r.source_line for r in report.rows if r.bucket == "exception"}
    l01 = next(x for x in report.lines if x.line_id == "L01")
    for rid, src_line in zip(l01.row_ids, l01.source_lines):
        if src_line in exception_lines:
            errors.append(f"L01 includes exception source line {src_line}")

    # Fail closed: colliding ids never enter fulfilled.
    from collections import Counter

    counts = Counter(r.row_id for r in report.rows if r.row_id)
    colliding = {i for i, n in counts.items() if n > 1}
    for rid in colliding:
        if rid in fulfilled_ids:
            errors.append(f"colliding id {rid} leaked into fulfilled")

    return errors


def _row_matches_predicate(row: ClassifiedRow, predicate: str) -> bool:
    if predicate == "bucket==fulfilled":
        return row.bucket == "fulfilled"
    if predicate == "bucket==cancelled":
        return row.bucket == "cancelled"
    if predicate == "bucket==hold":
        return row.bucket == "hold"
    if predicate == "bucket==exception":
        return row.bucket == "exception"
    if predicate.startswith("bucket==fulfilled AND channel=="):
        ch = predicate.split("channel==", 1)[1]
        return row.bucket == "fulfilled" and row.source.channel == ch
    if predicate.startswith("bucket==fulfilled AND sku=="):
        sku = predicate.split("sku==", 1)[1]
        return row.bucket == "fulfilled" and row.source.sku == sku
    raise ValueError("unknown predicate: " + predicate)


def lines_for_row(report: Report, row_id: str) -> List[SummaryLine]:
    return [line for line in report.lines if row_id in line.row_ids]


def render_markdown(report: Report) -> str:
    start = report.week_start.isoformat()
    end = report.week_end_exclusive.isoformat()
    lines_md = [
        f"# 週報 {report.week} — {report.dataset_label}",
        "",
        f"> {report.banner}",
        "",
        "## 対象",
        "",
        f"- 週: `{report.week}`（ISO、{report.timezone_name}）",
        f"- 期間: `{start}` 以上、`{end}` 未満（半開）",
        f"- 入力: `{report.source_rel}`",
        f"- 入力 SHA-256: `{report.input_sha256}`",
        f"- 生成時刻（固定）: `{report.generated_at}`",
        "- エンジン: `src/weekly_report.py`（n8n JSON は inactive の見本。正本はこのスクリプト）",
        "",
        "## 要約（各行が入力行へ戻れる）",
        "",
        "| 行ID | 指標 | 件数 | 数量 | 合成円 | 根拠（row_id → CSV行） |",
        "|---|---|---:|---:|---:|---|",
    ]
    for line in report.lines:
        lines_md.append(
            f"| {line.line_id} | {line.label} | {line.row_count} | {line.qty} | "
            f"{line.synthetic_jpy} | {line.evidence_cell(report.source_rel)} |"
        )
    lines_md += [
        "",
        "件数・数量・合成円は、根拠列の行だけを足した値である。根拠に無い行は足していない。",
        "",
        "## 除外明細（成功件数に混ぜない）",
        "",
        "| CSV行 | row_id | 理由 | リンク |",
        "|---:|---|---|---|",
    ]
    exceptions = [r for r in report.rows if r.bucket == "exception"]
    if not exceptions:
        lines_md.append("| — | — | 除外なし | — |")
    else:
        for row in sorted(exceptions, key=lambda r: r.source_line):
            reasons = ",".join(row.reasons)
            link = f"[L{row.source_line}]({row.source.fixture_link(report.source_rel)})"
            rid = row.row_id or "(empty)"
            lines_md.append(f"| {row.source_line} | `{rid}` | `{reasons}` | {link} |")

    lines_md += [
        "",
        "## 根拠索引（入力の全行）",
        "",
        "見出しの `row_id` から、どの要約行に使われたかを辿れる。",
        "",
    ]
    for row in report.rows:
        used = lines_for_row(report, row.row_id)
        used_s = ", ".join(x.line_id for x in used) if used else "（要約行なし）"
        occurred = row.occurred_at.isoformat() if row.occurred_at else row.source.occurred_at_raw or "(empty)"
        lines_md += [
            f"### {row.row_id or '(empty-id)'} · L{row.source_line}",
            "",
            f"- CSV: [行 {row.source_line}]({row.source.fixture_link(report.source_rel)})",
            f"- occurred_at: `{occurred}`",
            f"- channel: `{row.source.channel}` / sku: `{row.source.sku}` / status: `{row.source.status}`",
            f"- qty: `{row.source.qty_raw}` / unit_amount_jpy: `{row.source.unit_amount_raw}`",
            f"- 分類: `{row.bucket}`"
            + (f" / 理由: `{','.join(row.reasons)}`" if row.reasons else ""),
            f"- 載っている要約行: {used_s}",
            f"- note: {row.source.note}",
            "",
        ]

    lines_md += [
        "## このファイルが主張しないこと",
        "",
        "- 販売者（石田祐太 / yutalab）の実売上、実顧客、時短率、精度",
        "- n8n Partner / Expert などのバッジ",
        "- 本番シート・本番メール・公開済み運用",
        "",
        "再現手順は `README.md`。完了条件は `DOD.md`。言ってよい事実だけ `FACTS.md`。",
        "",
    ]
    return "\n".join(lines_md)


def _write_csv(path: Path, fieldnames: Sequence[str], records: Iterable[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(fieldnames), lineterminator="\n")
        writer.writeheader()
        for rec in records:
            writer.writerow(rec)


def write_outputs(report: Report, out_dir: Path) -> Dict[str, Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = f"weekly-{report.week}"
    paths = {
        "markdown": out_dir / f"{stem}.md",
        "summary": out_dir / f"{stem}-summary.csv",
        "evidence": out_dir / f"{stem}-evidence.csv",
        "exceptions": out_dir / f"{stem}-exceptions.csv",
        "run": out_dir / f"{stem}-RUN.json",
    }
    paths["markdown"].write_text(render_markdown(report), encoding="utf-8")

    _write_csv(
        paths["summary"],
        [
            "line_id",
            "section",
            "label",
            "predicate",
            "row_count",
            "qty",
            "synthetic_jpy",
            "row_ids",
            "source_lines",
            "evidence_links",
        ],
        (
            {
                "line_id": line.line_id,
                "section": line.section,
                "label": line.label,
                "predicate": line.predicate,
                "row_count": line.row_count,
                "qty": line.qty,
                "synthetic_jpy": line.synthetic_jpy,
                "row_ids": "|".join(line.row_ids),
                "source_lines": "|".join(str(n) for n in line.source_lines),
                "evidence_links": "|".join(
                    evidence_href(report.source_rel, n) for n in line.source_lines
                ),
            }
            for line in report.lines
        ),
    )

    evidence_records = []
    for line in report.lines:
        for rid, src_line in zip(line.row_ids, line.source_lines):
            evidence_records.append(
                {
                    "line_id": line.line_id,
                    "row_id": rid,
                    "source_line": src_line,
                    "evidence_link": evidence_href(report.source_rel, src_line),
                    "predicate": line.predicate,
                }
            )
    _write_csv(
        paths["evidence"],
        ["line_id", "row_id", "source_line", "evidence_link", "predicate"],
        evidence_records,
    )

    _write_csv(
        paths["exceptions"],
        [
            "source_line",
            "row_id",
            "reasons",
            "channel",
            "sku",
            "status",
            "occurred_at",
            "evidence_link",
        ],
        (
            {
                "source_line": row.source_line,
                "row_id": row.row_id,
                "reasons": "|".join(row.reasons),
                "channel": row.source.channel,
                "sku": row.source.sku,
                "status": row.source.status,
                "occurred_at": row.source.occurred_at_raw,
                "evidence_link": row.source.fixture_link(report.source_rel),
            }
            for row in report.rows
            if row.bucket == "exception"
        ),
    )

    counts = {
        "input_rows": len(report.rows),
        "fulfilled": sum(1 for r in report.rows if r.bucket == "fulfilled"),
        "cancelled": sum(1 for r in report.rows if r.bucket == "cancelled"),
        "hold": sum(1 for r in report.rows if r.bucket == "hold"),
        "exception": sum(1 for r in report.rows if r.bucket == "exception"),
    }
    run = {
        "ticket": "EARN-SHOWCASE-P2-20260916",
        "dataset_label": report.dataset_label,
        "synthetic": True,
        "seller_revenue_claim": False,
        "week": report.week,
        "week_start": report.week_start.isoformat(),
        "week_end_exclusive": report.week_end_exclusive.isoformat(),
        "timezone": report.timezone_name,
        "input": report.source_rel,
        "input_sha256": report.input_sha256,
        "generated_at": report.generated_at,
        "counts": counts,
        "lineage_error_count": len(lineage_errors(report)),
        "outputs": {k: v.name for k, v in paths.items() if k != "run"},
        "banner": report.banner,
    }
    paths["run"].write_text(json.dumps(run, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return paths


def assert_no_secrets(text: str, label: str) -> None:
    if SECRET_RE.search(text):
        raise SystemExit(f"refusing to write secret-like text in {label}")


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="P2 synthetic weekly CSV report with evidence links")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--week", default=DEFAULT_WEEK)
    parser.add_argument(
        "--timezone",
        default=DEFAULT_TZ_NAME,
        help="IANA timezone for week bounds (default Asia/Tokyo). JST is an alias.",
    )
    parser.add_argument("--generated-at", default=DEFAULT_GENERATED_AT)
    parser.add_argument("--dataset-label", default=DEFAULT_DATASET)
    parser.add_argument("--trace", metavar="ROW_ID", help="print summary lines that cite this row_id")
    parser.add_argument("--check", action="store_true", help="verify lineage and refuse on errors")
    args = parser.parse_args(argv)

    input_path = args.input if args.input.is_absolute() else (Path.cwd() / args.input)
    if not input_path.is_file():
        print(f"input not found: {input_path}", file=sys.stderr)
        return 2
    out_dir = args.out_dir if args.out_dir.is_absolute() else (Path.cwd() / args.out_dir)
    if str(args.out_dir) == str(DEFAULT_OUT) and not out_dir.exists():
        out_dir = DEFAULT_OUT

    try:
        report = build_report(
            input_path=input_path.resolve(),
            week=args.week,
            timezone_name=args.timezone,
            generated_at=args.generated_at,
            dataset_label=args.dataset_label,
        )
    except (ValueError, FileNotFoundError, OSError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    errors = lineage_errors(report)
    if args.trace:
        hits = lines_for_row(report, args.trace)
        if not hits:
            print(f"{args.trace}: not cited by any summary line", file=sys.stderr)
            return 1
        for line in hits:
            print(f"{line.line_id}\t{line.label}\tpredicate={line.predicate}")
        return 0

    if errors:
        for err in errors:
            print("lineage error:", err, file=sys.stderr)
        if args.check:
            return 2

    paths = write_outputs(report, out_dir)
    md = paths["markdown"].read_text(encoding="utf-8")
    assert_no_secrets(md, paths["markdown"].name)
    print(f"wrote {paths['markdown']}")
    print(f"wrote {paths['summary']}")
    print(f"wrote {paths['evidence']}")
    print(f"wrote {paths['exceptions']}")
    print(f"wrote {paths['run']}")
    print(
        "counts fulfilled={fulfilled} cancelled={cancelled} hold={hold} exception={exception} input={input_rows}".format(
            **{
                "fulfilled": sum(1 for r in report.rows if r.bucket == "fulfilled"),
                "cancelled": sum(1 for r in report.rows if r.bucket == "cancelled"),
                "hold": sum(1 for r in report.rows if r.bucket == "hold"),
                "exception": sum(1 for r in report.rows if r.bucket == "exception"),
                "input_rows": len(report.rows),
            }
        )
    )
    print(f"lineage_errors={len(errors)}")
    return 0 if not errors else 2


if __name__ == "__main__":
    sys.exit(main())
