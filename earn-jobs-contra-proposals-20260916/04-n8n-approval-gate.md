> **DRAFT_ONLY. DO NOT SEND.**  
> No live Contra applications from this pack. No secrets. Rates stay placeholders. Agent does not submit.

# CJ-04 — Contra Independent: n8n fail-closed approval / posting gate (one Job-feed posting)

## Fact table (operator; do not paste)

| key | value |
|---|---|
| pack | earn-jobs-contra-proposals-20260916 |
| id | CJ-04 |
| desk | Contra Independent |
| phase | JOBS |
| type | Application text on **one** Job-feed posting |
| seller_theme | n8n approval / posting gate |
| mode | DRAFT_ONLY, HANDS paste, one listing this style |
| draft | true |
| send | **forbidden** |
| rate_in_prose | no — paid-project form only |
| chars_preview | 124 |
| chars_short | 541 |
| chars_standard | 817 |

Assumed ask: automation may **run**; send or publish stays a **separate human switch** that fails closed.  
Decline: ungated public posting, engagement pods, “post TikTok unattended” (this seller’s public tool defaults to inbox upload; direct post is gated).

---

## Form fields (separate from prose)

| UI field | Paste / action |
|---|---|
| Paid-project name (if shown later) | `{{PROJECT_NAME}}` |
| Paid-project price (USD) | `{{FIXED_PRICE_USD}}` |
| Hourly (if shown) | `{{HOURLY_RATE_USD}}` |
| Timeline | `{{DELIVERY_DAYS}}` |
| Email slots (if shown) | Leave platform-owned. Do not type a new address into this letter |

---

## Send gate

- [ ] Job opened on contra.com Job feed
- [ ] `{{ONE_SPECIFIC_DETAIL}}` is from this posting
- [ ] This is the only listing for style 04
- [ ] A human stop before send/publish is acceptable
- [ ] Not an engagement / scrape brief
- [ ] I do not submit from this PR

---

## List preview (first line; rewrite first)

```
I am applying to "{{JOB_TITLE}}" because of {{ONE_SPECIFIC_DETAIL}}. The workflow can run; publish stays a separate switch.
```

---

## Short paste

```
I am applying to "{{JOB_TITLE}}" because of {{ONE_SPECIFIC_DETAIL}}.

I treat “the automation is running” and “it may send or publish” as two switches. The second fails closed: missing, unreadable, or malformed gate means no public send. I wire that in n8n or an official API, plus an operator SOP. I do not scrape and I do not fake engagement.

Public notes: {{PORTFOLIO_URL}}. Public fail-closed upload example: {{GITHUB_REPO_AUTOPILOT}}.

{{DISPLAY_NAME}}, Japan-based Independent, {{TIMEZONE}}. Stay on Contra.

Question: {{QUESTION_1}}
```

---

## Standard paste

```
I am applying to "{{JOB_TITLE}}" because of {{ONE_SPECIFIC_DETAIL}}. {{SCOPE_ONE_LINER}}

I am {{DISPLAY_NAME}}. For this posting I would: map the path on {{STACK_OR_TOOL}} or a documented connector, put a fail-closed gate in front of send/publish, log the refuse reason without printing secrets, and leave a one-page rerun note. Default is private / draft / operator-only. Opening the gate is a deliberate human act.

I will not claim unattended TikTok direct-post. Inbox-then-human-review is the honest default. I will not like, follow, comment, or view on a schedule.

If we continue on Contra, paid-project milestones would be: gate spec → working refuse/allow path → SOP. Amounts stay in the proposal form.

Public notes: {{PORTFOLIO_URL}}. {{GITHUB_REPO_AUTOPILOT}}.

Questions: {{QUESTION_1}} / {{QUESTION_2}}
```

---

## Fictional fill (not a real opportunity; do not send)

- Label: `Client D` (fictional)
- Title example: `[FICTION] n8n: prepare a YouTube draft; do not publish unless an operator file allows it`
- `{{SCOPE_ONE_LINER}}` example: `Prepare the asset; keep public send behind a fail-closed gate.`
- `{{QUESTION_1}}` example: `Which action is gated — email, social publish, or both?`
- `{{QUESTION_2}}` example: `If the gate file is missing, should the run stop or fall back to private/draft?`

---

## STOP

- Pass if they want ungated public posting or engagement automation
- Pro / wallet / Persona wall → stop
- Do not apply from this PR
