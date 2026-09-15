# CU play — A5 Upwork then A6 LinkedIn Services

Audience: computer-use agent. One human operator.  
Mode: **`DRAFT_ONLY`**. Timebox: **15–25 minutes per desk**.  
Serial for **this folder only**:

```
Upwork (profile draft + Catalog unpublished) → LinkedIn Services (Service Page draft)
```

Do not continue into TimeTicket / Contra / other Wave A desks from here. Those stay on the thick runbook.

---

## 0. One-screen GO / NO-GO

| Switch | Value | If you cannot keep it |
|---|---|---|
| Account | MAIN Google `{{GOOGLE_ACCOUNT_EMAIL}}` only | STOP. No second identity. |
| Publish | `DRAFT_ONLY` | STOP. Do not toggle public / submit / post. |
| KYC | Stop. Morning user. No uploads | Hand off. Do not continue that desk. |
| Auto-bid | Off | STOP if you were about to search jobs and apply. |
| Connects | **0 spent** | Do not buy. Do not send proposals. |
| Rates | Placeholders only | Park `rate_required` rather than invent USD. |
| Email OTP | Parent Gmail MCP | Do not open `mail.google.com` in the CU profile. |
| SMS OTP | User chat | Wait. Do not guess. |
| Press & Hold | `holdDurationMs` required | Do not fake a hold with click+sleep. |
| Secrets | Never in git / this log / code screenshots | Redact. |

Viewport: desktop **≥ 1280px**. Do not switch to a phone emulator mid-desk unless the site dead-ends on desktop (record it).

---

## 1. Preflight

1. Confirm you will use **one** browser profile signed into MAIN Google, or a clean profile that will **only** pick that Google account.
2. If a Press & Hold / 長押し / Cloudflare hold appears, the tool call **must** include `holdDurationMs` (start **1800**; one retry **2500**). If the schema has no such field: STOP (`tool_missing_holdDurationMs`).
3. Open [STOP-KYC.md](STOP-KYC.md) mentally. File pickers for ID = close without a file.
4. Paste packs: [01-upwork-profile.md](01-upwork-profile.md), [02-upwork-catalog.md](02-upwork-catalog.md), [03-linkedin-services.md](03-linkedin-services.md). Live form wins if it disagrees.

You will **not**: scrape, like, follow, message buyers, Easy Apply jobs, open Gmail in CU, buy Premium, or operate Autopilot Log posting.

---

## 2. MAIN Google login play

1. Click **Continue with Google** / **Google でログイン** when present.
2. Pick **only** the MAIN account. If the picker shows another user, do not continue.
3. After login, if you land on a **buyer / hire** home: switch to Freelancer / Provide services. If you cannot switch without KYC, stop as KYC.
4. **Already registered** with MAIN Google: do not duplicate. Open the existing seller/profile surface. Still no publish.

OTP:

- Mail code / magic link → **parent Gmail MCP**. CU does not open Gmail.
- SMS → **user chat**. One resend then `sms_wait_user` and park the desk (you may still start the other desk if the session is not locked).

---

## 3. Desk A5 — Upwork

| | |
|---|---|
| Role | **Freelancer. Work and get paid.** Not client. Not Agency. |
| Entry | https://www.upwork.com/ — Sign up / Log in → Continue with **Google** |
| Help | https://support.upwork.com/hc/en-us/articles/24492534968211-Register-as-a-freelancer |
| Google | **PREFER_GOOGLE**. If you Google-signup, always Google-login later. |
| Language | EN name fields. Do not put kanji in First/Last if the form rejects it. Legal name stays accurate. |
| Draft artifact | Profile **in progress**. Catalog project **not submitted**. **0 Connects spent.** |
| KYC stop | Photo ID, facial, payment setup, “verify to submit profile” if that verify is ID. |
| Do not | Buy Connects; boost; send proposals; create Agency; auto-bid. |

### A5 steps

1. Sign in MAIN Google as Freelancer.
2. Fill [01-upwork-profile.md](01-upwork-profile.md). Hourly = `{{HOURLY_USD}}` only. If the box will not save empty, park `rate_required` (still finish Catalog **text** in git; do not invent a number in the live UI).
3. Profile photo: `{{PROFILE_PHOTO_LOCAL_PATH}}` if the form asks and the file is a **real current photo of the operator**, not an ID scan, not a logo.
4. Open Catalog create only after profile fields that **block Catalog** are filled. Paste [02-upwork-catalog.md](02-upwork-catalog.md).
5. **Stop before Submit** (review queue = publish path). Concurrent projects = `1` if asked, then stop.
6. Do **not** open Find Work to send proposals. Proposal text is a different sibling pack and is HANDS-only.

Done codes (pick one): `done-draft` | `already_member_draft` | `kyc_wait` | `sms_wait_user` | `rate_required` | `no_draft_path` | `otp_missing`.

---

## 4. Desk A6 — LinkedIn Services

| | |
|---|---|
| Role | **Services marketplace** on the **existing** LinkedIn for MAIN Google. Not a new LinkedIn. Not **Jobs**. |
| Entry | https://www.linkedin.com/services — **Provide services** / Add services on the **personal** profile |
| Help | https://www.linkedin.com/help/linkedin/answer/a569554 |
| Google | Same LinkedIn as `rimone0511`. If signed out, Google that mailbox. **Do not** create a second LinkedIn. |
| Draft artifact | Service Page fields filled from [03-linkedin-services.md](03-linkedin-services.md), **not published**. Headline edit OK. **No feed post.** |
| SNS | `DRAFT_ONLY`. No share to feed, newsletter, or connection blast. |
| KYC stop | ID for ads wallet, Premium force-pay, verification badge that demands government ID. |
| Do not | Easy Apply; Recruiter; Sales Nav trial card; Company Page services (choice is **not currently reversible** per LinkedIn help). |

### A6 — Save may equal publish

Official personal-profile help: **Save** makes the Service Page **viewable by members**. Mobile copy often says **Publish**. Unpublish exists **after** it was live ([Unpublish help](https://www.linkedin.com/help/linkedin/answer/a1362963)). Save-then-unpublish is still a publish. **Do not.**

| If the live UI… | CU action |
|---|---|
| Has **Save as draft** / unpublished toggle that does **not** list you in Services search | Save draft. Stop. |
| Next confirmation is Save / Publish / “make viewable” | **STOP.** Record `no_draft_path`. Leave the paste in this folder. Do not click. |
| Already-published Service Page from a prior human | Do **not** edit-to-publish more. Do not share to feed. Log `already_member_draft` only if it is **not** newly published by you. |

### A6 steps

1. Confirm the session is the operator’s LinkedIn (name / MAIN mailbox), not a second account.
2. Profile → **Add profile section** → **Add services** (desktop). Do **not** attach to a Company Page.
3. Paste [03-linkedin-services.md](03-linkedin-services.md). Pricing: **Contact for pricing** (do not invent `{{STARTING_HOURLY_USD}}` unless the operator filled it locally **and** the field is optional).
4. Skip Premium media. Decline Premium / Sales Nav / Recruiter trials.
5. Do not click Jobs → Easy Apply. Do not send connection requests. Do not post “I now offer services.”
6. Stop per the Save table above.

---

## 5. Session log

Fill [SESSION-LOG.md](SESSION-LOG.md) or paste the table into the agent summary. No OTP, no ID crops, no passwords.

QUEUE.md `next` → `done-draft` is allowed **without secrets** if that sibling file is in the same checkout. Prefer the session log if QUEUE is on another PR.

---

## 6. Prompt stub (future CU agent)

```
Follow earn-upwork-linkedin-cu-handoff-20260916/CU-PLAY.md exactly.
Desks: Upwork profile + unpublished Catalog, then LinkedIn Services Service Page draft.
MAIN Google only. DRAFT_ONLY. Stop KYC. No auto-bid. 0 Connects. No proposals.
Do not invent rates; use placeholders or park rate_required.
Gmail OTP: parent Gmail MCP. Do not open Gmail in the CU browser.
SMS OTP: wait in user chat.
Press & Hold: holdDurationMs 1800, one retry 2500.
LinkedIn: personal profile Services only. If Save = viewable, stop (no_draft_path).
Do not publish. Do not Easy Apply. Do not share to feed.
```
