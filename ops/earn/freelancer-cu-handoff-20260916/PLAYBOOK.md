> DRAFT_ONLY CU handoff. NO secrets. NO invented credentials. NO live signup from this authoring agent.  
> Human / CU paste only. Live form wins.  
> Desk: Freelancer.com seller (CU-10 / QUEUE A10).  
> Auth: **MAIN Google** (`Continue with Google`). Fallback: same MAIN **email** on the same `/signup` form.  
> This pass: **profile draft only**. Surgical bids = **later**, default **do-not-send**. **No contests.**  
> Stop: **Verify my Identity** / wallet funding / paid upgrade. See [STOP-KYC.md](STOP-KYC.md) · [MONEY-FLAGS.md](MONEY-FLAGS.md).  
> Fields: [FIELD-MAP.md](FIELD-MAP.md). Session box: [STATUS.md](STATUS.md).

# PLAYBOOK — Freelancer.com seller signup (CU-10)

| Key | Value |
|---|---|
| Desk | Freelancer.com / **Freelancer · Seller** (not Employer / Buyer) |
| CU serial | CU-10 (QUEUE **A10**) |
| Mode | **DRAFT_ONLY** |
| Language | **English** profile is enough for a Japan-based operator |
| Google | **MAIN only** — public `/signup` shows **Continue with Google** |
| Email fallback | Same MAIN mailbox on **Email** + **Password** (same page). OTP = parent Gmail |
| Membership | **Free**. Do not buy Plus / membership / extra skill slots |
| This pass | Account (if needed) → headline / summary / skills **draft**. **No Bid. No contest.** |
| Surgical bids | **Later only** — after a later human GO. Not this folder’s submit path |
| `thin_site_skip` | **false** (public pages live 2026-09-16 folder stamp) |
| Authoring session | Public GET / help / Identity Policy / fees URL only. **Did not create an account** |

Sibling packs (bodies **not** copied here; this folder is the CU runner):

| Sibling | Path / PR |
|---|---|
| Profile + gap notes | `earn-freelancer-waveb-gap-notes-20260916/` ([#19](https://github.com/rimone0511/autopilot-log/pull/19)) |
| Surgical-bid templates | `earn-freelancer-surgical-bid-templates-20260916/` ([#47](https://github.com/rimone0511/autopilot-log/pull/47)) |
| Wave A STATUS (live box) | `earn-register-status-snapshot-20260916-0519/` ([#49](https://github.com/rimone0511/autopilot-log/pull/49)) |
| Profile/bid polish | `ops/earn/freelancer-surgical-polish-20260916/` ([#57](https://github.com/rimone0511/autopilot-log/pull/57)) |
| Morning KYC 1枚 | `earn-kyc-morning-checklist-20260916/` ([#4](https://github.com/rimone0511/autopilot-log/pull/4)) |

This playbook is the **step order**. Paste fences live in [FIELD-MAP.md](FIELD-MAP.md). Placeholders stay empty of secrets in git.

Do not jump the Wave A serial. Sibling snapshot still has TimeTicket open, then Contra → Craudia → **this desk**. This folder does not start those earlier desks.

---

## Hard rules (read before the first click)

1. **MAIN Google.** Open [freelancer.com/signup](https://www.freelancer.com/signup). Click **Continue with Google**. Use `{{GOOGLE_ACCOUNT_EMAIL}}` — MAIN mailbox only. Do not invent a new Google account, Facebook identity, or second Freelancer account (Code of Conduct: no multiple accounts).
2. **Email is the same person.** If Google is missing, fails, or the live wizard offers the on-page **Email** / **Password** path instead, use `{{EMAIL}}` = the **same** MAIN mailbox. Password = `{{PASSWORD_DO_NOT_STORE}}`. Never commit it. OTP / verify-link stays in **parent Gmail**. Do not paste codes into git or chat logs.
3. **Seller only.** Choose **Freelancer** / work-and-get-paid if the wizard asks. Do not stay on Employer / hire. If you cannot switch without KYC or a paid wall, **stop**.
4. **Free only.** Stay on free membership. Close Plus / extra bids / extra skill slots / cover-photo unlock / Preferred / Verified upsells. See [MONEY-FLAGS.md](MONEY-FLAGS.md).
5. **DRAFT_ONLY this pass.** Paste headline, summary, skills. Save the profile. Do **not** Bid. Do **not** enter a contest (including “free to enter”). Do **not** Publish a Hire-Me / contest entry.
6. **STOP before identity / wallet.** Do not click **Verify my Identity**. Do not fund the Site wallet / Minimum Account Balance. No how-to beyond [STOP-KYC.md](STOP-KYC.md) and [MONEY-FLAGS.md](MONEY-FLAGS.md).
7. **No credentials in git.** OTP, passwords, backup codes, bank, tax IDs, government numbers, live wallet balances, leftover bid counts — none of those belong in this repo.

Already a member on MAIN: **Log in** (Google MAIN, or Email or Username + password for the same mailbox). Do not open a second account.

---

## Step order

Live wizard order wins if it differs. Timebox: 15–25 minutes. Stuck > 10 minutes on one modal: park and write [STATUS.md](STATUS.md).

### A. Create or open the Free seller account

Public GET 2026-09-15 (no POST): `/signup` shows **Continue with Google**, **Continue with Facebook**, and an on-page **First Name / Last Name / Email / Password** form plus User Agreement + Privacy Policy. Login shows the same Google/Facebook buttons plus **Email or Username**.

| # | Do | Do not |
|---|---|---|
| 1 | Open https://www.freelancer.com/signup (existing member: https://www.freelancer.com/login) | Do not start from a contest, Recruiter, or “hire a freelancer” campaign URL |
| 2 | **Continue with Google** as MAIN `{{GOOGLE_ACCOUNT_EMAIL}}` | Facebook as a new identity. Guest. Incognito second identity. Invented Gmail |
| 3 | OAuth consent: basic profile / email. Deny Gmail-read-all / Drive / Contacts dump | Extra scopes “to finish signup” |
| 4 | Fallback if Google is absent or fails: **Email** `{{EMAIL}}` (same MAIN mailbox), **Password** `{{PASSWORD_DO_NOT_STORE}}`, check live **User Agreement** + **Privacy Policy** | New mailbox. Password in git. Apple path (not on this GET — do not invent it) |
| 5 | OTP / verify-link = **parent Gmail**. Resend at most once | Paste OTP digits into git / STATUS. Open `mail.google.com` unless the live CU has no other way **and** the user already authorized that |
| 6 | reCAPTCHA / hold: wait for the human if it is not a simple checkbox. Press-and-hold: set `holdDurationMs` (example 1800, retry 2500) then park if it still fails | Guess a captcha bypass. Retry until lockout |
| 7 | Role = **Freelancer** / seller. Username `{{FREELANCER_USERNAME}}` once, if asked | Employer. Second username to “retry” |
| 8 | Full name from ledger (`{{FULL_LEGAL_NAME}}` / First + Last). Must be able to match ID **later** | Fake brand as legal name. KYC now |
| 9 | Proceed with **free** membership | Plus / paid plan / extra skill slots / cover photo unlock |

Account exists after step 9 on a typical wizard. That is **not** “Verified” and **not** permission to bid. Stop is still before identity and wallet.

### B. Fill the profile (draft — this pass ends here)

Official help lists **Hourly Rate, Professional Headline, Top Skills, Summary**. Resume blocks may exist. Paste only what the live form asks. Fences: [FIELD-MAP.md](FIELD-MAP.md).

| # | Do | Do not |
|---|---|---|
| 10 | Headline + Summary from FIELD-MAP | Years, GMV, Job Completion Rate, “Preferred”, US/EU spoof |
| 11 | Skills: nearest **live dropdown** names, at or under the **free** cap | Buy extra slots. Invent hidden skill IDs. n8n Expert / Zapier Partner claims |
| 12 | Hourly rate: `{{HOURLY_RATE_USD}}` in the **rate field** only, or empty if allowed | Invent USD in git. Put a rate in the summary letter |
| 13 | Location: Japan / `{{CITY}}` / `{{COUNTRY}}` | Spoof a US/EU flag. Street address in git |
| 14 | Portrait from `{{PROFILE_PHOTO_LOCAL_PATH}}` (local disk, not git) if you add a photo | ID scan, keycode selfie, client private photos |
| 15 | Cover photo / extra profiles: **skip** if the UI says paid membership | Pay to unlock cover / extra profiles |
| 16 | Portfolio / website: public URLs only (`{{PORTFOLIO_URL}}`, `{{GITHUB_REPO_AUTOPILOT}}`). Skip **Publish** on portfolio items | Hire-Me-only items. Unrelated external sites. Email/phone in the profile |
| 17 | **Save** the profile | Bid. Contest. Verify my Identity. Add a card. Fund wallet |

### C. Hard stop (this CU pass)

18. **Do not** open **Verify my Identity**, keycode selfie, proof of address, or Security Phone as part of that wizard ([STOP-KYC.md](STOP-KYC.md)).
19. **Do not** fund the Site wallet / Minimum Account Balance, buy bid upgrades, or enter contests ([MONEY-FLAGS.md](MONEY-FLAGS.md)).
20. **Do not** click Bid / Place Bid / Submit entry. Surgical bids are **later**.
21. Record outcome in [STATUS.md](STATUS.md). Valid stop: `done-draft` or `already_member_draft` or `kyc_wait` / `wallet_stop`.

If the live form **blocks even a draft save** behind identity or a deposit, that is `kyc_wait` or `wallet_stop`. Close. Do not complete it. Morning user.

---

## Surgical bids — later only (parked)

This folder’s CU success line is a **saved profile draft**. It is **not** a bid.

Sibling CU still says: profile + skills; **No bids. No contests. No “Verify my Identity.”** This playbook does **not** override that.

Use bid paste only after a **later human GO**, and only if all of these stay true:

- One listing in the official UI (not a scrape dump, not an API bot)
- `{{ONE_SPECIFIC_DETAIL}}` filled from **that** listing, or **skip**
- Human clicks Bid — nothing in this folder submits
- Live form does **not** demand wallet funding, KYC, or a paid upgrade
- No Sponsored / Highlight / Sealed as a default
- **No contests** (including free entry)
- No leftover-bid spray / “use the monthly allotment”

Templates live in siblings [#47](https://github.com/rimone0511/autopilot-log/pull/47) and [#57](https://github.com/rimone0511/autopilot-log/pull/57). **Do not copy those bodies into this folder.** Do not send from this PR.

---

## Fees (cite only — do not pay, do not copy amounts)

| Claim | Status | Source |
|---|---|---|
| Signup / profile / skills / portfolio can be free | **cited, qualitative** | [Fees & Charges](https://www.freelancer.com/feesandcharges) — re-read live. **Do not copy amounts into git** |
| Bidding described as free with a monthly allotment + a minimum account balance | **cited, qualitative** | Same URL. This pack **does not bid** and **does not fund** |
| Optional bid upgrades exist | **cited, unused** | Same URL. Skip Sponsored / Highlight / Sealed |
| Awarded work has a seller introduction fee | **cited, unused** | Same URL. No award this pass |
| Contest entry may be described as free; contest fee on award | **cited, unused** | Same URL. **Do not enter contests** |
| Verified by Freelancer is a paid application path | **cited, unused** | Same URL + Identity Policy. Skip |
| Hourly number | **placeholder** | Rate field → `{{HOURLY_RATE_USD}}` only. Empty save, else ledger, else `rate_empty` |

Do not freeze fee-table numbers, leftover bid counts, or a live wallet balance in this folder. Walls: [MONEY-FLAGS.md](MONEY-FLAGS.md).

---

## Explicit do-not

- Employer / Buyer workspace instead of Seller
- Continue with Facebook (or any new SNS) as a second identity
- Second Freelancer account
- Plus / membership / extra bids / extra skill slots / cover-photo paywall
- **Verify my Identity** / keycode selfie / proof of address / KYC security-phone
- Site-wallet top-up / Minimum Account Balance funding
- Bid / Place Bid / contest entry (this pass)
- Sponsored / Highlight / Sealed as a tactic
- Preferred Freelancer exam / Recruiter-only rows
- Email, phone, WhatsApp, Telegram, “pay me off-site” in profile or a later bid
- Invented USD, GMV, Job Completion Rate, US/EU location spoof
- That Autopilot Log posts TikTok unattended (inbox upload is the default; direct post is gated)
- Browser automation / scraper / Freelancer API as a bid bot
- This authoring agent POSTing `/signup`

---

## Success line (secret-free)

Valid outcomes: `done-draft` | `already_member_draft` | `kyc_wait` | `wallet_stop` | `sms_wait_user` | `no_draft_path` | `otp_missing` | `hold_failed` | `card_wall` | `oauth_overreach` | `rate_empty`.

Not success: “bid sent,” “contest entered,” “Verified,” “wallet funded,” “Preferred.”

```
desk: Freelancer.com
pack: ops/earn/freelancer-cu-handoff-20260916/
auth: google-main | email-same-mailbox | already_member | blocked
otp: gmail-parent | sms-chat | none | otp_missing | sms_wait_user
kyc: none | wait-morning + verify_my_identity
draft_profile: yes/no
bid: no
contest: no
publish: no
membership: free
pro_upgrade: no
wallet_fund: no
rate: empty | placeholder-from-ledger | rate_empty
holdDurationMs_used: <e.g. 1800 or none>
next: stop
```

Copy the same keys into [STATUS.md](STATUS.md) after a live run. Do not put OTP digits, passwords, ID numbers, a live phone, or a wallet amount there.

---

## URLs (public; re-open before CU)

| What | URL |
|---|---|
| Home | https://www.freelancer.com/ |
| Signup | https://www.freelancer.com/signup |
| Login | https://www.freelancer.com/login |
| Edit profile help | https://www.freelancer.com/support/profile/how-to-edit-your-profile |
| Skills help | https://www.freelancer.com/support/Profile/how-to-edit-your-list-of-skills |
| Portfolio help | https://www.freelancer.com/support/Profile/how-to-add-a-portfolio |
| Fees (URL only — no amounts in git) | https://www.freelancer.com/feesandcharges |
| Identity Policy (STOP, not a fill guide) | https://www.freelancer.com/page.php?p=info%2Fkyc_policy |
| User Agreement | https://www.freelancer.com/about/terms |
| Code of Conduct | https://www.freelancer.com/info/codeofconduct |
| Membership (do not buy) | https://www.freelancer.com/membership |
| Preferred (do not apply) | https://www.freelancer.com/preferred-freelancer-program |
| Bid help (SPA — later GO only) | https://www.freelancer.com/support/freelancer/Project/how-to-bid-1633 |

Support article **bodies** often do not render in a plain GET. Trust the live page + the form counter.

---

## 日本語（運用だけ）

下書きのみ。このエージェントは登録しない。MAIN Google（なければ同じメール）。プロフィール下書きまで。入札・コンテスト・本人確認・ウォレット入金はしない。外科入札は後で、人が GO したときだけ。残高と手数料の数字は捏造しない。
