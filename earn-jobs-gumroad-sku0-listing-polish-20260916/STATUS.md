# STATUS — Gumroad SKU-0 listing polish (JOBS)

Pack date: **2026-09-16**
Folder: `earn-jobs-gumroad-sku0-listing-polish-20260916/`
State: **DRAFT_ONLY — listing paste landed; product stays unpublished**

Desk: Gumroad (Wave A+). Queue `done-draft`. CU hint `draft_saved`.
This JOBS pack does not occupy a CU slot and does not walk the live editor.

Forbidden in this PR: secrets, product permalinks invented for git, payout
setup, Publish / Enable, New product, KYC upload, GMV.

## Verdict

| Item | Status |
|---|---|
| This listing-polish pack | **ready · draft** (markdown only) |
| EN listing paste | **ready** — [LISTING-EN.md](LISTING-EN.md) |
| JA listing paste | **ready** — [LISTING-JA.md](LISTING-JA.md) |
| Buyer FAQ EN+JA | **ready** — [FAQ-EN.md](FAQ-EN.md) / [FAQ-JA.md](FAQ-JA.md) |
| Price rule | **keep $39** if on the draft, else `{{PRICE}}` — [PRICING.md](PRICING.md) |
| Pre-publish checklist | **ready** — still **do not publish** from this pack |
| Live Gumroad paste | **not run** from this agent |
| Buyer zip / n8n stubs in this folder | **not this pack** (ship-blocker on [CHECKLIST.md](CHECKLIST.md) until a human attaches files) |
| Live `gumroad.com/l/...` URL in repo | **missing** (do not invent) |
| Gumroad desk | **`draft_saved`** — leave unpublished |
| Payout / KYC | **not this pack** — do not open |

## What this PR is

Polished unpublished listing copy for SKU-0 (form → table → notify), plus buyer
FAQ and a checklist a human must clear **before** any later Publish decision.

It fills the listing-paste gap called out by the look-don't-ship QA pack
([#55](https://github.com/rimone0511/autopilot-log/pull/55)).

## What this PR is not

| Missing / out of scope | Do not |
|---|---|
| n8n stub JSON / buyer zip | Author or attach Content-tab files from this agent |
| Cover / thumbnail binaries | Upload n8n or lab logos |
| Live look-pass ticks | Claim the Gumroad editor was opened from this agent |
| Publish | Click Publish / Enable |
| Payout | Open bank / tax / ID |

## Next (human)

1. Keep Gumroad **unpublished**. No Publish / Enable from this pack.
2. Optional: paste EN and/or JA listing + FAQ into the existing unpublished SKU-0.
3. Price: keep **$39** if already set; otherwise type a local `{{PRICE}}`.
4. Walk [CHECKLIST.md](CHECKLIST.md). Content files remain a ship-blocker until attached by a human.
5. Do not set up payout. Do not upload ID.
6. A later human Publish is a **separate** decision after every ship-blocker is green.

## This PR does not

- Publish or enable a Gumroad product
- Create a Gumroad product or attach files / covers
- Set up payout, bank, tax, or identity
- Invent a product URL
- Change Python posting-gate tests
- Claim the live title / price / icons / files were verified in the editor
