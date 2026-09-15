> **DRAFT_ONLY.** Fill after a later CU session. The authoring agent of this PR did **not** sign up.
> **No secrets.** No OTP digits, passwords, phone numbers, CSRF, cookies, or ID filenames.

# Session log — Workship → SOKUDAN → Offers

Date (JST):  
Operator:  
CU agent / run:

Valid `outcome` values: `done-draft` | `already_member_draft` | `kyc_wait` | `sms_wait_user` | `no_draft_path` | `otp_missing` | `hold_failed` | `card_wall` | `oauth_overreach` | `not_run`.

`publish` and `apply` must stay `no`.

| desk | outcome | auth | otp | kyc | draft_profile | publish | apply | holdDurationMs_used | next |
|---|---|---|---|---|---|---|---|---|---|
| Workship | not_run | | | | | no | no | | SOKUDAN |
| SOKUDAN | not_run | | | | | no | no | | Offers |
| Offers | not_run | | | | | no | no | | stop |

Notes (secret-free):

```
```
