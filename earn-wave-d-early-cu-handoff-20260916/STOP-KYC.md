# Stop-at-KYC + paid-plan park — Wave D-early KEEP (CU)

Pack: `earn-wave-d-early-cu-handoff-20260916`  
Mode: **`DRAFT_ONLY`**  
Checked: 2026-09-16 public pages / public help. **No marketplace login** from the authoring agent. Re-check labels at click-time. This is not legal advice.

Queue rule: if KYC appears, stop and hand the **desk name** and the **kind of screen** to the morning operator. The agent does not upload documents.

Morning-operator sheet (human only): sibling `earn-kyc-morning-checklist-20260916/`.

Paid-plan rule: **do not subscribe**. Park `blocked_paid_plan`.

Shufti / カイコク are **NOTES only** — do not reach a KYC form from this serial.

---

## Allowed for this pack

### note

- [ ] MAIN Google signup / login (`Googleでログイン` on public `/login` HTML)
- [ ] Email fallback only if Google is missing (`{{EMAIL}}` — still the MAIN mailbox)
- [ ] Draft display name, bio from [01-note.md](01-note.md)
- [ ] One **unpublished** paid-article draft (do not 公開)
- [ ] Do not launch メンバーシップ / 定期購読
- [ ] Do not connect 口座

### Braintrust

- [ ] Talent Join (Google if visible; else MAIN mailbox)
- [ ] English headline / bio / skills
- [ ] Photo of the operator (`{{PROFILE_PHOTO_LOCAL_PATH}}`)
- [ ] Placeholder rate if the wizard blocks — else skip
- [ ] **Stop before Get Certified / ID-verified / AI Skills Interview-for-identity / payout bank**

### Twine

- [ ] Google freelancer signup
- [ ] Portfolio / profile draft, hidden if offered
- [ ] **0 applications** (direct jobs only were the activity proof; still do not apply)
- [ ] Stay on Standard **$0.00 / month**

### Fastwork

- [ ] Open https://fastwork.co/en/start-selling
- [ ] If Google exists, MAIN account
- [ ] **If ID or bank fields appear: stop. Do not upload. Do not “post immediately.”**
- [ ] Do not submit a service for 48h review

### 99freelas

- [ ] `/register` → **Eu quero Trabalhar**
- [ ] Google if the button exists after role select
- [ ] Profile skills + bio. No phone/email/links in profile (Termos)
- [ ] **0 propostas**. No Premium

### Gulp

- [ ] Email signup with MAIN mailbox (no Google OAuth on public HTML 2026-09-16)
- [ ] Free **Basisprofil** fields from [06-gulp.md](06-gulp.md)
- [ ] Leave incomplete / not searchable if offered
- [ ] **0 Bewerbungen**

---

## Hard stop — do not continue

Hand desk + screen type only. Do not save documents in git or chat.

### Identity / KYC (every desk)

- [ ] Government photo ID (passport, driver’s license, My Number card face, national ID, Thai ID)
- [ ] QR-code camera flow that captures the ID
- [ ] Liveness / selfie-with-ID / biometric match
- [ ] Proof of address (utility bill, bank statement, residence record)
- [ ] Visual video call with a reviewer
- [ ] Braintrust **Get Certified / ID-verified** and AI interview if it asks for government ID or a liveness selfie
- [ ] Fastwork **“Register with your ID and bank details for verification”**
- [ ] note / 99freelas / Gulp payout identity
- [ ] Any “verify now or the account is held” banner — **stop and tell morning**

### Tax / payout / bank / ads

- [ ] W-8BEN / VAT ID / My Number / 適格請求書番号 entered into a live payout form from this pack
- [ ] Withdrawal method, bank book, Payoneer, Wise, PayPal payout, IBAN/BIC, Stripe Connect
- [ ] Credit card on file “for verification”
- [ ] Braintrust Payment Processor banking (Site Service Fees terms)

Fill tax/payout later, on a morning-operator pass, after this draft pack is done.

### Paid plans and publish / bid (do not)

**note**

- [ ] 公開 of profile, 有料記事, マガジン, メンバーシップ
- [ ] Invent creator fee % (help-note.com 403 this IP)

**Braintrust**

- [ ] Apply to jobs
- [ ] Complete certification that requires ID
- [ ] Fake US / EU location

**Twine**

- [ ] Business **$139.99 per project**
- [ ] Apply to jobs (including Ari)
- [ ] Un-hide portfolio without a later human decision

**Fastwork**

- [ ] Specialist / boost / BYOB paid
- [ ] Post services for team approval
- [ ] Face-to-face categories

**99freelas**

- [ ] Premium **R$ 54,90 a R$ 89,90 por mês**
- [ ] Turbinar / extra visibility from **R$ 19,90**
- [ ] Send propostas
- [ ] Contact data in profile

**Gulp**

- [ ] **GULP Membership** 120 / 180 Euro netto
- [ ] Apply to projects (especially CH onsite)
- [ ] IT-Haftpflicht checkout

---

## Name / location warning (do not “fix” with fake data)

Keep `{{COUNTRY}}` / `{{CITY}}` honest. Japan is acceptable. Do not spoof US / UK / EU / LATAM / DE / TH / BR location to chase filters.

Profile photo must be a real current photo of the operator (`{{PROFILE_PHOTO_LOCAL_PATH}}`). Logos, cartoons, and other people’s faces are a reject risk. ID crops are KYC — do not use them as the profile photo.

---

## If the wall appears during signup

1. Do not upload.
2. Do not subscribe. Do not pay a badge to skip a wall.
3. Close the ID / checkout flow.
4. Record in the morning note: date, desk, screen type, required vs optional, paid vs free.
5. Mark this pack complete as **draft copy only** (git files still count).
6. You may continue the **next** desk only if the browser session is not identity-locked.

Do not store screenshots that show ID, face, full account email, or OTP.
