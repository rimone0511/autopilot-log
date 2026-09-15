# n8n Approval-Gated Notify Pack (SKU-2)

Buyer README — digital download
Status of these JSON files: **stubs / placeholders**. They are inactive on purpose.

This pack is **not** n8n Cloud hosting, not a managed service, and not an official
n8n product. You import the graphs into **your** n8n Cloud or self-hosted instance
and you enter credentials yourself.

## What you get

1. This README
2. `credentials.placeholders.json` — names of connections only. No secrets.
3. `stubs/sku2-approval-gate.stub.json` — webhook → draft row → hold; **no outbound**
4. `stubs/sku2-outbound-notify.stub.json` — approve / reject intake; outbound is **NoOp**

SKU-2 sits after a classifier pack (SKU-1) and a starter intake pack (SKU-0).
You do not need those packs installed. If you already have a hold table, point
the gate at that table instead of inventing a second source of truth.

## What it is for

You have a **draft notify** (a message that might leave your n8n: chat, mail, or
a webhook you already own). You want a **human yes** before it goes out:

| Decision | Meaning |
|---|---|
| `approve` | A person said yes. The stub still does **not** send; the outbound node is a NoOp placeholder you replace later. |
| `reject` | A person said no. Stop. Do not send. |
| missing / unknown / timeout | **Fail closed.** Treat as no. Do not guess. |

The product is the **gate**, not a promised delivery-time or approval-rate number.

## What it deliberately does not do

- No outbound without an explicit `approve` from a person
- No auto-reply, auto-invoice, auto-post, or “send if nobody answers”
- No browser automation, scraping, likes, follows, or views
- No storing of API keys, passwords, or customer PII in these files
- No guaranteed time saved, conversion rate, or SLA
- No n8n hosting purchase and no partner badge

## Import (your n8n)

Official steps: [Export and import](https://docs.n8n.io/build/manage-workflows/export-and-import/)

1. Open **your** n8n. Do not import into a shared demo instance you do not control.
2. New workflow (or empty canvas) → three-dot menu → **Import from File**.
3. Import `sku2-approval-gate.stub.json` first, then `sku2-outbound-notify.stub.json`.
4. Confirm both workflows show **Inactive** / not production-active.
5. Replace every `{{PLACEHOLDER}}` in node parameters. Never paste real secrets into
   chat; create credentials inside n8n’s credential UI.
6. Run **one dummy payload** (no real customer names, no live channel). Check: the
   draft lands on `pending`, and a missing `decision` does **not** reach outbound.
7. Only you turn a workflow on. If import fails on your n8n version, rebuild from the
   sticky notes on the canvas. Stubs are teaching graphs, not a version-locked product.

n8n’s own docs warn that workflow JSON can include **credential names**. These stubs
use fake names such as `{{N8N_NOTIFY_CREDENTIAL_NAME}}`. If you later export *your*
copy to share, strip names that identify a private system.

Optional later (not in these stubs): n8n’s [Wait node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.wait/)
can pause one execution and resume on a webhook or form. The stubs use a **static**
approval webhook so they import without a live wait/resume URL. Do not wire
`$execution.resumeUrl` into a public page that anyone can hit.

## Dummy payload (safe) — proposed notify

POST to the gate path you set (`{{WEBHOOK_PATH_SKU2}}`). Example body — fictional:

```json
{
  "source": "form-stub",
  "channel": "example-operator-inbox",
  "draft_text": "EXAMPLE-ONLY — office closed tomorrow",
  "audience": "internal-operator",
  "auto_send": false
}
```

Do not replay real customer mail or a live social post into the first test.

## Dummy payload (safe) — decision

POST to the approval path (`{{WEBHOOK_PATH_SKU2_APPROVAL}}`). Example bodies — fictional:

```json
{
  "decision": "reject",
  "approver_label": "example-operator",
  "note": "EXAMPLE-ONLY dummy reject"
}
```

To exercise the approve branch, send `"decision": "approve"` against the **same dummy
draft**. The approve branch still ends on a NoOp. It does not send mail, chat, or a
public post.

Do not send `auto_send: true`. The stub refuses that path.

## Operator loop (required)

1. Gate stub writes a draft row with `approval_status=pending` and `outbound_allowed=false`.
2. A person looks at the hold / table (your table, your n8n).
3. A person posts `approve` or `reject` to the approval webhook (or clicks a control
   you add later).
4. Reject / missing / unknown / timeout → **STOP**.
5. Approve → still a **NoOp outbound placeholder**. If a row would send money, publish,
   or delete data, the stub **stops**. Those nodes are NoOp placeholders with sticky
   notes, not live actions.

## Replace locally (never commit filled secrets)

See `credentials.placeholders.json`. Minimum set:

- `{{N8N_BASE_URL}}` — your instance, not the seller’s
- `{{WEBHOOK_PATH_SKU2}}` — path only, not a full URL with a secret token
- `{{WEBHOOK_PATH_SKU2_APPROVAL}}` — separate path for the human decision
- `{{TABLE_KIND}}` / `{{SHEET_NAME}}` — your table; ID stays off shared notes
- `{{OPERATOR_NOTIFY_CHANNEL}}` — a channel you own
- `{{APPROVAL_DECISION_FIELD}}` — field name only (`decision` in the dummy)

## Support boundary

This download is templates + this README. It is not a hosted inbox, not a custom
build, and not legal or tax advice. If you need a workflow designed against your
real systems, that is a separate freelance job — still official APIs only.

## Affiliation

Independent creator. Not a partner, employee, or certified expert of n8n, Gumroad,
or any AI lab. Tool names are tools, not badges.
