# STATUS — Gumroad SKU-0 Publish GO card (JOBS)

Pack date: **2026-09-16**
Folder: `earn-jobs-gumroad-publish-go-card-20260916/`
State: **DRAFT_ONLY — 2-minute parent GO card landed; live look-pass not run; GO = NO**

Desk: Gumroad (Wave A+). Queue `done-draft`. CU hint `draft_saved`.
This JOBS pack does not occupy a CU slot and does not walk the live editor.

Forbidden in this PR: secrets, product permalinks invented for git, payout
setup, Publish / Enable, New product, KYC upload, GMV, a YES verdict.

---

## Verdict

| Item | Status |
|---|---|
| This 2-minute parent GO card | **ready · draft** (markdown only) |
| GO | **NO** (pack default; not flipped by files + $39) |
| Live SKU-0 GO look-pass (files / $39 / unpaid draft) | **not run** from this agent |
| Listing polish paste | sibling [#74](https://github.com/rimone0511/autopilot-log/pull/74) — not re-authored here |
| Live Gumroad session | **not opened** from this agent |
| Live `gumroad.com/l/...` URL in repo | **missing** (do not invent) |
| Gumroad desk | **`draft_saved`** — leave unpublished |
| Payout / KYC | **not this pack** — do not open |
| CU on this desk | **do not open** — parent card only |

Look-targets (human, later, still not Publish):

| Look | Target |
|---|---|
| Files | Content-tab buyer files **attached** |
| Price | **$39** USD, PWYW off |
| Draft | **Unpaid** unpublished draft |

---

## What exists

In **this** PR:

- [OPERATOR-CARD.md](OPERATOR-CARD.md) — 2-minute GO clock (files / $39 / unpaid draft)
- [GO.md](GO.md) — one-page verdict; never emits YES
- [DRAFT_ONLY.md](DRAFT_ONLY.md) — unpublished / no payout / no secrets
- [STATUS.md](STATUS.md) — this file
- [README.md](README.md) — path map and hard rules

On the earn-ops / earn-jobs desk (sibling PRs; bodies not copied):

| Pack | Path (on that PR branch) | PR |
|---|---|---|
| Listing polish EN+JA | `earn-jobs-gumroad-sku0-listing-polish-20260916/` | [#74](https://github.com/rimone0511/autopilot-log/pull/74) |
| Full QA (title / price / icons / **files**) | `ops/earn/gumroad-draft-qa-20260916/` | [#55](https://github.com/rimone0511/autopilot-log/pull/55) |
| 2-minute look (title / price / icons only) | `ops/earn/gumroad-look-dont-ship-20260916/` | [#63](https://github.com/rimone0511/autopilot-log/pull/63) |
| Register QUEUE | Gumroad A+ `done-draft` | [#1](https://github.com/rimone0511/autopilot-log/pull/1) |
| Wave A morning-loop STATUS | Gumroad `draft_saved` | [#54](https://github.com/rimone0511/autopilot-log/pull/54) |
| Morning KYC slip (Gumroad) | unpublished; no payout this pass | [#43](https://github.com/rimone0511/autopilot-log/pull/43) |

SKU-0 **shape** (in-repo product description): starter intake, form → table →
notify, unpublished. Listing paste: [#74](https://github.com/rimone0511/autopilot-log/pull/74).
Predecessor shape source: SKU-1 pack text on
[PR#37](https://github.com/rimone0511/autopilot-log/pull/37). That folder is
not SKU-0.

---

## What does not exist (do not invent)

| Missing | Do not |
|---|---|
| YES on [GO.md](GO.md) | Authorize Publish from this card |
| `earn-sku0-*` / `ops/earn/sku-0*` buyer-zip pack | Invent or attach Content-tab files from this agent |
| Product URL | Write `gumroad.com/l/...` or enable a permalink |
| Filled `{{PRICE_USD_SKU0}}` | Commit a USD/JPY number (look-target is keep $39) |
| Live GO-pass ticks | Claim files / $39 / unpaid draft were inspected from this agent |
| Payout method | Open bank / tax / ID |

Sibling SKU-1 / SKU-2 / SKU-3 folders are **other unpublished paste packs**:

| SKU | Path (PR branch) | PR |
|---|---|---|
| SKU-1 | `earn-sku1-n8n-pack-draft-20260916/` | [#37](https://github.com/rimone0511/autopilot-log/pull/37) |
| SKU-2 | `earn-sku2-approval-gate-pack-draft-20260916/` | [#46](https://github.com/rimone0511/autopilot-log/pull/46) |
| SKU-3 | `earn-sku3-sheet-sync-pack-draft-20260916/` | [#52](https://github.com/rimone0511/autopilot-log/pull/52) |

Do not QA-publish those from this card. Do not attach their stubs to SKU-0.

---

## Next (parent)

1. Keep Gumroad **unpublished**. No Publish / Enable. **GO = NO**.
2. Optional 2-minute GO look with [OPERATOR-CARD.md](OPERATOR-CARD.md). Keep live
   strings local. Write [GO.md](GO.md) locally as NO.
3. If no unpublished SKU-0 draft exists: stop. Do not create it from this card.
4. Listing paste: sibling [PR#74](https://github.com/rimone0511/autopilot-log/pull/74) — not this card.
5. Do not set up payout. Do not upload ID. Unpaid draft stays unpaid on this pass.
6. A human Publish pack is a **separate** earn-jobs task. This card is not that pack.
7. Next CU is **not** Gumroad (desk stays `draft_saved`). CU does not run this card.

---

## This PR does not

- Publish or enable a Gumroad product
- Create a Gumroad product or attach files / covers
- Open a live Gumroad session
- Set up payout, bank, tax, or identity
- Invent a product URL
- Copy sibling PR listing bodies into a fake SKU-0 pack
- Change Python posting-gate tests
- Claim the live files / $39 / unpaid-draft state were verified
- Emit GO = YES
- Send a CU agent to Gumroad
