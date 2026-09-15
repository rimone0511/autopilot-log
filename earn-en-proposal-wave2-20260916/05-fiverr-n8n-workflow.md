> **DRAFT_ONLY. DO NOT SEND.**  
> No live Briefs, custom offers, or inbox sends from this pack. No secrets. Rates stay placeholders. Agent does not submit.

# EN-W2-05 — Fiverr: n8n workflow (Brief intro / custom-offer body)

## Fact table (operator; do not paste)

| key | value |
|---|---|
| pack | earn-en-proposal-wave2-20260916 |
| id | EN-W2-05 |
| desk | Fiverr |
| type | Brief introduction **or** custom-offer description |
| seller_theme | n8n workflow |
| mode | DRAFT_ONLY, HANDS paste |
| draft | true |
| send | **forbidden** |
| rate_in_prose | no — offer form only |
| chars_preview | 108 |
| chars_short | 480 |
| chars_standard | 746 |

When: Fiverr showed **you** this Brief, or a buyer already opened a Gig thread and you have enough answers for an offer.  
When not: Cold DM. Scraped buyer-request lists. Gig page copy (sibling pack).

---

## Form fields (separate from prose)

| UI field | Paste / action |
|---|---|
| Price (USD) | `{{FIXED_PRICE_USD}}` — $5–$20,000 per Fiverr help; re-read the live article |
| Delivery (days) | `{{DELIVERY_DAYS}}` — 1–90 if help still says so; trust the form |
| Revisions | `{{REVISION_COUNT}}` |
| Gig to attach | Unpublished n8n Gig from sibling pack, if it exists; else skip this file |
| Brief action | Create offer / Ask questions / Not interested — in that UI |

Price in the description only if it **matches the field**. Prefer: description has **no** price.

---

## Send gate

- [ ] Brief or inbox opened inside Fiverr (not an extension list)
- [ ] `{{ONE_SPECIFIC_DETAIL}}` is a phrase from **this** buyer
- [ ] I will not send the same paragraph to a stack of briefs without rewriting the detail line
- [ ] No off-platform pay or messenger
- [ ] I submit in the Fiverr UI myself — **not from this PR**

---

## List preview (first line; rewrite first)

```
I read {{ONE_SPECIFIC_DETAIL}} on "{{JOB_TITLE}}". I would build that as one n8n path plus an operator SOP.
```

---

## Short paste (inbox / Ask questions)

```
Thanks for writing about {{ONE_SPECIFIC_DETAIL}} on "{{GIG_TITLE}}".

I can scope this as an n8n workflow plus an operator note (what it does, what to do when it fails). Official APIs or documented connectors only — no browser bots, no likes/follows/views.

To send an accurate custom offer in this inbox I need:
1. {{QUESTION_1}}
2. {{QUESTION_2}}

Please keep the order on Fiverr. Price, delivery days, and revisions go in the offer form after you answer — not in this message.
```

---

## Standard paste (Brief intro / custom-offer body)

```
Custom offer for: {{ONE_SPECIFIC_DETAIL}}
{{SCOPE_ONE_LINER}}

Included:
1. Map the current steps and the stop conditions
2. Build one n8n workflow on {{STACK_OR_TOOL}} (official API or documented connector only)
3. Hand over a short operator SOP and a change note (what to edit, what is a secret)

Not included: extra tools, extra channels, likes/follows/views, browser scraping, or posting that bypasses your approve step. New scope = a new offer.

Public notes: {{PORTFOLIO_URL}}. Fail-closed official-API example: {{GITHUB_REPO_AUTOPILOT}}.

I am {{DISPLAY_NAME}}, Japan-based, async in {{TIMEZONE}}. Stay on Fiverr for chat and payment.

Revisions and delivery days are the values in the offer form, not a second set of numbers in this box.
```

---

## Fictional fill (not a real buyer; do not send)

- Label: `Client E` (fictional)
- Title example: `[FICTION] n8n: new Typeform row → Sheet; Slack only on error`
- `{{SCOPE_ONE_LINER}}` example: `One happy path and one failure alert, then a one-page rerun note.`
- `{{QUESTION_1}}` example: `Cloud n8n or a host you already control?`
- `{{QUESTION_2}}` example: `What must never be written into the Sheet (raw passwords, ID images)?`

---

## STOP

- Do not Publish a Gig from this file
- Do not cold-DM buyers
- Do not send the offer from this PR
