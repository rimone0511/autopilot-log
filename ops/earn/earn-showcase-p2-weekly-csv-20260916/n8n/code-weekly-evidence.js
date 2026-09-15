/**
 * P2 weekly evidence aggregator for n8n Code node (inactive showcase).
 * Canonical engine is ../src/weekly_report.py — keep predicates aligned.
 *
 * Expects items with CSV columns:
 * row_id, occurred_at, channel, sku, qty, unit_amount_jpy, status, note
 * plus optional source_line (1-based CSV line; defaults to item index + 2).
 *
 * No send. No credentials. Synthetic stationery shop only.
 */
const ALLOWED_CHANNELS = new Set(['store', 'web', 'phone', 'wholesale']);
const ALLOWED_SKUS = new Set(['NB-A5', 'PEN-BK', 'CLIP-20']);
const ALLOWED_STATUSES = new Set(['fulfilled', 'cancelled', 'hold']);
const WEEK_START = Date.parse('2026-09-07T00:00:00+09:00');
const WEEK_END = Date.parse('2026-09-14T00:00:00+09:00');
const SOURCE_REL = 'fixtures/inbound-ops-synthetic-w37.csv';

function parseIntStrict(raw) {
  const text = String(raw ?? '').trim();
  if (text === '') return { value: null, error: 'missing_number' };
  if (!/^-?\d+$/.test(text)) return { value: null, error: 'not_integer' };
  return { value: Number(text), error: null };
}

function parseDt(raw) {
  const text = String(raw ?? '').trim();
  if (!text) return null;
  const ms = Date.parse(text);
  if (Number.isNaN(ms)) return null;
  return ms;
}

const incoming = $input.all();
const sources = incoming.map((item, idx) => {
  const j = item.json || {};
  return {
    source_line: Number(j.source_line || idx + 2),
    row_id: String(j.row_id || '').trim(),
    occurred_at_raw: String(j.occurred_at || '').trim(),
    channel: String(j.channel || '').trim(),
    sku: String(j.sku || '').trim(),
    qty_raw: String(j.qty ?? '').trim(),
    unit_amount_raw: String(j.unit_amount_jpy ?? '').trim(),
    status: String(j.status || '').trim(),
    note: String(j.note || '').trim(),
  };
});

const idCounts = {};
for (const src of sources) {
  if (src.row_id) idCounts[src.row_id] = (idCounts[src.row_id] || 0) + 1;
}

const rows = sources.map((src) => {
  const reasons = [];
  if (!src.row_id) reasons.push('missing_row_id');
  else if ((idCounts[src.row_id] || 0) > 1) reasons.push('id_collision');

  const occurredMs = parseDt(src.occurred_at_raw);
  if (occurredMs === null) reasons.push('missing_or_bad_occurred_at');
  else if (occurredMs < WEEK_START || occurredMs >= WEEK_END) reasons.push('out_of_week');

  if (!ALLOWED_CHANNELS.has(src.channel)) reasons.push('unknown_channel');
  if (!src.sku) reasons.push('missing_sku');
  else if (!ALLOWED_SKUS.has(src.sku)) reasons.push('unknown_sku');
  if (!ALLOWED_STATUSES.has(src.status)) reasons.push('unknown_status');

  const qty = parseIntStrict(src.qty_raw);
  if (qty.error) reasons.push('bad_qty');
  else if (qty.value < 0) reasons.push('negative_qty');
  else if (qty.value === 0) reasons.push('zero_qty');

  const amount = parseIntStrict(src.unit_amount_raw);
  if (amount.error) reasons.push('bad_unit_amount');
  else if (amount.value < 0) reasons.push('negative_unit_amount');

  let lineAmount = null;
  if (qty.value !== null && amount.value !== null && qty.value > 0 && amount.value >= 0) {
    lineAmount = qty.value * amount.value;
  }

  return {
    ...src,
    bucket: reasons.length ? 'exception' : src.status,
    reasons,
    qty: qty.value,
    unit_amount_jpy: amount.value,
    line_amount_jpy: lineAmount,
  };
});

function agg(group) {
  const ordered = group.slice().sort((a, b) => a.source_line - b.source_line || a.row_id.localeCompare(b.row_id));
  return {
    row_count: ordered.length,
    qty: ordered.reduce((s, r) => s + (r.qty || 0), 0),
    synthetic_jpy: ordered.reduce((s, r) => s + (r.line_amount_jpy || 0), 0),
    row_ids: ordered.map((r) => r.row_id),
    source_lines: ordered.map((r) => r.source_line),
    evidence_links: ordered.map((r) => `../${SOURCE_REL}#L${r.source_line}`),
  };
}

const fulfilled = rows.filter((r) => r.bucket === 'fulfilled');
const cancelled = rows.filter((r) => r.bucket === 'cancelled');
const hold = rows.filter((r) => r.bucket === 'hold');
const exceptions = rows.filter((r) => r.bucket === 'exception');

const lines = [
  { line_id: 'L01', label: '確定件数（fulfilled）', predicate: 'bucket==fulfilled', ...agg(fulfilled) },
  { line_id: 'L03', label: '確定・合成金額(円)', predicate: 'bucket==fulfilled', ...agg(fulfilled) },
  { line_id: 'L11', label: 'キャンセル件数（確定合計に含めない）', predicate: 'bucket==cancelled', ...agg(cancelled) },
  { line_id: 'L13', label: '確認待ち件数（確定合計に含めない）', predicate: 'bucket==hold', ...agg(hold) },
  { line_id: 'L15', label: '除外件数（失敗は成功に混ぜない）', predicate: 'bucket==exception', ...agg(exceptions) },
];

const banner = 'SYNTHETIC / 合成データ。販売者の売上・顧客実績ではない。n8n は inactive 見本。正本は src/weekly_report.py。';
const md = [
  '# 週報 2026-W37 — n8n smoke（合成）',
  '',
  `> ${banner}`,
  '',
  '| 行ID | 指標 | 件数 | 合成円 | 根拠 |',
  '|---|---|---:|---:|---|',
  ...lines.map((line) => {
    const ev = line.row_ids.map((id, i) => `${id} (L${line.source_lines[i]})`).join(', ') || '（該当なし）';
    return `| ${line.line_id} | ${line.label} | ${line.row_count} | ${line.synthetic_jpy} | ${ev} |`;
  }),
  '',
  'このノードは送信しない。Operator が markdown をコピーするだけ。',
].join('\n');

return [
  {
    json: {
      synthetic: true,
      seller_revenue_claim: false,
      week: '2026-W37',
      banner,
      markdown: md,
      lines,
      exception_rows: exceptions.map((r) => ({
        row_id: r.row_id,
        source_line: r.source_line,
        reasons: r.reasons.join('|'),
        evidence_link: `../${SOURCE_REL}#L${r.source_line}`,
      })),
      next: 'operator-copy-only',
    },
  },
];
