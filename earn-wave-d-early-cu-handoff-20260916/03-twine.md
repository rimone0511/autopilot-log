> DRAFT_ONLY paste pack. NO secrets. NO marketplace login from this authoring PR. NO publish.
> CU-ready field map for a later human/CU session.
> Skip Ari aggregated jobs. Direct Twine posts were the activity proof — still 0 applications.
> Do not invent a freelancer commission %. Public “Service fee from 5%” is client hire copy.

# PACK — Twine — this-folder play 3

| Key | Value |
|---|---|
| inventory | 03 |
| cu_serial | **unindexed** |
| queue | D3 Wave D (`needs_activity_check` → PR#22 **alive**) |
| activity_gate | **alive** (PR#22: direct Remote job “Posted 4 days ago”) |
| self_serve | yes (public `/signup` 200) |
| cu_ready | true (pack exists. **not registered**) |
| official | https://www.twine.net/ |
| jobs | https://www.twine.net/jobs |
| signup | https://www.twine.net/signup |
| pricing | https://www.twine.net/pricing |
| help | https://help.twine.net/en/ |
| google_signup_preference | **PREFER_GOOGLE** (signup JS: `signingUpViaGoogle` / `gotGoogleOAuthURL`. Visible button needs JS) |
| worker_fee_public | Freelancer: sibling “Create a portfolio for free”. Pricing Standard **$ 0.00 per month**, “Free to start and only pay a Twine service fee when you hire” = **client**. “Service fee from 5%” = client sliding fee. **Do not write a seller % that was not on a freelancer fee table.** |
| paid | **NO** — skip Business **$ 139.99 per project** |
| stop_at_kyc | **STOP** |
| draft | true |
| observed | 2026-09-16 public GET |

`/jobs` has two surfaces. Use only “Jobs posted directly onto the Twine platform”. The Ari block “searches hundreds of sources” is aggregator — **SKIP**.

## needs_check

- Visible Google button label after JS (this GET noscript: “Looks like you have JavaScript disabled”).
- Freelancer vs client accountType on the live form.
- Whether portfolio can stay hidden.

## CU handoff

1. Open https://www.twine.net/signup (not Hire an Expert).
2. **Google** as `{{GOOGLE_ACCOUNT_EMAIL}}`. Fallback: email `{{EMAIL}}` + `{{PASSWORD_DO_NOT_STORE}}`.
3. Account type **freelancer / find work**.
4. Draft portfolio: EN bios, skills, `{{WEBSITE_URL}}`. Hidden if offered.
5. Stay on Standard **$0.00 / month**. Close Business.
6. **STOP.** No applications (direct or Ari). No quotes. No ID/payout.

Cloudflare / Press & Hold: `holdDurationMs`. Do not invent job-board density.

## Field map (placeholders)

### Account

| UI field | Paste | Notes |
|---|---|---|
| Intent | Find work / freelancer | Not hire. |
| Google | `{{GOOGLE_ACCOUNT_EMAIL}}` | Preferred. |
| Email | `{{EMAIL}}` | MAIN mailbox. |
| Password | `{{PASSWORD_DO_NOT_STORE}}` | Email path. |
| Username | `{{DISPLAY_NAME}}` | |
| Full name | `{{FULL_LEGAL_NAME}}` | Do not KYC now. |

### Portfolio / profile

| UI field | Paste | Notes |
|---|---|---|
| Tagline | Short bio | English. |
| About | Long bio | No off-platform “message me”. |
| Skills | `n8n, automation, API, technical writing, SOP, AI, documentation, webhooks` | Live picker. |
| Location | `{{CITY}}, {{COUNTRY}}` | Honest. Remote. |
| Rate | `{{HOURLY_RATE_USD}}` | Empty → `rate_required`. |
| Photo | `{{PROFILE_PHOTO_LOCAL_PATH}}` | Face. |
| Website | `{{WEBSITE_URL}}` | Public site OK; not a pay-off-Twine pitch. |
| Visibility | hidden if offered | Draft. |

## EN bios

### Short

```
n8n automation + operator docs. English. I stay on Twine for chat and files.
```

### Long

```
I build n8n workflows and the short manuals that let a teammate rerun them.

If your work is stuck between a form, a spreadsheet, a CRM, and a chat tool, I connect those steps, add a failure alert, and write a numbered SOP (what to click, what never to paste into chat, how to replay a failed item).

I work in English, based in {{CITY}}, {{COUNTRY}}, timezone {{TIMEZONE}}. Japanese is available for operator notes if you want a bilingual SOP -- say so in the Twine thread.

I do not:
- Move the project off Twine
- Automate likes, follows, or fake traffic
- Scrape a product that has no official API
- Apply to Ari aggregated listings from other boards

For a first project, pick one process. I will quote inside Twine only. Starting at {{STARTING_BUDGET_USD}}. Hourly {{HOURLY_RATE_USD}}.
```

## STOP

Do NOT: Ari applications, any job apply, Business plan, ID/payout, invent seller 5% as “my fee”, un-hide without a human GO.

Allowed: Google/email signup, draft portfolio, Standard $0.

## Activity note

PR#22 **alive** (direct Remote timestamp). This GET: `/jobs` `/signup` `/pricing` 200. `thin_site_skip: false`.
