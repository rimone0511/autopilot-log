# Malt.com (EU) -- freelancer profile DRAFT pack

Desk: Malt.com (EU freelance marketplace / FMS)
Pack: Week-2 GLOBAL
Checked: 2026-09-15 (malt.com home, country freelancer pages, Malt Help)
Mode: DRAFT ONLY -- stop before identity and company-document validation
Paid plans: NO (signup is free; do not buy boosts if offered)
Language: English profile OK for a Japanese operator
Google signup: **needs_check** (not confirmed on a public help page; email "create my account" is documented)

Public entry:

- Global home: https://www.malt.com/
- Freelancer pitch (EN): https://www.malt.com/c/freelancers
- Create-account path (from help): click **create my account** (UI may route through `/who-are-you`)
- Help -- get started: https://help.malt.com/hc/en-150/articles/30748346951826-How-do-I-get-started-as-a-freelancer-on-Malt
- Help -- complete profile: https://help.malt.com/hc/en-150/articles/29517405925778-How-do-I-complete-and-modify-my-profile-on-Malt
- Help -- legal documents: https://help.malt.com/hc/en-150/articles/29943035945106-How-to-validate-your-legal-documents-on-Malt
- Help -- register from abroad: https://help.malt.com/hc/en-150/articles/29511599491090-I-am-a-freelancer-registered-abroad-For-which-countries-does-Malt-authorize-registration-in-this-situation
- Western Europe legal fields: https://help.malt.com/hc/en-150/articles/29946127990162-Western-Europe
- Public n8n talent tag (FR, activity signal): https://www.malt.fr/s/tags/n8n-68b1ce80892ea37fa07d5f7b

Malt is **matchmaking**, not a public job board. Clients search profiles or send briefs. Completing a profile is not the same as KYC. Payments require legal-document validation -- that is the stop line.

---

## 1. Signup steps (draft)

1. Open https://www.malt.com/ (or a country host such as https://en.malt.fr/ if the UI geo-routes). Switch the UI to **English** if offered.
2. Click **Create my account** / **I'm looking for a project** (freelancer), not company hire.
3. Signup method:
   - If a **Google** button is visible, you may use `{{GOOGLE_ACCOUNT_EMAIL}}`. Record the actual button labels in the operator log. Public help did not document Google as of 2026-09-15 (`needs_check`).
   - Otherwise use email: `{{EMAIL}}` + `{{PASSWORD_DO_NOT_STORE}}`.
4. Fill personal and professional fields from the map below. Use English for headline, description, and skills.
5. Location: `{{CITY}}`, `{{COUNTRY}}`. Help lists **JP - Japan** among countries where registration is not globally blocked. Still: Malt is an EU-centered client base. Do not invent an EU tax address.
6. Legal status: you may **select** sole trader vs registered business as a form value if the wizard will not continue without it. Do **not** upload passport, national ID, driving licence, INPI, URSSAF, VAT proof, statutes, or beneficial-owner files.
7. Profile photo: clear, face-on, professional. Help: facial-recognition rejects tilted / inappropriate photos. Use `{{PROFILE_PHOTO_LOCAL_PATH}}` (face of the operator, not a logo).
8. Description: paste Long bio (help: at least **200 characters**).
9. Category + job: pick one primary pair (see field map). Help: a second unrelated profession needs a second email account -- do not open a second account in this pack.
10. Skills, experience, rate, remote/travel, languages.
11. Optional: import experience from a LinkedIn PDF or CV. LinkedIn import is **not** KYC. Skip if it would leak extra personal data you do not want on Malt yet.
12. Freelancer charter: accepting a charter is not identity upload. You may accept if it is a checkbox/sign, then STOP.
13. Leave profile **not publicly searchable** if the UI allows a draft/hidden state. If the only states are visible vs incomplete, keep incomplete rather than triggering document validation.
14. STOP before "validate my identity", "upload documents", "fiscal address verification", or payment onboarding.

---

## 2. Field map (PLACEHOLDERS only)

### 2.1 Account

| UI field | Paste value | Notes |
|---|---|---|
| Account intent | freelancer / looking for a project | Not company. |
| Google | `{{GOOGLE_ACCOUNT_EMAIL}}` if button exists | `needs_check`. |
| Email | `{{EMAIL}}` | Documented path. |
| Password | `{{PASSWORD_DO_NOT_STORE}}` | Never commit. |
| First / last name | split `{{FULL_LEGAL_NAME}}` | Help: official name as on passport/ID -- but do not upload the ID. |
| Birth date / birth place / citizenship | **do not fill** if the screen is the legal KYC tab | If the marketing signup only asks country, use `{{COUNTRY}}`. If it asks passport data, STOP. |
| Photo | `{{PROFILE_PHOTO_LOCAL_PATH}}` | Face, not logo. |

### 2.2 Profile (from public complete-profile help)

| UI field | Paste value | Notes |
|---|---|---|
| Headline | Short bio | English. |
| Description | Long bio | Min 200 characters (official help). |
| Category | `IT, Tech, Data & Cybersecurity` or `AI` if listed as its own category | Home page groups AI and IT/Tech. Confirm live labels. |
| Job / role | closest to `Automation engineer` / `No-code / integration` / `Technical writer` | One primary job. |
| Skills (max 50) | `n8n, workflow automation, API, webhooks, technical documentation, SOP, Google Workspace, AI automation, Make, Zapier migration, Notion, Airtable` | Avoid duplicate skills. |
| Daily rate | `{{DAILY_RATE_EUR}}` | Malt is day-rate native. Do not invent a EUR figure in git. |
| Availability | remote first; full day or half day as true | Help: remote vs on-site, full vs half day. |
| Work cities / travel radius | none extra, or home city only | Do not list EU cities you cannot actually work in. |
| Languages | `English` fluent-or-honest-level; `Japanese` native if true | English profile, JP operator. |
| Industry expertise | `SaaS`, `Professional services` if asked | Only if true. |
| Experience rows | title / company / dates / bullets from Long bio | No fake employers. |
| Portfolio | `{{PORTFOLIO_URL}}` or skip | Public docs samples only. No secrets. |
| Profile URL slug | optional later | Not required for draft. |

### 2.3 Legal / business tab -- STOP MAP

These fields exist on Malt for AML payments. Treat the whole tab as a wall.

| UI field | Action |
|---|---|
| Fiscal address | STOP if it starts document collection |
| Legal entity search (company registry autofill) | STOP |
| VAT / intra-community VAT | STOP -- never paste a real VAT ID into git; do not submit here |
| Passport / national ID / driving licence | STOP |
| URSSAF attestation, INPI certificate, company statutes, UBO | STOP (FR and other country packs) |
| Umbrella company vs own business | Do not pick umbrella just to bypass docs |

Japan note: abroad-registration help includes `JP - Japan` on the open-country list. That is **eligibility to register**, not a request to upload KYC in this pack.

---

## 3. EN bios (AI automation / n8n / docs seller)

Malt clients are mostly EU companies. English copy is fine. Do not pretend to be based in Paris/Berlin unless `{{CITY}}` is that city.

### Short

```
n8n + AI workflow freelancer -- I ship the automation and the operator docs.
```

### Long (min 200 characters; this block is longer on purpose)

```
I set up n8n workflows and write the instructions your team actually uses.

EU and remote teams hire me when a process is stuck in inboxes and spreadsheets: leads that never reach the CRM, weekly reports built by hand, or a Make/Zapier scenario that became unreadable. I rebuild that as a small n8n system with retries, a failure alert, and a short SOP.

What a typical mission looks like:
1. Map the process (trigger, systems, definition of done)
2. Build the workflow in your n8n Cloud or self-hosted instance
3. Document operator steps, secret locations, and how to rerun a failed job
4. Hand over in English, async, with written notes

Stack I use on purpose: n8n, HTTP APIs, Google Workspace, Notion/Airtable, and light LLM steps for classify/summarize/draft. I do not scrape products that have no public API, and I do not run social-engagement bots.

Based in {{CITY}}, {{COUNTRY}}. Working language: English. Timezone: {{TIMEZONE}}. Remote-first.

I am not signing legal documents or identity uploads in this first profile draft. When Malt asks for passport or company papers for payout, that is a later human decision -- not part of this pack.
```

(The last paragraph is for the operator's local notes if you need a private reminder. **Delete it before any public profile save** if you do not want process language on the live bio. Public bio should stop at the Remote-first line.)

### Long -- public-safe version (paste this)

```
I set up n8n workflows and write the instructions your team actually uses.

EU and remote teams hire me when a process is stuck in inboxes and spreadsheets: leads that never reach the CRM, weekly reports built by hand, or a Make/Zapier scenario that became unreadable. I rebuild that as a small n8n system with retries, a failure alert, and a short SOP.

What a typical mission looks like:
1. Map the process (trigger, systems, definition of done)
2. Build the workflow in your n8n Cloud or self-hosted instance
3. Document operator steps, secret locations, and how to rerun a failed job
4. Hand over in English, async, with written notes

Stack I use on purpose: n8n, HTTP APIs, Google Workspace, Notion/Airtable, and light LLM steps for classify/summarize/draft. I do not scrape products that have no public API, and I do not run social-engagement bots.

Based in {{CITY}}, {{COUNTRY}}. Working language: English. Timezone: {{TIMEZONE}}. Remote-first.
```

---

## 4. Stop-before-KYC checklist

Malt verifies identity and business papers for AML-CTF because it handles payments. Help: EEA passports / national ID / some driving licences; non-EEA often **passport only**, plus company registration docs.

Do NOT:

- [ ] Upload passport, national ID, or driving licence
- [ ] Upload proof of company registration (<3 months), statutes, UBO, URSSAF, INPI
- [ ] Submit VAT numbers into the live form from this pack
- [ ] Pay anyone to "boost" or "super Malter" the profile
- [ ] Create a second Malt account
- [ ] List fake EU work cities
- [ ] Turn on payout / bank / Wise details

Allowed for this pack:

- [ ] Create freelancer account (email; Google only if the button is really there)
- [ ] English headline, bio (>=200 characters), skills, category/job
- [ ] Photo of the operator
- [ ] Placeholder day rate `{{DAILY_RATE_EUR}}`
- [ ] Charter checkbox if it is not a document upload
- [ ] Stop at legal-document validation

---

## 5. Activity note

Verdict: **alive**

Evidence from public pages on 2026-09-15 (no traffic totals invented):

- https://www.malt.com/ loads with current marketing (including a **Malt Tech Trends 2026** report that names AI agents and n8n).
- Country freelancer pages (FR/DE/ES EN mirrors) invite profile creation and describe client search + brief matching.
- Public search https://www.malt.fr/s/tags/n8n-68b1ce80892ea37fa07d5f7b titles a live n8n freelancer tag and shows many public profiles with day rates. That is a dense public talent directory, not a thin placeholder page.
- Malt does not publish a public job list (help: clients message you). Activity is judged from the live directory + current site, not from job-card timestamps.

Vendor headlines such as "1M+ freelancers" / "90,000 companies" are not used as measured counts.

Google button: **needs_check** at click-time.

---

## 6. Operator notes (JP / EN)

- English UI + English profile is allowed. Japanese legal entity / Japan address can stay in the (later) legal tab -- not in this draft.
- Day rates on public n8n profiles vary widely; do not copy someone else's EUR number into git. Fill `{{DAILY_RATE_EUR}}` privately.
- Facial-recognition photo rules are strict. Use a recent, straight-on photo of the operator.
- Do not import a LinkedIn PDF that contains ID numbers or address scans.
