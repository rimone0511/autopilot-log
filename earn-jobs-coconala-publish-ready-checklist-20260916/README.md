# ココナラ publish-ready チェックリスト（JOBS）— 2026-09-16

**DRAFT_ONLY. NO LIVE PUBLISH.**  
Operator checklist to take an existing **draft_saved** Coconala seller profile to a **publish-ready 通常サービス** draft (fields / images / price / FAQ).  
**公開する is not this pack.** It needs an explicit human GO in [HUMAN-GO.md](HUMAN-GO.md) **and** 祐太 clicking the live control.

Pack date: 2026-09-16  
Desk: ココナラ / Coconala — Wave A1 / CU-01  
Start state: profile **`draft_saved`** (QUEUE `done-draft`)  
Target state: listing **`publish_ready_unpublished`** (下書き完了。公開中ではない)  
This authoring agent: **did not log in, did not 公開する, did not send 見積もり.**

Paste bodies live in sibling first-gig packs. **Point. Do not duplicate.**

Primary first-gig paste: **[PR#87](https://github.com/rimone0511/autopilot-log/pull/87)** `SERVICE-PASTE.md`. Do not also open PR#79 `01` as a second listing of the same n8n first gig.

---

## Hard rules

- **MAIN Google only** (`{{GOOGLE_ACCOUNT_EMAIL}}`). Do not create a second Coconala.
- **No secrets** in git (passwords, API keys, OTP, bank, My Number, ID images, filled yen).
- **No live publish.** Save as **下書きで保存する** only, until [HUMAN-GO.md](HUMAN-GO.md) is flipped **and** a human clicks 公開する.
- Do not send 見積もり / 募集応募 / トーク営業 from this pack.
- Do not invent GMV, 受注率, 時短, 精度％, or “this will sell”.
- Live form wins. Public help cited below; help.zendesk 403 from this agent is not a dead site.
- Buyer-facing text must not say “unpublished draft” (it would remain after a later GO).

---

## Files

| File | Role |
|---|---|
| [CHECKLIST.md](CHECKLIST.md) | Ordered ticks: profile stay parked → first-gig fields → images → price → FAQ → 下書き保存 |
| [HUMAN-GO.md](HUMAN-GO.md) | Fail-closed switch. Default `coconala_publish_listing: false` |
| [GAPS.md](GAPS.md) | Empty template for what the look/fill pass found |
| [STATUS.md](STATUS.md) | Desk box. This agent did not run a live fill |

Tick boxes on a **local** copy. Do not commit a live service URL, filled `{{PRICE_YEN}}`, or an ID screenshot.

---

## First-gig paste packs (point here — do not copy fences)

These are the listing paste sources. This folder is the **operator order + GO gate**.

| Pack | Path (on that PR branch, not `master`) | PR | Use for |
|---|---|---|---|
| **First n8n gig full paste** | `earn-jobs-coconala-first-gig-full-paste-20260916/` | [#87](https://github.com/rimone0511/autopilot-log/pull/87) | **This pass.** `SERVICE-PASTE.md` title / catch / TOC / サービス内容 / FAQ 7 / tiers `{{YEN}}` / options / お願い. Gates: `DRAFT_ONLY.md` `STOP-KYC.md` |
| Listing DRAFTS x3 | `earn-jobs-coconala-service-drafts-20260916/` | [#79](https://github.com/rimone0511/autopilot-log/pull/79) | Later **different** offers only (`02` 分類 / `03` AI運用伴走). Do **not** also paste `01` as a second first gig |
| Pricing overlay (tokens) | `earn-jobs-pricing-menu-20260916/COCONALA-PASTE.md` | [#82](https://github.com/rimone0511/autopilot-log/pull/82) | `{{PRICE_JPY_SKU_*}}` ladder. Does **not** retitle over #87 |
| QUEUE placeholder | `earn-packs/coconala/` | [#8](https://github.com/rimone0511/autopilot-log/pull/8) INDEX | **missing** (`unknown`). Do not invent files there |

Default first gig for **this** pass: **#87 `SERVICE-PASTE.md`** (`n8nの小さな自動化を1本作ります`).  
#79 `02` / `03` are different offers, not duplicate SKUs. Do **not** publish them from this checklist. Optional later drafts only. Do not run #79 `01` and #87 on two listings — same first-gig family.

Do **not** paste estimate/proposal packs into サービス内容:

| Pack | Path | PR | Why not listing body |
|---|---|---|---|
| Wave 1 見積もり | `earn-jp-proposal-drafts-20260916/03-llm-ops-coconala-estimate.md` | [#11](https://github.com/rimone0511/autopilot-log/pull/11) | Estimate reply. Explicitly not the 1000-字 gig body |
| Wave 2 応募文 | `earn-jp-proposal-wave2-20260916/` `03` / `07` / `10` | [#28](https://github.com/rimone0511/autopilot-log/pull/28) | Inquiry/custom **replies**, not 出品ページ |
| JOBS replies | `earn-jobs-coconala-proposal-replies-20260916/` | [#81](https://github.com/rimone0511/autopilot-log/pull/81) | After a live 見積もり thread. Out of this pack |

---

## Starting desk state (pointers — do not rewrite QUEUE)

| Source | Path | PR | Coconala hint |
|---|---|---|---|
| QUEUE | `earn-register-expand-20260916/QUEUE.md` A1 | [#1](https://github.com/rimone0511/autopilot-log/pull/1) | `done-draft` — 出品は下書きのまま。公開しない |
| Wave A morning STATUS | `ops/earn/register-wave-a-status-20260916/STATUS.md` | [#54](https://github.com/rimone0511/autopilot-log/pull/54) | `draft_saved` |
| Snapshot 05:19 JST | `earn-register-status-snapshot-20260916-0519/STATUS.md` | [#49](https://github.com/rimone0511/autopilot-log/pull/49) | `draft_saved` |
| KYC slip | `earn-morning-kyc-slip-refresh-20260916/01-coconala.md` | [#43](https://github.com/rimone0511/autopilot-log/pull/43) | 出品 GO ではない。振込・NDA 画面が出たときだけ |
| JOBS week | `earn-jobs-weekly-earn-plan-20260916/` | [#76](https://github.com/rimone0511/autopilot-log/pull/76) | Day 2 look. `coconala_publish_listing: false` there too |

PR#76 was written before #79 / #87 landed; its “listing body pack is missing” line is stale for paste. **#87 is the first-gig pack.** This checklist is the fill order + GO gate.

---

## Public help (re-read at paste time)

| Topic | URL | GET this agent 2026-09-16 |
|---|---|---|
| 出品ガイド（通常サービス、キャッチ 30 字、価格帯、画像ステップ、公開） | https://coconala.com/pages/guide_sell | 200 |
| ルールとマナー（同一サービス複数出品・外部決済・虚偽） | https://coconala.com/pages/guide_rule | 200 |
| タイトル分割（提供内容 最大 25 字・「ます」、キャッチ 最大 30 字） | https://coconala.com/news/170 | 200 |
| 説明文（通常 1,000 字。セラーサポート 1,500 は買わない） | https://coconala.com/news/1220 | 200 |
| 文字数・画像（2026-09-01 案内。#87 が引用。ライブを正） | https://coconala.com/news/1372 | 200 |
| カテゴリ一覧 | https://coconala.com/categories/ | 200 |
| マグ：サービスページのコツ（FAQ・画像必須の案内） | https://mag.coconala.com/articles/knowhow-the-basics-of-service-pages | 200 |
| マグ：改善チェックリスト（できること／できないこと） | https://mag.coconala.com/articles/knowhow-list-to-improve-service-pages | 200 |
| マグ：景品表示法の販売ルール | https://mag.coconala.com/articles/knowhow-rules-about-selling | 200 |
| カテゴリ最低価格 | https://help.coconala.com/hc/ja/articles/360020963554 | 403 from this agent; still the cited help |
| 出品禁止一覧 | https://help.coconala.com/hc/ja/articles/9517249749017 | 403 from this agent |
| 本人確認（このパックでは開かない） | https://help.coconala.com/hc/ja/articles/218832717 | 403 from this agent |
| 出品フォーム（ログイン後） | https://coconala.com/services/add | 202 (challenge). Live logged-in form wins |

Fee %: guide_sell cites **22%** on 通常サービス販売総額 (2026-09-16 public page). Do not freeze that number in buyer-facing paste. Re-read before any human GO. Video-chat / phone services are **out of this pack**.

---

## Out of scope

- Marketplace signup / second account
- KYC / 口座 / インボイス / 電話番号登録
- 公開する / 受付中にする / SNS「出品しました」
- 見積もり送信・募集応募
- PRO / 有料ブースト / セラーサポート購入
- Copying sibling fences into `earn-packs/coconala/`
- Python posting-gate changes
