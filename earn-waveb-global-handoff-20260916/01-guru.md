> DRAFT_ONLY paste pack. NO secrets. NO marketplace login from this authoring PR. NO publish.
> CU-ready field map for a later human/CU session.
> Stop at KYC. Stay on free Basic. No invented traffic.

# CU-19 PACK — Guru.com (seller / profile)

| Key | Value |
|---|---|
| inventory | 01 |
| cu_serial | CU-19 (INDEX). **This-folder play: 1** |
| queue | B8 |
| activity_gate | sibling PR#2 **pass** (2026-dated public jobs). This GET: homepage/jobs **403** Incapsula → click-time confirm |
| self_serve | yes (public Sign Up as Freelancer) |
| cu_ready | true (pack exists. **not registered**) |
| official | https://www.guru.com/ |
| jobs | https://www.guru.com/d/jobs/ |
| signup_help | https://www.guru.com/help/freelancer/create-an-account-freelancer/ |
| profile_help | https://www.guru.com/help/freelancer/profile-overview/ |
| services_help | https://www.guru.com/help/freelancer/services/ |
| membership_help | https://www.guru.com/help/freelancer/membership/ |
| id_help | https://www.guru.com/help/freelancer/submitting-your-documents-freelancer/ |
| google_signup_preference | **PREFER_GOOGLE** (also Facebook, LinkedIn, email) |
| paid | **NO** — stay free Basic |
| stop_at_kyc | **STOP** |
| draft | true |
| observed | 2026-09-15 public GET (this folder METHOD) |

## needs_check

- Jobs recency not readable in this environment (Incapsula 403). Sibling recorded recent 2026 timestamps including “Posted 1 hr ago”. Do not invent a new count.
- Confirm Google button labels at click-time.

## CU handoff

Allowed later (draft only):

1. Open https://www.guru.com/ → Sign Up.
2. **Google** as `{{GOOGLE_ACCOUNT_EMAIL}}`. Fallback: email `{{EMAIL}}` + `{{PASSWORD_DO_NOT_STORE}}` (never commit).
3. Account type **Freelancer** (not Employer).
4. Stay on **Basic**. Close upgrade.
5. Fill field map. Profile **Hidden** if offered.
6. One Service only. Placeholder rates.
7. **STOP.** No Verify. No card. No Quote.

## Field map (placeholders)

### Account

| UI field | Paste | Notes |
|---|---|---|
| Full name | `{{FULL_LEGAL_NAME}}` | Must later match ID. Do not KYC now. |
| Email | `{{EMAIL}}` | MAIN mailbox. |
| Password | `{{PASSWORD_DO_NOT_STORE}}` | Email path only. |
| Account type | `Freelancer` | Required. |
| Google | `{{GOOGLE_ACCOUNT_EMAIL}}` | Preferred. |

### Profile About (public Profile Overview help)

| UI field | Paste | Notes |
|---|---|---|
| Screen Name | `{{DISPLAY_NAME}}` | |
| Website | leave blank | Help: URL on paid tiers. Do not pay to unhide. |
| Profile type | `Individual` | |
| Tagline | Short bio below | |
| Bio / Company History | Long bio below | English. |
| Work Terms | Work Terms paste | |
| Profile visibility | `Hidden` if available | Draft default. |

### Service (Edit Profile → Services → +)

| UI field | Paste | Notes |
|---|---|---|
| Title | `n8n and AI automation plus operator docs` | |
| Description | Service description paste | |
| Skills (max 25) | `n8n, AI automation, workflow automation, API integration, technical documentation, SOP writing, Zapier migration, Make migration, Google Workspace, webhooks` | Match live picker. |
| Rate/Hour | `{{HOURLY_RATE_USD}}` | Do not invent in git. |
| Starting at | `{{STARTING_BUDGET_USD}}` | |
| Category | `Programming & Development` | Confirm live. |

Do not create Featured Services.

### Work Terms paste

```
Availability: weekdays in {{TIMEZONE}}, async-first.
Payment: Guru SafePay / invoice on platform only. No off-platform payment.
Communication: Guru messages first. English. Written requirements before build.
Revisions: scoped in the quote. Extra scope is a new milestone.
```

### Service description paste

```
I design, build, and document n8n workflows so operators can run them without me.

Typical work:
- Map the current manual process
- Build the n8n workflow (triggers, APIs, error handling)
- Hand over a short operator guide (what breaks, how to rerun, where secrets live)

I do not scrape platforms that have no official API, and I do not ship unpublished social posts.

Starting at {{STARTING_BUDGET_USD}}. Hourly {{HOURLY_RATE_USD}}.
```

## EN bios

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

## STOP

Allowed: Google/email Freelancer create, draft profile + one Service, free Basic.

Stop:

- Verify / ID Verification (documents, SMS-for-ID, card micro-charge, **4.95 USD** fee)
- Paid membership / extra quotes / Sales Messages
- Sending a Quote
- Un-hiding the profile without a later human decision

## Activity note

Sibling PR#2: **alive** (jobs browse with 2026 timestamps). This GET: **403**. Do not invent traffic. `thin_site_skip: false` (WAF ≠ dead).
