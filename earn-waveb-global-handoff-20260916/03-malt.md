> DRAFT_ONLY paste pack. NO secrets. NO marketplace login from this authoring PR. NO publish.
> CU-ready field map for a later human/CU session.
> Google button needs_check. Stop at AML document validation.

# CU-21 PACK — Malt.com (EU, English profile)

| Key | Value |
|---|---|
| inventory | 03 |
| cu_serial | CU-21 (INDEX). **This-folder play: 2** |
| queue | B10 |
| activity_gate | sibling PR#2 **pass** for English draft (live n8n directory). This GET: **403** Cloudflare |
| self_serve | yes (create my account / looking for a project) |
| cu_ready | true (pack exists. **not registered**) |
| official | https://www.malt.com/ |
| freelancer_pitch | https://www.malt.com/c/freelancers |
| help_start | https://help.malt.com/hc/en-150/articles/30748346951826-How-do-I-get-started-as-a-freelancer-on-Malt |
| help_profile | https://help.malt.com/hc/en-150/articles/29517405925778-How-do-I-complete-and-modify-my-profile-on-Malt |
| help_legal | https://help.malt.com/hc/en-150/articles/29943035945106-How-to-validate-your-legal-documents-on-Malt |
| help_abroad | https://help.malt.com/hc/en-150/articles/29511599491090-I-am-a-freelancer-registered-abroad-For-which-countries-does-Malt-authorize-registration-in-this-situation |
| google_signup_preference | **needs_check** (not documented on public help as of sibling check; this GET blocked) |
| paid | **NO** (signup free; no boosts) |
| stop_at_kyc | **STOP** (legal documents / AML) |
| draft | true |
| observed | 2026-09-15 public GET |

Malt is **matchmaking**, not a public job board. Completing a profile ≠ KYC. Payments require legal-document validation — that is the stop line.

## needs_check

- Google button presence (record live labels).
- Whole site 403 in this environment. Sibling: FR n8n tag directory looked dense. Do not invent a freelancer count.
- If the only Save makes the profile searchable and there is no incomplete/hidden state → `no_draft_path`.

## CU handoff

1. Open https://www.malt.com/ (or geo-routed country host). English UI if offered.
2. **Create my account** / **I'm looking for a project** (freelancer), not company hire.
3. If **Google** is visible → MAIN account. Else email `{{EMAIL}}` + `{{PASSWORD_DO_NOT_STORE}}`.
4. English headline, bio (≥ **200 characters** per Malt help), skills, one primary category/job.
5. Location: `{{CITY}}`, `{{COUNTRY}}`. Sibling: Japan listed among countries not globally blocked. Do **not** invent an EU tax address.
6. Legal status: you may **select** a form value if the wizard blocks. Do **not** upload ID or company papers.
7. Photo: `{{PROFILE_PHOTO_LOCAL_PATH}}` (face, not logo).
8. STOP before validate identity / upload documents / fiscal address verification / payout.

## Field map (placeholders)

### Account

| UI field | Paste | Notes |
|---|---|---|
| Intent | freelancer / looking for a project | Not company. |
| Google | `{{GOOGLE_ACCOUNT_EMAIL}}` if button exists | `needs_check`. |
| Email | `{{EMAIL}}` | MAIN mailbox. |
| Password | `{{PASSWORD_DO_NOT_STORE}}` | Never commit. |
| First / last name | split `{{FULL_LEGAL_NAME}}` | Official name — do not upload ID. |
| Birth date / birth place / citizenship | **do not fill** if this is the legal KYC tab | If passport data appears, STOP. |
| Photo | `{{PROFILE_PHOTO_LOCAL_PATH}}` | Face. |

### Profile

| UI field | Paste | Notes |
|---|---|---|
| Headline | Short bio | English. |
| Description | Long — public-safe | Min 200 characters. |
| Category | `IT, Tech, Data & Cybersecurity` or `AI` if listed | Confirm live. |
| Job / role | closest to automation / integration / technical writer | One primary job. Help: second profession = second email — **do not**. |
| Skills (max 50) | `n8n, workflow automation, API, webhooks, technical documentation, SOP, Google Workspace, AI automation, Make, Zapier migration, Notion, Airtable` | |
| Daily rate | `{{DAILY_RATE_EUR}}` | Do not invent EUR in git. |
| Availability | remote first | Honest. |
| Work cities | home city only | No fake EU cities. |
| Languages | English (honest level); Japanese native if true | |
| Portfolio | `{{PORTFOLIO_URL}}` or skip | No secrets. |

### Legal tab — STOP MAP

| UI field | Action |
|---|---|
| Fiscal address / company registry autofill | STOP if document collection starts |
| VAT / intra-community VAT | STOP — never paste a real VAT ID into git |
| Passport / national ID / driving licence | STOP |
| URSSAF, INPI, statutes, UBO | STOP |
| Umbrella company to bypass docs | Do not |

## EN bios

### Short

```
n8n + AI workflow freelancer -- I ship the automation and the operator docs.
```

### Long — public-safe (paste this)

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

## STOP

Allowed: account create, English profile fields, photo, placeholder day rate, charter checkbox.

Stop: passport/company papers, VAT submit, boosts, second account, payout/bank, fake EU location.

## Activity note

Sibling: alive directory + 2026 Tech Trends marketing (vendor totals ignored). This GET: Cloudflare 403. `thin_site_skip: false`.
