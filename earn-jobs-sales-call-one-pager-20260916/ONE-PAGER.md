> **DRAFT_ONLY. DO NOT CALL. DO NOT SEND.**  
> Operator sheet. Do not screenshare this file. Do not put the map on camera.

# Sales-call one-pager — JOBS 2026-09-16

Pack: `earn-jobs-sales-call-one-pager-20260916/`  
Desks: **Coconala** · **Gumroad** · **Contra Independent**  
Mode: **DRAFT_ONLY**  
Speak: **one** language. Record / send: **forbidden** from this pack.

Public (may be spoken): `{{DISPLAY_NAME}}` · Japan · async `{{TIMEZONE}}` · https://yutalab.dev/ · https://github.com/rimone0511/autopilot-log

---

## 60-second setup (before anyone talks)

1. Thread is already open on **one** desk. Do not add a channel.
2. Fill `{{ONE_SPECIFIC_DETAIL}}` from **this** buyer’s words. Empty → skip.
3. Pick **one** row in the map below. Default: one theme, ~90–120 seconds (PR #78).
4. Dummy props only (`EXAMPLE-ONLY`). Canvas **Inactive**. Crop webhook / sheet IDs.
5. Prices stay off-camera. Menu close is optional — only if they ask what it costs / what to buy.

---

## Map (operator; not a slide)

| Buyer pain (this week) | Demo (PR #78) | Menu SKU (PR #82) | Coconala | Gumroad | Contra |
|---|---|---|---|---|---|
| Form / sheet intake; ping a person; **you** send | `01-form-sheet-notify.md` JOBS-DEMO-01 | `SKU-STARTER` | Listing 01 n8n自動化 ([#79](https://github.com/rimone0511/autopilot-log/pull/79)); estimate pastes exist — **do not send** | SKU-0 shape; listing polish [#74](https://github.com/rimone0511/autopilot-log/pull/74); **unpublished** | Service “starter intake”; Job-feed 01 ([#71](https://github.com/rimone0511/autopilot-log/pull/71)) — **do not Apply** |
| Inbound tags + **uncertain / hold**; no auto-reply | `02-lead-classify.md` JOBS-DEMO-02 | `SKU-CLASSIFIER` | Listing 02 問い合わせ分類 | SKU-1 pack [#37](https://github.com/rimone0511/autopilot-log/pull/37); unpublished | Service classifier; Job-feed 02 — **do not Apply** |
| Draft waits for `approve`; timeout is **not** approve | `03-approval-gate.md` JOBS-DEMO-03 | `SKU-APPROVAL` | Use PR #82 `COCONALA-PASTE.md` approval-gate — **not** listing 03 | SKU-2 pack [#46](https://github.com/rimone0511/autopilot-log/pull/46); unpublished | Service approval-gate; Job-feed 04 — **do not Apply** |
| SOP for a flow they already have; no new workflow | **No demo in #78.** Do not fake a Loom | `SKU-DOCS` | PR #82 docs paste only | PR #82 Gumroad docs paste; no zip pack on `master` | PR #82 Contra docs service; **Save as unpublished** |

Do not stack three demos. Classify **then** gate only if the buyer’s ask already names both steps.

**Do not map**

| Sibling | Why it stays off this sheet |
|---|---|
| Coconala listing 03 AI運用伴走 ([#79](https://github.com/rimone0511/autopilot-log/pull/79)) | Not JOBS-DEMO-03. Different offer. |
| Contra proposal 03 inspectable AI ops / 05 sheet sync ([#71](https://github.com/rimone0511/autopilot-log/pull/71)) | Not in the four-SKU menu. |
| Gumroad SKU-3 sheet sync ([#52](https://github.com/rimone0511/autopilot-log/pull/52)) | Explicitly out of PR #82. |

---

## Call flow

| Beat | Time | What you open | What you say |
|---|---|---|---|
| Open | ~20 s | Face or title; **not** this markdown | [TALK-TRACK.md](TALK-TRACK.md) Spoken OPEN |
| One demo | 90–120 s | PR #78 file 01 / 02 / 03 shot list + Spoken fence | That file’s Spoken EN **or** Spoken JA. Cut “what you would own” if the timer runs long |
| Demo questions | in that file | Stay on dummy sheet / canvas | The **two questions in the demo file**. Do not skip them to pitch a bundle |
| Menu close | ~30–45 s, **optional** | Nothing priced on screen | [TALK-TRACK.md](TALK-TRACK.md) Spoken MENU — only if they ask price / SKU / “what do I buy” |
| Off-camera | after | Same thread | Next step stays on this desk. Do not paste PR #78 `FACTS.md` |

---

## Desk rules (same thread)

| Desk | Stay here | Price field (local ledger, not git) | Hard stop from this pack |
|---|---|---|---|
| ココナラ Coconala | トークルーム | `{{PRICE_JPY_SKU_*}}` / `{{PRICE_YEN_DRAFT}}`. Empty + `rate_empty` if the box refuses a token | 公開する / 見積もり送信 / 電話相談サービス作成 |
| Gumroad | Product message / unpublished draft | `{{PRICE_USD_SKU_*}}`. SKU-0: keep **$39** if that number is **already** on the unpublished draft ([#74](https://github.com/rimone0511/autopilot-log/pull/74)) — do not speak it | Publish / Enable / New product / payout / $0 checkout test |
| Contra Independent | Existing thread or unpublished service | Prefer **Contact for pricing** ([help 9322412](https://help.contra.com/en/articles/9322412-how-to-add-services-to-your-contra-profile)) | Publish / Apply / Discoverable / Pro / Persona / wallet |

Auth: **MAIN Google** only. Contra live box ([#64](https://github.com/rimone0511/autopilot-log/pull/64)): Free plan, `draft_saved`, **apply: no**, location leftover is **not** a sales-call fix. If asked where you work: **Japan**. Do not spoof US/EU.

Paid boosts stay off: Coconala ads, Gumroad Discover, Contra Pro.

---

## Honest offer (one line each)

| SKU | It is | It is not |
|---|---|---|
| starter | One inbound path → table → human ping; person sends | Browser bots, live list-mail, partner badges |
| classifier | Labels the buyer already uses + uncertain hold | Auto-reply, scraped lists, accuracy % |
| approval-gate | Draft sits until `approve`; reject / missing / timeout fail closed | Auto-send-on-timeout, SLA, live outbound on camera |
| docs | SOP / rerun notes for **their** existing flow | A new n8n build (that is the other three) |

Work after a contract: **official APIs / documented n8n connectors** only. Buyer’s n8n, buyer’s credentials.

Custom-desk delivery / revisions in PR #82 are **DRAFT SUGGESTION** (starter 7d/1, classifier 7d/1, approval-gate 10d/2, docs 5d/1). Gumroad download is as-is — do not read those days as a zip SLA. Live form wins.

---

## Do not say (even if asked)

- Hours saved, GMV, win rate, “N clients”, years in business, accuracy %
- A yen or USD figure that is not on the **private** ledger for **this** desk
- Competitor prices, “going rate”, or the PR #82 ladder as a market study
- “Timeout counts as approve”
- “n8n Expert / Partner”, Top Rated, lab affiliation
- A live listing URL
- “I’ll email you a deck / Zoom link”

If they ask for proof: public site + public repo only. No invented case.

---

## After the conversation (operator)

- Keep chat on the **same desk**
- Do not commit filled `{{PRICE_*}}`, `{{LOOM_URL_DO_NOT_COMMIT}}`, or a buyer’s real name
- Park `rate_required` / `rate_empty` if a form blocked submit
- This pack still has not sent, published, or recorded anything

## 日本語（運用・この1枚）

会話の前に `{{ONE_SPECIFIC_DETAIL}}` を埋める。デモは PR #78 から1本。料金を聞かれたときだけ PR #82 のメニュー1行。数字はローカル台帳。机をまたがない。公開しない。
