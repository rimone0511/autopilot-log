> **DRAFT_ONLY.** Public GET notes. No live signup. No publish. No paid plan.
> **No secrets.** No passwords, OTP, CSRF tokens, OAuth `state`, cookies, phone, ID.
> **No invented fees / traffic.** Cite official public pages only. Category counts, 「○万人」, GMV are not activity proof.
> This folder is **prep**, not a CU playbook. Wave B CU does not start until Wave A `pending` is parked.

# Wave B activity-gate — batch 2 (2026-09-16)

Folder: `ops/earn/waveb-activity-gate-batch2-20260916/`  
Observed: **2026-09-16 JST** (public GET only). Login cookie: none. Forms: not submitted.

This batch’s desk ids **B10 / B11 / B12** are this folder’s labels:

| This folder | Desk | QUEUE (PR#1) | CU serial (PR#8) |
|---|---|---|---|
| **B10** | Anycrew | B5 | CU-15 |
| **B11** | MENTA | B6 | CU-16 |
| **B12** | ストアカ | B7 | CU-17 |

QUEUE **B10 Malt / B11 Workana / B12 Freelancermap** are different desks. Do not mix.

First JP Wave B gate: [PR#12](https://github.com/rimone0511/autopilot-log/pull/12) (`earn-activity-gate-waveB-20260916/`). That pass recorded all three as `needs_check` (SPA / WAF). This folder is a **re-GET**, not a copy of that body.

## Files

- [INDEX.md](INDEX.md) — pack map (paths, CU vs prep, sibling PRs)
- [STATUS.md](STATUS.md) — gate labels + CU hints for this batch
- [METHOD.md](METHOD.md) — URLs and HTTP only
- [records/b10-anycrew.md](records/b10-anycrew.md)
- [records/b11-menta.md](records/b11-menta.md)
- [records/b12-street-academy.md](records/b12-street-academy.md)

## Gate labels (this GET)

| Label | Meaning |
|---|---|
| `pass` | Public page shows a living desk **and** a freshness clue (dated card, 新着 card, official update date). Draft-only later. No publish |
| `needs_check` | Catalog unread (SPA / WAF / no date). Do not guess `pass` |
| `fail` / `SKIP thin` | Not used in this batch |

## This PR does not

- Create marketplace accounts or complete OAuth
- Upload KYC, bank, Stripe identity
- Publish profiles, plans, or classes
- Store secrets
- Invent fee % or traffic
- Change Python posting-gate tests
- Start Wave B CU (Wave A serial is still the live box)
