# Session log — template (secret-free)

Copy this block into an agent summary, or save locally as  
`earn-waveb-global-handoff-20260916/sessions/<YYYYMMDD-HHMM>-jst.md`  
(**do not commit** OTP, mail quotes, ID crops, or filled passwords).

This folder’s CU serial is **Guru → Malt → Workana → Freelancermap → PeoplePerHour**.

```
date_jst:
cu_agent: earn-waveb-global-handoff-20260916
google: MAIN rimone0511 (yes/no)
sns_mode: DRAFT_ONLY
paid_subscribe: no
quotes_or_applies_sent: 0
holdDurationMs_used: [e.g. 1800 on Cloudflare @ Workana / none]

| desk | pack_path | auth | otp | kyc | paid | draft | publish | rates | next |
|---|---|---|---|---|---|---|---|---|---|
| Guru | 01-guru.md |  |  |  | no |  | no | placeholders / rate_required | Malt |
| Malt | 03-malt.md |  |  |  | no |  | no | placeholders / rate_required / no_draft_path | Workana |
| Workana | 04-workana.md |  |  |  | no |  | no | placeholders / rate_required | Freelancermap |
| Freelancermap | 05-freelancermap.md |  |  |  | no |  | no | placeholders / rate_required | PeoplePerHour |
| PeoplePerHour | 02-peopleperhour.md |  |  |  | blocked_paid_plan / no |  | no | placeholders / rate_required | stop (this pack) |
```

Allowed cell values:

- `auth`: `google-main` | `email-same-mailbox` | `blocked` | `already_member` | `google_needs_check`
- `otp`: `gmail-parent` | `sms-chat` | `none` | `otp_missing` | `sms_wait_user`
- `kyc`: `none` | `wait-morning` + type (`photo_id` / `my_number` / `selfie` / `address` / `bank` / `card_microcharge` / `persona_silt` / `aml_docs`)
- `paid`: `no` | `blocked_paid_plan` (never `subscribed` in this GO)
- `draft`: `yes` | `no` | `no_draft_path` | `already_member_draft`
- `publish`: always `no` in this GO
- `rates`: `placeholders` | `rate_required` (never a made-up USD/EUR in git)

Morning KYC / paywall list (names + screen types only):

- 
