# Buyer FAQ paste — SKU-0 (English)

Desk: Gumroad
Phase: JOBS
Product: SKU-0 n8n Starter Intake Pack
Mode: **DRAFT_ONLY — paste into the unpublished listing, never Publish**
Language: English (buyer-facing). Do not mention draft / unpublished in these answers.

Gumroad’s standard product form has **no separate FAQ field** (help: Adding a product —
description, summary, additional details, CTA). Paste the “Description FAQ” block
at the **end of the description**, after [LISTING-EN.md](LISTING-EN.md) section 4.

If a later custom landing page has FAQ slots, reuse the same Q/A pairs. Do not invent
schema markup or a second product URL.

Eight pairs. Voice matches the listing: form → table → notify, you send, no auto-reply.

Counts next to each paste were measured with Python `len()` on the fenced text
(spaces count; fences do not).

---

## Description FAQ (paste after the main description)

Paste this whole block:

```
FAQ

What is SKU-0?
An n8n starter intake pack you import into your own instance. A form or webhook writes one row to a table you control. A notify stub pings a person. You send. Nothing auto-replies.

Do I already need n8n?
Yes — n8n Cloud or self-hosted that you control. This download is templates, not hosting. I do not buy n8n for you or create accounts in your name.

Does this send email or chat for me?
No. Notify means a person is pinged. Send stays human. There is no auto-reply, auto-invoice, or post in your name.

Are passwords or API keys in the zip?
No. The zip has credential names and empty secrets. You enter keys inside n8n. Never paste secrets into chat or a shared note.

Do I need SKU-1, SKU-2, or SKU-3?
No. SKU-0 stands alone. Classifier, approval gate, and sheet-sync packs are separate products if/when published. Do not expect them in this zip.

Is AI included?
No. Stubs are routing and notify only. If you later add a model, you still review it. If you want no AI, leave the stubs as they are.

Are you affiliated with n8n or Gumroad?
No. Independent seller. Not a partner or employee of n8n, Gumroad, Google, OpenAI, or xAI. Tool names are tools, not badges.

What if import fails on my n8n version?
Rebuild from the sticky notes on the canvas. Stubs are teaching graphs, not a version-locked product. Contact me with the n8n version only — no secrets.
```

---

## Optional: Additional-details one-liners

If the additional-details box is short, skip the long FAQ and keep
[LISTING-EN.md](LISTING-EN.md) section 5 only.

---

## Split pairs (if a later form has Question / Answer fields)

### Q1 (14) / A1 (144)

```
What is SKU-0?
```

```
An n8n starter intake pack for your own instance. A form or webhook writes one table row. A notify stub pings a person. You send. No auto-reply.
```

### Q2 (22) / A2 (138)

```
Do I already need n8n?
```

```
Yes — n8n Cloud or self-hosted that you control. This is templates, not hosting. I do not buy n8n for you or create accounts in your name.
```

### Q3 (36) / A3 (95)

```
Does this send email or chat for me?
```

```
No. Notify pings a person. Send stays human. No auto-reply, auto-invoice, or post in your name.
```

### Q4 (37) / A4 (104)

```
Are passwords or API keys in the zip?
```

```
No. Credential names only; secrets stay empty. You enter keys inside n8n. Never paste secrets into chat.
```

### Q5 (33) / A5 (103)

```
Do I need SKU-1, SKU-2, or SKU-3?
```

```
No. SKU-0 stands alone. Classifier, approval gate, and sheet-sync packs are separate if/when published.
```

### Q6 (15) / A6 (96)

```
Is AI included?
```

```
No. Stubs are routing and notify only. A later model call is optional and still reviewed by you.
```

### Q7 (39) / A7 (90)

```
Are you affiliated with n8n or Gumroad?
```

```
No. Independent seller. Not a partner or employee of n8n, Gumroad, Google, OpenAI, or xAI.
```

### Q8 (39) / A8 (124)

```
What if import fails on my n8n version?
```

```
Rebuild from the sticky notes on the canvas. Tell me the n8n version only. Do not send secrets, table IDs, or customer data.
```

---

## Do not put in FAQ

- “This listing is unpublished / a draft”
- A live `gumroad.com/l/...` URL
- Filled `{{PRICE}}`, fee %, or GMV
- Refund-as-marketing (“30-day no questions”) unless a human later sets the live refund policy field
- Partner badges, accuracy %, time saved
