> **DRAFT_ONLY. DO NOT SEND.**  
> No live bids. No secrets. No client PII. Rates stay placeholders. Agent does not submit.  
> **One listing of this style, then stop.** Default remains do-not-send.

# FL-SB-01 — Freelancer.com: fixed-price n8n / workflow (bid proposal)

## Fact table (operator; do not paste)

| key | value |
|---|---|
| pack | earn-freelancer-surgical-bid-templates-20260916 |
| id | FL-SB-01 |
| desk | Freelancer.com |
| listing_style | **fixed-price** project (n8n / workflow automation) |
| type | Bid proposal body |
| seller_theme | n8n workflow |
| mode | DRAFT_ONLY, HANDS paste, surgical (one listing) |
| draft | true |
| send | **forbidden** (default do-not-send) |
| signup | **forbidden** |
| spray | **forbidden** |
| rate_in_prose | no — bid amount form field only |
| fees_in_git | no — https://www.freelancer.com/feesandcharges only |
| chars_preview | 128 |
| chars_short | 765 |
| chars_standard | 1349 |

Assumed listing type (not a real job): one n8n path a non-engineer can rerun — trigger, honest steps, destination, failure alert, short SOP. Public browse (not a bid): https://www.freelancer.com/jobs/n8n

Out of scope: browser automation, scraping without an official API, likes/follows/views, partner-badge impersonation, contests, Preferred/Recruiter-only rows.

---

## Form fields (separate from prose)

| UI field | Paste / action |
|---|---|
| Bid type | **Fixed price** on the live form. If the listing is hourly, use [02-hourly-ai-ops.md](02-hourly-ai-ops.md) instead — do not stretch this file |
| Bid amount (USD) | `{{BID_AMOUNT_USD}}` |
| Delivery time | `{{DELIVERY_DAYS}}` |
| Milestone 1 (optional) | `{{MILESTONE_1}}` — create on-platform only |
| Sponsored / Highlight / Sealed | **skip** — do not buy from this pack |
| Proposal body | Fenced paste below, after `{{ONE_SPECIFIC_DETAIL}}` is filled |

Empty required rate → park `rate_required`. Do not invent USD in git. Do not send from this file.

Re-read https://www.freelancer.com/feesandcharges before considering a bid. Do not paste amounts from that page into this letter.

---

## Send gate

- [ ] Project opened on freelancer.com (not a scrape dump)
- [ ] Listing is **fixed-price**, not hourly, not a contest
- [ ] `{{ONE_SPECIFIC_DETAIL}}` is unique to this post
- [ ] I have **not** already used this style file on another listing
- [ ] Theme still matches **n8n / workflow automation**, not writing-only or lead-classify-only
- [ ] No email / phone / messenger
- [ ] Live form does not demand wallet funding, KYC, membership, or a bid upgrade
- [ ] I click Bid myself — **not from this PR**

---

## List preview (first line; rewrite first)

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{PROJECT_TITLE}}". I would treat that as the first n8n path, not a generic template.
```

---

## Short paste

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{PROJECT_TITLE}}". I would treat that as the first n8n path, not a generic template.

I build n8n workflows a non-engineer can rerun: official APIs or documented connectors only, retries, a failure alert, and a short SOP (what starts it, what is safe to edit, where secrets live). I do not use browser automation. I do not scrape platforms that have no API.

Public example of that posture: Autopilot Log (official posting APIs; posting gate fails closed) — {{GITHUB_REPO_AUTOPILOT}}. Field notes: {{PORTFOLIO_URL}}.

I am {{DISPLAY_NAME}}, based in Japan, async in {{TIMEZONE}}. English is fine. Please keep scoping on Freelancer.com until an award / milestone starts.

Two questions:
1. {{QUESTION_1}}
2. {{QUESTION_2}}
```

---

## Standard paste

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{PROJECT_TITLE}}". {{SCOPE_ONE_LINER}}

I am {{DISPLAY_NAME}}. I sell a scoped n8n workflow plus operator docs, not an unbounded retainer. Typical pieces: a trigger you already have (form, webhook, schedule, or a new sheet row); honest steps through {{STACK_OR_TOOL}} or an equivalent documented connector; a destination (inbox, sheet, CRM field, or internal API); retries or a failure alert; an SOP that names what starts it, what breaks, and how to rerun. Secrets stay in the credential store. The SOP does not paste them.

I will not scrape a site that has no public API. I will not automate likes, follows, comments, or fake views. I will not publish on your behalf unless you hold the posting switch.

Public notes: {{PORTFOLIO_URL}}. Fail-closed API posting example: {{GITHUB_REPO_AUTOPILOT}}.

I work in English, async in {{TIMEZONE}}, from Japan. I do not invent a US address.

What I would deliver under a milestone:
1. A short map of the current copy-paste and the stop conditions
2. One working n8n path with a visible failure path
3. An operator SOP and a change note

Two questions before I outline further milestones here:
1. {{QUESTION_1}}
2. {{QUESTION_2}}

Please keep chat on Freelancer.com until an award starts. Bid amount and delivery days stay in the form fields, not in this letter.
```

---

## Fictional fill (not a real job; do not send)

- Label: `Client A` (fictional)
- Title example: `[FICTION] Build n8n: Typeform to Google Sheet plus Slack on failure`
- `{{ONE_SPECIFIC_DETAIL}}` example: `Slack only when the Sheet write fails, not on every new row`
- `{{SCOPE_ONE_LINER}}` example: `One inbound form should land as a row, and a person should see a Slack note only when the write fails.`
- `{{QUESTION_1}}` example: `Is n8n Cloud already in use, or would this be a self-hosted instance you control?`
- `{{QUESTION_2}}` example: `Who is allowed to retry a failed run — you, or anyone with the sheet?`

Do not replace the fictional label with a live client name in git. Do not bid this invented title.

---

## STOP

- Do not paste the fact table or the form-field rate tokens as if they were a quote
- Do not claim n8n Expert / Zapier Partner / Make Partner
- Do not copy fee amounts; the only fees citation is https://www.freelancer.com/feesandcharges
- Do not use this file on a second listing
- This file is not a bid until a human personalizes it **and** clicks Bid later, outside this PR
