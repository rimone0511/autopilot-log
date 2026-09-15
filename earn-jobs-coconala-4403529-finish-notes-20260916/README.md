# Coconala 4403529 — finish notes (unpublished)

Pack date: **2026-09-16**  
Desk: ココナラ / Coconala  
Listing (seller-dashboard id): **4403529**  
Mode: **JOBS polish note. DRAFT_ONLY.**

This folder records **operator-supplied live draft state** for one unpublished 通常サービス. It is not a paste pack, not a live CU log, and not permission to click **公開する**.

This authoring agent **did not log in**. Public GET of `https://coconala.com/services/4403529` returned **HTTP 404** (no public listing page). No live CU.

## Files

| File | Role |
|---|---|
| [STATUS.md](STATUS.md) | Snapshot: unpublished, FAQ 6, price, estimate, images, title |
| [TITLE-FIX.md](TITLE-FIX.md) | If the title UI doubles **ます**, fix the field (do not save ますます) |
| [OPERATOR-NEXT.md](OPERATOR-NEXT.md) | Next human steps: **cover first**, then 祐太 GO for 公開 |
| [HUMAN-GO.md](HUMAN-GO.md) | Fail-closed. `coconala_publish_listing: false` |
| [DRAFT_ONLY.md](DRAFT_ONLY.md) | Hard stop. No secrets. No 見積もり送信 |

## Live draft (operator record — this pass)

| Item | Recorded |
|---|---|
| Public | **unpublished** (404 as guest; do not announce a live URL) |
| FAQ | **6** pairs; slot 6 **fixed** (スクレイピング out of scope) |
| Price on form | **10000** yen (unpublished draft observation, not 相場) |
| 見積もり | **ON** (受付する). Sending an estimate is still **off** |
| Images | **`image_missing`** — GO-blocker |
| Title | Canonical field `n8n自動化と手順書を作ります`. UI may show doubled ます — see TITLE-FIX |

Family: [#79](https://github.com/rimone0511/autopilot-log/pull/79) `01-n8n-automation-listing.md` (`n8n自動化と手順書を作ります`). Same first-gig family as [#87](https://github.com/rimone0511/autopilot-log/pull/87). Do not open a second n8n listing.

## Operator next (one line)

Attach an original cover (secrets cropped, no partner logos) → leave unpublished → **human GO** before 公開. This pack does not flip GO.

## Out of scope

- Coconala login / CU from this agent
- Clicking 公開する / 見積もり送信 / 口座 / 本人確認
- Rewriting サービス内容 fences
- Python posting-gate edits
- Committing cover binaries, emails, passwords, OTP
