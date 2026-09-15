# ココナラ 価格フィル カード（JOBS）— 2026-09-16

**DRAFT_ONLY. DO NOT PUBLISH.**  
**DRAFT SUGGESTIONS. NOT MARKET FACTS.**  
Human GO before **公開する**. No secrets. Agent does not log in.

観測・作成日: 2026-09-16（JST 起算のパック名）  
机: Coconala（ココナラ）  
位相: **JOBS**（価格欄のローカル埋め。出品本文は [#79](https://github.com/rimone0511/autopilot-log/pull/79)）  
対象: PR#79 の 3 本（n8n / 分類 / AI運用伴走）の `{{PRICE_YEN}}` ほか  
売り手: 個人。推奨表示名はローカルの `{{DISPLAY_NAME}}`

This folder is a **local price-fill card**. It is not a live Coconala service, not a market survey, and not permission to click 公開する.

---

## After PR#79

Listing paste lives on [#79](https://github.com/rimone0511/autopilot-log/pull/79) (`earn-jobs-coconala-service-drafts-20260916/`). That pack left yen as tokens on purpose.

This pack does **not** rewrite those サービス内容 fences. It tells the operator:

1. which of the three listings to paste **first**
2. how to pick a **local** integer for `{{PRICE_YEN}}` from DRAFT SUGGESTION bands
3. to **下書きで保存する**
4. to stop until a human GO flips 公開

If #79 is still a draft branch, use that branch’s listing files. Do not invent a fourth listing.

---

## Files

| File | Role |
|---|---|
| [OPERATOR-CARD.md](OPERATOR-CARD.md) | Local fill card. Clock, tokens, 下書き保存, stop |
| [PASTE-ORDER.md](PASTE-ORDER.md) | **Paste 01 first.** Then 02. Then 03. One sitting = one listing |
| [PRICE-BANDS.md](PRICE-BANDS.md) | `{{PRICE_YEN}}` bands. **DRAFT SUGGESTIONS, not market facts** |
| [GO-GATES.md](GO-GATES.md) | Fail-closed. `coconala_publish_listing: false` until 祐太 |
| [STATUS.md](STATUS.md) | Pack ready. Live yen not filled from this agent |

---

## Hard rules

- **公開する** is a human GO. This pack’s gate row stays `false`.
- **下書きで保存する** is allowed. That is not publish.
- Fill `{{PRICE_YEN}}` on a **local ledger**. Do not commit the filled integer.
- Suggestion bands in [PRICE-BANDS.md](PRICE-BANDS.md) are **starting hypotheses**. They are not 相場, not scraped competitor prices, not Coconala’s recommended price, not GMV.
- Official category **floor** is a platform constraint. Re-read [help](https://help.coconala.com/hc/ja/articles/360020963554-%E3%82%AB%E3%83%86%E3%82%B4%E3%83%AA%E3%81%94%E3%81%A8%E3%81%AE%E6%9C%80%E4%BD%8E%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9%E4%BE%A1%E6%A0%BC) immediately before paste. The snapshot in PRICE-BANDS is not frozen.
- No secrets: no password, API key, bank, My Number, OTP, live email, customer text.
- No invented live URL (`coconala.com/services/123…`).
- No paid boost / PRO / 同一内容の複数出品.
- Agent does not complete Coconala login as a done condition.

## Allowed without flipping GO

1. Read #79 listing files.
2. Pick **01** first ([PASTE-ORDER.md](PASTE-ORDER.md)).
3. Re-read the live category floor.
4. Copy a DRAFT SUGGESTION band into a **local** note as `{{PRICE_YEN}}`.
5. Paste into an existing seller account’s **通常サービス** form.
6. **下書きで保存する.** Confirm still 下書き.
7. Stop.

## Related (pointers only)

- Service listing DRAFTS x3: [#79](https://github.com/rimone0511/autopilot-log/pull/79)
- Inquiry / custom replies (not listing body): [#81](https://github.com/rimone0511/autopilot-log/pull/81)
- JOBS week calendar (Day 2 Coconala): [#76](https://github.com/rimone0511/autopilot-log/pull/76)
- Wave 2 見積もり返信: `earn-jp-proposal-wave2-20260916/` (not サービス内容)

## This PR does not

- Publish a Coconala service
- Send 見積もり
- Register / KYC / 口座
- Commit filled yen
- Change Python posting-gate code
