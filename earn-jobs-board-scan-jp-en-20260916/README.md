# JOBS PHASE — JP+EN board scan (2026-09-16)

**DRAFT_ONLY. DO NOT APPLY FROM THIS PACK.**

Public-web scan only. Folder: `earn-jobs-board-scan-jp-en-20260916/`.  
Agent did **not** sign up, log in, KYC, message, bid, or publish.  
Apply later is a **human** step, after click-time recheck.

Scan clock: 2026-09-15 UTC (folder date 2026-09-16, same GO wave as other earn-ops packs).  
Operator public evidence (not a guarantee): https://yutalab.dev/ · https://github.com/rimone0511/autopilot-log

---

## What this pack is

A list of **up to 20 concrete apply-candidate jobs/gigs** (URL + why-fit + draft angle) from:

| Market | Desks | What “apply” means here |
|---|---|---|
| JP | CrowdWorks / Lancers / Coconala | Bid on a **job/request**, or (Coconala) treat a **catalog gig** as keyword demand — not a bid |
| EN | Upwork / Fiverr / Contra | Bid on a **job**, or use **keyword + public gig/opportunity** URLs when the job UI is login/JS gated |

This is **JOBS PHASE**, not a proposal send pack. Parallel paste packs (`earn-jp-proposal-*`, `earn-en-proposal-*`) stay unused until a human picks a still-open URL.

## Hard rules

- **No signup.** Search, public job/request/gig pages, and search-indexed snippets only.
- **No invented pay.** If yen/USD is not on the cited public page, write `pay_not_on_page`. Listing bands on a card are **that listing**, not GMV, take-rate, or expected earnings.
- **`needs_check`** when this agent did not fully read the live page (login wall, JS/PX challenge, timeout, empty body). Recheck in a browser before treating it as open.
- **`closed_read`** means the public page was read and the board says 募集終了 / 表示できません. **Do not apply.** Kept only as “same-shape may reopen” notes, outside the 20.
- **DRAFT_ONLY angles.** Do not send. Do not paste a numeric bid from this pack.

## Fit filter (this operator)

Public repo `autopilot-log` is a **Python CLI** for **YouTube Data API v3** and TikTok **Content Posting API**, with a fail-closed posting gate. It **does not** do browser automation, scraping, likes/follows/comments, or posting content the client does not own.

| In scope (say yes) | Out of scope (say no in the angle) |
|---|---|
| Official API upload / metadata / quota-honest scheduling | Playwright / Selenium “human-like” posting |
| OAuth once, then unattended **private-by-default** upload | Auto-comments, auto-likes, view/follow bots |
| n8n / GAS / Sheets as **orchestration around official APIs** | Scraping channels for clip-theft |
| Human inspect before public | “Guaranteed views / freeze-proof” |

## Files

| File | Role |
|---|---|
| [SCOREBOARD.md](SCOREBOARD.md) | 20 candidates: URL, status, why-fit, draft angle |
| [KEYWORDS.md](KEYWORDS.md) | JP/EN search strings and public browse URLs |
| [CLOSED.md](CLOSED.md) | Public jobs this scan **read as ended** (do not apply) |

## Out of scope

- Marketplace accounts, proposals, DMs, gig publish
- Secrets, client PII, real bid amounts in git
- Income / win-rate / time-saved guarantees
- Changing Python posting-gate code (untouched)

## Verification

Markdown research pack. Click-time recheck is the `needs_check` list at the bottom of SCOREBOARD.md.  
Existing tests still apply to the CLI, not this folder: `python3 tests/test_gate.py`, `python3 tests/test_tiktok_gate.py`.
