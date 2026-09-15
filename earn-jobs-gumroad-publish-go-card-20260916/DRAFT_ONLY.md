# DRAFT_ONLY — SKU-0 Publish GO card (unpublished)

Pack date: 2026-09-16
Phase: JOBS
Desk: Gumroad
Product: SKU-0 starter intake (form → table → notify)

**This folder is a parent GO card. It is not a live product.**

Default: **do not publish.** `GO: NO` in [GO.md](GO.md) is not a suggestion.

No agent session may:

- Click Gumroad **Publish**, **Enable**, or otherwise make the product buyable
- Announce a live `gumroad.com/l/...` URL
- Upload identity documents, selfies, or tax forms
- Add bank / payout details
- Put secrets into git or into a buyer zip
- Claim partnership with n8n, Gumroad, or an AI lab
- Create a **New product** if an unpublished SKU-0 draft already exists
- Treat “files attached + price $39” as a go-live

## Allowed for this pack

- [ ] MAIN Google login as `{{GOOGLE_ACCOUNT_EMAIL}}` (already `done-draft` on the queue)
- [ ] Open the **existing unpublished** SKU-0 digital product (do not create a second one)
- [ ] Look at Content-tab files (attached?). Do not upload. Do not download secrets.
- [ ] Look at price: expect **$39** already on the draft. Do not change it from this card.
- [ ] Confirm **unpaid draft** (unpublished; payout not this pass)
- [ ] Write local GO = **NO** using [GO.md](GO.md) / [OPERATOR-CARD.md](OPERATOR-CARD.md)
- [ ] Stop

## Hard stop — do NOT

Publish:

- [ ] Publish / Enable / un-pause the product
- [ ] Turn on a public permalink and treat it as live
- [ ] Attach a buyer zip from an agent browser
- [ ] Post the product to X, note, BOOTH, or a profile as “now on sale”
- [ ] Flip GO to YES in git

Payout and KYC:

- [ ] Add bank account, PayPal payout, or stripe-style onboarding beyond viewing the screen
- [ ] Upload government ID, My Number, residence card, selfie, proof of address
- [ ] Submit W-9 / other tax forms (do not claim a US person if that is false)
- [ ] Type tax IDs into git or chat logs
- [ ] Open payout “to confirm unpaid” — unpaid is the default; do not probe KYC

Paid extras:

- [ ] Gumroad paid discover / boosts
- [ ] Custom domain purchase from this pack

Secrets:

- [ ] n8n API keys, webhook secret tokens, Google OAuth client secrets
- [ ] Real `{{TABLE_ID_DO_NOT_COMMIT}}`, customer emails, phone numbers
- [ ] Passwords (`{{PASSWORD_DO_NOT_STORE}}` stays a token)
- [ ] Filled `{{PRICE}}` committed as if it were research
- [ ] Live Content-tab filenames that contain an email, invoice, or ID

## Why unpaid draft is not a loophole

The look-target is an unpublished SKU-0 with files attached and $39 set, and
**no payout** owned by this pass. That combination is **not** a reason to:

1. Publish anyway (buyer could pay; you still have not owned payout/KYC).
2. Set up payout so Publish “makes sense”.

Both stay forbidden. Desk remains `draft_saved`.

## SKU-1 / SKU-2 / SKU-3

Later SKUs are separate unpublished paste packs. This SKU-0 GO card does not
publish them, does not attach their stubs to SKU-0, and does not bundle their
prices into the SKU-0 price box.

## Secrets policy

This card has look instructions and empty secret fields only. If a filled secret
appears in a working copy, delete it before commit and rotate the credential.

## Verification of this PR

Markdown only. Python posting-gate tests are unchanged.
No Gumroad product was published from this agent. No live checkout was created.
No payout method was added. No live Gumroad session was opened.
