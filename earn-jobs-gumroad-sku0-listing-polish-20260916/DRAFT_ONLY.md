# DRAFT_ONLY — SKU-0 listing polish (unpublished)

Pack date: 2026-09-16
Phase: JOBS
Desk: Gumroad
Product: SKU-0 starter intake (form → table → notify)

**This folder is listing paste. It is not a live product.**

No agent session may:

- Click Gumroad **Publish**, **Enable**, or otherwise make the product buyable
- Announce a live `gumroad.com/l/...` URL
- Upload identity documents, selfies, or tax forms
- Add bank / payout details
- Put secrets into git or into a buyer zip
- Claim partnership with n8n, Gumroad, or an AI lab
- Create a **New product** if an unpublished SKU-0 draft already exists

## Allowed for this pack

- [ ] MAIN Google login as `{{GOOGLE_ACCOUNT_EMAIL}}` (already `done-draft` on the queue)
- [ ] Open the **existing unpublished** SKU-0 digital product (do not create a second one)
- [ ] Paste [LISTING-EN.md](LISTING-EN.md) and/or [LISTING-JA.md](LISTING-JA.md)
- [ ] Paste [FAQ-EN.md](FAQ-EN.md) and/or [FAQ-JA.md](FAQ-JA.md) into the description FAQ block
- [ ] Price: **keep $39** if that number is already on the draft; otherwise leave `{{PRICE}}` until a human types a number **locally**
- [ ] Walk [CHECKLIST.md](CHECKLIST.md). Every ship-blocker stays a blocker.
- [ ] Confirm status is unpublished / draft
- [ ] Stop

## Hard stop — do NOT

Publish:

- [ ] Publish / Enable / un-pause the product
- [ ] Turn on a public permalink and treat it as live
- [ ] Attach a buyer zip from an agent browser
- [ ] Post the product to X, note, BOOTH, or a profile as “now on sale”

Payout and KYC:

- [ ] Add bank account, PayPal payout, or stripe-style onboarding beyond viewing the screen
- [ ] Upload government ID, My Number, residence card, selfie, proof of address
- [ ] Submit W-9 / other tax forms (do not claim a US person if that is false)
- [ ] Type tax IDs into git or chat logs

Paid extras:

- [ ] Gumroad paid discover / boosts
- [ ] Custom domain purchase from this pack

Secrets:

- [ ] n8n API keys, webhook secret tokens, Google OAuth client secrets
- [ ] Real `{{TABLE_ID_DO_NOT_COMMIT}}`, customer emails, phone numbers
- [ ] Passwords (`{{PASSWORD_DO_NOT_STORE}}` stays a token)
- [ ] Filled `{{PRICE}}` committed as if it were research

## SKU-1 / SKU-2 / SKU-3

Later SKUs are separate unpublished paste packs. This SKU-0 polish does not
publish them, does not attach their stubs to SKU-0, and does not bundle their
prices into the SKU-0 price box.

## Secrets policy

Listing paste has names and empty secret fields only. If a filled secret appears
in a working copy, delete it before commit and rotate the credential.

## Verification of this PR

Markdown only. Python posting-gate tests are unchanged.
No Gumroad product was published from this agent. No live checkout was created.
No payout method was added.
