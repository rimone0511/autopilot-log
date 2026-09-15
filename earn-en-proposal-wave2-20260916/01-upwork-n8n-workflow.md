> **DRAFT_ONLY. DO NOT SEND.**  
> No live bids. No secrets. No client PII. Rates stay placeholders. Agent does not submit.

# EN-W2-01 — Upwork: n8n workflow (cover letter)

## Fact table (operator; do not paste)

| key | value |
|---|---|
| pack | earn-en-proposal-wave2-20260916 |
| id | EN-W2-01 |
| desk | Upwork |
| type | Job proposal / cover letter |
| seller_theme | n8n workflow |
| mode | DRAFT_ONLY, HANDS paste |
| draft | true |
| send | **forbidden** |
| rate_in_prose | no — form field only |
| chars_preview | 124 |
| chars_short | 735 |
| chars_standard | 1313 |

Assumed listing type (not a real job): one n8n path a non-engineer can rerun — trigger, honest steps, destination, failure alert, short SOP.

Out of scope: browser automation, scraping without an official API, likes/follows/views, partner-badge impersonation.

---

## Form fields (separate from prose)

| UI field | Paste / action |
|---|---|
| Bid type | Live form: hourly **or** fixed — do not write a second price in the letter |
| Hourly (USD) | `{{HOURLY_RATE_USD}}` |
| Fixed price (USD) | `{{FIXED_PRICE_USD}}` |
| Project duration / milestone dates | `{{DELIVERY_DAYS}}` |
| Connects | Human per-job choice; this pack does not tell you to buy or spray |

Empty required rate → park `rate_required`. Do not invent USD in git. Do not send from this file.

---

## Send gate

- [ ] Job opened on upwork.com (not a scrape dump)
- [ ] `{{ONE_SPECIFIC_DETAIL}}` is unique to this post
- [ ] Theme still matches **n8n / workflow automation**, not writing-only or lead-classify-only
- [ ] No email / phone / messenger
- [ ] I click Submit myself

---

## List preview (first line; rewrite first)

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{JOB_TITLE}}". I would treat that as the first n8n path, not a generic template.
```

---

## Short paste

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{JOB_TITLE}}". I would treat that as the first n8n path, not a generic template.

I build n8n workflows a non-engineer can rerun: official APIs or documented connectors only, retries, a failure alert, and a short SOP (what starts it, what is safe to edit, where secrets live). I do not use browser automation. I do not scrape platforms that have no API.

Public example of that posture: Autopilot Log (official posting APIs; posting gate fails closed) — {{GITHUB_REPO_AUTOPILOT}}. Field notes: {{PORTFOLIO_URL}}.

I am {{DISPLAY_NAME}}, based in Japan, async in {{TIMEZONE}}. Please keep scoping on Upwork Messages until a contract starts.

Two questions:
1. {{QUESTION_1}}
2. {{QUESTION_2}}
```

---

## Standard paste

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{JOB_TITLE}}". {{SCOPE_ONE_LINER}}

I am {{DISPLAY_NAME}}. I sell a scoped n8n workflow plus operator docs, not an unbounded retainer. Typical pieces: a trigger you already have (form, webhook, schedule, or a new sheet row); honest steps through {{STACK_OR_TOOL}} or an equivalent documented connector; a destination (inbox, sheet, CRM field, or internal API); retries or a failure alert; an SOP that names what starts it, what breaks, and how to rerun. Secrets stay in the credential store. The SOP does not paste them.

I will not scrape a site that has no public API. I will not automate likes, follows, comments, or fake views. I will not publish on your behalf unless you hold the posting switch.

Public notes: {{PORTFOLIO_URL}}. Fail-closed API posting example: {{GITHUB_REPO_AUTOPILOT}}.

I work in English, async in {{TIMEZONE}}, from Japan. I do not invent a US address.

What I would deliver under a contract:
1. A short map of the current copy-paste and the stop conditions
2. One working n8n path with a visible failure path
3. An operator SOP and a change note

Two questions before I outline milestones here:
1. {{QUESTION_1}}
2. {{QUESTION_2}}

Please keep chat on Upwork until a contract starts. Bid amount stays in the form fields, not in this letter.
```

---

## Fictional fill (not a real job; do not send)

- Label: `Client A` (fictional)
- Title example: `[FICTION] Build n8n: Typeform to Google Sheet plus Slack on failure`
- `{{SCOPE_ONE_LINER}}` example: `One inbound form should land as a row, and a person should see a Slack note only when the write fails.`
- `{{QUESTION_1}}` example: `Is n8n Cloud already in use, or would this be a self-hosted instance you control?`
- `{{QUESTION_2}}` example: `Who is allowed to retry a failed run — you, or anyone with the sheet?`

Do not replace the fictional label with a live client name in git.

---

## STOP

- Do not paste the fact table or the form-field rate tokens as if they were a quote
- Do not claim n8n Expert / Zapier Partner / Make Partner
- This file is not an application until a human personalizes it **and** clicks Submit later, outside this PR
