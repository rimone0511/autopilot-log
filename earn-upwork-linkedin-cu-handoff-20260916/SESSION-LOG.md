# Session log — template (secret-free)

Copy this block into an agent summary, or save locally as  
`earn-upwork-linkedin-cu-handoff-20260916/sessions/<YYYYMMDD-HHMM>-jst.md`  
(**do not commit** OTP, mail quotes, ID crops, or filled passwords).

This folder’s CU serial is **A5 then A6 only**.

```
date_jst:
cu_agent: earn-upwork-linkedin-cu-handoff-20260916
google: MAIN rimone0511 (yes/no)
sns_mode: DRAFT_ONLY
auto_bid: no
connects_spent: 0
holdDurationMs_used: [e.g. 1800 on Cloudflare @ Upwork / none]

| desk | pack_path | auth | otp | kyc | draft | publish | rates | next |
|---|---|---|---|---|---|---|---|---|
| Upwork | 01-upwork-profile.md + 02-upwork-catalog.md |  |  |  |  | no | placeholders / rate_required | LinkedIn Services |
| LinkedIn Services | 03-linkedin-services.md |  |  |  |  | no | contact-for-pricing / rate_required / no_draft_path | stop (this pack) |
```

Allowed cell values:

- `auth`: `google-main` | `email-same-mailbox` | `blocked` | `already_member`
- `otp`: `gmail-parent` | `sms-chat` | `none` | `otp_missing` | `sms_wait_user`
- `kyc`: `none` | `wait-morning` + type (`photo_id` / `my_number` / `selfie` / `address` / `bank` / `card_microcharge` / `ads_wallet`)
- `draft`: `yes` | `no` | `no_draft_path` | `already_member_draft`
- `publish`: always `no` in this GO
- `rates`: `placeholders` | `contact-for-pricing` | `rate_required` (never a made-up USD in git)

Morning KYC list (names + screen types only):

- 
