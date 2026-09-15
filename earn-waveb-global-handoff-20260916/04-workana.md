> DRAFT_ONLY paste pack. NO secrets. NO marketplace login from this authoring PR. NO publish.
> CU-ready field map for a later human/CU session.
> Jobs list unread (Cloudflare). Skip paid Priority Moderation.

# CU-22 PACK — Workana (freelancer / talent)

| Key | Value |
|---|---|
| inventory | 04 |
| cu_serial | CU-22 (INDEX). **This-folder play: 3** |
| queue | B11 |
| activity_gate | site alive (sibling). Jobs **needs_check** (Cloudflare 403 this GET and sibling) |
| self_serve | yes (EN signup; register/browse/bid described free) |
| cu_ready | true (pack exists. **not registered**) |
| official | https://www.workana.com/ |
| signup | https://www.workana.com/en/signup |
| login | https://www.workana.com/en/login |
| jobs | https://www.workana.com/en/jobs |
| how_it_works | https://www.workana.com/how-it-works/freelancer |
| profile_help | https://help.workana.com/hc/en-us/articles/360041477394-How-can-I-create-edit-my-worker-profile |
| review_help | https://help.workana.com/hc/en-us/articles/360041401194-Why-do-we-review-profiles |
| payment_id_help | https://help.workana.com/hc/en-us/articles/360041359554-My-payment-is-on-Verification-What-is-this |
| google_signup_preference | **PREFER_GOOGLE** (sibling `/en/login` HTML: Google / Facebook / Apple). This GET 403 — confirm |
| paid | **NO** — skip **Priority Moderation** |
| stop_at_kyc | **STOP** |
| draft | true |
| observed | 2026-09-15 public GET |

Homepage markets LATAM talent matching **and** still exposes `/en/jobs`. Do not assume which surface a JP/EN operator sees until click-time.

## needs_check

- `/en/jobs` recency unread (Cloudflare). Do not invent “N jobs/day”.
- Google button on `/en/signup` vs `/en/login`.

## CU handoff

1. Open https://www.workana.com/en/signup (English).
2. **Find work** / Freelancer — not Hire talent.
3. **Continue with Google** as `{{GOOGLE_ACCOUNT_EMAIL}}`. Fallback: Facebook, Apple, or email.
4. Email confirm via parent Gmail MCP.
5. Profile wizard: independent/solo, real photo, English About, honest languages, placeholder rate.
6. Phone: SMS OTP only (`{{PHONE_E164}}`). ID via WhatsApp = STOP.
7. Free skills quiz OK. Do not pay for certificates.
8. **Keep my profile public** unchecked.
9. STOP before Priority Moderation, My Finances, government ID.
10. Do not send proposals.

Cloudflare: human hold with `holdDurationMs`. Do not automate the challenge.

## Field map (placeholders)

### Account

| UI field | Paste | Notes |
|---|---|---|
| Intent | Find work / Freelancer | Not client. |
| Google | `{{GOOGLE_ACCOUNT_EMAIL}}` | Preferred. |
| First / last name | split `{{FULL_LEGAL_NAME}}` | |
| Email | `{{EMAIL}}` | MAIN mailbox. |
| Password | `{{PASSWORD_DO_NOT_STORE}}` | Email path. |
| Country | `{{COUNTRY}}` | Honest. JP OK. |

### Worker profile

| UI field | Paste | Notes |
|---|---|---|
| Photo | `{{PROFILE_PHOTO_LOCAL_PATH}}` | |
| Hourly rate | `{{HOURLY_RATE_USD}}` | Skip withdrawal setup. |
| About | Long bio | Original English. Copied profiles forbidden (help). |
| Professional history | 1–3 real projects | No fake clients. |
| Skills | `n8n, automation, API integration, technical writing, SOP, documentation, workflow` | |
| Independent vs company | Independent | |
| Languages | English, Japanese + honest levels | |
| Behance | skip | Mandatory for Multimedia/Design only — this desk is automation/docs. |
| Keep my profile public | OFF | Draft. |
| Phone / WhatsApp | `{{PHONE_E164}}` for SMS OTP only | No ID photos. |

Do not paste email, phone, Skype, LinkedIn, GitHub, or off-platform pay in About (public policy).

## EN bios

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

For a first project, pick one process. I will quote inside Workana only.
```

## STOP

Do NOT: government ID, WhatsApp ID, My Finances, Priority Moderation, public checkbox, proposals, fake history, off-platform links in About.

Allowed: Google/email signup, SMS OTP, photo, English bios, free test, incomplete profile rather than KYC.

## Activity note

This GET: all Workana URLs **403**. Sibling: living marketing site; jobs unread. Draft profile **pass** as copy; job-board liquidity **needs_check**. No invented traffic. `thin_site_skip: false`.
