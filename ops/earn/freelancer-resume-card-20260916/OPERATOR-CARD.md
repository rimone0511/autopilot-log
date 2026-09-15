> **DRAFT_ONLY.** No secrets. No bids. No wallet fund.  
> Resume card only. Authoring agent did **not** sign up, KYC, Bid, or top up.  
> Live form wins. Tick boxes on a **local** copy. Do not commit a filled STATUS.

# OPERATOR-CARD — Freelancer.com username resume (`yutaautomates`)

Pack date: 2026-09-16  
Audience: **parent operator** (祐太), or CU **only after** the live spinner has cleared.  
Desk: Freelancer.com / **Seller** (CU-10 / QUEUE A10)  
Mode: **DRAFT_ONLY.** Park while the spinner spins. Resume later. **Do not Bid. Do not fund.**

This card is the **username step** after a signup wizard spinner. It is not a bid pack, not a wallet how-to, and not a claim that a live account already exists in git.

Google: MAIN only (`{{GOOGLE_ACCOUNT_EMAIL}}`). Do not create a second Freelancer account (Code of Conduct: no multiple accounts).

Full CU order (signup → profile draft → stop) lives on sibling
[`ops/earn/freelancer-cu-handoff-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/freelancer-cu-handoff-ac4d/ops/earn/freelancer-cu-handoff-20260916)
([PR#66](https://github.com/rimone0511/autopilot-log/pull/66)). Do **not** copy that playbook here. Do **not** start those earlier Wave A desks from this card.

---

## Resume fact (operator-supplied — not a live GET)

When the Freelancer username control **already accepted** a handle and then a **spinner** covered the wizard:

| Token | Value | Rule |
|---|---|---|
| Resume username | **`yutaautomates`** | **Already accepted.** Re-use it. Do not pick a retry alias |
| Allowed charset | **letters and numbers only** | Official help: alphanumeric, **starts with a letter**, **16 characters at most** |
| This handle | `yutaautomates` | 13 characters. Starts with `y`. Letters only. No hyphen, underscore, dot, space, or Japanese |

Do not invent a second handle (`yuta-automates`, `yuta_automates`, `yutaautomates1`, brand-as-username). Username is picked **once**. A paid username-change extra on the fees page is **not** this card — skip it.

This line is **not** proof that a seller account exists. Sibling Wave A STATUS still lists Freelancer.com as `pending` until a live CU writes its own box. This pack does not rewrite that box.

---

## Clock (spinner first, then one username, then stop)

| Min | Do | Do not |
|---|---|---|
| 0:00–0:20 | Hard stop. Is the **spinner still on screen**? | Bid. Fund. New Google identity. Mash retry |
| 0:20–0:50 | If spinning: **park**. Local note `spinner_wait`. Close or leave the tab | Type a second username “while it thinks”. Buy a change |
| 0:50–1:30 | If **cleared**: confirm the field still shows **`yutaautomates`** (accepted) | Clear the field. Hyphen / underscore / retry suffix |
| 1:30–2:00 | Continue sibling profile **draft** only if the wizard already moved past username | Place Bid. Contest. Verify my Identity. Wallet top-up |

Stuck > 10 minutes on the spinner after a later resume: park again. Do not invent a bypass.

---

## 0. Hard stop (read before touching Freelancer)

- [ ] This pass is **resume-when-spinner-clears**, not a new signup from this authoring agent.
- [ ] MAIN Google only. Same MAIN mailbox if the live path is Email + Password.
- [ ] Do **not** click **Bid** / **Place Bid** / **Submit bid**.
- [ ] Do **not** fund the Site wallet / Minimum Account Balance.
- [ ] Do **not** enter a contest (including “free to enter”).
- [ ] Do **not** click **Verify my Identity** / keycode selfie / proof of address / security-phone wizard.
- [ ] Do **not** buy membership, extra bids, Sponsored / Highlight / Sealed, Preferred exam, or Verified application.
- [ ] Do **not** buy a **username change**.
- [ ] Do **not** open a second account to “retry” the spinner.
- [ ] Do **not** commit passwords, OTP, phone, ID, or a live wallet / leftover-bid number.

If a wallet, KYC, or paid-upgrade screen appears: close it. Local note the **screen type** only. Stop.

Public entry (desk, not a profile URL):

- Signup: https://www.freelancer.com/signup
- Login: https://www.freelancer.com/login
- Getting started (username rules): https://www.freelancer.com/support/general/how-to-get-started-at-freelancer-com
- Username guidelines: https://www.freelancer.com/support/general/username-guidelines
- Fees (cite URL only; do not copy amounts): https://www.freelancer.com/feesandcharges
- User Agreement: https://www.freelancer.com/about/terms
- Code of Conduct (no multiple accounts): https://www.freelancer.com/info/codeofconduct

---

## 1. Spinner still showing → park

The live control may show a loading spinner while it checks the username. Official help bodies are often a SPA shell — **the live widget wins**.

- [ ] Spinner **visible**: do not type, do not submit, do not pick a fallback handle.
- [ ] Do not refresh in a loop. Do not open a second tab as a new identity.
- [ ] Local note `spinner_wait`. Date it locally. **STOP this pass.**
- [ ] Resume **later** with this same card. Username remains **`yutaautomates`**.

reCAPTCHA / press-and-hold is **not** this spinner. If that wall appears, park `hold_failed` and hand the **screen type** to morning human. Do not invent a bypass. That is still not a Bid or a fund.

---

## 2. Spinner cleared → resume with `yutaautomates`

Operator fact: the username was **already accepted** as `yutaautomates` before the spinner covered the step. Resume that fact. Do not treat a cleared spinner as “pick again.”

Letters / numbers only (public getting-started / username-guidelines; live form wins if it is stricter):

1. **Letters and numbers only** (alphanumeric).
2. **Starts with a letter.**
3. **16 characters at most.**

`yutaautomates` already matches. Do not “improve” it.

- [ ] Logged in / wizard still on MAIN Google (or same MAIN email). Not a second account.
- [ ] Username field still holds **`yutaautomates`**, or you type **exactly** that string once.
- [ ] No hyphen `-`, underscore `_`, dot `.`, space, or non-ASCII.
- [ ] No extra suffix because the spinner “felt like a failure.”
- [ ] Accepted / available / green-check (live label wins): **leave it.** Continue the wizard **Next**.
- [ ] If the field is **empty** after the spinner: type `yutaautomates` **once**. Wait for the new check. Do not spray candidates.
- [ ] If the live check now says **taken / invalid**: **STOP.** Local note `username_rejected_after_spinner`. Do **not** invent `yutaautomates2`. Do **not** buy a username-change extra. Morning human.
- [ ] If the wizard skipped username and you are already inside the seller desk: **do not change** an existing handle from this card. Local note `username_step_already_past`. Continue sibling profile draft only.

---

## 3. After username — still not a bid

Username accepted is **not** “Verified” and **not** permission to Bid.

If the wizard is still in CU-10 profile-draft territory, follow sibling [PR#66](https://github.com/rimone0511/autopilot-log/pull/66) (bodies not copied): headline / summary / skills **save**. Then stop.

From **this** card, after the username step:

- [ ] Role still **Freelancer / seller** if asked. Not Employer.
- [ ] Membership still **free**. Close Plus / extra-slot upsells.
- [ ] **No Bid. No contest. No wallet top-up. No KYC upload.**
- [ ] **STOP** or hand off to the CU playbook. Do not send a surgical letter from here ([PR#68](https://github.com/rimone0511/autopilot-log/pull/68) stays do-not-send).

---

## Out of scope (never this card)

- Creating a new Google / Facebook / second Freelancer identity
- Clicking Bid / Place Bid / leftover-bid spray
- Funding Site wallet / Minimum Account Balance
- Contests, Preferred exam, Verified application
- Verify my Identity / document upload
- Paid username-change request
- Committing `{{PASSWORD_DO_NOT_STORE}}`, OTP, phone, or a live balance
- Rewriting Wave A STATUS / QUEUE boxes
- Copying sibling bid / profile paste bodies into this folder

Sibling packs (bodies **not** copied; paths exist on **those** branches, not on `master`):

| Need | Path (PR branch) | PR |
|---|---|---|
| CU runner (Google/email → profile draft → stop) | `ops/earn/freelancer-cu-handoff-20260916/` | [#66](https://github.com/rimone0511/autopilot-log/pull/66) |
| Profile + Wave B gap notes | `earn-freelancer-waveb-gap-notes-20260916/` | [#19](https://github.com/rimone0511/autopilot-log/pull/19) |
| Surgical-bid templates (do-not-send) | `earn-freelancer-surgical-bid-templates-20260916/` | [#47](https://github.com/rimone0511/autopilot-log/pull/47) |
| Profile/bid polish | `ops/earn/freelancer-surgical-polish-20260916/` | [#57](https://github.com/rimone0511/autopilot-log/pull/57) |
| JOBS bid-ready letters (account must already exist) | `earn-jobs-freelancer-bid-ready-20260916/` | [#68](https://github.com/rimone0511/autopilot-log/pull/68) |
| Wave A STATUS snapshot | `earn-register-status-snapshot-20260916-0519/` | [#49](https://github.com/rimone0511/autopilot-log/pull/49) |
| TODAY apply queue (Freelancer bids only when account exists) | `earn-jobs-apply-queue-today-20260916/` | [#88](https://github.com/rimone0511/autopilot-log/pull/88) |

---

## Local observation (do not commit filled)

```
date_jst:
operator: parent / cu
spinner: still_spinning / cleared / not_checked
username_on_screen: yutaautomates / empty / other / not_checked
username_accepted: yes / no / unknown
letters_numbers_only: yes / no
second_username_tried: no
bid: no
contest: no
wallet_fund: no
kyc_upload: no
username_change_purchased: no
stopped_at: spinner_wait | username_accepted | username_rejected_after_spinner | username_step_already_past | hold_failed | wallet_stop | kyc_wait
next: park | sibling_profile_draft | morning_human
```

---

## Official help (public)

- Getting started (username: alphanumeric, starts with a letter, 16 max): https://www.freelancer.com/support/general/how-to-get-started-at-freelancer-com
- Username guidelines: https://www.freelancer.com/support/general/username-guidelines
- Username change request (do **not** file from this card): https://www.freelancer.com/support/employer/profile/username-change-request
- Fees & Charges (URL only): https://www.freelancer.com/feesandcharges
- Identity Policy (STOP, not a fill guide): https://www.freelancer.com/page.php?p=info%2Fkyc_policy

Help article bodies often fail in a plain GET. **Live counter and spinner win.**

---

## 日本語（運用だけ）

Freelancer のユーザー名スピナーが回っている間は触らない。消えたら **`yutaautomates`**（すでに accepted）。英数字のみ・先頭は文字・16文字以内。ハイフンや別案でリトライしない。入札しない。入金しない。本人確認を上げない。有料のユーザー名変更を買わない。アカウントができたとは git に書かない。
