# n8n Inquiry Classifier Pack (SKU-1)

Buyer README — digital download
Status of these JSON files: **stubs / placeholders**. They are inactive on purpose.

This pack is **not** n8n Cloud hosting, not a managed service, and not an official
n8n product. You import the graphs into **your** n8n Cloud or self-hosted instance
and you enter credentials yourself.

## What you get

1. This README
2. `credentials.placeholders.json` — names of connections only. No secrets.
3. `stubs/sku1-inquiry-classifier.stub.json` — webhook → normalize → label → route
4. `stubs/sku1-hold-queue.stub.json` — uncertain / hold path; operator notify; **no send**

SKU-1 sits after a starter intake pack (SKU-0: form → table → notify). You do not
need SKU-0 installed. If you already have an intake table, point the classifier at
that table instead of inventing a second source of truth.

## What it is for

You receive short inbound text (form, help mailbox, or a webhook you already own).
You want a **label column** a person can check:

| Label | Meaning |
|---|---|
| `billing` | Invoice, receipt, payment status — still a person confirms amounts |
| `support` | How-to / breakage — still a person replies |
| `sales` | New work request — still a person decides |
| `uncertain` | Does not clearly match. **Hold.** Do not guess. |

The product is the **hold behavior**, not a promised accuracy number.

## What it deliberately does not do

- No auto-reply, auto-invoice, or auto-post in your name
- No browser automation, scraping, likes, follows, or views
- No storing of API keys, passwords, or customer PII in these files
- No guaranteed time saved, conversion rate, or classification accuracy
- No n8n hosting purchase and no partner badge

## Import (your n8n)

Official steps: [Export and import](https://docs.n8n.io/build/manage-workflows/export-and-import/)

1. Open **your** n8n. Do not import into a shared demo instance you do not control.
2. New workflow (or empty canvas) → three-dot menu → **Import from File**.
3. Import `sku1-inquiry-classifier.stub.json` first, then `sku1-hold-queue.stub.json`.
4. Confirm both workflows show **Inactive** / not production-active.
5. Replace every `{{PLACEHOLDER}}` in node parameters. Never paste real secrets into
   chat; create credentials inside n8n’s credential UI.
6. Run **one dummy payload** (no real customer names). Check: billing / support / sales
   routes, and an unclear payload lands on `uncertain`.
7. Only you turn a workflow on. If import fails on your n8n version, rebuild from the
   sticky notes on the canvas. Stubs are teaching graphs, not a version-locked product.

n8n’s own docs warn that workflow JSON can include **credential names**. These stubs
use fake names such as `{{N8N_NOTIFY_CREDENTIAL_NAME}}`. If you later export *your*
copy to share, strip names that identify a private system.

## Dummy payload (safe)

POST to the webhook path you set (`{{WEBHOOK_PATH_SKU1}}`). Example body — fictional:

```json
{
  "source": "form-stub",
  "subject": "EXAMPLE-ONLY — office hours",
  "body": "What time do you answer email?",
  "from_label": "example-sender"
}
```

Do not replay real customer mail into the first test.

## Operator loop (required)

1. Classifier writes a label (or `uncertain`).
2. Hold-queue stub is the place a person looks.
3. A person sends, closes, or relabels.
4. If a row would send money, publish, or delete data, the stub **stops**. Those
   nodes are NoOp placeholders with sticky notes, not live actions.

## Replace locally (never commit filled secrets)

See `credentials.placeholders.json`. Minimum set:

- `{{N8N_BASE_URL}}` — your instance, not the seller’s
- `{{WEBHOOK_PATH_SKU1}}` — path only, not a full URL with a secret token
- `{{TABLE_KIND}}` / `{{SHEET_NAME}}` — your table; ID stays off shared notes
- `{{OPERATOR_NOTIFY_CHANNEL}}` — a channel you own

## Support boundary

This download is templates + this README. It is not a hosted inbox, not a custom
build, and not legal or tax advice. If you need a workflow designed against your
real systems, that is a separate freelance job — still official APIs only.

## Affiliation

Independent creator. Not a partner, employee, or certified expert of n8n, Gumroad,
or any AI lab. Tool names are tools, not badges.
