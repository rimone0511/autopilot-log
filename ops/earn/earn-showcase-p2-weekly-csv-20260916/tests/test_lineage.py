#!/usr/bin/env python3
"""Lineage DoD for P2 weekly CSV showcase. Stdlib only."""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

PACK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PACK / "src"))

import weekly_report as wr  # noqa: E402

FIXTURE = PACK / "fixtures" / "inbound-ops-synthetic-w37.csv"
OUT = PACK / "out"
N8N = PACK / "n8n" / "p2-weekly-csv-evidence.inactive.json"


class LineageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = wr.build_report(FIXTURE)

    def test_lineage_closed_world(self):
        errors = wr.lineage_errors(self.report)
        self.assertEqual(errors, [])

    def test_sample_totals(self):
        l01 = next(x for x in self.report.lines if x.line_id == "L01")
        l02 = next(x for x in self.report.lines if x.line_id == "L02")
        l03 = next(x for x in self.report.lines if x.line_id == "L03")
        self.assertEqual(l01.row_count, 14)
        self.assertEqual(l02.qty, 38)
        self.assertEqual(l03.synthetic_jpy, 9600)

    def test_exceptions_never_in_fulfilled(self):
        l01 = next(x for x in self.report.lines if x.line_id == "L01")
        exception_lines = {r.source_line for r in self.report.rows if r.bucket == "exception"}
        self.assertTrue(exception_lines)
        self.assertTrue(set(l01.source_lines).isdisjoint(exception_lines))

    def test_collision_fail_closed(self):
        dups = [r for r in self.report.rows if r.row_id == "ROW-W37-DUP"]
        self.assertEqual(len(dups), 2)
        self.assertTrue(all(r.bucket == "exception" for r in dups))
        self.assertTrue(all("id_collision" in r.reasons for r in dups))
        l01 = next(x for x in self.report.lines if x.line_id == "L01")
        self.assertNotIn("ROW-W37-DUP", l01.row_ids)

    def test_zero_qty_and_out_of_week_excluded(self):
        by_id = {r.row_id: r for r in self.report.rows if r.row_id != "ROW-W37-DUP"}
        self.assertIn("zero_qty", by_id["ROW-W37-014"].reasons)
        self.assertIn("out_of_week", by_id["ROW-W37-019"].reasons)
        self.assertIn("out_of_week", by_id["ROW-W37-020"].reasons)
        l03 = next(x for x in self.report.lines if x.line_id == "L03")
        self.assertNotIn("ROW-W37-014", l03.row_ids)
        self.assertNotIn("ROW-W37-019", l03.row_ids)
        self.assertNotIn("ROW-W37-020", l03.row_ids)

    def test_channel_and_sku_partition_fulfilled(self):
        l01 = next(x for x in self.report.lines if x.line_id == "L01")
        channel_ids = []
        sku_ids = []
        for line in self.report.lines:
            if line.section == "channel":
                channel_ids.extend(line.row_ids)
            if line.section == "sku":
                sku_ids.extend(line.row_ids)
        self.assertEqual(sorted(channel_ids), sorted(l01.row_ids))
        self.assertEqual(sorted(sku_ids), sorted(l01.row_ids))

    def test_trace_wholesale_row(self):
        ids = [x.line_id for x in wr.lines_for_row(self.report, "ROW-W37-007")]
        self.assertIn("L01", ids)
        self.assertIn("L03", ids)
        self.assertIn("L07", ids)  # wholesale
        self.assertIn("L10", ids)  # CLIP-20

    def test_markdown_has_banner_and_links(self):
        md = wr.render_markdown(self.report)
        self.assertIn("SYNTHETIC", md)
        self.assertIn("販売者の売上", md)
        self.assertIn("../fixtures/inbound-ops-synthetic-w37.csv#L2", md)
        self.assertIn("ROW-W37-001", md)
        self.assertNotRegex(md, wr.SECRET_RE)

    def test_committed_out_matches_generator(self):
        with tempfile.TemporaryDirectory(prefix="p2-w37-") as tmp:
            wr.write_outputs(self.report, Path(tmp))
            for name in (
                "weekly-2026-W37.md",
                "weekly-2026-W37-summary.csv",
                "weekly-2026-W37-evidence.csv",
                "weekly-2026-W37-exceptions.csv",
                "weekly-2026-W37-RUN.json",
            ):
                got = (Path(tmp) / name).read_text(encoding="utf-8")
                committed = (OUT / name).read_text(encoding="utf-8")
                self.assertEqual(got, committed, name)

    def test_run_json_honest(self):
        run = json.loads((OUT / "weekly-2026-W37-RUN.json").read_text(encoding="utf-8"))
        self.assertTrue(run["synthetic"])
        self.assertFalse(run["seller_revenue_claim"])
        self.assertEqual(run["lineage_error_count"], 0)
        self.assertEqual(run["counts"]["fulfilled"], 14)
        self.assertEqual(run["counts"]["exception"], 11)

    def test_n8n_inactive_no_secrets(self):
        raw = N8N.read_text(encoding="utf-8")
        data = json.loads(raw)
        self.assertIs(data.get("active"), False)
        self.assertNotRegex(raw, wr.SECRET_RE)
        self.assertIn("DO NOT ACTIVATE", raw)
        self.assertNotIn("gmail", raw.lower())
        self.assertNotIn("slack", raw.lower())
        self.assertNotIn("webhook", raw.lower())
        names = [n.get("type") for n in data.get("nodes", [])]
        self.assertTrue(all("telegram" not in (t or "") for t in names))
        self.assertTrue(all("gmail" not in (t or "") for t in names))
        js = (PACK / "n8n" / "code-weekly-evidence.js").read_text(encoding="utf-8")
        code_node = next(n for n in data["nodes"] if n["name"] == "Evidence weekly STUB")
        self.assertEqual(code_node["parameters"]["jsCode"], js)

    def test_deterministic_hash_in_footer(self):
        self.assertEqual(self.report.input_sha256, wr.sha256_file(FIXTURE))
        md = (OUT / "weekly-2026-W37.md").read_text(encoding="utf-8")
        self.assertIn(self.report.input_sha256, md)


if __name__ == "__main__":
    unittest.main()
