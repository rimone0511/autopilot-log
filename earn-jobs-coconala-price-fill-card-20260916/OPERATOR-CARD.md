# OPERATOR-CARD — Coconala local `{{PRICE_YEN}}` fill

Pack date: 2026-09-16  
Audience: **parent operator** (祐太). Not computer-use.  
Desk: Coconala（ココナラ）  
Phase: JOBS — after listing DRAFTS [#79](https://github.com/rimone0511/autopilot-log/pull/79)  
Mode: **DRAFT_ONLY. Fill locally. 下書き保存. Do not 公開する.**

Google: MAIN only (`{{GOOGLE_ACCOUNT_EMAIL}}`). Do not create a second Coconala.

This card fills **price tokens**. It does not rewrite サービス内容. It does not send 見積もり.

---

## Banner

- **DRAFT SUGGESTIONS** in [PRICE-BANDS.md](PRICE-BANDS.md) are **not market facts.**
- **Paste 01 first** ([PASTE-ORDER.md](PASTE-ORDER.md)).
- **Human GO** before 公開する ([GO-GATES.md](GO-GATES.md)). Gate is closed.

---

## Clock (one listing, then stop)

| Step | Do | Do not |
|---|---|---|
| 0 | Read hard stop + paste-first = **01** | Open 02 or 03 first |
| 1 | Open #79 `01-n8n-automation-listing.md` | Invent a fourth listing |
| 2 | Re-read [live category floor](https://help.coconala.com/hc/ja/articles/360020963554-%E3%82%AB%E3%83%86%E3%82%B4%E3%83%AA%E3%81%94%E3%81%A8%E3%81%AE%E6%9C%80%E4%BD%8E%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9%E4%BE%A1%E6%A0%BC) | Trust the snapshot alone |
| 3 | Pick band S/M/H → one local integer as `{{PRICE_YEN}}` | Commit that integer |
| 4 | Paste #79 fields into **通常サービス**. Price box = local integer | 公開する |
| 5 | **下書きで保存する.** Confirm 下書き | 見積もりを送る / 告知する |
| 6 | **STOP** | Sitting 2 (02) until 01 is saved |

Tick boxes on a **local** copy.

---

## 0. Hard stop (read before opening Coconala)

- [ ] #79 listing pack is the source of body/title/FAQ. This card is prices only.
- [ ] First paste is **01 n8n自動化**. Not 02. Not 03.
- [ ] Agent / CU does **not** log in from this card. Parent only.
- [ ] Do not click **公開する**, 出品を公開, 公開中にする.
- [ ] Do not send 見積もり / 提案 / カスタマイズ返信 from this card.
- [ ] Do not open 本人確認 / マイナンバー / 口座 / 出金.
- [ ] Do not buy PRO, ads, or boosts.
- [ ] Do not paste passwords, API keys, or customer mail.
- [ ] Do not commit filled yen.

If a KYC or bank screen appears: close it. Local note `kyc_or_bank_screen`. Stop.

Public entry (not a live service URL):

- 出品: https://coconala.com/services/add
- 出品ガイド: https://coconala.com/pages/guide_sell
- 価格の床: https://help.coconala.com/hc/ja/articles/360020963554-%E3%82%AB%E3%83%86%E3%82%B4%E3%83%AA%E3%81%94%E3%81%A8%E3%81%AE%E6%9C%80%E4%BD%8E%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9%E4%BE%A1%E6%A0%BC
- 手数料（読むだけ。率を固定しない）: https://help.coconala.com/hc/ja/articles/230180287-%E8%B2%A9%E5%A3%B2%E6%99%82%E3%81%AE%E6%89%8B%E6%95%B0%E6%96%99%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6

---

## 1. Tokens (local ledger)

From #79. Fill **off-repo**.

| Token | Field |
|---|---|
| `{{PRICE_YEN}}` | サービス価格（円） |
| `{{PRICE_YEN_OPTION_1}}` `{{PRICE_YEN_OPTION_2}}` `{{PRICE_YEN_OPTION_3}}` | 有料オプション。空なら行を足さない |
| `{{PRICE_YEN_BAND_PICK}}` | `S` / `M` / `H` / `custom` |
| `{{LEAD_DAYS}}` | 予想お届け日数。ぶれるなら画面の「要相談」 |
| `{{PLATFORM_FEE_NOTE}}` | Fee one-liner after reading official help |
| `{{DISPLAY_NAME}}` | Profile side. Not required in listing body |
| `{{PORTFOLIO_URL}}` | Public site only. Recommended `https://yutalab.dev/` |
| `{{GOOGLE_ACCOUNT_EMAIL}}` | MAIN Google. Do not commit the address |

`{{PASSWORD_DO_NOT_STORE}}` — do not use.

---

## 2. Pick the number (still not a market fact)

Open [PRICE-BANDS.md](PRICE-BANDS.md).

- [ ] Live floor for **this** category is written on the local ledger.
- [ ] Local `{{PRICE_YEN}}` ≥ live floor.
- [ ] Local `{{PRICE_YEN}}` is **not** the floor.
- [ ] Band labeled in mind as **DRAFT SUGGESTION**, not 相場.
- [ ] Default = **M** if no other local number.
- [ ] 見積もり・カスタマイズ = 受付する. 購入前の見積もり必須 = する.
- [ ] Options not required. Each used option < body.
- [ ] Tax display follows the form.

01 default DRAFT SUGGESTION (not a fact): band **M** `25000–40000`, then **one** integer.

---

## 3. Paste (01 first)

- [ ] Logged in as MAIN Google on an **existing** seller account (register packs are out of scope).
- [ ] 通常サービス. Not 電話 / ビデオチャットサービス.
- [ ] Category from #79 for 01. Live dropdown wins. Do not invent IDs.
- [ ] Title / catch / body / お願い / FAQ / 見積もりお願い from #79 fences (buyer text does not say “unpublished draft”).
- [ ] Price box = local `{{PRICE_YEN}}` integer. Not the token string.
- [ ] Character counters on-screen still pass after the URL / name substitution.
- [ ] Images stay empty on this unpublished pass (#79).

---

## 4. Save as 下書き — then STOP

- [ ] Click **下書きで保存する** (live label wins).
- [ ] Status is still 下書き. Not 公開中 / 受付中.
- [ ] No X / note / blog “出品しました”.
- [ ] [GO-GATES.md](GO-GATES.md) `coconala_publish_listing` still `false`.
- [ ] **STOP.** Sitting 2 (02) is optional and later.

If **公開する** is the only way the form will accept the page: **do not click it.** Local note `publish_required_to_save`. Leave.

---

## Out of scope

- Publishing
- 見積もり送信 (sibling replies [#81](https://github.com/rimone0511/autopilot-log/pull/81) are still DRAFT)
- KYC / 口座 / インボイス application
- Python / n8n code in this repo
- Rewriting #79 サービス内容
- Scraping other sellers for “the real 相場”

---

## Local observation (do not commit filled yen)

```
date_jst:
operator: parent
paste_first: 01
live_floor_checked: yes / no
{{PRICE_YEN_BAND_PICK}}:
{{PRICE_YEN}}:                 # local only
01_draft_saved: yes / no / not_started
publish_clicked: no
stopped_at: draft_saved | publish_dialog | kyc_or_bank_screen | draft_save_failed
```
