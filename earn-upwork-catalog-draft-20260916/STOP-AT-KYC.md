# Stop-at-KYC -- Upwork Catalog pack

Desk: Upwork (freelancer + Project Catalog)
Pack: `earn-upwork-catalog-draft-20260916`
Mode: DRAFT ONLY
Checked: 2026-09-15 from public help (no account, no uploads)

Official identity help (read at click-time; do not treat this file as legal advice):

- Identity verification: https://support.upwork.com/hc/en-us/articles/360001176427-How-to-verify-your-identity-as-a-freelancer
- Government ID: https://support.upwork.com/hc/en-us/articles/360000563227-How-to-verify-your-identity-with-a-government-ID
- ID + proof of address: listed in the same help section as a sibling article
- Phone number: listed in the same help section as a sibling article
- Optional identity badge: 35 Connects -- **do not buy**

Queue rule (Wave A): if KYC appears, stop and hand the screen to the **morning operator**.
The agent does not upload documents.

## Allowed for this pack

- [ ] MAIN Google signup / login as Freelancer (`{{GOOGLE_ACCOUNT_EMAIL}}`)
- [ ] Email fallback only if Google is missing (`{{EMAIL}}` -- still the MAIN mailbox)
- [ ] Phone SMS / call **code** if the account-create wall requires it (not a document)
- [ ] Draft profile fields with placeholders (name, title, overview kept local)
- [ ] Save Catalog copy in this folder
- [ ] Stop before **Create Project → Submit**

## Hard stop -- do not continue

Hand the desk name and the **kind of screen** (ID / selfie / tax / bank / submit) to the morning operator. Do not save documents in git or chat.

### Identity / KYC

- [ ] Government photo ID (passport, driver's license, My Number card face, national ID)
- [ ] QR-code camera flow that captures the ID
- [ ] Liveness / selfie / short video to match the profile photo
- [ ] Proof of address (utility bill, bank statement, residence record)
- [ ] Visual video call with an Upwork reviewer
- [ ] Optional **identity verification badge** (35 Connects)
- [ ] Any "verify now or the account is held in seven days" banner -- **stop and tell the morning operator**; do not upload to dismiss it from this pack

Public help (2026-09-15): after a required verify notice you have seven days, or the account may be put on hold. Not verifying can block proposals, direct-hire accepts, and withdrawals. That is a reason to **escalate**, not a reason for this pack to upload ID.

### Tax / payout / bank (not Catalog copy)

- [ ] W-8BEN or other tax form if it asks for My Number, residence-card scans, or ID images
- [ ] Withdrawal method, bank, Payoneer, Wise, or similar
- [ ] Credit card on file "for verification"

Fill tax/payout later, on a morning-operator pass, after this draft pack is done.

### Catalog / marketplace actions that count as publish or paid

- [ ] **Submit** a Project Catalog listing (review queue = publish path)
- [ ] Boost a project / buy keyword boost
- [ ] Buy Connects
- [ ] Send a proposal or accept an interview
- [ ] Turn on consultations
- [ ] Share the project URL off-platform
- [ ] Put phone, email, or a "contact me at" URL in any Catalog box

## Name match warning (do not "fix" with fake data)

Public help: the name on the ID, the withdrawal method, and tax info must match.
Country on the ID must match the profile. Japan is acceptable. Do not spoof a US
location to chase U.S.-only jobs.

Profile photo must be a real current photo of the operator (`{{PROFILE_PHOTO_LOCAL_PATH}}`).
Logos, cartoons, and other people's faces are a reject risk.

## If the wall appears during signup

1. Do not upload.
2. Do not pay Connects for a badge.
3. Close the ID flow.
4. Record in the morning note: date, desk `Upwork`, screen type, whether it was required vs optional badge.
5. Mark this pack complete as **draft copy only**.
