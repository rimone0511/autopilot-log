> **DRAFT_ONLY. DO NOT SEND.**  
> Inbound Services RFP only. No secrets. No client PII. Rates stay placeholders. Agent does not Submit.

# LI-W2-09 — Services proposal: AI ops (EN)

## Fact table (operator; do not paste)

| key | value |
|---|---|
| pack | earn-linkedin-outreach-wave2-20260916 |
| id | LI-W2-09 |
| desk | LinkedIn Services (personal Service Page admin) |
| type | Proposal **personal message** |
| seller_theme | AI ops |
| lang | EN |
| mode | DRAFT_ONLY, HANDS paste |
| draft | true |
| send | **forbidden** |
| inbound_rfp_required | **yes** |
| rate_in_prose | no — form field only |
| chars_short | 399 |
| chars_standard | 1196 |
| chars_decline | 199 |

Assumed request (not a real RFP): prompts, inspection checklists, and a human stop before anything is sent or published. The product is the ops loop, not a lab badge.

Out of scope: fully autonomous outbound, invented citations, KYC-by-proxy, “agent that emails your customers tonight.”

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
- [ ] Ask is inspectable AI ops, not “set it loose on production”
- [ ] No contact details in the message
- [ ] I do **not** click Submit from this pack

---

## Short paste

```
You asked about {{ONE_SPECIFIC_DETAIL}}. I would pin the stop conditions before any model drafts a message: brief, draft, inspect, a person presses send.

I am {{DISPLAY_NAME}}, Japan, async {{TIMEZONE}}. Public notes: {{PORTFOLIO_URL}}. I do not claim the model is always right.

Questions: {{QUESTION_1}} / {{QUESTION_2}}

Fee stays in the proposal form. This text is a draft and is not submitted.
```

---

## Standard paste

```
You asked about {{ONE_SPECIFIC_DETAIL}}. {{SERVICE_REQUEST_SUMMARY}}

I am {{DISPLAY_NAME}}. AI ops, here, is not “an agent that runs the company.” It is a small loop: (1) write the brief so a second person could run it, (2) keep investigate / change / check as separate steps, (3) inspect drafts for secrets, over-claim, and out-of-scope actions, (4) leave a short regression note. I will not send customer email, post publicly, or move money without your approve step.

Public notes: {{PORTFOLIO_URL}}. Fail-closed example (official APIs): {{GITHUB_REPO_AUTOPILOT}}. I am not affiliated with xAI or with any model vendor.

Deliverables:
- Operator brief (allowed / forbidden / stop)
- Draft path (human still sends)
- Inspection list (secrets, tone, facts you must confirm)
- Short rerun note

Out of scope: fully autonomous outbound, invented citations, identity checks for someone else, guaranteed accuracy percentages.

Japan-based, English or Japanese, async {{TIMEZONE}}. Keep scoping on LinkedIn. No email or WhatsApp in this message.

Questions:
1. {{QUESTION_1}}
2. {{QUESTION_2}}

Price and timing stay in the Services form fields. This file is a draft. It is not a submitted proposal.
```

---

## Decline paste (out of scope; still do not click from this pack)

```
Thank you for the request about {{ONE_SPECIFIC_DETAIL}}. I am declining this one. I do not take fully autonomous outbound, invented citations, or identity/KYC work for someone else. No need to reply.
```

---

## Fictional fill (not a real RFP; do not send)

- Label: `Request I` (fictional)
- `{{ONE_SPECIFIC_DETAIL}}` example: `support macros drafted by a model, nothing auto-sends`
- `{{SERVICE_REQUEST_SUMMARY}}` example: `The model may draft; a person must press send; secrets stay out of the prompt.`
- `{{QUESTION_1}}` example: `Which system holds the macros today, and who may publish a change?`
- `{{QUESTION_2}}` example: `What must never go into a prompt?`

---

## STOP

- No inbound RFP → do not use this file
- Do not claim vendor employment
- Do not submit
