> **DRAFT_ONLY. DO NOT RECORD. DO NOT SEND.**  
> Dummy inbound only. No auto-reply. Agent does not click Record.

# JOBS-DEMO-02 — Lead classify

## Fact table (operator; do not put on camera)

| key | value |
|---|---|
| pack | earn-jobs-demo-scripts-n8n-20260916 |
| id | JOBS-DEMO-02 |
| theme | lead / inquiry classify |
| buyer_value | Existing labels plus an uncertain bucket. A person reviews. Nothing auto-replies. |
| mode | DRAFT_ONLY, HANDS talk-through / later Loom |
| draft | true |
| record | **forbidden** from this pack |
| runtime_target | 90–120 seconds |
| sibling_shape | SKU-1 inquiry classifier (unpublished Gumroad pack) |
| related_proposal | EN-W2-02; JP-W2-05 |

Assumed buyer (not a real company): inbound form or help text that a person currently tags by hand (billing / support / sales).

Out of scope: scraped contact lists, auto-spam sequences, fake intent scores, LinkedIn crawling, accuracy %, auto-reply.

---

## Why this demo (buyer)

**EN.** Classification is a label a person can audit, not a promise that a lead will buy. Unclear text goes to **uncertain** and waits. This walkthrough runs three fictional lines: a billing-shaped note, a how-to question, and a vague line that must hold.

**JA.** 分類は、人が検品できるラベルです。受注の約束ではありません。曖昧な文は **未確定** に置き、人が見ます。この動画は架空の3件だけです。請求っぽい文、使い方の質問、保留すべき曖昧な1行。

---

## Props (dummy only)

| Prop | Safe rehearsal |
|---|---|
| Inbound | Three webhook POSTs (or three Form submits) with the JSON below |
| n8n canvas | Inactive: Webhook → label map → route; **uncertain** → hold / NoOp |
| Sheet tab | `EXAMPLE-ONLY` — columns `label`, `hold`, `from_label` |
| Labels | `billing` / `support` / `sales` / `uncertain` only — do not invent a fifth on camera |
| Notify | Off, or NoOp “operator: check hold.” No mail |

### Dummy payloads (fictional)

Clear support-shaped (expect `support` or, if your stub is stricter, `uncertain` — **narrate what the canvas actually did**):

```json
{
  "source": "form-stub",
  "subject": "EXAMPLE-ONLY — office hours",
  "body": "What time do you answer email?",
  "from_label": "example-sender"
}
```

Clear billing-shaped:

```json
{
  "source": "form-stub",
  "subject": "EXAMPLE-ONLY — invoice copy",
  "body": "Please send a copy of last month's invoice.",
  "from_label": "example-sender"
}
```

Must-hold (expect `uncertain`):

```json
{
  "source": "form-stub",
  "subject": "EXAMPLE-ONLY — hi",
  "body": "Hi.",
  "from_label": "example-sender"
}
```

Do not replay a real mailbox thread to “prove accuracy.”

If the stub labels the how-to question `uncertain`, that is a **good** take: say so. Do not override the node on camera to look smarter.

---

## Shot list (Loom outline)

| t | Screen | Say / do | Do not |
|---|---|---|---|
| 0:00–0:08 | Title | “Labels you already use. Unsure holds.” | “AI that never misses” |
| 0:08–0:18 | Label legend | billing / support / sales / uncertain | A made-up score column |
| 0:18–0:50 | Three dummy submits | Show each payload; then the label cell | Real customer email |
| 0:50–1:10 | Hold queue / `uncertain` row | “This waits. Nobody replies from n8n.” | Auto-reply node “just for demo” |
| 1:10–1:30 | Canvas Inactive badge | Official connector / webhook only | Credentials UI |
| 1:30–1:55 | Face or zoom-out | What they would own; two questions | Accuracy %, price |

---

## Spoken EN

Rewrite `{{ONE_SPECIFIC_DETAIL}}` before a real conversation.

```
You mentioned {{ONE_SPECIFIC_DETAIL}}. I would classify those inbound rows first, and only then route them.

I am {{DISPLAY_NAME}}, Japan, async in {{TIMEZONE}}. Lead classify, for me, means tags a person agrees with, a route for billing, support, or sales, and a hold bucket for anything unsure. I do not scrape lists. I do not send outreach from the workflow.

Three dummy lines. First: “What time do you answer email?” That should look like support — or hold, if the rule is strict. I will not fake the label on camera.

Second: a request for an invoice copy. Billing-shaped. A person still confirms amounts. n8n does not charge anyone.

Third: just “Hi.” That is uncertain. It stays in the hold. Nobody auto-replies.

The product is the hold behavior, not a promised accuracy number. After a job you would own the label definitions, the path on your n8n, and an SOP for sampling and correcting a row. Notes: {{PORTFOLIO_URL}}.

Two questions:
1. What is the source of truth today — the form, a sheet, or the CRM?
2. Should “unsure” wait for a human, or is a Maybe tag allowed without review?
```

---

## Spoken JA

実会話の前に `{{ONE_SPECIFIC_DETAIL}}` を差し替える。

```
ご相談の {{ONE_SPECIFIC_DETAIL}} なら、先にラベルを付け、そのあとだけ振り分けます。

{{DISPLAY_NAME}}です。日本、{{TIMEZONE}}。分類は、依頼者が使っているラベルと、迷ったときの未確定です。リストの収集はしません。ワークフローから営業メールは出しません。

ダミーを3件。1件目は「メールは何時に見ますか」。サポート寄り。規則が厳しければ未確定でもよい。画面上でラベルを書き換えません。

2件目は請求書の再送。billing 寄り。金額の確定は人です。n8n は請求しません。

3件目は「こんにちは」だけ。未確定です。保留のまま。自動返信はありません。

売り物は精度の数字ではなく、人が止められる列です。仕事になれば、ラベル定義と n8n 上の道と、外れた行の直し方が残ります。メモ: {{PORTFOLIO_URL}}。

確認したいことは2つです。
1. いまの正本はフォームですか、表ですか、CRMですか。
2. 未確定は人が見るまで待ちますか。人なしの Maybe を許しますか。
```

---

## On-screen captions (optional)

EN:

```
billing · support · sales · uncertain
Unsure holds
No auto-reply
```

JA:

```
請求 · サポート · 営業 · 未確定
迷ったら保留
自動返信なし
```

Do not burn in “98% accurate” or a partner badge.

---

## Close (after the take — not on the Loom unless asked)

Keep chat on the same desk. Do not add a mailbox. Do not paste real inquiry bodies into git after the call.

---

## Fictional fill (not a real buyer; do not send)

- Label: `Client B` / `依頼者B`
- `{{ONE_SPECIFIC_DETAIL}}` example: `demo-form rows landing in one tab with no tag`
- `{{ONE_SPECIFIC_DETAIL}}` 例: `デモフォームの行がタグなしで1つのタブに溜まっている`

---

## STOP

- Do not record or upload from this PR
- Do not promise lead volume or close rate
- Do not show a live CRM
- Do not add an auto-reply node “so the buyer sees magic”
