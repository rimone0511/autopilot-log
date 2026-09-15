> **DRAFT_ONLY. DO NOT SEND.**  
> No live bids. No secrets. No KYC. Rates stay placeholders. Agent does not submit.  
> Upwork account may be blocked — do not send from this pack.

# English Upwork cover letter DRAFT pack — JOBS PHASE (2026-09-16)

Pack date: 2026-09-16  
Desk: **Upwork only**  
Phase: **JOBS** (posted-job cover letters)  
Mode: **DRAFT_ONLY** + **HANDS** (human paste, one listing at a time — and **not now**)  
Language: English paste for a Japan-based independent  
Seller: `{{DISPLAY_NAME}}` (recommended: Yuta Ishida / 石田祐太)  
Public notes: https://yutalab.dev/  
Public tool: https://github.com/rimone0511/autopilot-log

Wave 1 (`earn-en-proposal-drafts-20260916/`) is **desk-flow** copy (cover letter vs invite vs inbox).  
Wave 2 (`earn-en-proposal-wave2-20260916/`) is **theme × desk** (n8n / lead classify / AI ops / JP-EN × Upwork/Fiverr/Contra).  
This JOBS pack is **six Upwork job cover letters** for the seller’s n8n / AI ops / docs offer, with a **separate fact table** and rate placeholders only.

**Do not merge this as an auto-bidder.** There is no submit script. There is no Connects sprayer. There is no inbox crawler. Sibling STATUS packs report Upwork `blocked_skip` (Google access block). This folder does not retry that.

Rules: [HANDS-AND-TOS.md](HANDS-AND-TOS.md).  
Operator metadata + rates: [FACT-TABLE.md](FACT-TABLE.md) — **do not paste that file into Upwork**.

---

## Six drafts (n8n / AI ops / docs)

| # | File | Seller theme | Paste into |
|---|---|---|---|
| 01 | [01-n8n-inbound-workflow.md](01-n8n-inbound-workflow.md) | n8n inbound workflow | Job cover letter |
| 02 | [02-n8n-inquiry-classify.md](02-n8n-inquiry-classify.md) | n8n inquiry classify | Job cover letter |
| 03 | [03-n8n-approval-gate.md](03-n8n-approval-gate.md) | n8n approval gate | Job cover letter |
| 04 | [04-n8n-sheet-sync.md](04-n8n-sheet-sync.md) | n8n Google Sheet sync | Job cover letter |
| 05 | [05-ai-ops-inspect-loop.md](05-ai-ops-inspect-loop.md) | AI ops inspect loop | Job cover letter |
| 06 | [06-operator-docs-sop.md](06-operator-docs-sop.md) | operator docs / SOP | Job cover letter |

Pick **one** file that matches the listing. Do not stack six themes into one paste.

Each file keeps a **fact table** (operator metadata) **outside** the fenced paste. The pack-level table is [FACT-TABLE.md](FACT-TABLE.md). Do not copy either table into the marketplace.

---

## Send gate (every paste)

Skip — and **do not send from this PR**. If a later human un-parks send, skip the listing if any box is false.

- [ ] Upwork account is actually usable (today: **may be blocked**; do not retry Google SSO from this pack)
- [ ] I opened **this** job in the **official site UI** (not a scraper, not a third-party bid tool)
- [ ] I replaced `{{ONE_SPECIFIC_DETAIL}}` with a fact from **this** listing. If I cannot name one in about a minute, I skip
- [ ] Leftover placeholders from a previous listing are gone
- [ ] No email, phone, WhatsApp, Telegram, Slack, Discord, or “text me at…” in the paste
- [ ] No off-platform payment, crypto-to-wallet, or “pay me outside”
- [ ] Rate fields on the form use `{{HOURLY_RATE_USD}}` or `{{FIXED_PRICE_USD}}` from the **local ledger**. Git has no live USD
- [ ] I will click **Submit** myself. Nothing in this folder submits for me
- [ ] The work is official APIs / documented connectors + docs, or operator writing. Scraping, likes/follows/views, ungated posting, or ghostwritten reviews → decline (Wave 1 snippet 08)

---

## Fact table vs prose

| Layer | Lives in | Contains rates? |
|---|---|---|
| Pack fact table | [FACT-TABLE.md](FACT-TABLE.md) | Yes — **placeholders only**, mapped to UI fields |
| Per-file fact table | Markdown above the fences | Same placeholders; do not paste |
| Form fields on the live desk | Upwork bid form | Human types the local number |
| Fenced paste | Cover letter | **No live prices.** Do not paste the fact table |

If a live form **blocks** submit with an empty rate: park `rate_required` and stop. Do not invent USD in git. Do not send from this PR.

---

## Shared placeholders

Replace locally. Never commit filled values (except the public URLs already listed).

| Token | Meaning | In this repo |
|---|---|---|
| `{{DISPLAY_NAME}}` | Seller display name | Recommended: Yuta Ishida |
| `{{JOB_TITLE}}` | Listing title | Fictional examples only (`Job-A` … `Job-F`) |
| `{{ONE_SPECIFIC_DETAIL}}` | Phrase only this listing contains | Required; skip if empty |
| `{{SCOPE_ONE_LINER}}` | One-sentence restatement of the ask | Fictional examples only |
| `{{STACK_OR_TOOL}}` | n8n, Sheets, CRM field, etc. | Do not claim partner badges |
| `{{QUESTION_1}}` `{{QUESTION_2}}` | Scope questions | Empty → do not send |
| `{{HOURLY_RATE_USD}}` | Hourly form field | Placeholder; not a quote |
| `{{FIXED_PRICE_USD}}` | Fixed price field | Must match the form if the form shows a price |
| `{{DELIVERY_DAYS}}` | Delivery / duration field | Placeholder |
| `{{TIMEZONE}}` | Async window | Local ledger (example: `JST`) |
| `{{PORTFOLIO_URL}}` | Public site | `https://yutalab.dev/` |
| `{{GITHUB_REPO_AUTOPILOT}}` | Public fail-closed example | `https://github.com/rimone0511/autopilot-log` |

Public URLs (not secrets):

- https://yutalab.dev/
- https://github.com/rimone0511
- https://github.com/rimone0511/autopilot-log

---

## What this pack will not claim

- Years of experience, GMV, Job Success Score, “Top Rated”, or traffic counts
- A US/EU address (Japan is fine; do not spoof location)
- That Autopilot Log posts TikTok unattended (inbox upload is the default; direct post is gated)
- n8n Expert / Zapier Partner / Make Partner / xAI affiliation
- That an AI agent will send customer email, publish, or take payment without a human stop
- Scraping, engagement pods, or bypass of a platform with no official API

---

## Length (practical; live counter wins)

Upwork cover letters: most letters ~200–300 words or fewer ([cover letter tips](https://www.upwork.com/resources/cover-letter-tips)). First sentence must include `{{ONE_SPECIFIC_DETAIL}}`.

Character counts in [FACT-TABLE.md](FACT-TABLE.md) are `len()` of the fenced body (placeholders unsubstituted, 2026-09-16). Filling placeholders **increases** length. Re-count on the live form.

Measured this pack (`len` including the trailing newline inside each fence):

| File | preview | short | standard |
|---|---:|---:|---:|
| 01 n8n inbound | 154 | 803 | 1321 |
| 02 n8n classify | 153 | 716 | 1255 |
| 03 n8n approval | 169 | 641 | 1092 |
| 04 n8n sheet sync | 133 | 673 | 1047 |
| 05 AI ops | 138 | 637 | 1081 |
| 06 operator docs | 140 | 670 | 1233 |

---

## Out of this folder on purpose

- Account signup / KYC (other earn-ops packs)
- Retry of Upwork Google SSO / access block
- Fiverr Gig body / Upwork Catalog copy / profile overview (sibling packs)
- Wave 1 invite-reply / stay-on-platform decline snippets
- Wave 2 Fiverr / Contra theme files
- Buying Connects, Boosted Proposals
- Any script, extension, or API call that submits a bid

## 日本語（運用だけ）

下書きのみ。**送らない。** アカウントが止まっている可能性あり（Google アクセスブロック）。1件ずつ公式画面で貼る前提だが、このPRからは送信しない。`{{ONE_SPECIFIC_DETAIL}}` が埋まらなければ送らない。本文に金額を埋め込まない。自動応募・一括送信・外部ボットはしない。メール・電話・WhatsApp は契約前に書かない。秘密はコミットしない。
