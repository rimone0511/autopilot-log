# Freelancer.com — profile DRAFT paste

Desk: Freelancer.com (QUEUE Wave A10)  
Role: **Freelancer / Seller**, not Employer / Buyer  
Mode: **DRAFT_ONLY** — stop before KYC, wallet funding, bids, contests  
Google: **PREFER_GOOGLE**  
Language: English profile is enough for a Japan-based operator  
Checked: 2026-09-15 public GET (no login)

Public entry (opened; re-verify before CU):

- Home: https://www.freelancer.com/
- Signup: https://www.freelancer.com/signup
- Fees schedule (do not treat git as the live table): https://www.freelancer.com/feesandcharges
- Membership (do not buy): https://www.freelancer.com/membership
- KYC / Identity Policy: https://www.freelancer.com/page.php?p=info%2Fkyc_policy
- User Agreement: https://www.freelancer.com/about/terms
- Code of Conduct: https://www.freelancer.com/info/codeofconduct
- Edit profile help: https://www.freelancer.com/support/profile/how-to-edit-your-profile
- Skills help: https://www.freelancer.com/support/Profile/how-to-edit-your-list-of-skills
- Portfolio help: https://www.freelancer.com/support/Profile/how-to-add-a-portfolio
- Preferred Freelancer program (do not apply from this pack): https://www.freelancer.com/preferred-freelancer-program

CU runbook (sibling) already says: draft artifact = profile + skills; **no bids; no contests; no “Verify my Identity”.** This file is the paste for that profile step.

---

## 1. Signup steps (draft notes only — agent does not sign up)

Do this in a browser **you** control. Do not store the password in this repo. Do not complete this from an unattended CU session unless the serial runbook is open and KYC is still off.

1. Open https://www.freelancer.com/signup
2. Prefer **Continue with Google**. Sign in as `{{GOOGLE_ACCOUNT_EMAIL}}` (MAIN Google only).
   Fallback: email `{{EMAIL}}` + `{{PASSWORD_DO_NOT_STORE}}`. OTP goes to the parent Gmail path, not into git.
3. Choose **Freelancer** / work-and-get-paid. If you land on Employer / hire, back out and switch role. If you cannot switch without KYC, **stop**.
4. Agree to the live User Agreement if prompted. Do not paste legal text into chat.
5. Land on profile setup. Stay on the **free** membership. Close upgrade / Preferred / Verified upsells.
6. Paste headline, summary, and skills from this file. Hourly rate = `{{HOURLY_RATE_USD}}` locally, or leave empty if the live form allows it. **Do not invent a rate in git.**
7. Location: Japan / `{{CITY}}` / `{{COUNTRY}}`. Do not spoof a US/EU flag.
8. **STOP.** Do not click Verify my Identity. Do not add a credit card. Do not fund the Site wallet. Do not bid. Do not enter a contest. Do not apply to Preferred Freelancer.

---

## 2. Field map (PLACEHOLDERS only)

Official help (Editing my profile) lists these editable parts: **Hourly Rate, Professional Headline, Top Skills, Summary**. Resume blocks on the same page: Experience, Reference, Education, Qualification, Publication, Certification, Article. Paste only what the live form asks.

### 2.1 Account / identity-adjacent

| UI field (typical) | Paste value | Notes |
|---|---|---|
| Signup path | Google | PREFER_GOOGLE |
| Email | `{{EMAIL}}` | Same mailbox as MAIN Google |
| Password | `{{PASSWORD_DO_NOT_STORE}}` | Email path only. Never commit |
| Account type | Freelancer | Not Employer |
| Username | `{{FREELANCER_USERNAME}}` | Pick once. Do not create a second account to “retry” |
| Full name | `{{FULL_LEGAL_NAME}}` | Must later match ID if KYC is ever done. Do not KYC now |
| Country / flag | `{{COUNTRY}}` | Honest Japan is fine |
| City | `{{CITY}}` | Do not invent a US city |
| Phone | only if SMS play is already authorized elsewhere | Security phone is on the KYC path — skip unless the form blocks account create. If it is a verification selfie / ID flow, stop |

### 2.2 Profile (from public “Editing my profile” help)

| UI field | Paste value | Notes |
|---|---|---|
| Hourly Rate | `{{HOURLY_RATE_USD}}` | USD. Empty / skip if the form allows. Do not invent in git |
| Professional Headline | see Headline paste | Keep it skills + docs, not a metric claim |
| Top Skills | see Skills list | Official skills help: a **free** account may add **up to 20** skills. Do not buy membership to add more |
| Summary | see Summary paste | English |
| Profile photo | `{{PROFILE_PHOTO_LOCAL_PATH}}` | Portrait only. Never an ID scan |
| Cover photo | skip | Official help: uploading a cover photo **requires a paid membership**. Do not pay |
| Extra / multiple profiles | skip | Official help: extra profiles are Plus or higher. Do not buy |
| Portfolio item | optional later | Help’s last step is **Publish** on the item. Skip Publish. No Hire-Me-only items |

### 2.3 Resume blocks (optional, draft)

Fill only if the live form shows them. No fake employers. No invented years.

| UI field | Paste value |
|---|---|
| Experience title | `Independent automation + operator docs` |
| Experience summary | One workflow + SOP + official APIs. Public example: Autopilot Log |
| Education / Qualification | leave blank unless true |
| Website / portfolio URL if a field exists | `{{PORTFOLIO_URL}}` |
| GitHub if a field exists | `{{GITHUB_REPO_AUTOPILOT}}` |

User Agreement (public): do not advertise an unrelated external website; any URL must relate to the user / service on the site. Paste **public** portfolio / GitHub only in fields that ask for work samples. Do not put email, phone, WhatsApp, or “pay me off-site” in the profile.

### 2.4 Skills list (stay at or under 20)

Paste the nearest live skill names (the dropdown is the source of truth; do not invent hidden skill IDs):

```
n8n
API Integration
Python
Technical Writing
Documentation
Google Workspace
Zapier
Make (Integromat)   ← pick the live label
Automation
Webhooks
Workflow
ChatGPT / AI        ← pick the live label; do not claim a lab affiliation
```

If the dropdown has no exact match, skip that token. Do not buy extra skill slots.

---

## 3. Paste blocks

### Headline

```
n8n and AI automation with operator docs (official APIs, no scraping)
```

### Summary

```
I help small teams stop copy-pasting between tools.

I build n8n workflows and light AI steps (classify, summarize, draft) on official APIs or documented connectors: forms, sheets, CRMs, inboxes, internal APIs. Then I write the docs a non-engineer can follow: what the workflow does, what to do when it fails, and which values are secrets vs. safe to edit.

Typical deliverable:
- One production workflow with retries and a failure alert
- A short SOP / README for the operator
- A change log so the next edit is not guesswork

Public example of that posture: Autopilot Log (YouTube Data API v3 + TikTok Content Posting API; posting gate fails closed) — {{GITHUB_REPO_AUTOPILOT}}. Field notes: {{PORTFOLIO_URL}}.

I am {{DISPLAY_NAME}}, based in Japan, async in {{TIMEZONE}}. English is fine. Keep scoping on Freelancer.com messages. I do not scrape platforms that have no official API. I do not ship likes, follows, or fake views. I do not publish social posts without your own approve/gate step.

Hourly rate belongs in the rate field ({{HOURLY_RATE_USD}} locally). I do not take payment or files off Freelancer.com.
```

### Work Terms (only if a free-text box exists)

```
Availability: weekdays in {{TIMEZONE}}, async-first.
Payment: Freelancer Milestone / on-platform only. No off-platform payment.
Communication: Freelancer messages first. English. Written requirements before build.
Revisions: scoped in the milestone. Extra scope is a new milestone.
```

---

## 4. STOP-AT-KYC / paid walls

Official Identity Policy (opened 2026-09-15): Verified-by-Freelancer asks for government photo ID, **keycode selfie with ID**, and proof of address (utility bills / bank statements). Account name must match the ID. **Never do this in CU.** Morning human only, and only after an explicit GO.

Do NOT:

- [ ] Click **Verify my Identity**
- [ ] Upload passport / driver’s license / national ID
- [ ] Upload the keycode photo (face + ID + unique code)
- [ ] Upload proof of address (utility bill, bank statement)
- [ ] Complete Security Phone Number as part of that KYC wizard
- [ ] Pay any “Verified by Freelancer” application fee (live amounts are on the fees page — do not copy them here as a to-do)
- [ ] Apply to Preferred Freelancer (exam + KYC path)
- [ ] Buy membership, extra bids, sponsored / highlight / sealed bid upgrades
- [ ] Fund the Site wallet / Minimum Account Balance from this pack
- [ ] Send a bid or contest entry (see surgical-bid notes; default remains **no send**)
- [ ] Create a second account (Code of Conduct: no multiple accounts)

Allowed for this draft:

- [ ] Google (or email) account create as Freelancer
- [ ] Headline, summary, ≤20 skills
- [ ] Portrait photo from a local path (not ID)
- [ ] Leave membership on free

---

## 5. Activity note (desk, not GMV)

Verdict for “is the product page up”: **alive** (homepage and signup returned HTTP 200 on 2026-09-15).  
Not used: signup-title marketing totals.

This file does **not** bid. Wallet and bid limits live on the fees page and the bid UI — re-read those immediately before any later human bid.

---

## 6. Shared placeholders

Replace locally. Never commit filled values.

```
{{FULL_LEGAL_NAME}}
{{DISPLAY_NAME}}                 recommended: Yuta Ishida
{{FREELANCER_USERNAME}}
{{EMAIL}}
{{GOOGLE_ACCOUNT_EMAIL}}
{{PASSWORD_DO_NOT_STORE}}
{{COUNTRY}}
{{CITY}}
{{TIMEZONE}}
{{HOURLY_RATE_USD}}              form field; do not invent a live rate in git
{{PROFILE_PHOTO_LOCAL_PATH}}
{{PORTFOLIO_URL}}                public: https://yutalab.dev/
{{GITHUB_REPO_AUTOPILOT}}        public: https://github.com/rimone0511/autopilot-log
```
