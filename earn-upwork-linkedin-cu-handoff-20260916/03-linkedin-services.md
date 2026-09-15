# LinkedIn Services — Service Page DRAFT (CU)

Desk: LinkedIn **Services** (Wave A6)  
Not: LinkedIn **Jobs**, feed posts, newsletters, Recruiter, Sales Navigator  
Seller: Yuta Ishida / 石田祐太  
Pack: 2026-09-16  
Mode: **`DRAFT_ONLY`**

Public entry (re-check at click-time):

- Marketplace: https://www.linkedin.com/services
- Offer services on a **personal** profile: https://www.linkedin.com/help/linkedin/answer/a569554
- Edit Service Page: https://www.linkedin.com/help/linkedin/answer/a570566
- Unpublish (after it was live — **do not use as a “draft” trick**): https://www.linkedin.com/help/linkedin/answer/a1362963
- Profile vs Company Page (choice **not currently reversible**): https://www.linkedin.com/help/linkedin/answer/a7436041
- FAQs: https://www.linkedin.com/help/linkedin/answer/a569534

QUEUE: same LinkedIn as MAIN Google. **Do not create a second LinkedIn.** Jobs boards are SKIP aggregators; this desk is Services only.

---

## 0. How far to go (then stop)

1. Confirm you are on the operator’s existing LinkedIn (MAIN Google mailbox), **personal** profile.
2. Me → View profile → **Add profile section** → **Add services** (desktop ≥ 1280px).
3. First-time “How it works” → Continue.
4. **Do not** choose Company Page / ユタラボ Page even if offered. Freelancer = personal profile. LinkedIn help: after setup you **cannot currently change** profile vs Page.
5. Fill sections 1–4 below.
6. **Save / Publish / “make viewable”:** see [CU-PLAY.md](CU-PLAY.md) §4. Official personal-profile help says **Save** makes the page **viewable by members**. If there is no unpublished draft control, record `no_draft_path` and **do not click Save**.

If KYC, Premium paywall, or ads-identity appears, [STOP-KYC.md](STOP-KYC.md).

---

## 1. Service categories (max 10)

LinkedIn uses a **fixed taxonomy** (type-to-search). Do not invent category IDs. Do not pick Home Improvement, Photography, Real Estate, etc.

First try, in order, if the live picker lists them:

| Priority | Search for | Use if… |
|---|---|---|
| 1 | Software Development | listed |
| 2 | Automation / Workflow / Integration | closest token to n8n |
| 3 | IT consulting / Consulting | only if it is clearly software/process, not life coaching |
| 4 | Technical writing / Documentation | if listed as a service type |
| 5 | API / Web development | only if listed and accurate |

Cap: **up to 10**. Prefer **3–6 honest** types over stuffing ten vague umbrellas.

`n8n` may **not** exist as a LinkedIn service type. Do not type a custom free-text category. Use Software Development / Automation neighbours.

---

## 2. About description — paste

Optional in LinkedIn help; fill it. **Live character limit wins.** Third-party writeups often cite ~500 characters; this paste is **362 characters** so it should fit. If the box is shorter, cut from the pricing sentence first, then the location sentence.

```
I build n8n workflows and the operator docs a non-engineer can rerun. Official APIs, webhooks, and first-party connectors only. No scraping, no likes or follows, no publishing to your social accounts. English, async, remote from {{CITY}}, {{COUNTRY}}. Work stays on LinkedIn until a contract exists. Pricing: Contact for pricing — not a public guaranteed hourly.
```

Do not put `{{EMAIL}}`, `{{PHONE_E164}}`, WhatsApp, or “email me at.” Inbound LinkedIn messages are enough.

Do not claim xAI / Grok employment, n8n Expert, or invented years / client counts.

---

## 3. Location and remote

| UI field | Value |
|---|---|
| Work location | `{{CITY}}`, `{{COUNTRY}}` (honest Japan location) |
| Open to remote work | **On** (checkbox) |
| Service area / radius | confirm live; do not claim “United States only” |

Do not spoof a US city to chase US buyers.

---

## 4. Pricing — no invented rates

LinkedIn help: starting hourly is a **minimum shown to buyers, not a guarantee**. You may choose **Contact for pricing**.

| Field | This pack |
|---|---|
| Starting hourly rate | **Do not fill** unless `{{STARTING_HOURLY_USD}}` was supplied **locally** by the operator for this session |
| Contact for pricing | **Select this** |

If the form requires a number and Contact-for-pricing is missing: park `rate_required`. Do not type a guessed USD.

Skip Premium-only media (documents, photos, videos, websites on the Service Page). Do not start a Premium Business / Sales Nav / Recruiter trial to unlock media.

---

## 5. Message / consultation toggles

Confirm labels in the live editor. Typical controls:

| Control | Draft stance |
|---|---|
| Allow messages from people outside your network (if shown **inside** the Services editor) | May leave **on** only if it does **not** require Save-to-publish. If it is bundled with Save = viewable, **do not Save**. |
| Provide free consultation / Request services button | **Off** unless the operator later GO’s inbound lead forms. Default for this pack: do not advertise a free consult you have not staffed. |
| Custom CTA on a Company Page | N/A — we are not on a Company Page |

---

## 6. Profile headline (optional, not a feed post)

If the Services flow also offers a profile headline edit, paste **only if** it does not auto-share:

```
n8n automation with operator docs
```

33 characters. Do **not** click Share to feed, Notify network, or Create a post about services.

---

## 7. Explicitly out of scope on this desk

- LinkedIn **Jobs** / Easy Apply / “Open to work” photo frame (Jobs = aggregator SKIP)
- Connection request blasts, InMail sequences, scraping, auto-DM
- Company Page creation, Showcase Page, University Page
- Newsletter send, article publish, feed post, event
- Ads Manager, Campaign Manager, identity for billing
- Recruiter / Sales Navigator / Premium paywalls
- Partner applications (n8n / Zapier / Make) — Wave C `late`

---

## 8. Activity note

Verdict: **Services surface exists** as a seller desk (Wave A). Not treated as closed. **Jobs is a different product.**

Evidence (2026-09-15 / help retrieved 2026-09-16), no search-volume invented:

- `linkedin.com/services` is the marketplace URL in QUEUE.
- LinkedIn Help articles for creating, editing, and unpublishing a Service Page are live.
- Help states Save makes a personal Service Page viewable; unpublish removes it from profile, feeds, and the provider directory — which is why this pack treats Save as a publish path unless a true draft control is visible.

Do not write “N buyers in your area” or similar UI marketing totals as measured demand.

---

## 9. Operator notes (JP / EN)

- English Service About. Legal location stays Japan (`{{COUNTRY}}` / `{{CITY}}`).
- MAIN Google / existing LinkedIn only.
- If the account is already offering services from an old experiment: do not publish extra categories to “complete” this pack. Log `already_member_draft` and stop.
- SNS `DRAFT_ONLY` includes **not** posting that you joined Services.
