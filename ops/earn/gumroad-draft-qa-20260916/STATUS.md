# STATUS — Gumroad SKU-0 draft QA

Pack date: **2026-09-16**  
Folder: `ops/earn/gumroad-draft-qa-20260916/`  
State: **DRAFT_ONLY — look-don't-ship pack landed; live look-pass not run**

Desk: Gumroad (Wave A+). Queue `done-draft`. CU hint `draft_saved`. Does not
occupy CU-11.

This file is the status of **this QA pack**, not a signup log and not a live
Gumroad product page.

Forbidden in this PR: secrets, product permalinks invented for git, payout
setup, Publish / Enable, New product, KYC upload, GMV.

---

## Verdict

| Item | Status |
|---|---|
| This checklist pack | **ready · draft** (markdown only) |
| Live SKU-0 look-pass (title / price / icons / files) | **not run** from this agent |
| SKU-0 product pack in repo | **missing** |
| Live `gumroad.com/l/...` URL in repo | **missing** (do not invent) |
| Gumroad desk | **`draft_saved`** — leave unpublished |
| Payout / KYC | **not this pack** — do not open |

---

## What exists

In **this** PR:

- [CHECKLIST.md](CHECKLIST.md) — look-don't-ship for an existing unpublished SKU
  (title, price, cover/thumbnail, content files)
- [GAPS.md](GAPS.md) — empty template; repo-side SKU-0 rows already `missing`
- [README.md](README.md) — path map and hard rules

On the earn-ops desk (sibling PRs; bodies not copied):

- Gumroad login `done-draft` — [PR#1](https://github.com/rimone0511/autopilot-log/pull/1) QUEUE A+
- Gumroad `draft_saved` — [PR#49](https://github.com/rimone0511/autopilot-log/pull/49)
- Gumroad KYC slip: unpublished; payout only when a human is actually withdrawing
  — [PR#43](https://github.com/rimone0511/autopilot-log/pull/43) `06-gumroad.md`

SKU-0 **shape** (the only in-repo description): starter intake, form → table →
notify, unpublished. Source: SKU-1 pack text on
[PR#37](https://github.com/rimone0511/autopilot-log/pull/37)
(`earn-sku1-n8n-pack-draft-20260916/`). That folder is not SKU-0.

---

## What does not exist (do not invent)

| Missing | Do not |
|---|---|
| `earn-sku0-*` / `ops/earn/sku-0*` pack | Invent listing paste, buyer zip, or cover files |
| `earn-packs/gumroad/` | Treat the INDEX placeholder as a real pack ([PR#14](https://github.com/rimone0511/autopilot-log/pull/14)) |
| Product URL | Write `gumroad.com/l/...` or enable a permalink |
| Filled `{{PRICE_USD_SKU0}}` | Commit a USD/JPY number |
| Live look-pass ticks | Claim title/price/icons/files were inspected from this agent |

Sibling SKU-1 / SKU-2 / SKU-3 folders are **other unpublished paste packs**:

| SKU | Path (PR branch) | PR |
|---|---|---|
| SKU-1 | `earn-sku1-n8n-pack-draft-20260916/` | [#37](https://github.com/rimone0511/autopilot-log/pull/37) |
| SKU-2 | `earn-sku2-approval-gate-pack-draft-20260916/` | [#46](https://github.com/rimone0511/autopilot-log/pull/46) |
| SKU-3 | `earn-sku3-sheet-sync-pack-draft-20260916/` | [#52](https://github.com/rimone0511/autopilot-log/pull/52) |

Do not QA-publish those from this pack. Do not attach their stubs to SKU-0.

---

## Next (human)

1. Keep Gumroad **unpublished**. No Publish / Enable.
2. Optional look-pass with [CHECKLIST.md](CHECKLIST.md). Fill a local [GAPS.md](GAPS.md).
3. If no unpublished SKU-0 draft exists: stop. Do not create it from this pack.
4. Do not set up payout. Do not upload ID.
5. A SKU-0 **product pack** is a separate earn-ops task. This QA pack is not that pack.
6. Next CU is **not** Gumroad (desk stays `draft_saved`).

---

## This PR does not

- Publish or enable a Gumroad product
- Create a Gumroad product or attach files / covers
- Set up payout, bank, tax, or identity
- Invent a product URL
- Copy sibling PR listing bodies into a fake SKU-0 pack
- Change Python posting-gate tests
- Claim the live title / price / icons / files were verified
