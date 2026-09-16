> **DRAFT_ONLY. DO NOT APPLY / SEND / PUBLISH / BID / PAY / KYC.**  
> Patrol: **2026-09-16 ~08:44 JST** · Owner: **仕事窓口** · Auth: MAIN Google only · **REGISTER-CU-CUT** active.

# APPLY-QUEUE — 2026-09-16 PM

JOBS-only refresh of today's DRAFT_ONLY apply queue. Public-read boards only. No marketplace registration. No Wave B/D register packs / activity gates. No publish / apply / bid / send.

Boards reused from prior packs: [#80](https://github.com/rimone0511/autopilot-log/pull/80) JP+EN scan, [#112](https://github.com/rimone0511/autopilot-log/pull/112) AM queue, JP drafts [#11](https://github.com/rimone0511/autopilot-log/pull/11) [#28](https://github.com/rimone0511/autopilot-log/pull/28) [#81](https://github.com/rimone0511/autopilot-log/pull/81) [#92](https://github.com/rimone0511/autopilot-log/pull/92), EN/Contra [#71](https://github.com/rimone0511/autopilot-log/pull/71) [#98](https://github.com/rimone0511/autopilot-log/pull/98), inquiry template [#122](https://github.com/rimone0511/autopilot-log/pull/122).

This file is **not** a GO. Rank is proximity to a still-open thread, not GMV.

**URL rule:** live IDs below were fetched this PM, or marked **`unverified`**. Do not invent a new apply URL.

---

## Already done / parked this morning (do not redo)

| Item | State | Note |
|---|---|---|
| Contra style-01 paste | **`blocked_pro_wall`** · parked | Do not retry Pro / Apply. [#98](https://github.com/rimone0511/autopilot-log/pull/98) stays do-not-send. |
| Coconala listing **4403529** cover | **`cover_saved_unpublished`** | Guest GET still **404**. Do not 公開する. [#103](https://github.com/rimone0511/autopilot-log/pull/103) [#113](https://github.com/rimone0511/autopilot-log/pull/113) |
| Coconala request **5258870** estimate | **`prepped_not_sent`** | Owner GO deferred. **Do not re-send.** Recheck URL only if a later dated GO names this ID. |
| Coconala request **5259006** | **skip** | Lステップ / エルメ must-have. Still `open_read` — do not apply. |
| CrowdWorks / Lancers / Upwork | **`blocked_skip`** | Public look only. No login retry. |
| REGISTER-CU-CUT | **active** | No Wave B/D register. No KYC. |

---

## Next CU (do these, then stop)

Max **2** concrete jobs. Both URLs were **`open_read`** this PM (guest recheck still OPEN). Filled drafts live in [drafts/DRAFTS-INDEX.md](drafts/DRAFTS-INDEX.md) (`draft_ready_not_sent`). **Do not send.**

### 1. Coconala 5272940 — Claude / Sheets / GAS 全体設計（第1フェーズ）

| | |
|---|---|
| Desk | ココナラ request |
| URL | https://coconala.com/requests/5272940 · **`open_read`** 締切 **2026-09-22** · 掲載 2026-09-15 |
| Page text | 予算帯 **3万〜5万円**（listing band, not a bid）· 応募 61 / 契約 0（this fetch; numbers move） |
| Why-fit | 太陽光施工会社の Claude 製社内アプリ群の **初期診断・全体設計**。求めるスキル欄は **GAS / スプレッドシート**。Drive / Sheets / Slack 連携。実装費ではなく 1–2h ヒアリング + 構成提案。公開 CLI より **LLM-ops + Sheets** に近い。 |
| CU action | Recheck URL. If 募集終了 → stop. Open **one** sibling draft. Rewrite `{{ONE_SPECIFIC_DETAIL}}` from **this** page (例: 案件管理 / 工事単価表 / 現場報告が複数台帳に散っている). Price stays `{{PRICE_YEN}}` local. **Stop before 見積もり送信.** |
| Draft pointer | **Filled:** [drafts/5272940-coconala-proposal.md](drafts/5272940-coconala-proposal.md). Voice from [#81](https://github.com/rimone0511/autopilot-log/pull/81) `05`/`06` · [#11](https://github.com/rimone0511/autopilot-log/pull/11) `03` · [#122](https://github.com/rimone0511/autopilot-log/pull/122) JP inquiry. **Do not paste the 5258870 letter onto this ID.** |
| Expected | **`draft_ready_not_sent`** · do-not-send |
| GO-gate | `coconala_send_estimate: false` |
| Do not | 公開する / 見積もり送信 / 本人確認 / Web3 5260959 / invent yen |

### 2. Coconala 5257064 — マニュアル／取材動画の自動編集ワークフロー

| | |
|---|---|
| Desk | ココナラ request |
| URL | https://coconala.com/requests/5257064 · **`open_read`** 締切 **2026-09-20** · 掲載 2026-09-07 |
| Page text | 予算帯 **5万〜8万円**（listing band, not a bid; page also shows 5万 / 10万 一式 as **their** wording）· 応募 47 / 契約 0（this fetch） |
| Why-fit | 既存素材 → 粗編集 / 字幕 / 規定アニメの **再利用ワークフロー + Claude Code ソース + 手順**. Adjacent to [#92](https://github.com/rimone0511/autopilot-log/pull/92) Python pipeline honesty and [#78](https://github.com/rimone0511/autopilot-log/pull/78) demo SOPs. **Not** a YouTube upload job. |
| CU action | Recheck URL. Closed → stop. One sibling file. Fill `{{ONE_SPECIFIC_DETAIL}}` from **this** page (例: お手本動画と同構成 / 50–100GB 素材 / 依頼者環境で再実行). Honest split: local FFmpeg / 字幕同期 yes; ブラウザ編集 no; 投稿 API は別見積. **Stop before 見積もり送信.** |
| Draft pointer | **Filled:** [drafts/5257064-coconala-proposal.md](drafts/5257064-coconala-proposal.md). Angle only from [#92](https://github.com/rimone0511/autopilot-log/pull/92) `01` and [#78](https://github.com/rimone0511/autopilot-log/pull/78). **New ID = new letter.** Do not reuse the 5258870 filled paste. |
| Expected | **`draft_ready_not_sent`** · do-not-send |
| GO-gate | `coconala_send_estimate: false` |
| Do not | Bid amounts in git / 郵送デバイス受け取りの個人情報 / 公開する |

One CU at a time. Do not stack 5272940 + 5257064 send.

---

## Apply candidates (max 10)

| # | Title | Desk | URL / status | Why-fit | Draft pointer | GO-gate |
|---|---|---|---|---|---|---|
| **1** | Claude 社内アプリ群の全体設計（第1フェーズ） | ココナラ request | https://coconala.com/requests/5272940 · **`open_read`** 締切 **2026-09-22** | Sheets / GAS / Slack / Claude 設計相談。実装ではない。 | [drafts/5272940-coconala-proposal.md](drafts/5272940-coconala-proposal.md) **`draft_ready_not_sent`** · voice [#81](https://github.com/rimone0511/autopilot-log/pull/81)/[#11](https://github.com/rimone0511/autopilot-log/pull/11)/[#122](https://github.com/rimone0511/autopilot-log/pull/122) · **do-not-send** | `coconala_send_estimate: false` |
| **2** | マニュアル／取材動画の自動編集ワークフロー | ココナラ request | https://coconala.com/requests/5257064 · **`open_read`** 締切 **2026-09-20** | 再利用 WF + ソース + 手順。投稿は範囲外。 | [drafts/5257064-coconala-proposal.md](drafts/5257064-coconala-proposal.md) **`draft_ready_not_sent`** · new letter · angle [#92](https://github.com/rimone0511/autopilot-log/pull/92)/[#78](https://github.com/rimone0511/autopilot-log/pull/78) · **do-not-send** | `coconala_send_estimate: false` |
| **3** | Python YouTube 生成スクリプト（Whisper / Claude / VOICEVOX / FFmpeg → mp4） | ココナラ request | https://coconala.com/requests/5258870 · **`open_read`** 締切 **2026-09-22** · AM **`prepped_not_sent`** | Still open. Upload is not in the brief. | [#92](https://github.com/rimone0511/autopilot-log/pull/92) `01-5258870-…` already prepped. **Owner GO deferred — do not re-send.** | `coconala_send_estimate: false` |
| **4** | SNS / LINE・Lステップ自動化 | ココナラ request | https://coconala.com/requests/5259006 · **`open_read`** 締切 **2026-09-22** · listing band 5万〜8万（page text, not a bid） | Still open. **Lステップ/エルメ必須.** | [#92](https://github.com/rimone0511/autopilot-log/pull/92) `02-5259006-…` · **skip** | `coconala_send_estimate: false` |
| **5** | 求職者向け公式LINE構築 | ココナラ request | https://coconala.com/requests/5263315 · **`open_read`** 締切 **2026-09-20** | Same Lステップ must-have as 5259006. | No new letter. **skip** | `coconala_send_estimate: false` |
| **6** | Contra Job-feed · style **01** inbound n8n / official-API | Contra Independent | **No inbound-n8n Job-feed ID this PM** · feed URL **`unverified`** (logged-out GET timeout / 103) · desk **`blocked_pro_wall`** | Seller core still matches [#98](https://github.com/rimone0511/autopilot-log/pull/98). Wall is Pro, not missing copy. | [#98](https://github.com/rimone0511/autopilot-log/pull/98) `PASTE.md` · **parked** · do-not-send | `contra_apply_opportunity: false` |
| **7** | Kajabi portal + email automation | Contra opportunity | https://contra.com/opportunity/UBkkYMmW-kajabi-portal-and-automation-developer-needed · page **`open_read`** (JobPosting JSON) · `datePosted` **2025-08-18** → still-hiring **`unverified`** | Weak vs CLI. Kajabi is not the public repo. | [#71](https://github.com/rimone0511/autopilot-log/pull/71) / [#5](https://github.com/rimone0511/autopilot-log/pull/5) `06` only if still hiring **and** honest stretch · else skip. Desk parked. | `contra_apply_opportunity: false` |
| **8** | AI社員の設計・運用支援（Codex） | ココナラ request | https://coconala.com/requests/5266371 · **`open_read`** 締切 **2026-09-25** | Multi-agent / cron / 失敗記録は隣接。**必須は Codex 経験**（Claude Code 不可と明記）。 | Stretch only if Codex is honest. Else **skip**. Pointer: [#81](https://github.com/rimone0511/autopilot-log/pull/81) `05` angle, new letter. | `coconala_send_estimate: false` |
| **9** | ココナラ inbound 見積もり on existing draft | ココナラ seller | Inbox **`unverified`** (no login this patrol) · listing **4403529** still unpublished (guest **404**) | Nearest JP paid thread **if** a live 相談 exists. Cover is already `cover_saved_unpublished`. | [#81](https://github.com/rimone0511/autopilot-log/pull/81) or [#122](https://github.com/rimone0511/autopilot-log/pull/122) JP inquiry · one thread · fill `{{ONE_SPECIFIC_DETAIL}}` or skip | `coconala_send_estimate: false` |
| **10** | システム開発 依頼一覧（GAS / Sheets 混在） | ココナラ requests | https://coconala.com/requests/categories/232 · **`read_search`** · **no new in-scope apply ID this PM** | Almost all cards **募集終了**. Live-but-out: [5260959](https://coconala.com/requests/5260959) Web3/wallet（skip）. Interview [5252560](https://coconala.com/requests/5252560) Linux kernel（skip）. | After a **clicked open** in-scope ID: [#11](https://github.com/rimone0511/autopilot-log/pull/11) / [#28](https://github.com/rimone0511/autopilot-log/pull/28). Skip フォーム一括送信 / ブラウザ操作. | `coconala_send_estimate: false` |

**Keyword searches this PM (not extra apply IDs):**

| Query | URL | Result |
|---|---|---|
| Coconala requests `n8n` | https://coconala.com/requests?keyword=n8n | **`read_search`**. Cards were closed / false-positive titles. No live n8n-titled request extracted. Closed n8n twins: [4788537](https://coconala.com/requests/4788537) 2026-01-31 · [4127646](https://coconala.com/requests/4127646) 2025-04-20. |
| Coconala requests `Python` | https://coconala.com/requests?keyword=Python | **`read_search`**. Live in-scope hit = **5258870** (already prepped). |
| Coconala requests `自動化` | https://coconala.com/requests?keyword=%E8%87%AA%E5%8B%95%E5%8C%96 | **`read_search`**. Live hits used above (5258870 / 5259006 / 5257064 / 5266371). |
| Coconala cat 28 生成AI | https://coconala.com/requests/categories/28 | **`read_search`**. Live: 5272940 / 5258870 / 5270292 / 5266371. |
| Contra `/jobs` + `/independent/jobs` | contra.com job feed | **`unverified`** (timeout). Do not invent a Job-feed slug. |
| Contra Airtable opportunity | https://contra.com/opportunity/P2POBPYP-airtable-and-automation-expert-needed | **`unverified`** (timeout this PM). |

**Not apply (catalog / out-of-scope):** Coconala `n8n` seller search, competitor gigs 4268304 / 4268246, Contra portfolio pages, Fiverr PX, Web3 5260959, ハローワーク scrape 5270892, Amazon SP-API pentest 5273912, FX EA 5273878. Use catalog wording later. Do not bid on another seller's gig.

---

## Closed / skip this PM (do not recycle paste)

| ID | Status | Note |
|---|---|---|
| Coconala **5258870** send | `open_read` · **do-not-resend** | `prepped_not_sent`. Owner GO deferred. |
| Coconala **5259006** | `open_read` · **skip** | Lステップ / エルメ must-have. |
| Coconala **5263315** | `open_read` · **skip** | 公式LINE + Lステップ必須. |
| Coconala **4403529** public | **404** | unpublished draft id only · cover already saved |
| Coconala **5253047** | **closed** | 締切 2026-09-11 |
| Coconala **5228081** | **closed** | 締切 2026-08-24 |
| Coconala **5194189** | **closed** | GAS/LINE 不動産 · 締切 2026-08-18 |
| Coconala **5214788** | **closed** | Zoom×Slack×Sheets 公式API · 締切 2026-08-25 · 契約 1 |
| Coconala **4788537** / **4786490** | **closed** | n8n/Make 台本WF · 締切 2026-01-31 |
| Coconala **4127646** | **closed** | n8n チャットボットサポート · 締切 2025-04-20 |
| Coconala **5239457** + [#80](https://github.com/rimone0511/autopilot-log/pull/80) CLOSED.md | **closed** | Stay closed unless a **new** URL reopens |
| Coconala cat 232 remainder | **closed** (this PM list) | GOLD EA 5258184, 予約 5242583, マークテック 5239457, バレエExcel 5234776, ダンスSheets 5212586, フォーム営業 5157494, TikTok Shop 5058160, いいね自動化 5048760, ほか一覧の「募集終了」 |
| CrowdWorks / Lancers / Upwork desks | **`blocked_skip`** | No apply. AM CW 13438314 stay do-not-apply (Flutter + desk 403). Lancers 5459128 / 5457696 stay closed. |
| Contra apply | **`blocked_pro_wall`** | Parked. No Pro. No second account. |

If a URL says 募集終了 / 非公開: stop. Do not paste that draft onto a different ID.

---

## How to use a template (still DRAFT)

1. Recheck the official URL. Closed → stop.
2. Open **one** sibling file. Do not invent a new letter. Do not move a filled paste onto another ID.
3. Replace `{{ONE_SPECIFIC_DETAIL}}` from **that** page. Empty in ~1 minute → skip.
4. Price / rate tokens stay **local**. Do not commit yen/USD. Do not invent bid amounts.
5. No email / phone / LINE / off-platform pay in the paste.
6. Agent never clicks 応募する / Apply / Bid / 公開する / 見積もりを送る.

---

## Hard stops

- No marketplace registration. **REGISTER-CU-CUT** active. No Wave B/D register packs. No activity-gate CU notes.
- No Fiverr hold retry, Lancers captcha retry, CrowdWorks 403 retry, Upwork Google retry.
- No Contra Pro / Persona / wallet. `blocked_pro_wall` stays parked.
- No KYC / ads / Connects / secrets in git.
- No publish / apply / bid / send from this PR.
- DRAFT_ONLY. GO-gates stay **false**.

## 日本語（運用）

今ある下書きは **2つだけ**（`draft_ready_not_sent`）: [5272940](drafts/5272940-coconala-proposal.md) と [5257064](drafts/5257064-coconala-proposal.md)。公式URLが開いていることを再確認し、**送らない**。朝に済んだ Contra 貼り付け（Pro壁）・4403529 カバー・5258870 見積もり下書きは触らない。5259006 / 5263315 は Lステップ必須なのでスキップ。CW / Lancers / Upwork は机ごとスキップ。送信・公開は人が GO を書いたあと。
