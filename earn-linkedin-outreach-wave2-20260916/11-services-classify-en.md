> **DRAFT_ONLY. DO NOT SEND.**  
> Inbound Services RFP only. No secrets. No client PII. Rates stay placeholders. Agent does not Submit.

# LI-W2-11 — Services proposal: lead classify (EN)

## Fact table (operator; do not paste)

| key | value |
|---|---|
| pack | earn-linkedin-outreach-wave2-20260916 |
| id | LI-W2-11 |
| desk | LinkedIn Services (personal Service Page admin) |
| type | Proposal **personal message** |
| seller_theme | lead classify |
| lang | EN |
| mode | DRAFT_ONLY, HANDS paste |
| draft | true |
| send | **forbidden** |
| inbound_rfp_required | **yes** |
| rate_in_prose | no — form field only |
| chars_short | 386 |
| chars_standard | 975 |
| chars_decline | 170 |

Assumed request (not a real RFP): existing labels, a route, and an **unsure** bucket a person reviews. No auto-close. No scraped lists.

Out of scope: outbound sequences, fake intent percentages, buying or scraping contacts.

If Admin view has **no** New request, stop. Do not recycle this as a connection note or a cold DM.

---

## Form fields (separate from prose)

| UI field | Paste / action |
|---|---|
| Personal message | short or standard fence below |
| Fee / rate (if shown) | `{{HOURLY_RATE_USD}}` or `{{FIXED_PRICE_USD}}` |
| Timeline (if shown) | `{{LEAD_TIME_DRAFT}}` |
| Submit proposal | **do not click** — [STOP-AT-PUBLISH.md](STOP-AT-PUBLISH.md) |
| No thanks / Decline | only for out-of-scope; irreversible |

Empty required rate → park `rate_required`. Do not invent USD in git.

---

## Send gate

- [ ] Request opened in **Services admin → New requests**
- [ ] `{{ONE_SPECIFIC_DETAIL}}` is from **this** RFP
- [ ] Ask is tags + human review of unsure, not a spam sequence
- [ ] No contact details in the message
- [ ] I do **not** click Submit from this pack

---

## Short paste

```
You asked about {{ONE_SPECIFIC_DETAIL}}. I would map to labels you already use, route the easy ones, and leave an unsure bucket a person reviews. I will not auto-close or auto-email.

I am {{DISPLAY_NAME}}, Japan, async {{TIMEZONE}}. Public notes: {{PORTFOLIO_URL}}.

Questions: {{QUESTION_1}} / {{QUESTION_2}}

Fee stays in the proposal form. This text is a draft and is not submitted.
```

---

## Standard paste

```
You asked about {{ONE_SPECIFIC_DETAIL}}. {{SERVICE_REQUEST_SUMMARY}}

I am {{DISPLAY_NAME}}. Classify, here, is routing — not a promise that a score is true. I start from your existing labels, write what “unsure” means, and keep a person on that bucket. I will not scrape a list, buy contacts, or fire a message sequence from a tag.

Public notes: {{PORTFOLIO_URL}}. Fail-closed example (official APIs): {{GITHUB_REPO_AUTOPILOT}}.

Deliverables:
- Label map (including unsure)
- Route diagram a second operator can follow
- Sample of mis-routes to inspect (dummy data, no secrets)
- A stop: no send from a predicted intent

Out of scope: scraped CRMs, engagement pods, guaranteed precision, auto-close.

Japan-based, English or Japanese, async {{TIMEZONE}}. Keep scoping on LinkedIn. No email or WhatsApp in this message.

Questions:
1. {{QUESTION_1}}
2. {{QUESTION_2}}

Price and timing stay in the Services form fields. This file is a draft. It is not a submitted proposal.
```

---

## Decline paste (out of scope; still do not click from this pack)

```
Thank you for the request about {{ONE_SPECIFIC_DETAIL}}. I am declining this one. I do not take scraped lists, auto-DM sequences, or fake intent scores. No need to reply.
```

---

## Fictional fill (not a real RFP; do not send)

- Label: `Request K` (fictional)
- `{{ONE_SPECIFIC_DETAIL}}` example: `inbox tags: billing / product / unsure`
- `{{SERVICE_REQUEST_SUMMARY}}` example: `You want a first pass into current tags; unsure stays for a person.`
- `{{QUESTION_1}}` example: `What are the exact labels in use today?`
- `{{QUESTION_2}}` example: `Who reviews the unsure bucket, and how often?`

---

## STOP

- No inbound RFP → do not use this file
- Do not offer a scraped lead list
- Do not submit
