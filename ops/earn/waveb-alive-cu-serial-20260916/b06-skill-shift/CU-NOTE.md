> **MAIN Google mailbox only.** Public JS has no Google OAuth (PR#33). Do not create Facebook for this desk.
> **DRAFT_ONLY.** 個人登録 → プロフィール下書き. 応募しない.
> **STOP-KYC.** 本人確認サービス資料は上げない。Shared: [STOP-KYC.md](../STOP-KYC.md).
> **No secrets. No invented fees. No signup from this PR.**

# CU-NOTE — B06 Skill Shift

Play **4 / 6** in [ORDER.md](../ORDER.md) (after Offers). Host is **`www.skill-shift.com`**.

| キー | 値 |
|---|---|
| this_folder | B06 |
| QUEUE | **B16** (not QUEUE B6 MENTA) |
| cu_serial | **CU-27** |
| activity_gate | **pass** (PR#12). This GET: `/api/jobs` `created_at` **2026-09-14…11** |
| Google | **NOT_OFFERED_OAUTH** this HTML |
| official | https://www.skill-shift.com/ |
| signup | https://www.skill-shift.com/sign-up |
| terms | https://www.skill-shift.com/terms-of-service |
| jobs_api | https://www.skill-shift.com/api/jobs （件数は書かない） |
| CU hint | `pack_ready` + `pending` |

Do not use `https://skillshift.jp/` (this GET: host not found). Do not open `skillshift.global`.

## Pointers (do not copy paste bodies)

- Thick: [PR#33 `01-skill-shift.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-skillshift-sokudan-menta-deep-0734/earn-skillshift-sokudan-menta-deep-20260916/01-skill-shift.md)
- Gate: [PR#12 `records/08-skill-shift.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-activity-gate-waveb-jp-fced/earn-activity-gate-waveB-20260916/records/08-skill-shift.md)

## CU steps

1. `/sign-up` — **個人**. 企業会員・資料請求は閉じる.
2. メール = `{{EMAIL}}`. If a Google button is **visible**, then and only then PREFER_GOOGLE (and note it). Else stay mailbox.
3. Thick pack field map. 仮登録メール = parent Gmail MCP. **Save profile draft.** 応募しない.
4. 本人確認サービス = STOP.
5. Next: **B07 ITプロパートナーズ**.

現場のみ / 常駐のみの行は見ても応募しない. 机全体は SKIP しない.

## This GET (2026-09-16, no login)

- `/` and `/sign-up` 200 SPA shells. sign-up meta:「Skill Shiftの個人登録ページです。」
- `/api/jobs` 200 — `is_recruiting: true`. `created_at` 2026-09-14, 09-13, 09-12, 09-11. Position example「AI活用で業務効率化！業務棚卸しから始めるAIアドバイザー」(`side_job_style`: オンライン想定). Another: オンライン中心 / リモート中心（現地訪問相談あり）
- `skillshift.jp` DNS fail

**pagination / meta totals not written.** Fee % unstated this GET.

## Skip this desk if

KYC, paid wall, OTP missing, only 現場 rows and operator marks thin (human). Then next desk.
