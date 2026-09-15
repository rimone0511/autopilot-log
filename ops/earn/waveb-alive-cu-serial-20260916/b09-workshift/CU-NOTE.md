> **MAIN Google mailbox only.** This GET: mail / Facebook / LinkedIn / GitHub — **no** `/google/login`. Do not create Facebook for this desk.
> **DRAFT_ONLY.** フリーランス登録 → プロフィール下書き. 応募しない.
> **STOP-KYC.** 本人確認 Yes / パスポート画面は上げない。Shared: [STOP-KYC.md](../STOP-KYC.md).
> **No secrets. No invented fees. No signup from this PR.**
> **Workshift ≠ Workship.** Do not paste Workship bios here.

# CU-NOTE — B09 Workshift（ワークシフト）

Play **6 / 6** in [ORDER.md](../ORDER.md) (last). QUEUE: **not listed**. INDEX CU: **none — do not invent CU-29**.

| キー | 値 |
|---|---|
| this_folder | B09 |
| QUEUE | — (catalog-gap in PR#19; Wave D row in PR#13) |
| cu_serial | **none** |
| activity_gate | **pass** (PR#13). This GET: `/jobs/view/13758` date **2026-09-11** |
| Google | **NOT_OFFERED_OAUTH** this GET |
| official | https://workshift-sol.com/ |
| company | https://workshift-sol.co.jp/ （会社. 登録入口ではない） |
| signup | https://workshift-sol.com/registration/mail_start |
| search | https://workshift-sol.com/jobs/search （CAPTCHA. `/job/search` is the wrong path） |
| terms | https://workshift-sol.com/pages/term |
| CU hint | `pack_ready` + `pending` |

Not DMM 生成AI人材バンク. Not Workship `goworkship.com`.

## Pointers (do not copy paste bodies)

- Gate record: [PR#13 `records/08-workshift.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-activity-gate-waved-b552/earn-activity-gate-waveD-20260916/records/08-workshift.md)
- Catalog-gap (older `needs_check` on unread listing HTML): [PR#19 `04-workshift.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-freelancer-waveb-gap-notes-40b7/earn-freelancer-waveb-gap-notes-20260916/waveb-catalog-gap/04-workshift.md)
- No thick JA bio pack. Live form + placeholders. **Do not invent a bio.**

## CU steps

1. Confirm the tab is **Workshift** (`workshift-sol.com`), not Workship.
2. 人材 / フリーランス. Client 依頼は閉じる.
3. `/registration/mail_start` — メール = `{{EMAIL}}`. Skip new Facebook / LinkedIn / GitHub unless that identity **already is** MAIN (still prefer email).
4. Profile draft if a save exists. **0 応募.**
5. 現地カード (展示会通訳・現地営業) = look, don't apply.
6. Next: **stop** (end of this serial).

## This GET (2026-09-16, no login)

- `/` 200 — title「クラウドソーシングで海外進出支援「ワークシフト」Workshift」. Links `/jobs/view/13758`, `13757`, `13756`
- `/jobs/view/13758` 200 — SIAL Paris 現地日英通訳 (10/17–10/21). Date string **2026-09-11**. 「本人確認: 無し」on **this** card. **Do not apply** (現地)
- `/jobs/search` 200 — CAPTCHA present. Listing dates unread here
- `/registration/mail_start` 200 — `facebook/login`, `linkedin/login`, `github/login`, mail_start. No `/google/login`
- `/pages/term` 200 — **2026年4月11日改定**

Fee % unstated this GET → 作らない. Company-page headcount is marketing, not activity.

## Skip this desk if

Google-only policy cannot be met and email OTP missing; KYC Yes; paid wallet wall; operator decides JP-remote fit is thin (human). End serial.
