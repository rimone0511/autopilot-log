# Freelancer.com — surgical-bid ONLY notes

Status: **DRAFT_ONLY**. **HANDS**. This is copy text for a human. It is not a bidder.

**Surgical-bid** means: you open **one** project in the official UI, you can name one detail only that listing contains, you rewrite the first lines, you paste, **you** click Bid — or you skip. A computer must not be the thing that submits. There is no leftover-bid spray, no “use the monthly allotment”, no sponsored-bid default.

Sibling CU runbook for A10: profile + skills; **No bids. No contests.** This file does not override that. Default for CU and for this PR: **do not send**. Use the paste only after a later human GO, and only if the live bid form does not demand wallet funding, KYC, or a paid upgrade.

## Send gate (every listing)

Skip if any box is false.

- [ ] I opened **this** project on freelancer.com (not a scrape dump, not a third-party bid tool).
- [ ] I replaced `{{ONE_SPECIFIC_DETAIL}}` with a fact from **this** listing. If I cannot name one in about a minute, I skip.
- [ ] Leftover placeholders from a previous listing are gone.
- [ ] No email, phone, WhatsApp, Telegram, Slack, Discord, or “text me at…” in the paste.
- [ ] No off-platform payment, crypto-to-wallet, or “pay me outside”.
- [ ] I will click **Bid / Place Bid** myself. Nothing in this folder submits for me.
- [ ] The work is official APIs / documented connectors + docs. Scraping, likes/follows/views, or ungated posting → decline (do not bid).
- [ ] The live form does **not** require funding the Site wallet, buying a bid, buying membership, or completing KYC to proceed. If it does: **stop**. Do not pay from CU.
- [ ] I am not entering a contest, not buying Highlight / Sealed / Sponsored, not applying to Preferred Freelancer.

If more than one project is open in your head, you are already off surgical. Close the extras.

## Official lines this pack is obeying

Help text moves. Re-open the live page before you argue with a client. **Do not invent fees.** The schedule is https://www.freelancer.com/feesandcharges — read it at send time. This file does not copy the table into a payment plan.

### User Agreement — spam and bots

https://www.freelancer.com/about/terms (opened 2026-09-15)

- Do not distribute or post **spam, unsolicited, or bulk** electronic communications.
- Do not use any **robot, spider, scraper or other automated means** to access the Website (including the API) without Freelancer’s express written permission.
- Before submitting a bid, a Seller must hold the **Minimum Account Balance** specified in the live Fees & Charges schedule. If the bid UI asks you to fund that balance: **stop** (this pack does not authorize a top-up).
- Do not advertise an unrelated external website in a bid. URLs must relate to the project / user / service on the site.
- Do not put private contact details in public project communication.

### Code of Conduct — bidding and spam

https://www.freelancer.com/info/codeofconduct (opened 2026-09-15)

- Bid only on projects you **plan to complete**.
- Do not underbid to avoid fees.
- Do not spam or advertise a website or service unless otherwise allowed.
- Do not create multiple accounts.
- Do not ask other users for private contact details; communicate through official website features.
- Do not seek to communicate or receive/initiate payments off-site.

### API

https://www.freelancer.com/about/apiterms — do not build a bid bot against the API. Do not circumvent rate limits.

### Bid help (SPA — re-read in a browser)

Support hub titles seen on 2026-09-15 (article bodies did not render in a plain GET; **trust the live article + the form counter**):

- Bidding on projects: https://www.freelancer.com/support/freelancer/Project/how-to-bid-1633
- Writing a proper bid proposal (same hub)
- Bid limit and replenishment
- Bidding requirements
- I cannot bid on a project

Do **not** treat third-party blogs (“1500 characters”, “always sponsor”) as ToS. If the form shows a counter, that counter is the cap.

### Fees / upgrades (read live; do not pay from this pack)

https://www.freelancer.com/feesandcharges

The public freelancer section states that signup/profile/portfolio/notifications/contest **entry** can be free, that **bidding is described as free** with a **free-member monthly bid allotment**, and that a **minimum account balance** plus **optional bid upgrades** exist. Exact numbers move. **CU does not fund, upgrade, or buy bids.**

Preferred Freelancer Recruiter-project fees and “Verified by Freelancer” application fees are paid walls. Do not apply from this pack.

## Allowed (this pack)

- Draft in git with placeholders
- One human-personalized paste per listing, after a human GO
- Asking scope questions on-platform after a bid is actually in play (not this PR)
- Declining work that needs scraping, engagement fraud, or off-platform pay
- Linking **public** portfolio / GitHub where the bid field allows a work-sample URL
- Stopping at KYC / wallet / paid upgrade

## Forbidden (do not add later either)

- Auto-apply / auto-bid / “use remaining bids this month” queues
- Browser automation, headless browsers, scrapers, or extensions that submit faster than a person
- Freelancer API / MCP use to spam bids or scrape projects
- Multiple accounts to dodge bid limits
- Sponsored / highlight / sealed bids as a default tactic
- Contests (including “free to enter”) from this pack
- Contact info in a pre-award bid
- Off-platform payment instructions
- Preferred Freelancer exam / KYC selfie from CU

## Paste (one project)

Target: short. First sentence must contain `{{ONE_SPECIFIC_DETAIL}}`. Bid amount / delivery time belong in **form fields**, not as a second price in the letter unless the project asked you to name one — then use `{{BID_AMOUNT_USD}}` / `{{DELIVERY_DAYS}}` from your local ledger, never from git.

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{PROJECT_TITLE}}". I would treat that as the first milestone, not a generic n8n template.

I build automations a non-engineer can rerun: official APIs or documented connectors only, retries, a failure alert, and a short SOP (what it does, what breaks, where secrets live). I do not use browser automation. I do not scrape platforms that have no API. I do not ship likes, follows, or fake views.

Public example of that posture: Autopilot Log — {{GITHUB_REPO_AUTOPILOT}}. Field notes: {{PORTFOLIO_URL}}.

I am {{DISPLAY_NAME}}, based in Japan, async in {{TIMEZONE}}. English is fine. Please keep scoping on Freelancer.com until an award / milestone starts.

Two questions:
1. {{QUESTION_1}}
2. {{QUESTION_2}}
```

### Suggested question stems (pick two; rewrite)

- Which system is the source of truth today (Sheet, CRM, inbox, other)?
- What should happen on failure — retry, Slack/email alert, or stop?
- Who has to approve a send/post before it goes live?
- Is this one workflow, or a pack that shares credentials?

### Do not paste

- “I have 10 years…” / fake metrics / fake Job Completion Rate
- Skype / WhatsApp / Telegram / a mailto
- “Pay me on PayPal/crypto to start”
- A US city you do not live in
- “I will bid your whole list this week”

## Decline instead of bidding

Same class as the EN HANDS pack:

- Like / follow / view / “engagement” automation
- Browser automation or scraping where there is no official API
- Publishing to social without the client’s own approve/gate step
- Anything that needs you to pretend you are in another country
- Local-only on-site work you will not do
- Anything that requires you to complete KYC or fund a wallet **in order to send this one bid** — park it; morning human

## After a human actually bids (not this PR)

Keep milestones on-platform. Do not underbid to dodge fees (Code of Conduct). Do not discuss taking the thread to email. If KYC appears after award, stop uploads and hand the screen type (not the documents) to morning KYC.

## Placeholders

```
{{DISPLAY_NAME}}
{{PROJECT_TITLE}}
{{ONE_SPECIFIC_DETAIL}}       REQUIRED
{{QUESTION_1}}
{{QUESTION_2}}
{{BID_AMOUNT_USD}}            form field; empty in git
{{DELIVERY_DAYS}}             form field; empty in git
{{TIMEZONE}}
{{PORTFOLIO_URL}}
{{GITHUB_REPO_AUTOPILOT}}
```
