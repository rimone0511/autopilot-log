# STOP-KYC one-pager — Wave D-early KEEP

Mode: **`DRAFT_ONLY`**. This PR did **not** sign up.  
Full checklist (do not copy here):  
[`earn-wave-d-early-cu-handoff-20260916/STOP-KYC.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-wave-d-early-cu-handoff-9adc/earn-wave-d-early-cu-handoff-20260916/STOP-KYC.md) ([PR#42](https://github.com/rimone0511/autopilot-log/pull/42)).

Morning human sheet: `earn-kyc-morning-checklist-20260916/` ([PR#4](https://github.com/rimone0511/autopilot-log/pull/4)).

**Rule:** if a wall appears, close the picker **without a file**. Hand **desk name + screen type** to morning. Do not pay to skip. You may start the **next** desk only if the browser session is not identity-locked.

---

## Hard stop (every desk)

| Wall | Examples | Code |
|---|---|---|
| Identity | Passport, license, My Number, Thai ID, QR-ID camera, liveness, selfie-with-ID, video review | `kyc_wait` |
| Address | Utility bill, bank statement, 住民票 | `kyc_wait` |
| Payout / tax | Bank book, IBAN, Stripe/Wise, Payoneer, W-8BEN, VAT, 適格請求書, card-for-identity | `kyc_wait` |
| Paid plan | Any checkout, badge, boost, membership | `blocked_paid_plan` |
| Publish / bid | 公開, Post services, apply, proposta, bewerben | do not click; stay `DRAFT_ONLY` |
| Rate required | Live form needs JPY/USD/EUR/THB/BRL and placeholder is empty | `rate_required` |
| SMS OTP | Phone code; user not in chat | `sms_wait_user` |
| Hold tool | Cloudflare / 長押し with no `holdDurationMs` in the schema | `tool_missing_holdDurationMs` |

Do not store screenshots that show ID, face, full mailbox, or OTP.

Keep `{{COUNTRY}}` / `{{CITY}}` honest (Japan is fine). Do not spoof US / EU / DE / TH / BR to chase filters. Profile photo = operator face (`{{PROFILE_PHOTO_LOCAL_PATH}}`), never an ID crop.

---

## Desk walls (KEEP six only)

| Play | Desk | Immediate stop | Do not buy / send |
|---|---|---|---|
| 1 | note | 口座 / 振込 / 本人確認 | 公開, メンバーシップ launch |
| 2 | Braintrust | Get Certified / ID-verified / AI interview-for-identity / Stripe or Wise bank | Apply to `/jobs` |
| 3 | Twine | ID / payout / card-for-identity | Business **$139.99/project**; any application (incl. Ari) |
| 4 | Fastwork | **ID + bank at register** (public start-selling copy). Park. Do not upload. | Post services (48h review = publish); Specialist / BYOB |
| 5 | 99freelas | Payout / government ID / bank | Premium **R$54,90–89,90/mês**; Turbinar; propostas |
| 6 | Gulp | Steuer-ID / ID / bank file picker | Membership **120 / 180 Euro netto**; Bewerbungen (esp. CH onsite) |

Out of this serial: Shufti / カイコク (NOTES only). Twago / Xing Projects (SKIP). Do not reach their KYC forms from here.

---

## If the wall appears during signup

1. Do not upload. Do not subscribe.
2. Close the ID / checkout flow.
3. Note: date, desk, screen type, required vs optional, paid vs free.
4. Mark the desk `kyc_wait` or `blocked_paid_plan` (git packs still count as draft copy).
5. Continue the next KEEP desk only if the session is not locked.
