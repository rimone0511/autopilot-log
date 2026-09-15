# CU play-order — Wave D-early KEEP (serial only)

Audience: computer-use agent. One human operator.  
Mode: **`DRAFT_ONLY`**. Timebox: **15–25 minutes per KEEP desk**.  
This PR: **markdown only. No marketplace login. No signup.**

Serial for **KEEP six from [PR#42](https://github.com/rimone0511/autopilot-log/pull/42)** (PR#22 operator order). Not INDEX CU. **Do not invent CU-29+.**

```
note → Braintrust → Twine → Fastwork → 99freelas → Gulp
```

Do **not** continue into Shufti, カイコク, Twago, Xing, Wave A, or Wave B from here.

Paste bodies are **not** in this folder. Open the pack path, fill from it, **live form wins**.

---

## Pack paths (PR#42 — do not paste here)

Root: `earn-wave-d-early-cu-handoff-20260916/`  
Branch (until merge): `cursor/earn-wave-d-early-cu-handoff-9adc`

| Play | Desk | QUEUE | Gate | Pack path |
|---|---|---|---|---|
| 1 | note | C4 | **alive** | `earn-wave-d-early-cu-handoff-20260916/01-note.md` |
| 2 | Braintrust | C8 | **alive** | `earn-wave-d-early-cu-handoff-20260916/02-braintrust.md` |
| 3 | Twine | D3 | **alive** | `earn-wave-d-early-cu-handoff-20260916/03-twine.md` |
| 4 | Fastwork | D6 | **alive** | `earn-wave-d-early-cu-handoff-20260916/04-fastwork.md` |
| 5 | 99freelas | gate add | **alive** | `earn-wave-d-early-cu-handoff-20260916/05-99freelas.md` |
| 6 | Gulp | gate add | **alive** | `earn-wave-d-early-cu-handoff-20260916/06-gulp.md` |

GitHub (same files):

- [01-note.md](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-wave-d-early-cu-handoff-9adc/earn-wave-d-early-cu-handoff-20260916/01-note.md)
- [02-braintrust.md](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-wave-d-early-cu-handoff-9adc/earn-wave-d-early-cu-handoff-20260916/02-braintrust.md)
- [03-twine.md](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-wave-d-early-cu-handoff-9adc/earn-wave-d-early-cu-handoff-20260916/03-twine.md)
- [04-fastwork.md](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-wave-d-early-cu-handoff-9adc/earn-wave-d-early-cu-handoff-20260916/04-fastwork.md)
- [05-99freelas.md](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-wave-d-early-cu-handoff-9adc/earn-wave-d-early-cu-handoff-20260916/05-99freelas.md)
- [06-gulp.md](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-wave-d-early-cu-handoff-9adc/earn-wave-d-early-cu-handoff-20260916/06-gulp.md)

Also in that folder (read, do not copy): `CU-PLAY.md` (thick handoff), `STOP-KYC.md` (full list), `SESSION-LOG.md` (secret-free template), `NOTES-shufti.md`, `NOTES-kaikoku.md`, `SKIP.md`.

This-folder KYC sheet: [STOP-KYC.md](STOP-KYC.md) (one-pager).

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
| Traffic / GMV / fees | Do not invent | Use pack `worker_fee_public` / `unknown` only. |
| Email OTP | Parent Gmail MCP | Do not open `mail.google.com` in the CU profile. |
| SMS OTP | User chat | Wait. Do not guess. |
| Press & Hold | `holdDurationMs` required | Do not fake a hold with click+sleep. |
| Secrets | Never in git / this log / code screenshots | Redact. |
| Shufti / カイコク | NOTES only (PR#42) | Do not open signup. |
| Twago / Xing | SKIP (PR#42 `SKIP.md`) | Close if opened by mistake. |

Viewport: desktop **≥ 1280px**. One desk per loop. Do not parallelize logins.

---

## 1. Preflight

1. One browser profile: MAIN Google only (or a clean profile that will pick only that account).
2. Press & Hold / 長押し / Cloudflare: tool call **must** include `holdDurationMs` (start **1800**; one retry **2500**). Schema missing that field → STOP (`tool_missing_holdDurationMs`).
3. Open [STOP-KYC.md](STOP-KYC.md). File pickers for ID / bank book = close without a file.
4. Confirm the six pack files above exist (PR#42 branch or a local checkout). If a pack file is missing, **park** that desk (`pack_missing`) and continue the next KEEP desk. Do not invent paste copy.
5. PR#42 authoring used **public GET only**. Click-time labels may differ. WAF (Cloudflare) is expected on help-note.com and `/register/freelancer`.

You will **not** (this play or this git PR): scrape, like, follow, message buyers, send quotes, apply, open Gmail in CU, subscribe, upload ID, complete marketplace signup from the authoring agent, or operate Autopilot Log posting.

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
| Pack | `earn-wave-d-early-cu-handoff-20260916/01-note.md` |
| Role | Creator. Not 法人プラン sales. |
| Entry | https://note.com/signup — if SPA empty, https://note.com/login then 会員登録はこちら |
| Google | **PREFER_GOOGLE** (`/login` `Googleでログイン`; confirm `/signup` at click-time) |
| Draft | Profile + **unpublished** paid-article. Membership **not launched**. |
| Stop | 口座・振込・本人確認 → [STOP-KYC.md](STOP-KYC.md) |
| Do not | 公開 / 有料マガジン公開 / invent help-note.com fees (Cloudflare 403) |

Fill **from the pack**. Do not paste the pack into this file.

Done: `done-draft` \| `already_member_draft` \| `kyc_wait` \| `sms_wait_user` \| `rate_required` \| `otp_missing` \| `pack_missing`.

---

## 4. Desk 2 — Braintrust (C8)

| | |
|---|---|
| Pack | `earn-wave-d-early-cu-handoff-20260916/02-braintrust.md` |
| Role | Talent. Not client / Book a Demo. |
| Entry | https://www.usebraintrust.com/for-talent → Join → https://app.usebraintrust.com/auth/sign_up/goals |
| Google | **needs_check** (app auth SPA). Google if visible; else MAIN mailbox. |
| Draft | Profile / skills / EN bio from the pack. |
| Stop | Get Certified / ID-verified / AI interview-for-identity / Stripe-Wise |
| Do not | Apply to `/jobs`. Fake US location. Treat “2M+ / 10K+” as marketing. |

If the only Save makes the profile searchable and there is no incomplete/hidden state → `no_draft_path`.

---

## 5. Desk 3 — Twine (D3)

| | |
|---|---|
| Pack | `earn-wave-d-early-cu-handoff-20260916/03-twine.md` |
| Role | Freelancer / Find work. Not Hire an Expert. |
| Entry | https://www.twine.net/signup |
| Google | **PREFER_GOOGLE** (signup JS `signingUpViaGoogle`; confirm visible button at click-time) |
| Draft | Portfolio / profile draft. **0 applications.** |
| Stop | ID / payout / card-for-identity |
| Do not | Apply to **Ari** aggregated jobs. Buy Business **$139.99/project**. Invent a freelancer % (public “from 5%” is **client** copy). |

---

## 6. Desk 4 — Fastwork (D6) — **KYC likely at signup**

| | |
|---|---|
| Pack | `earn-wave-d-early-cu-handoff-20260916/04-fastwork.md` |
| Role | Freelancer. Online categories only. |
| Entry | https://fastwork.co/en/start-selling (`/en/signup` and `/en/login` were **404** SPA on the pack GET) |
| Google | **needs_check**. No Continue-with-Google label on that public HTML. |
| Draft | **Often none.** Public copy: register with **ID and bank**. If that form appears → `kyc_wait`. Do not upload. Do not post services (48h team approval = publish). |
| Stop | National ID + bank at register |
| Do not | Face-to-face TH cats. Specialist / BYOB. Invent seller commission (unread). |

---

## 7. Desk 5 — 99freelas

| | |
|---|---|
| Pack | `earn-wave-d-early-cu-handoff-20260916/05-99freelas.md` |
| Role | **Eu quero Trabalhar**. Not Contratar. |
| Entry | https://www.99freelas.com.br/register (`/register/freelancer` Cloudflare **403** on the pack GET — start at `/register`, pick Trabalhar) |
| Google | **PREFER_GOOGLE** after role select. Do not copy OAuth client IDs from HTML into git. |
| Draft | Skills + bio from the pack. **No contact/links in profile** (Termos). **0 proposals.** |
| Stop | Payout / government ID / bank |
| Do not | Premium R$ 54,90–89,90/mês. Off-platform pay. Invent job totals. Fake native-PT fluency. |

Cloudflare: human hold with `holdDurationMs`. Do not automate the challenge.

---

## 8. Desk 6 — Gulp / Randstad Professional

| | |
|---|---|
| Pack | `earn-wave-d-early-cu-handoff-20260916/06-gulp.md` |
| Role | **Freelancer**. Not Unternehmen / GULP Corporate / Bewerber jobs board. |
| Entry | https://www.gulp.de/registrieren → Freelancer “Jetzt kostenlos registrieren” → https://www.gulp.de/gulp2/g/neu/experten/registrieren |
| Google | **NOT_OFFERED_OAUTH** on public registrieren HTML (2026-09-16). Email = MAIN mailbox. |
| Draft | Free **GULP Basisprofil**. Leave incomplete/private if offered. **0 applications.** |
| Stop | Steuer-ID / ID / bank if a file picker appears |
| Do not | Membership **120 / 180 Euro netto**. Apply to CH / onsite cards. Pay “7 Euro Servicegebühr” (that copy is **GULP Direkt for companies**). |

---

## 9. After each desk

Fill the secret-free table in  
`earn-wave-d-early-cu-handoff-20260916/SESSION-LOG.md`  
([template](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-wave-d-early-cu-handoff-9adc/earn-wave-d-early-cu-handoff-20260916/SESSION-LOG.md)).  
Do not commit OTP, ID crops, passwords, or a second copy of that template here.

Then open the **next** KEEP desk in the serial. After Gulp: **stop this play**.

---

## 10. Prompt stub (future CU agent)

```
Follow earn-wave-d-early-play-order-20260916/CU-PLAY.md exactly.
Serial: note → Braintrust → Twine → Fastwork → 99freelas → Gulp.
Paste from earn-wave-d-early-cu-handoff-20260916/ (PR#42). Do not invent pack copy.
MAIN Google preferred. Same MAIN mailbox if a desk has no Google button (Gulp).
DRAFT_ONLY. Stop KYC (see this folder STOP-KYC.md). No paid plan subscribe. No signup from authoring.
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
