# n8n Google Sheet Sync Pack (SKU-3)

Buyer README — digital download
Status of these JSON files: **stubs / placeholders**. They are inactive on purpose.

This pack is **not** n8n Cloud hosting, not a managed service, and not an official
n8n or Google product. You import the graphs into **your** n8n Cloud or self-hosted
instance and you enter credentials yourself.

## What you get

1. This README
2. `credentials.placeholders.json` — names of connections only. No secrets.
3. `stubs/sku3-sheet-inbound.stub.json` — inbound row → hold; **no outbound**
4. `stubs/sku3-human-notify.stub.json` — operator ping intake; outbound is **NoOp**

SKU-3 sits after a starter intake pack (SKU-0), a classifier pack (SKU-1), and
an approval-gate pack (SKU-2). You do not need those packs installed. If you
already have a sheet of inbound rows, point this pack at **that** sheet instead
of inventing a second source of truth.

## What it is for

A **new row** lands (Google Sheet, or a webhook that stands in while you test).
You want a **person** to see it before anything leaves your n8n:

| Signal | Meaning |
|---|---|
| inbound row | Park it. Ping an operator channel you own. Do not send to the row’s audience. |
| `auto_send: true` | **Refuse.** The stub never treats this as permission to send. |
| empty / unreadable row | **Fail closed.** Do not guess a message. |
| already-sent claim in the payload | **Refuse.** The stub does not trust a client that says it already sent. |

The product is the **human-notify hold**, not a promised sync interval or
row-throughput number.

The Google Sheets Trigger node is **not** wired in these stubs. n8n’s own
[Google Sheets Trigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.googlesheetstrigger/)
docs describe row-added / row-updated events. You add that node later, on
**your** instance, with a credential **you** create in n8n’s UI. Until then,
POST a dummy row to the webhook path.

## What it deliberately does not do

- No outbound mail, chat, invoice, or public post from a new row
- No auto-reply, auto-invoice, auto-post, or “send if nobody answers”
- No browser automation, scraping, likes, follows, or views
- No storing of API keys, passwords, spreadsheet IDs, or customer PII in these files
- No guaranteed time saved, conversion rate, or SLA
- No n8n hosting purchase and no partner badge
- No Google Workspace admin access and no service-account JSON in the zip

## Import (your n8n)

Official steps: [Export and import](https://docs.n8n.io/build/manage-workflows/export-and-import/)

1. Open **your** n8n. Do not import into a shared demo instance you do not control.
2. New workflow (or empty canvas) → three-dot menu → **Import from File**.
3. Import `sku3-sheet-inbound.stub.json` first, then `sku3-human-notify.stub.json`.
4. Confirm both workflows show **Inactive** / not production-active.
5. Replace every `{{PLACEHOLDER}}` in node parameters. Never paste real secrets into
   chat; create credentials inside n8n’s credential UI.
6. Run **one dummy payload** (no real customer names, no live sheet ID). Check: the
   row stays on hold, `auto_send` does **not** reach outbound, and the notify node
   is still a NoOp.
7. Only you turn a workflow on. If import fails on your n8n version, rebuild from the
   sticky notes on the canvas. Stubs are teaching graphs, not a version-locked product.

n8n’s own docs warn that workflow JSON can include **credential names**. These stubs
use fake names such as `{{GOOGLE_SHEETS_CREDENTIAL_NAME}}`. If you later export *your*
copy to share, strip names that identify a private system.

Optional later (not in these stubs): replace the inbound webhook with n8n’s
[Google Sheets Trigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.googlesheetstrigger/)
after you add a Google credential in n8n
([Google credentials](https://docs.n8n.io/integrations/builtin/credentials/google/)).
Do not commit the spreadsheet ID, OAuth client secret, or a service-account JSON
file. n8n’s Sheets docs also note that Google Drive API may be required alongside
Sheets API — follow **current** n8n + Google help, not this README, for enablement.

Do not paste `$execution.resumeUrl` onto a public sheet that anyone can edit.

## Dummy payload (safe) — inbound row

POST to the inbound path you set (`{{WEBHOOK_PATH_SKU3}}`). Example body — fictional:

```json
{
  "event": "row_added",
  "sheet_name": "EXAMPLE-ONLY",
  "row_index": "2",
  "status": "new",
  "note": "EXAMPLE-ONLY — office closed tomorrow",
  "auto_send": false,
  "already_sent": false
}
```

Do not replay a real customer row, a live spreadsheet ID, or a production form
into the first test.

## Dummy payload (safe) — human notify

POST to the notify path (`{{WEBHOOK_PATH_SKU3_NOTIFY}}`). Example body — fictional:

```json
{
  "sheet_name": "EXAMPLE-ONLY",
  "row_index": "2",
  "status": "new",
  "note": "EXAMPLE-ONLY dummy operator ping",
  "auto_send": false
}
```

The notify branch still ends on a NoOp. It does not send mail, chat, or a
public post.

Do not send `auto_send: true`. The stub refuses that path.

## Operator loop (required)

1. Inbound stub parks a row with `outbound_allowed=false` and `live_send=false`.
2. A person looks at the sheet / hold (your sheet, your n8n).
3. A person decides what, if anything, to send **outside** this pack (or via a
   later gate such as SKU-2).
4. Auto-send / already-sent / empty row → **STOP**.
5. Human notify → still a **NoOp outbound placeholder**. If a row would send
   money, publish, or delete data, the stub **stops**. Those nodes are NoOp
   placeholders with sticky notes, not live actions.

## Replace locally (never commit filled secrets)

See `credentials.placeholders.json`. Minimum set:

- `{{N8N_BASE_URL}}` — your instance, not the seller’s
- `{{WEBHOOK_PATH_SKU3}}` — path only, not a full URL with a secret token
- `{{WEBHOOK_PATH_SKU3_NOTIFY}}` — separate path for the operator ping
- `{{SHEET_NAME}}` — tab name; spreadsheet ID stays off shared notes
- `{{GOOGLE_SHEETS_CREDENTIAL_NAME}}` — name only, created in your n8n
- `{{OPERATOR_NOTIFY_CHANNEL}}` — a channel you own
- `{{ROW_EVENT}}` — event name only (`row_added` in the dummy)

## Support boundary

This download is templates + this README. It is not a hosted inbox, not a custom
build, and not legal or tax advice. If you need a workflow designed against your
real systems, that is a separate freelance job — still official APIs only.

## Affiliation

Independent creator. Not a partner, employee, or certified expert of n8n, Gumroad,
Google, or any AI lab. Tool names are tools, not badges.
