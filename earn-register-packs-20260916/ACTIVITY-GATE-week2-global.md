# ACTIVITY-GATE -- Week-2 GLOBAL desks

Pack folder: `earn-register-packs-20260916/`
Public-page check: 2026-09-15
Operator constraint: Japanese, English profiles allowed
Mode: draft packs only -- no live KYC, no paid plans, no publish

Gate labels:

- `pass` -- public pages show a living marketplace; draft work may proceed to the stop line
- `fail` -- do not spend operator time (dead, or a hard policy block)
- `needs_check` -- public evidence missing or mixed; human click-time confirm
- `blocked_paid_plan` -- marketplace may be alive but seller activation appears paid (still no payment)

No traffic counts are invented. Vendor marketing totals are ignored as activity proof.

---

## Summary table

| Desk | File | Activity | Google signup | Free seller path | KYC stop documented | Gate |
|---|---|---|---|---|---|---|
| Guru.com | `01-guru-com-seller-profile-draft.md` | alive | yes | yes (Basic) | yes (ID + card + 4.95 USD fee) | **pass** |
| PeoplePerHour Hourlies/Offers | `02-peopleperhour-hourlies-draft.md` | alive | yes | no / `needs_check` (Terms: PPH Basic is a paid annual plan) | yes (Payments document upload) | **blocked_paid_plan** (do not subscribe). Marketplace activity **pass**. Overall desk **needs_check** at subscription screen |
| Malt.com (EU) | `03-malt-com-eu-draft.md` | alive | `needs_check` | yes (profile draft free) | yes (AML identity + company docs) | **pass** for English draft profile; Google `needs_check` |
| Workana | `04-workana-draft.md` | site alive; jobs list unread (Cloudflare) | yes (login HTML) | yes (register/browse/bid described free; skip paid Priority Moderation) | yes (payment verification may request government ID) | **needs_check** for job-board liquidity; draft profile **pass** |

---

## Per-desk evidence (short)

### Guru.com -- pass

- Jobs browse https://www.guru.com/d/jobs/ and skill pages showed 2026-dated posts, including very recent timestamps ("Posted 1 hr ago", "Posted 14 hrs ago") with quotes already received.
- Homepage categories load.
- Free Basic membership is documented (10 quotes/month). Stay there.
- Stop: Verify dashboard -> government ID, proof of address, credit-card micro-charge, 4.95 USD review fee.

### PeoplePerHour -- marketplace pass, paid-plan block

- Register page shows Continue with Google / Facebook / email.
- Freelance jobs page on 2026-09-15 showed many cards with timestamps down to "2 minutes ago".
- `/hourlie/` URLs still serve Offers (including n8n automation packages). Surface is alive. Sales volume unknown -- not guessed.
- Terms describe PPH Basic as a paid annual subscription and TopAccess as a second paid bundle. This pack must not pay. If the UI refuses to submit without a plan, stop and keep `blocked_paid_plan`.
- Stop: Settings -> Payments document upload; Fast-Track KYC; featured Offers.

### Malt.com -- pass (draft)

- Global site and 2026 Tech Trends report are current; report copy even names n8n.
- Public FR tag page for n8n lists a large set of freelancer profiles with day rates -- directory looks dense, not thin.
- No public job board (clients message profiles). Alive is judged from directory + current site, not job timestamps.
- Japan appears on Malt's open-country registration list. English profile is allowed. Do not fake an EU address.
- Google button not confirmed in official help (`needs_check`).
- Stop: identity document + company/VAT papers for payout.

### Workana -- needs_check (jobs), pass (draft profile)

- Homepage is an actively marketed LATAM talent product (not a parked domain).
- `/en/jobs` exists but was not readable (Cloudflare challenge) on 2026-09-15, so job recency is unknown.
- `/en/login` HTML includes Continue with Google / Facebook / Apple.
- Register/browse/propose described as free; Priority Moderation is the paid skip -- do not buy it.
- Stop: government ID for payment verification; withdrawal setup.

---

## Hard stops that apply to every desk

1. No real passwords, government IDs, tax IDs, or KYC images in git or in chat.
2. No paid memberships, featured listings, fast-track reviews, or document-processing fees.
3. No publishing, bidding, or client messages from these packs.
4. If a screen asks for passport / national ID / proof of address / credit card for identity, stop.
5. If activity cannot be seen on a public page, mark `needs_check` -- never fill with a guessed number.

---

## Suggested operator order

1. Guru.com draft profile + Service (free Basic) -- **go**
2. Malt.com English profile draft, skip legal uploads, confirm Google at click-time -- **go**
3. Workana EN talent draft, profile not public, no Priority Moderation -- **go**, then human-check `/en/jobs` after Cloudflare
4. PeoplePerHour -- fill application text locally; **open register only to see if a zero-cost submit still exists**; if the next step is PPH Basic or TopAccess, close the tab

---

## Result for Week-2 GLOBAL

Paste packs: **complete** (four desks + this gate).

Activity gate overall: **mixed** -- two clear alive desks (Guru, Malt), one alive marketplace with a paid-plan wall (PeoplePerHour), one living site whose public job feed was not inspectable (Workana).

No desk is marked `fail` for being dead. No desk is authorized past KYC or paid plans.
