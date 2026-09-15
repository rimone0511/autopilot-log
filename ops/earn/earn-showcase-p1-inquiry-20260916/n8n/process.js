// Canonical runner is ../run.py. This Code node is the no-credential n8n mirror.
const AS_OF = Date.parse('2026-09-16T12:00:00Z');
const ALLOWED = new Set(['email', 'form', 'chat', 'phone_note']);
const RISK = ['返金', '苦情', 'クレーム', '弁護士', '訴訟', '法的', '詐欺', 'refund', 'lawyer', 'attorney', 'lawsuit', 'legal action', 'complaint'];
const UNCLEAR = new Set(['こんにちは', 'はじめまして', 'hello', 'hi', 'hey', '営業です', '資料希望', '?', '？']);
const PLACEHOLDER = new Set(['', '不明', 'unknown', 'n/a', 'なし', '未記載']);
const EMAIL_RE = /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/;
const NEAR = 0.88;
const AMBIG = 0.6;

function s(v) {
  return (v == null ? '' : String(v)).trim();
}
function email(v) {
  return s(v).toLowerCase();
}
function phone(v) {
  let d = s(v).replace(/\D+/g, '');
  if (d.startsWith('81') && d.length >= 12) d = '0' + d.slice(2);
  return d;
}
function normText(v) {
  return s(v).normalize('NFKC').toLowerCase().replace(/\s+/g, ' ').trim();
}
function shingles(v) {
  const t = normText(v).replace(/\s+/g, '').replace(/[。、．，,.!！?？:：;；'"「」『』（）()[\]/-]+/g, '');
  const out = new Set();
  if (!t) return out;
  if (t.length < 2) {
    out.add(t);
    return out;
  }
  for (let i = 0; i < t.length - 1; i++) out.add(t.slice(i, i + 2));
  return out;
}
function jaccard(a, b) {
  if (a.size === 0 || b.size === 0) return 0;
  let inter = 0;
  for (const x of a) if (b.has(x)) inter += 1;
  return inter / new Set([...a, ...b]).size;
}

function validate(row) {
  const reasons = [];
  if (!s(row.inquiry_id)) reasons.push('MISSING_INQUIRY_ID');
  const raw = s(row.received_at);
  const received = raw ? Date.parse(raw) : NaN;
  if (!raw) reasons.push('MISSING_RECEIVED_AT');
  else if (Number.isNaN(received)) reasons.push('UNPARSEABLE_RECEIVED_AT');
  else if (received > AS_OF) reasons.push('FUTURE_RECEIVED_AT');
  if (!ALLOWED.has(s(row.channel).toLowerCase())) reasons.push('UNKNOWN_CHANNEL');
  if (PLACEHOLDER.has(s(row.name).toLowerCase())) reasons.push('MISSING_NAME');
  const em = email(row.email);
  const ph = phone(row.phone);
  if (!em && !ph) reasons.push('MISSING_CONTACT');
  if (em && !EMAIL_RE.test(em)) reasons.push('INVALID_EMAIL');
  if (ph && (ph.length < 10 || ph.length > 11)) reasons.push('INVALID_PHONE');
  if (!s(row.subject)) reasons.push('MISSING_SUBJECT');
  const body = s(row.body);
  if (!body) reasons.push('MISSING_BODY');
  if (body && body.length < 8) reasons.push('BODY_TOO_SHORT');
  if (UNCLEAR.has(body.toLowerCase())) reasons.push('UNCLEAR_INTENT');
  const blob = `${s(row.subject)}\n${body}`.toLowerCase();
  if (RISK.some((k) => blob.includes(k.toLowerCase()))) reasons.push('RISK_KEYWORD');
  return reasons;
}

function keys(row) {
  const em = email(row.email);
  const ph = phone(row.phone);
  const name = normText(row.name);
  const company = normText(row.company);
  const out = {};
  if (em) out.email = em;
  if (ph && ph.length >= 10 && ph.length <= 11) out.phone = ph;
  if (name && company) out.name_company = `${name}|${company}`;
  return out;
}

function comparePair(newer, older) {
  const reasons = [];
  const a = keys(newer);
  const b = keys(older);
  const contacts = [];
  if (a.email && a.email === b.email) contacts.push('email');
  if (a.phone && a.phone === b.phone) contacts.push('phone');
  const body = jaccard(shingles(newer.body), shingles(older.body));
  if (contacts.includes('email')) reasons.push('EXACT_EMAIL_DUPLICATE');
  if (contacts.includes('phone')) reasons.push('EXACT_PHONE_DUPLICATE');
  if (body >= NEAR) reasons.push(contacts.length ? 'NEAR_DUPLICATE' : 'AMBIGUOUS_SIMILARITY');
  else if (body >= AMBIG) reasons.push('AMBIGUOUS_SIMILARITY');
  if (a.name_company && a.name_company === b.name_company && !contacts.length) reasons.push('AMBIGUOUS_IDENTITY');
  return { reasons: [...new Set(reasons)], body, contacts };
}

const incoming = $input.all().map((item) => item.json);
incoming.sort((x, y) => `${x.received_at}|${x.inquiry_id}`.localeCompare(`${y.received_at}|${y.inquiry_id}`));

const idCounts = {};
for (const row of incoming) {
  const id = s(row.inquiry_id);
  if (id) idCounts[id] = (idCounts[id] || 0) + 1;
}

const results = [];
const prior = [];
for (const row of incoming) {
  const validation = validate(row);
  const inquiryId = s(row.inquiry_id);
  if (inquiryId && idCounts[inquiryId] > 1) validation.push('DUPLICATE_INQUIRY_ID');
  const hits = [];
  for (const older of prior) {
    const cmp = comparePair(row, older);
    if (cmp.reasons.length) {
      hits.push({ other_id: older.inquiry_id, reasons: cmp.reasons, body_similarity: Math.round(cmp.body * 1000) / 1000, shared_contact: cmp.contacts });
    }
  }
  const reasons = [...new Set([...validation, ...hits.flatMap((h) => h.reasons)])];
  const queue = reasons.length ? 'needs_human' : 'ready_for_review';
  const item = {
    ...row,
    queue,
    severity: queue === 'needs_human' ? 'BLOCK' : 'REVIEW',
    decision: queue === 'needs_human' ? 'fail_closed' : 'human_review_required',
    reasons: reasons.length ? reasons : ['VALID_UNIQUE'],
    reason_text: (reasons.length ? reasons : ['VALID_UNIQUE']).join(';'),
    duplicate_of: hits.map((h) => h.other_id).join(','),
    sent: false,
    published: false,
    synthetic: true,
    reply_draft_sample: null,
  };
  if (queue === 'ready_for_review') {
    item.reply_draft_sample = {
      label: 'SAMPLE / 合成下書き',
      send_status: 'not_sent',
      body: `【SAMPLE / 合成下書き】この文面は見本です。送信しないでください。\n\n${s(row.name)} 様\nお問い合わせ「${s(row.subject)}」を受け付けました。`,
    };
  }
  results.push(item);
  const blockedId = ['MISSING_CONTACT', 'INVALID_EMAIL', 'INVALID_PHONE', 'MISSING_INQUIRY_ID'];
  const exact = reasons.some((r) => r.startsWith('EXACT_') || r === 'NEAR_DUPLICATE');
  if (queue === 'ready_for_review') prior.push(row);
  else if (!exact && !reasons.some((r) => blockedId.includes(r))) prior.push(row);
}

results.sort((x, y) => x.inquiry_id.localeCompare(y.inquiry_id));
return results.map((json) => ({ json }));
