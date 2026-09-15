# Fiverr Gig paste — n8n automation (UNPUBLISHED DRAFT)

Desk: Fiverr
Checked: 2026-09-15 (public help + public Automations & Workflows category)
Mode: DRAFT ONLY — fill the form, **never click Publish Gig**
Paid plans: NO (no Seller Plus, no Promoted Gigs)
Language: English Gig (required). Japanese operator. Honest `{{COUNTRY}}`.
Google signup: YES — MAIN Google only (`{{GOOGLE_ACCOUNT_EMAIL}}`)

Public entry:

- Home: https://www.fiverr.com/
- Seller Gig create (desktop): profile → **Create a New Gig** or My Business → Gigs
- Category landing: https://www.fiverr.com/categories/programming-tech/software-development/automations-workflows
- Creating a Gig: https://help.fiverr.com/hc/en-us/articles/360010451397-Creating-a-Gig

Gig creation is **desktop only** per Fiverr help. Do not use the mobile app to create it.

---

## 0. How far to go (then stop)

1. MAIN Google → Fiverr. Do not invent a second account.
2. **Become a Seller** if the account is still client-only. Individual, not Agency.
3. Minimum profile (section 7) if the form blocks Gig create without it.
4. Create a New Gig. Paste sections 1–5.
5. Confirm status is **Draft** (or that Publish was never clicked).
6. **STOP** at Identity Verification, tax forms, or ID upload. See [STOP-KYC.md](STOP-KYC.md).

If KYC appears before a draft can be saved, stop. This paste is still the pack.

---

## 1. Overview — title, category, tags

Fiverr pre-fills `I will`. Paste **only the field**, not the prefix.
Avoid special characters `&` `/` `"` `+` in the title (Fiverr Creating a Gig help).

### Title field (paste)

```
build n8n automation with operator docs you can rerun
```

| Count | Value |
|---|---|
| Title field | 53 characters (limit 80) |
| Full display `I will …` | 60 characters |

Do not replace this with keyword-stuffed "n8n ai agent xAI grok" titles.

### Category (pick in the live dropdown; do not invent IDs)

| Level | Value |
|---|---|
| Category | Programming & Tech |
| Subcategory | Software Development |
| Nested / service | Automations & Workflows |

If the live tree differs, pick the closest **automation / workflow** node under Programming & Tech. Do not put this Gig in AI image, video, or voice categories.

### Search tags (exactly 5; each ≤ 20 characters)

```
n8n automation
n8n workflow
workflow automation
api integration
operator docs
```

| Tag | Characters |
|---|---|
| n8n automation | 14 |
| n8n workflow | 12 |
| workflow automation | 19 |
| api integration | 15 |
| operator docs | 13 |

Do not tag `xAI`, `Grok`, `ChatGPT`, or competitor spam lists.

### Short phrases / metadata (only if Overview also asks)

Fiverr help: up to five words or short phrases that describe the Gig.

```
n8n
business automation
webhook
sop writing
api workflow
```

If the form has only **one** set of five tags, use the Search tags list and skip this block.

### Service type / tool metadata (only if shown)

- Tool / platform: `n8n`
- Do not check Zapier or Make as the **product** of this Gig (migration is FAQ-only).
- Do not check official-partner / Pro-only flags you do not have.

---

## 2. Scope & pricing — packages

Turn **Offer packages** on (three tiers). Prices are USD. Minimum $5.
**Do not commit live prices.** Fill `{{PRICE_*}}` locally.

Fiverr help: at least one revision per package.

### Package names

| Tier | Paste name | Characters |
|---|---|---|
| Basic | `Starter workflow` | 16 |
| Standard | `Production workflow` | 19 |
| Premium | `Workflow and SOP` | 16 |

### Package descriptions (keep ≤ 100 characters)

**Basic** (70):

```
One scoped n8n workflow plus short operator notes. Official APIs only.
```

**Standard** (70):

```
Production n8n workflow with error alert, README, and importable JSON.
```

**Premium** (59):

```
Up to two related workflows plus a full SOP and change log.
```

### Scope table

| | Basic | Standard | Premium |
|---|---|---|---|
| Price USD | `{{PRICE_BASIC_USD}}` | `{{PRICE_STANDARD_USD}}` | `{{PRICE_PREMIUM_USD}}` |
| Delivery (days) | 3 | 5 | 7 |
| Revisions | 1 | 2 | 3 |
| n8n workflows | 1 scoped | 1 production | up to 2 related |
| Official-API / webhook paths | 1 | 2 | up to 4 |
| Error handling | happy path + 1 fail note | retries note + failure alert | retries note + failure alert |
| Docs | short operator notes | operator README | full SOP + change log |
| Importable workflow JSON | yes | yes | yes |
| Light AI step (classify / summarize / draft) | only if buyer asks | only if buyer asks | only if buyer asks |
| Social publish / browser bots / scraping | no | no | no |
| n8n hosting purchase | no | no | no |

If the category exposes numeric metadata (number of automations, number of integrations), copy the counts from this table. Do not inflate.

### Optional extras (off unless the form requires a row)

Do not add extras that need a paid Fiverr subscription.

| Extra | Delivery / qty | Price |
|---|---|---|
| Extra fast delivery | shorter than the selected package | `{{PRICE_EXTRA_FAST_USD}}` |
| Additional n8n workflow | +1 related workflow | `{{PRICE_EXTRA_WORKFLOW_USD}}` |
| Additional official-API integration | +1 | `{{PRICE_EXTRA_INTEGRATION_USD}}` |
| Extra revision | +1 | `{{PRICE_EXTRA_REVISION_USD}}` |

Leave video consultation **off** for this draft.

---

## 3. Description (English, ≤ 1,200 characters)

Official Creating a Gig help: up to 1,200 characters. This paste is **1155**.

```
I build n8n workflows you can operate without me.

You get a scoped workflow on your n8n Cloud or self-hosted instance, wired through official APIs and webhooks only. I do not drive browsers, scrape sites, or automate likes, follows, or views.

Every order is custom. I map the current manual steps, build the flow, test the happy path and one failure path, then hand over operator docs: what it does, how to rerun, what to do when it fails, and which values are secrets versus safe to edit. Standard and Premium include importable workflow JSON and a short change log.

AI is optional. If you ask, I can add a light step to classify, summarize, or draft. I still design, test, and document the workflow. If you want no AI, say so at the start and I will not add model calls. I do not deliver unmodified AI output, deepfakes, impersonation, or fake accounts. I am an independent freelancer, not a partner or employee of n8n or any AI company.

Not included: social posting without your review, buying n8n hosting, or off-platform payment.

Message me with the copy-paste job you want to retire. Do not send passwords in chat; you enter credentials in n8n.
```

Do not append keyword walls. Do not add "unpublished draft" (buyer-facing text must stay valid if a human later publishes).

---

## 4. FAQ (10 items; Q ≤ 70, A ≤ 300)

Conservative limits from common Fiverr form behavior. Counts checked 2026-09-16.

### Q1 (26) / A1 (259)

```
Do you use AI in this Gig?
```

```
Only if you ask. Default is a human-designed n8n workflow with tests and operator docs. Optional light steps: classify, summarize, or draft. I review every delivery. If you want no AI, say so when you order. I do not sell raw model output or reused templates.
```

### Q2 (46) / A2 (172)

```
Are you affiliated with n8n or any AI company?
```

```
No. I am an independent freelancer. n8n is a tool I build in. I do not represent n8n, OpenAI, xAI, Google, or Fiverr. I will not claim their logos, jobs, or partner badges.
```

### Q3 (24) / A3 (198)

```
What do I need to start?
```

```
A short write-up of the manual process, the tools to connect, and whether you already have n8n Cloud or self-hosted. You enter API keys in n8n. Do not paste passwords or ID documents in Fiverr chat.
```

### Q4 (25) / A4 (213)

```
n8n Cloud or self-hosted?
```

```
Either. You keep the instance. I do not buy hosting for you. If n8n is not installed yet, say so in the order. Installing on a server you already own can be a custom offer. I will not create accounts in your name.
```

### Q5 (36) / A5 (176)

```
Will you post to my social accounts?
```

```
Not as an unattended public post. I can prepare a workflow that talks to official APIs. You keep the publish switch. No browser automation, no scraping, and no fake engagement.
```

### Q6 (31) / A6 (216)

```
Can you migrate Zapier or Make?
```

```
Often, when the same official APIs exist in n8n. I rebuild the logic rather than importing a black box. Send a screenshot of the scenario with secrets hidden. If a step has no official API, I will say so and skip it.
```

### Q7 (24) / A7 (177)

```
How are secrets handled?
```

```
You store credentials in n8n. I never ask you to send keys, ID scans, or bank details in chat. Operator docs mark secret vs editable fields. Off-platform payment is not allowed.
```

### Q8 (21) / A8 (209)

```
What is not included?
```

```
Engagement automation, deepfakes, impersonation, bulk AI content, scraping without an official API, buying paid Fiverr or n8n plans for you, and extra workflows beyond the package. Those extras stay on Fiverr.
```

### Q9 (22) / A9 (161)

```
Language and timezone?
```

```
Gig text is English. I am based in {{COUNTRY}} and work async in {{TIMEZONE}}. Japanese is OK in order chat if you prefer. Legal name and location stay accurate.
```

### Q10 (22) / A10 (170)

```
How do revisions work?
```

```
Basic includes 1, Standard 2, Premium 3, inside the original scope. New tools, new workflows, or extra-fast delivery are extras. Request them on Fiverr, not off-platform.
```

---

## 5. Requirements (asked before an order starts)

Keep questions short. Mark all five **required**. Do not ask for passwords or ID.

1. Describe the manual process you want automated.
2. Which tools should connect, and do they offer official APIs?
3. Do you already use n8n Cloud, self-hosted n8n, or neither?
4. May I add a light AI step (classify, summarize, or draft), or is this a no-AI order?
5. Confirm you will enter API credentials in n8n yourself. Do not paste secrets here. (yes / no)

---

## 6. Gallery — skip for this draft

Fiverr help: **at least one image is required to publish**. This pack does not publish.

- Do not upload to publish.
- Do not use n8n, xAI, Grok, OpenAI, Google, or Fiverr logos in a way that implies partnership.
- Do not download random Gig images from the internet.
- Later (human publish decision): original screenshot of **your** workflow canvas or docs, 1280×769 px, owned by you. Optional PDF of a redacted SOP (first three pages preview only).

Video: optional in this category; skip. Do not add copyrighted audio.

---

## 7. Minimum freelancer profile (only if Gig create requires it)

Display name: `{{DISPLAY_NAME}}` (recommended public: 石田祐太 / Yuta Ishida — pick what the form allows; keep legal name accurate).

Occupation / headline:

```
n8n automation with operator docs
```

About / description (509 characters; Fiverr About is often 600):

```
I help small teams stop copy-pasting between tools.

I build n8n workflows and, only when you ask, light AI steps (classify, summarize, draft). Then I write operator docs a non-engineer can follow: what the workflow does, how to rerun it, and which values are secrets.

Public work: Autopilot Log (official YouTube and TikTok posting APIs, fail-closed private-by-default). Site: https://yutalab.dev/

Independent freelancer in {{COUNTRY}}. Not affiliated with n8n or any AI lab. English async in {{TIMEZONE}}.
```

Skills if asked: `n8n`, `workflow automation`, `API integration`, `technical documentation`, `webhooks`.
Do not add `xAI` or `Grok` as skills.

Website: `{{WEBSITE_URL}}` or `https://yutalab.dev/`
Photo: `{{PROFILE_PHOTO_LOCAL_PATH}}` — local file only, never commit.

US person: **No**. Location: `{{COUNTRY}}` / `{{CITY}}` (Japan is fine; do not spoof).

---

## 8. Publish step — do not complete

Fiverr help lists, before publish: display name, tax forms where applicable, phone verification, email verification, personal and business information verification (KYC), and at least one gallery image.

This pack stops **before** that list. Leave the Gig unpublished.

Do not:

- Click **Publish Gig**
- Enroll in Seller Plus Kickstart
- Promote the Gig
- Accept or send orders from this draft
