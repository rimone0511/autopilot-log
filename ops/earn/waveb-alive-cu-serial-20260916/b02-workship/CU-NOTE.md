> **MAIN Google only.** SNS **Google**. No Facebook / Apple / LINE as a new identity.
> **DRAFT_ONLY.** Profile save only. No エントリー / スカウト返信 / 成約報告.
> **STOP-KYC.** 前払い本人確認・契約署名・口座は上げない。Shared: [STOP-KYC.md](../STOP-KYC.md).
> **No secrets. No invented fees. No signup from this PR.**

# CU-NOTE — B02 Workship（ワークシップ）

Play **1 / 6** in [ORDER.md](../ORDER.md). **Not** Workshift.

| キー | 値 |
|---|---|
| this_folder | B02 |
| QUEUE | B2 |
| cu_serial | **CU-11** |
| activity_gate | **pass** (PR#12 `/portal/search`) |
| Google | **PREFER_GOOGLE** (icon label at click-time) |
| official | https://goworkship.com/ |
| signup | https://goworkship.com/signup |
| search | https://goworkship.com/portal/search |
| help_signup | https://goworkship.com/help/how_to/44 |
| prepaid_kyc | https://goworkship.com/help/agreement/95 |
| CU hint | `pack_ready` + `pending` |

## Pointers (do not copy paste bodies)

- Thick: [PR#30 `01-workship.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-waveb-cu-handoff-batch2-87d0/earn-waveb-cu-handoff-batch2-20260916/01-workship.md)
- Serial play: [PR#50 `01-workship.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-workship-sokudan-offers-serial-cu-19f9/earn-workship-sokudan-offers-serial-cu-20260916/01-workship.md)
- Gate: [PR#12 `records/02-workship.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-activity-gate-waveb-jp-fced/earn-activity-gate-waveB-20260916/records/02-workship.md)

## CU steps

1. `/signup`. Close `enterprise.goworkship.com`.
2. 「SNSで登録」→ **Google** only if the icon **says Google**. Else email = `{{EMAIL}}`.
3. Paste from thick pack. **Save draft.** エントリー 0.
4. 前払い / 署名 / 口座 = STOP.
5. Next: **B01 SOKUDAN**.

## This GET (2026-09-16, no login)

- `/signup` 200 — title「フリーランス登録をする」. 「SNSで登録」. FirebaseUI. JS: `firebase.auth.GoogleAuthProvider.PROVIDER_ID`
- `/portal/search` 200 — headings e.g. 「LLM活用｜業務効率化・設計レビュー・テスト品質改善エンジニア募集」「【基本リモ/週20h～相談可】財務BI導入…」. **No `2026-09-*` card date in this HTML**
- help/agreement/95 200 — 「前払いオプションを利用するには、本人確認が必要です」

Page listing counts are display chrome, not GMV. Do not cite them as traffic.

## Skip this desk if

Google icon missing **and** email OTP missing; KYC; enterprise-only dead-end. Then next desk.
