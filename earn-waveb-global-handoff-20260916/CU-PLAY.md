# CU play — Wave B GLOBAL (this folder)

Audience: computer-use agent. One human operator.  
Mode: **`DRAFT_ONLY`**. Timebox: **15–25 minutes per desk**.  
Serial for **this folder only** (paywall last; not INDEX CU-19→CU-20):

```
Guru (profile + one Service, free Basic)
  → Malt (English profile draft; skip legal uploads)
  → Workana (EN talent draft; profile not public)
  → Freelancermap (free Basic profile; do not Activate-to-apply)
  → PeoplePerHour (open register only; park if PPH Basic / TopAccess paywall)
```

Do not continue into YOUTRUST / Offers / JP Week2 / Wave A from here.

INDEX CU numbers (inventory): Guru CU-19, PPH CU-20, Malt CU-21, Workana CU-22, Freelancermap CU-23.  
QUEUE: B8–B12. Wave A `next` must be `done-draft` before a **production** Week2 serial. This folder is the GLOBAL handoff pack.

---

## 0. One-screen GO / NO-GO

| Switch | Value | If you cannot keep it |
|---|---|---|
| Account | MAIN Google `{{GOOGLE_ACCOUNT_EMAIL}}` only | STOP. No second identity. |
| Google button missing | Same MAIN mailbox as email | Do not invent a new address. |
| Publish | `DRAFT_ONLY` | STOP. Do not toggle public / submit / apply. |
| KYC | Stop. Morning user. No uploads | Hand off. Do not continue that desk. |
| Paid plans | **Do not subscribe** | Park `blocked_paid_plan`. Especially **PPH Basic annual**. |
| Quotes / proposals / applications | **0 sent** | Do not bid. Do not apply. |
| Rates | Placeholders only | Park `rate_required` rather than invent USD/EUR. |
| Traffic / GMV | Do not invent | `pass` / `needs_check` / `blocked_paid_plan` only. |
| Email OTP | Parent Gmail MCP | Do not open `mail.google.com` in the CU profile. |
| SMS OTP | User chat | Wait. Do not guess. |
| Press & Hold | `holdDurationMs` required | Do not fake a hold with click+sleep. |
| Secrets | Never in git / this log / code screenshots | Redact. |

Viewport: desktop **≥ 1280px**. Do not switch to a phone emulator mid-desk unless the site dead-ends on desktop (record it).

---

## 1. Preflight

1. Confirm you will use **one** browser profile signed into MAIN Google, or a clean profile that will **only** pick that Google account.
2. If a Press & Hold / 長押し / Cloudflare hold appears, the tool call **must** include `holdDurationMs` (start **1800**; one retry **2500**). If the schema has no such field: STOP (`tool_missing_holdDurationMs`).
3. Open [STOP-KYC.md](STOP-KYC.md). File pickers for ID = close without a file.
4. Paste packs: [01-guru.md](01-guru.md) → [03-malt.md](03-malt.md) → [04-workana.md](04-workana.md) → [05-freelancermap.md](05-freelancermap.md) → [02-peopleperhour.md](02-peopleperhour.md). **Live form wins** if it disagrees.
5. This authoring PR used **public GET only**. Click-time labels may differ. WAF (Incapsula / Cloudflare) is expected on Guru / Malt / Workana.

You will **not**: scrape, like, follow, message buyers, send quotes, apply to jobs, open Gmail in CU, subscribe, or operate Autopilot Log posting.

---

## 2. MAIN Google login play

1. Click **Continue with Google** / **Continue with GOOGLE** when present.
2. Pick **only** the MAIN account. If the picker shows another user, do not continue.
3. After login, if you land on a **buyer / hire / project provider** home: switch to Freelancer / I want to work. If you cannot switch without KYC or a paid plan, stop with that code.
4. **Already registered** with MAIN Google: do not duplicate. Open the existing seller/profile surface. Still no publish.
5. **No Google button** (Freelancermap public HTML on 2026-09-15): email path with `{{EMAIL}}` = MAIN mailbox. Password is `{{PASSWORD_DO_NOT_STORE}}` — never commit. Activation link via parent Gmail MCP.

OTP:

- Mail code / magic link / activation URL → **parent Gmail MCP**. CU does not open Gmail.
- SMS → **user chat**. One resend then `sms_wait_user` and park the desk (you may still start the next desk if the session is not locked).

---

## 3. Desk 1 — Guru.com (CU-19 / B8)

| | |
|---|---|
| Role | **Freelancer**. Not Employer. |
| Entry | https://www.guru.com/ — Sign Up → Google |
| Pack | [01-guru.md](01-guru.md) |
| Google | **PREFER_GOOGLE** (sibling public help). This environment’s GET was Incapsula **403** — confirm the button at click-time. |
| Draft artifact | Profile **hidden** if offered. One Service with placeholder rates. Membership **free Basic**. |
| KYC stop | Verify dashboard → government ID, proof of address, card micro-charge, **4.95 USD** review fee. |
| Do not | Upgrade Basic; buy quotes; send a Quote; un-hide for search. |

Done codes: `done-draft` | `already_member_draft` | `kyc_wait` | `sms_wait_user` | `rate_required` | `blocked_paid_plan` | `otp_missing`.

---

## 4. Desk 2 — Malt.com (CU-21 / B10)

| | |
|---|---|
| Role | Freelancer / I’m looking for a project. Not company hire. |
| Entry | https://www.malt.com/ — Create my account. English UI if offered. |
| Pack | [03-malt.md](03-malt.md) |
| Google | **needs_check**. Use it if the button exists. Else MAIN mailbox email. |
| Draft artifact | English headline + bio (≥200 characters per Malt help). Skills + category. **No legal-document tab.** |
| KYC stop | Passport / national ID / company papers / VAT submit / AML validation. |
| Do not | Fake an EU address. Second Malt account. Boost / Super Malter. Payout / bank. |

If Save = searchable and there is no hidden/incomplete state, stop (`no_draft_path`) rather than publishing.

---

## 5. Desk 3 — Workana (CU-22 / B11)

| | |
|---|---|
| Role | Find work / Freelancer. Not Hire talent. |
| Entry | https://www.workana.com/en/signup — Google preferred |
| Pack | [04-workana.md](04-workana.md) |
| Google | **PREFER_GOOGLE** on sibling `/en/login` HTML. This environment’s GET was Cloudflare **403** — confirm at click-time. |
| Draft artifact | EN About + skills + photo. **Keep my profile public = OFF**. No bids. |
| KYC stop | Government ID for payment verification; WhatsApp ID send; My Finances. |
| Do not | Priority Moderation. Off-platform contact in About. Fake LATAM city. |

Cloudflare: complete as a human with `holdDurationMs`. Do not invent job-board density if `/en/jobs` still challenges.

---

## 6. Desk 4 — Freelancermap (CU-23 / B12)

| | |
|---|---|
| Role | **Freelancer / Agency** seeking projects. Not Project provider. |
| Entry | https://www.freelancermap.com/registration |
| Pack | [05-freelancermap.md](05-freelancermap.md) |
| Google | **NOT_OFFERED_OAUTH** on public registration/login HTML (2026-09-15 GET). Email = MAIN mailbox. |
| Draft artifact | Free **Basic** profile fields. Leave **inactive / private / anonymous** if the UI allows. **0 applications.** |
| KYC stop | Profile verification (Persona / SILT): ID + selfie biometrics (paid: public pricing €50/year Premium, €75/year Basic). |
| Do not | Premium (€13.99/month billed annually on public pricing). IBAN/PayPal for membership. Apply to projects. Activate-to-apply if that is a publish path. |

---

## 7. Desk 5 — PeoplePerHour (CU-20 / B9) — **paywall last**

| | |
|---|---|
| Role | **I want to work as a freelancer**. Not hire. |
| Entry | https://www.peopleperhour.com/site/register |
| Pack | [02-peopleperhour.md](02-peopleperhour.md) |
| Google | **PREFER_GOOGLE** — public register HTML 2026-09-15: button **Continue with GOOGLE**. |
| Draft artifact | Application text + photo locally in the pack. **Do not subscribe.** |
| KYC stop | Settings → Payments document upload; Fast-Track KYC. |
| **Park if paywall** | Public Terms: **PPH Basic is a non-refundable annual subscription** (monthly or prepaid for the Annual Term). TopAccess is a second paid annual bundle. If the UI will not submit without a plan → close tab. Code: `blocked_paid_plan`. **Do not pay to find out.** |

Keep Hourlie/Offer copy in the pack. Do not **Post an Offer** if posting requires a paid plan.

---

## 8. STOP notes (all desks)

Hand **desk name + screen type** to morning. Do not upload. Do not pay.

| Stop | Examples | Code |
|---|---|---|
| KYC / identity | Passport, license, My Number, liveness, proof of address, Persona, SILT, Guru Verify, Malt legal docs | `kyc_wait` |
| Paid plan | PPH Basic annual, TopAccess, Guru paid tier, Freelancermap Premium, featured, Fast-Track, Priority Moderation | `blocked_paid_plan` |
| Publish / bid | Submit Service, un-hide profile, send Quote, Post Offer, apply to project, Keep profile public ON | do not click; stay `DRAFT_ONLY` |
| Rate wall | Required USD/EUR and placeholder empty | `rate_required` |
| SMS | Phone OTP, user not in chat | `sms_wait_user` |
| Tool | Cloudflare hold with no `holdDurationMs` in schema | `tool_missing_holdDurationMs` |

You may continue the **next** desk only if the browser session is not identity-locked.

---

## 9. Session log

Fill [SESSION-LOG.md](SESSION-LOG.md). No OTP, no ID crops, no passwords.

---

## 10. Prompt stub (future CU agent)

```
Follow earn-waveb-global-handoff-20260916/CU-PLAY.md exactly.
Serial: Guru → Malt → Workana → Freelancermap → PeoplePerHour last.
MAIN Google preferred. Same MAIN mailbox if a desk has no Google button.
DRAFT_ONLY. Stop KYC. No paid plan subscribe.
PeoplePerHour: public Terms call PPH Basic a paid annual subscription — park blocked_paid_plan if the next click is pay. Do not subscribe to find a free path.
No quotes, proposals, applications, or invented traffic.
Gmail OTP: parent Gmail MCP. Do not open Gmail in the CU browser.
SMS OTP: wait in user chat.
Press & Hold: holdDurationMs 1800, one retry 2500.
Live form wins. Do not publish.
```
