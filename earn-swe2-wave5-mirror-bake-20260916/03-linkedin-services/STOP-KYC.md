# Stop-at-KYC — Upwork + LinkedIn Services (CU)

Pack: `earn-upwork-linkedin-cu-handoff-20260916`  
Mode: **`DRAFT_ONLY`**  
Checked: 2026-09-15 public help (no account, no uploads). Re-check labels at click-time. This is not legal advice.

Queue rule (Wave A): if KYC appears, stop and hand the **desk name** and the **kind of screen** to the morning operator. The agent does not upload documents.

Morning-operator sheet (human only): sibling `earn-kyc-morning-checklist-20260916/`. A6 LinkedIn is often **not** a same-morning KYC desk; still stop if ID appears.

---

## Allowed for this pack

### Upwork

- [ ] MAIN Google signup / login as Freelancer (`{{GOOGLE_ACCOUNT_EMAIL}}`)
- [ ] Email fallback only if Google is missing (`{{EMAIL}}` — still the MAIN mailbox)
- [ ] Phone SMS / call **code** if account-create requires it (not a document)
- [ ] Draft profile fields from [01-upwork-profile.md](01-upwork-profile.md)
- [ ] Fill Catalog copy from [02-upwork-catalog.md](02-upwork-catalog.md)
- [ ] Stop before **Create Project → Submit**
- [ ] **0 Connects**

### LinkedIn Services

- [ ] Same existing LinkedIn as MAIN Google (no second account)
- [ ] Open **Add services** on the **personal** profile
- [ ] Fill [03-linkedin-services.md](03-linkedin-services.md)
- [ ] Stop before Save if Save = viewable (`no_draft_path`)
- [ ] Decline Premium / Sales Nav / Recruiter / ads wallet

---

## Hard stop — do not continue

Hand desk + screen type only. Do not save documents in git or chat.

### Identity / KYC (both desks)

- [ ] Government photo ID (passport, driver’s license, My Number card face, national ID)
- [ ] QR-code camera flow that captures the ID
- [ ] Liveness / selfie / short video to match the profile photo
- [ ] Proof of address (utility bill, bank statement, residence record)
- [ ] Visual video call with a reviewer
- [ ] LinkedIn verification badge that demands government ID
- [ ] Upwork optional **identity verification badge** (public help: 35 Connects — **do not buy**)
- [ ] Any “verify now or the account is held” banner — **stop and tell morning**; do not upload to dismiss it from this pack

Public Upwork help (2026-09-15, sibling Catalog pack): after a required verify notice you may have seven days, or the account may be put on hold. That is a reason to **escalate**, not a reason for this pack to upload ID.

### Tax / payout / bank / ads

- [ ] W-8BEN or other tax form if it asks for My Number, residence-card scans, or ID images
- [ ] Withdrawal method, bank, Payoneer, Wise, Stripe identity
- [ ] Credit card on file “for verification” or LinkedIn ads billing
- [ ] LinkedIn Premium / Sales Navigator / Recruiter **trial that requires a card**

Fill tax/payout later, on a morning-operator pass, after this draft pack is done.

### Marketplace actions that count as publish, paid, or bidding

**Upwork**

- [ ] **Submit** a Project Catalog listing (review queue = publish path)
- [ ] Boost a project / buy keyword boost
- [ ] Buy Connects
- [ ] Send a proposal, Boosted Proposal, or accept an interview
- [ ] Turn on consultations
- [ ] Auto-bid / “easy apply” / job RSS apply / any apply loop
- [ ] Create an Agency
- [ ] Put phone, email, or a “contact me at” URL in any Catalog or profile box

**LinkedIn**

- [ ] Save / Publish Service Page when that makes it viewable (unless a true draft control exists)
- [ ] Share to feed, notify network, newsletter, article
- [ ] Easy Apply Jobs; Open-to-work campaign
- [ ] Connection blast / InMail sequence / scraper
- [ ] Company Page services (locked choice)

---

## Name match warning (do not “fix” with fake data)

Public Upwork help: the name on the ID, the withdrawal method, and tax info must match. Country on the ID must match the profile. Japan is acceptable. Do not spoof a US location to chase U.S.-only jobs.

Profile photo must be a real current photo of the operator (`{{PROFILE_PHOTO_LOCAL_PATH}}`). Logos, cartoons, and other people’s faces are a reject risk. ID crops are KYC — do not use them as the profile photo.

---

## If the wall appears during signup

1. Do not upload.
2. Do not pay Connects for a badge. Do not start LinkedIn Premium to skip a wall.
3. Close the ID flow.
4. Record in the morning note: date, desk (`Upwork` / `LinkedIn Services`), screen type, required vs optional badge.
5. Mark this pack complete as **draft copy only** (git files still count).
6. You may continue the **other** desk only if the browser session is not identity-locked.

Do not store screenshots that show ID, face, full account email, or OTP.
