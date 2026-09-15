> **DRAFT_ONLY. DO NOT RECORD. DO NOT SEND.**  
> Dummy data only. No live sheet. No live notify. Agent does not click Record.

# JOBS-DEMO-01 — Form → sheet → notify

## Fact table (operator; do not put on camera)

| key | value |
|---|---|
| pack | earn-jobs-demo-scripts-n8n-20260916 |
| id | JOBS-DEMO-01 |
| theme | form → sheet → notify |
| buyer_value | Intake becomes a row a person can see. The ping is a hold, not a send. |
| mode | DRAFT_ONLY, HANDS talk-through / later Loom |
| draft | true |
| record | **forbidden** from this pack |
| runtime_target | 90–120 seconds |
| sibling_shape | SKU-0 starter intake (zip not in this repo) |
| related_proposal | JP-W2-01; EN n8n workflow covers |

Assumed buyer (not a real company): a small team pasting form answers into a spreadsheet, then pinging chat by hand.

Out of scope: browser automation, scraping, list-mail from n8n, partner-badge impersonation, live customer PII.

---

## Why this demo (buyer)

**EN.** Copy-paste from a form into a sheet is slow and easy to skip. n8n can append the row the moment the form lands. A person still decides whether anything leaves the building. This walkthrough uses a fictional “office closed tomorrow” row. Nothing is mailed.

**JA.** フォームの内容を表へ手で移す作業は漏れやすいです。n8n は行を足せます。外へ出す判断は人のままです。この動画は架空の「明日休業」1件だけです。実送信しません。

---

## Props (dummy only)

| Prop | Safe rehearsal |
|---|---|
| Form | Webhook POST or n8n Form with the JSON below |
| n8n canvas | Inactive: Webhook → (optional Set) → Sheets append stand-in → NoOp notify |
| Sheet tab | `EXAMPLE-ONLY` — columns `status`, `note`, `auto_send` |
| Notify | Sticky note “operator ping — not sent”. Do not attach Slack/mail credentials |
| Browser chrome | Crop `{{N8N_BASE_URL}}` and any webhook token |

### Dummy payload (fictional)

```json
{
  "source": "form-stub",
  "sheet_name": "EXAMPLE-ONLY",
  "status": "new",
  "note": "EXAMPLE-ONLY — office closed tomorrow",
  "auto_send": false
}
```

If `auto_send` is true, **stop the take**. Say that this path refuses. Do not “just send it so the demo looks finished.”

---

## Shot list (Loom outline)

| t | Screen | Say / do | Do not |
|---|---|---|---|
| 0:00–0:08 | Title card or face + name | One-line promise | Logo wall, “official n8n partner” |
| 0:08–0:20 | Dummy form | Submit the fictional row | Real customer name |
| 0:20–0:45 | n8n canvas (Inactive) | Point: trigger → row → ping hold | Open Credentials UI |
| 0:45–1:05 | Sheet tab `EXAMPLE-ONLY` | New row, `auto_send` false | Live spreadsheet ID in the URL bar |
| 1:05–1:25 | Notify node / sticky | “Ping is a hold. You send.” | Click a live Slack Send |
| 1:25–1:50 | Face or canvas zoom-out | What they would own; two questions | Price, hours saved, GMV |

Cut at 2:00 even if you skip the “what you would own” sentence.

---

## Spoken EN

Rewrite `{{ONE_SPECIFIC_DETAIL}}` before a real conversation. This fence is the take.

```
You mentioned {{ONE_SPECIFIC_DETAIL}}. I would start with one n8n path: form to sheet to a human ping. Not a blast.

I am {{DISPLAY_NAME}}. I work from Japan, async in {{TIMEZONE}}. I build this on your n8n, with official connectors only. I do not drive browsers. I do not scrape.

Watch a dummy submit. The note is “office closed tomorrow.” No real customer.

n8n appends a row and parks a notify. In this demo the notify node is a hold. It does not email your list. It does not post.

Here is the sheet tab EXAMPLE-ONLY. Status new. Auto-send false. If auto-send were true, this path would refuse.

After a real job you would own the workflow in your workspace, a short SOP, and the send button still in a person’s hands. Public notes: {{PORTFOLIO_URL}}. Same fail-closed habit: {{GITHUB_REPO_AUTOPILOT}}.

Two questions:
1. Is the source of truth the form, or the sheet?
2. Who is allowed to retry a failed write — you, or anyone with the tab?
```

---

## Spoken JA

実会話の前に `{{ONE_SPECIFIC_DETAIL}}` を差し替える。このフェンスが本番の台詞。

```
ご相談の {{ONE_SPECIFIC_DETAIL}} から始めるなら、n8n は1本で十分です。フォームの内容を表へ足し、人へ下書き通知する。一斉送信ではありません。

{{DISPLAY_NAME}}です。日本から、{{TIMEZONE}} で非同期に進めています。動かす場所は依頼者の n8n です。公式のコネクタだけ使います。ブラウザの自動操作はしません。

いまはダミーです。「明日休業」というメモだけ送ります。実在のお客さんの名前は使いません。

n8n が行を足して、通知を保留します。このデモの通知ノードはホールドです。メーリングリストへは出しません。投稿もしません。

表のタブは EXAMPLE-ONLY。status は new。auto_send は false。true なら、この道は拒否します。

本番の仕事なら、ワークスペース内のシナリオと短い手順書が残ります。送信ボタンは人です。公開メモ: {{PORTFOLIO_URL}}。同じ「壊れたら出さない」姿勢: {{GITHUB_REPO_AUTOPILOT}}。

確認したいことは2つです。
1. 正本はフォームですか、表ですか。
2. 失敗した行を再実行してよい人は誰ですか。
```

---

## On-screen captions (optional)

EN:

```
Form → sheet → ping (hold)
Dummy row only
You send
```

JA:

```
フォーム → 表 → 通知（保留）
ダミー1行だけ
送信は人
```

Do not burn in a price, a live URL, or “n8n Expert.”

---

## Close (after the take — not on the Loom unless asked)

Off-camera next step for the human operator: keep chat on the **same desk** where the conversation started. Do not add email, phone, or WhatsApp. Do not paste [FACTS.md](FACTS.md).

---

## Fictional fill (not a real buyer; do not send)

- Label: `Client A` / `依頼者A`
- `{{ONE_SPECIFIC_DETAIL}}` example: `weekend intake from the contact form sitting in a tab overnight`
- `{{ONE_SPECIFIC_DETAIL}}` 例: `問い合わせフォームが夜までタブに残っている`

Do not replace the fictional label with a live client name in git.

---

## STOP

- Do not record or upload from this PR
- Do not show a production sheet “because it looks more real”
- Do not claim minutes saved
- Do not treat sibling SKU-3 (sheet sync) as a live Google credential in this take
