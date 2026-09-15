# PeoplePerHour -- Hourlies / Offers DRAFT pack

Desk: PeoplePerHour (PPH)
Product name: public URLs still use `/hourlie/`; help and listing pages now say **Offers** (fixed-price packages, max 5-day delivery). This pack covers both names.
Pack: Week-2 GLOBAL
Checked: 2026-09-15 (register page, freelance-jobs page, public Hourlie URLs, PPH Terms)
Mode: DRAFT ONLY -- stop before ID docs and before any paid subscription
Paid plans: NO (PPH Basic and TopAccess look paid in current Terms -- do not subscribe)
Language: English profile OK for a Japanese operator
Google signup: YES (also Facebook or email)

Public entry:

- Home: https://www.peopleperhour.com/
- Register: https://www.peopleperhour.com/site/register
- Freelance jobs: https://www.peopleperhour.com/freelance-jobs
- Hourlie/Offer URL pattern: https://www.peopleperhour.com/hourlie/...
- Application help: https://support.peopleperhour.com/hc/en-us/articles/4408655983633-Freelancer-Application-Process
- Offers posting help: https://support.peopleperhour.com/hc/en-us/articles/205217517-Posting-Offers
- Account verify (KYC) help: https://support.peopleperhour.com/hc/en-us/articles/360001764608-Verify-your-Account
- Terms (subscription language): https://www.peopleperhour.com/static/terms

---

## 1. Signup steps (draft)

1. Open https://www.peopleperhour.com/site/register
2. Choose **I want to work as a freelancer** (not hire).
3. Prefer **Continue with Google** as `{{GOOGLE_ACCOUNT_EMAIL}}`.
   Fallback: Facebook or **Sign up with email** (`{{EMAIL}}` / `{{PASSWORD_DO_NOT_STORE}}`).
4. Complete email verification. Official application help: you cannot start the freelancer application form until the email is verified. Click the mail link. Do not paste the link or code into git.
5. Application form (draft only):
   - Upload a genuine photo of the person operating the desk (`{{PROFILE_PHOTO_LOCAL_PATH}}`). Help: no logos, cartoons, illustrations, or fake faces.
   - Location: `{{CITY}}`, `{{COUNTRY}}` -- must be accurate. Help warns mismatched location can reject the application.
   - About you: paste Long bio below.
   - Skills: n8n, automation, documentation (see field map).
6. STOP at **choose your subscription**.
   - Current public Terms describe **PPH Basic** as a non-refundable annual subscription (monthly or prepaid) and **TopAccess** as a second paid annual plan.
   - This pack forbids paid plans. If the UI will not submit the application without a paid plan, leave the account as an unverified / unsubmitted draft and record `blocked_paid_plan` in the activity log.
   - Do not buy TopAccess, extra proposal credits, featured Offers, or Fast-Track document review.
7. Do not open Settings -> Payments to upload ID documents.
8. Keep Hourlie/Offer copy in this file until an unpaid posting path exists. Do not click **Post an Offer** if posting requires a paid plan.

---

## 2. Field map (PLACEHOLDERS only)

### 2.1 Register / application

| UI field | Paste value | Notes |
|---|---|---|
| Role | `work as a freelancer` | Not buyer. |
| Google | `{{GOOGLE_ACCOUNT_EMAIL}}` | Confirmed on public register page 2026-09-15. |
| Email | `{{EMAIL}}` | Still verified even after Google, per application help. |
| Password | `{{PASSWORD_DO_NOT_STORE}}` | Email path only. |
| Profile picture | `{{PROFILE_PHOTO_LOCAL_PATH}}` | Real headshot. Rejection risk if logo/cartoon. |
| Location | `{{CITY}}, {{COUNTRY}}` | Honest. JP OK. |
| About you | Long bio | English. |
| Skills | `n8n, workflow automation, API integration, technical writing, SOP, AI automation, Google Workspace, documentation` | Match live skill picker; do not invent skill IDs. |
| Subscription | **do not select a paid plan** | See stop list. |

### 2.2 Hourlie / Offer draft (do not post if paid-gated)

Help: Post an Offer from the header. Offers are fixed-price, not hourly, deliverable within **maximum 5 days** after buyer instructions. Price is tax/VAT-inclusive. No name, contact details, or website in the Offer text.

| UI field | Paste value | Notes |
|---|---|---|
| Title | `I will build one n8n workflow and write the operator SOP` | Search-shaped, not vague. |
| Price | `{{HOURLY_RATE_USD}}` converted to a **fixed** package price locally | Field is not hourly. Do not put a live number in git. Include VAT if you are VAT-registered; otherwise follow the on-screen tax hint. |
| Delivery time | `5` days or less | Hard cap per Offers help. If the real job needs more than 5 days, split into a smaller Offer -- still draft only. |
| Category | Programming / automation closest live option | Confirm in UI. |
| Subcategory | confirm in UI | Do not guess IDs. |
| Keywords (about 5) | `n8n, automation, SOP, API, documentation` | YouTube 2026 walkthroughs mention max five keywords; confirm live limit. |
| Images | original screenshots of a sanitized demo workflow | No stock photos. No client PII. No secrets in the screenshot. |
| Search blurb (2-3 lines) | see Short Offer blurb | |
| Description | see Offer description | Must state exact deliverables and exclusions. |
| What I need to start | see Buyer inputs | |
| Add-ons | draft only; do not purchase featured | |
| Priority delivery | leave off | Extra paid-looking option; skip. |

Add-on drafts (text only):

```
Add-on A: Extra revision pass after the operator tests the workflow -- extra {{ADDON_PRICE_A}}, +1 day
Add-on B: Second small workflow (same stack) -- extra {{ADDON_PRICE_B}}, +2 days
```

Do not enable paid Priority Delivery.

### 2.3 Short Offer blurb

```
One n8n workflow plus a short operator SOP. APIs, sheets, or forms in; alerts out. English handoff. 5-day cap.
```

### 2.4 Offer description paste

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

### 2.5 Buyer inputs paste

```
1. The process in 5-10 bullets (trigger, steps, done)
2. Tools to connect (names only)
3. Example of a good vs bad output
4. Whether you already have n8n Cloud or self-host
Do not send passwords. Use placeholder credentials until the paid job (later) starts.
```

---

## 3. EN bios (AI automation / n8n / docs seller)

### Short (About teaser / profile headline if asked)

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

---

## 4. Stop-before-KYC checklist

PPH Payments verification (official help): Profile -> Settings -> Payments -> upload identification documents. Fast-Track vs Basic review is a paid speed choice. Stop before that screen.

Do NOT:

- [ ] Upload government ID, utility bill, or other KYC files
- [ ] Pay Fast-Track document approval
- [ ] Subscribe to PPH Basic if the UI charges for it
- [ ] Subscribe to TopAccess (partner marketplaces bundle)
- [ ] Buy extra proposal credits, featured Offers, or featured profile
- [ ] Pay a qualifying-period "extension package"
- [ ] Put contact details or a website inside an Offer
- [ ] Post the Offer / send proposals from this draft
- [ ] Claim CERT / verified badge

Allowed for this pack:

- [ ] Google (or email) freelancer register
- [ ] Email verify
- [ ] Draft application fields + photo
- [ ] Save Offer copy locally in this pack
- [ ] Stop if the next button is a paid subscription

---

## 5. Activity note

Verdict: **alive** (marketplace). Seller activation: **blocked_paid_plan** unless a free submit path still appears in the live UI (`needs_check` at click-time).

Evidence from public pages on 2026-09-15 (no traffic totals invented):

- Register page loads with Google / Facebook / email.
- https://www.peopleperhour.com/freelance-jobs listed many jobs with timestamps such as "2 minutes ago", "an hour ago", "2 hours ago" on 2026-09-15, with proposal counts on those cards.
- Hourlie URLs still resolve. Example public Offers about n8n automation were reachable (titles and fixed prices visible). That shows the packaged-service surface is not a dead route. It does not prove sales volume.

Paid-plan flag:

- PPH Terms (public) describe PPH Basic as a paid annual subscription (15 proposal credits / month; application review in two business days) and TopAccess as a higher paid bundle.
- Therefore this desk is **not** a free seller desk under current Terms, even though the job board looks alive.
- Click-time check: if a zero-cost application submit still exists, record it; do not assume it from Terms, and do not pay to find out.

---

## 6. Operator notes (JP / EN)

- Application help stresses a real photo and a real location. Japan is acceptable; a fake UK flag is a reject risk.
- English About-you is expected. Fluency claims must be honest.
- Hourlies are Offers: fixed price, <=5 days. A full docs+automation program that needs two weeks must be split or left for hourly projects later -- still not from this draft.
- Phoenix (on-site AI assistant) is PPH product UI, not our bot. Ignore it for this pack.
