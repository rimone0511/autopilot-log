> **DRAFT_ONLY. DO NOT SEND.**  
> No live bids. No secrets. No client PII. Rates stay placeholders. Agent does not submit.

# EN-W2-03 — Upwork: AI ops (cover letter)

## Fact table (operator; do not paste)

| key | value |
|---|---|
| pack | earn-en-proposal-wave2-20260916 |
| id | EN-W2-03 |
| desk | Upwork |
| type | Job proposal / cover letter |
| seller_theme | AI ops |
| mode | DRAFT_ONLY, HANDS paste |
| draft | true |
| send | **forbidden** |
| rate_in_prose | no — form field only |
| chars_preview | 125 |
| chars_short | 624 |
| chars_standard | 1081 |

Assumed listing type (not a real job): prompts, inspection checklists, and a human stop before anything is sent or published. Tool names (ChatGPT, Claude, n8n AI nodes) are interchangeable; the product is the ops loop, not a lab badge.

Out of scope: fully autonomous outbound, invented citations, KYC-by-proxy, “agent that emails your customers tonight.”

---

## Form fields (separate from prose)

| UI field | Paste / action |
|---|---|
| Bid type | Live form: hourly **or** fixed |
| Hourly (USD) | `{{HOURLY_RATE_USD}}` |
| Fixed price (USD) | `{{FIXED_PRICE_USD}}` |
| Duration | `{{DELIVERY_DAYS}}` |

Empty required rate → park `rate_required`. Do not invent USD in git.

---

## Send gate

- [ ] Job opened on upwork.com
- [ ] `{{ONE_SPECIFIC_DETAIL}}` is from this post
- [ ] The ask is inspectable AI ops, not “set it loose on production”
- [ ] No contact details in the letter
- [ ] I click Submit myself

---

## List preview (first line; rewrite first)

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{JOB_TITLE}}". I would pin the stop conditions before any model drafts a message.
```

---

## Short paste

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{JOB_TITLE}}". I would pin the stop conditions before any model drafts a message.

I set up AI ops a person can rerun: a one-page brief (goal, allowed inputs, done definition, forbidden actions), draft-then-inspect, and a human approve step before send or publish. I do not claim the model is always right. Unverified stays unverified.

Public notes: {{PORTFOLIO_URL}}. Same fail-closed habit on an official-API tool: {{GITHUB_REPO_AUTOPILOT}}.

I am {{DISPLAY_NAME}}, Japan-based, async in {{TIMEZONE}}. Keep scoping on Upwork.

Two questions:
1. {{QUESTION_1}}
2. {{QUESTION_2}}
```

---

## Standard paste

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{JOB_TITLE}}". {{SCOPE_ONE_LINER}}

I am {{DISPLAY_NAME}}. AI ops, here, is not “an agent that runs the company.” It is a small loop: (1) write the brief so a second person could run it, (2) keep investigate / change / check as separate steps, (3) inspect drafts for secrets, over-claim, and out-of-scope actions, (4) leave a short regression note for what used to work. {{STACK_OR_TOOL}} is fine if it is a documented connector; the brand of model is secondary.

I will not send customer email, post publicly, or move money without your approve step. I will not invent citations, client counts, or cost-savings percentages. I am not affiliated with xAI or with any model vendor.

Deliverables:
- Operator brief (allowed / forbidden / stop)
- Draft path (human still sends)
- Inspection list (secrets, tone, facts you must confirm)
- Short rerun note

Public notes: {{PORTFOLIO_URL}}. {{GITHUB_REPO_AUTOPILOT}}.

English, async in {{TIMEZONE}}, Japan. Price stays in the Upwork bid fields.

Questions:
1. {{QUESTION_1}}
2. {{QUESTION_2}}
```

---

## Fictional fill (not a real job; do not send)

- Label: `Client C` (fictional)
- Title example: `[FICTION] Human-in-the-loop drafts for support macros; nothing auto-sends`
- `{{SCOPE_ONE_LINER}}` example: `The model may draft a reply; a person must press send, and secrets must not appear in the draft.`
- `{{QUESTION_1}}` example: `Which system holds the macros today, and who is allowed to publish a change?`
- `{{QUESTION_2}}` example: `What must never go into a prompt (account numbers, tickets marked private)?`

---

## STOP

- Do not claim affiliation with xAI, OpenAI, Anthropic, or n8n as staff
- Do not offer to complete KYC or identity checks for the client
- Do not send
