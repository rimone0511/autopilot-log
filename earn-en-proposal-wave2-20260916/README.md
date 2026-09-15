> **DRAFT_ONLY. DO NOT SEND.**  
> No live bids, briefs, custom offers, or Contra applications from this pack.  
> No secrets. No KYC. Rates stay placeholders. Agent does not submit.

# English proposal DRAFT pack — Wave 2 (2026-09-16)

Pack date: 2026-09-16  
Desks: Upwork, Fiverr, Contra  
Mode: **DRAFT_ONLY** + **HANDS** (human paste, one listing at a time)  
Language: English paste for a Japan-based independent  
Seller: `{{DISPLAY_NAME}}` (recommended: Yuta Ishida / 石田祐太)  
Public notes: https://yutalab.dev/  
Public tool: https://github.com/rimone0511/autopilot-log

Wave 1 (`earn-en-proposal-drafts-20260916/`) is **desk-flow** copy (cover letter vs invite vs inbox vs Brief vs custom offer).  
This Wave 2 pack is **theme-specific** cover/offer text tied to the seller bio:

1. n8n workflow  
2. lead classify  
3. AI ops  
4. JP/EN writing assist  

Pick **one** file that matches both the desk **and** the listing. Do not stack three themes into one paste.

**Do not merge this as an auto-bidder.** There is no submit script. There is no Connects sprayer. There is no inbox crawler.

Rules: [HANDS-AND-TOS.md](HANDS-AND-TOS.md).

---

## Twelve drafts (4 themes × 3 desks)

| # | File | Desk | Seller theme | Paste into |
|---|---|---|---|---|
| 01 | [01-upwork-n8n-workflow.md](01-upwork-n8n-workflow.md) | Upwork | n8n workflow | Job cover letter |
| 02 | [02-upwork-lead-classify.md](02-upwork-lead-classify.md) | Upwork | lead classify | Job cover letter |
| 03 | [03-upwork-ai-ops.md](03-upwork-ai-ops.md) | Upwork | AI ops | Job cover letter |
| 04 | [04-upwork-jp-en-writing.md](04-upwork-jp-en-writing.md) | Upwork | JP/EN writing assist | Job cover letter |
| 05 | [05-fiverr-n8n-workflow.md](05-fiverr-n8n-workflow.md) | Fiverr | n8n workflow | Brief intro / custom-offer body |
| 06 | [06-fiverr-lead-classify.md](06-fiverr-lead-classify.md) | Fiverr | lead classify | Brief intro / custom-offer body |
| 07 | [07-fiverr-ai-ops.md](07-fiverr-ai-ops.md) | Fiverr | AI ops | Brief intro / custom-offer body |
| 08 | [08-fiverr-jp-en-writing.md](08-fiverr-jp-en-writing.md) | Fiverr | JP/EN writing assist | Inbox reply / custom-offer body |
| 09 | [09-contra-n8n-workflow.md](09-contra-n8n-workflow.md) | Contra | n8n workflow | One public opportunity |
| 10 | [10-contra-lead-classify.md](10-contra-lead-classify.md) | Contra | lead classify | One public opportunity |
| 11 | [11-contra-ai-ops.md](11-contra-ai-ops.md) | Contra | AI ops | One public opportunity |
| 12 | [12-contra-jp-en-writing.md](12-contra-jp-en-writing.md) | Contra | JP/EN writing assist | One public opportunity |

Each file keeps a **fact table** (operator metadata + form-field rates) **outside** the fenced paste. Do not copy the fact table into the marketplace.

---

## Send gate (every paste)

Skip the listing if any box is false. This pack still does **not** send.

- [ ] I opened **this** job / brief / inquiry in the **official site UI** (not a scraper, not a third-party bid tool).
- [ ] I replaced `{{ONE_SPECIFIC_DETAIL}}` with a fact from **this** listing. If I cannot name one in about a minute, I skip.
- [ ] Leftover placeholders from a previous listing are gone.
- [ ] No email, phone, WhatsApp, Telegram, Slack, Discord, or “text me at…” in the paste.
- [ ] No off-platform payment, crypto-to-wallet, or “pay me outside”.
- [ ] Rate fields on the form use `{{HOURLY_RATE_USD}}` or `{{FIXED_PRICE_USD}}` from the **local ledger**. Git has no live USD.
- [ ] I will click **Submit / Send** myself. Nothing in this folder submits for me.
- [ ] The work is official APIs / documented connectors + docs, or bilingual writing of operator text. Scraping, likes/follows/views, ungated posting, or ghostwritten reviews → decline (Wave 1 snippet 08).

---

## Fact table vs prose

| Layer | Lives in | Contains rates? |
|---|---|---|
| Fact table | Markdown above the fences | Yes — **placeholders only**, mapped to UI fields |
| Form fields on the live desk | Upwork bid / Fiverr offer / Contra proposal | Human types the local number |
| Fenced paste | Cover letter / offer body / application | **No live prices.** Do not paste the fact table |

If a live form **blocks** submit with an empty rate: park `rate_required` and stop. Do not invent USD in git. Do not send from this PR.

---

## Shared placeholders

Replace locally. Never commit filled values (except the public URLs already listed).

| Token | Meaning | In this repo |
|---|---|---|
| `{{DISPLAY_NAME}}` | Seller display name | Recommended: Yuta Ishida |
| `{{CLIENT_LABEL}}` | Internal memo label | Fictional only (`Client A` … `Client L`) |
| `{{JOB_TITLE}}` | Listing title | Fictional examples only |
| `{{ONE_SPECIFIC_DETAIL}}` | Phrase only this listing contains | Required; skip if empty |
| `{{SCOPE_ONE_LINER}}` | One-sentence restatement of the ask | Fictional examples only |
| `{{STACK_OR_TOOL}}` | n8n, Sheets, CRM field, etc. | Do not claim partner badges |
| `{{QUESTION_1}}` `{{QUESTION_2}}` | Scope questions | Empty → do not send |
| `{{HOURLY_RATE_USD}}` | Hourly form field | Placeholder; not a quote |
| `{{FIXED_PRICE_USD}}` | Fixed / custom-offer price field | Must match the form if the form shows a price |
| `{{DELIVERY_DAYS}}` | Delivery / duration field | Placeholder |
| `{{REVISION_COUNT}}` | Revisions field | Placeholder |
| `{{TIMEZONE}}` | Async window | Local ledger (example: `JST`) |
| `{{GIG_TITLE}}` | Fiverr Gig title | Sibling Gig pack; unpublished |
| `{{PORTFOLIO_URL}}` | Public site | `https://yutalab.dev/` |
| `{{GITHUB_REPO_AUTOPILOT}}` | Public fail-closed example | `https://github.com/rimone0511/autopilot-log` |
| `{{PLATFORM_FEE_NOTE}}` | Fee one-liner | Re-read official help; do not freeze a % here |

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

| Desk | Paste | Guidance |
|---|---|---|
| Upwork cover letter | Short or standard | Most letters ~200–300 words or fewer ([cover letter tips](https://www.upwork.com/resources/cover-letter-tips)). First sentence must include `{{ONE_SPECIFIC_DETAIL}}`. |
| Fiverr inbox / Brief | Short | Keep the first reply short; price lives in the offer form. |
| Fiverr custom offer | Standard | Trust the on-screen character counter. |
| Contra opportunity | Short or standard | Rewrite `{{ONE_SPECIFIC_DETAIL}}` every time. No identical blasts. |

Character counts in each file’s fact table are `len()` of the fenced body (placeholders unsubstituted, 2026-09-16). Filling placeholders **increases** length. Re-count on the live form.

Measured this pack (`len` including the trailing newline inside each fence):

| File | preview | short | standard |
|---|---:|---:|---:|
| 01 n8n / Upwork | 124 | 735 | 1313 |
| 02 lead classify / Upwork | 127 | 656 | 1191 |
| 03 AI ops / Upwork | 125 | 624 | 1081 |
| 04 JP/EN writing / Upwork | 132 | 644 | 1162 |
| 05 n8n / Fiverr | 108 | 480 | 746 |
| 06 lead classify / Fiverr | 111 | 425 | 739 |
| 07 AI ops / Fiverr | 103 | 385 | 738 |
| 08 JP/EN writing / Fiverr | 122 | 448 | 658 |
| 09 n8n / Contra | 69 | 502 | 711 |
| 10 lead classify / Contra | 108 | 438 | 678 |
| 11 AI ops / Contra | 108 | 417 | 774 |
| 12 JP/EN writing / Contra | 112 | 450 | 795 |

Upwork standard pastes are ~166–211 words (inside the “about 200–300 or fewer” guidance). Fiverr / Contra stay shorter.

---

## Out of this folder on purpose

- Account signup / KYC (other earn-ops packs)
- Fiverr Gig body / Upwork Catalog copy / profile overview (sibling packs)
- Wave 1 desk-flow snippets (invite reply, stay-on-platform decline)
- Buying Connects, Boosted Proposals, featured Gigs, Contra Pro
- Any script, extension, or API call that submits a bid

## 日本語（運用だけ）

下書きのみ。1件ずつ公式画面で貼る。`{{ONE_SPECIFIC_DETAIL}}` が埋まらなければ送らない。本文に金額を埋め込まない（画面の料金欄はプレースホルダ）。自動応募・一括送信・外部ボットはしない。メール・電話・WhatsApp は契約前に書かない。秘密はコミットしない。
