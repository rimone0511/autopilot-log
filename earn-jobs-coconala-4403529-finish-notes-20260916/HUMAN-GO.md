# HUMAN-GO — ココナラ 4403529 公開する（fail closed）

Pack date: 2026-09-16  
Desk: Coconala  
Listing: **4403529** (unpublished at record time)  
Mirrors Autopilot Log posting-gate: **a saved draft is not permission to go live.**

Default (commit this way):

```
coconala_jobs_gate:
  pack: earn-jobs-coconala-4403529-finish-notes-20260916
  listing_id: 4403529
  draft_only: true
  coconala_publish_listing: false
  coconala_send_estimate: false
  coconala_resume_accepting: false
  coconala_blog_embed: false
  coconala_sns_announce: false
  any_payout_kyc_upload: false
```

If this file is missing, unread, or the block is half-filled, treat **every row as `false`**.

Do not infer GO from: FAQ 6 being fixed, yen on the form, estimate ON, `image_missing` cleared, a merged PR, JOBS week Day 2, or [#90](https://github.com/rimone0511/autopilot-log/pull/90) / [#76](https://github.com/rimone0511/autopilot-log/pull/76) checklists.

**This authoring agent never flips a row to `true` and never clicks 公開する.**

---

## UI labels that mean GO (do not click unless the matching row is `true`)

| Gate row (must be `true`) | Live control (labels vary; live wins) |
|---|---|
| `coconala_publish_listing` | **公開する** / 出品を公開 / 公開中にする / この内容で公開する |
| `coconala_send_estimate` | 見積もりを送る / 提案する / 相談に返信して送信 |
| `coconala_resume_accepting` | 受付再開 / 受付中にする |
| `coconala_blog_embed` | ブログで紹介する / 埋め込みコード発行 |
| `coconala_sns_announce` | X / note / Blog / 「出品しました」 |
| `any_payout_kyc_upload` | 本人確認 / 口座 / インボイス / 顔撮影 |

If a dialog after **下書きで保存する** says the service will become **公開**, treat it as `coconala_publish_listing` — **cancel**.

---

## Allowed with every row false

1. MAIN Google on the **existing** account.
2. Open unpublished draft **4403529**.
3. Attach cover. Fix title ます if needed. Confirm FAQ 6 still covers スクレイピング.
4. **下書きで保存する** only when that control does not publish.
5. Close.

---

## Human GO procedure (only 祐太)

1. Cover is on the draft. Not `image_missing`.
2. Displayed title is `n8n自動化と手順書を作ります` (one ます).
3. Re-read guide_sell / guide_rule / category floor help.
4. Flip **one** row in a **local** copy if 祐太 wants an audit trail (still no secrets).
5. Click the **one** matching live control.
6. Stop. Do not also send 見積もり on the same click.

Committed default for this PR: **all `false`**.
