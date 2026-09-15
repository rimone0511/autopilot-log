# DRAFT_ONLY — do not publish

Pack: `earn-jobs-pricing-menu-20260916/`  
Date: 2026-09-16  
Desks: Coconala / Gumroad / Contra Independent  
Mode: paste menu only. Not a live catalog.

**This folder is a paste pack. It is not a live product, not a sent estimate, and not a published service.**

No agent session may:

- Click Coconala **公開する** / 出品確定 / 見積もり送信
- Click Gumroad **Publish**, **Enable**, or otherwise make a product buyable
- Click Contra **Publish** on a service (help: use **Save as unpublished**)
- Announce a live `coconala.com/services/...`, `gumroad.com/l/...`, or Contra service URL as “now on sale”
- Upload identity documents, selfies, My Number, Persona, or tax forms
- Add bank / payout / wallet details
- Put secrets into git or into buyer files
- Claim partnership with n8n, Coconala, Gumroad, Contra, or an AI lab
- Type a researched-looking yen or USD amount into git as if it were a market fact

## Allowed for this pack

- [ ] Read public help URLs in [README.md](README.md)
- [ ] MAIN Google login as `{{GOOGLE_ACCOUNT_EMAIL}}` (do not create a second identity)
- [ ] Paste **text** into a human-operated draft form that is already open
- [ ] Leave every price as a `{{PRICE_*}}` token, or empty + park `rate_required` / `rate_empty`
- [ ] Confirm Coconala stays 受付休止 or not public; Gumroad unpublished; Contra unpublished
- [ ] Stop

## Hard stop — do NOT

Publish / sell:

- [ ] 公開 / Publish / Enable / un-pause / go-live permalink
- [ ] 見積もり提案の送信、募集への応募送信、Contra inquiry reply as a bid
- [ ] Post the menu to X, note, BOOTH, or a profile as “now on sale”
- [ ] Attach a buyer zip from an agent browser

Payout and KYC:

- [ ] Add bank account, PayPal, Stripe-style onboarding, Contra Wallet → Add account
- [ ] Upload government ID, My Number, residence card, selfie, proof of address, Persona
- [ ] Submit W-8BEN / W-9 / other tax forms
- [ ] Type tax IDs into git or chat logs

Paid extras:

- [ ] Coconala サービス広告 / セラーサポート purchase from this pack
- [ ] Gumroad paid discover / boosts / custom domain
- [ ] Contra Pro (`$29/mo` or `$199/yr` **cited** from public pricing pages — still **do not buy**; live pricing wins)

Secrets:

- [ ] n8n API keys, webhook secret tokens, Google OAuth client secrets
- [ ] Real `{{TABLE_ID_DO_NOT_COMMIT}}`, customer emails, phone numbers
- [ ] Passwords (`{{PASSWORD_DO_NOT_STORE}}` stays a token)

## If a live form requires a number

Do not invent yen or USD. Options, in order:

1. Leave the box empty if the form allows it, park `rate_empty`
2. Paste the matching `{{PRICE_*}}` token if the field accepts text
3. Fill from a **private local ledger** the human already chose — never commit the filled value
4. Contra: **Contact for pricing** is an official option (help 9322412). Prefer it until a human chooses a number
5. Stop. Do not publish a $0 / ¥500 “just to test checkout” from this pack

¥500 on Coconala `guide_sell` is a **platform minimum**, not a recommended price.
Gumroad help: a product may be free or up to USD 5,000. That is a bound, not a quote.

## Verification of this PR

Markdown only. Python posting-gate tests are unchanged.
No Coconala / Gumroad / Contra listing was published from this agent.
No payout method was added. No estimate was sent.
