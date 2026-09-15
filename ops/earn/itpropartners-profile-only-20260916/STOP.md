> **MAIN Google mailbox only.** `{{EMAIL}}`. No second account.
> **DRAFT_ONLY.** Profile save / input only.
> **No interview booking.** エージェント面談・電話ヒアリング・企業面談の日程は CU が確定しない。
> **STOP-KYC.** Agents and CU **do not upload**. Morning user only.
> **No secrets.** No ID photos, My Number, bank digits, OTP, passwords, CSRF/`_token` in git or chat.
> **No invented fees.** Do not pay to skip identity or to skip 面談.
> **No publish / no 応募.** Saving a draft is not a listing and is not an application.

# STOP — B07 ITプロパートナーズ (interview-heavy)

Pack: `ops/earn/itpropartners-profile-only-20260916/`  
Pack date: **2026-09-16**  
Mode: **DRAFT_ONLY**  
Audience: 朝の本人 and later CU. One desk.

This STOP is **stricter than “no KYC”**. The official seller path is interview-heavy. Early CU may type a **profile draft**. It may **not** book interviews.

Long KYC rows (not copied): [PR#30 STOP-KYC CU-28](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-waveb-cu-handoff-batch2-87d0/earn-waveb-cu-handoff-batch2-20260916/STOP-KYC.md). Morning 1枚: [PR#4](https://github.com/rimone0511/autopilot-log/pull/4).

Official flow cited this GET (logged out):

| Step | Where | CU |
|---|---|---|
| 01 無料会員登録 | `/` / `/register` | Profile draft **only if** a human GO. This PR does not submit |
| 02 エージェント面談 | `/`「電話、もしくは**面談予約**にてヒアリング」。Blog ②プロ面談（オフィス） | **STOP. Do not book.** |
| 03 案件紹介・企業面談 | `/` / Blog ③ご推薦と企業面談 | **STOP. Do not apply. Do not schedule.** |
| 04 契約・業務開始 | Blog ④内定・ご契約（個別契約書 / 秘密保持契約書） | **STOP.** 身分証が乗ったら即停止 |

---

## 止める（この机）

1. **面談予約** — カレンダー確定、予約フォーム送信、オフィス来訪の確定、Zoom リンクの CU 確定。
2. **電話ヒアリング** — 登録後「担当者からご連絡」に CU が出ない。番号をチャットに残さない。朝メモだけ。
3. **企業面談** — 推薦後のクライアント面談の日程調整を CU が確定しない。
4. **応募** — 公開カードの「応募」「気になる」「詳細を確認」からのエントリー送信。
5. **KYC / 契約書類** — 免許・住民票・マイナンバー・顔写真・口座。個別契約書 / NDA の代行署名。
6. **有料で面談や本人確認を飛ばす** — 公式HTMLにその商品は見ていない。あっても買わない。
7. **秘密** — `_token` / CSRF / パスワード設定リンクの中身 / OTP を git に書かない。
8. **画面がこの NOTE と違う** → **画面を正**。推測で 面談予約 を「プロフィールの一部」と読まない。

## やってよい（KYC でも面談でもない）

- 公開 GET（ログインなし）で職種面・案件カード日付を見る
- 人間 GO のときだけ: `/register` 職種 **エンジニア**、MAIN mailbox、スキル / 自己紹介の **下書き入力**
- 親 Gmail OTP（コードは git に書かない）。CU ブラウザで Gmail を開かない
- SMS は **下書き保存が電話で止まるときだけ**、ユーザーがチャットに置いた番号。ID 付きなら KYC STOP
- 公開トグルがあるなら **off** のまま

## 朝メモの型（秘密なし）

```
date:
desk: ITプロパートナーズ
screen: register_job | profile_draft | interview_booking | agent_call | company_interview | apply | kyc | nda | other
saved_draft: yes/no/unknown
interview_booked: no
apply: no
kyc_shown: yes/no
upload: none
next: morning-user | park | stop
```

`kyc_wait` and `interview_stop` are valid outcomes. They are not failure. They are **not** a reason to start another Wave B register desk from this folder (REGISTER-CU-CUT; prefer JOBS).

---

## If 面談予約 / 電話 / 企業面談 appears

1. Do **not** pick a slot. Do **not** submit 予約.
2. Do **not** answer the agent call from the CU session.
3. Leave whatever unpublished draft already saved.
4. Record only: date, desk, `screen` (`interview_booking` / `agent_call` / `company_interview`).
5. Morning operator decides. Default: **park**.

## If KYC / NDA appears

1. Close the upload dialog. Do not choose a file. Do not take a selfie.
2. Do not tick 秘密保持 / 個別契約 on behalf of the user.
3. Record `screen`: `photo_id` / `my_number` / `selfie` / `address` / `bank` / `nda` / `contract`.
4. Morning operator. No upload.

Do not store screenshots that show ID, face, full account email, or CSRF in the repo.
