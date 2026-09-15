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
        self.assertEqual(self.report.source_rel, "fixtures/inbound-ops-synthetic-w37.csv")
        self.assertEqual(self.report.timezone_name, "Asia/Tokyo")


class ProvenanceAndTimezoneTest(unittest.TestCase):
    """SOL P2 FAIL: labels/links must follow the real --input; timezone must calculate."""

    DEFAULT_NAME = "inbound-ops-synthetic-w37.csv"

    def test_custom_input_provenance_matches_source_link_and_hash(self):
        with tempfile.TemporaryDirectory(prefix="p2-custom-in-") as tmp:
            tmp_path = Path(tmp)
            custom = tmp_path / "customer-input.csv"
            custom.write_bytes(FIXTURE.read_bytes())
            digest = wr.sha256_file(custom)
            self.assertEqual(digest, wr.sha256_file(FIXTURE))
            self.assertEqual(wr.source_rel_for(custom), "customer-input.csv")
            self.assertNotIn(tmp_path.as_posix(), wr.source_rel_for(custom))

            report = wr.build_report(custom)
            self.assertEqual(report.source_rel, "customer-input.csv")
            self.assertEqual(report.input_sha256, digest)
            self.assertNotIn(self.DEFAULT_NAME, report.source_rel)

            out_dir = tmp_path / "out"
            paths = wr.write_outputs(report, out_dir)
            md = paths["markdown"].read_text(encoding="utf-8")
            evidence = paths["evidence"].read_text(encoding="utf-8")
            summary = paths["summary"].read_text(encoding="utf-8")
            exceptions = paths["exceptions"].read_text(encoding="utf-8")
            run = json.loads(paths["run"].read_text(encoding="utf-8"))

            self.assertIn("入力: `customer-input.csv`", md)
            self.assertIn(digest, md)
            self.assertIn("../customer-input.csv#L2", md)
            self.assertNotIn(self.DEFAULT_NAME, md)
            self.assertNotIn(tmp_path.as_posix(), md)

            self.assertEqual(run["input"], "customer-input.csv")
            self.assertEqual(run["input_sha256"], digest)
            self.assertNotIn(self.DEFAULT_NAME, run["input"])

            for body in (evidence, summary, exceptions):
                self.assertIn("customer-input.csv#L", body)
                self.assertNotIn(self.DEFAULT_NAME, body)
                self.assertNotIn(tmp_path.as_posix(), body)

            rc = wr.main(
                [
                    "--input",
                    str(custom),
                    "--out-dir",
                    str(out_dir / "cli"),
                    "--check",
                ]
            )
            self.assertEqual(rc, 0)
            cli_run = json.loads((out_dir / "cli" / "weekly-2026-W37-RUN.json").read_text(encoding="utf-8"))
            self.assertEqual(cli_run["input"], "customer-input.csv")
            self.assertEqual(cli_run["input_sha256"], digest)

    def test_broken_temp_copy_is_cited_as_evidence_source(self):
        with tempfile.TemporaryDirectory(prefix="p2-broken-copy-") as tmp:
            custom = Path(tmp) / "broken-copy.csv"
            text = FIXTURE.read_text(encoding="utf-8")
            text = text.replace(
                "ROW-W37-001,2026-09-07T09:12:00+09:00,store,NB-A5,2,480,fulfilled,合成・店頭",
                "ROW-W37-001,2026-09-07T09:12:00+09:00,store,NB-A5,-1,480,fulfilled,合成・壊した行",
            )
            custom.write_text(text, encoding="utf-8")
            digest = wr.sha256_file(custom)
            self.assertNotEqual(digest, wr.sha256_file(FIXTURE))

            report = wr.build_report(custom)
            l03 = next(x for x in report.lines if x.line_id == "L03")
            l15 = next(x for x in report.lines if x.line_id == "L15")
            self.assertNotIn("ROW-W37-001", l03.row_ids)
            self.assertIn("ROW-W37-001", l15.row_ids)
            self.assertEqual(l03.synthetic_jpy, 8640)

            paths = wr.write_outputs(report, Path(tmp) / "out")
            md = paths["markdown"].read_text(encoding="utf-8")
            run = json.loads(paths["run"].read_text(encoding="utf-8"))
            evidence = paths["evidence"].read_text(encoding="utf-8")
            self.assertEqual(run["input"], "broken-copy.csv")
            self.assertEqual(run["input_sha256"], digest)
            self.assertIn("broken-copy.csv", md)
            self.assertIn("../broken-copy.csv#L2", evidence)
            self.assertNotIn(self.DEFAULT_NAME, md)
            self.assertNotIn(self.DEFAULT_NAME, evidence)

    def test_timezone_utc_is_used_for_bounds_and_recorded(self):
        jst_report = wr.build_report(FIXTURE, timezone_name="Asia/Tokyo")
        utc_report = wr.build_report(FIXTURE, timezone_name="UTC")
        jst_alias = wr.build_report(FIXTURE, timezone_name="JST")

        self.assertEqual(jst_report.timezone_name, "Asia/Tokyo")
        self.assertEqual(jst_alias.timezone_name, "Asia/Tokyo")
        self.assertEqual(utc_report.timezone_name, "UTC")
        self.assertEqual(jst_report.week_start.isoformat(), "2026-09-07T00:00:00+09:00")
        self.assertEqual(utc_report.week_start.isoformat(), "2026-09-07T00:00:00+00:00")
        self.assertEqual(utc_report.week_end_exclusive.isoformat(), "2026-09-14T00:00:00+00:00")

        with tempfile.TemporaryDirectory(prefix="p2-tz-bound-") as tmp:
            custom = Path(tmp) / "tz-boundary.csv"
            custom.write_text(
                "row_id,occurred_at,channel,sku,qty,unit_amount_jpy,status,note\n"
                "ROW-TZ-JST-ONLY,2026-09-07T00:30:00+09:00,store,NB-A5,1,480,fulfilled,合成・JST週内UTC週外\n"
                "ROW-TZ-BOTH,2026-09-08T12:00:00+09:00,store,NB-A5,1,480,fulfilled,合成・両帯で週内\n",
                encoding="utf-8",
            )
            jst_b = wr.build_report(custom, timezone_name="Asia/Tokyo")
            utc_b = wr.build_report(custom, timezone_name="UTC")
            by_jst = {r.row_id: r for r in jst_b.rows}
            by_utc = {r.row_id: r for r in utc_b.rows}
            self.assertEqual(by_jst["ROW-TZ-JST-ONLY"].bucket, "fulfilled")
            self.assertEqual(by_utc["ROW-TZ-JST-ONLY"].bucket, "exception")
            self.assertIn("out_of_week", by_utc["ROW-TZ-JST-ONLY"].reasons)
            self.assertEqual(by_jst["ROW-TZ-BOTH"].bucket, "fulfilled")
            self.assertEqual(by_utc["ROW-TZ-BOTH"].bucket, "fulfilled")

            utc_paths = wr.write_outputs(utc_b, Path(tmp) / "out-utc")
            utc_md = utc_paths["markdown"].read_text(encoding="utf-8")
            utc_run = json.loads(utc_paths["run"].read_text(encoding="utf-8"))
            self.assertEqual(utc_run["timezone"], "UTC")
            self.assertEqual(utc_run["week_start"], "2026-09-07T00:00:00+00:00")
            self.assertEqual(utc_run["input"], "tz-boundary.csv")
            self.assertIn("（ISO、UTC）", utc_md)
            self.assertIn("tz-boundary.csv", utc_md)
            self.assertNotIn(self.DEFAULT_NAME, utc_md)

            rc = wr.main(
                [
                    "--input",
                    str(custom),
                    "--out-dir",
                    str(Path(tmp) / "out-cli"),
                    "--timezone",
                    "UTC",
                    "--check",
                ]
            )
            self.assertEqual(rc, 0)
            cli_run = json.loads((Path(tmp) / "out-cli" / "weekly-2026-W37-RUN.json").read_text(encoding="utf-8"))
            self.assertEqual(cli_run["timezone"], "UTC")
            self.assertEqual(cli_run["week_start"], "2026-09-07T00:00:00+00:00")

    def test_unknown_timezone_and_missing_input_fail_closed(self):
        with self.assertRaises(ValueError):
            wr.build_report(FIXTURE, timezone_name="Not/AZone")
        with tempfile.TemporaryDirectory(prefix="p2-missing-") as tmp:
            missing = Path(tmp) / "no-such.csv"
            rc_missing = wr.main(["--input", str(missing), "--out-dir", tmp, "--check"])
            self.assertEqual(rc_missing, 2)
            rc_tz = wr.main(
                [
                    "--input",
                    str(FIXTURE),
                    "--out-dir",
                    tmp,
                    "--timezone",
                    "Not/AZone",
                    "--check",
                ]
            )
            self.assertEqual(rc_tz, 2)


if __name__ == "__main__":
    unittest.main()
