> **DRAFT_ONLY. DO NOT APPLY / SEND / PUBLISH / BID / PAY / KYC.**  
> Patrol: **2026-09-16 ~06:35 JST** · Owner: **仕事窓口** · Auth: MAIN Google only.

# APPLY-QUEUE — 2026-09-16 AM

Refresh of today's JOBS apply queue. Boards reused from prior packs: [#80](https://github.com/rimone0511/autopilot-log/pull/80) JP+EN scan, [#25](https://github.com/rimone0511/autopilot-log/pull/25) world gigs, JP CW/Coconala drafts [#11](https://github.com/rimone0511/autopilot-log/pull/11) [#28](https://github.com/rimone0511/autopilot-log/pull/28) [#92](https://github.com/rimone0511/autopilot-log/pull/92), EN/Contra [#5](https://github.com/rimone0511/autopilot-log/pull/5) [#31](https://github.com/rimone0511/autopilot-log/pull/31) [#71](https://github.com/rimone0511/autopilot-log/pull/71) [#98](https://github.com/rimone0511/autopilot-log/pull/98).

This file is **not** a GO. Rank is proximity to a still-open thread, not GMV.

**URL rule:** live IDs below were fetched this AM, or marked **`unverified`**. Do not invent a new apply URL.

---

## Next CU (do these, then stop)

### 1. Contra — one paste DRAFT (do-not-send)

| | |
|---|---|
| Desk | Contra Independent · already `draft_saved` ([#64](https://github.com/rimone0511/autopilot-log/pull/64)) · **`apply: no`** |
| Pack | [#98](https://github.com/rimone0511/autopilot-log/pull/98) `PASTE.md` = PR#71 style **01 n8n inbound** only |
| Playbook | [#86](https://github.com/rimone0511/autopilot-log/pull/86) LOOK → PREP. Do not skip. |
| CU action | Existing Free Independent, MAIN Google. Official Job feed. **One** listing that is inbound n8n / official-API + failure alert + SOP. Rewrite `{{ONE_SPECIFIC_DETAIL}}` **locally**. Re-count. **Stop before Apply.** |
| Expected | `prepped_not_sent` or `style_skipped` |
| GO-gate | `contra_apply_opportunity: false` · `send_go: false` |
| Do not | Styles 02–05, Pro/Max, Persona/wallet, Kent USA → Japan, Apply/Submit, second account |

No live Job-feed ID is claimed this AM. Kajabi (#5) is **stretch / age-check**, not the one-shot match.

### 2. Coconala — cover-image gap (listing, not apply)

| | |
|---|---|
| Desk | ココナラ unpublished 通常サービス **4403529** |
| Pack | [#103](https://github.com/rimone0511/autopilot-log/pull/103) · checklist [#90](https://github.com/rimone0511/autopilot-log/pull/90) |
| This AM | Guest GET `https://coconala.com/services/4403529` → **404** (still unpublished). Do not announce as a shop. |
| CU action | Open **existing** draft. Attach **one original** cover (n8n flow + 手順書; secrets/emails/tokens cropped; no partner logos). Optional title check: displayed `n8n自動化と手順書を作ります` (one ます). **下書きで保存する.** Confirm still 下書き. |
| Expected | `image_missing` → cover attached, still unpublished |
| GO-gate | `coconala_publish_listing: false` · `coconala_send_estimate: false` |
| Do not | 公開する / 見積もり送信 / 本人確認 / second n8n listing / commit the image |

Cover first. Publish is a later human GO **outside** this folder.

---

## Apply candidates (max 10)

| # | Title | Desk | URL / status | Why-fit | Draft-status | GO-gate |
|---|---|---|---|---|---|---|
| **1** | Python YouTube 生成スクリプト（Whisper / Claude / VOICEVOX / FFmpeg → mp4） | ココナラ request | https://coconala.com/requests/5258870 · **`open_read`** 締切 **2026-09-22** | Local Python pipeline + 手順書. **Upload is not in the brief.** | Reuse [#92](https://github.com/rimone0511/autopilot-log/pull/92) `01-5258870-…` · **do-not-send** | `coconala_send_estimate: false` |
| **2** | SNS / LINE・Lステップ自動化 | ココナラ request | https://coconala.com/requests/5259006 · **`open_read`** 締切 **2026-09-22** · listing band 5万〜8万（page text, not a bid） | Stretch. **Lステップ/エルメ必須.** Skip unless that experience is honest. | Reuse [#92](https://github.com/rimone0511/autopilot-log/pull/92) `02-5259006-…` · default **skip** | `coconala_send_estimate: false` |
| **3** | Contra Job-feed · style **01** inbound n8n | Contra Independent | **No ID this AM** · LOOK first | Matches seller core + [#98](https://github.com/rimone0511/autopilot-log/pull/98) one-shot | [#98](https://github.com/rimone0511/autopilot-log/pull/98) `PASTE.md` · **do-not-send** | `contra_apply_opportunity: false` |
| **4** | Kajabi portal + email automation | Contra opportunity | https://contra.com/opportunity/UBkkYMmW-kajabi-portal-and-automation-developer-needed · page **`open_read`** (JobPosting JSON) · `datePosted` **2025-08-18** → **still-hiring `unverified`** | Weak vs CLI. Kajabi is not the public repo. | [#71](https://github.com/rimone0511/autopilot-log/pull/71) / [#5](https://github.com/rimone0511/autopilot-log/pull/5) `06` only if still hiring **and** honest stretch · else skip | `contra_apply_opportunity: false` |
| **5** | ココナラ inbound 見積もり on existing draft | ココナラ seller | Inbox **`unverified`** (no login this patrol) · listing **4403529** unpublished | Nearest JP paid thread **if** a live 相談 exists. Cover gap does **not** block reading inbox. | [#11](https://github.com/rimone0511/autopilot-log/pull/11) `03-llm-ops-coconala-estimate.md` or [#81](https://github.com/rimone0511/autopilot-log/pull/81) · one thread · fill `{{ONE_SPECIFIC_DETAIL}}` or skip | `coconala_send_estimate: false` |
| **6** | システム開発 依頼一覧（GAS / Sheets / Cursor 混在） | ココナラ requests | https://coconala.com/requests/categories/232 · **`read_search`** · **no new apply ID extracted this AM** | Small Sheets/GAS/GitHub jobs sit next to out-of-scope cards. | After a **clicked open** ID: [#11](https://github.com/rimone0511/autopilot-log/pull/11) / [#28](https://github.com/rimone0511/autopilot-log/pull/28). Skip フォーム一括送信 / ブラウザ操作. | `coconala_send_estimate: false` |
| **7** | n8n / GAS 歓迎 · **Flutter 必須** | CrowdWorks | https://crowdworks.jp/public/jobs/13438314 · **`open_read`** 応募期限 **2026-09-22** | n8n/GAS/Webhook welcome. **Must:** Flutter + Node + AWS/Firebase. Public CLI is not Flutter. | Desk is **`blocked_skip` 403** ([#88](https://github.com/rimone0511/autopilot-log/pull/88) PARK). Do not retry login. If desk later clears: still **skip** unless Flutter is honest. Template pointer only: [#28](https://github.com/rimone0511/autopilot-log/pull/28) n8n slice. | Desk GO **closed** · no CW apply from this pack |
| **8** | CrowdWorks keyword `n8n` / `YouTube API` / `Dify` | CrowdWorks search | https://crowdworks.jp/public/jobs?search%5Bkeywords%5D=n8n · **`unverified`** (thin/login HTML, same as #80) | Same nouns as Wave 2 JP packs. Prior IDs in #80 CLOSED.md stay closed. | Browser **募集中** only. [#11](https://github.com/rimone0511/autopilot-log/pull/11) `01` / [#28](https://github.com/rimone0511/autopilot-log/pull/28) `01` `05` after a live ID. | Desk **`blocked_skip`** · do not apply |
| **9** | Lancers `keyword=n8n` (請求・初期構築カード) | Lancers search | https://www.lancers.jp/work/search?keyword=n8n · **`read_search`** · **click-ID `unverified`** | n8n + Sheets + 手順書 matches Wave 2. | Closed this AM (do not apply): [5459128](https://www.lancers.jp/work/detail/5459128) 2025-12-26終了 · [5457696](https://www.lancers.jp/work/detail/5457696) 2025-12-25終了. New row → [#28](https://github.com/rimone0511/autopilot-log/pull/28) `02` / `03`. | Desk **`blocked_skip` captcha** · do not apply |
| **10** | Upwork n8n board + prior apply URLs | Upwork | https://www.upwork.com/freelance-jobs/n8n/ · **`unverified`** (timeout this AM) · sibling apply URLs in #80 rows 12–15 still **`needs_check`** | Official-API n8n jobs match EN packs. | [#70](https://github.com/rimone0511/autopilot-log/pull/70) / [#31](https://github.com/rimone0511/autopilot-log/pull/31) `01` after live recheck. **0 Connects.** | Desk **`blocked_skip` Google/SSO** · do not apply |

**Not apply (catalog / keyword only):** Coconala `n8n` search, competitor gigs 4268304 / 4268246, Contra portfolio pages, Fiverr PX search. Use for wording later. Do not bid on another seller's gig.

---

## Closed / skip this AM (do not recycle paste)

| ID | Note |
|---|---|
| Coconala 5253047 | 募集終了（締切 2026-09-11） |
| Coconala 5228081 | 募集終了（締切 2026-08-24） |
| Coconala 4403529 **public** | 404 · unpublished draft id only |
| Lancers 5459128 / 5457696 | 募集終了 2025-12 · still in search HTML |
| #80 CLOSED.md IDs | Stay closed unless a **new** URL reopens |

If a URL says 募集終了 / 非公開: stop. Do not paste that draft onto a different ID.

---

## How to use a template (still DRAFT)

1. Recheck the official URL. Closed → stop.
2. Open **one** sibling file. Do not invent a new letter.
3. Replace `{{ONE_SPECIFIC_DETAIL}}` from **that** page. Empty in ~1 minute → skip.
4. Price / rate tokens stay **local**. Do not commit yen/USD.
5. No email / phone / LINE / off-platform pay in the paste.
6. Agent never clicks 応募する / Apply / Bid / 公開する.

---

## Hard stops

- No marketplace registration. No Wave B–D register packs. No activity-gate CU notes.
- No Fiverr hold retry, Lancers captcha retry, CrowdWorks 403 retry, Upwork Google retry.
- No Pro / Connects / wallet / KYC / ads.
- No secrets in git.

## 日本語（運用）

今やるのは **2つだけ**: Contra の 01 文面を1件ローカルで埋めて送らない。ココナラ 4403529 にカバー画像を足して下書きのまま。応募候補は上表。開いていると確認できたのは **5258870 / 5259006**（9006 は Lステップ必須なので原則スキップ）と CW **13438314**（机が 403・Flutter 必須なので応募しない）。それ以外の URL は **未確認** か検索一覧。送信・公開は人が GO を書いたあと。
