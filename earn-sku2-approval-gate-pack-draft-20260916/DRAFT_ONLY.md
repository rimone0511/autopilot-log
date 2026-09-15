# DRAFT_ONLY — SKU-2 unpublished

Pack date: 2026-09-16
Desk: Gumroad
Product: SKU-2 n8n Approval-Gated Notify Pack

**This folder is a paste pack. It is not a live product.**

No agent session may:

- Click Gumroad **Publish**, **Enable**, or otherwise make the product buyable
- Announce a live `gumroad.com/l/...` URL
- Upload identity documents, selfies, or tax forms
- Add bank / payout details
- Put secrets into git or into the buyer zip
- Claim partnership with n8n, Gumroad, Slack, or an AI lab
- Activate the n8n stubs or attach live notify credentials

## Allowed for this pack

- [ ] MAIN Google login as `{{GOOGLE_ACCOUNT_EMAIL}}` (already `done-draft` on the queue)
- [ ] Open **New product** → Digital product
- [ ] Paste [LISTING-EN.md](LISTING-EN.md) and/or [LISTING-JA.md](LISTING-JA.md)
- [ ] Leave price as `{{PRICE_USD}}` until a human chooses a number **locally**
- [ ] Confirm status is unpublished / draft
- [ ] Stop

## Hard stop — do NOT

Publish:

- [ ] Publish / Enable / un-pause the product
- [ ] Turn on a public permalink
- [ ] Attach the buyer zip from an agent browser
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
- [ ] Live Slack / mail / chat tokens in stub JSON

Outbound:

- [ ] Replace NoOp outbound with a live send node from this agent
- [ ] Turn workflows **Active**
- [ ] Treat timeout as approve

## SKU-0 and SKU-1

SKU-0 is the Gumroad starter intake pack. SKU-1 is the inquiry classifier pack.
Both are **unpublished** unless a later human pack says otherwise. This SKU-2 pack
does not publish SKU-0 or SKU-1 either.

## Secrets policy (buyer zip)

The zip a human may later attach contains **stubs**. Credential files have names
and empty secret fields. If a filled secret appears in a working copy, delete it
before commit and rotate the credential.

## Verification of this PR

Markdown + JSON stubs only (`active: false`). Python posting-gate tests are unchanged.
No Gumroad product was published from this agent. No live checkout was created.
No n8n instance was activated from this pack.
