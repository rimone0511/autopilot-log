> DRAFT_ONLY CU handoff. NO secrets. NO invented credentials. NO publish. NO Pro. NO KYC.
> Human / CU paste only. Live form wins.
> Desk: Contra Independent / Share work (CU-08 / QUEUE A8).
> Auth: **MAIN Google** (`Continue with Google`). Free account only.
> Stop: **before Wallet / Add account / Persona**. See [STOP-KYC.md](STOP-KYC.md).
> Fields: [FIELD-MAP.md](FIELD-MAP.md). Session box: [STATUS.md](STATUS.md).

# PLAYBOOK — Contra Independent signup (CU-08)

| Key | Value |
|---|---|
| Desk | Contra Independent / **Share work** |
| CU serial | CU-08 (QUEUE **A8**) |
| Mode | **DRAFT_ONLY** |
| Language on Independent page | **English** |
| Google | **MAIN only** — public signup shows **Continue with Google** |
| Plan | **Free**. Do not buy Contra Pro / Max |
| `thin_site_skip` | **false** (public pages live 2026-09-16) |
| Authoring session | Public GET / help only. **Did not create an account** |

Sibling paste packs (do not copy into `earn-packs/`; this folder is the CU runner):

- Thin: `earn-timeticket-contra-craudia-handoff-20260916/08-contra.md` ([PR #18](https://github.com/rimone0511/autopilot-log/pull/18))
- Deep: `earn-contra-timeticket-deep-paste-20260916/02-contra.md` ([PR #41](https://github.com/rimone0511/autopilot-log/pull/41))

This playbook is the **step order**. Paste fences below match those packs. Placeholders stay empty in git.

---

## Hard rules (read before the first click)

1. **MAIN Google.** Open [contra.com/sign-up](https://contra.com/sign-up) (or Sign up from [contra.com](https://contra.com/)). Click **Continue with Google**. Use `{{GOOGLE_ACCOUNT_EMAIL}}` — MAIN mailbox only. Do not invent a new Google account, Apple ID, or second Contra identity.
2. **Independent only.** On “What brings you to Contra?” choose **Share work**. Do not choose **Hire creative talent**. Do not create a separate Agency / Hire persona.
3. **Free only.** Official onboarding: you can sign up for Contra Pro **or proceed with a free account**. Proceed with **free**. Close Get Pro / upgrade / card walls (`card_wall`).
4. **DRAFT_ONLY.** Save profile / case study / service as draft or unpublished. Do not Publish to feed. Do not Apply. Do not invoice.
5. **STOP before wallet / Persona.** Official profile-complete Step 5 is “Verify identity & set up your wallet.” Do not open it. No how-to beyond [STOP-KYC.md](STOP-KYC.md).
6. **No credentials in git or chat paste logs.** OTP stays in parent Gmail. Do not type passwords, backup codes, bank, tax IDs, or government numbers into this repo.

Fallback if Google is missing on the live wizard: same MAIN email in the email path. OTP = parent Gmail. Still no new mailbox.

Already a member on MAIN: log in. Do not open a second account.

---

## Step order

Official Independent onboarding (help updated 2026-01-27). **Live wizard order wins** if it differs.

Timebox: 15–25 minutes. Stuck > 10 minutes: park and write [STATUS.md](STATUS.md).

### A. Create the Free Independent account

| # | Do | Do not |
|---|---|---|
| 1 | Open https://contra.com/ or https://contra.com/sign-up | Do not start from a Hire / client campaign URL |
| 2 | **Continue with Google** as MAIN `{{GOOGLE_ACCOUNT_EMAIL}}` | New SNS. Guest. Incognito second identity |
| 3 | **What brings you to Contra?** → **Share work** | **Hire creative talent**. Agency as a second person |
| 4 | Profile photo from `{{PHOTO_LOCAL_PATH}}` (local disk, not git). Skip if the wizard allows skip | Government ID, selfie-for-KYC, client private photos |
| 5 | One-liner: paste **One-liner A or B** below. Cut if the field is shorter | Contact info, rates, “DM me off Contra” |
| 6 | Create account: **proceed with a free account** | Contra Pro (`$29 / month` or yearly on [pricing](https://contra.com/pricing)). Card |
| 7 | Topics: pick **existing** chips closest to automation, APIs, documentation | Invent a topic the picker does not list |

Account exists after step 7 on the official guide. That is **not** “profile complete” and **not** Discoverable. Stop is still before wallet.

### B. Fill the profile (draft, not Discover-complete)

Official “Completing your profile” list. This GO **does not** fill the identity/wallet step.

| # | Do | Do not |
|---|---|---|
| 8 | Cover: public screenshot with no secrets, or skip | ID photo as cover |
| 9 | Work: public URLs only (`{{PORTFOLIO_URL}}`, `{{GITHUB_REPO_AUTOPILOT}}`). Case study → **Save as draft**. Import only **public** links | **Publish**. **Post to feed**. Private repos, client files |
| 10 | Rate: leave empty if the form allows. Else `{{HOURLY_USD}}` from **local ledger only**. If required and ledger empty → `rate_empty` | Invent USD. Paste the paid-projects fee table into About |
| 11 | Social: `{{PORTFOLIO_URL}}` and `{{GITHUB_URL}}`. Existing LinkedIn URL only if already public | Create a LinkedIn post. Put email/phone in social slots |
| 12 | About / bio: **200 or 400** fence. Official cap **400 characters** | 800-character About. Credentials. Off-platform pay pitch |
| 13 | Display name: `{{DISPLAY_NAME}}` (suggested fill **from local ledger**, e.g. everyday Latin name). First / Last as the form splits them | Job title as name (“SEO Expert”) |
| 14 | Location: country/region from ledger (`{{COUNTRY}}` / `{{PREFECTURE}}`). No street address | Email hello@contra.com with proof-of-residence / ID to change country |
| 15 | Discoverable / public toggle → **off** if present | Check the official “you're now discoverable” box (that box includes wallet) |

### C. Hard stop

16. **Do not** open Wallet, **Add account** / **Add an account**, Persona, Airwallex, Expert verification, W-8 / tax, bank / PayPal / USDC payout, or any government-ID upload.
17. **Do not** apply to jobs, send invoices, create paid projects, or buy Pro to “finish” Discover.
18. Record outcome in [STATUS.md](STATUS.md). Valid stop: `done-draft` or `kyc_wait`.

If the live form **blocks even a draft save** behind identity, that is `kyc_wait`. Close. Do not complete it. Morning user.

---

## Paste fences (known pack lengths)

Contact lines stay out. Do not add email, phone, or a second Google identity.

### One-liner A (63 characters — short, official-example shape)

Help: brief elevator pitch; no numeric cap published. Live field may be shorter — cut, do not wrap onto a second bio.

```
Japan-based: n8n and official-API automation plus operator docs
```

### One-liner B (68 characters — use if A fits with room)

```
Official-API automation plus operator docs a non-engineer can follow
```

### About 200 (short Description slot)

Official cap is 400. Use 200 when the live box is tight.

```
I am {{DISPLAY_NAME}} (Japan). I replace copy-paste with n8n or official-API workflows plus operator docs. Notes: {{PORTFOLIO_URL}} I do not scrape or take Contra work off-platform. Async in {{TIMEZONE}}.
```

### About 400 (official limit — Bios help)

https://help.contra.com/en/articles/9322626-bios-on-contra — “Please note that there is a 400-character limit.”

```
I am {{DISPLAY_NAME}}, a Japan-based independent. I help small teams replace copy-paste with an n8n or official-API workflow plus docs a non-engineer can follow. Public notes: {{PORTFOLIO_URL}} Tool: Autopilot Log (YouTube Data API v3 + TikTok Content Posting API, fail-closed gate). I do not scrape, fake engagement, or move Contra-originated work off Contra. Async text in {{TIMEZONE}}. Scope is first.
```

Do not place an 800-character About. After substituting placeholders, **recount**: official cap is 400. Sibling filled examples (ledger name + public notes URL + `Asia/Tokyo`) measured **200** and **400**. If the live count exceeds 400, trim the last sentence — do not invent a longer bio. `{{TIMEZONE}}` example from ledger: `Asia/Tokyo`. No street address in git.

### Work sample titles (if the form wants one line)

| Sample | URL placeholder | Title line |
|---|---|---|
| 1 | `{{PORTFOLIO_URL}}` | Operator-facing notes on AI automation (Japanese, public) |
| 2 | `{{GITHUB_REPO_AUTOPILOT}}` | Autopilot Log — YouTube Data API v3 + TikTok Content Posting API, fail-closed gate |

Do not upload private videos, client files, or ID. Do not Publish to feed.

---

## Fees (cite only — do not pay)

| Claim | Status | Source |
|---|---|---|
| Independent profile is free | **cited** | [Independents](https://contra.com/how-it-works/independents): “Your Contra profile is free and doesn’t cost you a dime!” · [Pricing](https://contra.com/pricing): “Join Contra for free” |
| Free path at signup | **cited** | [Onboarding](https://help.contra.com/en/articles/9322381-onboarding-and-completing-your-profile): “sign up for Contra Pro or proceed with a free account” |
| Pro list price (do not buy) | **cited** | Help [What is Contra Pro?](https://help.contra.com/en/articles/9322981-what-is-contra-pro) (2026-05-12): `$29 / month` or yearly `$17 / month` billed annually. Live [pricing](https://contra.com/pricing) also shows `$199 / year (save 43%)` or `$29 / month`. **Live pricing wins. Still do not buy.** |
| Commission-free for creatives | **cited** | Pricing: “Contra is always commission-free for all creatives.” Free plan still shows **client payment fees** — not a reason to upgrade this pass |
| Non-Pro project fees | **cited, unused** | [Paid projects](https://help.contra.com/en/articles/9322763-paid-projects) table (`$2` … `$29` by size). This pack does **not** create a paid project, so do not treat the table as “pay now” |
| Hourly number | **placeholder** | Onboarding “Add your rate” → `{{HOURLY_USD}}` only. Empty save, else ledger, else `rate_empty` |
| Processing fees | **cited** | Pricing footnote: third-party processing fees exist. Do not invent a % |

Do not buy Pro to waive fees or to skip wallet.

---

## Explicit do-not

- Hire workspace instead of Independent
- Get Pro / Max / card
- Wallet / Add account / Persona (no how-to — just stop)
- Discoverable on
- Publish to feed / Publish service (use **Save as unpublished** / case-study **draft**)
- Apply / invoice / payment link (EN proposal copy lives in sibling packs; do not send it here)
- Invent `{{HOURLY_USD}}` or a Google password
- Off-platform pay for Contra-originated work
- Country-change email that asks for utility bill / lease / ID ([location help](https://help.contra.com/en/articles/13465157-how-to-change-your-location-on-contra))

---

## Success before stop

| Outcome | Meaning |
|---|---|
| `done-draft` | MAIN Google. Share work. Free. One-liner + About ≤400. Public URLs. Discoverable off. No wallet. No Pro |
| `already_member_draft` | Same MAIN already had Contra. Profile checked/filled. No Pro upgrade. No second account |
| `kyc_wait` | Wallet / Persona / ID appeared. Closed. Morning user. Not a failed desk |
| `rate_empty` | Rate required and local ledger empty. Did not invent USD |
| `card_wall` | Pro demanded a card. Closed |
| `otp_missing` | Email confirm not in parent Gmail. Park |

CU return box (no secrets):

```
desk: Contra
pack: ops/earn/contra-cu-handoff-20260916/
auth: google-main | email-same-mailbox | already_member | blocked
otp: gmail-parent | none | otp_missing
kyc: none | wait-morning
draft_profile: yes/no
plan: free
pro_upgrade: no
publish: no
apply: no
rate: empty | placeholder-from-ledger | rate_empty
next: stop
```

---

## Sources (public)

- Sign up UI: https://contra.com/sign-up (`Continue with Google`)
- Independents: https://contra.com/how-it-works/independents
- Pricing: https://contra.com/pricing
- Terms: https://contra.com/policies/terms
- Onboarding: https://help.contra.com/en/articles/9322381-onboarding-and-completing-your-profile
- One-liner: https://help.contra.com/en/articles/9322675-writing-your-one-liner-on-contra
- Bios (400): https://help.contra.com/en/articles/9322626-bios-on-contra
- Name / email / About / profile URL: https://help.contra.com/en/articles/16275340-how-to-change-your-name-email-and-profile-information-on-contra
- Social links: https://help.contra.com/en/articles/11758863-how-to-update-social-links-on-your-profile
- Location: https://help.contra.com/en/articles/13465157-how-to-change-your-location-on-contra
- Case study + **save as draft**: https://help.contra.com/en/articles/9322393-how-to-build-a-case-study-from-scratch-on-contra
- Import public links: https://help.contra.com/en/articles/9322427-how-to-import-existing-work-on-contra
- Services + **Save as unpublished**: https://help.contra.com/en/articles/9322412-how-to-add-services-to-your-contra-profile
- Account type switch (do not switch this pass): https://help.contra.com/en/articles/9322386-switching-account-types-on-contra
- Wallet / identity URLs: listed only as **STOP triggers** in [STOP-KYC.md](STOP-KYC.md)
