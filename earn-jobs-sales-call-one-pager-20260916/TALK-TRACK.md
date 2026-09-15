> **DRAFT_ONLY. DO NOT RECORD. DO NOT SEND.**  
> Dummy talk only. No live price. No case metrics. Agent does not join a call.

# Talk track — sales call (EN + JA)

Pack: `earn-jobs-sales-call-one-pager-20260916/`  
Use with: [ONE-PAGER.md](ONE-PAGER.md)  
Demo spoken fences live in [PR #78](https://github.com/rimone0511/autopilot-log/pull/78) — **do not paste those bodies here.**

Rewrite `{{ONE_SPECIFIC_DETAIL}}` before a real conversation. Record **one** language.  
Prices and `{{HOURLY_RATE_USD}}` / `{{PRICE_YEN_DRAFT}}` stay **off** this track.

After Spoken OPEN, switch to the matching PR #78 file (01 / 02 / 03). Come back here only for Spoken MENU.

---

## Spoken OPEN (English)

This fence is the take’s first ~20 seconds. Then stop talking from this file until the demo’s two questions are done.

```
You mentioned {{ONE_SPECIFIC_DETAIL}}. I will walk one n8n path. Official connectors only. A person still sends.

I am {{DISPLAY_NAME}}. I work from Japan, async in {{TIMEZONE}}. I do not drive browsers. I do not scrape. I do not auto-reply.

This walkthrough is dummy data. It is not a live sheet and not a live send.
```

Then: open PR #78 Spoken EN for JOBS-DEMO-01, 02, or 03 (one file). Keep the dummy run and that file’s two questions.

---

## Spoken MENU (English) — optional

Use **only** if they ask what it costs, what they would buy, or whether this is a bundle. Do not append it to every demo.

```
If we go further, it is one line on the menu, not a bundle.

Starter intake is form or sheet in, notify a person, you send.
Classifier is your labels plus an uncertain hold. Nothing auto-replies.
Approval-gate waits for approve. Reject, missing, or timeout does not send.
Docs is a runbook for a flow you already have. No new workflow.

I will not read a yen or dollar figure on this call. If we continue on this desk, the price field uses a private ledger for that desk. On Contra, Contact for pricing is allowed until a number is chosen.

I will not quote hours saved, a win rate, or a past client's result. Those numbers are not in this pack.

Next step stays in this thread. I will not add email, phone, or a second marketplace.
```

Do not fill the menu with a SKU they did not ask for. Do not say “unpublished draft” to the buyer.

---

## Spoken OPEN (日本語)

実会話の前に `{{ONE_SPECIFIC_DETAIL}}` を差し替える。このフェンスが冒頭。続けて PR #78 の Spoken JA を1本。

```
ご相談の {{ONE_SPECIFIC_DETAIL}} から、n8n の道を1本だけ見せます。公式の接続だけ使います。送信は人のままです。

{{DISPLAY_NAME}}です。日本から、{{TIMEZONE}} で非同期に進めています。ブラウザの自動操作はしません。自動返信もしません。

いまはダミーです。本番の表ではありません。実送信しません。
```

続けて PR #78 の JOBS-DEMO-01 / 02 / 03 の Spoken JA（1ファイル）。そのファイルの確認2問は省略しない。

---

## Spoken MENU (日本語) — 任意

料金・何を買うか・束ね売りかを聞かれたときだけ。毎回のデモの末尾に足さない。

```
続きがあるなら、メニューの1行です。束ね売りではありません。

受付スターターは、フォームや表から受けて人へ知らせます。送るのは人です。
分類は、既存のラベルに分け、迷ったら未確定にします。自動返信しません。
承認ゲートは、approve まで外に出しません。却下・欠落・時間切れでは送りません。
手順書は、既存フローの再実行メモです。新しいフローは作りません。

この会話で円額やドル額は口にしません。続けるなら、この机の料金欄はローカルの台帳です。Contra は数字を決めるまで Contact for pricing で構いません。

時短、受注率、お客さんの実名成果は、このパックに無いので言いません。

次の一手はこのスレッドのままです。メール、電話、別の市場は足しません。
```

買い手向けフェンスに「未公開ドラフト」と書かない。

---

## Placeholders in these fences

| Token | On this track? |
|---|---|
| `{{DISPLAY_NAME}}` | yes |
| `{{ONE_SPECIFIC_DETAIL}}` | yes — rewrite per conversation |
| `{{TIMEZONE}}` | yes if asked / in OPEN |
| `{{PORTFOLIO_URL}}` | only if the **demo file** already speaks it; do not add a third URL here |
| `{{PRICE_*}}` `{{HOURLY_RATE_USD}}` `{{PRICE_YEN_DRAFT}}` | **never** in these fences |
| `{{LOOM_URL_DO_NOT_COMMIT}}` | **never** in git |

Fictional fill (not a real buyer; do not send): `{{ONE_SPECIFIC_DETAIL}}` example — `weekend intake from the contact form sitting in a tab overnight` / `問い合わせフォームが夜までタブに残っている`.

---

## Length (this pack only)

Python `len()` of the Spoken fences, placeholders unsubstituted, 2026-09-16. Filling `{{ONE_SPECIFIC_DETAIL}}` increases length. PR #78 demo fences are **not** included in these counts.

| Fence | Chars | Words (EN) |
|---|---:|---:|
| Spoken OPEN EN | 319 | 55 |
| Spoken MENU EN | 733 | 137 |
| Spoken OPEN JA | 178 | — |
| Spoken MENU JA | 344 | — |

Rehearse OPEN + one demo + optional MENU once with a timer. Do not pad with testimonials.

---

## STOP

- Do not record or upload from this PR
- Do not speak a live price “so the buyer can decide today”
- Do not invent a case study when they ask for proof
- Do not dual-use this track as a Coconala 見積もり or Contra Apply paste
