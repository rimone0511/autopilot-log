# CU play — Wave D-early KEEP (this folder)

Audience: computer-use agent. One human operator.  
Mode: **`DRAFT_ONLY`**. Timebox: **15–25 minutes per KEEP desk**.  
Serial for **this folder only** (PR#22 operator order; not INDEX CU):

```
note (JP profile + paid-article DRAFT, do not 公開)
  → Braintrust (Talent profile draft; STOP at ID / Certified / AI interview-for-identity)
  → Twine (portfolio draft; Ari jobs SKIP; 0 applications)
  → Fastwork (open start-selling only; STOP if ID or bank is required — public page says they are)
  → 99freelas (freelancer role; Google; profile draft; 0 proposals; no Premium)
  → Gulp (free Basisprofil; MAIN mailbox; do not apply, especially CH onsite)
```

Do **not** continue into Shufti, カイコク, Twago, Xing, Wave A, or Wave B from here.

INDEX CU numbers: **unindexed**. QUEUE: C4 / C8 / D3 / D6 + gate-added 99freelas / Gulp. Wave A `next` must stay ahead in production. This folder is the D-early KEEP handoff only.

---

## 0. One-screen GO / NO-GO

| Switch | Value | If you cannot keep it |
|---|---|---|
| Account | MAIN Google `{{GOOGLE_ACCOUNT_EMAIL}}` only | STOP. No second identity. |
| Google button missing | Same MAIN mailbox as email | Do not invent a new address. |
| Publish | `DRAFT_ONLY` | STOP. Do not 公開 / Submit / Post / apply. |
| KYC | Stop. Morning user. No uploads | Hand off. Do not continue that desk. |
| Paid plans | **Do not subscribe** | Park `blocked_paid_plan`. |
| Quotes / proposals / applications | **0 sent** | Do not bid. Do not apply. |
| Rates | Placeholders only | Park `rate_required` rather than invent JPY/USD/EUR/THB/BRL. |
| Traffic / GMV | Do not invent | `pass` / `alive` / `needs_check` / `blocked_paid_plan` only. |
| Email OTP | Parent Gmail MCP | Do not open `mail.google.com` in the CU profile. |
| SMS OTP | User chat | Wait. Do not guess. |
| Press & Hold | `holdDurationMs` required | Do not fake a hold with click+sleep. |
| Secrets | Never in git / this log / code screenshots | Redact. |
| Shufti / カイコク | NOTES only | Do not open signup. |
| Twago / Xing | SKIP | Close if opened by mistake. |

Viewport: desktop **≥ 1280px**. Do not switch to a phone emulator mid-desk unless the site dead-ends on desktop (record it).

---

## 1. Preflight

1. Confirm you will use **one** browser profile signed into MAIN Google, or a clean profile that will **only** pick that Google account.
2. If a Press & Hold / 長押し / Cloudflare hold appears, the tool call **must** include `holdDurationMs` (start **1800**; one retry **2500**). If the schema has no such field: STOP (`tool_missing_holdDurationMs`).
3. Open [STOP-KYC.md](STOP-KYC.md). File pickers for ID / bank book = close without a file.
4. Paste packs: [01-note.md](01-note.md) → [02-braintrust.md](02-braintrust.md) → [03-twine.md](03-twine.md) → [04-fastwork.md](04-fastwork.md) → [05-99freelas.md](05-99freelas.md) → [06-gulp.md](06-gulp.md). **Live form wins** if it disagrees.
5. This authoring PR used **public GET only**. Click-time labels may differ. WAF (Cloudflare) is expected on help-note.com and `/register/freelancer`.

You will **not**: scrape, like, follow, message buyers, send quotes, apply to jobs, open Gmail in CU, subscribe, upload ID, or operate Autopilot Log posting.

---

## 2. MAIN Google login play

1. Click **Googleで登録** / **Googleでログイン** / **Continue with Google** / **Sign up with Google** when present.
2. Pick **only** the MAIN account. If the picker shows another user, do not continue.
3. After login, if you land on a **buyer / client / 企業** home: switch to creator / talent / freelancer. If you cannot switch without KYC or a paid plan, stop with that code.
4. **Already registered** with MAIN Google: do not duplicate. Open the existing seller/profile surface. Still no publish.
5. **No Google button** (Gulp public HTML 2026-09-16): email path with `{{EMAIL}}` = MAIN mailbox. Password is `{{PASSWORD_DO_NOT_STORE}}` — never commit. Activation link via parent Gmail MCP.

OTP:

- Mail code / magic link / activation URL → **parent Gmail MCP**. CU does not open Gmail.
- SMS → **user chat**. One resend then `sms_wait_user` and park the desk (you may still start the next desk if the session is not locked).

---

## 3. Desk 1 — note (C4)

| | |
|---|---|
| Role | Creator. Not 法人プラン sales. |
| Entry | https://note.com/signup — if SPA empty, https://note.com/login then 会員登録はこちら |
| Pack | [01-note.md](01-note.md) |
| Google | **PREFER_GOOGLE** — `/login` HTML: button `aria-label="Googleでログイン"` plus X / Apple / メール. Confirm the same on `/signup` at click-time (`/signup` this GET was title-only SPA). |
| Draft artifact | Profile + **unpublished** paid-article body. Membership **not launched**. |
| KYC stop | 口座・振込・本人確認. |
| Do not | 公開 / 有料マガジン公開 / help-note.com fee invention (this IP: Cloudflare 403). |

Done codes: `done-draft` | `already_member_draft` | `kyc_wait` | `sms_wait_user` | `rate_required` | `otp_missing`.

---

## 4. Desk 2 — Braintrust (C8)

| | |
|---|---|
| Role | Talent. Not client / Book a Demo. |
| Entry | https://www.usebraintrust.com/for-talent → Join the Network → https://app.usebraintrust.com/auth/sign_up/goals |
| Pack | [02-braintrust.md](02-braintrust.md) |
| Google | **needs_check**. App signup/login this GET = SPA shell (title only). Use Google if the button exists; else MAIN mailbox. |
| Draft artifact | Profile fields / skills / EN bio. **Stop before Get Certified / ID-verified / AI Skills Interview if that flow captures identity.** |
| KYC stop | ID verification, liveness, Stripe/Wise bank for payout (Site Service Fees terms: banking info to Payment Processor). |
| Do not | Apply to `/jobs`. Treat “2M+ members” / “10K+ roles” as marketing. Fake US location. |

If the only Save makes the profile searchable and there is no incomplete/hidden state → `no_draft_path`.

---

## 5. Desk 3 — Twine (D3)

| | |
|---|---|
| Role | Freelancer / Find work. Not Hire an Expert. |
| Entry | https://www.twine.net/signup |
| Pack | [03-twine.md](03-twine.md) |
| Google | **PREFER_GOOGLE** — signup page JS includes `signingUpViaGoogle` / `gotGoogleOAuthURL`. Visible button needs JS (noscript this GET). Confirm label at click-time. |
| Draft artifact | Portfolio / profile draft. **0 applications.** |
| KYC stop | ID / payout / card-for-identity. |
| Do not | Apply to **Ari** aggregated jobs. Buy Business **$139.99 per project**. Invent a freelancer % (public pricing “Service fee from 5%” is **client** success-fee copy). |

---

## 6. Desk 4 — Fastwork (D6) — **KYC likely at signup**

| | |
|---|---|
| Role | Freelancer. Online categories only. |
| Entry | https://fastwork.co/en/start-selling (this GET title “Join as a Freelancer”). `/en/signup` = **404** SPA. `/en/login` = **404**. |
| Pack | [04-fastwork.md](04-fastwork.md) |
| Google | **needs_check**. Start-selling “Sign Up as a Freelancer” button was `disabled` in this HTML. No Continue-with-Google label found. |
| Draft artifact | **Often none.** Public copy: “Register with your ID and bank details for verification.” If that form appears → `kyc_wait` and close. Do not upload. Do not post services (48h team approval = publish path). |
| KYC stop | National ID + bank at register; “Freelancers verify their identity in the system before hiring begins.” |
| Do not | Massage / housekeeping / on-site TH services. Specialist program. Invent seller commission (unread). |

Seller % is `unknown`. Do not copy BYOB “0% commission” marketing into the fee field.

---

## 7. Desk 5 — 99freelas

| | |
|---|---|
| Role | **Eu quero Trabalhar**. Not Contratar. |
| Entry | https://www.99freelas.com.br/register (this GET 200). `/register/freelancer` = Cloudflare **403** this IP — if that URL challenges, start at `/register` and pick Trabalhar. |
| Pack | [05-99freelas.md](05-99freelas.md) |
| Google | **PREFER_GOOGLE** — public JS defines `registerFreelancer` + Google OAuth URL. Confirm the button after role select. Do not copy client IDs from HTML into git. |
| Draft artifact | Profile skills + EN (or honest JA) bio. **Keep contact/links out of profile** (Termos). **0 proposals.** |
| KYC stop | Payout / government ID / bank. |
| Do not | Premium R$ 54,90–89,90/mês. Off-platform pay. Invent job totals from homepage marketing. |

Cloudflare: human hold with `holdDurationMs`. Do not automate the challenge.

---

## 8. Desk 6 — Gulp / Randstad Professional

| | |
|---|---|
| Role | **Freelancer**. Not Unternehmen / GULP Corporate / Bewerber jobs board. |
| Entry | https://www.gulp.de/registrieren → Freelancer “Jetzt kostenlos registrieren” → https://www.gulp.de/gulp2/g/neu/experten/registrieren (this GET: JS-required shell). |
| Pack | [06-gulp.md](06-gulp.md) |
| Google | **NOT_OFFERED_OAUTH** on public registrieren HTML (2026-09-16). Email = MAIN mailbox. |
| Draft artifact | Free **GULP Basisprofil**. Leave incomplete/private if offered. **0 applications.** |
| KYC stop | Steuer-ID / ID / bank if a file picker appears. |
| Do not | GULP Membership **120 Euro netto / 6 Monate** or **180 Euro netto / 12 Monate**. Apply to CH / onsite cards (Wallisellen, Zürich, Bern, …). Treat homepage “714 Jobs / 876 Projekte” as marketing. |

Client-side copy “7 Euro Servicegebühr pro Freelancer-Stunde” is **GULP Direkt for companies**, not a seller membership. Do not pay it. Do not invent a freelancer %.

---

## 9. STOP notes (all desks)

Hand **desk name + screen type** to morning. Do not upload. Do not pay.

| Stop | Examples | Code |
|---|---|---|
| KYC / identity | Passport, license, My Number, liveness, bank book, Stripe/Wise onboarding, Fastwork ID+bank | `kyc_wait` |
| Paid plan | Twine Business, 99freelas Premium, GULP Membership, note paid boosts, Fastwork Specialist paywall | `blocked_paid_plan` |
| Publish / bid | note 公開, Braintrust apply, Twine apply, Fastwork Post services, 99freelas proposta, Gulp bewerben | do not click; stay `DRAFT_ONLY` |
| Rate wall | Required JPY/USD/EUR/THB/BRL and placeholder empty | `rate_required` |
| SMS | Phone OTP, user not in chat | `sms_wait_user` |
| Tool | Cloudflare hold with no `holdDurationMs` in schema | `tool_missing_holdDurationMs` |

You may continue the **next** desk only if the browser session is not identity-locked.

---

## 10. Session log

Fill [SESSION-LOG.md](SESSION-LOG.md). No OTP, no ID crops, no passwords.

---

## 11. Prompt stub (future CU agent)

```
Follow earn-wave-d-early-cu-handoff-20260916/CU-PLAY.md exactly.
Serial: note → Braintrust → Twine → Fastwork → 99freelas → Gulp.
MAIN Google preferred. Same MAIN mailbox if a desk has no Google button (Gulp).
DRAFT_ONLY. Stop KYC. No paid plan subscribe.
Fastwork: public start-selling says register with ID and bank — park kyc_wait. Do not upload.
Braintrust: stop at ID-verified / Get Certified / payout bank.
Twine: skip Ari aggregated jobs. 0 applications.
Gulp: free Basisprofil only. Do not apply to onsite CH cards. Do not buy Membership.
Shufti and カイコク: NOTES only. Twago and Xing Projects: SKIP.
No quotes, proposals, applications, or invented traffic/fees.
Gmail OTP: parent Gmail MCP. Do not open Gmail in the CU browser.
SMS OTP: wait in user chat.
Press & Hold: holdDurationMs 1800, one retry 2500.
Live form wins. Do not publish.
```
