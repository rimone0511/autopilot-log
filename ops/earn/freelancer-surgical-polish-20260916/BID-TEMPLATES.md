> **DRAFT_ONLY. DO NOT SEND.**  
> Surgical bids only. Default **do-not-send**. No spray. No contests. No secrets.  
> Agent does not submit. There is no bid script. Rates stay form-field placeholders.

# Freelancer.com — surgical bid templates (polish)

Pack: `ops/earn/freelancer-surgical-polish-20260916/`  
Desk: [Freelancer.com](https://www.freelancer.com/) (QUEUE Wave A10 / CU-10)  
Mode: **HANDS** paste · **one listing per style**, then stop  
Seller: `{{DISPLAY_NAME}}` (recommended: Yuta Ishida / 石田祐太)

**Surgical** means: you open **one** project in the official bid UI, you can name one detail only that listing contains, you rewrite the first lines, you paste, **you** click Bid — or you skip. A computer must not be the thing that submits. Leftover monthly bids are not a reason to send another. Identical first paragraphs across projects are spray.

Sibling CU and this pack’s default remain **no bids / no contests**. Use a paste only after a later human GO, and only if the live form does not demand wallet funding, KYC, or a paid upgrade. See [MONEY-FLAGS.md](MONEY-FLAGS.md) and [STOP-KYC.md](STOP-KYC.md).

Fees: cite https://www.freelancer.com/feesandcharges only. Do not copy amounts into git.

Profile paste is [PROFILE-PASTE.md](PROFILE-PASTE.md). This file does not sign up.

Public browse (not a bid; re-open in a browser):

- n8n board: https://www.freelancer.com/jobs/n8n
- AI agents board: https://www.freelancer.com/jobs/ai-agents
- Bid help hub (SPA — trust the live article + form counter): https://www.freelancer.com/support/freelancer/Project/how-to-bid-1633
- User Agreement: https://www.freelancer.com/about/terms
- Code of Conduct: https://www.freelancer.com/info/codeofconduct
- API terms: https://www.freelancer.com/about/apiterms

---

## Three styles (one listing each)

Pick **one** file-style that matches the listing. Do not stack three styles into one paste. Do not open a contest, a Preferred / Recruiter-only row, or a “fund the Site wallet to continue” wall.

| id | Listing style | Paste into | Public browse (not a bid) |
|---|---|---|---|
| FL-SB-01 | **Fixed-price** n8n / workflow | Bid proposal on **one** fixed-price project | https://www.freelancer.com/jobs/n8n |
| FL-SB-02 | **Hourly** AI ops / inspectable agent | Bid proposal on **one** hourly project | https://www.freelancer.com/jobs/ai-agents |
| FL-SB-03 | **Lead classify / inbound route** (fixed *or* hourly form) | Bid proposal on **one** inbound-classify project | same boards; pick classify/route, not outbound spray |

Using a style on a **second** project of the same style is spray. Close the extras.

---

## Send gate (every paste)

Skip if any box is false. This pack still does **not** send.

- [ ] I opened **this** project on freelancer.com (not a scrape dump, not a third-party bid tool).
- [ ] I replaced `{{ONE_SPECIFIC_DETAIL}}` with a fact from **this** listing. If I cannot name one in about a minute, I skip.
- [ ] This is the **only** listing I will use this style on (no leftover-bid spray, no “use the monthly allotment”).
- [ ] Leftover placeholders from a previous listing are gone.
- [ ] No email, phone, WhatsApp, Telegram, Slack, Discord, or “text me at…” in the paste.
- [ ] No off-platform payment, crypto-to-wallet, or “pay me outside”.
- [ ] Bid amount / hourly rate / delivery days stay in **form fields**. Git has no live USD.
- [ ] I re-read https://www.freelancer.com/feesandcharges immediately before considering a bid. I did **not** copy the table into this letter.
- [ ] The live form does **not** require funding the Site wallet, buying a bid, buying membership, completing KYC, or a bid upgrade (Sponsored / Highlight / Sealed) to proceed. If it does: **stop**.
- [ ] I am **not** entering a contest. I am not applying to Preferred Freelancer.
- [ ] I will click **Bid / Place Bid** myself. Nothing in this folder submits for me.
- [ ] The work is official APIs / documented connectors + docs. Scraping, likes/follows/views, or ungated posting → decline (do not bid).

If more than one project is open in your head, you are already off surgical. Close the extras.

### Fact table vs prose

| Layer | Lives in | Contains rates? |
|---|---|---|
| Form fields on the live desk | Bid amount / hourly / delivery | Human types the local number |
| Fenced paste | Bid proposal body | **No live prices.** Do not paste operator tables |

Empty required rate → park `rate_required` and stop. Do not invent USD in git. Empty required `{{ONE_SPECIFIC_DETAIL}}` → skip. Do not reuse a detail from another listing.

---

## HANDS + ToS (no auto-bid)

Do **not** write or run: auto-apply / auto-bid queues; browser automation, scrapers, or extensions that submit faster than a person; Freelancer API / MCP use to spam bids or scrape projects; multiple accounts to dodge bid limits; Sponsored / Highlight / Sealed as a default; **contests** (including “free to enter”); Preferred exam / Recruiter-only rows; contact info in a pre-award bid; off-platform pay; live USD in git; fee tables copied from anywhere.

User Agreement (https://www.freelancer.com/about/terms): no spam/bulk; no robot/spider/scraper without written permission; a Seller must hold the **Minimum Account Balance** on the live fees schedule **before** bidding — if the UI asks you to fund it, **stop** (this pack does not authorize a top-up; do not invent the number); no unrelated external website in a bid; no private contact in public project communication.

Code of Conduct (https://www.freelancer.com/info/codeofconduct): bid only on projects you plan to complete; do not underbid to avoid fees; no multiple accounts; communicate on-site; do not take payment off-site.

Native “saved replies” are still templates you insert by hand; personalize `{{ONE_SPECIFIC_DETAIL}}` before any later send.

---

## Style-specific take / decline

| Style | Take | Decline |
|---|---|---|
| 01 Fixed-price n8n | Official API / documented connector + SOP + failure alert; amount in the bid field | Browser bots, unofficial scrapers, partner-badge impersonation, contest entries |
| 02 Hourly AI ops | Draft / inspect / human approve before send; hourly in the rate field | Fully autonomous outbound, invented citations, KYC-by-proxy, “always-on clone” with no stop |
| 03 Lead classify | Tags + route + human review of the unsure bucket | Auto-spam sequences, scraped contact lists, fake intent scores, LinkedIn crawling |

---

## FL-SB-01 — fixed-price n8n / workflow

Assumed listing (not a real job): one n8n path a non-engineer can rerun — trigger, honest steps, destination, failure alert, short SOP.

Form: **Fixed price**. Bid amount `{{BID_AMOUNT_USD}}`. Delivery `{{DELIVERY_DAYS}}`. Milestone 1 optional `{{MILESTONE_1}}` on-platform only. Sponsored / Highlight / Sealed = **skip**. If the listing is hourly, use FL-SB-02.

### Preview

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{PROJECT_TITLE}}". I would treat that as the first n8n path, not a generic template.
```

### Short

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{PROJECT_TITLE}}". I would treat that as the first n8n path, not a generic template.

I build n8n workflows a non-engineer can rerun: official APIs or documented connectors only, retries, a failure alert, and a short SOP (what starts it, what is safe to edit, where secrets live). I do not use browser automation. I do not scrape platforms that have no API.

Public example of that posture: Autopilot Log (official posting APIs; posting gate fails closed) — {{GITHUB_REPO_AUTOPILOT}}. Field notes: {{PORTFOLIO_URL}}.

I am {{DISPLAY_NAME}}, based in Japan, async in {{TIMEZONE}}. English is fine. Please keep scoping on Freelancer.com until an award / milestone starts.

Two questions:
1. {{QUESTION_1}}
2. {{QUESTION_2}}
```

### Standard

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

Fictional fill (do not send): `Client A` · `[FICTION] Build n8n: Typeform to Google Sheet plus Slack on failure` · detail `Slack only when the Sheet write fails, not on every new row` · scope `One inbound form should land as a row, and a person should see a Slack note only when the write fails.` · Q1 `Is n8n Cloud already in use, or would this be a self-hosted instance you control?` · Q2 `Who is allowed to retry a failed run — you, or anyone with the sheet?`

---

## FL-SB-02 — hourly AI ops / inspectable agent

Assumed listing (not a real job): ongoing inspectable AI steps — draft, classify, summarize — with a **human approve/gate** before anything is sent or published.

Form: **Hourly**. Rate `{{HOURLY_RATE_USD}}`. Weekly hours: honest or skip; do not invent. Sponsored / Highlight / Sealed = **skip**. If the listing is fixed-price n8n-only, use FL-SB-01. If it is inbound tag/route only, use FL-SB-03.

### Preview

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{PROJECT_TITLE}}". I would keep a human approve step before that output leaves the system.
```

### Short

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{PROJECT_TITLE}}". I would keep a human approve step before that output leaves the system.

I do AI ops a second person can inspect: draft, label, or summarize on official APIs or documented connectors, then a hold for you to approve before send or publish. I do not ship an agent that emails customers, posts, or takes payment on its own. I do not invent citations.

Public notes: {{PORTFOLIO_URL}}. Same fail-closed habit: {{GITHUB_REPO_AUTOPILOT}}.

I am {{DISPLAY_NAME}}, Japan-based, async in {{TIMEZONE}}. Please keep scoping on Freelancer.com.

Two questions:
1. {{QUESTION_1}}
2. {{QUESTION_2}}
```

### Standard

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

Fictional fill (do not send): `Client B` · `[FICTION] Hourly: inspectable support-draft agent with Salesforce hold` · detail `hand off to a human when the intent score is below your threshold` · scope `Drafts may be written automatically; nothing posts to the customer until you approve the unsure bucket.` · Q1 `Which Salesforce object is the source of truth for an open case?` · Q2 `Who is allowed to press send after a draft — one named person, or anyone with the queue?`

---

## FL-SB-03 — lead classify / inbound route

Assumed listing (not a real job): inbound form / inbox / sheet rows tagged (e.g. Hot / Maybe / Noise) and routed, with a human looking at the unsure bucket.

Form: **fixed** or **hourly** — match the listing; do not write a second price in the letter. `{{BID_AMOUNT_USD}}` if fixed. `{{HOURLY_RATE_USD}}` if hourly. `{{DELIVERY_DAYS}}` if the fixed form asks. Sponsored / Highlight / Sealed = **skip**.

### Preview

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{PROJECT_TITLE}}". I would classify those inbound rows first, and only then route them.
```

### Short

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{PROJECT_TITLE}}". I would classify those inbound rows first, and only then route them.

I set up lead classification an operator can inspect: tags a person agrees with, a route for Hot / Maybe / Noise, and a hold bucket for anything unsure. I do not scrape contact lists. I do not send outreach from the workflow. Classification is not a promise that a lead will buy.

Public notes: {{PORTFOLIO_URL}}. Same inspectable-automation habit: {{GITHUB_REPO_AUTOPILOT}}.

I am {{DISPLAY_NAME}}, Japan-based, async in {{TIMEZONE}}. Please keep scoping on Freelancer.com.

Two questions:
1. {{QUESTION_1}}
2. {{QUESTION_2}}
```

### Standard

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

Fictional fill (do not send): `Client C` · `[FICTION] Tag inbound demo-form rows Hot / Maybe / Noise before Slack` · detail `only Hot should ping sales; Maybe stays in the sheet` · scope `New form rows should get a tag a person can audit, and only Hot should ping sales.` · Q1 `What is the source of truth today — the form tool, a Sheet, or the CRM?` · Q2 `Should “unsure” wait for a human, or is a Maybe tag allowed without review?`

---

## Suggested question stems (pick two; rewrite)

- Which system is the source of truth today (Sheet, CRM, inbox, other)?
- What should happen on failure — retry, Slack/email alert, or stop?
- Who has to approve a send/post before it goes live?
- Is this one workflow, or a pack that shares credentials?

---

## Length (practical; live counter wins)

Do **not** treat third-party blogs as a character cap. If the bid form shows a counter, that counter is the cap.

Character counts below are `len()` of the fenced body (placeholders unsubstituted). Filling placeholders **increases** length. Re-count on the live form.

| Style | preview | short | standard |
|---|---:|---:|---:|
| 01 fixed-price n8n | 128 | 765 | 1349 |
| 02 hourly AI ops | 134 | 646 | 1281 |
| 03 lead classify | 131 | 659 | 1273 |

First sentence of every paste must contain `{{ONE_SPECIFIC_DETAIL}}`.

---

## Shared placeholders

Replace locally. Never commit filled secrets (public URLs already listed are fine).

| Token | Meaning | In this repo |
|---|---|---|
| `{{DISPLAY_NAME}}` | Seller display name | Recommended: Yuta Ishida |
| `{{PROJECT_TITLE}}` | Listing title | Fictional examples only |
| `{{ONE_SPECIFIC_DETAIL}}` | Phrase only this listing contains | **Required**; skip if empty |
| `{{SCOPE_ONE_LINER}}` | One-sentence restatement of the ask | Fictional examples only |
| `{{STACK_OR_TOOL}}` | n8n, Sheets, CRM field, etc. | Do not claim partner badges |
| `{{QUESTION_1}}` `{{QUESTION_2}}` | Scope questions | Empty → do not send |
| `{{BID_AMOUNT_USD}}` | Fixed-price bid **form field** | Placeholder; not a quote in prose |
| `{{HOURLY_RATE_USD}}` | Hourly bid **form field** | Placeholder; not a quote in prose |
| `{{DELIVERY_DAYS}}` | Delivery / duration **form field** | Placeholder |
| `{{MILESTONE_1}}` | Optional first milestone label | Placeholder; create on-platform only |
| `{{TIMEZONE}}` | Async window | Local ledger (example: `JST`) |
| `{{PORTFOLIO_URL}}` | Public site | `https://yutalab.dev/` |
| `{{GITHUB_REPO_AUTOPILOT}}` | Public fail-closed example | `https://github.com/rimone0511/autopilot-log` |

Public URLs (not secrets): https://yutalab.dev/ · https://github.com/rimone0511/autopilot-log · https://www.freelancer.com/feesandcharges

---

## After a human actually bids (not this PR)

Keep milestones on-platform. Do not underbid to dodge fees. Do not discuss taking the thread to email. If KYC appears after award, stop uploads and hand the screen type (not the documents) to morning KYC.

## 日本語（運用だけ）

下書きのみ。既定は送らない。スタイルごとに公式画面で **1件だけ**。`{{ONE_SPECIFIC_DETAIL}}` が埋まらなければスキップ。本文に金額を埋め込まない。コンテストは入らない。手数料の数字は書かず https://www.freelancer.com/feesandcharges を送る直前に読む。自動入札・残り入札の使い切りはしない。
