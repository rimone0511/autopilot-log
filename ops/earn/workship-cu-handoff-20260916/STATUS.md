# STATUS — Workship (B02) CU handoff

Snapshot: **2026-09-16** (folder stamp)  
Folder: `ops/earn/workship-cu-handoff-20260916/`  
State: **DRAFT_ONLY**

This file is the desk box for **B02 / QUEUE B2 / CU-11 Workship（ワークシップ）**. It is not a signup log and **does not claim an account exists**.

Authoring session: public Workship HTML + Help Center only. **No login. No 登録する. No credentials invented or stored.**

---

## Desk hint

| Field | Value |
|---|---|
| Desk | Workship freelance worker（ワークシップ） |
| IDs | **B02** · QUEUE **B2** · **CU-11** |
| Not | Workshift (`workshift-sol.com`, B09) |
| CU hint | `pending` — pack ready; live CU has **not** run this folder |
| Activity gate | **pass** ([PR#12](https://github.com/rimone0511/autopilot-log/pull/12) `/portal/search`) |
| Google | MAIN only (`SNSで登録` on public `/signup`; icon label at click-time) |
| Plan | Free only ([help/41](https://goworkship.com/help/about_workship/41)) |
| Stop | **気になる / エントリー** + KYC/bank — [STOP.md](STOP.md) |
| Runner | [PLAYBOOK.md](PLAYBOOK.md) · [FIELD-MAP.md](FIELD-MAP.md) |
| Morning context | Sibling [PR#72](https://github.com/rimone0511/autopilot-log/pull/72) **REGISTER-CU-CUT** (jobs-first). This folder is still the Workship runner **when** this desk is opened |

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

## Live CU outcome (empty until a human/CU runs the playbook)

Do not pre-fill success. Valid later values match PLAYBOOK:

```
desk: Workship
pack: ops/earn/workship-cu-handoff-20260916/
ids: B02 / QUEUE-B2 / CU-11
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
next: stop
```

Current: **not run**.

---

## This PR does not

- Create or log into a Workship account
- Invent or commit Google / email / password / OTP / phone / bank / My Number
- Press **気になる！** or **エントリー**
- Reply to スカウト or 成約報告
- Open 契約管理 署名 / 前払い本人確認 / 振込先口座
- Buy anything or invent worker 手数料％
- Mix Workship with Workshift
- Merge sibling pack folders
- Change Python posting-gate tests
