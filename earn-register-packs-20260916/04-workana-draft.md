# Workana -- freelancer / talent DRAFT pack

Desk: Workana
Pack: Week-2 GLOBAL
Checked: 2026-09-15 (home, signup/login public HTML, how-it-works snippets, help titles)
Mode: DRAFT ONLY -- stop before government-ID / payment KYC
Paid plans: NO (register/browse/bid are described as free; skip **Priority Moderation**)
Language: English profile OK (EN locale exists: `/en/signup`, `/en/login`, `/en/jobs`)
Google signup: YES on the public login page (Google, Facebook, Apple). Signup page is the same family; confirm the Google button on `/signup` at click-time.

Public entry:

- Home: https://www.workana.com/
- Signup: https://www.workana.com/signup/ and https://www.workana.com/en/signup
- Login (social buttons visible in public HTML): https://www.workana.com/en/login
- Jobs index: https://www.workana.com/en/jobs
- How it works (freelancer): https://www.workana.com/how-it-works/freelancer
- Profile help: https://help.workana.com/hc/en-us/articles/360041477394-How-can-I-create-edit-my-worker-profile
- Profile review help: https://help.workana.com/hc/en-us/articles/360041401194-Why-do-we-review-profiles
- Payment identity request: https://help.workana.com/hc/en-us/articles/360041359554-My-payment-is-on-Verification-What-is-this
- Security / verification policy: https://help.workana.com/hc/en-us/articles/38945543921175-Security-Verification-and-Compliance-Policy

Positioning note: the 2026 homepage markets **LATAM talent matching** for companies ("Build Your Team with Latin America's A-Players") and also still exposes a freelancer jobs URL. Treat Workana as two surfaces (agency-style matching + classic jobs). Do not assume which one a new EN/JP operator will see until click-time.

---

## 1. Signup steps (draft)

1. Open https://www.workana.com/en/signup (English).
2. Choose **Find work** / **Freelance** / **I want to work as a Freelancer** (wording varies). Do not choose Hire talent.
3. Prefer **Continue with Google** (`https://www.workana.com/login/Google` from the public login page) as `{{GOOGLE_ACCOUNT_EMAIL}}`.
   Fallback: Facebook, Apple, or email (`{{EMAIL}}` / `{{PASSWORD_DO_NOT_STORE}}`).
4. If email path: confirm the inbox link. Do not paste tokens into git.
5. Profile wizard (draft):
   - Role / specializations: automation, n8n, documentation (see field map).
   - Independent vs team: **independent / solo**.
   - Photo: real operator photo `{{PROFILE_PHOTO_LOCAL_PATH}}`.
   - Languages: English + Japanese levels that are true.
   - About + history: bios below.
   - Hourly rate: `{{HOURLY_RATE_USD}}` (help: profile currency should match later withdrawal currency; skip withdrawal setup now).
6. Phone / WhatsApp: if the wizard asks for a number only to send an SMS code, you may use `{{PHONE_E164}}` to save the draft. If it asks for a photo of ID, selfie-with-ID, or WhatsApp document send, STOP.
7. Platform "certification" / mandatory test: a skills quiz is not KYC. You may take a free test. Do not pay for certificates.
8. Completeness: help says 100% profile is required before bids. Fill text/photo/rate/history. Still **do not** submit government ID to reach 100%.
9. Visibility: help describes a **Keep my profile public** checkbox. For this draft, leave it **unchecked** (profile not on Google) if the control exists.
10. STOP before:
    - Priority Moderation (paid 24h review)
    - My Finances / withdrawal methods (PayPal / Payoneer)
    - Any request for official government ID images
11. Do not send proposals. Help: bidding is free of a subscription, but this pack is draft-only.

Cloudflare often sits in front of Workana HTML. If a challenge page appears, complete it as a human; do not automate it.

---

## 2. Field map (PLACEHOLDERS only)

### 2.1 Account

| UI field | Paste value | Notes |
|---|---|---|
| Intent | Find work / Freelancer | Not client. |
| Track | Freelance (project) not long-term exclusive | Unless you truly want FT matching later. |
| Google | `{{GOOGLE_ACCOUNT_EMAIL}}` | Confirmed on `/en/login`. |
| Facebook / Apple | skip unless Google fails | |
| First name / last name | split `{{FULL_LEGAL_NAME}}` | |
| Email | `{{EMAIL}}` | |
| Password | `{{PASSWORD_DO_NOT_STORE}}` | Email path. |
| Country | `{{COUNTRY}}` | Honest. JP OK. |

### 2.2 Worker profile (from public help + third-party walkthroughs of the wizard)

| UI field | Paste value | Notes |
|---|---|---|
| Photo | `{{PROFILE_PHOTO_LOCAL_PATH}}` | Required for approval chances. |
| Hourly rate | `{{HOURLY_RATE_USD}}` | USD display if you would later use PayPal/Payoneer -- but do not configure payout now. |
| About / Information about yourself | Long bio | English. Help: copied text from another profile is not allowed. |
| Professional history | 1-3 real projects or roles | Title, dates, skills, description. No fake clients. |
| Skills / function | `n8n, automation, API integration, technical writing, SOP, documentation, workflow` | Match live checkboxes. |
| Independent vs company | Independent | |
| Other languages | `English`, `Japanese` + honest levels | |
| Portfolio / Behance / Codewars | skip unless you have a real public URL `{{PORTFOLIO_URL}}` | Help: Behance is mandatory **for Multimedia and Design**. This desk is automation/docs -- skip Behance. |
| Certification / test | free platform test only | |
| Keep my profile public | OFF | Draft. |
| Phone / WhatsApp | `{{PHONE_E164}}` only for SMS OTP | No ID via WhatsApp. Official policy: Workana may WhatsApp from verified official accounts only; users must not move jobs off-platform. |

### 2.3 Do-not-paste (policy)

Workana policies (public help) forbid in the profile:

- Contact information (email, phone, Skype, WhatsApp, LinkedIn, GitHub, external links used to leave the platform)
- Off-platform payment offers
- Free-service offers
- Copied profile text

Keep `{{PORTFOLIO_URL}}` off the About box if it is only a contact funnel. A docs sample on a public site without chat widgets is the safer optional extra.

---

## 3. EN bios (AI automation / n8n / docs seller)

### Short

```
n8n automation + operator docs. English. I stay on Workana for chat and files.
```

### Long

```
I build n8n workflows and the short manuals that let a teammate rerun them.

If your work is stuck between a form, a spreadsheet, a CRM, and a chat tool, I connect those steps, add a failure alert, and write a numbered SOP (what to click, what never to paste into chat, how to replay a failed item).

I work in English, based in {{CITY}}, {{COUNTRY}}, timezone {{TIMEZONE}}. Japanese is available for operator notes if you want a bilingual SOP -- say so in the Workana thread.

I do not:
- Move the project to WhatsApp or email
- Automate likes, follows, or fake traffic
- Scrape a product that has no official API

For approval reviewers: this is a real person photo, a real location, and original English text. The offer is automation plus documentation, not design (no Behance).
```

Delete the last paragraph before a public-facing save if you do not want reviewer-facing language on the profile. Safer public close:

```
For a first project, pick one process. I will quote inside Workana only.
```

---

## 4. Stop-before-KYC checklist

Workana may later email you for payment verification and ask for **images of an official government ID** (and sometimes social-network proof). Help: up to 72 hours; 48 hours to reply or they refund the other party. That is KYC. Also do not use Priority Moderation.

Do NOT:

- [ ] Upload government ID, selfie-with-ID, or address documents
- [ ] Send ID photos over WhatsApp
- [ ] Open My Finances / Configure Withdrawal Options
- [ ] Buy Priority Moderation
- [ ] Check "Keep my profile public" in this draft
- [ ] Send proposals or chat pitches
- [ ] Put phone, email, or off-platform links in About
- [ ] Create simulated projects or fake history (security policy)

Allowed for this pack:

- [ ] Google (or email) talent/freelancer signup
- [ ] Email confirm
- [ ] SMS OTP if required to store the draft
- [ ] Photo, English bios, skills, rate placeholder, work history
- [ ] Free (not paid) skills test
- [ ] Leave profile incomplete rather than feeding KYC

---

## 5. Activity note

Verdict: **needs_check** (job-board liquidity). Site/brand: **alive**, not abandoned.

Evidence from public pages on 2026-09-15 (no traffic totals invented):

- https://www.workana.com/ homepage loads a current LATAM hiring product (named talent cards, rates, timezone marketing). That is an active marketing site.
- https://www.workana.com/en/jobs exists with a signup CTA. Direct fetch on 2026-09-15 returned a Cloudflare challenge, so **individual job cards and recency were not inspected**. Do not invent "N jobs/day".
- How-it-works copy still describes weekly new clients and proposal bidding. That is vendor copy, not a count.
- Login HTML shows **Continue with Google / Facebook / Apple**.
- Help still describes a 15-30 day profile review queue and optional paid Priority Moderation -- a living moderation process, not proof of buyer density.

Because the classic jobs list was not readable through Cloudflare, activity for **earning via public projects** stays `needs_check`. Do not treat homepage talent-matching as proof that an EN/JP freelancer will see a thick job feed.

---

## 6. Operator notes (JP / EN)

- EN UI is enough. Do not write the About section in Spanish/Portuguese unless you will also operate those queues.
- LATAM-timezone marketing on the home page does not require you to fake a LATAM city. Keep `{{COUNTRY}}` honest.
- Profile review can take 15-30 days per help. Waiting is not a reason to pay Priority Moderation.
- Phone verification is not the same as government-ID KYC. Stop when documents start.
