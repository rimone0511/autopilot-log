# PRICE-BANDS — `{{PRICE_YEN}}` DRAFT SUGGESTIONS

> **DRAFT SUGGESTIONS. NOT MARKET FACTS.**  
> Not 相場. Not a competitor scrape. Not Coconala’s recommended price.  
> Not promised GMV, 受注率, or “this band sells.”  
> Not a live filled `{{PRICE_YEN}}` to commit.

Pack date: 2026-09-16  
Desk: Coconala  
Use: local ledger → type one integer into the form → **do not git-add that integer**

The operator picks **one** integer per listing from a band (or rejects every band and writes a local number that still clears the **live** category floor). Empty option rows stay empty.

---

## Two different kinds of numbers

| Kind | What it is | What it is not |
|---|---|---|
| **Official category floor** | Platform constraint from [ココナラヘルプ：カテゴリごとの最低サービス価格](https://help.coconala.com/hc/ja/articles/360020963554-%E3%82%AB%E3%83%86%E3%82%B4%E3%83%AA%E3%81%94%E3%81%A8%E3%81%AE%E6%9C%80%E4%BD%8E%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9%E4%BE%A1%E6%A0%BC). Re-read **immediately before paste**. Snapshot below can be stale | A suggested selling price. A market average |
| **DRAFT SUGGESTION band** | Starting hypothesis for a **local** `{{PRICE_YEN}}` pick on an estimate-required, unpublished 通常サービス | Market fact. Competitor research. Official advice. Income forecast |

If the live help table or the live form floor disagrees with the snapshot: **the live page wins.** Raise the local integer. Do not lower a band to “match a blog.”

---

## Official floor snapshot (re-read live)

Fetched from the public help article above while writing this pack (2026-09-16). **Not frozen.**

| #79 listing | Public-tree category used in #79 | Help-table row to look up | Snapshot floor (yen) |
|---|---|---|---|
| 01 n8n自動化 | 業務自動化・効率化支援 → その他（業務自動化・効率化） | **業務自動化・効率化支援** | 3000 |
| 02 問い合わせ分類 | same parent as 01 | **業務自動化・効率化支援** | 3000 |
| 03 AI運用伴走 | ITサポート・コンサル相談 → ITコンサル相談 | **ITサポート・コンサル相談** | 1000 |

Upper bound: help says category max can differ. Read the live form. Do not invent a max in git.

If the live dropdown lands on a **different** node (for example 03’s allowed alternate `AI導入・活用支援`): look up **that** row. Do not keep the snapshot floor.

Do **not** pick the floor as the selling price for these three offers. Floor = “the form will accept this.” It is not a strategy.

---

## How to pick (method, not a market)

All three #79 listings are **見積もり必須**. The listed yen is a starting display price, not “the whole job.”

1. Re-read the live floor for **this** listing’s live category.
2. Stay **at or above** that floor.
3. Do not pick the floor.
4. Choose band **S / M / H** below as a DRAFT SUGGESTION, then pick **one** integer inside it (or a local number outside it that still clears the floor).
5. Default when the operator has no other local number: **band M**.
6. Each 有料オプション, if used, is **lower than the body** and **not required**.
7. Follow the form’s 税込 / 税抜 switch. Do not freeze tax in git.
8. Fee % lives in [販売時の手数料](https://help.coconala.com/hc/ja/articles/230180287-%E8%B2%A9%E5%A3%B2%E6%99%82%E3%81%AE%E6%89%8B%E6%95%B0%E6%96%99%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6). Token `{{PLATFORM_FEE_NOTE}}`. **Do not freeze a rate in this pack.**

---

## Body `{{PRICE_YEN}}` — DRAFT SUGGESTION bands

Yen ranges below are **DRAFT SUGGESTIONS**. They are not 相場.

### 01 — n8n自動化 (`JP-JOBS-COCONALA-01`) — paste first

Scope in #79: scoped n8n flow 1 + 手順書. Official API only. Human publish switch.

| Band | DRAFT SUGGESTION (yen) | Local meaning (not a fact) |
|---|---|---|
| S | 15000–25000 | First unpublished draft. Still 見積もり必須 |
| **M (default pick)** | 25000–40000 | Working local starting display if no other number exists |
| H | 40000–60000 | Only if the **local ledger already** holds a higher number. Do not inflate to “look premium” |

Local tokens: `{{PRICE_YEN}}` `{{PRICE_YEN_BAND_PICK}}` = `S` / `M` / `H` / `custom`

### 02 — 問い合わせ分類 (`JP-JOBS-COCONALA-02`) — second

Scope in #79: label routing + 未確定. **No auto-reply.** Same parent category as 01.

Bands sit **a step below 01** because the #79 offer is narrower (型 + 未確定, not a full n8n build). That is a **scope note**, not a market survey.

| Band | DRAFT SUGGESTION (yen) | Local meaning (not a fact) |
|---|---|---|
| S | 12000–20000 | First unpublished draft |
| **M (default pick)** | 20000–30000 | Working local starting display |
| H | 30000–45000 | Only if local ledger already higher |

Do not paste 02 until 01 is 下書き ([PASTE-ORDER.md](PASTE-ORDER.md)).

### 03 — AI運用伴走 (`JP-JOBS-COCONALA-03`) — last

Scope in #79: 検品リスト + 依頼文の版. Not 常駐代行. Not AIエージェント開発.

Help-table floor snapshot for **ITサポート・コンサル相談** is **1000**. **Do not use 1000.** That floor is a form constraint, not a consulting display price.

| Band | DRAFT SUGGESTION (yen) | Local meaning (not a fact) |
|---|---|---|
| S | 10000–18000 | First unpublished draft. Still well above the 1000 floor snapshot |
| **M (default pick)** | 18000–30000 | Working local starting display |
| H | 30000–50000 | Only if local ledger already higher |

Re-read the **03** floor separately. It is a different mid-category from 01/02.

---

## Options `{{PRICE_YEN_OPTION_1}}` `{{PRICE_YEN_OPTION_2}}` `{{PRICE_YEN_OPTION_3}}`

From #79: three optional rows per listing. **Must-buy options are forbidden** (Coconala rule and #79 STOP-PUBLISH).

| Rule | DRAFT SUGGESTION (not a fact) |
|---|---|
| Empty local number | **Do not add that row** |
| Each option vs body | Option **<** `{{PRICE_YEN}}` |
| Option 1 | about 30–50% of the local body pick |
| Option 2 | same band or smaller than option 1 |
| Option 3 (修正+1) | smallest of the three |
| Floor | Each option must also clear **that category’s live option/body rules** on the form. If the form rejects, raise locally. Do not commit the retry |

Names stay as in #79. Do not invent a fourth paid option from this card.

---

## What this file refuses to do

- Quote a competitor’s live yen as “the market”
- Freeze `22%` or any other fee as if it cannot change
- Promise 時短 / 受注 / 月収
- Put a filled integer into git
- Set `{{PRICE_YEN}}` to 0, 500, or the category floor “to test checkout”
- Add compare-at / fake discount / countdown
- Turn 見積もり必須 off to make a cheap impulse buy

---

## Local ledger (do not commit filled)

Copy to a private note. Type into Coconala from that note.

```
date_jst:
listing: 01 / 02 / 03
live_category_node:
live_floor_yen:          # from help + form, not from memory
{{PRICE_YEN_BAND_PICK}}: S / M / H / custom
{{PRICE_YEN}}:
{{PRICE_YEN_OPTION_1}}:  # empty = omit row
{{PRICE_YEN_OPTION_2}}:
{{PRICE_YEN_OPTION_3}}:
{{LEAD_DAYS}}:
{{PLATFORM_FEE_NOTE}}:   # read help; do not paste a guessed %
tax_display: 税込 / 税抜 / follow-form
saved_as: 下書き
publish_clicked: no
```
