> **DRAFT_ONLY. DO NOT SEND.**  
> Default for this folder is **do-not-send**. No live bids. No spray. No signup. No secrets.  
> Agent does not submit. There is no bid script.

# Freelancer.com surgical-bid DRAFT templates (2026-09-16)

Pack date: 2026-09-16  
Desk: [Freelancer.com](https://www.freelancer.com/) (QUEUE Wave A10)  
Mode: **DRAFT_ONLY** + **HANDS** (human paste, **one listing per style**, then stop)  
Language: English paste for a Japan-based independent  
Seller: `{{DISPLAY_NAME}}` (recommended: Yuta Ishida / 石田祐太)  
Public notes: https://yutalab.dev/  
Public tool: https://github.com/rimone0511/autopilot-log

**Surgical-bid** means: you open **one** project in the official bid UI, you can name one detail only that listing contains, you rewrite the first lines, you paste, **you** click Bid — or you skip. A computer must not be the thing that submits.

This folder is **three** bid-letter templates, **one listing each style**. Using a template on a second project of the same style is spray. Close the extras.

Sibling notes (`earn-freelancer-waveb-gap-notes-20260916/freelancer-com-surgical-bid-notes.md`) remain the CU gate: **No bids. No contests.** This pack does **not** override that. CU serial stays profile-only until a later human GO. Even after a GO, this pack’s default is still **do not send**.

Rules: [HANDS-AND-TOS.md](HANDS-AND-TOS.md).

Fees / charges: read the live schedule at send time. **Cite this URL only. Do not copy amounts into git.**

https://www.freelancer.com/feesandcharges

---

## Three styles (one listing each)

| # | File | Listing style | Public browse (not a bid) | Paste into |
|---|---|---|---|---|
| 01 | [01-fixed-price-n8n.md](01-fixed-price-n8n.md) | **Fixed-price** n8n / workflow project | https://www.freelancer.com/jobs/n8n | Bid proposal on **one** fixed-price project |
| 02 | [02-hourly-ai-ops.md](02-hourly-ai-ops.md) | **Hourly** AI ops / inspectable-agent project | https://www.freelancer.com/jobs/ai-agents | Bid proposal on **one** hourly project |
| 03 | [03-lead-classify.md](03-lead-classify.md) | **Lead classify / inbound route** project (fixed *or* hourly form) | same boards; pick a listing that is classify/route, not outbound spray | Bid proposal on **one** inbound-classify project |

Pick **one** file that matches the listing. Do not stack three styles into one paste. Do not open a contest, a Preferred/Recruiter-only row, or a “fund the Site wallet to continue” wall.

Each file keeps a **fact table** (operator metadata + form-field rates) **outside** the fenced paste. Do not copy the fact table into the marketplace.

---

## Send gate (every paste)

Skip if any box is false. This pack still does **not** send.

- [ ] I opened **this** project on freelancer.com (not a scrape dump, not a third-party bid tool).
- [ ] I replaced `{{ONE_SPECIFIC_DETAIL}}` with a fact from **this** listing. If I cannot name one in about a minute, I skip.
- [ ] This is the **only** listing I will use this style file on (no leftover-bid spray, no “use the monthly allotment”).
- [ ] Leftover placeholders from a previous listing are gone.
- [ ] No email, phone, WhatsApp, Telegram, Slack, Discord, or “text me at…” in the paste.
- [ ] No off-platform payment, crypto-to-wallet, or “pay me outside”.
- [ ] Bid amount / hourly rate / delivery days stay in **form fields** (`{{BID_AMOUNT_USD}}` / `{{HOURLY_RATE_USD}}` / `{{DELIVERY_DAYS}}` from the local ledger). Git has no live USD.
- [ ] I re-read https://www.freelancer.com/feesandcharges immediately before considering a bid. I did **not** copy the table into this letter.
- [ ] The live form does **not** require funding the Site wallet, buying a bid, buying membership, completing KYC, or a bid upgrade (Sponsored / Highlight / Sealed) to proceed. If it does: **stop**.
- [ ] I am not entering a contest. I am not applying to Preferred Freelancer.
- [ ] I will click **Bid / Place Bid** myself. Nothing in this folder submits for me.
- [ ] The work is official APIs / documented connectors + docs. Scraping, likes/follows/views, or ungated posting → decline (do not bid).

If more than one project is open in your head, you are already off surgical. Close the extras.

---

## Fact table vs prose

| Layer | Lives in | Contains rates? |
|---|---|---|
| Fact table | Markdown above the fences | Yes — **placeholders only**, mapped to UI fields |
| Form fields on the live desk | Freelancer bid amount / hourly / delivery | Human types the local number |
| Fenced paste | Bid proposal body | **No live prices.** Do not paste the fact table |

If a live form **blocks** submit with an empty rate: park `rate_required` and stop. Do not invent USD in git. Do not send from this PR.

Empty required `{{ONE_SPECIFIC_DETAIL}}` → skip. Do not reuse a detail from another listing.

---

## Shared placeholders

Replace locally. Never commit filled values (except the public URLs already listed).

| Token | Meaning | In this repo |
|---|---|---|
| `{{DISPLAY_NAME}}` | Seller display name | Recommended: Yuta Ishida |
| `{{CLIENT_LABEL}}` | Internal memo label | Fictional only (`Client A` / `B` / `C`) |
| `{{PROJECT_TITLE}}` | Listing title | Fictional examples only |
| `{{ONE_SPECIFIC_DETAIL}}` | Phrase only this listing contains | **Required**; skip if empty |
| `{{SCOPE_ONE_LINER}}` | One-sentence restatement of the ask | Fictional examples only |
| `{{STACK_OR_TOOL}}` | n8n, Sheets, CRM field, etc. | Do not claim partner badges |
| `{{QUESTION_1}}` `{{QUESTION_2}}` | Scope questions | Empty → do not send |
| `{{BID_AMOUNT_USD}}` | Fixed-price bid **form field** | Placeholder; not a quote in prose |
| `{{HOURLY_RATE_USD}}` | Hourly bid **form field** | Placeholder; not a quote in prose |
| `{{DELIVERY_DAYS}}` | Delivery / duration **form field** | Placeholder |
| `{{MILESTONE_1}}` | Optional first milestone label | Placeholder; create on-platform only |
| `{{TIMEZONE}}` | Async window | Local ledger (example: `JST`) |
| `{{PORTFOLIO_URL}}` | Public site | `https://yutalab.dev/` |
| `{{GITHUB_REPO_AUTOPILOT}}` | Public fail-closed example | `https://github.com/rimone0511/autopilot-log` |

Public URLs (not secrets):

- https://yutalab.dev/
- https://github.com/rimone0511
- https://github.com/rimone0511/autopilot-log
- https://www.freelancer.com/feesandcharges

---

## What this pack will not claim

- Years of experience, GMV, Job Completion Rate, “Preferred Freelancer”, or traffic counts
- A US/EU address (Japan is fine; do not spoof location)
- That Autopilot Log posts TikTok unattended (inbox upload is the default; direct post is gated)
- n8n Expert / Zapier Partner / Make Partner / xAI affiliation
- That an AI agent will send customer email, publish, or take payment without a human stop
- Scraping, engagement pods, or bypass of a platform with no official API
- Any fee, membership, or bid-upgrade **amount** (read the live fees page)

---

## Length (practical; live counter wins)

Do **not** treat third-party blogs as a character cap. If the bid form shows a counter, that counter is the cap.

Character counts in each file’s fact table are `len()` of the fenced body (placeholders unsubstituted, 2026-09-16). Filling placeholders **increases** length. Re-count on the live form.

Measured this pack (`len` including the trailing newline inside each fence):

| File | preview | short | standard |
|---|---:|---:|---:|
| 01 fixed-price n8n | 128 | 765 | 1349 |
| 02 hourly AI ops | 134 | 646 | 1281 |
| 03 lead classify | 131 | 659 | 1273 |

First sentence of every paste must contain `{{ONE_SPECIFIC_DETAIL}}`.

---

## Out of this folder on purpose

- Account signup / Google login / KYC / wallet funding (sibling profile pack; **this pack does not sign up**)
- Profile headline / skills paste (sibling `freelancer-com-profile-draft.md`)
- Contests, Preferred Freelancer exams, Sponsored / Highlight / Sealed bids
- Buying membership or extra bids
- Any script, extension, scraper, or Freelancer API call that submits a bid
- Copying the fees table into git

## 日本語（運用だけ）

下書きのみ。既定は送らない。スタイルごとに公式画面で **1件だけ**。`{{ONE_SPECIFIC_DETAIL}}` が埋まらなければスキップ。本文に金額を埋め込まない。手数料の数字は書かず https://www.freelancer.com/feesandcharges を送る直前に読む。自動入札・残り入札の使い切り・登録・秘密のコミットはしない。
