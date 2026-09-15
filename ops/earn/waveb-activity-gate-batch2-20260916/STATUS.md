# STATUS — Wave B activity-gate batch 2

Snapshot: **2026-09-16 05:32 JST**  
Folder: `ops/earn/waveb-activity-gate-batch2-20260916/`  
State: **DRAFT_ONLY**

Public GET re-check of three JP Wave B desks. Not a signup log. Does not claim an account exists. Does not start Wave B CU.

Live CU box remains Wave A ([PR#49](https://github.com/rimone0511/autopilot-log/pull/49)). This STATUS does not override that box.

Forbidden: secrets, real emails/phones/passwords, KYC files, signup, publish, paid plans, invented traffic/GMV.

## Gate (this GET)

| # | desk | QUEUE | CU | gate label | freshness clue (public) | CU hint |
|---|---|---|---|---|---|---|
| B10 | Anycrew | B5 | CU-15 | `needs_check` | Job board `/offers` is an empty React shell. Company news **2026-08-31**. Blog **2026.08.26**. Not job-card dates | `pending` — do not open. Human must see one offer card date first |
| B11 | MENTA | B6 | CU-16 | `pass` | Public `/plan` cards with **NEW** labels (example titles recorded). Register face open | `pending` — Wave A first. Later: profile draft only; no plan publish |
| B12 | ストアカ | B7 | CU-17 | `pass` | `/online/all` class cards with session times **9月16日(水)** … and date filter JSON **2026-09-16** onward | `pending` — Wave A first. Later: teacher profile draft; no class publish |

Counts this box: `pass` 2 · `needs_check` 1 · `fail` 0 · `SKIP thin` 0.

## CU hint legend

| Hint | Use |
|---|---|
| `pending` | Not this pass. Do not open until Wave A parks and (for B10) a human has seen a dated offer card |
| `draft_saved` | Not claimed here. No account was created |
| `blocked_skip` | Not used in this batch |
| `in_progress` | Not this folder. Live box is Wave A |

## This pass

1. Record only. **Do not signup.**
2. B10 stays `needs_check`. SPA `/offers` has no card titles in this GET. Do not treat company news as job activity.
3. B11 / B12 may be considered for **draft** CU after Wave A. Still: no publish, stop at KYC.
4. If www.street-academy.com returns AWS WAF 405, retry a normal browser UA or park. WAF is not a dead site.
5. If MENTA filtered URLs (`/plan?order=2`) return WAF 202, use `/plan` with no query. Do not complete OAuth from this pack.

## vs PR#12 (first JP Wave B gate)

PR#12 body is not copied. That GET: Anycrew / MENTA / ストアカ all `needs_check`.  
This GET: MENTA and ストアカ have public catalog freshness clues → `pass`. Anycrew catalog still unread → `needs_check`.

## This PR does not

- Create accounts or complete Google / LINE / Facebook OAuth
- Publish profiles, mentor plans, or classes
- Buy paid plans
- Store CSRF / authenticity tokens / OAuth state
- Retry Wave A `blocked_skip` desks
- Start CU-15 / CU-16 / CU-17
