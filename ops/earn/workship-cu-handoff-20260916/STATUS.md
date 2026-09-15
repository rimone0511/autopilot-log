# STATUS — Workship (B02) CU handoff

> ## REGISTER-CU-CUT
>
> **2026-09-16.** Workship register CU is **not next live CU**.
> Prefer **JOBS phase** (`register-winddown` / jobs-first).
> **Do not** treat this folder as the step after Freelancer.com (A10 / CU-10).
> **Do not autoplay.** No OAuth, no 登録する, no 気になる, no エントリー from this pack unless a later **human GO** names this desk.
> Hint: **`register_cu_cut`**. Pack stays **DRAFT_ONLY** archive + runner text. Not a signup GO.

Snapshot: **2026-09-16** (folder stamp)  
Folder: `ops/earn/workship-cu-handoff-20260916/`  
State: **DRAFT_ONLY** / **REGISTER-CU-CUT** (not next CU)  
CU hint: **`register_cu_cut`** (`pack_ready` files exist; **do not play**)

This file is the desk box for **B02 / QUEUE B2 / CU-11 Workship（ワークシップ）**. It is not a signup log and **does not claim an account exists**. **Cut overrides play.**

Authoring session: public Workship HTML + Help Center only. **No login. No 登録する. No credentials invented or stored. No autoplay.**

---

## Desk hint

| Field | Value |
|---|---|
| Desk | Workship freelance worker（ワークシップ） |
| IDs | **B02** · QUEUE **B2** · **CU-11** |
| Not | Workshift (`workshift-sol.com`, B09) |
| CU hint | **`register_cu_cut`** — pack files exist; **not** a play GO. Live CU has **not** run this folder |
| Activity gate | **pass** ([PR#12](https://github.com/rimone0511/autopilot-log/pull/12) `/portal/search`) |
| Google | MAIN only (`SNSで登録` on public `/signup`; icon label at click-time) |
| Plan | Free only ([help/41](https://goworkship.com/help/about_workship/41)) |
| Stop | **気になる / エントリー** + KYC/bank — [STOP.md](STOP.md) |
| Runner | [PLAYBOOK.md](PLAYBOOK.md) · [FIELD-MAP.md](FIELD-MAP.md) |
| Morning context | **REGISTER-CU-CUT / jobs-first.** Same cut as [PR#72](https://github.com/rimone0511/autopilot-log/pull/72). Do **not** chain Freelancer → Workship. JOBS: [PR#76](https://github.com/rimone0511/autopilot-log/pull/76) week plan, [PR#88](https://github.com/rimone0511/autopilot-log/pull/88) apply queue, [PR#68](https://github.com/rimone0511/autopilot-log/pull/68) Freelancer bids (do-not-send). Human GO only if this desk is re-opened |

Sibling paste (bodies not merged here except 自己紹介 fences already in FIELD-MAP):

| Pack | PR |
|---|---|
| Thick CU-11 | [#30](https://github.com/rimone0511/autopilot-log/pull/30) |
| Thin Week2 | [#3](https://github.com/rimone0511/autopilot-log/pull/3) |
| Gate record | [#12](https://github.com/rimone0511/autopilot-log/pull/12) |
| Serial pointer | [#50](https://github.com/rimone0511/autopilot-log/pull/50) |
| Alive CU-NOTE B02 | [#72](https://github.com/rimone0511/autopilot-log/pull/72) |

---

## Public livecheck (authoring, 2026-09-16, no login, no POST)

| URL | HTTP | Result used |
|---|---|---|
| https://goworkship.com/signup | 200 | Title **フリーランス登録をする**. **SNSで登録**. `#firebaseui-auth-container`. JS `firebase.auth.GoogleAuthProvider.PROVIDER_ID`. Headless render: FirebaseUI **Google G** button. Email **メールアドレス 必須** / **パスワード 必須** (8–20) / **招待コード** / **登録する** / reCAPTCHA. Static HTML still has no “Google” string on icons |
| https://goworkship.com/login | 200 | **フリーランス用ログイン**. **SNSでログイン**. **採用担当者はこちら** = close |
| https://goworkship.com/help/how_to/44 | 200 | SNSアイコン + 確認URL **24時間**. 契約管理 **署名をする** (STOP) |
| https://goworkship.com/help/how_to/72 | 200 | **気になる！ = エントリー完了** + メッセージルーム |
| https://goworkship.com/help/how_to/77 | 200 | エントリー後の流れ |
| https://goworkship.com/help/edit_profile/52 | 200 | 自己紹介 **更新する**. AI自動入力 = read before save |
| https://goworkship.com/help/edit_profile/56 | 200 | スキル: 経験年数・スキルレベル必須. DBに無いスキルは登録不可 |
| https://goworkship.com/help/edit_profile/58 | 200 | 項目ごと公開／非公開. 登録名はエントリー前イニシャル |
| https://goworkship.com/help/edit_profile/69 | 200 | 活動名 / 通称名 / 屋号 **不可**. 本名 or 旧姓 |
| https://goworkship.com/help/about_workship/41 | 200 | フリーランス登録 **無料**. 成約後サービス利用料なし（worker） |
| https://goworkship.com/help/about_workship/71 | 200 | 国内住民票 + 本人名義国内口座（資格。口座は今は開けない） |
| https://goworkship.com/help/agreement/95 | 200 | 前払い = **本人確認が必要**. 手数料％ **未記載 → 作らない** |
| https://goworkship.com/help/agreement/105 | 200 | 三者間契約. 成約報告のあと |
| https://goworkship.com/flow | 200 | STEP1–8. This pack stops after STEP2 |
| https://goworkship.com/portal/search | 200 | 案件カードあり（gate pass）. **Do not 気になる**. 件数見出しは GMV ではない |
| https://enterprise.goworkship.com/ | 200 | ENTERPRISE 採用 — **close** |

CSRF `_Token`, reCAPTCHA site keys, and Firebase API keys are **not** recorded here.

`thin_site_skip: false`.

---

## Live CU outcome (empty until a **human GO** — default is cut)

Do **not** autoplay this playbook. Do not pre-fill success. Default now:

```
desk: Workship
pack: ops/earn/workship-cu-handoff-20260916/
ids: B02 / QUEUE-B2 / CU-11
hint: register_cu_cut
auth:
otp:
kyc:
draft_profile:
entry: no
kininaru: no
scout_reply: no
publish: no
plan: free
prepaid: no
bank: no
rate:
next: jobs-first | stop
```

Current: **not run** / **`register_cu_cut`**. Prefer JOBS. Not next live CU.

---

## This PR does not

- Autoplay Workship register CU (cut; jobs-first)
- Treat this pack as next live CU after Freelancer.com
- Create or log into a Workship account
- Invent or commit Google / email / password / OTP / phone / bank / My Number
- Press **気になる！** or **エントリー**
- Reply to スカウト or 成約報告
- Open 契約管理 署名 / 前払い本人確認 / 振込先口座
- Buy anything or invent worker 手数料％
- Mix Workship with Workshift
- Merge sibling pack folders
- Change Python posting-gate tests
