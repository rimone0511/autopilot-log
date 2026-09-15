# CU handoff — Wave B GLOBAL (Guru / Malt / Workana / Freelancermap / PPH)

Pack date: 2026-09-16  
Public GET: 2026-09-15 (this PR). No marketplace login from the agent that wrote these files.  
Seller: Yuta Ishida / 石田祐太 (n8n, AI automation, operator docs)  
Operator: Japanese; English profiles  
Audience: a **computer-use (CU)** agent filling official UI, plus a human who pastes by hand  
Mode: **`DRAFT_ONLY`**

These files are paste + stop rules. They are not live accounts, not identity files, not a publish GO, and not a bidding bot.

Queue: Wave B **B8–B12** in sibling `earn-register-expand-20260916/QUEUE.md` (`week-2`). INDEX CU numbers: **CU-19–CU-23**.

This folder’s **play order is not INDEX order**. PPH sits last because public Terms describe **PPH Basic as a paid annual subscription**. See [CU-PLAY.md](CU-PLAY.md).

## Hard rules

- **MAIN Google preferred.** Login identity is `{{GOOGLE_ACCOUNT_EMAIL}}` (operator MAIN: `rimone0511@gmail.com`). Do not create a second Google or a second marketplace identity. If a desk has no Google button, use the **same MAIN mailbox** as email — still not a second account.
- **Stop KYC.** No government ID, liveness, address proof, tax scans, bank, IBAN, Persona/SILT, Guru ID Verification. See [STOP-KYC.md](STOP-KYC.md).
- **No paid plan subscribe.** Especially **PeoplePerHour Basic (annual)** and PPH TopAccess. Also skip Guru paid membership, Freelancermap Premium, Malt boosts, Workana Priority Moderation, paid identity badges. If the next click is pay → **park** (`blocked_paid_plan`).
- **`DRAFT_ONLY`.** Save unpublished / hidden / inactive where the UI allows. Do not Publish / Submit for review / send proposals / apply to jobs.
- **No secrets** in git, screenshots, or session logs (no passwords, OTP digits, API keys, tax numbers, ID images).
- **No invented traffic / GMV.** Activity is `pass` / `needs_check` / `blocked_paid_plan` from public pages only. Vendor marketing totals are ignored.
- **No invented rates.** Prices stay `{{PLACEHOLDER}}`. If a field requires a number and the placeholder is empty, **park** (`rate_required`).

## Files

| File | Desk | INDEX CU | QUEUE | This-folder play |
|---|---|---|---|---|
| [CU-PLAY.md](CU-PLAY.md) | all five | — | — | Serial + OTP + Press & Hold + prompt stub |
| [01-guru.md](01-guru.md) | Guru.com | CU-19 | B8 | 1 |
| [03-malt.md](03-malt.md) | Malt.com (EU) | CU-21 | B10 | 2 |
| [04-workana.md](04-workana.md) | Workana | CU-22 | B11 | 3 |
| [05-freelancermap.md](05-freelancermap.md) | Freelancermap | CU-23 | B12 | 4 |
| [02-peopleperhour.md](02-peopleperhour.md) | PeoplePerHour | CU-20 | B9 | 5 (paywall last) |
| [STOP-KYC.md](STOP-KYC.md) | all | — | — | Identity / payout / paid-plan stop list |
| [SESSION-LOG.md](SESSION-LOG.md) | all | — | — | Secret-free log template |
| [METHOD.md](METHOD.md) | — | — | — | Public GET log (no login) |
| [INDEX.md](INDEX.md) | — | — | — | Paste order vs INDEX CU serial |

## Sibling packs (do not duplicate work)

| Pack | What it is | This folder vs sibling |
|---|---|---|
| `earn-register-packs-20260916/` ([PR#2](https://github.com/rimone0511/autopilot-log/pull/2)) | Week-2 GLOBAL register drafts for Guru / PPH / Malt / Workana | Field maps here are CU-ready. Sibling remains the Week-2 register path. **Freelancermap is first written here.** |
| `earn-register-pack-index-20260916/INDEX.md` ([PR#8](https://github.com/rimone0511/autopilot-log/pull/8)) | CU-19–CU-23 numbering | INDEX serial is QUEUE order. This folder parks PPH last. |
| `earn-cu-runbook-20260916/RUNBOOK.md` ([PR#7](https://github.com/rimone0511/autopilot-log/pull/7)) | Thick Wave A → Wave B **passes only** | This folder is GLOBAL B8–B12 paste only. |
| `earn-kyc-morning-checklist-20260916/` ([PR#4](https://github.com/rimone0511/autopilot-log/pull/4)) | Morning human KYC | Agent does not upload. |
| Wave B JP ALIVE sample ([PR#21](https://github.com/rimone0511/autopilot-log/pull/21)) | SOKUDAN / 複業クラウド / Anycrew / MENTA / ストアカ | Out of this serial. |

Wave A `next` desks stay on the thick runbook. Do not open JP Week2 from here.

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
{{HOURLY_RATE_USD}}
{{DAILY_RATE_EUR}}
{{STARTING_BUDGET_USD}}
{{ADDON_PRICE_A}}
{{ADDON_PRICE_B}}
```

Recommended **public** URLs (already public; still do not paste them as “message me off platform”):

- `{{WEBSITE_URL}}` / `{{PORTFOLIO_URL}}` → `https://yutalab.dev/`
- `{{GITHUB_URL}}` → `https://github.com/rimone0511`
- `{{GITHUB_REPO_AUTOPILOT}}` → `https://github.com/rimone0511/autopilot-log`

`{{GOOGLE_ACCOUNT_EMAIL}}` / `{{EMAIL}}` for login = MAIN mailbox. Do not put that address in public profile / Offer / Service boxes.

## Out of scope

- Marketplace login or account create **from this git PR** (markdown only; later CU may run)
- Buying PPH Basic / TopAccess, Guru paid membership, Freelancermap Premium, Malt boosts, Workana Priority Moderation
- KYC uploads, Persona / SILT / Guru ID Verification / AML docs
- Sending proposals, quotes, applications, or client messages
- Inventing job counts, GMV, or “earn X”
- Autopilot Log posting-gate / YouTube / TikTok publish
