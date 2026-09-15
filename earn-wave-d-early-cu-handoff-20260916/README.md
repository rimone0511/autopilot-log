# CU handoff — Wave D-early KEEP (note / Braintrust / Twine / Fastwork / 99freelas / Gulp)

Pack date: **2026-09-16**  
Public GET: 2026-09-16 (this PR). **No marketplace login. No signup. No OAuth completion.**  
Seller: Yuta Ishida / 石田祐太 (n8n, AI automation, operator docs)  
Operator: Japanese; English profiles on EN desks; Portuguese UI on 99freelas (do not fake PT fluency)  
Audience: a **computer-use (CU)** agent filling official UI, plus a human who pastes by hand  
Mode: **`DRAFT_ONLY`**

These files are paste + stop rules. They are not live accounts, not identity files, not a publish GO, and not a bidding bot.

Activity source: sibling [PR#22](https://github.com/rimone0511/autopilot-log/pull/22) `earn-activity-gate-wave-d-early-20260916/` (`keep_queue` / `alive` = 6). This GET re-read the same public URLs. Do not invent traffic / GMV. Vendor marketing totals are ignored.

QUEUE: parent `earn-register-expand-20260916/QUEUE.md`. note = **C4**, Braintrust = **C8** (Wave C). Twine = **D3**, Fastwork = **D6**. 99freelas / Gulp were added by the D-early gate (not original D1–D8 rows). **Do not promote any of these ahead of Wave A/B.** INDEX CU-01–CU-28 ([PR#8](https://github.com/rimone0511/autopilot-log/pull/8)) does **not** number these desks — this folder uses a **this-folder play** only. Do not invent CU-29+.

## Hard rules

- **MAIN Google preferred.** Login identity is `{{GOOGLE_ACCOUNT_EMAIL}}` (operator MAIN mailbox). Do not create a second Google or a second marketplace identity. If a desk has no Google button, use the **same MAIN mailbox** as email — still not a second account.
- **Stop KYC.** No government ID, liveness, My Number, address proof, tax scans, bank, IBAN, Stripe/Wise payout identity. See [STOP-KYC.md](STOP-KYC.md). Fastwork’s public start-selling page says signup uses **ID and bank** — that is an immediate stop.
- **No paid plan subscribe.** Skip note membership launch, Twine Business ($139.99/project), 99freelas Premium (R$ 54,90–89,90/mês), GULP Membership (120 / 180 Euro netto), Fastwork Specialist/boosts.
- **`DRAFT_ONLY`.** Save unpublished / hidden / incomplete where the UI allows. Do not Publish / 公開 / Post services / send proposals / apply.
- **No secrets** in git, screenshots, or session logs.
- **No invented traffic / GMV / fees.** Fee percentages only where an official public page stated them; otherwise `needs_check` / `unknown`.
- **No invented rates.** Prices stay `{{PLACEHOLDER}}`. If a field requires a number and the placeholder is empty, **park** (`rate_required`).

## Files

| File | Desk | QUEUE | Gate (PR#22 + this GET) | This-folder play |
|---|---|---|---|---|
| [CU-PLAY.md](CU-PLAY.md) | KEEP six | — | — | Serial + OTP + Press & Hold + prompt stub |
| [01-note.md](01-note.md) | note | C4 | **alive** | 1 |
| [02-braintrust.md](02-braintrust.md) | Braintrust | C8 | **alive** | 2 (ID / Certified → STOP) |
| [03-twine.md](03-twine.md) | Twine | D3 | **alive** | 3 (Ari SKIP) |
| [04-fastwork.md](04-fastwork.md) | Fastwork | D6 | **alive** | 4 (ID+bank at register → STOP) |
| [05-99freelas.md](05-99freelas.md) | 99freelas | gate add | **alive** | 5 |
| [06-gulp.md](06-gulp.md) | Gulp / Randstad Professional | gate add | **alive** | 6 (onsite CH cards: do not apply) |
| [NOTES-shufti.md](NOTES-shufti.md) | Shufti | D1 / CU-18 inventory | **needs_check** | **NOTES only — no full CU** |
| [NOTES-kaikoku.md](NOTES-kaikoku.md) | カイコク | not in QUEUE table | **needs_check** | **NOTES only — no full CU** |
| [SKIP.md](SKIP.md) | Twago, Xing Projects | D07 / D10 | **dead** | do not CU |
| [STOP-KYC.md](STOP-KYC.md) | all KEEP | — | — | Identity / payout / paid-plan stop list |
| [SESSION-LOG.md](SESSION-LOG.md) | KEEP six | — | — | Secret-free log template |
| [METHOD.md](METHOD.md) | — | — | — | Public GET log (no login) |
| [INDEX.md](INDEX.md) | — | — | — | Paste order vs unindexed CU |

## Sibling packs (do not duplicate work)

| Pack | What it is | This folder vs sibling |
|---|---|---|
| `earn-activity-gate-wave-d-early-20260916/` ([PR#22](https://github.com/rimone0511/autopilot-log/pull/22)) | D01–D10 activity gate | Gate is the keep/skip source. Packs here are CU paste for **alive** only. |
| `earn-register-expand-20260916/QUEUE.md` ([PR#1](https://github.com/rimone0511/autopilot-log/pull/1)) | Wave C/D table | note / Braintrust stay Wave C. Twine / Fastwork stay behind A/B. |
| `earn-register-pack-index-20260916/INDEX.md` ([PR#8](https://github.com/rimone0511/autopilot-log/pull/8)) | CU-01–CU-28 | Shufti may be CU-18 inventory there. **This folder does not run Shufti CU.** |
| `earn-kyc-morning-checklist-20260916/` ([PR#4](https://github.com/rimone0511/autopilot-log/pull/4)) | Morning human KYC | Agent does not upload. |
| Wave B GLOBAL / JP ALIVE CU ([PR#29](https://github.com/rimone0511/autopilot-log/pull/29) / [PR#21](https://github.com/rimone0511/autopilot-log/pull/21)) | Week-2 desks | Out of this serial. |

Wave A `next` and Wave B stays on those runbooks. Do not open those desks from here.

## Shared placeholders

Replace locally. Never commit filled secrets.

```
{{FULL_LEGAL_NAME}}
{{LEGAL_NAME_KANJI}}
{{DISPLAY_NAME}}
{{GOOGLE_ACCOUNT_EMAIL}}
{{EMAIL}}
{{PASSWORD_DO_NOT_STORE}}
{{COUNTRY}}
{{CITY}}
{{PREFECTURE}}
{{TIMEZONE}}
{{PHONE_E164}}
{{PROFILE_PHOTO_LOCAL_PATH}}
{{PORTFOLIO_URL}}
{{WEBSITE_URL}}
{{GITHUB_URL}}
{{GITHUB_REPO_AUTOPILOT}}
{{HOURLY_RATE_USD}}
{{HOURLY_RATE_EUR}}
{{STARTING_BUDGET_USD}}
{{NOTE_PAID_PRICE_JPY}}
```

Recommended **public** URLs (already public; still do not paste them as “message me off platform”):

- `{{WEBSITE_URL}}` / `{{PORTFOLIO_URL}}` → `https://yutalab.dev/`
- `{{GITHUB_URL}}` → `https://github.com/rimone0511`
- `{{GITHUB_REPO_AUTOPILOT}}` → `https://github.com/rimone0511/autopilot-log`

`{{GOOGLE_ACCOUNT_EMAIL}}` / `{{EMAIL}}` for login = MAIN mailbox. Do not put that address in public profile / note body / proposal boxes.

## Out of scope

- Marketplace login or account create **from this git PR** (markdown only; later CU may run)
- Full CU packs for Shufti / カイコク (`needs_check` — NOTES only)
- Twago / Xing Projects (SKIP / dead)
- Buying paid plans, KYC uploads, publishing, bidding, applying
- Inventing job counts, GMV, or “earn X”
- Autopilot Log posting-gate / YouTube / TikTok publish
