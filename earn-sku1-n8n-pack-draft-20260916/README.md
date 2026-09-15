# SKU-1 n8n pack — DRAFT (unpublished)

Pack date: 2026-09-16
Desk: Gumroad (Wave A+ in the 2026-09-16 earn-ops queue; login is `done-draft`)
Product code: **SKU-1**
Predecessor: **SKU-0** (Gumroad starter intake pack — form → table → notify, unpublished)
Mode: **DRAFT_ONLY — do not publish on Gumroad**

These files are a digital-product **draft** for a second n8n automation pack.
They are not a live Gumroad listing, not a payout setup, and not a claim of
employment or partnership with n8n, xAI, OpenAI, Google, or Gumroad.

## What SKU-1 is

SKU-0 (separate pack) is the starter: intake lands in a table, a person sends.

SKU-1 is the next download: **inquiry classifier**. Inbound text is mapped onto
labels the buyer already uses. Anything unclear goes to **uncertain / hold**.
Nothing is auto-replied, auto-charged, or posted in the buyer’s name.

## Hard rules

- No secrets in these files or in git (no real passwords, API keys, IDs, tax numbers).
- Use PLACEHOLDER tokens only (example: `{{EMAIL}}`).
- **Do not publish.** Leave the Gumroad product unpublished / draft.
- Do not click Gumroad **Publish** / **Enable** / go-live on a custom permalink.
- Stop before payout, bank, tax forms, or identity upload. See [DRAFT_ONLY.md](DRAFT_ONLY.md).
- No fake n8n / lab / Gumroad partnership badges.
- Do not invent sales counts, GMV, accuracy %, or time saved.
- Do not create or publish the Gumroad product from an agent browser session.

## Files

| File | Audience | Purpose |
|---|---|---|
| [BUYER-README.md](BUYER-README.md) | Buyer (zip contents) | How to import stubs, replace placeholders, keep send human |
| [LISTING-EN.md](LISTING-EN.md) | Operator paste | Gumroad listing copy (English) |
| [LISTING-JA.md](LISTING-JA.md) | Operator paste | Gumroad listing copy (Japanese) |
| [PRICING.md](PRICING.md) | Operator | Price placeholders only — not a live price |
| [DRAFT_ONLY.md](DRAFT_ONLY.md) | Operator | Unpublished / no live Gumroad / no secrets |
| [credentials.placeholders.json](credentials.placeholders.json) | Buyer stub | Credential *names* only; empty secrets |
| [stubs/sku1-inquiry-classifier.stub.json](stubs/sku1-inquiry-classifier.stub.json) | Buyer stub | Inactive classifier graph |
| [stubs/sku1-hold-queue.stub.json](stubs/sku1-hold-queue.stub.json) | Buyer stub | Inactive hold / operator-notify graph |

Buyer zip (when a **human** later ships this product — not this PR):

- `BUYER-README.md`
- `credentials.placeholders.json`
- `stubs/*.stub.json`

Do not zip operator files (`README.md`, listings, `DRAFT_ONLY.md`, `PRICING.md`)
into a customer download.

## Shared placeholders

Replace locally. Never commit filled values.

```
{{FULL_LEGAL_NAME}}
{{DISPLAY_NAME}}
{{EMAIL}}
{{GOOGLE_ACCOUNT_EMAIL}}
{{PASSWORD_DO_NOT_STORE}}
{{COUNTRY}}
{{GUMROAD_PERMALINK_SKU1}}
{{PRICE_USD}}
{{PRICE_JPY_DISPLAY}}
{{N8N_BASE_URL}}
{{WEBHOOK_PATH_SKU1}}
{{OPERATOR_NOTIFY_CHANNEL}}
{{N8N_NOTIFY_CREDENTIAL_NAME}}
{{TABLE_KIND}}
{{TABLE_ID_DO_NOT_COMMIT}}
{{SHEET_NAME}}
{{PORTFOLIO_URL}}
{{WEBSITE_URL}}
```

Suggested public URLs (already public; still not a live Gumroad product URL):

- Site: `https://yutalab.dev/`
- Tooling example: `https://github.com/rimone0511/autopilot-log`
- n8n import help: `https://docs.n8n.io/build/manage-workflows/export-and-import/`
- Gumroad add-product help: `https://gumroad.com/help/article/149-adding-a-product`

Do not type a real phone, ID number, tax ID, webhook secret, or n8n API key into git.

## Activity note

Gumroad creator login is already `done-draft` on the 2026-09-16 queue (MAIN Google).
This pack does **not** change that state to published.

Evidence from public pages (no GMV invented):

- Help: https://gumroad.com/help/article/149-adding-a-product (New product, price, description, content pages, versions)
- n8n import: https://docs.n8n.io/build/manage-workflows/export-and-import/ (Import from File; JSON may carry credential *names*)

## Official help used for this pack

- Adding a product: https://gumroad.com/help/article/149-adding-a-product
- n8n export and import: https://docs.n8n.io/build/manage-workflows/export-and-import/
- n8n sticky-note / editor: buyer rebuilds nodes if a stub fails to import on their version
