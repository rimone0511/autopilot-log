# GAPS.md — template (SKU-0 look-don't-ship)

Pack date: 2026-09-16  
Desk: Gumroad  
SKU: **SKU-0** (starter intake: form → table → notify)  
Mode: **DRAFT_ONLY. Template only in git. Do not publish. No payout setup.**

Fill a **local** copy after a [CHECKLIST.md](CHECKLIST.md) look-pass. Prefer
`present` / `missing` / `mismatch` / `not_checked` / `n/a` over live strings.

**Do not commit** a real `gumroad.com/l/...` URL, a filled price, a bank/tax
value, or a cover filename that contains a secret. If you must name a live
field, use a placeholder token.

This file ships empty of live observations. The rows below are the template.

---

## How to fill

| Value | Meaning |
|---|---|
| `not_checked` | Look-pass not run yet (default in this PR) |
| `missing` | Expected for a later ship; absent on the draft |
| `present` | Seen on the unpublished product; still do not publish |
| `mismatch` | Present but does not match SKU-0 shape (form → table → notify) |
| `n/a` | Not applicable (e.g. no live draft to inspect) |
| `blocked` | Screen stopped the look (payout, KYC, captcha). Stop. Do not retry from an agent |

Leave `notes` short. No GMV, no “will sell”, no invented permalink.

---

## Repo / pack (known paths only)

SKU-0 product files are **not in this repository**. Do not invent a pack path.

| ID | Item | Status | Notes (no live product URL) |
|---|---|---|---|
| R1 | SKU-0 pack folder on `master` (`earn-sku0-*` or `ops/earn/sku-0*`) | `missing` | Searched this checkout; not present |
| R2 | SKU-0 pack on a sibling PR branch | `missing` | No `earn-sku0-*` PR at pack-write time |
| R3 | QUEUE placeholder `earn-packs/gumroad/` | `missing` | INDEX in [PR#14](https://github.com/rimone0511/autopilot-log/pull/14) lists it as no PR |
| R4 | Live product URL in git | `missing` | Do not invent `gumroad.com/l/...` |
| R5 | Listing paste (`LISTING-EN.md` / `LISTING-JA.md`) for SKU-0 | `missing` | SKU-1/2/3 listings are other SKUs |
| R6 | Buyer zip / stubs for SKU-0 | `missing` | Do not attach SKU-1/2/3 stubs |
| R7 | Price token `{{PRICE_USD_SKU0}}` | `missing` | Named in SKU-1 PRICING; owning pack absent |
| R8 | Permalink token `{{GUMROAD_PERMALINK_SKU0}}` | `n/a` | Local only; no URL to record |

Sibling paste packs (not SKU-0, not this look-target):

- SKU-1: `earn-sku1-n8n-pack-draft-20260916/` — [PR#37](https://github.com/rimone0511/autopilot-log/pull/37)
- SKU-2: `earn-sku2-approval-gate-pack-draft-20260916/` — [PR#46](https://github.com/rimone0511/autopilot-log/pull/46)
- SKU-3: `earn-sku3-sheet-sync-pack-draft-20260916/` — [PR#52](https://github.com/rimone0511/autopilot-log/pull/52)

---

## Live unpublished SKU (human look-pass)

Default `not_checked`: this agent did not open Gumroad.

| ID | Item | Status | Notes |
|---|---|---|---|
| L1 | Unpublished digital product found on products list | `not_checked` | If none: `missing` + stop (do not New product) |
| L2 | Matches SKU-0 shape (form → table → notify), not SKU-1/2/3 | `not_checked` | |
| L3 | Status unpublished / not buyable | `not_checked` | If live: `already_published` + stop; do not unpublish from an agent |
| L4 | Title / name filled | `not_checked` | Do not commit the live name |
| L5 | Title not partner-keyword-stuffed | `not_checked` | |
| L6 | Price present on draft (look only; do not change) | `not_checked` | Token `{{PRICE_USD_SKU0}}`; do not commit the number |
| L7 | Pay-what-you-want off | `not_checked` | |
| L8 | Fake compare-at / scarcity off | `not_checked` | |
| L9 | Extra paid versions off | `not_checked` | One digital SKU |
| L10 | Cover image(s) | `not_checked` | Empty is an allowed gap; do not upload n8n logo |
| L11 | Thumbnail (≥ 600×600 if used) | `not_checked` | Optional; empty is an allowed gap |
| L12 | Cover is original / not a partner badge | `not_checked` | `n/a` if no cover |
| L13 | Content-tab files present | `not_checked` | Empty is a later ship-blocker, not a publish prompt |
| L14 | Files look like buyer content, not operator/KYC | `not_checked` | `n/a` if no files |
| L15 | No filled secrets in attached files | `not_checked` | |
| L16 | Payout / KYC screen stayed closed | `not_checked` | If it opened: `blocked` + stop |
| L17 | Publish / Enable not clicked | `not_checked` | Must remain true |

---

## Ship-blockers (human later — not this PR)

A later human may ship only after **all** of these are resolved **and** a
separate, explicit human decision to publish. This pack does not grant that
decision.

- [ ] SKU-0 pack exists in git (listing paste + buyer zip + `DRAFT_ONLY`)
- [ ] Live draft title matches that listing paste
- [ ] Live price chosen locally (not $0 “to test”)
- [ ] Cover / thumbnail: original assets, or an explicit human “ship without”
- [ ] Content tab: buyer files only, stubs inactive, no secrets
- [ ] Still unpublished until the human Publish click (not an agent)

Until then: `draft_saved`. Next CU is not Gumroad.

---

## Local observation block (do not commit filled)

```
date_jst:
operator:
sku0_live_draft: yes / no / not_checked
{{GUMROAD_PERMALINK_SKU0}}:
{{PRICE_USD_SKU0}}:
cover_count:
file_count:
stopped_at: unpublished | payout_screen | already_published | missing_draft
```
