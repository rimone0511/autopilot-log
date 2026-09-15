# CHECKLIST — Coconala draft_saved → publish-ready (unpublished)

Pack date: 2026-09-16  
Desk: ココナラ / Coconala  
Start: profile **`draft_saved`**  
End of this pack: **`publish_ready_unpublished`** or a named gap  
Mode: **DRAFT_ONLY.** [HUMAN-GO.md](HUMAN-GO.md) stays closed.

Tick on a **local** copy. Point at first-gig paste; do not paste sibling fences into git.

First-gig pack: `earn-jobs-coconala-service-drafts-20260916/` ([PR#79](https://github.com/rimone0511/autopilot-log/pull/79)).  
Default listing this pass: `01-n8n-automation-listing.md`.

---

## 0. Hard stop (read before opening Coconala)

- [ ] Role = **出品者 / 通常サービス**. 仕事を依頼する側・電話相談・ビデオチャットサービスに入らない。
- [ ] MAIN Google only (`{{GOOGLE_ACCOUNT_EMAIL}}`). Second Coconala = STOP.
- [ ] **公開する** を押さない。[HUMAN-GO.md](HUMAN-GO.md) `coconala_publish_listing: false`.
- [ ] 見積もりを送らない。トークで営業しない。外部 LINE / Zoom / メールへ誘導しない。
- [ ] 本人確認・口座・インボイスに入らない。画面が出たら閉じる。Slip: [PR#43](https://github.com/rimone0511/autopilot-log/pull/43) `01-coconala.md`.
- [ ] 円の実売価・鍵・顧客本文を git に戻さない。
- [ ] この authoring エージェントはログイン完了を PR の成功条件にしない。

やらない: PRO 申請、有料ブースト、セラーサポート購入、同一サービスの複製出品、景品表示法の根拠なし実績。

---

## 1. Preflight

- [ ] You are the **human operator** (or CU serial under these ticks), not the pack-author claiming a live fill.
- [ ] Viewport desktop. One marketplace profile. Do not also live in Gmail in that profile.
- [ ] Timebox 15–25 min. 公開ダイアログが出たら即閉じる。
- [ ] Wave A box still says Coconala `draft_saved` / QUEUE `done-draft`. This pack does **not** reopen the **profile** to make it public.
- [ ] Read [README.md](README.md) first-gig table. Open PR#79 files in another window. Do not copy their fenced bodies into this repo.

Public entries (not a live service URL):

| What | URL |
|---|---|
| 出品ガイド | https://coconala.com/pages/guide_sell |
| 出品フォーム（ログイン後） | https://coconala.com/services/add |
| カテゴリ | https://coconala.com/categories/ |

---

## 2. Profile stays parked (`draft_saved`)

Profile work is **done**. Do not “finish” the seller by publishing the profile.

- [ ] Logged in as the existing MAIN-Google member (`already_member_draft`). Do not sign up.
- [ ] 出品者情報 / プロフィール公開トグルを **公開側へ動かさない**。
- [ ] 表示名を資格の創作で飾り直さない。
- [ ] プロフィール画像に KYC 自撮りを使わない。

If login is blocked (captcha / hold): park `blocked_skip`. Do not invent a workaround. Do not create another account.

---

## 3. Find or open **one** unpublished 通常サービス

Guide: 種類 → カテゴリ・タイトル → サービス内容 → 画像 → **公開**. This pack stops before 公開.

- [ ] Open **出品サービス管理** (live menu label wins) and look for an existing **下書き**.
- [ ] If **one** draft matches first-gig 01 (n8n 自動化 + 手順書): use that. Do not open a second “test” listing.
- [ ] If **several** drafts: do not guess. List titles as `present / mismatch` in a local GAPS copy (not the live URL). Pick 01-shaped or stop.
- [ ] If **no** service draft: create **one** 通常サービス from PR#79 `01-…` only. Still **下書き**. Do not also create 02 and 03 this pass.
- [ ] If the row is already **公開中**: `already_published`. Do not unpublish from an agent. Stop.
- [ ] 見積もり・カスタマイズ受付: first-gig 01 says **受付する** + 購入前見積もり **必須**. Confirm on the live form. That is not 見積もり送信.

02 / 03 remain optional later drafts (different offers). Coconala ルール: 同一サービスの複数出品は禁止。タイトルを変えただけのコピーを作らない。

---

## 4. Fields (paste from first-gig — do not rewrite from memory)

Ceilings (public news/guide; **live counter wins**):

| 欄 | Ceiling | First-gig 01 (PR#79 measured) |
|---|---|---|
| サービスタイトル（ます止め） | 25 | 15 — `n8n自動化と手順書を作ります` |
| キャッチコピー | 30 | 18 |
| サービス内容 | 1000 (通常枠) | 655 |
| 購入にあたってのお願い | 500 | 302 |
| 見積もりにあたってのお願い | 200 | 122 |
| 有料オプション名 | 60 / max 10 | 3 optional rows, not required |

Category from PR#79 01 (live dropdown wins; do not invent IDs):

| 段 | 値 |
|---|---|
| 大 | IT相談・システム開発 |
| 中 | 業務自動化・効率化支援 |
| 小 | その他（業務自動化・効率化） |

近い代替: 同中カテの API連携・開発。  
入れない: Excelマクロ専用、GAS専用、RPA、AI画像/動画/音声、AIエージェント開発、占い。

Ticks:

- [ ] 種類 = **通常サービス**（メッセージ完結）。ビデオチャット表示オフ。物販配送オフ。
- [ ] カテゴリ = table above or nearest live node. Not a duplicate of another of your listings.
- [ ] タイトル = PR#79 01 fence. Form may auto-append「ます」— do not double it. Counter ≤ 25.
- [ ] キャッチ = PR#79 01 fence. Counter ≤ 30.
- [ ] サービス内容 = PR#79 01 fence (not Wave 1/2 estimate files). Counter ≤ 1000.
- [ ] 範囲外ブロックが本文に残っている（ブラウザ自動操作・無人公開・鍵の代理入力）。
- [ ] パートナー名乗りが無い（n8n / ココナラ / AI 企業）。
- [ ] 未確認の件数・時短・精度・収入保証が無い。
- [ ] 基本内容 / 無料修正回数 **1** / 同時受注 **1** / ファイル形式 JSON・Markdown（欄があれば）。
- [ ] 予想お届け日数 = local `{{LEAD_DAYS}}` or **要相談と表示する**. Do not invent a market-fast number.
- [ ] 有料オプション: optional. Empty token → do not add the row. Do not make options required (公式も禁止寄り).
- [ ] 購入にあたってのお願い = PR#79 01 fence. Direct 購入を急がせない（見積もり必須）。
- [ ] 見積もりにあたってのお願い = PR#79 01 fence.
- [ ] Pricing-menu [#82](https://github.com/rimone0511/autopilot-log/pull/82) titles are **overlay only**. If 01 is already pasted, do not retitle to `受付から通知までn8nで作ります` in the same pass.

`{{PORTFOLIO_URL}}` : public `https://yutalab.dev/` is allowed. If the live form rejects external URLs in サービス内容, move it out (profile / お願い) rather than fighting the filter.

---

## 5. Images / video

Guide_sell ステップ3: 成果物サンプル or イメージ画像.  
マグ「サービスページのコツ」: **画像は必ず設定**. 1枚目が検索結果。  
First-gig pack §11: **this paste pack does not upload** (because it does not publish). **This checklist** treats missing images as a **GO-blocker**, not as a reason to click 公開する.

- [ ] Look at the image slots on the existing draft. Do **not** upload from the pack-author agent.
- [ ] If empty: record `images_missing` in a local GAPS copy. Human prepares originals **later**. Still save 下書き.
- [ ] If present: originals (or clearly licensed). Secrets cropped (tokens, emails, customer names, n8n API keys).
- [ ] 1枚目 shows **what the service is** (n8n flow + 手順書), not a partner badge.
- [ ] No n8n / Coconala / lab / xAI logo as affiliation.
- [ ] No other seller’s listing image. No ID / selfie / bank screenshot.
- [ ] Filename has no email or invoice number.
- [ ] 動画 URL empty unless an original public YouTube exists. No copyrighted audio.
- [ ] Do not fill 10 slots with keyword spam.

Conservative local spec (third-party blogs; **live uploader wins**): first-gig pack does not freeze px. If the form shows a size, follow the form. Do not commit binary images to this repo.

---

## 6. Price

Guide_sell: 販売価格は **500円〜1,000,000円（※カテゴリによる）**. 有料オプション最大 10、各 500円〜.  
Help: カテゴリごとの最低サービス価格 — re-read https://help.coconala.com/hc/ja/articles/360020963554 immediately before typing a number.  
First-gig + pricing menu: git keeps **`{{PRICE_YEN}}` / `{{PRICE_JPY_SKU_STARTER}}` only**.

- [ ] Price box is not blank if the form requires it to **save** a draft. If it refuses tokens, use the **local ledger** number, never commit it.
- [ ] Local number ≥ live category minimum. ¥500 is the platform floor, not a recommended rate. Do not invent a “market” yen in git.
- [ ] No strikethrough / fake discount / 数量限定 without a real limit (景品表示法 / マグ販売ルール).
- [ ] Displayed price matches the numeric field (禁止: 設定価格と表記価格の不一致).
- [ ] おひねり前提・オプション必須の出品にしない。
- [ ] 無料役務・成果報酬・月額のサイト外支払を本文に書かない。
- [ ] Fee % not pasted into buyer-facing fields. `{{PLATFORM_FEE_NOTE}}` stays local. Public guide cited 22% on 2026-09-16; re-read before GO.
- [ ] Compare overlay [#82](https://github.com/rimone0511/autopilot-log/pull/82) only for SKU-STARTER token name. Do not publish a four-SKU duplicate listing this pass.

If the form blocks save without a price and the ledger is empty: `rate_empty`. **Leave unpublished.** Do not type a made-up 5000.

---

## 7. FAQ

マグ: よくある質問は購入前のずれを減らす欄。最初だけ書いて放置しない — このパスでは **6 件を載せて下書き保存** まで。  
First-gig 01 §9 = six Q/A pairs. Do not copy them into this file.

| # | Q (operator hint — paste from PR#79) |
|---|---|
| 1 | AI は使いますか |
| 2 | n8n や AI 企業の公式ですか |
| 3 | 鍵やパスワードはどこへ入れますか |
| 4 | SNS へ自動投稿できますか |
| 5 | n8n の契約も代行しますか |
| 6 | 修正と追加作業の違いは |

- [ ] Six pairs pasted from **01**, not from Fiverr FAQ English packs.
- [ ] Buyer-facing answers do not say DRAFT / 未公開.
- [ ] No fake affiliation, no accuracy %, no “必ず成果”.
- [ ] Secrets stay “依頼者の n8n 接続画面”. Never “トークに貼ってください”.
- [ ] If the live form allows more than 6: do not stuff keywords. 6 is enough for publish-ready.
- [ ] If the live form allows fewer: keep 1–4 (affiliation, secrets, SNS, 範囲外) first. Note `faq_trimmed` in GAPS.

---

## 8. Save 下書き — confirm still unpublished

- [ ] Click **下書きで保存する** (live label wins). Not **公開する**.
- [ ] If there is no 下書き保存 and only 公開する: **fill then leave** (`listing_draft_no_save_path`). Do not press 公開する.
- [ ] Status still 下書き / 非公開 / 受付休止. Not 公開中 / 受付中.
- [ ] No blog embed. No X/note announce.
- [ ] No live `coconala.com/services/<id>` committed.
- [ ] Copy secret-free keys into a local [STATUS.md](STATUS.md) / [GAPS.md](GAPS.md).
- [ ] **STOP.** Publish-ready ≠ published.

---

## 9. Success line (secret-free)

Valid: `publish_ready_unpublished` | `draft_saved_fields_incomplete` | `images_missing` | `rate_empty` | `listing_draft_no_save_path` | `already_published` | `blocked_skip` | `kyc_wait` | `no_listing_draft`.

Not success: 「公開した」「見積もり送った」「口座登録した」「PRO にした」.

```
desk: Coconala
pack: earn-jobs-coconala-publish-ready-checklist-20260916/
profile: draft_saved | unknown
listing: none | draft | publish_ready_unpublished | already_published
listing_id_in_git: none
first_gig_source: PR79-01 | PR79-02 | PR79-03 | other | missing
fields: pasted | partial | not-entered
images: none | original-ok | images_missing | needs_human
price: placeholder-local | rate_empty | saved-not-in-git
faq: 0-6
save: 下書き | no-save-path | not-run
publish_clicked: no
estimate_sent: no
kyc_opened: no
human_go_coconala_publish_listing: false
next: stop
```

---

## 10. Out of scope

- This markdown’s authoring agent logging in to complete the ticks
- 02 / 03 live create in the same sitting (optional later, still unpublished)
- Estimate send ([PR#81](https://github.com/rimone0511/autopilot-log/pull/81) / #11 / #28)
- KYC / bank / phone-consult number
- Python posting-gate edits
- Copying PR#79 fences into `earn-packs/coconala/`
