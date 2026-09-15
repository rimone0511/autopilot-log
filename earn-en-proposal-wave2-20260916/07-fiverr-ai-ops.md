> **DRAFT_ONLY. DO NOT SEND.**  
> No live Briefs, custom offers, or inbox sends from this pack. No secrets. Rates stay placeholders. Agent does not submit.

# EN-W2-07 — Fiverr: AI ops (Brief intro / custom-offer body)

## Fact table (operator; do not paste)

| key | value |
|---|---|
| pack | earn-en-proposal-wave2-20260916 |
| id | EN-W2-07 |
| desk | Fiverr |
| type | Brief introduction **or** custom-offer description |
| seller_theme | AI ops |
| mode | DRAFT_ONLY, HANDS paste |
| draft | true |
| send | **forbidden** |
| rate_in_prose | no — offer form only |
| chars_preview | 103 |
| chars_short | 385 |
| chars_standard | 738 |

Assumed ask: brief + draft + inspect + human send. Optional AI nodes in n8n.  
Decline: autonomous outbound, fake lab badges, KYC-by-proxy.

---

## Form fields (separate from prose)

| UI field | Paste / action |
|---|---|
| Price (USD) | `{{FIXED_PRICE_USD}}` |
| Delivery (days) | `{{DELIVERY_DAYS}}` |
| Revisions | `{{REVISION_COUNT}}` |

Honor a buyer “no AI” requirement: skip this theme file; use n8n-workflow without model nodes, or decline.

---

## Send gate

- [ ] Brief or inbox is on Fiverr
- [ ] `{{ONE_SPECIFIC_DETAIL}}` is from this buyer
- [ ] Human approve-before-send is acceptable to them
- [ ] No xAI / vendor staff claim
- [ ] I do not send from this PR

---

## List preview (first line; rewrite first)

```
I read {{ONE_SPECIFIC_DETAIL}} on "{{JOB_TITLE}}". I would keep a human stop before any draft is sent.
```

---

## Short paste (inbox / Ask questions)

```
Thanks for writing about {{ONE_SPECIFIC_DETAIL}} on "{{GIG_TITLE}}".

I can scope AI ops as a brief you can rerun, a draft path, and an inspection list. A person still sends or publishes. I do not claim the model is always correct. I am not affiliated with xAI or with a model vendor.

I need:
1. {{QUESTION_1}}
2. {{QUESTION_2}}

Stay on Fiverr. Price stays in the custom-offer form.
```

---

## Standard paste (Brief intro / custom-offer body)

```
Custom offer for: {{ONE_SPECIFIC_DETAIL}}
{{SCOPE_ONE_LINER}}

Included:
1. One-page operator brief (goal, allowed inputs, done, forbidden, stop)
2. Draft path on {{STACK_OR_TOOL}} (documented connector / official API). Model brand is your choice or “no model”
3. Inspection list (secrets, over-claim, out-of-scope actions) and a short rerun note

Not included: auto-send to customers, auto-publish, invented citations, extra brands of model, KYC or identity work. New loop = a new offer.

Public notes: {{PORTFOLIO_URL}}. Fail-closed official-API example: {{GITHUB_REPO_AUTOPILOT}}.

{{DISPLAY_NAME}}, Japan, async {{TIMEZONE}}. Keep chat and payment on Fiverr.

Revisions and delivery are the form fields. This box has no second price.
```

---

## Fictional fill (not a real buyer; do not send)

- Label: `Client G` (fictional)
- Title example: `[FICTION] Draft FAQ answers from a help doc; seller clicks send`
- `{{SCOPE_ONE_LINER}}` example: `The model drafts; you approve; nothing leaves the inbox without you.`
- `{{QUESTION_1}}` example: `Must this run with no AI if a buyer later asks for no-AI?`
- `{{QUESTION_2}}` example: `Which fields are forbidden in the prompt (passwords, payment IDs)?`

---

## STOP

- Honor no-AI; do not sneak a model in
- Do not send from this PR
