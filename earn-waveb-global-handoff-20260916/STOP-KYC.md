# Stop-at-KYC + paid-plan park — Wave B GLOBAL (CU)

Pack: `earn-waveb-global-handoff-20260916`  
Mode: **`DRAFT_ONLY`**  
Checked: 2026-09-15 public pages / public help. **No marketplace login** from the authoring agent. Re-check labels at click-time. This is not legal advice.

Queue rule (Wave B): if KYC appears, stop and hand the **desk name** and the **kind of screen** to the morning operator. The agent does not upload documents.

Morning-operator sheet (human only): sibling `earn-kyc-morning-checklist-20260916/`.

Paid-plan rule: **do not subscribe**. Especially **PeoplePerHour Basic (annual)**. Park `blocked_paid_plan`.

---

## Allowed for this pack

### Guru.com

- [ ] MAIN Google signup / login as Freelancer (`{{GOOGLE_ACCOUNT_EMAIL}}`)
- [ ] Email fallback only if Google is missing (`{{EMAIL}}` — still the MAIN mailbox)
- [ ] Draft Screen Name, tagline, bio, Work Terms from [01-guru.md](01-guru.md)
- [ ] Draft **one** Service with placeholder rates
- [ ] Stay on **free Basic**. Close upgrade screens.
- [ ] Profile **Hidden** if the control exists

### Malt.com

- [ ] Freelancer account (Google if the button exists; else MAIN mailbox)
- [ ] English headline, bio (≥200 characters), skills, category/job
- [ ] Photo of the operator (`{{PROFILE_PHOTO_LOCAL_PATH}}`)
- [ ] Placeholder day rate `{{DAILY_RATE_EUR}}`
- [ ] Charter checkbox if it is not a document upload
- [ ] Stop at legal-document validation

### Workana

- [ ] Google (or email) talent/freelancer signup
- [ ] Email confirm via parent Gmail MCP
- [ ] SMS OTP if required to store the draft (not a document)
- [ ] Photo, English bios, skills, rate placeholder
- [ ] Free (not paid) skills test
- [ ] **Keep my profile public** OFF
- [ ] Leave incomplete rather than feeding KYC

### Freelancermap

- [ ] Email signup with MAIN mailbox (no Google OAuth on public HTML 2026-09-15)
- [ ] Activation link via parent Gmail MCP
- [ ] Draft profile fields from [05-freelancermap.md](05-freelancermap.md)
- [ ] Stay on **free Basic**
- [ ] Leave profile inactive / private / anonymous if offered
- [ ] **0 applications**

### PeoplePerHour

- [ ] Google freelancer register (`Continue with GOOGLE` on public register HTML)
- [ ] Email verify
- [ ] Draft application fields + real photo
- [ ] Save Offer copy **in this pack only**
- [ ] **Stop if the next button is a paid subscription**

---

## Hard stop — do not continue

Hand desk + screen type only. Do not save documents in git or chat.

### Identity / KYC (every desk)

- [ ] Government photo ID (passport, driver’s license, My Number card face, national ID)
- [ ] QR-code camera flow that captures the ID
- [ ] Liveness / selfie-with-ID / biometric match (Guru photo-for-ID, Malt facial-recognition **for documents**, Freelancermap **Persona / SILT**, PPH Payments upload)
- [ ] Proof of address (utility bill, bank statement, residence record)
- [ ] Visual video call with a reviewer
- [ ] Guru **ID Verification** (official help: documents + credit-card micro-charge + **4.95 USD** fee — KYC **and** paid)
- [ ] Malt **validate legal documents** / AML-CTF (passport, company registry, VAT submit, URSSAF, INPI, UBO)
- [ ] Workana payment verification that asks for government ID images (including WhatsApp ID send)
- [ ] Freelancermap **Verify profile** (public pricing: €50/year Premium members, €75/year Basic — paid identity)
- [ ] Any “verify now or the account is held” banner — **stop and tell morning**; do not upload to dismiss it from this pack

### Tax / payout / bank / ads

- [ ] W-8BEN / VAT ID / My Number entered into a live payout form from this pack
- [ ] Withdrawal method, bank, Payoneer, Wise, PayPal payout, IBAN/BIC, SEPA
- [ ] Credit card on file “for verification” or membership checkout
- [ ] Guru random ≤10 USD card charge for ID

Fill tax/payout later, on a morning-operator pass, after this draft pack is done.

### Paid plans and publish / bid (do not)

**PeoplePerHour (strict)**

- [ ] Subscribe to **PPH Basic** (public Terms: non-refundable **annual** subscription, monthly or prepaid)
- [ ] Subscribe to **TopAccess**
- [ ] Extra proposal credits, featured Offers, Fast-Track document review, qualifying-period extension
- [ ] Post an Offer / send proposals if gated on a plan

**Guru**

- [ ] Upgrade Basic → Basic+ / Professional / Business / Executive
- [ ] Buy extra quotes, Premium Quotes, Sales Messages, featured ranking
- [ ] Send a live Quote
- [ ] Un-hide the profile for search without a later human decision

**Malt**

- [ ] Boost / Super Malter / any paid visibility
- [ ] Second account for a second profession
- [ ] Fake EU work cities

**Workana**

- [ ] **Priority Moderation**
- [ ] Check “Keep my profile public”
- [ ] Send proposals or chat pitches
- [ ] Put phone, email, or off-platform links in About

**Freelancermap**

- [ ] **Premium** (public pricing starts €13.99/month, billed annually)
- [ ] Profile verification purchase
- [ ] Apply to projects / use up the Basic application contingent
- [ ] Activate a public searchable profile if the only next step is apply-ready publish

---

## Name / location warning (do not “fix” with fake data)

Keep `{{COUNTRY}}` / `{{CITY}}` honest. Japan is acceptable. Do not spoof US / UK / EU / LATAM / DE location to chase filters.

Profile photo must be a real current photo of the operator (`{{PROFILE_PHOTO_LOCAL_PATH}}`). Logos, cartoons, and other people’s faces are a reject risk. ID crops are KYC — do not use them as the profile photo.

---

## If the wall appears during signup

1. Do not upload.
2. Do not subscribe (especially PPH Basic annual). Do not pay a badge to skip a wall.
3. Close the ID / checkout flow.
4. Record in the morning note: date, desk, screen type, required vs optional, paid vs free.
5. Mark this pack complete as **draft copy only** (git files still count).
6. You may continue the **next** desk only if the browser session is not identity-locked.

Do not store screenshots that show ID, face, full account email, or OTP.
