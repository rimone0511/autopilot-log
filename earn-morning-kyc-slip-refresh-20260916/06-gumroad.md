# Slip — Gumroad

**DRAFT_ONLY.** 商品（SKU-0 / SKU-1）は unpublished。Publish / Enable しない。  
**エージェントは signup しない。アップロードしない。商品を公開しに戻らない。**

| | |
|---|---|
| Desk | Gumroad（Wave A+。CU-11 をずらさない） |
| CU hint | `draft_saved`（QUEUE `done-draft`。MAIN Google ログイン確認済み） |
| Who | **祐太だけ** |
| 入口 | Payout / Payments settings（ライブメニューを正） |
| いつ | **出金が必要になった朝**。下書き商品のため先回りしない |

---

## この机のいま

ログイン済み・商品は下書き。PR#4 の朝1枚では **対象外** だった。  
`draft_saved` なので **公開しに戻らない**。Stripe の本人確認は売上・出金のあとで出やすい。売り上げゼロの下書きでは、Payout を開かなくてよい。

SKU パック（[PR#37](https://github.com/rimone0511/autopilot-log/pull/37) など）は paste だけ。エージェントは Gumroad 商品を作らない・公開しない。

---

## 上げるもの（サイトの画面にだけ。出金画面が出たとき）

Gumroad のカード／銀行出金は **Stripe の KYC**（国で中身が変わる）。画面が求めたものだけ。

よく出るもの（公式 payout 案内の要約。画面を正）:

- 氏名（書類どおり。ミドルネームがあれば含める）
- 実在の住所（PO Box 不可、と公式）
- 政府発行フォトID（免許は **表裏**、パスポート。JPEG/PNG。**PDF は上げない**、と公式）
- 画面が求めたときだけ住所証明（公共料金など）

PayPal 出金だけなら ID 不要、と公式 payout 設定の案内がある。**銀行を足すために ID を先回りしない。** 日本の売り手は US SSN / W-9 を出さない。

ヘルプ:  
https://gumroad.com/help/article/13-getting-paid  
https://gumroad.com/help/article/260-your-payout-settings-page

---

## 上げない / やらない

- [ ] **Publish / Enable** / 公開パーマリンク / `gumroad.com/l/...` を「発売」と告知
- [ ] SKU-0 / SKU-1 をエージェントのブラウザから作る・zip を付ける
- [ ] 銀行・Stripe 出金を、下書きだけの今の朝に無理に完了する
- [ ] マイナンバー番号、税ID、口座番号を git / チャットに書く
- [ ] Gumroad Discover / boost / 独自ドメイン購入
- [ ] n8n / ラボ / Gumroad の提携バッジを名乗る
- [ ] 売上件数・GMV を書く
- [ ] 書類を git / チャット / エージェントへ
- [ ] 2つ目の Gumroad を作る

---

## DRAFT_ONLY reminder

本人確認は **出金の門**。商品を公開する門ではない。  
`draft_saved` のまま次へ。公開は人が別の朝に決める。

状態: `なし` / `上げた` / `待ち` / `詰まった` / `draft_savedのまま`
