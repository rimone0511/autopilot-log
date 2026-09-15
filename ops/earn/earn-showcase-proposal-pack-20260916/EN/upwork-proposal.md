> **DRAFT_ONLY. DO NOT SEND.**  
> Thin EN variant. Active lanes are Coconala + Contra. Do not spend Connects. Do not submit.  
> Account may be blocked — treat as not usable until a later GO. Agent does not bid.

# Upwork — one cover letter (human-held intake)

## Fact table (operator; do not paste)

| key | value |
|---|---|
| pack | earn-showcase-proposal-pack-20260916 |
| desk | Upwork (thin / parked) |
| type | Job proposal / cover letter |
| seller_theme | Human-held inquiry intake → hold-for-human list |
| phase | parked unless a lane-swap GO |
| draft | true |
| send | **forbidden** |
| connects | **do not spend** |

**Next action:** if there is no explicit lane-swap GO, close this file.

Assumed listing type (not a real job): inbound rows → a person-reviewed hold list; no auto-email.

---

## Form fields (separate from prose)

| UI field | Paste / action |
|---|---|
| Bid type | Live form: hourly **or** fixed — not both in the letter |
| Hourly (USD) | `{{HOURLY_RATE_USD}}` |
| Fixed price (USD) | `{{FIXED_PRICE_USD}}` — policy token `{{PRICE}}` |
| Duration | `{{DELIVERY_DAYS}}` |
| Connects | **Do not spend** from this pack |

Empty required rate → park `rate_required`. Do not invent USD.

---

## Send gate

- [ ] A later human **swapped** an active lane to Upwork
- [ ] Account is actually usable (today: treat as **may be blocked**)
- [ ] Job opened on upwork.com (`{{TARGET_URL}}`)
- [ ] `{{ONE_SPECIFIC_DETAIL}}` is unique to this post
- [ ] No email / phone / messenger
- [ ] I would click Submit myself — **not now**, and **not if Connects would be spent**

---

## List preview (first line; rewrite first)

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{JOB_TITLE}}". I would treat that as a human-held intake, not an auto-reply bot.
```

---

## Short paste

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{JOB_TITLE}}". I would treat that as a human-held intake, not an auto-reply bot.

I build intake that a person can stop: validate rows, surface duplicates and colliding IDs, and output a hold-for-human list. I do not add send nodes. n8n is optional; official APIs or a spreadsheet path are in scope. I do not scrape. I do not use browser automation.

Public synthetic demo (not a client case): https://github.com/rimone0511/autopilot-log/pull/115 (head 541bb18). Duplicate inquiry_id holds every collided row. CSV matches JSON. --check clean.

I am {{DISPLAY_NAME}}, based in Japan, async {{TIMEZONE}}. Please keep scoping on Upwork Messages until a contract starts.

Two questions:
1. {{QUESTION_1}}
2. {{QUESTION_2}}
```

---

## Standard paste

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{JOB_TITLE}}". {{SCOPE_ONE_LINER}}

I am {{DISPLAY_NAME}}. I sell a scoped human-held intake plus operator docs, not an unbounded retainer. Typical pieces: inbound rows you already have; validate; dedupe / colliding-id hold; a hold-for-human list; an SOP that names what starts it and who holds the send switch. n8n is an implementation option, not a requirement. Secrets stay in your store.

Public synthetic showcase (self-made; no live customers):
- Intake — https://github.com/rimone0511/autopilot-log/pull/115 head 541bb18. Validate, dedupe, hold-for-human. Duplicate inquiry_id → needs_human on every collided row. CSV = JSON.
- Optional weekly CSV with source / #Ln / SHA-256, timezone-aware — https://github.com/rimone0511/autopilot-log/pull/117 + https://github.com/rimone0511/autopilot-log/pull/120 head 14b818c.
- Optional fail-stop — https://github.com/rimone0511/autopilot-log/pull/116 head 0a822e0. Timeout is not approve. Actorless, missing, or reused event IDs do not write.

QA for FACTS-limited proposal prep only: https://github.com/rimone0511/autopilot-log/pull/121. I will not claim production n8n, revenue, hours saved, or accuracy %.

I work in English, async in {{TIMEZONE}}, from Japan. I do not invent a US address.

What I would deliver under a contract:
1. A short map of the current copy-paste and the stop conditions
2. One working intake → hold list on a PII-stripped sample
3. An operator SOP

Two questions:
1. {{QUESTION_1}}
2. {{QUESTION_2}}

Please keep chat on Upwork until a contract starts. Bid amount stays in the form fields, not in this letter.
```

---

## Fictional fill (not a real job; do not send)

- Label: `Job-A` (fictional)
- Title example: `[FICTION] Form submissions to a review sheet; do not email the sender`
- `{{SCOPE_ONE_LINER}}` example: `One intake path and a hold list a non-engineer can rerun.`
- `{{QUESTION_1}}` example: `Is n8n already in use, or is a spreadsheet-first path better?`
- `{{QUESTION_2}}` example: `Who is allowed to mark a hold row as sendable?`

Do not replace the fictional label with a live client name in git.

---

## STOP

- Do not spend Connects
- Do not claim n8n Expert / Zapier Partner
- Do not send while the account may be blocked
- This file is not an application
