> **DRAFT_ONLY. DO NOT SEND.**  
> No live Contra applications from this pack. No secrets. Rates stay placeholders. Agent does not submit.

# EN-W2-09 — Contra: n8n workflow (one public opportunity)

## Fact table (operator; do not paste)

| key | value |
|---|---|
| pack | earn-en-proposal-wave2-20260916 |
| id | EN-W2-09 |
| desk | Contra |
| type | Application text on **one** public opportunity |
| seller_theme | n8n workflow |
| mode | DRAFT_ONLY, HANDS paste |
| draft | true |
| send | **forbidden** |
| rate_in_prose | no — paid-project form only |
| chars_preview | 69 |
| chars_short | 502 |
| chars_standard | 711 |

When: you clicked through a **specific** public opportunity in the Contra UI.  
When not: mass-similar applications. Scraped lists. Paid Contra Pro upsell (not instructed).

---

## Form fields (separate from prose)

| UI field | Paste / action |
|---|---|
| Paid-project price (USD) | `{{FIXED_PRICE_USD}}` — official proposal flow only, after they want a project |
| Hourly (if shown) | `{{HOURLY_RATE_USD}}` |
| Timeline | `{{DELIVERY_DAYS}}` |
| Plan | Stay **Free** until a paying client; do not buy Pro from this pack |

Create numbers in Contra’s official proposal UI ([Paid projects](https://help.contra.com/en/articles/9322763-paid-projects)), not in git.

---

## Send gate

- [ ] Opportunity opened on contra.com
- [ ] `{{ONE_SPECIFIC_DETAIL}}` is from this posting
- [ ] I am not sending the same blob to a list
- [ ] No off-Contra payment pitch
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

I help small teams replace copy-paste with an n8n or official-API workflow plus docs a non-engineer can follow. Public notes: {{PORTFOLIO_URL}}. API-only upload tool with a fail-closed posting gate: {{GITHUB_REPO_AUTOPILOT}}.

I am {{DISPLAY_NAME}}, a Japan-based independent. English, async in {{TIMEZONE}}.

I will not scrape, fake engagement, or take a Contra-originated project off Contra for payment.

Question: {{QUESTION_1}}
```

---

## Standard paste

```
I am applying to "{{JOB_TITLE}}" because of {{ONE_SPECIFIC_DETAIL}}. {{SCOPE_ONE_LINER}}

I am {{DISPLAY_NAME}}, Japan-based. I deliver one n8n path on {{STACK_OR_TOOL}} or an equivalent documented connector: trigger, honest steps, destination, failure alert, operator SOP. Secrets stay in the credential store.

If we continue on Contra I would propose (paid-project form, not this box):
- Milestone 1: process map and stop conditions
- Milestone 2: working workflow and failure alert
- Milestone 3: operator SOP

I will not scrape, fake engagement, or move payment off Contra.

Public notes: {{PORTFOLIO_URL}}. {{GITHUB_REPO_AUTOPILOT}}.

Async {{TIMEZONE}}. Question: {{QUESTION_1}}. Second: {{QUESTION_2}}.
```

---

## Fictional fill (not a real opportunity; do not send)

- Label: `Client I` (fictional)
- Title example: `[FICTION] n8n: inbound form to Notion; email the operator only on failure`
- `{{SCOPE_ONE_LINER}}` example: `One documented path, one alert, one rerun page.`
- `{{QUESTION_1}}` example: `Do you already have n8n, or is standing up the host in scope?`
- `{{QUESTION_2}}` example: `Who holds the posting/send switch if a later step emails a customer?`

---

## STOP

- Rewrite `{{ONE_SPECIFIC_DETAIL}}` every time or skip
- Do not apply from this PR
