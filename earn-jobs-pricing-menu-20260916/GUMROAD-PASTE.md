# Gumroad paste — DRAFT_ONLY

Desk: Gumroad (digital product)  
Pack: 2026-09-16  
Mode: **DRAFT_ONLY — fill the form, never Publish / Enable**

Help — Adding a product: https://gumroad.com/help/article/149-adding-a-product  
n8n import: https://docs.n8n.io/build/manage-workflows/export-and-import/

Product type: **Digital product**. Not membership, coffee, call, or commission.  
Google: MAIN only (`{{GOOGLE_ACCOUNT_EMAIL}}`).

Price: paste `{{PRICE_USD_SKU_*}}` only. Gumroad help: free or up to USD 5,000. That is a bound, not a quote.  
Pay what you want: **off**. No compare-at / fake discount. No max-purchase scarcity.

Do not attach a customer zip from this agent. Do not announce `gumroad.com/l/...`.  
Stop at payout / bank / tax / ID. See [DRAFT_ONLY.md](DRAFT_ONLY.md).

Sibling listing bodies (use those for the long description if the product pack exists):

| SKU | Long listing | This file |
|---|---|---|
| starter | No SKU-0 pack on `master`. Use the short paste below | name + summary + price token |
| classifier | PR #37 `LISTING-EN.md` / `LISTING-JA.md` | align the **name** (60 chars EN) |
| approval-gate | PR #46 same pattern | align the **name** |
| docs | none | this file is the listing paste |

CTA: built-in **I want this!** (help: do not invent a custom CTA).

---

## 1. n8n starter (SKU-0 shape)

### Name EN

```
n8n Starter Intake Pack — form to table, you send
```

### Name JA

```
n8n 受付スターター — 表に入れて、送信は人
```

### Summary EN

```
Importable n8n stubs: intake lands in a table, a person is notified, you send. No auto-reply.
```

### Summary JA

```
受付を表に入れ、人へ知らせる n8n スタブです。返信は人がします。自動送信しません。
```

### Price

| Field | Paste |
|---|---|
| Price | `{{PRICE_USD_SKU_STARTER}}` |
| Optional JP note (description only) | `{{PRICE_JPY_DISPLAY_SKU_STARTER}}` |

### Description EN (buyer-facing; no “unpublished”)

```
This is a starter n8n intake pack you run on your own instance.

Inbound (form, webhook, or sheet row) lands in a table. A person is notified. You send. The pack does not auto-reply, auto-invoice, or post in your name.

You get a short operator README and inactive workflow stubs (official APIs and webhooks only). No browser bots, scraping, or engagement automation.

This is a template pack, not n8n hosting, not a custom build, and not an official n8n or Gumroad product. After import, replace every placeholder, test with dummy data, and only you turn a workflow on.

Not included: classifier labels, approval-before-send, live credentials, or guaranteed time saved.

Revisions: a digital download is as-is. Same-scope file fixes, if offered, follow the seller menu (1 clarification in the delivery window for a custom fit — that custom fit is a separate service, not this zip).
```

### Description JA

```
自分の n8n で動かす受付スターターです。

フォームや表からの入力を表に入れ、人へ知らせます。返信・公開は人がします。自動送信しません。

手順の短い README と、停止中のワークフロースタブ（公式の接続と Webhook のみ）が入ります。ブラウザ自動操作、スクレイピング、いいね自動化は含みません。

テンプレであり、n8n のホスティングでも公式製品でもありません。取り込み後、プレースホルダを置き、ダミーで試し、オンにするのは購入者です。

含まないもの: ラベル分け、承認ゲート、本物の鍵、短縮時間の保証。
ダウンロード自体の「修正回数」はありません。同じ範囲のカスタム調整は別サービスです。
```

Tags (if the form shows them): `n8n` `automation` `workflow` `intake` `operator-docs`  
Do not tag `xAI`, `Grok`, `ChatGPT`, or partner words.

---

## 2. classifier (align SKU-1)

### Name EN (60 characters — keep in sync with PR #37)

```
n8n Inquiry Classifier Pack — labels, hold queue, human send
```

### Name JA

```
n8n 問い合わせ分類パック — 迷ったら未確定、送信は人
```

### Summary EN

```
Importable n8n stubs that label inbound text and park anything unclear. You send. No auto-reply.
```

### Price

`{{PRICE_USD_SKU_CLASSIFIER}}` / optional `{{PRICE_JPY_DISPLAY_SKU_CLASSIFIER}}`

Long description: paste from sibling `earn-sku1-n8n-pack-draft-20260916/LISTING-EN.md` (and JA) if that folder is on the branch you are filling. Do not invent a second product name.

If the sibling folder is absent, use:

```
SKU-1 is an n8n inquiry classifier pack you run on your own instance.

Inbound text is mapped onto labels you already use. Unclear messages go to uncertain / hold. Nothing is auto-replied or posted in your name.

Official APIs and webhooks only. AI is optional and off in the stubs. Not n8n hosting. Not an official n8n product.

Not included: starter intake as a bundle, approval-before-send, live credentials, or accuracy %.
Digital download is as-is. A custom relabel is a separate service.
```

---

## 3. approval-gate (align SKU-2)

### Name EN (60 characters — keep in sync with PR #46)

```
n8n Approval-Gated Notify — human must approve first to send
```

### Name JA

```
n8n 承認ゲート通知パック — 外に出す前に人が承認
```

### Summary EN

```
n8n stubs that hold outbound until a person approves. Reject, missing, or timeout fail closed.
```

### Price

`{{PRICE_USD_SKU_APPROVAL}}` / optional `{{PRICE_JPY_DISPLAY_SKU_APPROVAL}}`

Long description: sibling `earn-sku2-approval-gate-pack-draft-20260916/LISTING-EN.md` when present. Fallback:

```
This pack is an n8n approval gate you run on your own instance.

Nothing goes outbound until a person approves. Reject, missing, unknown, and timeout fail closed. There is no auto-send-on-timeout.

Official APIs and webhooks only. Live send credentials are not in the zip. Not n8n hosting. Not an official n8n product.

Not included: classifier labels as a bundle, SLA, or sending mail for you.
Digital download is as-is. Wiring a live notify node is a separate service.
```

---

## 4. docs

### Name EN

```
n8n Operator Docs Pack — SOP and rerun notes, no new flow
```

### Name JA

```
n8n 手順書パック — 再実行できるメモ、新規フローなし
```

### Summary EN

```
Markdown SOP for a workflow you already have: rerun, secrets vs edits, failure steps. No new flow.
```

### Summary JA

```
既存フロー向けの手順書です。再実行と秘密の区別を書きます。新しいフローは作りません。
```

### Price

`{{PRICE_USD_SKU_DOCS}}` / optional `{{PRICE_JPY_DISPLAY_SKU_DOCS}}`

### Description EN

```
This is a documentation pack, not a new n8n workflow.

You get Markdown: what starts the flow, what is safe to edit, where secrets live, how to rerun, and what to do when it fails. If you send screenshots with secrets hidden, the notes follow your screen names.

It does not include a new workflow, hosting, live credentials, or browser automation. I am an independent seller, not a partner of n8n or Gumroad.

Digital download is as-is. A custom rewrite against a different stack is a separate service.
```

### Description JA

```
新しい n8n フローではなく、手順書のパックです。

何が始まるか、編集してよい欄、秘密の置き場、再実行、失敗したときの順を Markdown で渡します。秘密を隠した画面があれば、その呼び名に合わせます。

新しいフロー、ホスティング、本物の鍵、ブラウザ自動操作は含みません。n8n / Gumroad の公式パートナーではありません。

ダウンロードは現状のファイルです。別スタックへの書き直しは別サービスです。
```

Tags: `n8n` `documentation` `sop` `runbook` `operator-docs`

---

## 5. Gumroad-wide revision note (all four)

Gumroad is a **file download**. Do not promise Fiverr-style revision counts inside the zip product.

If a human later sells a **custom fit** of the same SKU as a service (Coconala / Contra), use the revision counts in [SKU-MENU-EN.md](SKU-MENU-EN.md). Do not mix those counts into the Gumroad price box.

---

## 6. Character counts (fenced paste, `len()`, placeholders unsubstituted, 2026-09-16)

Live form wins. Gumroad help 149 does not cite a name/summary ceiling in the sibling SKU packs; SKU-1/2 names were kept at **60** English characters.

| Block | This pack |
|---|---|
| Name EN starter / classifier / approval / docs | 49 / 60 / 60 / 57 |
| Name JA ×4 | 24 / 29 / 27 / 29 |
| Summary EN ×4 | 93 / 96 / 94 / 98 |
| Description EN starter / classifier fallback / approval fallback / docs | 882 / 493 / 470 / 503 |
| Description JA starter / docs | 305 / 209 |

Classifier and approval-gate **names** match sibling PRs #37 and #46. Prefer those packs’ long listings when the folders are on the filling branch.

Do not keyword-stuff “official partner” or lab names.
