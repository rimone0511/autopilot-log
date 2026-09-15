> **MAIN Google only.** 「Google で登録」。Facebook「推奨」は使わない。
> **DRAFT_ONLY.** プロフィール下書き。応募しない。
> **STOP-KYC.** 規約の審査書類は上げない。Shared: [STOP-KYC.md](../STOP-KYC.md).
> **No secrets. No invented fees. No signup from this PR.**

# CU-NOTE — B01 SOKUDAN

Play **2 / 6** in [ORDER.md](../ORDER.md) (after Workship, before Offers).

| キー | 値 |
|---|---|
| this_folder | B01 |
| QUEUE | B1 |
| cu_serial | **CU-13** |
| activity_gate | **pass** (PR#12). This GET: outsourcing `createdAt` **2026-09-15** |
| Google | **PREFER_GOOGLE** |
| official | https://sokudan.work/ |
| signup | https://sokudan.work/signup/pro |
| login | https://sokudan.work/login |
| terms | https://sokudan.work/pages/terms |
| CU hint | `pack_ready` + `pending` |

## Pointers (do not copy paste bodies)

- Thick: [PR#33 `02-sokudan.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-skillshift-sokudan-menta-deep-0734/earn-skillshift-sokudan-menta-deep-20260916/02-sokudan.md)
- Serial card: [PR#50 `02-sokudan.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-workship-sokudan-offers-serial-cu-19f9/earn-workship-sokudan-offers-serial-cu-20260916/02-sokudan.md)
- Gate: [PR#12 `records/01-sokudan.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-activity-gate-waveb-jp-fced/earn-activity-gate-waveB-20260916/records/01-sokudan.md)

## CU steps

1. `/signup/pro` — フリーランス・副業. 企業は閉じる.
2. `alt="Google で登録"`. Fallback: メール = `{{EMAIL}}`. GitHub only if public repos match.
3. Paste from thick pack. **Save draft.** 応募しない. スカウト返信しない.
4. 審査書類 UI = STOP.
5. Next: **B19 Offers**.

## This GET (2026-09-16, no login)

- `/signup/pro` 200 — 無料新規登録. `/users/auth/google?category=signup`
- `/` 200 — titles e.g. 「【基本リモ】名古屋大学発AIスタートアップで業務設計から実装を担うFDE募集」. JSON `createdAt` 2026-09-15
- `/pages/terms` 200 — 審査書類 / 代理人登録不可. 手数料％なし

マーケ「○% リモート」は活動証明に使わない.

## Skip this desk if

KYC docs, 発注者 path, OTP missing, hold schema missing. Then next desk.
