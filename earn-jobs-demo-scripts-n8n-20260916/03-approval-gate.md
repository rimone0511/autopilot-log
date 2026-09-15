> **DRAFT_ONLY. DO NOT RECORD. DO NOT SEND.**  
> Dummy draft only. Timeout is not approve. Agent does not click Record.

# JOBS-DEMO-03 — Approval gate

## Fact table (operator; do not put on camera)

| key | value |
|---|---|
| pack | earn-jobs-demo-scripts-n8n-20260916 |
| id | JOBS-DEMO-03 |
| theme | approval-gated notify |
| buyer_value | A draft can exist. Nothing outbound until a person says approve. Missing / reject / timeout fail closed. |
| mode | DRAFT_ONLY, HANDS talk-through / later Loom |
| draft | true |
| record | **forbidden** from this pack |
| runtime_target | 90–120 seconds |
| sibling_shape | SKU-2 approval-gated notify (unpublished Gumroad pack) |
| related_proposal | JP-W2-02 (承認が付くまで送らない) |

Assumed buyer (not a real company): a team that wants n8n to **draft** a chat or mail, with a supervisor click before anything leaves.

Out of scope: auto-send-on-timeout, live outbound, SLA, browser bots, “I’ll approve it off-camera so Slack looks real.”

---

## Why this demo (buyer)

**EN.** Drafts are cheap. Accidental sends are not. The gate is the product: `approve` is the only yes; reject, missing, unknown, and timeout are **no**. In this walkthrough the approve branch still ends on a **NoOp**. That is honest. Replacing NoOp with a live Slack node is a later job on **your** credentials.

**JA.** 下書きは安く、誤送信は高くつきます。売り物はゲートです。`approve` だけが yes。却下・欠落・不明・タイムアウトは **no**。この動画の approve 分岐も **NoOp** で終わります。それが正直です。本物の Slack に差し替えるのは、依頼者の鍵での後作業です。

---

## Props (dummy only)

| Prop | Safe rehearsal |
|---|---|
| Draft intake | POST the proposed-notify JSON |
| Decision intake | Separate path: `reject`, then missing, then `approve` |
| n8n canvas | Inactive: webhook → pending row → switch on `decision` → NoOp outbound |
| Sheet / hold | `EXAMPLE-ONLY` — `approval_status=pending`, `outbound_allowed=false` |
| Wait node | Optional later; **do not** paste `$execution.resumeUrl` on a public page |

### Dummy payload — proposed notify (fictional)

```json
{
  "source": "form-stub",
  "channel": "example-operator-inbox",
  "draft_text": "EXAMPLE-ONLY — office closed tomorrow",
  "audience": "internal-operator",
  "auto_send": false
}
```

### Dummy payload — reject (show this first)

```json
{
  "decision": "reject",
  "approver_label": "example-operator",
  "note": "EXAMPLE-ONLY dummy reject"
}
```

### Dummy payload — approve (NoOp outbound)

```json
{
  "decision": "approve",
  "approver_label": "example-operator",
  "note": "EXAMPLE-ONLY dummy approve — still NoOp"
}
```

Do not send `auto_send: true`. If a missing `decision` body is posted, the take should show **no outbound**.

---

## Shot list (Loom outline)

| t | Screen | Say / do | Do not |
|---|---|---|---|
| 0:00–0:08 | Title | “Human yes before anything leaves.” | “We’ll auto-send overnight” |
| 0:08–0:25 | Draft lands | Pending row; outbound_allowed false | Live customer mail |
| 0:25–0:45 | Missing / empty decision | Fail closed — nothing leaves | “Pretend timeout is OK” |
| 0:45–1:00 | `reject` | Stop. Do not send. | Quietly retry |
| 1:00–1:20 | `approve` | Point at NoOp / sticky “not sent” | Attach a live Slack credential |
| 1:20–1:50 | Zoom-out | What they would own; two questions | SLA, price, partner badge |

---

## Spoken EN

Rewrite `{{ONE_SPECIFIC_DETAIL}}` before a real conversation.

```
You mentioned {{ONE_SPECIFIC_DETAIL}}. I would keep a human gate in front of any outbound.

I am {{DISPLAY_NAME}}, Japan, async in {{TIMEZONE}}. I draft on n8n. I do not send in your name until a person says approve. Timeout is not approve. A missing decision is not approve.

Dummy draft: “office closed tomorrow,” to an internal operator inbox. It sits pending. Outbound allowed is false.

If I post no decision, the path stops. If I post reject, it stops. I will not quietly resend.

If I post approve, this demo still ends on a NoOp. That is the point of the stub: the gate is real; the mail node is a placeholder you replace later on your instance, with your credential. I will not attach that credential on this call.

You would own the pending row, the approve/reject intake, a fail-closed note in the SOP, and the send switch still in a person’s hands. Notes: {{PORTFOLIO_URL}}. Same posture: {{GITHUB_REPO_AUTOPILOT}}.

Two questions:
1. Is approval a button in chat, or a status on the sheet?
2. Where does a rejected draft go — back to the author, or a hold tab?
```

---

## Spoken JA

実会話の前に `{{ONE_SPECIFIC_DETAIL}}` を差し替える。

```
ご相談の {{ONE_SPECIFIC_DETAIL}} なら、外に出す前の人のゲートを残します。

{{DISPLAY_NAME}}です。日本、{{TIMEZONE}}。n8n で下書きは作れます。人が approve と言うまで、依頼者の名前では送りません。タイムアウトは承認ではありません。decision が無いのも承認ではありません。

ダミーの下書きは「明日休業」。内部のオペレータ向け。pending のまま。outbound_allowed は false。

decision を送らなければ止まります。reject なら止まります。黙って再送しません。

approve を送っても、このデモは NoOp で終わります。それがスタブの意味です。ゲートは本物。メールノードはあとで依頼者の n8n と依頼者の鍵に差し替える置き場です。この通話で鍵は付けません。

残るのは、保留行、承認と却下の入口、壊れたら出さない手順、そして人の送信スイッチです。メモ: {{PORTFOLIO_URL}}。同じ姿勢: {{GITHUB_REPO_AUTOPILOT}}。

確認したいことは2つです。
1. 承認はチャットのボタンですか、表のステータスですか。
2. 却下した下書きは差出人に戻しますか、保留タブですか。
```

---

## On-screen captions (optional)

EN:

```
pending → human decision
reject / missing / timeout = no
approve still NoOp in this demo
```

JA:

```
pending → 人が決める
却下・欠落・期限切れ = 送らない
このデモの approve も NoOp
```

Do not burn in an SLA (“approved in 5 minutes”) or a live channel name.

---

## Close (after the take — not on the Loom unless asked)

Keep chat on the same desk. Do not collect the buyer’s mail credential “to finish the demo.” Do not wire `$execution.resumeUrl` to a public form.

---

## Fictional fill (not a real buyer; do not send)

- Label: `Client C` / `依頼者C`
- `{{ONE_SPECIFIC_DETAIL}}` example: `replies sitting in a shared inbox until a manager forwards them`
- `{{ONE_SPECIFIC_DETAIL}}` 例: `共有受信箱の返信が、上長の転送待ちのまま溜まっている`

---

## STOP

- Do not record or upload from this PR
- Do not send a real Slack/mail “so they believe you”
- Do not treat timeout as approve
- Do not claim n8n Wait-node magic unless it is on **their** instance later
