> **DRAFT_ONLY. DO NOT SEND.**  
> Operator one-shot paste for **one** Job-feed posting. Style **01** only. **GO is false.**  
> No live Contra applications from this pack. No secrets. Rates stay placeholders. Agent does not submit.

# CJ-01 one-shot — Contra Independent: n8n inbound path

Source: [PR#71](https://github.com/rimone0511/autopilot-log/pull/71) `01-n8n-inbound-path.md`.  
Playbook: [PR#86](https://github.com/rimone0511/autopilot-log/pull/86).  
Gate: [GO-GATES.md](GO-GATES.md) — `contra_apply_opportunity: false`.

If this file and PR#71 01 disagree, **PR#71 wins**.

---

## Fact table (operator; do not paste)

| key | value |
|---|---|
| pack | earn-jobs-contra-one-shot-ready-20260916 |
| id | CJ-01 |
| desk | Contra Independent |
| phase | JOBS |
| type | Application text on **one** Job-feed posting |
| seller_theme | n8n inbound path |
| mode | DRAFT_ONLY, HANDS paste, **one-shot** (this style only) |
| draft | true |
| send | **forbidden** |
| go | **false** |
| rate_in_prose | no — paid-project form only |
| chars_preview | 69 |
| chars_short | 533 |
| chars_standard | 832 |

When: you opened a **specific** Job-feed posting that asks for one inbound workflow (form, webhook, or documented connector) plus an operator can rerun it.  
When not: mass-similar applications. Scraped lists. Paid Contra Pro upsell. Browser-bot / scrape briefs. Classify-only / AI-ops-only / gate-only / sheet-only asks (those are PR#71 02–05 — out of this one-shot).

---

## Form fields (separate from prose)

| UI field | Paste / action |
|---|---|
| Paid-project name (if shown later) | `{{PROJECT_NAME}}` |
| Paid-project price (USD) | `{{FIXED_PRICE_USD}}` — official proposal flow only, after they want a project |
| Hourly (if shown) | `{{HOURLY_RATE_USD}}` |
| Timeline | `{{DELIVERY_DAYS}}` |
| Plan | Stay **Free** until a paying client; do not buy Pro from this pack |
| Email slots (if the live proposal form shows them) | Leave platform-owned. Do **not** type a new address into this letter |

Create numbers in Contra’s official proposal UI ([Paid projects](https://help.contra.com/en/articles/9322763-paid-projects)), not in git.

---

## Send gate

All unchecked. This pack does **not** send even if you later tick them locally.

- [ ] Job opened on contra.com Job feed (PR#86 LOOK done)
- [ ] `{{ONE_SPECIFIC_DETAIL}}` is from this posting
- [ ] This is the only listing for style 01
- [ ] I am not sending the same blob to a list
- [ ] No off-Contra payment pitch
- [ ] A dated human SEND GO exists **outside** this folder
- [ ] I submit the application myself — **not from this PR**

---

## List preview (first line; rewrite first)

```
I am applying to "{{JOB_TITLE}}" because of {{ONE_SPECIFIC_DETAIL}}.
```

---

## Short paste

```
I am applying to "{{JOB_TITLE}}" because of {{ONE_SPECIFIC_DETAIL}}.

I would build one n8n or official-API path: trigger, honest steps, destination, failure alert, plus an operator SOP. Secrets stay in the credential store. I do not scrape, and I do not email customers unless you hold the send switch.

Public notes: {{PORTFOLIO_URL}}. Fail-closed posting-gate example: {{GITHUB_REPO_AUTOPILOT}}.

I am {{DISPLAY_NAME}}, a Japan-based Independent. English, async {{TIMEZONE}}. Stay on Contra for payment.

Question: {{QUESTION_1}}
```

---

## Standard paste

```
I am applying to "{{JOB_TITLE}}" because of {{ONE_SPECIFIC_DETAIL}}. {{SCOPE_ONE_LINER}}

I am {{DISPLAY_NAME}}, Japan-based Independent. I deliver one documented path on {{STACK_OR_TOOL}} or an equivalent official connector: inbound trigger, named steps a non-engineer can follow, destination, failure alert, rerun note. Secrets stay in the credential store, not in the workflow JSON you screenshot.

If we continue on Contra I would propose (paid-project form, not this box):
- Milestone 1: process map and stop conditions
- Milestone 2: working workflow and failure alert
- Milestone 3: operator SOP

I will not scrape, fake engagement, or move payment off Contra for a Contra-originated project.

Public notes: {{PORTFOLIO_URL}}. {{GITHUB_REPO_AUTOPILOT}}.

Async {{TIMEZONE}}. Question: {{QUESTION_1}}. Second: {{QUESTION_2}}.
```

---

## Fictional fill (not a real opportunity; do not send)

- Label: `Client A` (fictional)
- Title example: `[FICTION] n8n: inbound form to Notion; email the operator only on failure`
- `{{SCOPE_ONE_LINER}}` example: `One documented path, one alert, one rerun page.`
- `{{QUESTION_1}}` example: `Do you already host n8n, or is standing up the host in scope?`
- `{{QUESTION_2}}` example: `Who holds the send switch if a later step emails a customer?`

Do **not** paste the `[FICTION]` title or `Client A` into Contra. They exist so you can rehearse length locally.

---

## STOP

- Rewrite `{{ONE_SPECIFIC_DETAIL}}` every time or skip
- Pro / wallet / Persona wall → stop
- Second listing of style 01 → stop (spray)
- Styles 02–05 → other files in PR#71, not this one-shot
- Do not apply from this PR
