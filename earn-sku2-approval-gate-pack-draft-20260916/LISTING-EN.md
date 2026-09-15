# Gumroad listing paste — SKU-2 (English)

Desk: Gumroad
Product: SKU-2 n8n Approval-Gated Notify Pack
Checked: 2026-09-16 (public help: adding a product)
Mode: **DRAFT_ONLY — fill the form, never Publish / Enable**
Language: English listing (Japanese operator). Honest `{{COUNTRY}}`.
Google: MAIN Google only (`{{GOOGLE_ACCOUNT_EMAIL}}`)

Public entry:

- Dashboard: https://gumroad.com/
- Help — Adding a product: https://gumroad.com/help/article/149-adding-a-product
- n8n import: https://docs.n8n.io/build/manage-workflows/export-and-import/

Product type in the New product picker: **Digital product** (file download).
Not membership, coffee, call, or commission.

---

## 0. How far to go (then stop)

1. MAIN Google → Gumroad (already `done-draft` on the 2026-09-16 queue).
2. **New product** → Digital product.
3. Paste name, description, summary, tags from this file.
4. Price: paste the **placeholder** from [PRICING.md](PRICING.md) only. Do not invent a live number in git.
5. Content tab: do **not** upload a customer zip from this agent. A human attaches files later.
6. Confirm the product stays **unpublished**.
7. **STOP** at payout, bank, tax, ID upload, or Publish. See [DRAFT_ONLY.md](DRAFT_ONLY.md).

Do not set a custom permalink live. Keep `{{GUMROAD_PERMALINK_SKU2}}` local.

---

## 1. Name

Paste:

```
n8n Approval-Gated Notify — human must approve first to send
```

| Count | Value |
|---|---|
| Name | 60 characters |

Do not keyword-stuff “n8n AI agent xAI Grok official partner”.

---

## 2. Call to action

Help: pick a built-in CTA. Do not invent a custom CTA (help says that is not available).

Suggested pick: **I want this!**

If the live list differs, pick the closest buy/download CTA. Do not pick Donate unless you intend a coffee-style product (you do not).

---

## 3. Summary (under the CTA)

Paste:

```
Importable n8n stubs that hold a draft notify until a person approves. A missing or late yes means no outbound. You send.
```

| Count | Value |
|---|---|
| Summary | 121 characters |

---

## 4. Description (English)

Buyer-facing. Do not write “unpublished draft” in this box (it would ship if a human later publishes).

```
SKU-2 is an n8n approval-gated notify pack you run on your own instance.

You import two inactive workflow stubs: one parks a draft outbound in a hold queue, and one is the approve/reject intake. A human must approve before anything leaves. Missing, unknown, rejected, or timed-out decisions fail closed — no outbound. The pack does not auto-reply, auto-invoice, or post in your name.

You get a buyer README, a credentials placeholder file (names only — no secrets), and JSON stubs. Official APIs and webhooks only. No browser bots, scraping, or engagement automation.

AI is optional and off in the stubs. If you later add a model call to draft text, you still approve the send. If you want no AI, leave the stubs as they are.

This is a template pack, not n8n hosting, not a custom build, and not an official n8n or Gumroad product. I am an independent seller. After import, replace every placeholder, test with dummy data, and only you turn a workflow on.

Not included: SKU-0 starter intake or SKU-1 classifier (sold separately if/when published), live credentials, guaranteed speed, or sending mail for you.

If a stub fails to import on your n8n version, rebuild from the sticky notes on the canvas. See the buyer README for dummy payloads and the operator loop.
```

---

## 5. Additional details (optional Gumroad box)

Help: extra details can sit below the CTA.

```
Format: n8n workflow JSON stubs + Markdown README
Runtime: your n8n Cloud or self-hosted instance
Activation: off until you turn it on
Secrets: you enter credentials in n8n; they are not in the zip
Gate: approve required; timeout is not approve
Languages: English README; Japanese listing exists for the JP storefront paste
```

---

## 6. Tags / taxonomy

Help mentions category / taxonomy on create. If the form shows tags, use:

```
n8n
automation
workflow
approval
operator-docs
```

Do not tag `xAI`, `Grok`, `ChatGPT`, or fake partner words.

If a category tree is required, pick the closest **software / templates / digital downloads** node. Do not file this under AI image, video, or voice.

---

## 7. Permalink (do not publish)

Local only:

```
{{GUMROAD_PERMALINK_SKU2}}
```

Do not announce a `gumroad.com/l/...` URL from this pack. Unpublished products should not be treated as live.

---

## 8. Content tab (human later)

When a human prepares the zip (not this agent):

- `BUYER-README.md`
- `credentials.placeholders.json`
- `stubs/sku2-approval-gate.stub.json`
- `stubs/sku2-outbound-notify.stub.json`

Do not attach operator files (`LISTING-*.md`, `DRAFT_ONLY.md`, `PRICING.md`, pack `README.md`).

Cover / thumbnail: skip until original images exist. Do not paste the n8n logo as if you were a partner.

---

## 9. Versions (leave off)

Help: versions are optional price/content splits. This SKU is **one digital download**.
Do not add a “with setup call” version that implies a live session you have not scoped.

---

## 10. Affiliation sentence (keep in description; repeat here for paste if a checkbox appears)

```
Independent seller. Not a partner or employee of n8n, Gumroad, or any AI company.
```
