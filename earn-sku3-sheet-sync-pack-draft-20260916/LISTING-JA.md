# Gumroad 出品文 — SKU-3（日本語）

机: Gumroad
商品: SKU-3 n8n Google シート同期パック
確認: 2026-09-16（公開ヘルプ: 商品の追加）
状態: **DRAFT_ONLY — フォームに貼るだけ。公開／有効化はしない**
言語: 日本語の出品文。英語 README は zip 側。
Google: MAIN Google のみ（`{{GOOGLE_ACCOUNT_EMAIL}}`）

入口:

- ダッシュボード: https://gumroad.com/
- ヘルプ（商品の追加）: https://gumroad.com/help/article/149-adding-a-product
- n8n の読み込み: https://docs.n8n.io/build/manage-workflows/export-and-import/
- n8n Google Sheets Trigger（購入者の後作業）: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.googlesheetstrigger/

新規商品の種類: **デジタル商品**（ファイル配布）。
メンバーシップ・Coffee・通話・コミッションにはしない。

---

## 0. ここまで（そのあと止める）

1. MAIN Google → Gumroad（2026-09-16 キューではログイン `done-draft`）。
2. **New product** → Digital product。
3. 名前・説明・要約・タグをこのファイルから貼る。
4. 価格は [PRICING.md](PRICING.md) の **プレースホルダだけ**。git に実売価を書かない。
5. Content タブに、このエージェントから顧客用 zip を上げない。添付は本人の後作業。
6. 商品が **未公開** のままか確認する。
7. 振込・口座・税・本人確認・Publish で **停止**。[DRAFT_ONLY.md](DRAFT_ONLY.md)。

カスタムパーマリンクを公開しない。`{{GUMROAD_PERMALINK_SKU3}}` はローカルだけ。

---

## 1. 商品名

貼る:

```
n8n シート同期パック — 新しい行は人へ、自動送信なし
```

| 数え | 値 |
|---|---|
| 商品名 | 29 字（空白・読点込み） |

「n8n AI エージェント 公式パートナー」などの詰め込みはしない。

---

## 2. CTA

ヘルプ: 用意された CTA から選ぶ。独自文言は作れない、と案内されている。

推奨: **I want this!**（画面が日本語なら、購入／ダウンロードに相当する項目）

Donate / Coffee 用の CTA は選ばない。

---

## 3. 要約（CTA の下）

貼る:

```
自分の n8n に入れるシート同期のスタブです。新しい行は人に知らせ、外へは出しません。自動送信はしません。
```

| 数え | 値 |
|---|---|
| 要約 | 54 字 |

---

## 4. 説明（日本語）

買い手向け。この欄に「未公開ドラフト」と書かない（あとで本人が公開したときに残る）。

```
SKU-3 は、自分の n8n で動かす Google シート同期パックです。

読み込む JSON は 2 本で、どちらも最初は停止したままです。1 本は入ってきた行（Google シートの行、または試験用の webhook）を保留します。もう 1 本は人への通知受付です。新しい行は人に知らせます。メール・チャット一斉送信・請求・公開投稿の自動送信はしません。自動送信フラグ、空の行、「もう送った」という自己申告は閉じた側（出さない）に倒れます。

入っているもの: 買い手 README、接続名だけのプレースホルダ（秘密の値もスプレッドシート ID も無し）、JSON スタブ。公式の API と webhook だけです。ブラウザ操作、スクレイピング、いいねやフォローの自動化は対象外です。

Google Sheets Trigger は任意で、スタブでは入っていません。読み込んだあと、n8n の接続画面で自分の Google 認証を作り、webhook を Trigger に差し替えられます。まだ OAuth を作りたくない場合は、webhook のままで構いません。

テンプレート販売です。n8n のホスティングでも、Google Workspace の管理でも、個別構築でも、n8n・Google・Gumroad の公式商品でもありません。個人の出品です。読み込んだあと、プレースホルダを自分の値に替え、ダミーで試し、本番のスイッチは自分だけが入れます。

含まれないもの: SKU-0 の受付スターター、SKU-1 の分類、SKU-2 の承認ゲート（出すときは別商品）、生きた鍵、同期速度の保証、代行送信。

自分の n8n の版で読み込めないときは、キャンバス上の付箋どおりに組み直してください。ダミーの送り方と、人が見る順番は README にあります。
```

---

## 5. 追加情報（任意欄）

```
形式: n8n ワークフロー JSON スタブ + Markdown README
実行場所: 購入者の n8n Cloud またはセルフホスト
初期状態: 停止（購入者が入れるまでオンにしない）
秘密: 鍵は n8n の接続画面で購入者が入れる。zip には入れない
ゲート: 新しい行は人へ通知。自動送信は拒否
言語: zip 内 README は英語。この出品文は日本語
```

---

## 6. タグ／分類

画面にタグがあれば:

```
n8n
自動化
ワークフロー
スプレッドシート
手順書
```

`xAI` / `Grok` / `ChatGPT` / 偽のパートナー語は付けない。

カテゴリ必須なら、ソフト／テンプレ／デジタル配布に近い項目。画像・動画・音声の AI 生成カテゴリには入れない。

---

## 7. パーマリンク（公開しない）

ローカルのみ:

```
{{GUMROAD_PERMALINK_SKU3}}
```

このパックから `gumroad.com/l/...` を告知しない。未公開の URL を売っている扱いにしない。

---

## 8. Content タブ（本人の後作業）

zip に入れるもの（エージェントは上げない）:

- `BUYER-README.md`
- `credentials.placeholders.json`
- `stubs/sku3-sheet-inbound.stub.json`
- `stubs/sku3-human-notify.stub.json`

オペレータ用（`LISTING-*.md`、`DRAFT_ONLY.md`、`PRICING.md`、パック `README.md`）は客向け zip に入れない。

カバー画像は、自分が撮った／作ったものがあるまで空。n8n や Google のロゴをパートナーの印のように使わない。

---

## 9. Versions

この SKU は **ダウンロード 1 種**。未契約の「設定通話つき」版は足さない。

---

## 10. 所属の一文

```
個人の出品です。n8n、Gumroad、Google、いずれの AI 企業のパートナー／社員でもありません。
```
