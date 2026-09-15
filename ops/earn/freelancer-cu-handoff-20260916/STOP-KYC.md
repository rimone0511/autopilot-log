> **DRAFT_ONLY.** Identity stop.  
> Agent does not upload. No ID images, numbers, or selfies in git or chat.  
> Morning human only, and only after an explicit GO.

# STOP-KYC — Freelancer.com

Mode: **DRAFT_ONLY**  
Pack: `ops/earn/freelancer-cu-handoff-20260916/`  
Desk: Freelancer.com (QUEUE Wave A10 / CU-10)  
Date: 2026-09-16  
Policy page (opened 2026-09-15, no login): https://www.freelancer.com/page.php?p=info%2Fkyc_policy

**This file is a stop list.** It does not tell anyone how to pass Verified by Freelancer, which ID to use, which country to pick, or how to attach a bank.

This pack **does not** finish identity. Wallet / identity / payout screens are **out of scope**. CU does not complete KYC. Morning operator owns any later ID work (sibling morning slip [PR#4](https://github.com/rimone0511/autopilot-log/pull/4) if present).

Related: [PLAYBOOK.md](PLAYBOOK.md) · [MONEY-FLAGS.md](MONEY-FLAGS.md) · [FIELD-MAP.md](FIELD-MAP.md) · [STATUS.md](STATUS.md)

---

## Allowed (non-KYC)

- [ ] MAIN Google signup or login (`Continue with Google`), or the same MAIN email if Google is missing
- [ ] Email verification via **parent Gmail** (do not paste codes into git)
- [ ] SMS / phone only if **draft save** is blocked, and only with a number the **user** placed in chat — and only if it is **not** the Identity Policy security-phone step
- [ ] Seller **profile** draft: headline, summary, free-cap skills ([FIELD-MAP.md](FIELD-MAP.md))
- [ ] Portrait photo from a local path (**not** an ID scan)
- [ ] Leave membership on **free**

Not allowed from this pack even after profile paste: bids, contests, wallet funding, Preferred, Verified application.

---

## Hard stop — do not open or complete

Identity / Verified by Freelancer:

- [ ] **Verify my Identity** (policy: Profile → Settings → Account Details → Verify my Identity)
- [ ] Government photo ID (policy lists passport / driver’s license / national ID)
- [ ] ID type / name-on-ID / ID **number** / expiration typed into the wizard
- [ ] Keycode verification photo (face + unique code + ID, side-by-side)
- [ ] Proof of address (utility bills and/or bank statements — policy: two different copies)
- [ ] Security Phone Number **as part of that KYC wizard** (address step may send a code if a Security Phone Number is not set)
- [ ] Pay any “Verified by Freelancer” application fee (live amounts: fees URL only — [MONEY-FLAGS.md](MONEY-FLAGS.md))
- [ ] Apply to Preferred Freelancer (exam + KYC path)
- [ ] Put ID numbers, dates of birth from an ID, addresses from bills, or selfie files in git / chat
- [ ] Falsify a name or country so that a later ID would not match (`{{FULL_LEGAL_NAME}}` must stay honest; still **do not KYC now**)
- [ ] Create a second account to dodge verification (Code of Conduct: no multiple accounts)
- [ ] Send ID photos or a selfie to Support

Payments:

- [ ] Site wallet top-up / Minimum Account Balance funding
- [ ] Bank / PayPal / card “to verify”
- [ ] Withdrawal setup

Publish / commerce:

- [ ] Bid / Place Bid
- [ ] Contest entry
- [ ] Publish a Hire-Me item that the UI treats as a paid unlock

If a phone-SMS step appears: it is **not** an instruction to start ID. If **draft save** is impossible without SMS, only a number the **user** already placed in chat may be used, then stop. If the same step asks for ID, selfie, keycode, or proof of address, treat it as KYC and **stop**.

If the live form **blocks account create** on phone-only (not ID/selfie), park and hand the screen type to morning human. If it is a verification selfie / ID flow, **stop**.

---

## Why we stop here (cite, not a procedure)

- Identity Policy: KYC / Verified by Freelancer asks for government-issued ID, keycode verification, and proof of address.  
  https://www.freelancer.com/page.php?p=info%2Fkyc_policy
- Policy: account details must match the name on the documentation. Failing verification can limit or suspend an account. Falsifying identity is described as a crime. That is a **human** decision, not a CU retry.
- Policy: Freelancer may request identity to uphold the User Agreement; verification may also be requested for payment-gateway checks.
- Review, when someone actually submits, is on Freelancer’s side (policy: business days). This pack never submits.

Do not follow the policy article’s **steps** in this pack. Do not quote its field lists into a CU prompt as “next clicks.” The four official stages exist so you can **recognize the wall**, not complete it:

1. Proof of identity  
2. Keycode verification  
3. Proof of address (+ security phone if unset)  
4. Submit for review  

Help hub titles also exist for KYC / KYC requirements / security phone / location flag. Article bodies often do not render in a plain GET. **Trust the live page.** If the live wizard differs, the wizard wins — still **do not upload**.

---

## If a KYC screen appears

1. Close the dialog. Do not choose a file. Do not continue into the camera / vendor. Do not type an ID number.
2. Leave whatever unpublished draft already saved.
3. Record only: date, desk `Freelancer.com`, screen type (`verify_my_identity` / `photo_id` / `keycode` / `proof_of_address` / `security_phone` / `wallet` / other). No document data.
4. Set outcome `kyc_wait`. Morning user decides.
5. Do not buy Verified / Preferred / membership as a workaround.
6. Do not discuss taking payment off-site to “avoid” verification.

`kyc_wait` is a valid desk outcome. It is not failure.

Do not store screenshots that show ID, face, full account email, or OTP.

## Morning memo (no secrets)

```
date:
desk: Freelancer.com
screen:
saved_draft: yes/no/unknown
kyc_shown: yes/no
upload: none
membership: free
bid: no
contest: no
wallet_fund: no
next: morning-user | park | next-desk
```

## 日本語（運用だけ）

本人確認は上げない。免許・パスポート・keycode 自撮り・公共料金／明細は git にもチャットにも置かない。画面の種類だけ朝へ。有料の Verified 申請も Preferred もこのパックからはしない。
