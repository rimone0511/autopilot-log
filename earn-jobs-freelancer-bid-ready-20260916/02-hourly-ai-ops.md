> **DRAFT_ONLY. DO NOT SEND.**  
> JOBS PHASE. Ready to paste **after an account exists**.  
> No live bids. No secrets. No client PII. Rates stay placeholders. Agent does not submit.  
> **One listing of this style, then stop.** Default remains do-not-send.

# FL-JOB-02 — Freelancer.com: hourly AI ops / inspectable agent (bid proposal)

## Fact table (operator; do not paste)

| key | value |
|---|---|
| pack | earn-jobs-freelancer-bid-ready-20260916 |
| id | FL-JOB-02 |
| desk | Freelancer.com |
| phase | JOBS (paste after account exists) |
| listing_style | **hourly** project (AI ops / inspectable agent) |
| type | Bid proposal body |
| seller_theme | AI ops |
| mode | DRAFT_ONLY, HANDS paste, surgical (one listing) |
| draft | true |
| send | **forbidden** (default do-not-send) |
| signup | **forbidden** |
| spray | **forbidden** |
| one_specific_detail | **required** — skip if empty |
| rate_in_prose | no — hourly form field only |
| fees_in_git | no — https://www.freelancer.com/feesandcharges only |
| chars_preview | 134 |
| chars_short | 646 |
| chars_standard | 1281 |

Assumed listing type (not a real job): ongoing inspectable AI steps — draft, classify, summarize — with a **human approve/gate** before anything is sent or published. Public browse (not a bid): https://www.freelancer.com/jobs/ai-agents

Out of scope: fully autonomous outbound, voice/video “clone of the founder” with no stop, invented citations, KYC-by-proxy, contests, Preferred/Recruiter-only rows.

If the listing is fixed-price n8n-only, use [01-fixed-price-n8n.md](01-fixed-price-n8n.md). If it is inbound tag/route only, use [03-lead-classify.md](03-lead-classify.md).

---

## Fill order (local; still do-not-send)

1. Account exists? If not → [ACCOUNT-PRECONDITION.md](ACCOUNT-PRECONDITION.md) and stop.
2. `{{ONE_SPECIFIC_DETAIL}}` from **this** listing only. Empty → skip.
3. `{{PROJECT_TITLE}}` `{{SCOPE_ONE_LINER}}` `{{STACK_OR_TOOL}}` `{{QUESTION_1}}` `{{QUESTION_2}}`
4. Form field (not prose): `{{HOURLY_RATE_USD}}`
5. Re-read https://www.freelancer.com/feesandcharges. Do not copy amounts.

---

## Form fields (separate from prose)

| UI field | Paste / action |
|---|---|
| Bid type | **Hourly** on the live form. If the listing is fixed-price, do not stretch this file |
| Hourly rate (USD) | `{{HOURLY_RATE_USD}}` |
| Availability / weekly hours (if shown) | leave honest or skip; do not invent |
| Sponsored / Highlight / Sealed | **skip** |
| Proposal body | Fenced paste below, after `{{ONE_SPECIFIC_DETAIL}}` is filled |

Empty required rate → park `rate_required`. Do not invent USD in git. Do not send from this file.

---

## Send gate

- [ ] Seller account already exists (not created by this pack)
- [ ] Project opened on freelancer.com
- [ ] Listing is **hourly**, not a contest, not Recruiter-only
- [ ] `{{ONE_SPECIFIC_DETAIL}}` is from **this** post
- [ ] I have **not** already used this style file on another listing
- [ ] The ask is inspectable AI ops with a human stop — not “send forever with no review”
- [ ] No email / phone / messenger
- [ ] Live form does not demand wallet funding, KYC, membership, or a bid upgrade
- [ ] I click Bid myself — **not from this PR**

---

## List preview (first line; rewrite first)

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{PROJECT_TITLE}}". I would keep a human approve step before that output leaves the system.
```

---

## Short paste

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{PROJECT_TITLE}}". I would keep a human approve step before that output leaves the system.

I do AI ops a second person can inspect: draft, label, or summarize on official APIs or documented connectors, then a hold for you to approve before send or publish. I do not ship an agent that emails customers, posts, or takes payment on its own. I do not invent citations.

Public notes: {{PORTFOLIO_URL}}. Same fail-closed habit: {{GITHUB_REPO_AUTOPILOT}}.

I am {{DISPLAY_NAME}}, Japan-based, async in {{TIMEZONE}}. Please keep scoping on Freelancer.com.

Two questions:
1. {{QUESTION_1}}
2. {{QUESTION_2}}
```

---

## Standard paste

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{PROJECT_TITLE}}". {{SCOPE_ONE_LINER}}

I am {{DISPLAY_NAME}}. AI ops, here, means: take a step you already run (inbox, ticket, sheet, or CRM field), add a model call you can sample, and leave a **human gate** before anything is sent, published, or billed to a customer. I connect {{STACK_OR_TOOL}} or an equivalent official API / documented connector. Secrets stay in the credential store. The SOP names the stop conditions.

I will not build a fully autonomous outbound agent. I will not clone a voice or face. I will not scrape a site that has no public API. I will not automate likes, follows, or fake views. I will not pretend Autopilot Log posts TikTok unattended — inbox upload is the default; direct post is a separate, gated path.

Hourly work I would actually log:
1. Map the current path and where a person must still look
2. One inspectable draft/classify/summarize step with a hold queue
3. An operator SOP: how to sample, how to reject, what never auto-sends

Public notes: {{PORTFOLIO_URL}}. {{GITHUB_REPO_AUTOPILOT}}.

English, async in {{TIMEZONE}}, Japan. Hourly rate stays in the form field, not in this letter.

Questions:
1. {{QUESTION_1}}
2. {{QUESTION_2}}

Please keep chat on Freelancer.com until an award starts.
```

---

## Fictional fill (not a real job; do not send)

- Label: `Client B` (fictional)
- Title example: `[FICTION] Hourly: inspectable support-draft agent with Salesforce hold`
- `{{ONE_SPECIFIC_DETAIL}}` example: `hand off to a human when the intent score is below your threshold`
- `{{SCOPE_ONE_LINER}}` example: `Drafts may be written automatically; nothing posts to the customer until you approve the unsure bucket.`
- `{{QUESTION_1}}` example: `Which Salesforce object is the source of truth for an open case?`
- `{{QUESTION_2}}` example: `Who is allowed to press send after a draft — one named person, or anyone with the queue?`

Do not bid this invented title. Do not paste a live client’s threshold into git.

---

## STOP

- Do not promise “autonomous,” “never misses,” or a founder clone
- Do not paste buyer emails from a listing into git
- Do not copy fee amounts; the only fees citation is https://www.freelancer.com/feesandcharges
- Do not use this file on a second listing
- Do not sign up from this file
- Do not send
