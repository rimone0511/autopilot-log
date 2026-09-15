> **DRAFT_ONLY. DO NOT CALL. DO NOT SEND. DO NOT PUBLISH.**  
> No Zoom / Meet / phone from this pack. No Loom. No 見積もり送信. No live prices.  
> No secrets. No invented case metrics. Agent does not join a call.

# JOBS — sales-call one-pager (2026-09-16)

Pack date: 2026-09-16  
Phase: **JOBS** (sales conversations)  
Mode: **DRAFT_ONLY** + **HANDS** (a person talks; a computer does not publish)  
Languages: **EN + JA** (speak **one** language per conversation)  
Seller: `{{DISPLAY_NAME}}` (recommended: Yuta Ishida / 石田祐太)  
Public notes: https://yutalab.dev/  
Public tool: https://github.com/rimone0511/autopilot-log

This folder is the **operator sheet** for a live sales conversation that already exists on **one** desk:

1. Walk **one** n8n demo from [PR #78](https://github.com/rimone0511/autopilot-log/pull/78)
2. If they ask what it costs / what to buy, name **one** line from the pricing menu [PR #82](https://github.com/rimone0511/autopilot-log/pull/82)
3. Stay on the desk where the thread started: **Coconala**, **Gumroad**, or **Contra Independent**

It is not a marketplace cover letter. It is not listing paste. It is not a video file. It is not a quote.

Rules: [DRAFT_ONLY.md](DRAFT_ONLY.md).  
Sheet: [ONE-PAGER.md](ONE-PAGER.md).  
Spoken fences: [TALK-TRACK.md](TALK-TRACK.md).

---

## Files

| File | Role |
|---|---|
| [ONE-PAGER.md](ONE-PAGER.md) | Printable operator sheet: open → one demo → optional menu → stay on desk |
| [TALK-TRACK.md](TALK-TRACK.md) | Spoken EN + spoken JA (this pack’s open / menu close only) |
| [DRAFT_ONLY.md](DRAFT_ONLY.md) | Fail-closed gate. Missing file = every flag `false` |
| [README.md](README.md) | Sibling pointers. Bodies are not copied here |

---

## When to use (still draft)

A human may later (GO outside this folder):

- Screenshare **one** PR #78 outline on an **already-open** Coconala トーク / Gumroad message / Contra thread
- Talk through the shot list live, without recording
- Record **one** private Loom and paste the share URL **only** in that thread (URL stays out of git)

This pack still does **not** join a call, record, send, or publish.

Skip the conversation if any box is false:

- [ ] [DRAFT_ONLY.md](DRAFT_ONLY.md) gate is still all `false`
- [ ] I rewrote `{{ONE_SPECIFIC_DETAIL}}` from **this** buyer’s ask. If I cannot name one in about a minute, I skip
- [ ] I picked **one** demo (01 / 02 / 03). I am not stacking all three
- [ ] Props are dummy (`EXAMPLE-ONLY`). No production sheet, no real inbox
- [ ] n8n on screen is **Inactive**. Credential UI and sheet IDs are cropped
- [ ] No yen / USD is spoken (local ledger only: `{{PRICE_*}}`)
- [ ] I stay on the desk that already holds the thread
- [ ] I click Send / 公開 / Publish / Apply / Record myself only after a GO outside this folder

---

## Sibling pointers (do not copy bodies)

| Need | PR | Path (on that branch, not `master`) |
|---|---|---|
| Demo outlines ×3 (form → sheet → notify / classify / approval) | [#78](https://github.com/rimone0511/autopilot-log/pull/78) | `earn-jobs-demo-scripts-n8n-20260916/` |
| Seller pricing menu (four SKUs, JP+EN, desk paste) | [#82](https://github.com/rimone0511/autopilot-log/pull/82) | `earn-jobs-pricing-menu-20260916/` |
| Coconala 通常サービス listings ×3 (unpublished) | [#79](https://github.com/rimone0511/autopilot-log/pull/79) | `earn-jobs-coconala-service-drafts-20260916/` |
| Coconala inquiry / custom replies ×8 (do not send) | [#81](https://github.com/rimone0511/autopilot-log/pull/81) | `earn-jobs-coconala-proposal-replies-20260916/` |
| Gumroad SKU-0 listing polish EN+JA | [#74](https://github.com/rimone0511/autopilot-log/pull/74) | `earn-jobs-gumroad-sku0-listing-polish-20260916/` |
| Gumroad SKU-0 look-don't-ship | [#55](https://github.com/rimone0511/autopilot-log/pull/55) [#63](https://github.com/rimone0511/autopilot-log/pull/63) | `ops/earn/gumroad-draft-qa-20260916/` / `ops/earn/gumroad-look-dont-ship-20260916/` |
| Gumroad SKU-1 / SKU-2 (classifier / approval-gate zips) | [#37](https://github.com/rimone0511/autopilot-log/pull/37) [#46](https://github.com/rimone0511/autopilot-log/pull/46) | `earn-sku1-n8n-pack-draft-20260916/` / `earn-sku2-approval-gate-pack-draft-20260916/` |
| Contra Job-feed apply drafts ×5 (do not send) | [#71](https://github.com/rimone0511/autopilot-log/pull/71) | `earn-jobs-contra-proposals-20260916/` |
| Contra live `draft_saved` (Free; apply: no) | [#64](https://github.com/rimone0511/autopilot-log/pull/64) | `ops/earn/contra-status-20260916/` |
| JOBS week calendar (four `draft_saved` desks) | [#76](https://github.com/rimone0511/autopilot-log/pull/76) | `earn-jobs-weekly-earn-plan-20260916/` |

**Out of this call on purpose**

- Gumroad SKU-3 sheet sync ([#52](https://github.com/rimone0511/autopilot-log/pull/52)) — pricing menu says not in the four-SKU list
- Coconala listing 03 AI運用伴走 ([#79](https://github.com/rimone0511/autopilot-log/pull/79)) — not an approval-gate demo; do not map it to JOBS-DEMO-03
- Contra proposal 03 inspectable AI ops / 05 sheet sync ([#71](https://github.com/rimone0511/autopilot-log/pull/71)) — not the four-SKU menu
- LinkedIn profile / Services ([#75](https://github.com/rimone0511/autopilot-log/pull/75) [#16](https://github.com/rimone0511/autopilot-log/pull/16)) — not this three-desk sheet
- Fiverr / Lancers / CrowdWorks / Upwork / TimeTicket / Craudia / Wave B–D

Seller facts that may be claimed on camera live in PR #78 `FACTS.md`. Do not put that file on screen. If a fact is not there, do not invent it.

---

## Prices (operator; never on camera)

All live amounts stay tokens. Empty in git is correct.

| Desk | Token family | If the live field demands a number |
|---|---|---|
| Coconala | `{{PRICE_JPY_SKU_*}}` / `{{PRICE_YEN_DRAFT}}` | Leave empty + park `rate_empty`. ¥500 on `guide_sell` is a **platform minimum**, not a quote |
| Gumroad | `{{PRICE_USD_SKU_*}}` | Do not publish at $0. SKU-0 polish ([#74](https://github.com/rimone0511/autopilot-log/pull/74)): **keep $39 if already on the unpublished draft** — that is a keep-if-set rule, not a spoken rate |
| Contra | Prefer official **Contact for pricing** | One-time `{{PRICE_USD_SKU_*}}` only if a private ledger already exists. Do not buy Pro |

Ladder in PR #82 is labeled **DRAFT SUGGESTION** (docs → starter → classifier → approval-gate). It is not a comparable, not a going rate, not GMV.

Do not paste Coconala yen into Contra. Do not paste Gumroad tokens into a Coconala yen box.

---

## What this pack will not claim

- Client counts, years in business, GMV, hours saved, close rate, accuracy %
- “n8n Expert”, “n8n Partner”, “Top Rated”, lab affiliation
- A guaranteed price, delivery SLA, or “timeout = send”
- That Autopilot Log posts TikTok unattended (inbox upload is the default)
- That this PR booked a call, recorded a Loom, or published a listing
- Live `coconala.com/services/…`, `gumroad.com/l/…`, `contra.com/@…`

## Out of this folder on purpose

- Account signup / KYC / payout
- Dual-use of a Loom script as a cover letter
- n8n hosting purchase, Expert Partner waitlist, Contra Pro, Gumroad Discover, Coconala ads
- Any script that submits a bid or starts a recorder

## 日本語（運用だけ）

下書きのみ。会話は **今いる机のスレッドだけ**（ココナラ / Gumroad / Contra）。デモは PR #78 から **1本**。料金は PR #82 のトークンとローカル台帳。円額・ドル額・時短・受注率は口にしない。Zoom / 電話 / メールは足さない。公開・見積もり送信・Apply・Loom 録画はこの PR からはしない。

## This PR does not

- Merge sibling packs or mark them ready-for-review
- Publish, apply, invoice, or send
- Invent listing URLs, case metrics, or live prices
- Change Python posting-gate tests
