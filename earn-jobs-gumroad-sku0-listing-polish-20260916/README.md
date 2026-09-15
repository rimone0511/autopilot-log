# SKU-0 listing polish — JOBS PHASE (DRAFT_ONLY)

Pack date: 2026-09-16
Phase: **JOBS** (listing copy, not a live desk walk)
Desk: Gumroad
Product: **SKU-0** — starter intake (form → table → notify)
Mode: **DRAFT_ONLY — do not publish, do not set up payout**

These files polish the **unpublished** Gumroad digital-product listing for SKU-0.
They are not a live product, not a buyer zip, not payout/KYC, and not a claim of
partnership with n8n, Gumroad, Google, or any AI lab.

Sibling earn-ops packs (do not merge their jobs into this folder):

| Pack | Path / PR | Role |
|---|---|---|
| Look-don't-ship QA | `ops/earn/gumroad-draft-qa-20260916/` [#55](https://github.com/rimone0511/autopilot-log/pull/55) | Title / price / icons / files **look** |
| 2-minute parent card | `ops/earn/gumroad-look-dont-ship-20260916/` [#63](https://github.com/rimone0511/autopilot-log/pull/63) | Title / price / icons only |
| SKU-1 classifier | `earn-sku1-n8n-pack-draft-20260916/` [#37](https://github.com/rimone0511/autopilot-log/pull/37) | Next SKU, unpublished |
| SKU-2 approval gate | `earn-sku2-approval-gate-pack-draft-20260916/` [#46](https://github.com/rimone0511/autopilot-log/pull/46) | Next SKU, unpublished |
| SKU-3 sheet sync | `earn-sku3-sheet-sync-pack-draft-20260916/` [#52](https://github.com/rimone0511/autopilot-log/pull/52) | Next SKU, unpublished |

This JOBS pack **authors the listing paste that those QA packs noted was missing**.
It does **not** attach Content-tab files, covers, or n8n stubs.

## What SKU-0 is

Starter intake you run on **your** n8n: a form (or webhook you already own) writes
a row to a table you control; a notify stub pings a person; **you** send.

It is not SKU-1 (classifier), not SKU-2 (approval gate), not SKU-3 (sheet sync).
Nothing auto-replies, auto-invoices, or posts in the buyer’s name.

## Files

| File | Audience | Purpose |
|---|---|---|
| [LISTING-EN.md](LISTING-EN.md) | Operator paste | Gumroad listing copy (English) |
| [LISTING-JA.md](LISTING-JA.md) | Operator paste | Gumroad listing copy (Japanese) |
| [FAQ-EN.md](FAQ-EN.md) | Operator paste / buyer-facing | Buyer FAQ (English), for the description |
| [FAQ-JA.md](FAQ-JA.md) | Operator paste / buyer-facing | Buyer FAQ (Japanese), for the description |
| [PRICING.md](PRICING.md) | Operator | Keep **$39** if already on the draft, else `{{PRICE}}` |
| [CHECKLIST.md](CHECKLIST.md) | Operator | Gate **before** Publish — this pack still does not publish |
| [DRAFT_ONLY.md](DRAFT_ONLY.md) | Operator | Unpublished / no payout / no secrets |
| [STATUS.md](STATUS.md) | Operator | Pack status; desk stays unpublished |

Do **not** zip operator files into a customer download.

## Hard rules

- No secrets in these files or in git (no real passwords, API keys, IDs, tax numbers).
- Use PLACEHOLDER tokens only (example: `{{EMAIL}}`, `{{PRICE}}`).
- **Do not publish.** Leave the Gumroad product unpublished / draft.
- Do not click Gumroad **Publish** / **Enable** / go-live on a custom permalink.
- Stop before payout, bank, tax forms, or identity upload.
- No fake n8n / lab / Gumroad partnership badges.
- Do not invent sales counts, GMV, accuracy %, or time saved.
- Do not create a second product if an unpublished SKU-0 draft already exists.
- Do not announce a live `gumroad.com/l/...` URL.

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

`{{PRICE}}` and `{{PRICE_USD_SKU0}}` are the same slot. See [PRICING.md](PRICING.md).

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

## Verification of this PR

Markdown only. Python posting-gate tests are unchanged. No Gumroad product was
opened, created, or published from this agent. No payout method was added.
