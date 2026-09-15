# STATUS — Gumroad look-don't-ship parent card

Pack date: **2026-09-16**  
Folder: `ops/earn/gumroad-look-dont-ship-20260916/`  
State: **DRAFT_ONLY — 2-minute parent card landed; live look-pass not run**

Desk: Gumroad (Wave A+). Queue `done-draft`. CU hint `draft_saved`. Does not
occupy CU-11.

This file is the status of **this parent operator card**, not a signup log and
not a live Gumroad product page. Audience is the parent operator (祐太), not CU.

Forbidden in this PR: secrets, product permalinks invented for git, payout
setup, Publish / Enable, New product, KYC upload, GMV, Content-tab file QA.

---

## Verdict

| Item | Status |
|---|---|
| This 2-minute parent card (title / price / icons) | **ready · draft** (markdown only) |
| Live SKU-0 look-pass (title / price / icons) | **not run** from this agent |
| Content-tab files look-pass | **out of scope** (sibling QA pack) |
| SKU-0 product pack in repo | **missing** |
| Live `gumroad.com/l/...` URL in repo | **missing** (do not invent) |
| Gumroad desk | **`draft_saved`** — leave unpublished |
| Payout / KYC | **not this pack** — do not open |
| CU on this desk | **do not open** — parent card only |

---

## What exists

In **this** PR:

- [OPERATOR-CARD.md](OPERATOR-CARD.md) — 2-minute look-don't-ship for title,
  price, and icons (cover / thumbnail) on an existing unpublished SKU
- [STATUS.md](STATUS.md) — this file

On the earn-ops desk (sibling PRs; bodies not copied):

| Pack | Path (on that PR branch) | PR |
|---|---|---|
| Full QA (title / price / icons / **files**) | `ops/earn/gumroad-draft-qa-20260916/` | [#55](https://github.com/rimone0511/autopilot-log/pull/55) |
| Register QUEUE | Gumroad A+ `done-draft` | [#1](https://github.com/rimone0511/autopilot-log/pull/1) |
| Wave A morning-loop STATUS | Gumroad `draft_saved` | [#54](https://github.com/rimone0511/autopilot-log/pull/54) |
| Morning KYC slip (Gumroad) | unpublished; no payout this pass | [#43](https://github.com/rimone0511/autopilot-log/pull/43) |

SKU-0 **shape** (the only in-repo product description): starter intake,
form → table → notify, unpublished. Source: SKU-1 pack text on
[PR#37](https://github.com/rimone0511/autopilot-log/pull/37). That folder is
not SKU-0.

---

## What does not exist (do not invent)

| Missing | Do not |
|---|---|
| `earn-sku0-*` / `ops/earn/sku-0*` pack | Invent listing paste, buyer zip, or cover files |
| `earn-packs/gumroad/` | Treat the INDEX placeholder as a real pack ([PR#14](https://github.com/rimone0511/autopilot-log/pull/14)) |
| Product URL | Write `gumroad.com/l/...` or enable a permalink |
| Filled `{{PRICE_USD_SKU0}}` | Commit a USD/JPY number |
| Live look-pass ticks | Claim title / price / icons were inspected from this agent |

Sibling SKU-1 / SKU-2 / SKU-3 folders are **other unpublished paste packs**:

| SKU | Path (PR branch) | PR |
|---|---|---|
| SKU-1 | `earn-sku1-n8n-pack-draft-20260916/` | [#37](https://github.com/rimone0511/autopilot-log/pull/37) |
| SKU-2 | `earn-sku2-approval-gate-pack-draft-20260916/` | [#46](https://github.com/rimone0511/autopilot-log/pull/46) |
| SKU-3 | `earn-sku3-sheet-sync-pack-draft-20260916/` | [#52](https://github.com/rimone0511/autopilot-log/pull/52) |

Do not QA-publish those from this card. Do not attach their stubs to SKU-0.

---

## Next (parent)

1. Keep Gumroad **unpublished**. No Publish / Enable.
2. Optional 2-minute look with [OPERATOR-CARD.md](OPERATOR-CARD.md). Keep live
   strings local.
3. If no unpublished SKU-0 draft exists: stop. Do not create it from this card.
4. Files / Content tab: later, sibling [PR#55](https://github.com/rimone0511/autopilot-log/pull/55) — not this card.
5. Do not set up payout. Do not upload ID.
6. A SKU-0 **product pack** is a separate earn-ops task. This card is not that pack.
7. Next CU is **not** Gumroad (desk stays `draft_saved`). CU does not run this card.

---

## This PR does not

- Publish or enable a Gumroad product
- Create a Gumroad product or attach files / covers
- Open or QA the Content tab
- Set up payout, bank, tax, or identity
- Invent a product URL
- Copy sibling PR listing bodies into a fake SKU-0 pack
- Change Python posting-gate tests
- Claim the live title / price / icons were verified
- Send a CU agent to Gumroad
