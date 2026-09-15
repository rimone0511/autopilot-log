> **DRAFT_ONLY. DO NOT SEND.**  
> Inbound Services RFP only. No secrets. No client PII. Rates stay placeholders. Agent does not Submit.

# LI-W2-07 — Services proposal: n8n (EN)

## Fact table (operator; do not paste)

| key | value |
|---|---|
| pack | earn-linkedin-outreach-wave2-20260916 |
| id | LI-W2-07 |
| desk | LinkedIn Services (personal Service Page admin) |
| type | Proposal **personal message** |
| seller_theme | n8n workflow |
| lang | EN |
| mode | DRAFT_ONLY, HANDS paste |
| draft | true |
| send | **forbidden** |
| inbound_rfp_required | **yes** |
| rate_in_prose | no — form field only |
| chars_short | 441 |
| chars_standard | 1150 |
| chars_decline | 203 |

Assumed request (not a real RFP): form → sheet → notify, with a human stop before send. Tool names (n8n, Sheets, a first-party webhook) are interchangeable; the product is the rerunnable loop, not a partner badge.

Out of scope: browser bots, scraping, likes/follows, ungated outbound, KYC-by-proxy.

If Admin view has **no** New request, stop. Do not recycle this as a connection note or a cold DM.

---

## Form fields (separate from prose)

| UI field | Paste / action |
|---|---|
| Personal message | short or standard fence below |
| Fee / rate (if shown) | `{{HOURLY_RATE_USD}}` or `{{FIXED_PRICE_USD}}` from the **local** ledger |
| Timeline (if shown) | `{{LEAD_TIME_DRAFT}}` |
| Submit proposal | **do not click** — [STOP-AT-PUBLISH.md](STOP-AT-PUBLISH.md) |
| No thanks / Decline | only for out-of-scope; decline is irreversible ([a570605](https://www.linkedin.com/help/linkedin/answer/a570605)) |

Empty required rate → park `rate_required`. Do not invent USD in git. Contact-for-pricing on the Service Page stays a sibling CU decision, not a number in this message.

---

## Send gate

- [ ] Request opened in **Services admin → New requests**
- [ ] `{{ONE_SPECIFIC_DETAIL}}` is from **this** RFP
- [ ] Ask is official connectors + a human stop, not a scraper
- [ ] No contact details in the message
- [ ] I do **not** click Submit from this pack

---

## Short paste

```
You wrote {{ONE_SPECIFIC_DETAIL}} on this Services request. I would build it in n8n on official connectors, with operator notes a second person can rerun. Send and publish stay human.

I am {{DISPLAY_NAME}}, Japan, async {{TIMEZONE}}. Public notes: {{PORTFOLIO_URL}}.

Out of scope: browser bots, scraping, likes/follows.

Questions: {{QUESTION_1}} / {{QUESTION_2}}

Fee stays in the proposal form. This text is a draft and is not submitted.
```

---

## Standard paste

```
You wrote {{ONE_SPECIFIC_DETAIL}} on this Services request. {{SERVICE_REQUEST_SUMMARY}}

I am {{DISPLAY_NAME}}. I set up n8n in the client workspace: official APIs and documented connectors only, a dummy run before production, and a human stop before anything sends or publishes. I do not click the live site for you. I do not store your keys.

Public notes: {{PORTFOLIO_URL}}. Same fail-closed habit on an official-API tool: {{GITHUB_REPO_AUTOPILOT}}.

Deliverables I would name in the project thread:
- Workflow in your n8n
- Connector list with secrets omitted
- Stop / rerun notes
- A check that existing sheets or inboxes were not overwritten

Out of scope: scraping, engagement automation, ungated outbound, identity checks for someone else, invented time-saved percentages.

I am Japan-based, English or Japanese, async in {{TIMEZONE}}. Keep this thread on LinkedIn until a contract exists. No email or WhatsApp in this message.

Questions:
1. {{QUESTION_1}}
2. {{QUESTION_2}}

Price and timing stay in the Services form fields ({{FIXED_PRICE_USD}} / {{LEAD_TIME_DRAFT}} are placeholders). This file is a draft. It is not a submitted proposal.
```

---

## Decline paste (out of scope; still do not click from this pack)

```
Thank you for the request about {{ONE_SPECIFIC_DETAIL}}. I am declining this one. I do not take scraping, engagement automation, ungated send/publish, or identity work for someone else. No need to reply.
```

---

## Fictional fill (not a real RFP; do not send)

- Label: `Request G` (fictional)
- `{{ONE_SPECIFIC_DETAIL}}` example: `form rows to a sheet, Slack only after a person checks`
- `{{SERVICE_REQUEST_SUMMARY}}` example: `You want new form rows copied, then a draft ping, not an auto-send.`
- `{{QUESTION_1}}` example: `Which form product holds the intake today?`
- `{{QUESTION_2}}` example: `Who is allowed to press send on the notify step?`

---

## STOP

- No inbound RFP → do not use this file
- Do not put {{EMAIL}} or a calendar link in the proposal
- Do not submit
