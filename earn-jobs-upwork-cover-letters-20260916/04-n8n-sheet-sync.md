> **DRAFT_ONLY. DO NOT SEND.**  
> JOBS PHASE. Upwork cover letter only. No live bids. No secrets. No client PII.  
> Rates stay placeholders. Account may be blocked — agent does not submit.

# JOBS-04 — Upwork: n8n Google Sheet sync (cover letter)

## Fact table (operator; do not paste)

See pack-level [FACT-TABLE.md](FACT-TABLE.md). Per-file copy:

| key | value |
|---|---|
| pack | earn-jobs-upwork-cover-letters-20260916 |
| id | JOBS-04 |
| desk | Upwork |
| type | Job proposal / cover letter |
| seller_theme | n8n Google Sheet sync |
| phase | JOBS |
| mode | DRAFT_ONLY, HANDS paste |
| draft | true |
| send | **forbidden** (account may be blocked; even if not, this file does not send) |
| rate_in_prose | no — form field only |
| chars_preview | 133 |
| chars_short | 673 |
| chars_standard | 1047 |

Assumed listing type (not a real job): inbound sheet row notifies a human. Nothing auto-sends. `auto_send` / empty / already-sent fail closed. Live spreadsheet IDs stay out of git.

Out of scope: auto-reply, live send nodes committed here, browser bots, n8n hosting as a service, fake partner badges.

---

## Form fields (separate from prose)

| UI field | Paste / action |
|---|---|
| Bid type | Live form: hourly **or** fixed |
| Hourly (USD) | `{{HOURLY_RATE_USD}}` |
| Fixed price (USD) | `{{FIXED_PRICE_USD}}` |
| Duration | `{{DELIVERY_DAYS}}` |
| Connects | Human per-job choice later. This pack: **do not spend, do not send** |

Empty required rate → park `rate_required`. Do not invent USD in git.

---

## Send gate

- [ ] Upwork account is actually usable (today: treat as **may be blocked**)
- [ ] Job opened on upwork.com
- [ ] `{{ONE_SPECIFIC_DETAIL}}` is from this post
- [ ] The ask is sheet inbound → human notify, not auto-email from the row
- [ ] No spreadsheet IDs / secrets in the letter
- [ ] I would click Submit myself — **not now**

---

## List preview (first line; rewrite first)

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{JOB_TITLE}}". I would sync that inbound sheet row to a human ping, and refuse auto-send.
```

---

## Short paste

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{JOB_TITLE}}". I would sync that inbound sheet row to a human ping, and refuse auto-send.

I build n8n Google Sheet sync an operator can rerun: a new or changed row notifies a person; `auto_send`, empty, and already-sent fail closed. I use the documented Google Sheets connector / official API, not a browser robot. Spreadsheet IDs and tokens stay in your credential store, not in the SOP paste.

Public notes: {{PORTFOLIO_URL}}. Fail-closed example: {{GITHUB_REPO_AUTOPILOT}}.

I am {{DISPLAY_NAME}}, Japan-based, async in {{TIMEZONE}}. Please keep scoping on Upwork Messages.

Two questions:
1. {{QUESTION_1}}
2. {{QUESTION_2}}
```

---

## Standard paste

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{JOB_TITLE}}". {{SCOPE_ONE_LINER}}

I am {{DISPLAY_NAME}}. Sheet sync, here, means: inbound rows you already own land in a sheet you control; n8n notices the row through {{STACK_OR_TOOL}} or the documented Google Sheets connector; a human gets a ping; nothing emails or posts from that row unless you later add a separate, gated path. Empty destination, `auto_send`, and already-sent all fail closed.

I will not paste live spreadsheet IDs into this letter or into git. I will not scrape a sheet from a URL that is not yours. I will not claim I host n8n for you as a product.

Deliverables I would outline:
1. Column map (what a row means; which fields must never leave the sheet)
2. One n8n inbound path + human notify; outbound send stays off
3. SOP: how to add a column, how to replay a row, where credentials live

Public notes: {{PORTFOLIO_URL}}. {{GITHUB_REPO_AUTOPILOT}}.

English, async in {{TIMEZONE}}, Japan. Bid amount stays in the form fields.

Questions:
1. {{QUESTION_1}}
2. {{QUESTION_2}}
```

---

## Fictional fill (not a real job; do not send)

- Label: `Job-D` (fictional)
- Title example: `[FICTION] n8n: new intake-sheet row pings Slack; do not email the submitter`
- `{{SCOPE_ONE_LINER}}` example: `A new row should notify ops; the submitter must not get an auto-email from this workflow.`
- `{{QUESTION_1}}` example: `Is the sheet already the source of truth, or does a form write it first?`
- `{{QUESTION_2}}` example: `Which columns are operator-only and must never appear in a notify?`

---

## STOP

- Do not commit spreadsheet IDs, tokens, or row dumps
- Do not offer auto-email from the sheet
- Do not send
