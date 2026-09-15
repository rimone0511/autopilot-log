> **MAIN Google mailbox only.** This GET: mail / Facebook / LinkedIn / GitHub — **no** `/google/login`. Do not create Facebook for this desk.
> **DRAFT_ONLY.** フリーランス登録 → プロフィール下書き. 応募しない. 公開しない.
> **STOP-KYC.** 本人確認 Yes / パスポート画面は上げない.
> **No secrets. No invented fees. No signup from this PR.**
> **Workshift ≠ Workship.** Do not paste Workship bios here.

# CU-NOTE — B09 Workshift（ワークシフト）

Short note. **No thick JA bio pack** — live form + placeholders only. **Do not invent a bio.** Shared box: [STATUS.md](../STATUS.md).

QUEUE: **not listed**. INDEX CU: **none — do not invent CU-29**.

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

Not DMM 生成AI人材バンク. Not Workship `goworkship.com`. Not QUEUE B9 PeoplePerHour.

## Google path

1. Confirm the tab is **Workshift** (`workshift-sol.com`), not Workship (`goworkship.com`).
2. 人材 / フリーランス. Client 依頼は閉じる.
3. https://workshift-sol.com/registration/mail_start — メール = `{{EMAIL}}` (MAIN mailbox).
4. Skip new Facebook / LinkedIn / GitHub unless that identity **already is** MAIN (still prefer email).
5. If a Google control / `/google/login` is **visible** live, then and only then PREFER_GOOGLE and note it. This GET: not offered.
6. Picker **Use another account** = STOP. OAuth overreach = deny.
7. Mail OTP = parent Gmail MCP. CU does **not** open `mail.google.com`. SMS = user chat.

## CU steps (only if human GO)

Default: **do not play** (Wave B register serial is cut — PR#72). Prefer JOBS unless a human types GO for **this** desk.

1. Confirm Workshift, not Workship.
2. Worker / フリーランス. Not 依頼.
3. `/registration/mail_start` — Google path above.
4. Profile draft if a save exists. **0 応募.** Do not invent a bio; live labels win.
5. 現地カード (展示会通訳・現地営業) = look, don't apply.
6. Park. End of this two-desk folder unless the GO names Skill Shift next.

Timebox: 15–25 min. Stuck > 10 min on one modal → park.

## Stop rules (this desk)

| Trigger | Do |
|---|---|
| 本人確認 Yes / パスポート / 顔 / 住所証明 / 口座 | Close upload. `kyc_wait`. Morning user |
| 現地ブース・展示会現地カードへの応募 | Do not apply that row |
| 新規 Facebook / LinkedIn / GitHub を身分にする | Skip. Mailbox = MAIN |
| 有料会員 / ウォレット最低残高必須 | `blocked_paid_plan`. Do not invent yen |
| 応募 / エントリー | Never |
| `/jobs/search` CAPTCHA blocks listing | Do not solve as a signup path. Search is not required to save a draft |
| Company site `workshift-sol.co.jp` as signup | Wrong. Use `workshift-sol.com` |
| Workship pack / `goworkship.com` | Wrong desk. Leave |
| Fee % required and official page has no number | `rate_empty`. Park |
| OTP missing | `otp_missing` / `sms_wait_user` |
| Publish | No. Draft only |

## Pointers (do not copy paste bodies)

- Gate record: [PR#13 `records/08-workshift.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-activity-gate-waved-b552/earn-activity-gate-waveD-20260916/records/08-workshift.md)
- Catalog-gap (older `needs_check` on unread listing HTML): [PR#19 `04-workshift.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-freelancer-waveb-gap-notes-40b7/earn-freelancer-waveb-gap-notes-20260916/waveb-catalog-gap/04-workshift.md)
- Serial sibling: [PR#72 `b09-workshift/CU-NOTE.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/waveb-alive-cu-serial-5788/ops/earn/waveb-alive-cu-serial-20260916/b09-workshift/CU-NOTE.md)
- No thick JA bio pack. Live form + placeholders. **Do not invent a bio.**

## This GET (2026-09-16, no login)

- `/` 200 — title「クラウドソーシングで海外進出支援「ワークシフト」Workshift」. Links `/jobs/view/13758`, `13757`, `13756`
- `/jobs/view/13758` 200 — SIAL Paris 現地日英通訳 (10/17–10/21). 仕事掲載日 **2026-09-11**. 「本人確認: 無し」on **this** card. **Do not apply** (現地)
- `/jobs/search` 200 — CAPTCHA present. Listing dates unread here
- `/registration/mail_start` 200 — `facebook/login`, `linkedin/login`, `github/login`, mail_start. No `/google/login`
- `/pages/term` 200 — **2026年4月11日改定**

Fee % unstated this GET → 作らない. Company-page headcount is marketing, not activity.

## Skip this desk if

Google-only policy cannot be met and email OTP missing; KYC Yes; paid wallet wall; operator decides JP-remote fit is thin (human); or no human GO. Then stop or the Skill Shift note — do not open Workship from here.
