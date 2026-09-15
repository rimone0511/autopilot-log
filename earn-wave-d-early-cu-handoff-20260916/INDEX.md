# INDEX — Wave D-early CU handoff (KEEP six + NOTES)

Observed: 2026-09-16 (public GET. **No marketplace login. No signup.**)  
State: **`DRAFT_ONLY`**. `cu_ready` means a pack exists. It does **not** mean registered.

Activity gate: [PR#22](https://github.com/rimone0511/autopilot-log/pull/22). This folder does not re-judge dead desks.

## This folder’s paste order (KEEP only)

INDEX CU-01–CU-28 does not include these Wave C remainder / Wave D-early desks. **Do not invent CU-29+.** Production serial elsewhere remains Wave A `next`, then JP CU-11, then GLOBAL CU-19. This folder does not skip those desks; it simply does not include them.

| Play | File | Desk | QUEUE | activity | Google (this GET) | Stop |
|---|---|---|---|---|---|---|
| 1 | [01-note.md](01-note.md) | note | C4 | **alive** (top `publishAt` 2026-09-14 / 15) | **PREFER_GOOGLE** (`/login` aria-label `Googleでログイン`; `/signup` SPA) | bank / 公開 / membership launch |
| 2 | [02-braintrust.md](02-braintrust.md) | Braintrust | C8 | **alive** (jobs cards + blog 2026-09-14) | **needs_check** (app signup SPA shell) | ID-verified / Certified / Stripe-Wise |
| 3 | [03-twine.md](03-twine.md) | Twine | D3 | **alive** (direct Remote “Posted 4 days ago”) | **PREFER_GOOGLE** (signup JS `signingUpViaGoogle`) | Ari jobs; Business plan; apply |
| 4 | [04-fastwork.md](04-fastwork.md) | Fastwork | D6 | **alive** (`/en/ai-automation` n8n/make) | **needs_check** | **ID + bank at register**; face-to-face cats |
| 5 | [05-99freelas.md](05-99freelas.md) | 99freelas | gate add | **alive** (`/projects` headings) | **PREFER_GOOGLE** (JS freelancer Google OAuth URL; `/register/freelancer` CF 403) | Premium; proposals; contact-in-profile |
| 6 | [06-gulp.md](06-gulp.md) | Gulp | gate add | **alive** (project cards Start ab 2026-09 / 11) | **NOT_OFFERED_OAUTH** → MAIN mailbox | Membership paid; onsite CH apply |

## NOTES only (not a CU play)

Do not paste a profile. Do not open a signup form from this serial. A human re-reads **one** public listing date before anyone writes a full pack.

| File | Desk | Gate | Why NOTES |
|---|---|---|---|
| [NOTES-shufti.md](NOTES-shufti.md) | Shufti | **needs_check** | `/jobs/search` SPA empty. Help is alive (手数料一覧, 2026シルバーウィーク). Sibling INDEX may list CU-18 — still no register from here. |
| [NOTES-kaikoku.md](NOTES-kaikoku.md) | カイコク | **needs_check** | LP + 会員登録前. Case studies have **no public dates**. Fee % unread. |

## SKIP (do not CU)

See [SKIP.md](SKIP.md). Twago → talent-pool.com (no public freelance board). Xing `/projects` **404**.

## Shared placeholders

Real values stay on the operator’s local ledger. Not in this repository.

- `{{FULL_LEGAL_NAME}}` / `{{LEGAL_NAME_KANJI}}` legal name
- `{{DISPLAY_NAME}}` public screen name
- `{{GOOGLE_ACCOUNT_EMAIL}}` / `{{EMAIL}}` MAIN Google mailbox
- `{{PASSWORD_DO_NOT_STORE}}` email-path only
- `{{COUNTRY}}` / `{{CITY}}` / `{{PREFECTURE}}` / `{{TIMEZONE}}` honest
- `{{PHONE_E164}}` SMS OTP only
- `{{PROFILE_PHOTO_LOCAL_PATH}}` operator face; not ID
- `{{PORTFOLIO_URL}}` / `{{WEBSITE_URL}}` recommended public: `https://yutalab.dev/`
- `{{GITHUB_URL}}` `https://github.com/rimone0511`
- `{{GITHUB_REPO_AUTOPILOT}}` `https://github.com/rimone0511/autopilot-log`
- `{{HOURLY_RATE_USD}}` / `{{HOURLY_RATE_EUR}}` / `{{STARTING_BUDGET_USD}}` / `{{NOTE_PAID_PRICE_JPY}}` empty in git

## This PR does not

- Create marketplace accounts
- Complete KYC or connect banks
- Subscribe to paid plans
- Publish, bid, or apply
- Commit secrets or real phone/email/password
- Invent traffic counts, GMV, or fee % missing from public HTML
- Promote Shufti / カイコク from `needs_check` to pass
