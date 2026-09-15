> **DRAFT_ONLY. DO NOT SEND.**  
> 「AIで時短○%」などの創作事例は禁止。エージェントは送信しない。

# CE-04 — AI ops 確認してから送る（日本語）

## 運用表（本文に貼らない）

| key | value |
|---|---|
| pack | earn-jobs-cold-email-ai-ops-20260916 |
| id | CE-04 |
| theme | AI ops |
| lang | JP |
| mode | DRAFT_ONLY, HANDS |
| send | **禁止** |
| smb_label | `SMB-D`（架空） |
| chars_subject | short 12 / std 47 |
| chars_short | 391 |
| chars_standard | 700 |

事実は [FACTS.md](FACTS.md)。門は [DRAFT_ONLY.md](DRAFT_ONLY.md)。

想定の公開ページ: 返信や投稿の下書きはあるが、モデルに送信させたくない。

範囲外: 無人の外向け送信、出典の捏造、本人確認の代行。

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
下書きはAI、送信は人手
```

## 件名（標準）

```
『{{ONE_SPECIFIC_DETAIL}}』— 確認キューであり、自動送信ではありません
```

---

## 短文

```
{{RECIPIENT_NAME}} さま

公開の{{PUBLIC_PAGE_KIND}}で『{{ONE_SPECIFIC_DETAIL}}』を拝見しました。

引き受ける作業は、下書き→人が見る→送信または公開、という AI ops です。モデルがお客さまへ直接メールすることはしません。

{{DISPLAY_NAME}}です。日本、非同期 {{TIMEZONE}}。メモ: {{PORTFOLIO_URL}}

範囲外: 人手確認なしの送信、出典の捏造、本人確認の代行。

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

{{DISPLAY_NAME}}です。二人が同じ手順で再実行できるループを組みます。モデルは下書きを出してよい。読むのは人。送信と公開のスイッチは人に残します。時短時間は書きません。出典も作りません。依頼者のメール送信ボタンは押しません。

公開メモ: {{PORTFOLIO_URL}}。「動いている」と「公開してよい」を分けた公式APIの例: {{GITHUB_REPO_AUTOPILOT}}。そこでの TikTok の既定は受信箱アップロードで、無人投稿ではありません。

小さく範囲を切るなら、運用メモと確認ステップと、開くまで閉じた門です。自律エージェント一式ではありません。

日本在住。日本語と英語。非同期 {{TIMEZONE}}。モデル会社の社員ではありません。独立の個人です。

{{QUESTION_1}}

一度きりの連絡の下書きです。すでに社内の確認者がいるなら無視してください。

---
本メールはフリーランスの AI ops（下書き→確認→人が承認）に関する広告宣伝メールの下書きです。送信していません。
送信者: {{DISPLAY_NAME}} · {{CITY}} · {{COUNTRY}}
住所: {{POSTAL_ADDRESS}}
以後の広告メールを希望されない場合は、{{OPT_OUT_CONTACT}} へ「配信停止」と返信してください。
公開: {{PORTFOLIO_URL}}
```

---

## 架空の記入例（実在しない。送信禁止）

- ラベル: `SMB-D`
- `{{PUBLIC_PAGE_KIND}}` 例: `サポート案内`
- `{{ONE_SPECIFIC_DETAIL}}` 例: `チャットボットではなく指定のメールへ、と書いてある`
- `{{QUESTION_1}}` 例: `いま下書きの返信を送ってよい人は誰ですか。`

---

## STOP

- 「AIが千通送った」と書かない
- 送信しない
