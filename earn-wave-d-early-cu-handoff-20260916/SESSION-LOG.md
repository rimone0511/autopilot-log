# Session log — template (secret-free)

Copy this block into an agent summary, or save locally as  
`earn-wave-d-early-cu-handoff-20260916/sessions/<YYYYMMDD-HHMM>-jst.md`  
(**do not commit** OTP, mail quotes, ID crops, or filled passwords).

This folder’s CU serial is **note → Braintrust → Twine → Fastwork → 99freelas → Gulp**.  
Shufti / カイコク = NOTES only. Twago / Xing = SKIP.

```
date_jst:
cu_agent: earn-wave-d-early-cu-handoff-20260916
google: MAIN rimone0511 (yes/no)
sns_mode: DRAFT_ONLY
paid_subscribe: no
quotes_or_applies_sent: 0
holdDurationMs_used: [e.g. 1800 on Cloudflare @ 99freelas / none]

| desk | pack_path | auth | otp | kyc | paid | draft | publish | rates | next |
|---|---|---|---|---|---|---|---|---|---|
| note | 01-note.md |  |  |  | no |  | no | placeholders / rate_required | Braintrust |
| Braintrust | 02-braintrust.md |  |  |  | no |  | no | placeholders / rate_required / no_draft_path | Twine |
| Twine | 03-twine.md |  |  |  | no |  | no | placeholders / rate_required | Fastwork |
| Fastwork | 04-fastwork.md |  |  |  | no |  | no | kyc_wait / placeholders | 99freelas |
| 99freelas | 05-99freelas.md |  |  |  | no |  | no | placeholders / rate_required | Gulp |
| Gulp | 06-gulp.md |  |  |  | no |  | no | placeholders / rate_required | stop (this pack) |
```

Allowed cell values:

- `auth`: `google-main` | `email-same-mailbox` | `blocked` | `already_member` | `google_needs_check`
- `otp`: `gmail-parent` | `sms-chat` | `none` | `otp_missing` | `sms_wait_user`
- `kyc`: `none` | `wait-morning` + type (`photo_id` / `my_number` / `selfie` / `address` / `bank` / `stripe_wise` / `thai_id_bank`)
- `paid`: `no` | `blocked_paid_plan` (never `subscribed` in this GO)
- `draft`: `yes` | `no` | `no_draft_path` | `already_member_draft` | `kyc_at_signup`
- `publish`: always `no` in this GO
- `rates`: `placeholders` | `rate_required` (never a made-up amount in git)

Morning KYC / paywall list (names + screen types only):

- 
