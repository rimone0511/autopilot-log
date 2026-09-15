> **MAIN Google only.** `data-testid="auth-google"` / `/oauth/worker_signup/google`. Do not create X / LinkedIn for this desk.
> **DRAFT_ONLY.** ワーカープロフィール下書き. 求人に応募しない.
> **STOP-KYC.** 面談・出金の本人確認は上げない。Shared: [STOP-KYC.md](../STOP-KYC.md).
> **No secrets. No invented fees. No signup from this PR.**

# CU-NOTE — B19 Offers

Play **3 / 6** in [ORDER.md](../ORDER.md) (after SOKUDAN, before Skill Shift).

| キー | 値 |
|---|---|
| this_folder | B19 |
| QUEUE | **B14** (not PR#59 local B14 = PPH) |
| cu_serial | **CU-25** |
| activity_gate | **pass** (PR#12 Jobs 業務委託). This GET: 更新日 **2026-09-10** |
| Google | **PREFER_GOOGLE** |
| official | https://offers.jp/ |
| worker_signup | https://offers.jp/worker/signup |
| jobs_side | https://offers.jp/jobs/engineer/side-job |
| terms | https://offers.jp/terms |
| CU hint | `pack_ready` + `pending` |

`https://offers.jp/signup` is **404** (this GET). Do not use `/client/`.

## Pointers (do not copy paste bodies)

- Thick: [PR#30 `04-offers.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-waveb-cu-handoff-batch2-87d0/earn-waveb-cu-handoff-batch2-20260916/04-offers.md)
- Serial card: [PR#50 `03-offers.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-workship-sokudan-offers-serial-cu-19f9/earn-workship-sokudan-offers-serial-cu-20260916/03-offers.md)
- Gate: [PR#12 `records/12-offers.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-activity-gate-waveb-jp-fced/earn-activity-gate-waveB-20260916/records/12-offers.md)

## CU steps

1. `/worker/signup` — ワーカー. 企業閉じる.
2. Google control (`auth-google`). Fallback: 「メールアドレスで登録する」= `{{EMAIL}}`. GitHub optional if public repos match.
3. Thick pack bio. 業務委託意欲 = nearest live value. Do not inflate 転職意欲.
4. Jobs = look, **don't press 応募**.
5. Next: **B06 Skill Shift**.

## This GET (2026-09-16, no login)

- `/worker/signup` 200 — `data-testid="auth-google"` `data-ovf-value="google"` `/oauth/worker_signup/google`. Visible heading「メールアドレスで登録する」. Google **word label not in this HTML** (SVG icon) — confirm at click-time
- `/jobs/engineer/side-job` 200 — 「【フルリモート】AI×FDE｜事業課題を解くフルスタックエンジニア募集」更新日文字列 **2026-09-10** (also 2026-09-08 / 09-07)
- `/terms` 200 — マッチング成功報酬はクライアント側の語. ユーザー％ unstated
- `/signup` **404**

LP「○人」is marketing. Not traffic.

## Skip this desk if

応募 wall required to save; KYC; 有料ブース required; OTP missing. Then next desk (Skill Shift).
