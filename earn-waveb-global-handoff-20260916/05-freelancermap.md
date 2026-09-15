> DRAFT_ONLY paste pack. NO secrets. NO marketplace login from this authoring PR. NO publish.
> CU-ready field map. First Freelancermap pack (INDEX CU-23 was `unknown` on PR#8).
> No Google OAuth on public HTML. Stay free Basic. Do not buy Premium or Persona/SILT verify.

# CU-23 PACK — Freelancermap (IT projects, DE/EU-centered)

| Key | Value |
|---|---|
| inventory | 05 |
| cu_serial | CU-23 (INDEX). **This-folder play: 4** |
| queue | B12 |
| activity_gate | **pass** — `/projects` HTML contained **2026-09-15** ISO timestamps (example `2026-09-15T19:36`). Homepage vendor totals ignored |
| self_serve | yes (free account; email activation) |
| cu_ready | true (pack exists. **not registered**) |
| official | https://www.freelancermap.com/ |
| registration | https://www.freelancermap.com/registration |
| login | https://www.freelancermap.com/login |
| projects | https://www.freelancermap.com/projects |
| pricing | https://www.freelancermap.com/pricing/freelancer |
| help | https://www.freelancermap.com/help.html |
| privacy | https://www.freelancermap.com/data-privacy.html |
| for_freelancer | https://www.freelancermap.com/for-freelancer |
| profile_tips_2026 | https://www.freelancermap.com/blog/freelance-profile-tips-examples/ |
| google_signup_preference | **NOT_OFFERED_OAUTH** on public registration/login HTML (2026-09-15). Use MAIN mailbox as email |
| paid | **NO** — free **Basic** only. Premium public price from €13.99/month billed annually |
| stop_at_kyc | **STOP** (optional paid Persona/SILT profile verification) |
| draft | true |
| observed | 2026-09-15 public GET |

Positioning: IT freelance project board, 0% commission marketing, DE/EU-heavy. Keep `{{COUNTRY}}` honest (Japan OK). Do not fake a German city. On-site DE contracts may appear — filter later; this pack does not apply.

## needs_check

- Whether the live UI later adds Google OAuth (not in this HTML).
- Whether “Activate profile” is required before save, and whether activate = searchable. Prefer inactive / private / anonymous (2026 blog describes those visibility modes).
- Basic application cap (FAQ: up to 10 projects/month) is **not** a reason to apply from this pack. Send **0**.

## CU handoff

1. Open https://www.freelancermap.com/registration
2. Account type **Freelancer / Agency** (seeking projects). **Not** Project provider.
3. Email = `{{EMAIL}}` / `{{GOOGLE_ACCOUNT_EMAIL}}` (same MAIN mailbox). Password `{{PASSWORD_DO_NOT_STORE}}`.
4. Activation link → parent Gmail MCP. FAQ: account is inactive until the link is clicked.
5. Dashboard → **Create profile**. Skills, experience, project history, English summary.
6. Photo: `{{PROFILE_PHOTO_LOCAL_PATH}}` (FAQ: JPEG/JPG/PNG, ≤5 MB).
7. Visibility: private or anonymous if offered. Do not push public search.
8. Stay **Basic**. Close Upgrade / Get Premium.
9. **STOP** before Verify profile (Persona/SILT), IBAN/PayPal checkout, and any **Apply**.

If a Google button appears at click-time despite this GET: **PREFER_GOOGLE** then, still MAIN only. Record the label change in the session log.

## Field map (placeholders)

### Registration (public HTML 2026-09-15)

| UI field | Paste | Notes |
|---|---|---|
| Account type | Freelancer / Agency | Not Project provider. |
| Email address | `{{EMAIL}}` | MAIN Google mailbox. No OAuth button in this HTML. |
| Password | `{{PASSWORD_DO_NOT_STORE}}` | FAQ: 8+ characters, number, special, uppercase (page JSON). |
| Country | `{{COUNTRY}}` | Honest. JP listed in country API payload. |
| Salutation | `None` / skip if optional | Do not invent. |
| First name | from `{{FULL_LEGAL_NAME}}` | |
| Last name | from `{{FULL_LEGAL_NAME}}` | |
| Date of birth | optional — skip unless required | FAQ placeholder `DD.MM.YYYY`. Not KYC by itself; still skip if it sits on a verify screen. |
| Newsletter | off unless required | |

### Profile (FAQ + 2026 blog; live form wins)

| UI field | Paste | Notes |
|---|---|---|
| Headline / title | Short bio | English. |
| About / summary | Long bio | |
| Skills / keywords | `n8n, workflow automation, API integration, technical documentation, SOP, Python, Google Workspace, AI automation` | Blog: platform suggests keywords from skills text. |
| Availability | remote / honest % | JSON has availability percents. Do not claim 100% on-site DE. |
| Daily / hourly rate | `{{DAILY_RATE_EUR}}` or `{{HOURLY_RATE_USD}}` as the live field asks | Park `rate_required` if empty and required. |
| Location | `{{CITY}}, {{COUNTRY}}` | No fake Berlin/Munich. |
| Languages | English; Japanese native if true | |
| Website | `{{WEBSITE_URL}}` only if the profile field is not an off-platform chat funnel | |
| Photo | `{{PROFILE_PHOTO_LOCAL_PATH}}` | |
| Profile active | **off / inactive** if save works without it | FAQ: apply requires active profile — we are not applying. |
| Visibility | private or anonymous if offered | 2026 blog. |
| VAT ID (Settings / Personal data) | **do not fill** from this pack | Intra-community reverse charge later. |
| IBAN / PayPal / SEPA | **STOP** | Membership checkout. |

### Do not open

| Screen | Why |
|---|---|
| `/pricing/freelancer` checkout / Get Premium now | Paid plan |
| Verify profile now | Paid KYC (Persona €50/year Premium, €75/year Basic on public pricing HTML) |
| Apply / one-click AI applications | Publish-path + Basic contingent |
| Project provider console | Wrong role |

## EN bios

### Short

```
n8n + API automation freelancer -- I ship the workflow and the operator SOP.
```

### Long

```
I build n8n workflows and the short manuals a teammate can rerun without me.

Typical mission: one process stuck between a form, a sheet, a CRM, and a chat tool. I map the trigger and the definition of done, connect official APIs, add a failure alert, and write a numbered SOP (what to edit, where secrets live, how to replay a failed item).

Stack I use on purpose: n8n, HTTP APIs, Google Workspace, Notion/Airtable, and light LLM steps for classify/summarize/draft. I do not scrape products that have no public API, and I do not run social-engagement bots.

I work in English, async, timezone {{TIMEZONE}}. Based in {{CITY}}, {{COUNTRY}}. Remote-first. I do not pretend to be on-site in the EU.

First engagement: one workflow plus docs. Extra systems are a new project. Chat and files stay on freelancermap.
```

## STOP

Allowed: email signup with MAIN mailbox, activation link, draft profile on **free Basic**, hidden/inactive if offered.

Stop:

- Premium / Business / Enterprise
- Profile verification (SILT / Persona: ID documents + selfie biometrics; paid)
- IBAN / PayPal / SEPA / credit card
- VAT ID submit
- Applying to projects / activating solely to apply
- Project-provider account

## Activity note

Verdict: **alive** (project listing timestamps on 2026-09-15). Free Basic documented on help + pricing. Google OAuth **not** on public register HTML. Homepage “thousands of experts / weekly projects” copy is vendor marketing — **not** used as a count.

`thin_site_skip: false`.
