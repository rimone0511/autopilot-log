> **JOBS phase. `DRAFT_ONLY`. DO NOT SAVE if Save publishes.**
> Existing recovered LinkedIn only. Personal Service Page paste: categories / About / CTA.
> Pricing = **Contact for pricing**. No secrets. Agent does not submit.

# LinkedIn Service Page DRAFT — JOBS phase (2026-09-16)

Pack date: 2026-09-16  
Phase: **JOBS** (seller-side Services paste). Not REGISTER signup. Not LinkedIn **Jobs** Easy Apply.  
Desk: LinkedIn **Services** on an **existing recovered personal profile**  
Not: feed posts, newsletters, Recruiter, Sales Navigator, Company Page, Open-to-work  
Seller: `{{DISPLAY_NAME}}` (recommended: Yuta Ishida / 石田祐太)  
Mode: **`DRAFT_ONLY`**

This folder is paste + a fail-closed Save gate. It is not a live account, not identity files, not a publish GO, and not a bidding bot.

Sibling setup copy (Wave A6 CU handoff) lives in PR [#16](https://github.com/rimone0511/autopilot-log/pull/16) `03-linkedin-services.md`. Outreach / inbound proposal replies live in PR [#38](https://github.com/rimone0511/autopilot-log/pull/38). This JOBS pack does not copy those folders. About + category order stay aligned so two agents do not ship two voices.

## Hard rules

- **Existing recovered profile only.** Same LinkedIn as MAIN Google (`{{GOOGLE_ACCOUNT_EMAIL}}`). Do not create a second LinkedIn. Do not run signup.
- **Personal profile, not Company Page.** LinkedIn help: after setup you **cannot currently change** profile vs Page ([a7436041](https://www.linkedin.com/help/linkedin/answer/a7436041)).
- **`DRAFT_ONLY`.** Official personal-profile help: **Save** makes the Service Page **viewable by members** ([a569554](https://www.linkedin.com/help/linkedin/answer/a569554)). If there is no unpublished draft control, record `no_draft_path` and **do not click Save**. See [STOP-AT-SAVE.md](STOP-AT-SAVE.md).
- **Contact for pricing.** Do not type a guessed USD/JPY. Empty required price → park `rate_required`.
- **No secrets** in git, screenshots, or session notes (no passwords, OTP digits, API keys, tax numbers, ID images).
- **No LinkedIn Jobs.** Easy Apply, job alerts, and the Open-to-work photo frame are out of this desk.
- **Stop KYC / Premium / ads.** Morning operator. Do not upload ID. Do not start a paid trial.

## Files

| File | Paste into | Role |
|---|---|---|
| [STOP-AT-SAVE.md](STOP-AT-SAVE.md) | — | Fail-closed gate. Save-if-viewable = stop |
| [CATEGORIES.md](CATEGORIES.md) | Service types picker (max 10) | Search-for order; no invented IDs |
| [ABOUT.md](ABOUT.md) | About + optional headline | 362-char About; no email/phone |
| [CTA.md](CTA.md) | Pricing + request / consult toggles | **Contact for pricing**; Premium CTA off |
| [STATUS.md](STATUS.md) | — | Pack box. Not `draft_saved` until a true draft exists |

## How far to go (then stop)

1. Confirm the recovered personal LinkedIn (MAIN Google mailbox). Desktop ≥ 1280px.
2. If captcha: checkbox / Press & Hold may be tried once per session (sibling PR [#53](https://github.com/rimone0511/autopilot-log/pull/53)). Image / tile puzzle → **stop**, human only.
3. Open the Service Page editor:
   - First time: Me → View profile → **Add profile section** → **Add services** → Continue ([a569554](https://www.linkedin.com/help/linkedin/answer/a569554)).
   - Already a member: admin view → **Edit page** ([a570566](https://www.linkedin.com/help/linkedin/answer/a570566)). Do not use Unpublish as a “draft” trick ([a1362963](https://www.linkedin.com/help/linkedin/answer/a1362963)).
4. Fill [CATEGORIES.md](CATEGORIES.md), [ABOUT.md](ABOUT.md), [CTA.md](CTA.md). Location: `{{CITY}}`, `{{COUNTRY}}` (honest Japan). Remote **On**.
5. **Stop before Save** unless a true unpublished control is visible. No Share / Notify network / Create a post.

If the page is already live from an old experiment: do not add extra categories to “finish” this pack. Log `already_member_draft` and leave.

## Placeholders (replace locally; never commit filled secrets)

```
{{DISPLAY_NAME}}
{{GOOGLE_ACCOUNT_EMAIL}}
{{CITY}}
{{COUNTRY}}
{{STARTING_HOURLY_USD}}
```

`{{STARTING_HOURLY_USD}}` stays empty in git. This pack selects **Contact for pricing** instead.

Do not put `{{GOOGLE_ACCOUNT_EMAIL}}`, phone, WhatsApp, or “email me at” in About or CTA prose.

## Counts (this pack)

| Block | This commit | Rule |
|---|---|---|
| About (fenced) | 362 characters | Third-party writeups cite ~500; **live form wins** |
| Optional headline | 33 characters | Do not auto-share |
| Categories | prefer 3–6 honest; cap 10 | Live picker only |
| Starting hourly | not filled | Contact for pricing |

## Official help (re-check at click-time)

- Marketplace: https://www.linkedin.com/services
- Offer services (personal): https://www.linkedin.com/help/linkedin/answer/a569554
- Edit Service Page: https://www.linkedin.com/help/linkedin/answer/a570566
- Unpublish (not a draft trick): https://www.linkedin.com/help/linkedin/answer/a1362963
- Profile vs Company Page: https://www.linkedin.com/help/linkedin/answer/a7436041
- Admin view: https://www.linkedin.com/help/linkedin/answer/a563489
- FAQs: https://www.linkedin.com/help/linkedin/answer/a569534

## Out of scope

- Creating or recovering a LinkedIn password from git
- LinkedIn **Jobs** / Easy Apply / Recruiter / Sales Nav
- Company Page services and Page custom CTA
- Connection blasts, InMail, inbound RFP replies (sibling Wave 2)
- Buying Premium / Business / Recruiter Lite to unlock media or Request services
- n8n / Zapier / Make partner applications
- Autopilot Log YouTube / TikTok posting-gate publish
