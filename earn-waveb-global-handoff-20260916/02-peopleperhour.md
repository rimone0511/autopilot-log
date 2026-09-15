> DRAFT_ONLY paste pack. NO secrets. NO marketplace login from this authoring PR. NO publish.
> **Park if paywall.** Public Terms: PPH Basic is a paid annual subscription. Do not subscribe.
> CU-ready field map for a later human/CU session.

# CU-20 PACK — PeoplePerHour (Hourlies / Offers)

| Key | Value |
|---|---|
| inventory | 02 |
| cu_serial | CU-20 (INDEX). **This-folder play: 5 (last)** |
| queue | B9 |
| activity_gate | marketplace **pass** this GET (jobs `posted_dt` 2026-09-15). Seller path **`blocked_paid_plan`** |
| self_serve | mixed — register is public; application submit may require PPH Basic |
| cu_ready | true (pack exists. **not registered**) |
| official | https://www.peopleperhour.com/ |
| register | https://www.peopleperhour.com/site/register |
| jobs | https://www.peopleperhour.com/freelance-jobs |
| terms | https://www.peopleperhour.com/static/terms |
| application_help | https://support.peopleperhour.com/hc/en-us/articles/4408655983633-Freelancer-Application-Process |
| offers_help | https://support.peopleperhour.com/hc/en-us/articles/205217517-Posting-Offers |
| kyc_help | https://support.peopleperhour.com/hc/en-us/articles/360001764608-Verify-your-Account |
| google_signup_preference | **PREFER_GOOGLE** — public register HTML: **Continue with GOOGLE** |
| paid | **NO.** PPH Basic annual + TopAccess = park |
| stop_at_kyc | **STOP** |
| draft | true |
| observed | 2026-09-15 public GET |

Product name: URLs still use `/hourlie/`; help says **Offers** (fixed-price, max 5-day delivery).

## needs_check

- Whether a **zero-cost** application submit still exists. Terms describe PPH Basic as paid. **Do not pay to find out.** If the next click is subscribe → `blocked_paid_plan` and close.

## CU handoff

1. Open https://www.peopleperhour.com/site/register
2. Choose **I want to work as a freelancer** (not hire).
3. **Continue with GOOGLE** as `{{GOOGLE_ACCOUNT_EMAIL}}`. Fallback: Facebook or email (`{{EMAIL}}` / `{{PASSWORD_DO_NOT_STORE}}`).
4. Email verify via parent Gmail MCP. Official help: application form waits on email verify.
5. Draft application: real photo, honest location, Long bio, skills.
6. **STOP at choose your subscription.**
   - Public Terms (this GET): **PPH Basic** is a **non-refundable annual** subscription (full or monthly for the Annual Term). By subscribing you receive fifteen proposal credits per month (Terms text).
   - **TopAccess** is a second non-refundable annual bundle.
   - If submit requires a plan: leave unsubmitted. Record `blocked_paid_plan`.
7. Do not open Settings → Payments (ID upload / Fast-Track).
8. Keep Offer copy in this file. Do not **Post an Offer** if posting needs a paid plan.

## Field map (placeholders)

### Register / application

| UI field | Paste | Notes |
|---|---|---|
| Role | work as a freelancer | Not buyer. |
| Google | `{{GOOGLE_ACCOUNT_EMAIL}}` | Confirmed public HTML 2026-09-15. |
| Email | `{{EMAIL}}` | MAIN mailbox. |
| Password | `{{PASSWORD_DO_NOT_STORE}}` | Email path. |
| Profile picture | `{{PROFILE_PHOTO_LOCAL_PATH}}` | Real headshot. No logo/cartoon. |
| Location | `{{CITY}}, {{COUNTRY}}` | Honest. JP OK. |
| About you | Long bio | English. |
| Skills | `n8n, workflow automation, API integration, technical writing, SOP, AI automation, Google Workspace, documentation` | Live picker wins. |
| Subscription | **do not select a paid plan** | Park if required. |

### Hourlie / Offer draft (do not post if paid-gated)

Help: Offers are fixed-price, deliverable within **maximum 5 days**. No name/contact/website in Offer text.

| UI field | Paste | Notes |
|---|---|---|
| Title | `I will build one n8n workflow and write the operator SOP` | |
| Price | fixed package from `{{HOURLY_RATE_USD}}` locally | Not hourly. No live number in git. |
| Delivery time | `5` days or less | Hard cap. |
| Keywords (~5) | `n8n, automation, SOP, API, documentation` | Confirm live limit. |
| Search blurb | Short Offer blurb | |
| Description | Offer description | |
| What I need to start | Buyer inputs | |
| Priority delivery | off | Skip paid-looking extras. |

Add-on drafts (text only):

```
Add-on A: Extra revision pass after the operator tests the workflow -- extra {{ADDON_PRICE_A}}, +1 day
Add-on B: Second small workflow (same stack) -- extra {{ADDON_PRICE_B}}, +2 days
```

### Short Offer blurb

```
One n8n workflow plus a short operator SOP. APIs, sheets, or forms in; alerts out. English handoff. 5-day cap.
```

### Offer description paste

```
What you get:
- 1 n8n workflow scoped to a single process (example: form -> sheet -> email/Slack alert)
- Error handling (retry or notify you when it fails)
- A short operator SOP: how to run it, what to edit, where secrets live
- A 15-minute async handoff note (written), not an open retainer

What you do not get:
- Unlimited tools or an all-company automation rebuild
- Scraping a site with no official API
- Social engagement automation (likes, follows, views)
- Publishing to YouTube/TikTok/other channels without your own posting gate
- Source code of unrelated products

Keep this Offer on-platform. Do not put phone, email, or a website in this box.

Languages: English.
Timezone: {{TIMEZONE}}.
```

### Buyer inputs paste

```
1. The process in 5-10 bullets (trigger, steps, done)
2. Tools to connect (names only)
3. Example of a good vs bad output
4. Whether you already have n8n Cloud or self-host
Do not send passwords. Use placeholder credentials until the paid job (later) starts.
```

## EN bios

### Short

```
English-speaking n8n builder: one workflow, one SOP, nothing off-platform.
```

### Long (About you / application)

```
I build n8n automations and the documentation that lets a non-engineer run them.

Most clients do not need a 40-node monster. They need one reliable path: a trigger, a few API or sheet steps, a clear failure alert, and a page that says what to do next. That is the pack I sell.

I also write operator docs: numbered steps, screenshots with secrets cropped out, and a change log. If you already have Zapier or Make, I can plan a migration into n8n as a separate Offer.

How I work:
- English, written-first, {{TIMEZONE}}
- Based in {{CITY}}, {{COUNTRY}} (accurate location)
- Scope in the Offer; extra work is an add-on or a new project
- All chat and files stay on PeoplePerHour

I will not automate fake engagement, scrape unofficial surfaces, or publish on your social accounts.

Photo is a real photo of me. Location is real. If that does not match your filters, skip me.
```

## STOP

Do NOT:

- Subscribe to **PPH Basic** (annual) or **TopAccess**
- Upload government ID / Fast-Track KYC
- Buy extra proposal credits or featured Offers
- Put contact details in an Offer
- Post the Offer / send proposals from this draft

Allowed: Google register, email verify, draft application text + photo, **park at paywall**.

## Activity note

This GET: freelance-jobs title **Sep 2026**; HTML `posted_dt` on **2026-09-15**. Register Google button present. Terms confirm paid Basic. Marketplace alive; seller activation **blocked_paid_plan**. No traffic totals invented.
