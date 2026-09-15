> **MAIN Google mailbox only.** Public signup HTML has no Google OAuth (GTM / Analytics / Fonts only). Do not create Facebook for this desk.
> **DRAFT_ONLY.** 個人登録 → プロフィール下書き. 応募しない. 公開しない.
> **STOP-KYC.** 本人確認サービス資料は上げない.
> **No secrets. No invented fees. No signup from this PR.**

# CU-NOTE — B06 Skill Shift

Short note. Thick paste lives in PR#33 — **do not copy the bio here.** Shared box: [STATUS.md](../STATUS.md).

| キー | 値 |
|---|---|
| this_folder | B06 |
| QUEUE | **B16** (not QUEUE B6 MENTA) |
| cu_serial | **CU-27** |
| activity_gate | **pass** (PR#12). This GET: `/api/jobs` `created_at` **2026-09-14…11** |
| Google | **NOT_OFFERED_OAUTH** this HTML |
| official | https://www.skill-shift.com/ |
| signup | https://www.skill-shift.com/sign-up |
| login | https://www.skill-shift.com/login |
| terms | https://www.skill-shift.com/terms-of-service |
| jobs_api | https://www.skill-shift.com/api/jobs （件数は書かない） |
| CU hint | `pack_ready` + `pending` |

Do not use `https://skillshift.jp/` (this GET: host not found). Do not open `skillshift.global`.

## Google path

1. Open https://www.skill-shift.com/sign-up — **個人**. 企業会員・資料請求は閉じる.
2. **メールアドレスで登録**（公開 JS in PR#33). メール = `{{EMAIL}}` (MAIN mailbox).
3. If a **Google** signup button is **visible** on the live form, then and only then PREFER_GOOGLE and note it. Else stay mailbox.
4. Facebook「で登録する」= skip. New SNS identity = skip.
5. Picker **Use another account** = STOP. OAuth Gmail-read-all / Drive / Contacts = `oauth_overreach` → deny.
6. Already a member on this mailbox: login. Do not open a second account.
7. 仮登録メール = parent Gmail MCP. CU does **not** open `mail.google.com`. SMS = user chat.

## CU steps (only if human GO)

Default: **do not play** (Wave B register serial is cut — PR#72). Prefer JOBS unless a human types GO for **this** desk.

1. `/sign-up` — 個人.
2. Google path above.
3. Thick pack field map (PR#33). **Save profile draft.** 応募しない.
4. 本人確認サービス = STOP.
5. Park. Do not chain into SOKUDAN / Offers from this two-desk folder unless that human GO says so.

現場のみ / 常駐のみの行は見ても応募しない. 机全体は SKIP しない.

Timebox: 15–25 min. Stuck > 10 min on one modal → park.

## Stop rules (this desk)

| Trigger | Do |
|---|---|
| 本人確認サービス / 審査書類 / 免許 / マイナンバー / 顔 / 口座 | Close upload. `kyc_wait`. Morning user |
| 規約の代理登録 | CU は本人同席前提. This authoring pass does not register |
| 応募 / 提案 / スカウト承諾 | Never |
| 企業会員・お問い合わせ資料請求 | Close. Wrong role |
| 有料壁 / 前払い | `blocked_paid_plan`. Do not invent yen or % |
| Fee % required on a form and official page has no number | `rate_empty`. Park |
| OTP missing | `otp_missing` / `sms_wait_user` |
| `skillshift.jp` or `skillshift.global` | Wrong host. Leave |
| Publish / 公開トグル | Off. Draft only |

## Pointers (do not copy paste bodies)

- Thick: [PR#33 `01-skill-shift.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-skillshift-sokudan-menta-deep-0734/earn-skillshift-sokudan-menta-deep-20260916/01-skill-shift.md)
- Gate: [PR#12 `records/08-skill-shift.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-activity-gate-waveb-jp-fced/earn-activity-gate-waveB-20260916/records/08-skill-shift.md)
- Serial sibling: [PR#72 `b06-skill-shift/CU-NOTE.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/waveb-alive-cu-serial-5788/ops/earn/waveb-alive-cu-serial-20260916/b06-skill-shift/CU-NOTE.md)
- Catalog-gap (older `needs_check` on unread signup path): [PR#19 `02-skill-shift.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-freelancer-waveb-gap-notes-40b7/earn-freelancer-waveb-gap-notes-20260916/waveb-catalog-gap/02-skill-shift.md)

## This GET (2026-09-16, no login)

- `/` and `/sign-up` 200 SPA shells. sign-up meta:「Skill Shiftの個人登録ページです。」
- `/api/jobs` 200 — `is_recruiting: true`. `created_at` 2026-09-14, 09-13, 09-12, 09-11. Position example「AI活用で業務効率化！業務棚卸しから始めるAIアドバイザー」(`side_job_style`: オンライン想定). Another: リモート中心（必要に応じて現地訪問のご相談あり）
- `skillshift.jp` DNS fail

**pagination / meta totals not written.** Fee % unstated this GET.

## Skip this desk if

KYC, paid wall, OTP missing, only 現場 rows and operator marks thin (human), or no human GO. Then stop or the other note in this folder — do not invent a third desk.
