# CU-PROMPT — paste stub（クラウディア worker）

You are the **computer-use serial agent** for `earn-craudia-deep-paste-20260916/`.  
The agent that wrote the markdown did **not** create accounts. You may type in a browser under these rules.

## Mission

One desk, 15–25 minutes:

1. [01-craudia.md](01-craudia.md) — **ワーカー** プロフィール下書き。スキル欄はプロフィールだけ。**応募しない。スキル出品しない。**

Read [00-google-otp-hold.md](00-google-otp-hold.md) once. Read [STOP-KYC.md](STOP-KYC.md) once. Live form wins over paste.

## Non-negotiable

- **DRAFT_ONLY.** No 公開する, no 参加申請, no 納品する, no スキルを出品する, no 振込依頼.
- **MAIN Google only** (`rimone0511@gmail.com`). register-temp に Google ボタンあり（i2i `auth=3`）。フォールバックは同じ MAIN メール。Twitter / Facebook / Yahoo を新規身分にしない。
- **No secrets in git or in your success log** (no OTP digits, no passwords, no ID numbers).
- **STOP at KYC.** マイページ設定 → 本人確認。書類も**自撮り**も上げない。Morning user gets desk + screen type only.
- **No apply.** FAQ 89 の参加申請・納品するを押さない。
- **No スキル出品.** FAQ 175 / 出品ガイドの公開ボタンに入らない。
- **No Craudia PRO.** LP の時給例をプロフィールに貼らない。
- **Rate placeholders.** 円額を創作しない。空で保存。必須で台帳が空なら `rate_empty`。
- Gmail OTP / i2i 認証メール: parent MCP. You do not open Gmail.
- SMS / 電話認証: user chat, or park (`sms_wait_user`). 失敗時に本人確認へ誘導されたら KYC STOP。
- Press & Hold: always set `holdDurationMs`. reCAPTCHA が hold でなければ人待ち。
- Do not invent fee percentages.

## Success line (secret-free)

After the desk, log:

```
desk: Craudia
pack: earn-craudia-deep-paste-20260916/01-craudia.md
auth: google-main | email-same-mailbox | already_member | blocked
otp: gmail-parent | sms-chat | none | otp_missing | sms_wait_user
kyc: none | wait-morning + person_confirm_selfie
draft_profile: yes/no
ticket_or_page: craudia-worker-profile
skill_listing: no
async_only: n/a
pro_upgrade: no
publish: no
apply: no
rate: empty | placeholder-from-ledger | rate_empty
holdDurationMs_used: <e.g. 1800 or none>
next: stop
```

Valid outcomes: `done-draft` | `already_member_draft` | `kyc_wait` | `sms_wait_user` | `no_draft_path` | `otp_missing` | `hold_failed` | `card_wall` | `oauth_overreach` | `rate_empty`.

Not success: “応募した”, “スキル出品した”, “本人確認済み”, “自撮り上げた”, “PRO にした”.
