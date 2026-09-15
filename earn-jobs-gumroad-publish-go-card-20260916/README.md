# SKU-0 Publish GO card — JOBS PHASE (DRAFT_ONLY)

Pack date: 2026-09-16
Phase: **JOBS** (parent 2-minute GO / NO-GO, not a live desk walk)
Desk: Gumroad
Product: **SKU-0** — starter intake (form → table → notify)
Audience: **parent operator only** (祐太). Not computer-use.
Mode: **DRAFT_ONLY — default is DO NOT PUBLISH. Do not set up payout.**

This folder is a **2-minute parent GO card** that runs **after** the listing-polish
paste pack ([PR#74](https://github.com/rimone0511/autopilot-log/pull/74)). It tells
the human what to look at before any later Publish on the unpublished Gumroad
SKU-0 draft. It is not a live product, not a buyer zip, not listing paste, not
payout/KYC, and not permission to click Publish.

Assumed live draft shape (look; do not invent a URL):

- Content-tab **files attached**
- Price **$39** USD, pay-what-you-want **off**
- **Unpaid draft** (unpublished; no payout set up from this card)

Even if those three look green, this card’s GO is **NO**. Green checks are
preconditions, not a go-live.

## Sibling packs (do not merge their jobs into this folder)

| Pack | Path / PR | Role |
|---|---|---|
| Listing polish EN+JA | `earn-jobs-gumroad-sku0-listing-polish-20260916/` [#74](https://github.com/rimone0511/autopilot-log/pull/74) | Paste name / summary / description / FAQ / price rule |
| Look-don't-ship QA | `ops/earn/gumroad-draft-qa-20260916/` [#55](https://github.com/rimone0511/autopilot-log/pull/55) | Title / price / icons / files **look** |
| 2-minute look card | `ops/earn/gumroad-look-dont-ship-20260916/` [#63](https://github.com/rimone0511/autopilot-log/pull/63) | Title / price / icons only (no files, no GO) |
| SKU-1 classifier | `earn-sku1-n8n-pack-draft-20260916/` [#37](https://github.com/rimone0511/autopilot-log/pull/37) | Next SKU, unpublished |
| SKU-2 approval gate | `earn-sku2-approval-gate-pack-draft-20260916/` [#46](https://github.com/rimone0511/autopilot-log/pull/46) | Next SKU, unpublished |
| SKU-3 sheet sync | `earn-sku3-sheet-sync-pack-draft-20260916/` [#52](https://github.com/rimone0511/autopilot-log/pull/52) | Next SKU, unpublished |

This JOBS pack does **not** re-author listing paste. Use [#74](https://github.com/rimone0511/autopilot-log/pull/74) for that.
It does **not** upload Content-tab files, covers, or n8n stubs.

## What SKU-0 is

Starter intake you run on **your** n8n: a form (or webhook you already own) writes
a row to a table you control; a notify stub pings a person; **you** send.

It is not SKU-1 (classifier), not SKU-2 (approval gate), not SKU-3 (sheet sync).
Nothing auto-replies, auto-invoices, or posts in the buyer’s name.

## Files

| File | Audience | Purpose |
|---|---|---|
| [OPERATOR-CARD.md](OPERATOR-CARD.md) | Parent | 2-minute GO clock: files / $39 / unpaid draft. Default **NO** |
| [GO.md](GO.md) | Parent | One-page verdict. This pack never emits YES |
| [DRAFT_ONLY.md](DRAFT_ONLY.md) | Operator | Unpublished / no Publish / no secrets / no payout |
| [STATUS.md](STATUS.md) | Operator | Pack status; desk stays unpublished |

Do **not** zip operator files into a customer download.

## Hard rules

- No secrets in these files or in git (no real passwords, API keys, IDs, tax numbers).
- Use PLACEHOLDER tokens only (example: `{{EMAIL}}`, `{{PRICE}}`).
- **Do not publish.** Default GO is **NO**. Leave the Gumroad product unpublished / draft.
- Do not click Gumroad **Publish** / **Enable** / go-live on a custom permalink.
- Do not treat “files attached + $39” as permission to ship an unpaid draft.
- Stop before payout, bank, tax forms, or identity upload.
- No fake n8n / lab / Gumroad partnership badges.
- Do not invent sales counts, GMV, accuracy %, or time saved.
- Do not create a second product if an unpublished SKU-0 draft already exists.
- Do not announce a live `gumroad.com/l/...` URL.
- CU does **not** open Gumroad from this card.

## Shared placeholders

Replace locally. Never commit filled values.

```
{{FULL_LEGAL_NAME}}
{{DISPLAY_NAME}}
{{EMAIL}}
{{GOOGLE_ACCOUNT_EMAIL}}
{{PASSWORD_DO_NOT_STORE}}
{{COUNTRY}}
{{GUMROAD_PERMALINK_SKU0}}
{{PRICE}}
{{PRICE_USD_SKU0}}
{{PRICE_JPY_DISPLAY}}
{{N8N_BASE_URL}}
{{WEBHOOK_PATH_SKU0}}
{{OPERATOR_NOTIFY_CHANNEL}}
{{N8N_NOTIFY_CREDENTIAL_NAME}}
{{TABLE_KIND}}
{{TABLE_ID_DO_NOT_COMMIT}}
{{SHEET_NAME}}
{{FORM_KIND}}
{{PORTFOLIO_URL}}
{{WEBSITE_URL}}
```

`{{PRICE}}` and `{{PRICE_USD_SKU0}}` are the same slot. On this card the look-target
is **$39 already on the draft**. Do not commit a filled number.

Suggested public URLs (already public; still not a live Gumroad product URL):

- Site: `https://yutalab.dev/`
- Tooling example: `https://github.com/rimone0511/autopilot-log`
- n8n import help: `https://docs.n8n.io/build/manage-workflows/export-and-import/`
- Gumroad add-product help: `https://gumroad.com/help/article/149-adding-a-product`

Do not type a real phone, ID number, tax ID, webhook secret, or n8n API key into git.

## Official help used

- Adding a product: https://gumroad.com/help/article/149-adding-a-product
- Cover and thumbnail: https://gumroad.com/help/article/60-adding-a-cover-image
- Getting paid (read only; do not set up): https://gumroad.com/help/article/13-getting-paid
- n8n export and import: https://docs.n8n.io/build/manage-workflows/export-and-import/

Public site (not a product URL): https://gumroad.com/

## Activity note

Gumroad creator login is already `done-draft` on the 2026-09-16 queue (MAIN Google).
Desk stays `draft_saved`. This pack does **not** change that state to published.
This pack does not occupy a CU slot.

## Verification of this PR

Markdown only. Python posting-gate tests are unchanged. No Gumroad product was
opened, created, or published from this agent. No payout method was added.
No live `gumroad.com/l/...` URL was written.
