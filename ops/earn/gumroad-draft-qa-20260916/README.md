# Gumroad draft QA — look-don't-ship (2026-09-16)

Pack date: 2026-09-16  
Desk: Gumroad (Wave A+ in the 2026-09-16 earn-ops queue)  
Target: **existing unpublished SKU-0** (starter intake: form → table → notify)  
Mode: **DRAFT_ONLY — look-don't-ship. Do not publish. No payout setup.**

This folder is an operator **QA checklist pack**. It is not a Gumroad product, not a
buyer zip, not a live listing, and not a payout / KYC run.

A human may open the already-unpublished SKU, look at title / price / icons / files,
and write gaps into [GAPS.md](GAPS.md). This pack does not create a product, attach
files, change a price, or click Publish / Enable.

## Hard rules

- **Look-don't-ship.** Inspect the existing unpublished SKU. Leave it unpublished.
- Do not click Gumroad **Publish** / **Enable** / go-live on a custom permalink.
- Do not announce a live `gumroad.com/l/...` URL. None is recorded in this repo.
- Stop before payout, bank, tax forms, or identity upload.
- MAIN Google only (`{{GOOGLE_ACCOUNT_EMAIL}}`). Do not create a second Gumroad.
- No secrets in git (passwords, API keys, tax IDs, bank numbers, ID scans).
- Do not invent product URLs, sales counts, GMV, or “this will sell”.
- Do not zip operator files into a customer download.
- Do not create or publish a Gumroad product from an agent browser session.

## Files

| File | Purpose |
|---|---|
| [CHECKLIST.md](CHECKLIST.md) | Look-don't-ship pass: title, price, icons (cover/thumbnail), files |
| [GAPS.md](GAPS.md) | Empty template for what the look-pass found (or did not find) |
| [STATUS.md](STATUS.md) | Pack status as of this PR — QA not run from this agent |

## SKU-0 paths in this repo

**No SKU-0 product pack is present on `master`, and no `earn-sku0-*` / `ops/earn/sku-0*` folder exists in sibling PRs searched for this pack.**

Do not invent a SKU-0 pack path or a Gumroad product URL. Record “missing” in
[GAPS.md](GAPS.md) until a later pack lands.

| Kind | Path / pointer | Present? |
|---|---|---|
| This QA pack | `ops/earn/gumroad-draft-qa-20260916/` | this PR |
| SKU-0 starter-intake pack | — | **missing** |
| QUEUE placeholder `earn-packs/gumroad/` | listed as missing in [PR#14](https://github.com/rimone0511/autopilot-log/pull/14) INDEX | **missing** |
| Live product URL `gumroad.com/l/...` | — | **not in repo** (do not invent) |
| Permalink token | `{{GUMROAD_PERMALINK_SKU0}}` (local only, if a later pack uses it) | token only |
| Price token | `{{PRICE_USD_SKU0}}` (named in SKU-1 PRICING as living in the SKU-0 pack) | token only; pack missing |

Sibling **SKU-1 / SKU-2 / SKU-3** paste packs exist as draft PRs. They are **not**
this look-pass target. Do not treat them as a live Gumroad SKU-0, and do not
publish them from this pack.

| Sibling (paste only) | Path (on that PR branch, not `master`) | PR |
|---|---|---|
| SKU-1 n8n inquiry classifier | `earn-sku1-n8n-pack-draft-20260916/` | [#37](https://github.com/rimone0511/autopilot-log/pull/37) |
| SKU-2 n8n approval-gated notify | `earn-sku2-approval-gate-pack-draft-20260916/` | [#46](https://github.com/rimone0511/autopilot-log/pull/46) |
| SKU-3 n8n Google Sheet sync | `earn-sku3-sheet-sync-pack-draft-20260916/` | [#52](https://github.com/rimone0511/autopilot-log/pull/52) |

SKU-1 describes SKU-0 as the predecessor: **form → table → notify**, unpublished.
That description is the only in-repo product shape for SKU-0. There is no listing
paste, buyer zip, or cover file to diff against until a SKU-0 pack exists.

## Related earn-ops (desk state, not product URLs)

| Pack | Path (on that PR branch) | PR |
|---|---|---|
| Register QUEUE | `earn-register-expand-20260916/QUEUE.md` — Gumroad A+ `done-draft` | [#1](https://github.com/rimone0511/autopilot-log/pull/1) |
| Wave A STATUS snapshot | `earn-register-status-snapshot-20260916-0519/STATUS.md` — Gumroad `draft_saved` | [#49](https://github.com/rimone0511/autopilot-log/pull/49) |
| Morning KYC slip (Gumroad) | `earn-morning-kyc-slip-refresh-20260916/06-gumroad.md` — unpublished; no payout this pass | [#43](https://github.com/rimone0511/autopilot-log/pull/43) |

## Official help (public)

- Adding a product: https://gumroad.com/help/article/149-adding-a-product
- Cover and thumbnail: https://gumroad.com/help/article/60-adding-a-cover-image
- Getting paid (read only; do not set up): https://gumroad.com/help/article/13-getting-paid
- Payout settings (read only; do not fill): https://gumroad.com/help/article/260-your-payout-settings-page

Public site (not a product URL): https://gumroad.com/

## Verification of this PR

Markdown only. Python posting-gate tests are unchanged. No Gumroad product was
opened, created, or published from this agent. No payout method was added.
