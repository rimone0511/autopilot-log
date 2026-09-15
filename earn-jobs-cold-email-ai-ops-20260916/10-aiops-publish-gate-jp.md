> **DRAFT_ONLY. DO NOT SEND.**  
> TikTok を無人投稿とは書かない。再生数などの創作禁止。エージェントは送信しない。

# CE-10 — AI ops 公開の門は閉じたまま倒れる（日本語）

## 運用表（本文に貼らない）

| key | value |
|---|---|
| pack | earn-jobs-cold-email-ai-ops-20260916 |
| id | CE-10 |
| theme | AI ops |
| lang | JP |
| mode | DRAFT_ONLY, HANDS |
| send | **禁止** |
| smb_label | `SMB-J`（架空） |
| chars_subject | short 19 / std 35 |
| chars_short | 468 |
| chars_standard | 684 |

事実は [FACTS.md](FACTS.md)。門は [DRAFT_ONLY.md](DRAFT_ONLY.md)。

想定の公開ページ: 小さな店や制作が、定期の投稿や案内メールに触れている。

正直に言ってよい公開ツール: Autopilot Log の投稿ゲートは壊れたら閉じる。未審査の YouTube API は非公開のまま。TikTok の既定は受信箱。クライアント事例ではない。

範囲外: 反応ボット、スクレイピング、「門なしで投稿代行」。

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
動いていることと、公開してよいことは別
```

## 件名（標準）

```
『{{ONE_SPECIFIC_DETAIL}}』— 送信と公開は人手
```

---

## 短文

```
{{RECIPIENT_NAME}} さま

公開の{{PUBLIC_PAGE_KIND}}で『{{ONE_SPECIFIC_DETAIL}}』を拝見しました。

AI ops と公式APIの作業では、「ジョブが動いている」と「公開してよい」を分けます。門が無い・壊れているときは公開しません。投稿ボタンは代行しません。

{{DISPLAY_NAME}}です。日本、非同期 {{TIMEZONE}}。メモ: {{PORTFOLIO_URL}}

公開の例（成果数値ではない）: {{GITHUB_REPO_AUTOPILOT}} — YouTube は審査と門の前は非公開。TikTok の既定は受信箱で、無人投稿ではありません。

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

{{DISPLAY_NAME}}です。すでに投稿や案内をしている中小向けに、公式APIと人手のストップを組みます。サイトに住み着くボットではありません。下書きは機械が手伝ってよい。送信・公開・支払いは人です。門のファイルが無い、読めない、壊れているときは、閉じた側に倒れます。

その分け方で作ってある公開ツール（鍵は運用者のもの。ログに秘密を出さない）: {{GITHUB_REPO_AUTOPILOT}}。御社で動いているとは言いません。再生数も言いません。そこでの TikTok は既定が受信箱アップロードです。

公開メモ: {{PORTFOLIO_URL}}。日本在住。日本語と英語。非同期 {{TIMEZONE}}。独立の個人です。

{{QUESTION_1}}

一度きりの連絡の下書きです。すでに閉じた公開スイッチと担当がいるなら無視してください。

---
本メールはフリーランスの AI ops（送信・公開の門は閉じたまま倒れる）に関する広告宣伝メールの下書きです。送信していません。
送信者: {{DISPLAY_NAME}} · {{CITY}} · {{COUNTRY}}
住所: {{POSTAL_ADDRESS}}
以後の広告メールを希望されない場合は、{{OPT_OUT_CONTACT}} へ「配信停止」と返信してください。
公開: {{PORTFOLIO_URL}}
```

---

## 架空の記入例（実在しない。送信禁止）

- ラベル: `SMB-J`
- `{{PUBLIC_PAGE_KIND}}` 例: `お知らせ`
- `{{ONE_SPECIFIC_DETAIL}}` 例: `更新曜日は書いてあるが、アプリで確認してほしいとある`
- `{{QUESTION_1}}` 例: `公開ボタンを押してよい人は誰で、下書きを回す人と同じですか。`

---

## STOP

- 「登録者1万を自動化」と書かない
- 送信しない
