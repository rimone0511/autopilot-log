> **MAIN Google mailbox only.** `{{EMAIL}}`. No second account. No new LINE / Facebook.
> **DRAFT_ONLY.** Profile save / input only — and **not this pass**.
> **No class publish.** 掲載審査 / 講座作成ウィザードの公開申請は CU が送らない.
> **STOP-KYC.** Agents and CU **do not upload** 本人確認書類 or 顔撮影.
> **No secrets.** No ID photos, bank digits, OTP, passwords, CSRF / `authenticity_token` in git or chat.
> **No invented fees.** Re-read `/fee` at click time. Help 403 ≠ a second rate table.

# STOP — B12 ストアカ

Pack: `ops/earn/earn-storeca-gate-20260916/`  
Pack date: **2026-09-16**  
Mode: **DRAFT_ONLY**  
Audience: 朝の本人 and later CU. One desk.

This STOP is **stricter than “no KYC”**. Early CU (if a human later GOs) may type a **teacher profile draft**. It may **not** submit a class.

Official `/teach` copy this GET (logged out): 「先生として活動いただくためには、本人確認書類の提出をお願いしています」. 提出しない.

| Step | Where | CU |
|---|---|---|
| 会員登録 | `/register` or `/teach`「新規登録はこちら（無料）」 | Email path **only if** a human GO. This PR does not submit |
| 先生プロフィール | 名前・顔写真・公開 URL・自己紹介 | Draft / input only after human GO |
| 本人確認 | `/teach` ※1 | **STOP. Do not upload.** |
| 講座作成 / 掲載審査 | `/teach`「完成したページを掲載審査に提出」 | **STOP. Do not submit.** |
| 公開・募集開始 | same flow | **STOP.** |

Thick KYC rows (not copied): [PR#39 STOP-KYC](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-fukugyo-anycrew-storeka-gapfill-02a2/earn-fukugyo-anycrew-storeka-gapfill-20260916/STOP-KYC.md). Morning 1枚: [PR#4](https://github.com/rimone0511/autopilot-log/pull/4).

---

## 止める（この机）

1. **講座の公開申請 / 掲載審査** — ウィザードに入っても送らない。下書きが無いならプロフィールのみ。
2. **本人確認** — 顔写真付き公的証明書、顔撮影、eKYC。画面を閉じる。
3. **口座 / 振込先** — 出金設定は上げない。
4. **LINE / Facebook OAuth** — `/auth/line` `/auth/facebook` を完走しない。新規 SNS をこの机のためだけに作らない。
5. **有料で本人確認や審査を飛ばす** — 公式 `/fee` は登録・月額 0円. 別商品があっても買わない。
6. **秘密** — `authenticity_token` / パスワード / OTP / 顔写真ファイルを git に書かない。
7. **画面がこの NOTE と違う** → **画面を正**。推測で 掲載審査 を「プロフィールの一部」と読まない。

## やってよい（KYC でも出品でもない）

- 公開 GET（ログインなし）で `/teach`・講座カード日付を見る
- 人間 GO のときだけ: `/register` メール = MAIN mailbox、先生プロフィールの **下書き入力**
- 親 Gmail OTP（コードは git に書かない）。CU ブラウザで Gmail を開かない
- 公開トグルがあるなら **off** のまま

## 朝メモの型（秘密なし）

```
date:
desk: ストアカ
screen: teach | register | profile_draft | class_wizard | listing_review | kyc | waf | other
saved_draft: yes/no/unknown
class_submitted: no
kyc_shown: yes/no
upload: none
waf: none | www_405 | cf_403 | other
next: morning-user | park | stop
```

`kyc_wait` and `listing_stop` are valid outcomes. They are not failure. They are **not** a reason to start another Wave B register desk from this folder (REGISTER-CU-CUT; prefer JOBS).

---

## If WAF / Cloudflare appears

1. www AWS WAF 405 / Human Verification: human solves, or **park**. Do not call the desk dead.
2. support.street-academy.com 403 / www `/faq` 403: leave help unread. Use `/fee` for rates. Do not guess help text.
3. www `/help` 404 this GET: not the Zendesk host.

## If KYC / 掲載審査 appears

1. Close the upload / 提出 dialog. Do not choose a file. Do not take a selfie.
2. Do not tick 掲載審査 on behalf of the user.
3. Record `screen`: `photo_id` / `selfie` / `listing_review` / `bank`.
4. Morning operator. No upload. No class submit.

Do not store screenshots that show ID, face, full account email, or CSRF in the repo.
