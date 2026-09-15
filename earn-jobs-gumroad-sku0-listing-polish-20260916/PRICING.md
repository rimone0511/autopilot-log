# SKU-0 pricing — keep $39 or `{{PRICE}}`

Pack date: 2026-09-16
Phase: JOBS
Desk: Gumroad
Product: SKU-0 starter intake
Mode: **DRAFT_ONLY**
Live price in git: **not required**

Gumroad help (Adding a product): a product may be free or up to USD 5,000.
A `+` after a minimum (example `$5+`) is pay-what-you-want. Charges are processed
in USD (or the customer’s local currency where Gumroad supports it).

This file does **not** invent GMV, a “fair” yen amount, or a launch discount.

## Rule for this polish

| If the unpublished draft already shows… | Do this |
|---|---|
| **$39** (USD 39, no `+`) | **Keep it.** Do not “optimize”, do not drop to $0 to test checkout, do not add PWYW. |
| Empty / token / other number you did not choose | Paste `{{PRICE}}` locally. A human types the number in the Gumroad form. Do not commit the filled value. |
| `$0` or `$0+` | Do **not** publish. Do not use $0 as a live-checkout test. Restore $39 if that was the prior draft, or leave `{{PRICE}}` for a human. |

`{{PRICE}}` and `{{PRICE_USD_SKU0}}` are the same slot. Use either token in notes.
Do not write a second checkout currency into git.

## Fields (tokens / keep)

| Gumroad field | Paste / keep | Notes |
|---|---|---|
| Price (display) | **$39** if already set; else `{{PRICE}}` | Required on create. Keep existing $39. |
| Currency display | USD unless the live picker says otherwise | Do not claim JPY settlement if the form still charges USD |
| Optional JP note (description only, not the price box) | `{{PRICE_JPY_DISPLAY}}` | Optional one-line display. Not a second checkout currency unless Gumroad shows it |
| Pay what you want | **off** for this draft | Do not add `+` unless a later human pack says so |
| Suggested price | empty | Only used if PWYW is on |
| Compare-at / strikethrough | empty | No fake discounts |
| Max purchase count | empty | No artificial scarcity |
| Versions / extra paid tiers | **none** | One digital SKU |

## Local ledger (do not commit)

Operator fills these on a private note, then types them into Gumroad — not into this repo:

```
{{PRICE}}
{{PRICE_USD_SKU0}}
{{PRICE_JPY_DISPLAY}}
{{GUMROAD_FEE_NOTE}}
```

If the draft already shows 39, the local ledger may read:

```
keep: 39 USD
{{PRICE_JPY_DISPLAY}}
{{GUMROAD_FEE_NOTE}}
```

`{{GUMROAD_FEE_NOTE}}`: read Gumroad’s current fee help immediately before a human
publish. Do not freeze a fee percentage in this pack.

## Relationship to later SKUs

SKU-1 / SKU-2 / SKU-3 are **separate** products and separate price tokens.
Do not bundle them into SKU-0’s price box in this draft.

## What not to do

- Do not publish at $0 “just to test live checkout”
- Do not copy a competitor’s number into git as if it were researched
- Do not promise income, refunds-as-marketing, or “launch discount ending tonight”
- Do not add paid Gumroad boosts / paid discover features from this pack
- Do not commit a filled JPY amount next to $39
