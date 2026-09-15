# GO-GATES — Coconala price-fill card 2026-09-16

> **STOP. Gate is closed.**  
> Missing, unread, or half-filled = do not 公開する.

Mirror of the Autopilot Log posting gate: **fail closed**.  
“Prices were typed” and “下書きで保存した” are not “the listing may go live.”

This file is the switch. [OPERATOR-CARD.md](OPERATOR-CARD.md) is the card. Neither file is a GO until the matching row is `true` **and** 祐太 clicks **公開する**.

Default (commit this way):

```
coconala_price_fill_gate:
  pack: earn-jobs-coconala-price-fill-card-20260916
  date: 2026-09-16
  draft_only: true
  after_pr: 79
  paste_first: 01
  fill_price_locally: true
  save_as_draft: true
  commit_filled_yen: false
  coconala_publish_listing: false
  coconala_send_estimate: false
  coconala_announce_live: false
  coconala_buy_boost_or_pro: false
  any_payout_kyc_upload: false
```

If this file is deleted, treat every publish / send / KYC row as `false`.  
Do not infer permission from a merged PR, from #79 existing, from #76 Day 2, or from “the form looks complete.”

`fill_price_locally: true` and `save_as_draft: true` mean: local ledger + **下書きで保存する** are in scope. They do **not** turn on 公開する.

---

## Human GO (only 祐太)

公開する is allowed only when **all** of these are true:

1. This file’s `coconala_publish_listing` has been flipped to `true` **by 祐太** for **this** listing id (`JP-JOBS-COCONALA-01` or 02 or 03).
2. Live category floor was re-read the same day.
3. `{{PRICE_YEN}}` is a local integer ≥ that floor, and is not the floor-as-gimmick.
4. 見積もり必須 is still on.
5. No secrets in the form.
6. 祐太 clicks **公開する** in the official UI.

The agent never flips the row. The agent never clicks 公開する.

Flipping 01 to GO does **not** GO 02 or 03. One listing per flip.

---

## UI labels that mean publish / send (stop)

Do not click. Log `stopped_at_publish` locally. Leave.

- 公開する / 出品を公開 / 公開中にする / 受付開始
- 見積もりを送る / 提案する / 相談に返信して送信
- 有料オプションを必須にする
- PRO / 有料広告 / ブースト checkout
- 本人確認 / マイナンバー / 免許 / 自撮り / 口座 / 出金

下書きで保存する / 下書きに戻す = allowed while `coconala_publish_listing` is `false`.

---

## What this card may do with the gate closed

1. Read #79.
2. Paste **01 first**.
3. Replace `{{PRICE_YEN}}` on a **local** note from [PRICE-BANDS.md](PRICE-BANDS.md) (**DRAFT SUGGESTIONS, not market facts**).
4. Type that integer into the form.
5. 下書きで保存する.
6. Close.

If the field cannot be saved as 下書き, do not 公開する to keep it.

---

## Sibling week gate

JOBS week pack [#76](https://github.com/rimone0511/autopilot-log/pull/76) also keeps `coconala_publish_listing: false`.  
**Both** must be `true` before a human publish click. One closed file is enough to stop.
