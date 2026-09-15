> **DRAFT_ONLY. DO NOT SEND.**  
> Default for this folder is **do-not-send**. No live Contra applications. No spray. No signup. No secrets.  
> Agent does not submit. There is no apply script.

# Contra Independent JOBS-phase proposal DRAFTs (2026-09-16)

Pack date: 2026-09-16  
Desk: [Contra](https://contra.com/) Independent / **Share work** (QUEUE A8 / CU-08)  
Phase: **JOBS** (Job feed apply text) — not signup, not profile paste, not KYC  
Mode: **DRAFT_ONLY** + **HANDS** (human paste, **one listing per style**, then stop)  
Language: English paste for a Japan-based independent  
Seller: `{{DISPLAY_NAME}}` (recommended: Yuta Ishida / 石田祐太)  
Public notes: https://yutalab.dev/  
Public tool: https://github.com/rimone0511/autopilot-log

**JOBS phase** means: you already have (or will have) an Independent account from a sibling CU pack. This folder is **five** n8n / AI-ops application drafts for the official Job feed. It does **not** click Apply.

Official apply help (live UI wins): [Applying to jobs on Contra](https://help.contra.com/en/articles/9322973-applying-to-jobs-on-contra) — Job feed → **Apply** or **Dismiss**. Paid-project numbers, if a fit happens later, live in the official proposal UI ([Paid projects](https://help.contra.com/en/articles/9322763-paid-projects); create URL cited there: `https://contra.com/proposal/new`). **Cite those URLs. Do not copy fee tables into git.**

Sibling CU STATUS still says **apply: no** until a later human GO. This pack does **not** override that. Default remains **do not send**.

Rules: [HANDS-AND-TOS.md](HANDS-AND-TOS.md).

---

## Five styles (one listing each)

| # | File | Listing style | Paste into |
|---|---|---|---|
| 01 | [01-n8n-inbound-path.md](01-n8n-inbound-path.md) | **n8n inbound path** — one trigger → destination → failure alert + SOP | Apply text on **one** Job-feed posting |
| 02 | [02-n8n-lead-classify.md](02-n8n-lead-classify.md) | **n8n lead classify / inbound route** — tags + Hold bucket; no outbound spray | Apply text on **one** inbound-classify posting |
| 03 | [03-ai-ops-inspectable.md](03-ai-ops-inspectable.md) | **Inspectable AI ops** — brief, draft, human approve before send/publish | Apply text on **one** AI-ops posting |
| 04 | [04-n8n-approval-gate.md](04-n8n-approval-gate.md) | **Fail-closed approval / posting gate** — automation may run; publish is a separate switch | Apply text on **one** gated-send/publish posting |
| 05 | [05-n8n-sheet-ops-sync.md](05-n8n-sheet-ops-sync.md) | **n8n sheet / ops sync** — documented connector + operator rerun page | Apply text on **one** sheet/ops-sync posting |

Pick **one** file that matches the posting. Do not stack five styles into one paste. Using a template on a second job of the same style is spray. Close the extras.

Each file keeps a **fact table** (operator metadata + form-field rates) **outside** the fenced paste. Do not copy the fact table into Contra.

Browse: the signed-in **Job feed** on contra.com (help: filter by tools, skills, budgets). Public marketing: [Find freelance jobs](https://contra.com/features/find-freelance-jobs). Do not scrape. Do not invent listing IDs.

---

## Send gate (every paste)

Skip if any box is false. This pack still does **not** send.

- [ ] I opened **this** job on contra.com (Job feed / opportunity UI — not a scrape dump, not a third-party apply tool).
- [ ] I replaced `{{ONE_SPECIFIC_DETAIL}}` with a fact from **this** posting. If I cannot name one in about a minute, I skip.
- [ ] This is the **only** listing I will use this style file on (no identical-blast, no “apply to more because the blog said habit”).
- [ ] Leftover placeholders from a previous listing are gone.
- [ ] No email, phone, WhatsApp, Telegram, Slack, Discord, or “text me at…” in the paste. If the live proposal form has email slots, leave platform-owned values; do not type a new off-platform address into git or into the letter.
- [ ] No off-platform payment, crypto-to-wallet, or “pay me outside”.
- [ ] Rate / timeline fields use `{{HOURLY_RATE_USD}}` / `{{FIXED_PRICE_USD}}` / `{{DELIVERY_DAYS}}` from the **local ledger**. Git has no live USD.
- [ ] I re-read [Paid projects](https://help.contra.com/en/articles/9322763-paid-projects) immediately before considering a paid-project form. I did **not** copy the fee table into this letter or into git.
- [ ] The live form does **not** require Contra Pro / Max, wallet funding, Persona / identity upload, or a card wall to Apply. If it does: **stop**.
- [ ] I am not using **Refer & Earn** from this pack (help opens DMs that can go off Contra — out of scope).
- [ ] I am not applying to Contra Labs, Expert programs, or Discover-boost from this pack.
- [ ] I will click **Apply** myself. Nothing in this folder submits for me.
- [ ] The work is official APIs / documented connectors + docs. Scraping, likes/follows/views, ungated posting, or fully autonomous outbound → **Dismiss** (do not apply).

If more than one job is open in your head, you are already off surgical. Close the extras.

---

## Fact table vs prose

| Layer | Lives in | Contains rates? |
|---|---|---|
| Fact table | Markdown **above** the fences, in each style file | Yes — **placeholders only**, mapped to UI fields |
| Form fields on the live desk | Contra Apply / paid-project proposal | Human types the local number |
| Fenced paste | Application / proposal body | **No live prices.** Do not paste the fact table |

If a live form **blocks** submit with an empty rate: park `rate_required` and stop. Do not invent USD in git. Do not send from this PR.

Empty required `{{ONE_SPECIFIC_DETAIL}}` → skip. Do not reuse a detail from another listing.

---

## Shared placeholders

Replace locally. Never commit filled values (except the public URLs already listed).

| Token | Meaning | In this repo |
|---|---|---|
| `{{DISPLAY_NAME}}` | Seller display name | Recommended: Yuta Ishida |
| `{{CLIENT_LABEL}}` | Internal memo label | Fictional only (`Client A` … `Client E`) |
| `{{JOB_TITLE}}` | Listing title | Fictional examples only |
| `{{ONE_SPECIFIC_DETAIL}}` | Phrase only this listing contains | **Required**; skip if empty |
| `{{SCOPE_ONE_LINER}}` | One-sentence restatement of the ask | Fictional examples only |
| `{{STACK_OR_TOOL}}` | n8n, Sheets, CRM field, etc. | Do not claim partner badges |
| `{{QUESTION_1}}` `{{QUESTION_2}}` | Scope questions | Empty → do not send |
| `{{HOURLY_RATE_USD}}` | Hourly **form field** | Placeholder; not a quote in prose |
| `{{FIXED_PRICE_USD}}` | Fixed / paid-project **form field** | Placeholder; not a quote in prose |
| `{{DELIVERY_DAYS}}` | Timeline **form field** | Placeholder |
| `{{PROJECT_NAME}}` | Paid-project name field (if shown) | Placeholder; create on-platform only |
| `{{TIMEZONE}}` | Async window | Local ledger (example: `JST`) |
| `{{PORTFOLIO_URL}}` | Public site | `https://yutalab.dev/` |
| `{{GITHUB_REPO_AUTOPILOT}}` | Public fail-closed example | `https://github.com/rimone0511/autopilot-log` |

Public URLs (not secrets):

- https://yutalab.dev/
- https://github.com/rimone0511
- https://github.com/rimone0511/autopilot-log
- https://help.contra.com/en/articles/9322973-applying-to-jobs-on-contra
- https://help.contra.com/en/articles/9322763-paid-projects
- https://contra.com/policies/terms
- https://contra.com/proposal/new

---

## What this pack will not claim

- Years of experience, GMV, “top-rated Independent”, Expert badge, Discover score, or traffic counts
- A US/EU address (Japan is fine; do not spoof location — sibling CU left location as a **stop**, not a jobs-phase fix)
- That Autopilot Log posts TikTok unattended (inbox upload is the default; direct post is gated)
- n8n Expert / Zapier Partner / Make Partner / xAI / Anthropic / OpenAI affiliation
- That an AI agent will send customer email, publish, or take payment without a human stop
- Scraping, engagement pods, or bypass of a platform with no official API
- Any Contra Pro price or paid-project **fee amount** (read the live help page)

---

## Length (practical; live counter wins)

Trust the on-screen counter. Help does not publish a character cap for Job-feed Apply text.

Character counts in each file’s fact table are `len()` of the fenced body (placeholders unsubstituted, 2026-09-16). Filling placeholders **increases** length. Re-count on the live form.

Measured this pack (`len` including the trailing newline inside each fence):

| File | preview | short | standard |
|---|---:|---:|---:|
| 01 n8n inbound path | 69 | 533 | 832 |
| 02 n8n lead classify | 108 | 508 | 755 |
| 03 AI ops inspectable | 108 | 435 | 810 |
| 04 n8n approval gate | 124 | 541 | 817 |
| 05 n8n sheet/ops sync | 106 | 496 | 835 |

First sentence of every paste must contain `{{ONE_SPECIFIC_DETAIL}}`.

---

## Out of this folder on purpose

- Account signup / Google login / KYC / wallet / Persona (sibling CU packs; **this pack does not sign up**)
- Profile / one-liner / About paste (sibling Contra paste packs)
- Wave 1 desk-flow snippets and Wave 2 4-theme × 3-desk cover letters (siblings; this pack is Contra Job-feed only)
- Buying Contra Pro / Max, Expert programs, Contra Labs, Refer & Earn, Discover boost
- Inviting off-platform clients onto Contra (first-client help Step 2 — not this GO)
- Any script, extension, scraper, or API call that submits an application

## 日本語（運用だけ）

下書きのみ。既定は送らない。スタイルごとに公式 Job feed で **1件だけ**。`{{ONE_SPECIFIC_DETAIL}}` が埋まらなければスキップ。本文に金額を埋め込まない。手数料の数字は書かず Paid projects ヘルプを送る直前に読む。Pro 課金壁・本人確認・ウォレットが Apply に必要なら止まる。自動応募・同一文面の連投・登録・秘密のコミットはしない。
