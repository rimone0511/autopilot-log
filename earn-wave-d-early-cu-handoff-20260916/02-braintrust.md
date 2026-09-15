> DRAFT_ONLY paste pack. NO secrets. NO marketplace login from this authoring PR. NO publish.
> CU-ready field map for a later human/CU session.
> Stop at KYC. $0 talent-fee copy is public; payout bank is still STOP.
> Do not invent traffic. Homepage “2M+ members” / “10K+ roles” are marketing.

# PACK — Braintrust (Talent) — this-folder play 2

| Key | Value |
|---|---|
| inventory | 02 |
| cu_serial | **unindexed** (not CU-01–CU-28) |
| queue | C8 Wave C (high-rate talent network; **not** braintrust.com eval SaaS) |
| activity_gate | **alive** (PR#22: `/jobs` role cards; blog heading **Sep 14, 2026**) |
| self_serve | mixed — Join the Network is public; **Get Certified / ID-verified** is a stop |
| cu_ready | true (pack exists. **not registered**) |
| official | https://www.usebraintrust.com/ |
| talent | https://www.usebraintrust.com/for-talent |
| jobs | https://www.usebraintrust.com/jobs |
| join | https://app.usebraintrust.com/auth/sign_up/goals |
| login | https://app.usebraintrust.com/auth/login |
| talent_terms | https://www.usebraintrust.com/talent-terms |
| fee_terms | https://www.usebraintrust.com/site-service-fees-terms |
| google_signup_preference | **needs_check** (app signup/login this GET = SPA shell; no Google control in HTML) |
| worker_fee_public | Talent page: **“$0 fees for talent”**, **“Keep 100% of your earnings. We never charge talent.”** Client/site-service fees: see fee terms; **do not invent client %** |
| paid | **NO** |
| stop_at_kyc | **STOP** (ID-verified / Certified / Stripe or Wise bank) |
| draft | true |
| observed | 2026-09-16 public GET |

Public path copy (for-talent): Create Your Profile (~20 minutes) → AI Skills Interview → Get Certified (ID-verified, skills-validated) → Get Matched → Start Earning.

## needs_check

- Google / email / LinkedIn button labels on `app.usebraintrust.com` (SPA). Use Google if present; else MAIN mailbox. Do not create a new SNS.
- Whether a profile can stay incomplete / unsearchable after Create Your Profile. If Save = live searchable and there is no hidden state → `no_draft_path`.
- Posted dates on `/jobs` are still blank in public HTML. Do not invent “N jobs/day”. Card rates ($150–200/hr etc.) are listing copy, not our rate.

## CU handoff

Allowed later (draft only):

1. Open https://www.usebraintrust.com/for-talent → **Join the Network** (not Book a Demo, not Find Talent).
2. If **Google** is visible → `{{GOOGLE_ACCOUNT_EMAIL}}`. Else email `{{EMAIL}}` + `{{PASSWORD_DO_NOT_STORE}}`.
3. Fill profile: skills, experience, goals, EN bio. Honest `{{CITY}}`, `{{COUNTRY}}` (JP OK).
4. Photo: `{{PROFILE_PHOTO_LOCAL_PATH}}` (face, not ID crop).
5. **STOP** at Get Certified / ID verification / liveness / government ID.
6. **STOP** at AI Skills Interview if it asks for a camera identity check or government ID. A skills quiz with **no** ID is optional; skip if unclear.
7. Do not open payout / Stripe / Wise (fee terms: banking info to Payment Processor).
8. Do not apply to jobs.

## Field map (placeholders)

### Account

| UI field | Paste | Notes |
|---|---|---|
| Intent | Talent / join the network | Not client hire. |
| Google | `{{GOOGLE_ACCOUNT_EMAIL}}` if button exists | `needs_check`. |
| Email | `{{EMAIL}}` | MAIN mailbox. |
| Password | `{{PASSWORD_DO_NOT_STORE}}` | Email path. |
| Full name | `{{FULL_LEGAL_NAME}}` | Must later match ID. Do not KYC now. |

### Profile

| UI field | Paste | Notes |
|---|---|---|
| Headline | Short bio | English. |
| About | Long bio | Public-safe. |
| Skills | `n8n, workflow automation, API integration, technical documentation, SOP, AI automation, Google Workspace, Python` | Live picker wins. |
| Role | closest to automation / integration / technical writer | One primary. |
| Location | `{{CITY}}`, `{{COUNTRY}}` | Honest. No fake US. |
| Hourly | `{{HOURLY_RATE_USD}}` | Empty in git → `rate_required` if mandatory. |
| Photo | `{{PROFILE_PHOTO_LOCAL_PATH}}` | Face. |
| Portfolio | `{{PORTFOLIO_URL}}` | `https://yutalab.dev/` |
| Visibility | hidden / incomplete if offered | Draft. |

### Legal / payout — STOP MAP

| UI field | Action |
|---|---|
| Government ID / passport | STOP |
| Liveness selfie | STOP |
| Get Certified / ID-verified badge | STOP |
| Stripe / Wise / bank | STOP |
| Tax / W-8 | STOP |

## EN bios

### Short

```
n8n and AI automation with operator docs -- workflows you can rerun without me.
```

### Long

```
I help small teams stop copy-pasting between tools.

I build n8n workflows and light AI steps (classify, summarize, draft) that connect the tools you already use: forms, sheets, CRMs, inboxes, and internal APIs. Then I write the docs a non-engineer can follow: what the workflow does, what to do when it fails, and which values are secrets vs. safe to edit.

Typical deliverables:
- One production n8n workflow with retries and a failure alert
- A short SOP or README for the operator
- A change log so the next edit is not guesswork

I work in English, async, in {{TIMEZONE}}. Location: {{CITY}}, {{COUNTRY}}. Japanese is available for operator notes if you ask in-thread.

I will not:
- Automate engagement (likes, follows, fake views)
- Bypass a platform that has no official API
- Publish content on your behalf without your posting gate
- Take payment or files off Braintrust

I do not invent traffic or earnings numbers. Public work: https://yutalab.dev/ and Autopilot Log (YouTube Data API v3 + TikTok Content Posting API only).
```

## STOP

Allowed: account create, English profile fields, photo, placeholder rate.

Stop: ID-verified certification, liveness, payout bank, job apply, fake location, inventing “10K+ roles” as our metric.

## Activity note

PR#22 **alive**. This GET: talent/jobs/blog/app 200. App auth is SPA (Google unread). `thin_site_skip: false`.
