# SKU-3 n8n pack — DRAFT (unpublished)

Pack date: 2026-09-16
Desk: Gumroad (Wave A+ in the 2026-09-16 earn-ops queue; login is `done-draft`)
Product code: **SKU-3**
Predecessor: **SKU-2** (Gumroad approval-gated notify pack — human must approve first, unpublished)
Mode: **DRAFT_ONLY — do not publish on Gumroad**

These files are a digital-product **draft** for a fourth n8n automation pack
(after SKU-0 starter intake, SKU-1 classifier, and SKU-2 approval gate).
They are not a live Gumroad listing, not a payout setup, and not a claim of
employment or partnership with n8n, xAI, OpenAI, Google, Slack, or Gumroad.

## What SKU-3 is

SKU-0 (separate pack) is the starter: intake lands in a table, a person sends.

SKU-1 (separate pack) is the classifier: inbound text gets a label; unclear
text goes to **uncertain / hold**.

SKU-2 (separate pack) is the approval gate: a draft outbound sits until a
**human approves**. Timeout is not approve.

SKU-3 is the next download: **Google Sheet sync**. A new inbound row (sheet
or a webhook that stands in for one) **notifies a human**. Nothing is
auto-sent — no mail, chat blast, invoice, or public post from these stubs.

## Hard rules

- No secrets in these files or in git (no real passwords, API keys, IDs, tax numbers, sheet IDs).
- Use PLACEHOLDER tokens only (example: `{{EMAIL}}`).
- **Do not publish.** Leave the Gumroad product unpublished / draft.
- Do not click Gumroad **Publish** / **Enable** / go-live on a custom permalink.
- Stop before payout, bank, tax forms, or identity upload. See [DRAFT_ONLY.md](DRAFT_ONLY.md).
- No fake n8n / lab / Google / Gumroad partnership badges.
- Do not invent sales counts, GMV, delivery-time SLAs, or “rows processed” stats.
- Do not create or publish the Gumroad product from an agent browser session.
- Do not attach a live Google Sheets credential or turn stubs **Active**.

## Files

| File | Audience | Purpose |
|---|---|---|
| [BUYER-README.md](BUYER-README.md) | Buyer (zip contents) | How to import stubs, replace placeholders, keep send human |
| [LISTING-EN.md](LISTING-EN.md) | Operator paste | Gumroad listing copy (English) |
| [LISTING-JA.md](LISTING-JA.md) | Operator paste | Gumroad listing copy (Japanese) |
| [PRICING.md](PRICING.md) | Operator | Price placeholders only — not a live price |
| [DRAFT_ONLY.md](DRAFT_ONLY.md) | Operator | Unpublished / no live Gumroad / no secrets |
| [credentials.placeholders.json](credentials.placeholders.json) | Buyer stub | Credential *names* only; empty secrets |
| [stubs/sku3-sheet-inbound.stub.json](stubs/sku3-sheet-inbound.stub.json) | Buyer stub | Inactive inbound-row hold graph (no send) |
| [stubs/sku3-human-notify.stub.json](stubs/sku3-human-notify.stub.json) | Buyer stub | Inactive human-notify graph; outbound is NoOp |

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
{{GUMROAD_PERMALINK_SKU3}}
{{PRICE_USD}}
{{PRICE_JPY_DISPLAY}}
{{N8N_BASE_URL}}
{{WEBHOOK_PATH_SKU3}}
{{WEBHOOK_PATH_SKU3_NOTIFY}}
{{OPERATOR_NOTIFY_CHANNEL}}
{{N8N_NOTIFY_CREDENTIAL_NAME}}
{{GOOGLE_SHEETS_CREDENTIAL_NAME}}
{{GOOGLE_SHEET_ID_DO_NOT_COMMIT}}
{{SHEET_NAME}}
{{ROW_EVENT}}
{{TABLE_KIND}}
{{TABLE_ID_DO_NOT_COMMIT}}
{{PORTFOLIO_URL}}
{{WEBSITE_URL}}
```

Suggested public URLs (already public; still not a live Gumroad product URL):

- Site: `https://yutalab.dev/`
- Tooling example: `https://github.com/rimone0511/autopilot-log`
- n8n import help: `https://docs.n8n.io/build/manage-workflows/export-and-import/`
- n8n Google Sheets Trigger (optional later; stubs use a webhook stand-in): `https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.googlesheetstrigger/`
- n8n Google Sheets node: `https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/`
- n8n Google credentials: `https://docs.n8n.io/integrations/builtin/credentials/google/`
- Gumroad add-product help: `https://gumroad.com/help/article/149-adding-a-product`

Do not type a real phone, ID number, tax ID, webhook secret, n8n API key,
Google client secret, or spreadsheet ID into git.

## Activity note

Gumroad creator login is already `done-draft` on the 2026-09-16 queue (MAIN Google).
This pack does **not** change that state to published.

Evidence from public pages (no GMV invented):

- Help: https://gumroad.com/help/article/149-adding-a-product (New product, price, description, content pages, versions)
- n8n import: https://docs.n8n.io/build/manage-workflows/export-and-import/ (Import from File; JSON may carry credential *names*)
- n8n Google Sheets Trigger: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.googlesheetstrigger/ (row added / updated; buyer owns the credential)
- n8n Google credentials: https://docs.n8n.io/integrations/builtin/credentials/google/ (OAuth or service account created in the buyer’s n8n, not in this zip)

## Official help used for this pack

- Adding a product: https://gumroad.com/help/article/149-adding-a-product
- n8n export and import: https://docs.n8n.io/build/manage-workflows/export-and-import/
- n8n Google Sheets Trigger: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.googlesheetstrigger/
- n8n Google Sheets: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/
- n8n Google credentials: https://docs.n8n.io/integrations/builtin/credentials/google/
- n8n sticky-note / editor: buyer rebuilds nodes if a stub fails to import on their version
