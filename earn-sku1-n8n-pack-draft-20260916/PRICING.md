# SKU-1 pricing — PLACEHOLDER ONLY

Pack date: 2026-09-16
Desk: Gumroad
Mode: **DRAFT_ONLY**
Live price: **not set in git**

Gumroad help (Adding a product): a product may be free or up to USD 5,000.
A `+` after a minimum (example `$5+`) is pay-what-you-want. Charges are processed
in USD (or the customer’s local currency where Gumroad supports it).

This file does **not** choose a market price, a “fair” yen amount, or a discount.
The operator fills numbers in the Gumroad form locally. Do not commit the filled
values. Do not invent GMV or “this will sell”.

## Fields to paste (tokens only)

| Gumroad field | Paste | Notes |
|---|---|---|
| Price (display) | `{{PRICE_USD}}` | Required on create. Leave token if the human has not chosen. |
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
{{PRICE_USD}}
{{PRICE_JPY_DISPLAY}}
{{GUMROAD_FEE_NOTE}}
```

`{{GUMROAD_FEE_NOTE}}`: read Gumroad’s current fee help immediately before a human
publish. Do not freeze a fee percentage in this pack.

## Relationship to SKU-0

SKU-0 (starter intake) is a **separate** product and a separate price token
(`{{PRICE_USD_SKU0}}` lives in that pack, not here). Do not bundle SKU-0 into
SKU-1’s price box in this draft.

## What not to do

- Do not publish at $0 “just to test live checkout”
- Do not copy a competitor’s number into git as if it were researched
- Do not promise income, refunds-as-marketing, or “launch discount ending tonight”
- Do not add paid Gumroad boosts / paid discover features from this pack
