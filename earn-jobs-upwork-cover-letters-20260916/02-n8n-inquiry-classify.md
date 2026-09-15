> **DRAFT_ONLY. DO NOT SEND.**  
> JOBS PHASE. Upwork cover letter only. No live bids. No secrets. No client PII.  
> Rates stay placeholders. Account may be blocked — agent does not submit.

# JOBS-02 — Upwork: n8n inquiry classify (cover letter)

## Fact table (operator; do not paste)

See pack-level [FACT-TABLE.md](FACT-TABLE.md). Per-file copy:

| key | value |
|---|---|
| pack | earn-jobs-upwork-cover-letters-20260916 |
| id | JOBS-02 |
| desk | Upwork |
| type | Job proposal / cover letter |
| seller_theme | n8n inquiry classify |
| phase | JOBS |
| mode | DRAFT_ONLY, HANDS paste |
| draft | true |
| send | **forbidden** (account may be blocked; even if not, this file does not send) |
| rate_in_prose | no — form field only |
| chars_preview | 153 |
| chars_short | 716 |
| chars_standard | 1255 |

Assumed listing type (not a real job): inbound form / inbox / sheet rows tagged (billing / support / sales / uncertain) and routed, with a human looking at the hold bucket. Send stays human.

Out of scope: scraped contact lists, auto-reply, auto-spam sequences, fake intent scores, LinkedIn crawling, “guaranteed pipeline.”

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
- [ ] `{{ONE_SPECIFIC_DETAIL}}` is from **this** post
- [ ] The ask is classify / route / tag inbound inquiries — not outbound spray
- [ ] No Means of Direct Contact
- [ ] I would click Submit myself — **not now**

---

## List preview (first line; rewrite first)

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{JOB_TITLE}}". I would label those inbound inquiries first, hold the unsure ones, and leave send to a person.
```

---

## Short paste

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{JOB_TITLE}}". I would label those inbound inquiries first, hold the unsure ones, and leave send to a person.

I set up n8n inquiry classification an operator can inspect: tags a person agrees with (for example billing / support / sales / uncertain), a route for the clear labels, and a hold queue for anything unsure. I do not scrape contact lists. I do not auto-reply. Classification is not a promise that a lead will buy.

Public notes: {{PORTFOLIO_URL}}. Same inspectable-automation habit: {{GITHUB_REPO_AUTOPILOT}}.

I am {{DISPLAY_NAME}}, Japan-based, async in {{TIMEZONE}}. Please keep scoping on Upwork Messages.

Two questions:
1. {{QUESTION_1}}
2. {{QUESTION_2}}
```

---

## Standard paste

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{JOB_TITLE}}". {{SCOPE_ONE_LINER}}

I am {{DISPLAY_NAME}}. Inquiry classify, for me, means: take inbound records you already own (form, inbox export, CRM field, or sheet), write down the label set, apply those labels in n8n in a way a person can sample, and route only the labels you approve. The unsure row stays in a hold queue. A human decides the next step. I will not invent a “score” that you cannot explain, and I will not attach a live send node.

I connect {{STACK_OR_TOOL}} or an equivalent documented connector / official API. I will not crawl LinkedIn, buy lists, or auto-email strangers. I will not claim conversion rates I have not measured on your data. Accuracy percentages do not belong in this letter.

Deliverables I would put on a milestone outline:
1. Label definitions and examples (including what is out of bounds)
2. An n8n classification path with a hold bucket and no auto-send
3. A short SOP: how to sample, how to correct a label, what never auto-sends

Public notes: {{PORTFOLIO_URL}}. Fail-closed API example: {{GITHUB_REPO_AUTOPILOT}}.

English, async in {{TIMEZONE}}, Japan. Bid amount stays in the Upwork form, not in this letter.

Questions:
1. {{QUESTION_1}}
2. {{QUESTION_2}}
```

---

## Fictional fill (not a real job; do not send)

- Label: `Job-B` (fictional)
- Title example: `[FICTION] n8n: tag inbound demo-form rows billing / support / sales / uncertain`
- `{{SCOPE_ONE_LINER}}` example: `New form rows should get a tag a person can audit, and only a human may send a reply.`
- `{{QUESTION_1}}` example: `What is the source of truth today — the form tool, a Sheet, or the CRM?`
- `{{QUESTION_2}}` example: `Should “uncertain” wait for a human, or is a Maybe tag allowed without review?`

---

## STOP

- Do not promise lead volume, close rate, or “AI that never misses”
- Do not paste buyer emails from a listing into git
- Do not send this file
