> **DRAFT_ONLY. DO NOT SEND.**  
> 実在メンバー名禁止。つながり申請は送信しない。秘密を書かない。エージェントは送信しない。

# LI-W2-02 — つながりメモ: n8n（日本語）

## ファクト表（運用。本文に貼らない）

| key | value |
|---|---|
| pack | earn-linkedin-outreach-wave2-20260916 |
| id | LI-W2-02 |
| desk | LinkedIn 個人プロフィール |
| type | つながり申請の **メモ** |
| seller_theme | n8n workflow |
| lang | JP |
| mode | DRAFT_ONLY, HANDS paste |
| draft | true |
| send | **禁止** |
| promotional_note | **禁止**（コミュニティポリシー） |
| urls_in_note | no |
| rate_in_prose | no |
| char_limit | 200（Basic。画面カウンタを正とする） |
| chars_note | 103 |
| detail_budget | `{{ONE_SPECIFIC_DETAIL}}` を短く。置換後に再計測 |

想定のきっかけ（実在しない）: n8n・公式API・送信前の人手確認についての公開投稿または見出し。1分で指せなければスキップ。

使わないもの: サービスの売り込み、InMail、「一度通話を」、スクレイピング、パートナー称号。

---

## 画面の別欄（本文に埋め込まない）

| 欄 | 貼る値 |
|---|---|
| メモを追加 | 下のフェンス |
| 送信 | **押さない** — [STOP-AT-PUBLISH.md](STOP-AT-PUBLISH.md) |
| InMail | 開かない |

きっかけが空 → 送らない。月のメモ上限 → `note_cap_hit` で止める。空の申請で逃げない。

---

## 送信ゲート

- [ ] linkedin.com で **この** プロフィールを開いた
- [ ] `{{ONE_SPECIFIC_DETAIL}}` は公開されている投稿または見出しから取った
- [ ] 売り込み文になっていない
- [ ] URL・メール・電話・予約リンクが無い
- [ ] 置換後も 200 字以内
- [ ] このパックから送信しない

---

## つながりメモ（置換後 ≤200）

```
『{{ONE_SPECIFIC_DETAIL}}』を拝見しました。n8nは公式コネクタと送信前の人手ストップだけです。{{DISPLAY_NAME}}（日本）。売り込みではなく同業者としてつながりたいです。
```

---

## 架空の記入例（実在しない。学習用。送信禁止）

- ラベル: `相手B`（架空）
- `{{ONE_SPECIFIC_DETAIL}}` 例: `公式Webhookだけで止める話`
- `{{DISPLAY_NAME}}` 例: `石田祐太`

置換例（計測用）: `『公式Webhookだけで止める話』を拝見しました。n8nは公式コネクタと送信前の人手ストップだけです。石田祐太（日本）。売り込みではなく同業者としてつながりたいです。`

---

## STOP

- きっかけの無い申請にこのメモを付けない
- サービス案内に書き換えない
- 送信しない
