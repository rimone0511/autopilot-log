> **DRAFT_ONLY. DO NOT SEND.**  
> JOBS PHASE. Upwork cover letter only. No live bids. No secrets. No client PII.  
> Rates stay placeholders. Account may be blocked — agent does not submit.

# JOBS-03 — Upwork: n8n approval gate (cover letter)

## Fact table (operator; do not paste)

See pack-level [FACT-TABLE.md](FACT-TABLE.md). Per-file copy:

| key | value |
|---|---|
| pack | earn-jobs-upwork-cover-letters-20260916 |
| id | JOBS-03 |
| desk | Upwork |
| type | Job proposal / cover letter |
| seller_theme | n8n approval gate |
| phase | JOBS |
| mode | DRAFT_ONLY, HANDS paste |
| draft | true |
| send | **forbidden** (account may be blocked; even if not, this file does not send) |
| rate_in_prose | no — form field only |
| chars_preview | 169 |
| chars_short | 641 |
| chars_standard | 1092 |

Assumed listing type (not a real job): a notify or draft is prepared, then a person must approve before anything leaves the building. Reject / missing / unknown / timeout fail closed. No auto-send-on-timeout.

Out of scope: auto-reply, live send without a gate, browser bots, “SLA: we send if you do not answer.”

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
- [ ] The ask is a human gate before outbound, not “send if nobody clicks”
- [ ] No contact details in the letter
- [ ] I would click Submit myself — **not now**

---

## List preview (first line; rewrite first)

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{JOB_TITLE}}". I would put a human approve step in front of any outbound notify, and fail closed if that click never happens.
```

---

## Short paste

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{JOB_TITLE}}". I would put a human approve step in front of any outbound notify, and fail closed if that click never happens.

I build n8n approval gates: draft or hold the notify, require an explicit approve, and treat reject / missing / unknown / timeout as “do not send.” I do not add an auto-send-on-timeout. Secrets stay in the credential store, not in the approval note.

Public notes: {{PORTFOLIO_URL}}. Same fail-closed habit: {{GITHUB_REPO_AUTOPILOT}}.

I am {{DISPLAY_NAME}}, Japan-based, async in {{TIMEZONE}}. Keep scoping on Upwork.

Two questions:
1. {{QUESTION_1}}
2. {{QUESTION_2}}
```

---

## Standard paste

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{JOB_TITLE}}". {{SCOPE_ONE_LINER}}

I am {{DISPLAY_NAME}}. An n8n approval gate, here, is a posting switch for outbound: (1) the workflow may prepare a draft notify, (2) a named person must approve, (3) reject / missing / unknown / timeout do not send, (4) the SOP names who holds the switch and how to rerun a held item. {{STACK_OR_TOOL}} is fine if it is a documented connector. I will not wire a live send node that fires because a timer expired.

I will not scrape, auto-DM, or publish on your behalf. I will not claim an SLA for “we send if you are asleep.” I will not put WhatsApp or email in this letter.

Deliverables I would outline:
1. Gate rules on one page (approve / reject / fail closed)
2. One n8n path that holds until approve; outbound stays off until you say so
3. An operator SOP: who clicks, what a timeout does (nothing), where secrets live

Public notes: {{PORTFOLIO_URL}}. {{GITHUB_REPO_AUTOPILOT}}.

English, async in {{TIMEZONE}}, Japan. Price stays in the Upwork bid fields.

Questions:
1. {{QUESTION_1}}
2. {{QUESTION_2}}
```

---

## Fictional fill (not a real job; do not send)

- Label: `Job-C` (fictional)
- Title example: `[FICTION] n8n: Slack draft for new Stripe events; human must approve before email`
- `{{SCOPE_ONE_LINER}}` example: `A new event may draft a note; nothing emails the customer unless a person approves.`
- `{{QUESTION_1}}` example: `Who is allowed to approve — one owner, or a small on-call list?`
- `{{QUESTION_2}}` example: `If nobody answers for a day, should the item stay held, or should it be marked expired without sending?`

---

## STOP

- Do not offer auto-send-on-timeout
- Do not claim partner badges
- Do not send
