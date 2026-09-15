# CU handoff — Upwork + LinkedIn Services (DRAFT_ONLY)

Pack date: 2026-09-16  
Public-page check date: 2026-09-15  
Seller: Yuta Ishida / 石田祐太 (n8n, AI automation, operator docs)  
Operator: Japanese; English listing copy  
Audience: a **computer-use (CU)** agent filling official UI, plus a human who pastes by hand  
Mode: **`DRAFT_ONLY`**

These files are paste + stop rules. They are not live accounts, not identity files, not a publish GO, and not a bidding bot.

Queue: Wave A **A5 Upwork** then **A6 LinkedIn Services** in `earn-register-expand-20260916/QUEUE.md` (`next`, MAIN Google, KYC → morning stop).

Thick serial (other desks): sibling `earn-cu-runbook-20260916/RUNBOOK.md`. This folder is the missing paste packs for A5 + A6 only.

## Hard rules

- **Google MAIN only.** Login identity is `{{GOOGLE_ACCOUNT_EMAIL}}` (operator MAIN: `rimone0511@gmail.com`). Do not create a second Google, Upwork, or LinkedIn.
- **Stop KYC.** No government ID, liveness, address proof, tax scans, bank, ads wallet, or paid identity badges. See [STOP-KYC.md](STOP-KYC.md).
- **No auto-bid.** No job-search loop, no proposal queue, no “apply to everything,” no scraper, no bot.
- **No Connects spray.** Do not buy Connects. Do not send proposals. Spend = **0**.
- **`DRAFT_ONLY`.** Save unpublished where the UI allows. Do not Publish / 公開する / Submit for review / Share to feed.
- **No secrets** in git, screenshots, or session logs (no passwords, OTP digits, API keys, tax numbers, ID images).
- **No invented rates as facts.** Prices stay `{{PLACEHOLDER}}`. If a field requires a number and the placeholder is empty, **park** (`rate_required`). Do not type a guessed USD/JPY/EUR.

## Files

| File | Desk | Role |
|---|---|---|
| [CU-PLAY.md](CU-PLAY.md) | A5 → A6 | Computer-use loop, OTP, Press & Hold, prompt stub |
| [01-upwork-profile.md](01-upwork-profile.md) | Upwork | Freelancer profile paste (title, overview, skills). Not a proposal. |
| [02-upwork-catalog.md](02-upwork-catalog.md) | Upwork | Project Catalog **unpublished** 3-tier paste |
| [03-linkedin-services.md](03-linkedin-services.md) | LinkedIn Services | Service Page **draft**; not Jobs; not feed |
| [STOP-KYC.md](STOP-KYC.md) | both | Identity / payout / publish stop list |
| [SESSION-LOG.md](SESSION-LOG.md) | both | Secret-free log template (do not commit filled OTP) |

## Sibling packs (do not duplicate work)

| Pack | What it is | This folder vs sibling |
|---|---|---|
| `earn-upwork-catalog-draft-20260916/` | Full Catalog paste + 800-word overview | Catalog **submit** text here matches that pack. Profile + CU play live **here**. |
| `earn-en-proposal-drafts-20260916/` | HANDS cover letters | **Do not send.** Out of this CU loop. |
| `earn-kyc-morning-checklist-20260916/` | Morning human KYC | Agent does not upload. |
| `earn-cu-runbook-20260916/RUNBOOK.md` | Full Wave A serial | This folder is A5+A6 paste only. |

## Shared placeholders

Replace locally. Never commit filled secrets.

```
{{FULL_LEGAL_NAME}}
{{DISPLAY_NAME}}
{{GOOGLE_ACCOUNT_EMAIL}}
{{EMAIL}}
{{PASSWORD_DO_NOT_STORE}}
{{COUNTRY}}
{{CITY}}
{{TIMEZONE}}
{{PHONE_E164}}
{{PROFILE_PHOTO_LOCAL_PATH}}
{{PORTFOLIO_URL}}
{{WEBSITE_URL}}
{{GITHUB_URL}}
{{GITHUB_REPO_AUTOPILOT}}
{{HOURLY_USD}}
{{TIER_STARTER_USD}}
{{TIER_STANDARD_USD}}
{{TIER_ADVANCED_USD}}
{{ADDON_REVISION_USD}}
{{ADDON_EXTRA_WORKFLOW_USD}}
{{ADDON_MIGRATION_PLAN_USD}}
{{STARTING_HOURLY_USD}}
```

Recommended **public** URLs (already public; still do not paste them as “message me off platform”):

- `{{WEBSITE_URL}}` → `https://yutalab.dev/`
- `{{GITHUB_URL}}` → `https://github.com/rimone0511`
- `{{GITHUB_REPO_AUTOPILOT}}` → `https://github.com/rimone0511/autopilot-log`

`{{GOOGLE_ACCOUNT_EMAIL}}` / `{{EMAIL}}` for login = MAIN mailbox. Do not put that address in Upwork Catalog boxes or LinkedIn Service About as a contact method.

## Counts (this pack)

| Block | Target | Rule |
|---|---|---|
| Upwork profile title | ≤ 70 characters | Upwork help (title/overview) |
| Upwork Catalog title (after “You will get”) | ≤ 75 characters | Catalog help |
| Catalog project summary | 800 characters | 121–1,200 Catalog box |
| LinkedIn Service About | confirm live | Third-party writeups cite ~500; **live form wins** |
| Catalog tiers | 3 | Starter / Standard / Advanced |
| Connects spent | 0 | Hard rule |

## Out of scope

- Live marketplace registration from **this git PR** (the CU agent may run later; this commit is markdown only)
- Buying LinkedIn Premium, Sales Nav, Recruiter, Upwork Freelancer Plus, identity badge
- Agency / Company Page (LinkedIn Company Services is a **locked** choice — do not pick it)
- LinkedIn **Jobs** Easy Apply (SKIP aggregators; not this desk)
- n8n / Zapier / Make partner applications (Wave C `late`)
- Autopilot Log posting-gate / YouTube / TikTok publish
