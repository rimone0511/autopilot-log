> **DRAFT_ONLY. DO NOT SEND.**  
> No live bids. No secrets. No client PII. Rates stay placeholders. Agent does not submit.

# EN-W2-02 — Upwork: lead classify (cover letter)

## Fact table (operator; do not paste)

| key | value |
|---|---|
| pack | earn-en-proposal-wave2-20260916 |
| id | EN-W2-02 |
| desk | Upwork |
| type | Job proposal / cover letter |
| seller_theme | lead classify |
| mode | DRAFT_ONLY, HANDS paste |
| draft | true |
| send | **forbidden** |
| rate_in_prose | no — form field only |
| chars_preview | 127 |
| chars_short | 656 |
| chars_standard | 1191 |

Assumed listing type (not a real job): inbound form / inbox / sheet rows tagged (e.g. Hot / Maybe / Noise) and routed, with a human looking at the unsure bucket.

Out of scope: scraped contact lists, auto-spam sequences, fake intent scores, LinkedIn crawling, “guaranteed pipeline.”

---

## Form fields (separate from prose)

| UI field | Paste / action |
|---|---|
| Bid type | Live form: hourly **or** fixed |
| Hourly (USD) | `{{HOURLY_RATE_USD}}` |
| Fixed price (USD) | `{{FIXED_PRICE_USD}}` |
| Duration | `{{DELIVERY_DAYS}}` |
| Connects | Human per-job choice; this pack does not instruct spend |

Empty required rate → park `rate_required`. Do not invent USD in git.

---

## Send gate

- [ ] Job opened on upwork.com
- [ ] `{{ONE_SPECIFIC_DETAIL}}` is from **this** post
- [ ] The ask is classify / route / tag inbound leads — not outbound spray
- [ ] No Means of Direct Contact
- [ ] I click Submit myself

---

## List preview (first line; rewrite first)

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{JOB_TITLE}}". I would classify those inbound rows first, and only then route them.
```

---

## Short paste

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{JOB_TITLE}}". I would classify those inbound rows first, and only then route them.

I set up lead classification an operator can inspect: tags a person agrees with, a route for Hot / Maybe / Noise, and a hold bucket for anything unsure. I do not scrape contact lists. I do not send outreach from the workflow. Classification is not a promise that a lead will buy.

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

I am {{DISPLAY_NAME}}. Lead classify, for me, means: take inbound records you already own (form, inbox export, CRM field, or sheet), write down the label set, apply those labels in a way a person can sample, and route only the labels you approve. The unsure row stays in a hold queue. A human decides whether it is Hot, Maybe, or Noise. I will not invent a “score” that you cannot explain.

I connect {{STACK_OR_TOOL}} or an equivalent documented connector / official API. I will not crawl LinkedIn, buy lists, or auto-email strangers. I will not claim conversion rates I have not measured on your data.

Deliverables I would put on a milestone outline:
1. Label definitions and examples (including what is out of bounds)
2. A classification path (n8n or sheet + documented connector) with a hold bucket
3. A short SOP: how to sample, how to correct a label, what never auto-sends

Public notes: {{PORTFOLIO_URL}}. Fail-closed API example: {{GITHUB_REPO_AUTOPILOT}}.

English, async in {{TIMEZONE}}, Japan. Bid amount stays in the Upwork form, not in this letter.

Questions:
1. {{QUESTION_1}}
2. {{QUESTION_2}}
```

---

## Fictional fill (not a real job; do not send)

- Label: `Client B` (fictional)
- Title example: `[FICTION] Tag inbound demo-form rows Hot / Maybe / Noise before Slack`
- `{{SCOPE_ONE_LINER}}` example: `New form rows should get a tag a person can audit, and only Hot should ping sales.`
- `{{QUESTION_1}}` example: `What is the source of truth today — the form tool, a Sheet, or the CRM?`
- `{{QUESTION_2}}` example: `Should “unsure” wait for a human, or is a Maybe tag allowed without review?`

---

## STOP

- Do not promise lead volume, close rate, or “AI that never misses”
- Do not paste buyer emails from a listing into git
- Do not send this file
