# Guru.com -- seller / profile DRAFT pack

Desk: Guru.com
Pack: Week-2 GLOBAL
Checked: 2026-09-15 (public help + public jobs browse)
Mode: DRAFT ONLY -- stop before ID verification
Paid plans: NO (stay on free Basic)
Language: English profile OK for a Japanese operator
Google signup: YES (also Facebook, LinkedIn, or email)

Public entry:

- Home: https://www.guru.com/
- Jobs browse: https://www.guru.com/d/jobs/
- Signup help: https://www.guru.com/help/freelancer/create-an-account-freelancer/
- Profile help: https://www.guru.com/help/freelancer/profile-overview/
- Services help: https://www.guru.com/help/freelancer/services/
- Membership help: https://www.guru.com/help/freelancer/membership/
- ID verification help: https://www.guru.com/help/freelancer/submitting-your-documents-freelancer/

---

## 1. Signup steps (draft)

Do this in a browser you control. Do not store the password in this repo.

1. Open https://www.guru.com/ and click Sign Up.
2. Prefer Google: choose Google, sign in as `{{GOOGLE_ACCOUNT_EMAIL}}`.
   Fallback: Facebook, LinkedIn, or email (`{{EMAIL}}` + `{{PASSWORD_DO_NOT_STORE}}`).
3. Select account type **Freelancer** (not Employer).
4. Agree to Terms of Service if prompted.
5. Click Proceed.
6. If you used email (not Google): enter the security code from the inbox. Code expires in 24 hours. Do not share the code in chat or git.
7. Land on the dashboard / profile builder. Stay on **Basic** membership (free). If an upgrade screen appears, close it.
8. Fill profile + one Service using the field map below. Keep the profile **hidden** if the UI offers public vs hidden, until a later human publish decision.
9. STOP. Do not click Verify / ID Verification. Do not add a credit card. Do not buy quotes, Premium Quotes, or Sales Messages.

Email security-code note (email path only): after three wrong attempts you can request a resend. If verification fails, stop and contact Guru support from the official site -- do not paste codes here.

---

## 2. Field map (PLACEHOLDERS only)

### 2.1 Account / identity-adjacent (account create only)

| UI field | Paste value | Notes |
|---|---|---|
| Full name | `{{FULL_LEGAL_NAME}}` | Must later match ID if KYC is ever done. Do not KYC now. |
| Email | `{{EMAIL}}` | Use Google email if Google signup. |
| Password | `{{PASSWORD_DO_NOT_STORE}}` | Email path only. Never commit. |
| Account type | `Freelancer` | Required. |
| Google social login | `{{GOOGLE_ACCOUNT_EMAIL}}` | Preferred path. |

### 2.2 Profile About (from public Profile Overview help)

| UI field | Paste value | Notes |
|---|---|---|
| Screen Name | `{{DISPLAY_NAME}}` | Display name across Guru. |
| Website | leave blank | Help says URL shows only on paid Professional / Business / Executive. Do not pay to unhide it. |
| Profile type | `Individual` | Not a company team profile. |
| Tagline | see Short bio | Mission / headline. |
| Bio / Company History | see Long bio | English OK. |
| Work Terms | see Work Terms paste | Hours, payment, comms. |
| Featured Team Members | leave blank | Company profiles only. |
| Attach Files / Videos | optional later | Portfolio files only. No ID scans. |
| Profile visibility | `Hidden` if available | Hidden profiles do not show in freelancer search. Draft default. |

### 2.3 Service listing (from public Services help)

Path: Edit Profile -> Services -> +

| UI field | Paste value | Notes |
|---|---|---|
| Title | `n8n and AI automation plus operator docs` | Skill keywords in the title. |
| Description | see Service description paste | Approach + deliverables. |
| Skills (max 25 per service) | `n8n, AI automation, workflow automation, API integration, technical documentation, SOP writing, Zapier migration, Make migration, Google Workspace, webhooks` | Skills also drive Job Matches. |
| Rate/Hour | `{{HOURLY_RATE_USD}}` | USD. Do not invent a live rate in git. |
| Starting at | `{{STARTING_BUDGET_USD}}` | Minimum budget. |
| Category | `Programming & Development` | Homepage lists this as a live category. |
| Subcategory | pick closest to automation / scripting / API in the live dropdown | If no exact match, use the nearest Programming skill set. Do not guess a hidden ID. |

Optional extra services (draft titles only, same rates placeholders):

1. `Technical documentation and SOP packs for automations`
2. `Migrate Zapier or Make scenarios into n8n`

Do not create paid Featured Services.

### 2.4 Work Terms paste

```
Availability: weekdays in {{TIMEZONE}}, async-first.
Payment: Guru SafePay / invoice on platform only. No off-platform payment.
Communication: Guru messages first. English. Written requirements before build.
Revisions: scoped in the quote. Extra scope is a new milestone.
```

### 2.5 Service description paste

```
I design, build, and document n8n workflows so operators can run them without me.

Typical work:
- Map the current manual process
- Build the n8n workflow (triggers, APIs, error handling)
- Hand over a short operator guide (what breaks, how to rerun, where secrets live)

I do not scrape platforms that have no official API, and I do not ship unpublished social posts.

Starting at {{STARTING_BUDGET_USD}}. Hourly {{HOURLY_RATE_USD}}.
```

---

## 3. EN bios (AI automation / n8n / docs seller)

English is the profile language. A Japanese operator may keep legal name and location accurate (`{{COUNTRY}}` / `{{CITY}}`). Do not invent a US/EU address.

### Short (tagline)

```
n8n and AI automation with operator docs -- workflows you can rerun without me.
```

### Long (Bio / Company History)

```
I help small teams stop copy-pasting between tools.

I build n8n workflows and light AI steps (classify, summarize, draft) that connect the tools you already use: forms, sheets, CRMs, inboxes, and internal APIs. Then I write the docs a non-engineer can follow: what the workflow does, what to do when it fails, and which values are secrets vs. safe to edit.

Typical deliverables:
- One production n8n workflow with retries and a failure alert
- A short SOP or README for the operator
- A change log so the next edit is not guesswork

I work in English, async, in {{TIMEZONE}}. Location: {{CITY}}, {{COUNTRY}}.

I will not:
- Automate engagement (likes, follows, fake views)
- Bypass a platform that has no official API
- Publish content on your behalf without your posting gate
- Take payment or files off Guru

If you need a scoped first pack -- one workflow plus docs -- start from the Service on this profile. If you need a larger system, send the job and I will quote milestones.
```

---

## 4. Stop-before-KYC checklist

Guru ID Verification is a hard stop. Official help lists document uploads, a credit-card micro-charge, and a non-refundable **4.95 USD** processing fee. That is both KYC and a paid step.

Do NOT:

- [ ] Click Verify on the dashboard
- [ ] Enter mobile number for Guru ID Verification (SMS as part of ID)
- [ ] Type legal name / residential address into the ID Verification form
- [ ] Upload a photo taken for ID Verification
- [ ] Upload government photo ID (passport, license, national ID, voter ID)
- [ ] Upload proof of address (utility bill, bank statement, card statement)
- [ ] Enter credit card data or complete the random <=10 USD charge
- [ ] Pay the 4.95 USD document-review fee
- [ ] Upgrade Basic -> Basic+ / Professional / Business / Executive
- [ ] Buy extra quotes, Premium Quotes, Sales Messages, or featured ranking
- [ ] Send a live Quote to an employer from this draft
- [ ] Un-hide the profile for search without a later human decision

Allowed for this pack:

- [ ] Google (or email) account create as Freelancer
- [ ] Email security-code verify if on the email path
- [ ] Draft Screen Name, tagline, bio, Work Terms
- [ ] Draft one Service with placeholder rates
- [ ] Leave membership on free Basic

---

## 5. Activity note

Verdict: **alive**

Evidence from public pages on 2026-09-15 (no traffic totals invented):

- Homepage https://www.guru.com/ loads and lists live freelancer categories (Programming & Development, Writing, Design, etc.).
- Jobs index https://www.guru.com/d/jobs/ shows current listings with recent timestamps in search snippets, including posts labeled "Posted 1 hr ago" and other 2026 dates with quotes already received.
- Category skill pages (example: Programming HTTP jobs, social-media automation jobs) also show 2026-dated posts with quote counts.

Not used: Guru's own marketing totals ("800,000 employers", "1 Million Paid Invoices") are vendor claims, not a measured activity count for this gate.

Membership: free Basic exists (10 quotes / month per Guru membership help). Stay there.

---

## 6. Operator notes (JP / EN)

- English profile is enough. Do not add a Japanese bio unless a later pack asks for it.
- Keep `{{COUNTRY}}` honest (Japan is fine). Do not spoof a US employer-friendly location.
- Job Matches may email you after skills are saved. That is not a publish action. Do not reply with quotes until KYC/paid policy is revisited.
