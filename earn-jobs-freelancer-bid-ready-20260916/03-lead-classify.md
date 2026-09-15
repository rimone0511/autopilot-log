> **DRAFT_ONLY. DO NOT SEND.**  
> JOBS PHASE. Ready to paste **after an account exists**.  
> No live bids. No secrets. No client PII. Rates stay placeholders. Agent does not submit.  
> **One listing of this style, then stop.** Default remains do-not-send.

# FL-JOB-03 — Freelancer.com: lead classify / inbound route (bid proposal)

## Fact table (operator; do not paste)

| key | value |
|---|---|
| pack | earn-jobs-freelancer-bid-ready-20260916 |
| id | FL-JOB-03 |
| desk | Freelancer.com |
| phase | JOBS (paste after account exists) |
| listing_style | **lead classify / inbound route** (fixed *or* hourly form; one listing) |
| type | Bid proposal body |
| seller_theme | lead classify |
| mode | DRAFT_ONLY, HANDS paste, surgical (one listing) |
| draft | true |
| send | **forbidden** (default do-not-send) |
| signup | **forbidden** |
| spray | **forbidden** |
| one_specific_detail | **required** — skip if empty |
| rate_in_prose | no — form field only |
| fees_in_git | no — https://www.freelancer.com/feesandcharges only |
| chars_preview | 131 |
| chars_short | 659 |
| chars_standard | 1273 |

Assumed listing type (not a real job): inbound form / inbox / sheet rows tagged (e.g. Hot / Maybe / Noise) and routed, with a human looking at the unsure bucket.

Out of scope: scraped contact lists, auto-spam sequences, fake intent scores, LinkedIn crawling, “guaranteed pipeline,” contests, Preferred/Recruiter-only rows.

If the listing is “build one n8n path” without classify/route, use [01-fixed-price-n8n.md](01-fixed-price-n8n.md). If it is ongoing AI ops with a send/publish gate, use [02-hourly-ai-ops.md](02-hourly-ai-ops.md).

---

## Fill order (local; still do-not-send)

1. Account exists? If not → [ACCOUNT-PRECONDITION.md](ACCOUNT-PRECONDITION.md) and stop.
2. `{{ONE_SPECIFIC_DETAIL}}` from **this** listing only. Empty → skip.
3. `{{PROJECT_TITLE}}` `{{SCOPE_ONE_LINER}}` `{{STACK_OR_TOOL}}` `{{QUESTION_1}}` `{{QUESTION_2}}`
4. Form fields (not prose): `{{BID_AMOUNT_USD}}` **or** `{{HOURLY_RATE_USD}}`, plus `{{DELIVERY_DAYS}}` if the fixed form asks
5. Re-read https://www.freelancer.com/feesandcharges. Do not copy amounts.

---

## Form fields (separate from prose)

| UI field | Paste / action |
|---|---|
| Bid type | Live form: **fixed** or **hourly** — match the listing; do not write a second price in the letter |
| Bid amount (USD) | `{{BID_AMOUNT_USD}}` if fixed |
| Hourly rate (USD) | `{{HOURLY_RATE_USD}}` if hourly |
| Delivery time | `{{DELIVERY_DAYS}}` if the fixed form asks |
| Sponsored / Highlight / Sealed | **skip** |
| Proposal body | Fenced paste below, after `{{ONE_SPECIFIC_DETAIL}}` is filled |

Empty required rate → park `rate_required`. Do not invent USD in git. Do not send from this file.

---

## Send gate

- [ ] Seller account already exists (not created by this pack)
- [ ] Project opened on freelancer.com
- [ ] The ask is classify / route / tag **inbound** leads — not outbound spray
- [ ] `{{ONE_SPECIFIC_DETAIL}}` is from **this** post
- [ ] I have **not** already used this style file on another listing
- [ ] Not a contest; not Recruiter-only
- [ ] No email / phone / messenger
- [ ] Live form does not demand wallet funding, KYC, membership, or a bid upgrade
- [ ] I click Bid myself — **not from this PR**

---

## List preview (first line; rewrite first)

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{PROJECT_TITLE}}". I would classify those inbound rows first, and only then route them.
```

---

## Short paste

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{PROJECT_TITLE}}". I would classify those inbound rows first, and only then route them.

I set up lead classification an operator can inspect: tags a person agrees with, a route for Hot / Maybe / Noise, and a hold bucket for anything unsure. I do not scrape contact lists. I do not send outreach from the workflow. Classification is not a promise that a lead will buy.

Public notes: {{PORTFOLIO_URL}}. Same inspectable-automation habit: {{GITHUB_REPO_AUTOPILOT}}.

I am {{DISPLAY_NAME}}, Japan-based, async in {{TIMEZONE}}. Please keep scoping on Freelancer.com.

Two questions:
1. {{QUESTION_1}}
2. {{QUESTION_2}}
```

---

## Standard paste

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{PROJECT_TITLE}}". {{SCOPE_ONE_LINER}}

I am {{DISPLAY_NAME}}. Lead classify, for me, means: take inbound records you already own (form, inbox export, CRM field, or sheet), write down the label set, apply those labels in a way a person can sample, and route only the labels you approve. The unsure row stays in a hold queue. A human decides whether it is Hot, Maybe, or Noise. I will not invent a “score” that you cannot explain.

I connect {{STACK_OR_TOOL}} or an equivalent documented connector / official API. I will not crawl LinkedIn, buy lists, or auto-email strangers. I will not claim conversion rates I have not measured on your data.

Deliverables I would put on a milestone outline:
1. Label definitions and examples (including what is out of bounds)
2. A classification path (n8n or sheet + documented connector) with a hold bucket
3. A short SOP: how to sample, how to correct a label, what never auto-sends

Public notes: {{PORTFOLIO_URL}}. Fail-closed API example: {{GITHUB_REPO_AUTOPILOT}}.

English, async in {{TIMEZONE}}, Japan. Bid amount or hourly rate stays in the Freelancer form, not in this letter.

Questions:
1. {{QUESTION_1}}
2. {{QUESTION_2}}

Please keep chat on Freelancer.com until an award starts.
```

---

## Fictional fill (not a real job; do not send)

- Label: `Client C` (fictional)
- Title example: `[FICTION] Tag inbound demo-form rows Hot / Maybe / Noise before Slack`
- `{{ONE_SPECIFIC_DETAIL}}` example: `only Hot should ping sales; Maybe stays in the sheet`
- `{{SCOPE_ONE_LINER}}` example: `New form rows should get a tag a person can audit, and only Hot should ping sales.`
- `{{QUESTION_1}}` example: `What is the source of truth today — the form tool, a Sheet, or the CRM?`
- `{{QUESTION_2}}` example: `Should “unsure” wait for a human, or is a Maybe tag allowed without review?`

Do not bid this invented title. Do not paste live buyer emails into git.

---

## STOP

- Do not promise lead volume, close rate, or “AI that never misses”
- Do not turn this file into an outbound sequencer
- Do not copy fee amounts; the only fees citation is https://www.freelancer.com/feesandcharges
- Do not use this file on a second listing
- Do not sign up from this file
- Do not send
