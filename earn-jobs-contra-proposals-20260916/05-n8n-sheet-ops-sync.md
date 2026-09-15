> **DRAFT_ONLY. DO NOT SEND.**  
> No live Contra applications from this pack. No secrets. Rates stay placeholders. Agent does not submit.

# CJ-05 — Contra Independent: n8n sheet / ops sync (one Job-feed posting)

## Fact table (operator; do not paste)

| key | value |
|---|---|
| pack | earn-jobs-contra-proposals-20260916 |
| id | CJ-05 |
| desk | Contra Independent |
| phase | JOBS |
| type | Application text on **one** Job-feed posting |
| seller_theme | n8n sheet / ops sync |
| mode | DRAFT_ONLY, HANDS paste, one listing this style |
| draft | true |
| send | **forbidden** |
| rate_in_prose | no — paid-project form only |
| chars_preview | 106 |
| chars_short | 496 |
| chars_standard | 835 |

Assumed ask: keep a spreadsheet or ops table in sync with a documented API / connector; operator can rerun.  
Decline: scraping a site with no official API; dumping API keys into cells; using the sheet as a secret store.

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
- [ ] This is the only listing for style 05
- [ ] Source and destination have a documented connector or official API
- [ ] No “scrape the dashboard” brief
- [ ] I do not submit from this PR

---

## List preview (first line; rewrite first)

```
I am applying to "{{JOB_TITLE}}" because of {{ONE_SPECIFIC_DETAIL}}. One documented sync, one rerun page.
```

---

## Short paste

```
I am applying to "{{JOB_TITLE}}" because of {{ONE_SPECIFIC_DETAIL}}.

I would wire one n8n or official-API sync into {{STACK_OR_TOOL}}: named columns, honest retries, failure alert to the operator, SOP a non-engineer can follow. Credentials stay in the secret store, not in the sheet. I do not scrape a UI that has no API.

Public notes: {{PORTFOLIO_URL}}. {{GITHUB_REPO_AUTOPILOT}}.

{{DISPLAY_NAME}}, Japan-based Independent, {{TIMEZONE}}. Stay on Contra for payment.

Question: {{QUESTION_1}}
```

---

## Standard paste

```
I am applying to "{{JOB_TITLE}}" because of {{ONE_SPECIFIC_DETAIL}}. {{SCOPE_ONE_LINER}}

I am {{DISPLAY_NAME}}. For this posting I would: list the source and destination, confirm both have a documented connector, map columns, set a schedule or a manual trigger, alert the operator on failure, and leave a rerun page. I will not put keys in cells. I will not invent a “live dashboard” that is actually a scrape.

If we continue on Contra I would propose (paid-project form, not this box):
- Milestone 1: field map and stop conditions
- Milestone 2: working sync + failure alert
- Milestone 3: operator SOP

I will not scrape, fake engagement, or move payment off Contra for a Contra-originated project.

Public notes: {{PORTFOLIO_URL}}. {{GITHUB_REPO_AUTOPILOT}}.

Async {{TIMEZONE}}. Question: {{QUESTION_1}}. Second: {{QUESTION_2}}.
```

---

## Fictional fill (not a real opportunity; do not send)

- Label: `Client E` (fictional)
- Title example: `[FICTION] n8n: nightly Google Sheet sync from a CRM export API; Slack only on failure`
- `{{SCOPE_ONE_LINER}}` example: `Official connector both sides; no keys in cells; operator alert on fail.`
- `{{QUESTION_1}}` example: `Is the source an official API / export, or a logged-in HTML page? (HTML scrape → I pass.)`
- `{{QUESTION_2}}` example: `Who owns the credential store, and who may rerun the workflow?`

---

## STOP

- Pass if they want scraping or keys-in-sheet
- Pro / wallet / Persona wall → stop
- Do not apply from this PR
