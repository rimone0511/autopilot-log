# CHECKLIST — Coconala draft_saved → publish-ready (unpublished)

Pack date: 2026-09-16  
Desk: ココナラ / Coconala  
Start: profile **`draft_saved`**  
End of this pack: **`publish_ready_unpublished`** or a named gap  
Mode: **DRAFT_ONLY.** [HUMAN-GO.md](HUMAN-GO.md) stays closed.

Tick on a **local** copy. Point at first-gig paste; do not paste sibling fences into git.

First-gig pack: `earn-jobs-coconala-first-gig-full-paste-20260916/` ([PR#87](https://github.com/rimone0511/autopilot-log/pull/87)).  
Default listing this pass: `SERVICE-PASTE.md`.  
Do not also paste [PR#79](https://github.com/rimone0511/autopilot-log/pull/79) `01` onto a second listing.

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
- [ ] Read [README.md](README.md) first-gig table. Open PR#87 `SERVICE-PASTE.md` in another window. Do not copy fenced bodies into this repo.

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
- [ ] If **one** draft matches first-gig #87 (n8n 小さな自動化 1本): use that. Do not open a second “test” listing.
- [ ] If it matches #79 `01` instead (`n8n自動化と手順書を作ります`): treat as the **same first-gig family**. Fill gaps from **#87** (FAQ 7, TOC, image rule) rather than creating a second listing.
- [ ] If **several** drafts: do not guess. List as `present / mismatch` in a local GAPS copy (not the live URL). Pick the n8n-1本 draft or stop.
- [ ] If **no** service draft: create **one** 通常サービス from PR#87 `SERVICE-PASTE.md` only. Still **下書き**. Do not also create #79 `01`/`02`/`03` this pass.
- [ ] If the row is already **公開中**: `already_published`. Do not unpublish from an agent. Stop.
- [ ] 見積もり・カスタマイズ: #87 §8.2 — live checkboxes win. 受付する ≠ 見積もり送信.

#79 `02` / `03` remain optional later drafts (different offers). Coconala ルール: 同一サービスの複数出品は禁止。タイトルを変えただけのコピーを作らない。

---

## 4. Fields (paste from first-gig — do not rewrite from memory)

Ceilings (public news/guide; **live counter wins**):

| 欄 | Ceiling cited | First-gig #87 (do not re-copy fences here) |
|---|---|---|
| サービスタイトル（ます止め） | 25 (news 170) | `n8nの小さな自動化を1本作ります` (17; form may store 15 without ます) |
| キャッチコピー | 30 | 23 |
| サービス内容 | news 1220: 1000 通常 / news 1372: 1500 cited by #87. **Counter wins.** Do not buy セラーサポート | #87 body measured 953 |
| 購入にあたってのお願い | live / #87 358 | #87 §8.1 |
| 有料オプション名 | 60 / max 10 (sibling #79) | #87 §6 four optional rows, prices empty |

Category from PR#87 (live dropdown wins; do not type IDs):

| 段 | 値 |
|---|---|
| 大 | IT相談・システム開発 |
| 中 | 業務自動化・効率化支援 |
| 小 | **API連携・開発** (`/categories/230/739` as a public tree hint only) |

Fallback if that leaf is missing: その他（業務自動化・効率化）— that is #79 `01`’s leaf, not a second listing.  
入れない: Excelマクロ専用、GAS専用、RPA、AI画像/動画/音声、AIエージェント開発、占い。

Ticks:

- [ ] 種類 = **通常サービス**（メッセージ完結）。ビデオチャット表示オフ。物販配送オフ。
- [ ] カテゴリ = table above or nearest live node. Not a duplicate of another of your listings.
- [ ] タイトル = PR#87 §1.1 fence. Form may auto-append「ます」— do not double it. Counter ≤ 25.
- [ ] キャッチ = PR#87 §1.2 fence. Counter ≤ 30.
- [ ] サービス内容 = PR#87 §3 TOC + §4 body (not Wave 1/2 / #81 estimate files). Stay under the **live** counter (1000 or 1500).
- [ ] 範囲外ブロックが本文に残っている（ブラウザ自動操作・無人公開・鍵の代理入力）。
- [ ] パートナー名乗りが無い（n8n / ココナラ / AI 企業）。
- [ ] 未確認の件数・時短・精度・収入保証が無い。
- [ ] 提供形式 = #87 §2.1 (制作物 + テキスト。ビデオチャット役務にしない).
- [ ] 料金: if the form has **3 プラン**, use #87 §5.1 tokens. If **one** サービス価格 only, use §5.2 `{{TIER_STANDARD_YEN}}`. Days: 5 / 7 / 10 as paste hints — live field wins.
- [ ] 一度に受注可能な件数 = **1** (#87 §5.3).
- [ ] 有料オプション: #87 §6. Empty token → do not add the row. Do not make options required.
- [ ] 購入にあたってのお願い = PR#87 §8.1. 鍵をトークに貼らせない。
- [ ] 見積もりチェック = PR#87 §8.2 (live). That is not 見積もり送信.
- [ ] Pricing-menu [#82](https://github.com/rimone0511/autopilot-log/pull/82) titles are **overlay only**. Do not retitle over #87 in the same pass.

`{{PORTFOLIO_URL}}` : public `https://yutalab.dev/` is allowed. If the live form rejects external URLs in サービス内容, move it out (profile / お願い) rather than fighting the filter.

---

## 5. Images / video

Guide_sell ステップ3: 成果物サンプル or イメージ画像.  
マグ「サービスページのコツ」: **画像は必ず設定**. 1枚目が検索結果。  
News 1372 (cited by #87): **新規出品は公開時にサービス画像 1枚以上**. Already-public listings without images are a different exception — not this first gig.  
#87 §9: if **下書き保存** works with no image, skip upload this pass. If save **requires** an image, use an original redacted workflow screenshot only (`{{PROFILE_PHOTO_LOCAL_PATH}}` locally). **This checklist** still treats missing images as a **HUMAN-GO blocker** (公開する needs ≥1).

- [ ] Look at the image slots on the existing draft. Do **not** upload from the pack-author agent.
- [ ] If empty and 下書き保存 succeeds: record `images_missing`. Human adds originals **before** any GO. Still save 下書き.
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
First-gig #87: git keeps **`{{YEN}}` / `{{TIER_*_YEN}}` / `{{OPTION_*_YEN}}`**. Overlay #82 uses `{{PRICE_JPY_SKU_*}}`. Same rule: no filled yen in git.

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

マグ: よくある質問は購入前のずれを減らす欄。  
First-gig #87 §7 = **seven** Q/A pairs (通説 max 7). Do not copy them into this file. Paste from `SERVICE-PASTE.md`.

| # | Operator hint (open PR#87 for the fences) |
|---|---|
| 1–7 | Affiliation, secrets, SNS/unattended, n8n hosting, 1本 scope, revisions/options, 公式API-only |

- [ ] Seven pairs pasted from **#87 §7**, not from Fiverr English FAQ packs and not a second copy of #79 `01`’s six.
- [ ] Buyer-facing answers do not say DRAFT / 未公開.
- [ ] No fake affiliation, no accuracy %, no “必ず成果”.
- [ ] Secrets stay on the buyer’s n8n connection screen. Never “トークに貼ってください”.
- [ ] If the live form allows fewer than 7: keep affiliation, secrets, SNS, 範囲外 first. Note `faq_trimmed` in GAPS.

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
first_gig_source: PR87 | PR79-01-same-family | PR79-02 | PR79-03 | other | missing
fields: pasted | partial | not-entered
images: none | original-ok | images_missing | needs_human
price: placeholder-local | rate_empty | saved-not-in-git
faq: 0-7
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
- #79 `01` as a second n8n listing next to #87
- #79 `02` / `03` live create in the same sitting (optional later, still unpublished)
- Estimate send ([PR#81](https://github.com/rimone0511/autopilot-log/pull/81) / #11 / #28)
- KYC / bank / phone-consult number
- Python posting-gate edits
- Copying PR#87 / #79 fences into `earn-packs/coconala/`
