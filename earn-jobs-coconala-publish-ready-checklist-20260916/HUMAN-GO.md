# HUMAN-GO — ココナラ 公開する（fail closed）

Pack date: 2026-09-16  
Desk: Coconala  
Mirrors Autopilot Log posting-gate: **“drafts are saved” is not “the marketplace may go live.”**

Default (commit this way):

```
coconala_jobs_gate:
  pack: earn-jobs-coconala-publish-ready-checklist-20260916
  draft_only: true
  coconala_publish_listing: false
  coconala_send_estimate: false
  coconala_resume_accepting: false
  coconala_blog_embed: false
  coconala_sns_announce: false
  any_payout_kyc_upload: false
```

If this file is missing, unread, or the YAML-like block is half-filled, treat **every row as `false`**.  
Do not infer permission from `draft_saved`, QUEUE `done-draft`, a merged PR, JOBS week Day 2, or “the checklist is all green.”

A weekly-plan row in [PR#76 GO-GATES](https://github.com/rimone0511/autopilot-log/pull/76) being `true` is **not** enough. This file must also show `coconala_publish_listing: true` **and** 祐太 must click **公開する** on the live page.

**This authoring agent never flips a row to `true` and never clicks 公開する.**

---

## What “publish-ready” means here

The listing has fields / images / price / FAQ filled from the first-gig paste pack, saved as **下書き**, and [GAPS.md](GAPS.md) has no ship-blockers **that a human still wants to ignore**.

It does **not** mean:

- 公開する was clicked
- 受付中
- 見積もりを送った
- 売上口座が付いた

---

## UI labels that mean GO (do not click unless the matching row is `true`)

| Gate row (must be `true`) | Live control (labels vary; live wins) |
|---|---|
| `coconala_publish_listing` | **公開する** / 出品を公開 / 公開中にする / この内容で公開する |
| `coconala_send_estimate` | 見積もりを送る / 提案する / 相談に返信して送信 |
| `coconala_resume_accepting` | 受付再開 / 受付中にする（休止解除） |
| `coconala_blog_embed` | ブログで紹介する / 埋め込みコード発行 |
| `coconala_sns_announce` | X / note / Blog / プロフィール外で「出品しました」 |
| `any_payout_kyc_upload` | 本人確認 / 口座 / インボイス / 顔撮影 |

If a confirm dialog appears after **下書きで保存する**, read it. If it says the service will become **公開**, treat it as `coconala_publish_listing` — **cancel**.

---

## Allowed without flipping a row

1. Open the official site as MAIN Google on the **existing** account.
2. Open the unpublished 通常サービス draft (or paste into a new draft you will **not** publish).
3. Fill from first-gig paste packs. Watch the character counter.
4. Click **下書きで保存する** only when that control does **not** make the listing public.
5. Record gaps locally / in a local GAPS copy.
6. Close.

First-gig STOP sibling: [PR#87 DRAFT_ONLY.md](https://github.com/rimone0511/autopilot-log/blob/cursor/coconala-first-gig-full-paste-54d5/earn-jobs-coconala-first-gig-full-paste-20260916/DRAFT_ONLY.md) (also [PR#79 STOP-PUBLISH.md](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-jobs-coconala-service-drafts-6662/earn-jobs-coconala-service-drafts-20260916/STOP-PUBLISH.md) for the x3 pack).

---

## If 公開する was already clicked (not this pack)

Do **not** unpublish from an agent. Log `already_published` in a local GAPS copy. Morning user decides. Do not paste the live `coconala.com/services/…` URL into git.

---

## Human GO procedure (only 祐太)

1. Re-read https://coconala.com/pages/guide_sell and https://coconala.com/pages/guide_rule.
2. Re-read category minimum-price help. Local `{{PRICE_YEN}}` ≥ live minimum. Do not commit the number.
3. Confirm images are original, secrets cropped, no partner logos.
4. Confirm FAQ 7 from the first-gig pack (#87) is on the draft.
5. Confirm 通常サービス (not 電話 / ビデオチャット).
6. Flip **one** row in a **local** copy of this file (do not push filled GO to git unless 祐太 wants the audit trail with `true` and a date — still no secrets).
7. Click the **one** matching live control.
8. Stop. Do not also send 見積もり the same click.

Default for this PR: leave the committed block **all `false`**.
