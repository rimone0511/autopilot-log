> **MAIN Google only.** `{{EMAIL}}` / `{{GOOGLE_ACCOUNT_EMAIL}}`. No second account.
> **DRAFT_ONLY.** Profile save only. No publish / 応募 / エントリー.
> **STOP-KYC.** Agents and CU **do not upload**. Morning user only.
> **No secrets.** No ID photos, My Number, bank digits, OTP, passwords, CSRF in git or chat.
> **No invented fees.** Do not pay to skip identity.
> **No publish.** Saving a draft is not KYC and is not a listing.

# STOP before KYC — Wave B alive serial (shared)

Pack: `ops/earn/waveb-alive-cu-serial-20260916/`  
Pack date: 2026-09-16  
Mode: **DRAFT_ONLY**  
Audience: 朝の本人 and later CU. One desk at a time.

Long official rows stay in sibling STOP files (bodies not copied):

- Workship / Offers / ITプロパートナーズ → [PR#30 STOP-KYC.md](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-waveb-cu-handoff-batch2-87d0/earn-waveb-cu-handoff-batch2-20260916/STOP-KYC.md)
- Skill Shift / SOKUDAN → [PR#33 STOP-KYC.md](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-skillshift-sokudan-menta-deep-0734/earn-skillshift-sokudan-menta-deep-20260916/STOP-KYC.md)
- 3-desk Google subset → [PR#50 STOP-KYC.md](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-workship-sokudan-offers-serial-cu-19f9/earn-workship-sokudan-offers-serial-cu-20260916/STOP-KYC.md)
- Morning 1枚 → [PR#4](https://github.com/rimone0511/autopilot-log/pull/4)
- PR#43 slip refresh is **Wave A** `draft_saved` / `blocked_skip`. These six desks are **not** that slip.

---

## 5つの止め（この6机）

1. ファイル選択ダイアログを開かない。カメラ権限を KYC に渡さない。
2. マイナンバー番号面 / 裏面、保険証の番号、口座番号を撮らない・貼らない。
3. git / チャット / セッションログに書類写真・顔・OTP・電話の実値を残さない。
4. 有料の本人確認ブースター・優先掲載・前払いを KYC の代わりに買わない。
5. 画面がパックと違う → **画面を正**。推測で別書類を足さない。

## 朝メモの型（秘密なし）

```
date:
desk: Workship | SOKUDAN | Offers | Skill Shift | ITプロパートナーズ | Workshift
screen:
saved_draft: yes/no/unknown
kyc_shown: yes/no
upload: none
next: morning-user | park | next-desk
```

`kyc_wait` is a valid desk outcome. It is not failure. Next desk in [ORDER.md](ORDER.md) is allowed after park.

---

## Per desk — stop here

### B02 Workship

- 前払いオプション（公開ヘルプ: 「本人確認が必要です」 https://goworkship.com/help/agreement/95 — this GET 200）
- 契約管理の署名で身分証や印鑑証明
- 口座・振込先・マイナンバー
- 募集へのエントリー / 成約報告のお祝い金フロー

プロフィール下書きには先回りしない。

### B01 SOKUDAN

- 利用規約が言う「審査に必要な書類」（this GET `/pages/terms` 200: 提出しない場合は登録を拒否しうる）
- 免許・マイナンバーカード・住民票・顔写真付き証明書
- 本人確認アプリ、口座、案件応募、発注者申込

規約: 代理人による会員登録は認められない。CU は本人同席前提。この markdown の著者は登録しない。

### B19 Offers

- 「登録して求人に応募する」
- ヘッドハント面談の日程確定（CU）
- 本人確認書類、口座・出金、有料ブース

トップが転職コピーでも、Jobs を見たあとに **応募しない**。

### B06 Skill Shift

- 利用規約の「本人確認サービス」資料提出（sibling PR#33 cites 第7条6 on https://www.skill-shift.com/terms-of-service — this GET 200 shell; live text wins）
- 代理登録（第3条: 本人が行う）
- 現場のみ行への応募、企業会員・資料請求

### B07 ITプロパートナーズ

- エージェント面談・個別契約書 / NDA の代行署名
- 面談で免許・住民票・マイナンバー
- 案件カードからの応募、営業電話に CU が出ること

Web の職種選択〜プロフィール入力は KYC ではない。**面談は本人。**

### B09 Workshift

- 案件カードの「本人確認: Yes」（this GET on `/jobs/view/13758` showed **無し** for that card — other cards may differ. If Yes / upload → STOP）
- パスポート / 顔写真 / 住所証明
- 現地ブース・展示会現地カードへの応募
- 新規 Facebook / LinkedIn を身分にすること
- 有料会員・ウォレット最低残高が必須なら `blocked_paid_plan`

---

## Allowed (not KYC)

- MAIN Google signup / login where the button exists
- Same MAIN mailbox + parent Gmail OTP on mailbox desks
- SMS only if **draft save** is blocked, and only with a number the **user** placed in chat. If the phone step asks for ID → KYC STOP
- Worker / 人材 / フリーランス **profile draft** (public toggle off if present)

## If KYC appears

1. Close the upload dialog. Do not choose a file. Do not take a selfie.
2. Leave whatever unpublished draft already saved.
3. Record only: date, desk, screen type (`photo_id` / `my_number` / `selfie` / `address` / `bank` / `review_docs` / `prepaid_id` / `agent_interview` / other).
4. Morning operator decides.
5. Continue to the **next** desk in ORDER.md if the session is not locked.

Do not store screenshots that show ID, face, or full account email in the repo.
