> **DRAFT_ONLY. DO NOT SEND.**  
> No live Contra applications from this pack. No secrets. Rates stay placeholders. Agent does not submit.  
> Rewrite of PR#71 style 01 — claims rebased onto showcase P1–P3.

# Contra Independent — Job-feed proposal 01 (human-held intake)

## Fact table (operator; do not paste)

| key | value |
|---|---|
| pack | earn-showcase-proposal-pack-20260916 |
| id | CJ-SHOW-01 |
| desk | Contra Independent (active lane 2/2) |
| type | Application text on **one** Job-feed posting |
| seller_theme | Human-held inquiry intake → hold-for-human list (P1 flagship) |
| ancestor | PR#71 `01-n8n-inbound-path.md` voice; **not** n8n-as-religion |
| draft | true |
| send | **forbidden** |

**Next action:** fill `{{ONE_SPECIFIC_DETAIL}}` from **this** posting or skip.

When: the posting asks for inbound intake, form/sheet capture, dedupe, or a list a person reviews before anyone is emailed.  
When not: mass-similar applications; scrape briefs; “n8n Expert / always-on production”; Pro upsell.

Showcase links (only these PRs): [ASSETS-POINTER.md](../ASSETS-POINTER.md).

---

## Form fields (separate from prose)

| UI field | Paste / action |
|---|---|
| Paid-project name (if shown later) | `{{PROJECT_NAME}}` |
| Paid-project price (USD) | `{{FIXED_PRICE_USD}}` — policy token `{{PRICE}}` |
| Hourly (if shown) | `{{HOURLY_RATE_USD}}` |
| Timeline | `{{DELIVERY_DAYS}}` |
| Plan | Stay **Free**. Do not buy Pro from this pack |
| Email slots | Leave platform-owned |

Create numbers in Contra’s official proposal UI ([Paid projects](https://help.contra.com/en/articles/9322763-paid-projects)), not in git.

---

## Send gate

- [ ] Job opened on contra.com (`{{TARGET_URL}}`)
- [ ] `{{ONE_SPECIFIC_DETAIL}}` is from this posting
- [ ] This is the only listing for this style (no spray)
- [ ] No off-Contra payment pitch
- [ ] FACTS.md forbidden list is still empty
- [ ] I submit myself — **not from this PR**

---

## List preview (first line; rewrite first)

```
I am applying to "{{JOB_TITLE}}" because of {{ONE_SPECIFIC_DETAIL}}.
```

---

## Short paste

```
I am applying to "{{JOB_TITLE}}" because of {{ONE_SPECIFIC_DETAIL}}.

I would build one human-held intake: validate inbound rows, surface duplicates, and stop on a hold-for-human list. Ambiguous or colliding rows do not become “ready to send.” I do not add send nodes. n8n is optional — a table plus a script is enough when that is the smaller fit.

Public synthetic demo (not a client case): https://github.com/rimone0511/autopilot-log/pull/115 (head 541bb18). Duplicate inquiry_id holds every collided row. CSV matches JSON. --check leaves git clean.

I am {{DISPLAY_NAME}}, a Japan-based Independent. English, async {{TIMEZONE}}. Stay on Contra for payment.

Question: {{QUESTION_1}}
```

---

## Standard paste

```
I am applying to "{{JOB_TITLE}}" because of {{ONE_SPECIFIC_DETAIL}}. {{SCOPE_ONE_LINER}}

I am {{DISPLAY_NAME}}, Japan-based Independent. I sell a documented intake a person can stop: inbound rows → validate → dedupe / id-collision hold → a hold-for-human list. Ready rows are still not sent. n8n is an implementation option (inactive samples only). I will not treat n8n as mandatory.

Public synthetic showcase (self-made; no live customers):
- Inquiry intake — https://github.com/rimone0511/autopilot-log/pull/115 head 541bb18. Validate, dedupe, hold-for-human. Duplicate inquiry_id → needs_human on every collided row. CSV = JSON. --check clean.
- Optional weekly CSV with source / #Ln / SHA-256 of the file actually read, timezone-aware — https://github.com/rimone0511/autopilot-log/pull/117 + https://github.com/rimone0511/autopilot-log/pull/120 head 14b818c.
- Optional fail-stop — https://github.com/rimone0511/autopilot-log/pull/116 head 0a822e0. Timeout is not approve. Actorless, missing, or reused event IDs do not write.

Independent QA (FACTS-limited prep only, not a production audit): https://github.com/rimone0511/autopilot-log/pull/121

I will not claim production n8n, revenue, hours saved, or accuracy %.

If we continue on Contra I would propose (paid-project form, not this box):
- Milestone 1: process map and stop conditions
- Milestone 2: working intake → hold list on your sample (PII stripped)
- Milestone 3: operator SOP; send switch stays with you

I will not scrape, fake engagement, or move payment off Contra for a Contra-originated project.

Public notes: {{PORTFOLIO_URL}}. {{GITHUB_REPO_AUTOPILOT}}.

Async {{TIMEZONE}}. Question: {{QUESTION_1}}. Second: {{QUESTION_2}}.
```

---

## Fictional fill (not a real opportunity; do not send)

- Label: `Client A` (fictional)
- Title example: `[FICTION] Inbound form rows to a review list; do not email the lead`
- `{{SCOPE_ONE_LINER}}` example: `One intake, one hold list, no send node.`
- `{{ONE_SPECIFIC_DETAIL}}` example: `You asked for duplicate form submits to stay visible, not silently merged.`
- `{{QUESTION_1}}` example: `Do you already host n8n, or is a spreadsheet-first path in scope?`
- `{{QUESTION_2}}` example: `Who holds the send switch if a later step emails a customer?`

---

## STOP

- Rewrite `{{ONE_SPECIFIC_DETAIL}}` every time or skip
- Pro / wallet / Persona wall → stop
- Do not apply from this PR
- Do not write “SOL cleared twice”
