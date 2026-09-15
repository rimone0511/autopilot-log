> **DRAFT_ONLY. DO NOT SEND.**  
> 「データを一度も壊したことがない」などの創作は禁止。エージェントは送信しない。

# CE-08 — n8n 既存の表を壊さない（日本語）

## 運用表（本文に貼らない）

| key | value |
|---|---|
| pack | earn-jobs-cold-email-ai-ops-20260916 |
| id | CE-08 |
| theme | n8n workflow |
| lang | JP |
| mode | DRAFT_ONLY, HANDS |
| send | **禁止** |
| smb_label | `SMB-H`（架空） |
| chars_subject | short 18 / std 45 |
| chars_short | 410 |
| chars_standard | 679 |

事実は [FACTS.md](FACTS.md)。門は [DRAFT_ONLY.md](DRAFT_ONLY.md)。

想定の公開ページ: 予約や依頼を表で管理している、と書いてある。

範囲外: 本番表の上書き、非公式の画面操作、パートナー称号。

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
行を足すだけ。本番の表はダミーのあと
```

## 件名（標準）

```
『{{ONE_SPECIFIC_DETAIL}}』— n8n は追記。黙って上書きしません
```

---

## 短文

```
{{RECIPIENT_NAME}} さま

公開の{{PUBLIC_PAGE_KIND}}で『{{ONE_SPECIFIC_DETAIL}}』を拝見しました。

公式コネクタで行を追記する n8n を、コピー側で先に動かします。本番の表はダミーではありません。対応づけは人が確認します。勝手に「整理」しません。

{{DISPLAY_NAME}}です。日本、非同期 {{TIMEZONE}}。メモ: {{PORTFOLIO_URL}}

範囲外: スクレイパー、表の画面をクリックするボット、データ損失ゼロの保証。

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

{{DISPLAY_NAME}}です。引き受ける小さな作業は、フォームやメールから、ドキュメントのある表のコネクタへ、人が「上書きしてよい」と言うまで追記だけ、という形です。最初はダミー。そのあと、既存の行が残っているかを見ます。鍵は依頼者の n8n に残します。ブックのコピーは持ち帰りません。

公開メモ: {{PORTFOLIO_URL}}。事故で公開しない側に倒す公式APIの例: {{GITHUB_REPO_AUTOPILOT}}。

範囲を名前にするなら: オフのフロー、列の対応（秘密は書かない）、再実行メモ、本番タブを差し替えていないことの記録。

日本在住。日本語と英語。非同期 {{TIMEZONE}}。Google や n8n のパートナーではありません。

{{QUESTION_1}}

一度きりの連絡の下書きです。すでに表の担当がいるなら無視してください。

---
本メールはフリーランスの n8n と表のつなぎに関する広告宣伝メールの下書きです。送信していません。
送信者: {{DISPLAY_NAME}} · {{CITY}} · {{COUNTRY}}
住所: {{POSTAL_ADDRESS}}
以後の広告メールを希望されない場合は、{{OPT_OUT_CONTACT}} へ「配信停止」と返信してください。
公開: {{PORTFOLIO_URL}}
```

---

## 架空の記入例（実在しない。送信禁止）

- ラベル: `SMB-H`
- `{{PUBLIC_PAGE_KIND}}` 例: `予約・依頼の案内`
- `{{ONE_SPECIFIC_DETAIL}}` 例: `依頼は表にまとめる、と書いてある`
- `{{QUESTION_1}}` 例: `本番のタブはどれで、触ってはいけないコピーはありますか。`

---

## STOP

- 「店舗○店で無停止」と書かない
- 送信しない
