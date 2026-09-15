> **MAIN Google mailbox only.** Register HTML has no Google signup control (GTM ≠ OAuth).
> **DRAFT_ONLY.** 職種選択〜プロフィール入力. 応募しない. 面談に出ない.
> **STOP-KYC.** 面談・契約の身分証は上げない。Shared: [STOP-KYC.md](../STOP-KYC.md).
> **No secrets. No invented fees. No signup from this PR.**

# CU-NOTE — B07 ITプロパートナーズ

Play **5 / 6** in [ORDER.md](../ORDER.md) (after Skill Shift). Agent desk: CU stops before 面談.

| キー | 値 |
|---|---|
| this_folder | B07 |
| QUEUE | **B17** (not QUEUE B7 ストアカ) |
| cu_serial | **CU-28** |
| activity_gate | **pass** (PR#12). This GET: 最終更新日 **2026/09/08** |
| Google | **NOT_OFFERED_OAUTH** |
| self_serve | **partial** (web register open; then agent) |
| official | https://itpropartners.com/ |
| signup | https://itpropartners.com/register |
| jobs_example | https://itpropartners.com/job/sale-4 |
| flow | https://itpropartners.com/blog/flow-itpropartners/ |
| CU hint | `pack_ready` + `pending` |

Do not use `/signup` as the register entry (sibling: cases shell).

## Pointers (do not copy paste bodies)

- Thick: [PR#30 `03-itpropartners.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-waveb-cu-handoff-batch2-87d0/earn-waveb-cu-handoff-batch2-20260916/03-itpropartners.md)
- Gate: [PR#12 `records/10-itpropartners.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-activity-gate-waveb-jp-fced/earn-activity-gate-waveB-20260916/records/10-itpropartners.md)

## CU steps

1. `/register` — 職種 **エンジニア** (nearest. Do not pick AI-only if that label is absent).
2. メール = `{{EMAIL}}`. Password not stored in git.
3. Thick pack skills / bio. **Draft / input only.** CU does **not** complete 担当者面談.
4. 応募しない. 月額バンド on cards → do not copy into 希望単価.
5. Next: **B09 Workshift**.

## This GET (2026-09-16, no login)

- `/register` 200 — 「あなたの職種を教えてください」. エンジニア / マーケター / デザイナー. Form POST exists — **not submitted**. CSRF not recorded.
- `/job/sale-4` 200 — 最終更新日 **2026/09/08**「【プロジェクトマネジメント】コーポレートIT／社内情報システム…」; **2026/09/05**「【営業】M&A事業部立ち上げにおけるアポ獲得…」
- `/blog/flow-itpropartners/` 200 — 利用の流れ (登録無料 copy in sibling; 契約は本人)

仲介マージン％: official HTML **needs_check**. Do not paste third-party 10–25%.

## Skip this desk if

面談 ID / NDA / 身分証; phone required and user away; OTP missing. Then next desk.
