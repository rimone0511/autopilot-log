# STOP-KYC — Contra Independent

Mode: **DRAFT_ONLY**  
Pack: `ops/earn/contra-cu-handoff-20260916/`  
Date: 2026-09-16

**This file is a stop list.** It does not tell anyone how to pass Persona, which ID to use, which country to pick, or how to attach a bank.

Official help says Independents complete **Verify identity & set up your wallet** to finish the Discoverable checklist. This pack **does not** finish that checklist. Wallet / identity / payout screens are **out of scope**.

CU does not complete KYC. Morning operator owns any later ID work (sibling morning slip if present).

---

## Allowed (non-KYC)

- [ ] MAIN Google signup or login (`Continue with Google`), or the same MAIN email if Google is missing
- [ ] Email verification via **parent Gmail** (do not paste codes into git)
- [ ] Independent **Share work** + **Free** plan
- [ ] One-liner, About ≤400, public URLs, Discoverable **off**
- [ ] Case study / service **draft or unpublished** only

---

## Hard stop — do not open or complete

Identity / wallet / payout:

- [ ] Wallet page
- [ ] **Add account** / **Add an account**
- [ ] Persona (or any identity vendor by another name)
- [ ] Government photo ID, selfie, liveness
- [ ] National ID / tax numbers (W-8, SSN, EIN, My Number, …)
- [ ] Bank, PayPal, USDC, Payoneer, Airwallex, debit card payout
- [ ] Expert verification that demands government ID
- [ ] Support mail that asks for proof of residence, lease, utility bill, or ID (including country-change)

Paid plan / card:

- [ ] Contra Pro / Max
- [ ] Add a card “to verify” or to waive fees

Publish / commerce:

- [ ] Publish to feed
- [ ] Publish a service
- [ ] Apply / invoice / paid project / payment link

If a phone-SMS step appears: it is **not** an instruction to start ID. If **draft save** is impossible without SMS, only a number the **user** already placed in chat may be used, then stop. If the same step asks for ID, selfie, or a paid ID vendor, treat it as KYC and **stop**.

---

## Why we stop here (cite, not a procedure)

- Completing Independent profile, last listed item = **Verify identity & set up your wallet**  
  https://help.contra.com/en/articles/9322381-onboarding-and-completing-your-profile
- Help titles that name Wallet / Persona exist. Opening them is **in scope for STOP**, not for fill:  
  https://help.contra.com/en/articles/9322950-your-contra-wallet  
  https://help.contra.com/en/articles/9322955-how-to-verify-your-identity-on-contra

Do not follow those articles’ steps in this pack. Do not quote their field lists into a CU prompt as “next clicks.”

---

## If a KYC screen appears

1. Close the dialog. Do not choose a file. Do not continue into the vendor.
2. Leave whatever unpublished draft already saved.
3. Record only: date, desk `Contra`, screen type (`wallet` / `persona` / `photo_id` / `selfie` / `bank` / `tax` / other). No document data.
4. Set outcome `kyc_wait`. Morning user decides.
5. Do not buy Pro as a workaround.

`kyc_wait` is a valid desk outcome. It is not failure.

Do not store screenshots that show ID, face, full account email, or OTP.

## Morning memo (no secrets)

```
date:
desk: Contra
screen:
saved_draft: yes/no/unknown
kyc_shown: yes/no
upload: none
pro_upgrade: no
publish: no
next: morning-user | park | next-desk
```
