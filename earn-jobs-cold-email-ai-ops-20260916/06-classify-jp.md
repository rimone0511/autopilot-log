> **DRAFT_ONLY. DO NOT SEND.**  
> 精度○%や自動返信の約束は禁止。エージェントは送信しない。

# CE-06 — 問い合わせ分類（日本語）

## 運用表（本文に貼らない）

| key | value |
|---|---|
| pack | earn-jobs-cold-email-ai-ops-20260916 |
| id | CE-06 |
| theme | lead classify |
| lang | JP |
| mode | DRAFT_ONLY, HANDS |
| send | **禁止** |
| smb_label | `SMB-F`（架空） |
| chars_subject | short 17 / std 38 |
| chars_short | 398 |
| chars_standard | 664 |

事実は [FACTS.md](FACTS.md)。門は [DRAFT_ONLY.md](DRAFT_ONLY.md)。

想定の公開ページ: 請求・サポート・営業が一つの入口に混ざる。

範囲外: リスト購入、外向けシーケンス、根拠のない確度スコア。

---

## ヘッダ（git に実アドレスを書かない）

| 欄 | 値 |
|---|---|
| To | `{{RECIPIENT_EMAIL}}` — **git では空** |
| From | `{{SENDER_EMAIL}}` |
| 件名 | 下の短文または標準 |

---

## 送信ゲート

- [ ] 公開ページから `{{ONE_SPECIFIC_DETAIL}}` を取った
- [ ] 法的根拠を言える。言えなければ捨てる
- [ ] 送信しない

---

## 件名（短）

```
ラベルと保留箱。自動返信はしません
```

## 件名（標準）

```
『{{ONE_SPECIFIC_DETAIL}}』— 振り分けまで。不明は人
```

---

## 短文

```
{{RECIPIENT_NAME}} さま

公開の{{PUBLIC_PAGE_KIND}}で『{{ONE_SPECIFIC_DETAIL}}』を拝見しました。

いま使っているラベルで、請求／サポート／営業に振り、判断できないものは保留箱へ入れます。自動返信はしません。請求書も出しません。精度は保証しません。

{{DISPLAY_NAME}}です。日本、非同期 {{TIMEZONE}}。メモ: {{PORTFOLIO_URL}}

範囲外: リスト購入、外向け配信、根拠のないスコア。

{{QUESTION_1}}

一度きりの下書きです。

---
広告宣伝メールの下書き（未送信）
送信者: {{DISPLAY_NAME}}（日本） 住所: {{POSTAL_ADDRESS}}
以後の広告メールが不要なら {{OPT_OUT_CONTACT}} へ「配信停止」と返信してください。
```

---

## 標準文

```
{{RECIPIENT_NAME}} さま

公開の{{PUBLIC_PAGE_KIND}}で『{{ONE_SPECIFIC_DETAIL}}』を拝見しました。

{{DISPLAY_NAME}}です。仕事は、すでに届いている文面のタグ付けと振り分けです。ラベルは依頼者がいま使っているもの。不明は待つ。決めるのは人。リストは買いません。「確度」という数字も作りません。お客さまへの返信はしません。

かたちは、依頼者の n8n 上で公式コネクタだけ: 文面が入る → ラベルが出る → 不明は保留。AI は任意で、最初はオフ。付けるなら提案だけ。見るのは人です。

公開メモ: {{PORTFOLIO_URL}}。門が閉じたら公開しない公式APIの例: {{GITHUB_REPO_AUTOPILOT}}。

日本在住。日本語と英語。非同期 {{TIMEZONE}}。n8n のパートナーではありません。

{{QUESTION_1}}

一度きりの連絡の下書きです。すでに担当とキューがあるなら無視してください。

---
本メールはフリーランスの問い合わせ分類・振り分けに関する広告宣伝メールの下書きです。送信していません。
送信者: {{DISPLAY_NAME}} · {{CITY}} · {{COUNTRY}}
住所: {{POSTAL_ADDRESS}}
以後の広告メールを希望されない場合は、{{OPT_OUT_CONTACT}} へ「配信停止」と返信してください。
公開: {{PORTFOLIO_URL}}
```

---

## 架空の記入例（実在しない。送信禁止）

- ラベル: `SMB-F`
- `{{PUBLIC_PAGE_KIND}}` 例: `一つのフォームしかないお問い合わせ`
- `{{ONE_SPECIFIC_DETAIL}}` 例: `取材と見積と不具合が同じ欄`
- `{{QUESTION_1}}` 例: `いま使っているラベルは何で、保留を見る人は誰ですか。`

---

## STOP

- 「精度92%」と書かない
- 送信しない
