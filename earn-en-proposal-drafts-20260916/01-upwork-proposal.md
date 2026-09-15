# 01 — Upwork job proposal (cover letter)

| | |
|---|---|
| Desk | Upwork |
| Type | Proposal / cover letter |
| Mode | DRAFT_ONLY, HANDS paste |
| When | You clicked Apply on **one** job in the Upwork UI |
| When not | Invites (use 02). Catalog drafts (other pack). Any auto-apply tool |

Paste into the proposal cover-letter field. Bid amount / hourly rate belong in **form fields**, not as a second price in the letter unless the job asked you to name one — then use `{{HOURLY_RATE_USD}}` or `{{FIXED_PRICE_USD}}` from your local ledger, never from git.

Upwork shows opening lines in the list. The first sentence must contain `{{ONE_SPECIFIC_DETAIL}}`.

Target: ~150–250 words. Official tip: keep most cover letters to about 200–300 words or fewer ([source](https://www.upwork.com/resources/cover-letter-tips)).

## Send gate

- [ ] Job opened on upwork.com (not a scrape dump)
- [ ] `{{ONE_SPECIFIC_DETAIL}}` is unique to this post
- [ ] No email / phone / messenger
- [ ] I click Submit myself; Connects spend is a **per-job** human choice (this pack does not tell you to buy or spray Connects)
- [ ] No Boosted Proposal unless a later human decision says so (not instructed here)

## Paste

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{JOB_TITLE}}". I would treat that as the first milestone, not a generic n8n template.

I build automations a non-engineer can rerun: official APIs or documented connectors only, retries, a failure alert, and a short SOP (what it does, what breaks, where secrets live). I do not use browser automation. I do not scrape platforms that have no API. I do not ship likes, follows, or fake views.

Public example of that posture: Autopilot Log (YouTube Data API v3 + TikTok Content Posting API; posting gate fails closed) — {{GITHUB_REPO_AUTOPILOT}}. Field notes: {{PORTFOLIO_URL}}.

I am {{DISPLAY_NAME}}, based in Japan, async in {{TIMEZONE}}. English is fine. Please keep scoping on Upwork Messages until a contract starts.

Two questions:
1. {{QUESTION_1}}
2. {{QUESTION_2}}
```

## Suggested question stems (pick two; rewrite)

- Which system is the source of truth today (Sheet, CRM, inbox, other)?
- What should happen on failure — retry, Slack/email alert, or stop?
- Who has to approve a send/post before it goes live?
- Is this one workflow, or a pack of three that share credentials?

## Do not paste

- “I have 10 years…” / fake metrics
- Skype / WhatsApp / Telegram
- “Pay me on PayPal/crypto to start”
- A US city you do not live in
