> **DRAFT_ONLY.** Money **flags** only.  
> Do **not** invent balances, leftover bids, fee tables, or live USD.  
> No wallet funding from this pack. No contests. No secrets.

# Freelancer.com — money flags (no invented balances)

Pack: `ops/earn/freelancer-surgical-polish-20260916/`  
Desk: Freelancer.com (QUEUE Wave A10 / CU-10)  
Checked: 2026-09-15 public GET of the fees page (no login, no wallet open)

This file names **stop / skip / park** walls. It is not a payment plan, not a wallet dump, and not a bid.

**Cite this URL only. Do not copy amounts into git.**

https://www.freelancer.com/feesandcharges

Re-read that page and the live form immediately before any later human bid. Numbers move. The form in front of you wins. This pack does **not** authorize a top-up.

Related: [BID-TEMPLATES.md](BID-TEMPLATES.md) (do-not-send) · [STOP-KYC.md](STOP-KYC.md) · [PROFILE-PASTE.md](PROFILE-PASTE.md)

---

## Do not invent

Do **not** write into git, chat, or a bid letter:

- A live Site-wallet / account **balance** (including “zero”, “unfunded”, or a guessed minimum)
- Remaining monthly bids / leftover allotment
- Membership, bid-upgrade, verification-application, contest, withdrawal, or commission **amounts**
- A USD quote invented to unblock an empty required rate field
- Employer-side project/contest fees mixed into a seller plan

If a number is required to proceed and git does not already have a **placeholder**, park the desk. Do not fill the gap from memory of the fees page.

---

## Flag table (action, not a price)

| Flag | What you might see on the live desk | Action from this pack | Do not record in git |
|---|---|---|---|
| **Minimum Account Balance / Site wallet** | Bid UI asks you to add funds, hold a balance, or “deposit to continue” before Bid | **STOP.** Do not top up. Do not buy credit. Hand the **screen type** (not the amount) to morning human | Live balance, required minimum, reserved funds |
| **Bid upgrades** | Sponsored / Highlight / Sealed (and similar promote-this-bid checkboxes) | **Skip.** Never a default tactic | Upgrade prices |
| **Membership / Corporate** | Free vs paid plan upsell, extra bids, extra skill slots, cover photo, extra profiles | Stay **free**. Close the upsell. If the control you need is paid-only, **stop** | Plan prices, “extra bids per month” counts |
| **Verified by Freelancer application** | Paid badge / apply-to-verify | **Skip** (also KYC — [STOP-KYC.md](STOP-KYC.md)) | Application / renewal fee |
| **Preferred Freelancer / Recruiter** | Exam, Preferred apply, Recruiter-only row | **Skip.** Do not bid Recruiter-only rows from this pack | Recruiter commission, exam prices |
| **Contest** | Contest entry / prize / guaranteed contest UI | **Do not enter** (including when entry is described as free) | Prize, entry upgrades |
| **Empty required rate** | Form blocks submit until bid amount or hourly is filled | Park `rate_required`. Stop. Do not send | Invented USD |
| **Hourly / bid / delivery fields** | Number fields next to the proposal | Local ledger placeholders only: `{{HOURLY_RATE_USD}}` `{{BID_AMOUNT_USD}}` `{{DELIVERY_DAYS}}` | Live quotes in fenced paste |
| **Off-platform pay** | “Pay me outside”, crypto wallet, mailto for invoice | Decline. Code of Conduct / UA: stay on-site | Bank / wallet addresses |
| **Username change / directory / exams as paid extras** | Optional paid services on the fees page | **Skip** from this pack | Those prices |

User Agreement (https://www.freelancer.com/about/terms): before submitting a bid, a Seller must hold the **Minimum Account Balance** specified on the live Fees & Charges schedule. This pack records that the **rule exists**. It does **not** copy the amount. If the bid UI asks you to fund that balance: **stop**.

---

## What the public freelancer section states (no table)

Opened 2026-09-15 on https://www.freelancer.com/feesandcharges — **qualitative only**:

- Signup, profile, skills, portfolio, notifications, and contest **entry** can be described as free for sellers.
- Bidding is described as free for free members, with a **monthly bid allotment**, and a **minimum account balance** before placing a bid.
- Optional **bid upgrades** exist.
- Awarded work has a seller project/contest **introduction fee** on the live schedule (fixed vs hourly vs contest vs Preferred/Recruiter can differ). **Do not paste those percentages or floors here.**
- **Verified by Freelancer** is a paid application path (also identity). Skip.
- Memberships (free vs paid) exist; stay free.

Exact numbers live only on that URL and on the form. Do not freeze them in this folder.

---

## Allowed money posture (this pack)

- Leave hourly / bid amount **empty in git**
- Keep profile on **free** membership
- Park `rate_required` when the live form demands a number you will not invent
- Stop at wallet funding / KYC / paid upgrade / contest
- After a later human award (not this PR): milestones **on-platform** only; do not underbid to dodge fees

## Forbidden (do not add later either)

- Funding the Site wallet from CU or from this PR
- Recording “we need X to bid” as if it were a GO
- Buying membership, extra bids, Sponsored / Highlight / Sealed, Preferred exam, or Verified application
- Entering contests to “use free entry”
- Copying the fees table into a bid letter or into git
- Off-platform payment instructions

## 日本語（運用だけ）

残高・残り入札・手数料の数字は捏造しない、git にも書かない。ライブは https://www.freelancer.com/feesandcharges と画面。ウォレット入金・有料入札アップグレード・会員課金・コンテストはこのパックからしない。必須金額欄が空なら `rate_required` で止める。
