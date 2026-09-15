> **MAIN Google only if a later human CU happens.** `{{EMAIL}}` for mail fallback. No second account. Facebook / LINE: do not use.
> **DRAFT_ONLY.** Profile save / input only.
> **No 「話を聞きたい」.** That is the warm-intro send. CU does not send it.
> **No job post.** Free 1-slot is **poster-side**. CU does not use it.
> **STOP-KYC.** Agents and CU **do not upload**. Morning user only.
> **No secrets.** No ID photos, My Number, bank digits, OTP, passwords, CSRF/`_token`, Set-Cookie values in git or chat.
> **No invented fees.** Do not buy 公式リクルーター or extra simultaneous jobs. Applicant % unread → do not invent.

# STOP — B18 YOUTRUST (warm intro / scout)

Pack: `earn-youtrust-gate-20260916/`  
Pack date: **2026-09-16**  
Mode: **DRAFT_ONLY**  
Audience: 朝の本人 and later CU. One desk.

This STOP is **stricter than “no KYC”**. Official talent conversion this GET is 「話を聞きたい」 (notify poster → カジュアル面談) or inbound recruiter **スカウト**. Early CU may type a **profile draft**. It may **not** send the intro.

Official flow cited this GET (logged out):

| Step | Where | CU |
|---|---|---|
| 01 Account create | help `account/create/` (mail / Google / Facebook / LINE). App `/sign_in` SPA | Profile draft **only if** a human GO. This PR does not submit |
| 02 Profile fill | help `want-to-talk/`: fill before 「話を聞きたい」 | Draft only. 副業・転職意欲: 閉じる側. If unclear, do not touch |
| 03 「話を聞きたい」 | jobs meta + `want-to-talk/`. Logged-out → 新規登録 then **notify**. Logged-in → メッセージ送信 | **STOP. Do not send.** |
| 04 カジュアル面談 / 面接 | `casual-vs-interview/` / `interview-step/` | **STOP. Do not book.** |
| 05 ジョブ投稿 | `how-to-post/` / `cost/` / `manage-applicants/` | **STOP.** Free 1 slot is poster-side |
| 06 公式リクルーター | `official-recruiter/` + recruiter scout help | **STOP. Do not buy.** |

---

## 止める（この机）

1. **「話を聞きたい」送信** — logged-out ボタン経由の新規登録完了も、ログイン後のメッセージ送信も。両方とも notify。
2. **つながり申請のばらまき** / Google連絡先「知り合いかも？」からの一括申請。
3. **ジョブ投稿** — 無料1件でも今は出さない。下書きジョブの「公開」もしない。
4. **公式リクルーター / 有料スカウト通数 / 同時複数ジョブ** — 買わない。問合せフォームも送らない。
5. **カジュアル面談・本面談の日程確定** — CU がスロットを取らない。
6. **KYC / 雇用契約書類** — 免許・住民票・マイナンバー・顔写真・口座。雇用契約を伴う求人の労働条件確認を CU が代行しない。
7. **秘密** — CSRF / `_token` / Set-Cookie / OTP / パスワード例を git に書かない。Help のパスワード例文字列も転記しない。
8. **画面がこの NOTE と違う** → **画面を正**。推測で 「話を聞きたい」を「プロフィールの一部」と読まない。

## やってよい（KYC でも warm-intro でもない）

- 公開 GET（ログインなし）で jobs shell / help / 401 JSON を見る
- 人間がブラウザで **1枚** ジョブカードの日付を見る（pass 判定用。CU ではない）
- 人間 GO のときだけ: `/sign_in` の Google（ボタン目視）または MAIN mailbox、プロフィール **下書き**
- 親 Gmail OTP（コードは git に書かない）。CU ブラウザで Gmail を開かない
- 公開トグル / 同僚に見えない設定があれば **閉じる側**。分からなければ触らない

## 朝メモの型（秘密なし）

```
date:
desk: YOUTRUST
screen: sign_in | profile_draft | want_to_talk | job_post | recruiter_pay | kyc | other
saved_draft: yes/no/unknown
want_to_talk_sent: no
job_posted: no
kyc_shown: yes/no
upload: none
next: morning-user | park | stop
```

`skip_live_cu` and `kyc_wait` are valid outcomes. They are **not** a reason to start another Wave B register desk from this folder (REGISTER-CU-CUT; prefer JOBS).

---

## If 「話を聞きたい」 / メッセージ送信 appears

1. Do **not** press the button. Do **not** send.
2. If the UI already opened a compose box, close it unsent.
3. Leave whatever unpublished draft already saved.
4. Record only: date, desk, `screen: want_to_talk`.
5. Morning operator. Default: **park**.

## If 公式リクルーター / 有料契約 appears

1. Do **not** open checkout. Do **not** submit お問い合わせ.
2. Record `screen: recruiter_pay`.
3. Keep `blocked_paid_plan` for that click. Close.

## If KYC appears

1. Close the upload dialog. Do not choose a file. Do not take a selfie.
2. Record `screen`: `photo_id` / `my_number` / `selfie` / `address` / `bank`.
3. Morning operator. No upload.

Do not store screenshots that show ID, face, full account email, CSRF, or cookies in the repo.
