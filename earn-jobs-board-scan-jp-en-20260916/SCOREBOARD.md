# SCOREBOARD — 20 apply-candidate jobs/gigs (JP+EN)

**DRAFT_ONLY. DO NOT APPLY.** Public-web scan only. No signup. No invented pay.

Scan: 2026-09-15 UTC. Folder date 2026-09-16.

## How to read status

| Status | Meaning |
|---|---|
| `open_read` | Live page read; board still accepting (or still showing 募集中 / あと N 日). Recheck before send. |
| `read_search` | Search/category HTML read; **specific apply ID may already be closed**. Click through. |
| `needs_check` | URL is public, but this agent did **not** fully read the live page (JS/PX, timeout, login wall, empty body). |
| `catalog_read` | Seller gig / portfolio (keyword demand). **Not a bid job.** Use for wording, not for “apply now”. |

**Pay:** only text that was on the cited page. `pay_not_on_page` = do not invent a number. Listing bands are **that listing**, not GMV.

**Fit:** qualitative vs this operator’s public CLI (YouTube Data API / TikTok Content Posting API / Python / fail-closed gate / no browser automation). Not a money rank.

Closed IDs confirmed this scan live in [CLOSED.md](CLOSED.md) — **not** counted in the 20.

---

## The 20

| # | ID | Desk | Kind | Status | Pay on page |
|---|---|---|---|---|---|
| 1 | JP-COCO-5258870 | Coconala request | Python YouTube 生成スクリプト | `open_read` (締切 2026-09-22) | `pay_not_on_page` |
| 2 | JP-COCO-5259006 | Coconala request | LINE / Lステップ / Instagram 自動化 | `open_read` (締切 2026-09-22) | listing 5万〜8万円 |
| 3 | JP-LAN-N8N | Lancers search | n8n 請求・初期構築カード | `read_search` | cards show bands; **click ID** |
| 4 | JP-LAN-AIAGENT | Lancers category | AI自動化・エージェント | `read_search` | cards show bands; **click ID** |
| 5 | JP-LAN-YT | Lancers search | keyword `YouTube` | `read_search` | mostly 編集/台本 cards |
| 6 | JP-CW-N8N | CrowdWorks search | keyword `n8n` | **`needs_check`** | — |
| 7 | JP-CW-YTAPI | CrowdWorks search | `YouTube API` / `Dify` | **`needs_check`** | — |
| 8 | JP-COCO-REQ232 | Coconala requests | システム開発 依頼一覧 | `read_search` | cards mix; **click ID** |
| 9 | JP-COCO-N8N-KW | Coconala catalog | search `n8n` | `catalog_read` | seller list prices |
| 10 | JP-COCO-4268304 | Coconala gig | YouTube 制作〜Data API 予約投稿 | `catalog_read` | seller 3万/5万 キャンペーン文 |
| 11 | JP-COCO-4268246 | Coconala gig | n8n フォルダ投入→YouTube投稿 | `catalog_read` | option 2万円帯 on page |
| 12 | EN-UW-OPENCLAW | Upwork job | n8n + OpenClaw + social publish | snippet `read` / page **`needs_check`** | hours on title; **no $ invented** |
| 13 | EN-UW-HERMES | Upwork job | Hermes agent, X+LinkedIn APIs | snippet `read` / page **`needs_check`** | title showed $300 fixed |
| 14 | EN-UW-CRM | Upwork job | Zapier/Make CRM; n8n nice-to-have | snippet `read` / page **`needs_check`** | `pay_not_on_snippet` |
| 15 | EN-UW-DOCS | Upwork job | Zapier/Make docs + e-sign | snippet `read` / page **`needs_check`** | `pay_not_on_snippet` |
| 16 | EN-UW-N8N-BOARD | Upwork browse | `/freelance-jobs/n8n/` | **`needs_check`** | — |
| 17 | EN-FV-N8N-YT | Fiverr search | `n8n youtube automation` | **`needs_check`** (PX) | — |
| 18 | EN-FV-JBENJAMIN | Fiverr gig | n8n YouTube / faceless / agent | index `read` / page **`needs_check`** | **do not copy seller $ as bid** |
| 19 | EN-CONTRA-KAJABI | Contra opportunity | Kajabi portal + email automation | `open_read` (JSON JobPosting) | `pay_not_on_page` |
| 20 | EN-CONTRA-YT-N8N | Contra project | n8n YouTube analytics pipeline | `catalog_read` | `pay_not_on_page` |

---

## 1. JP-COCO-5258870 — Python YouTube 生成（apply）

- **URL:** https://coconala.com/requests/5258870
- **Status:** `open_read`. 掲載 2026-09-08。締切 **2026-09-22**（ページ「あと N 日」）。応募人数はページ表示（この fetch で 140 / 契約 0）。数字は変動する。
- **Pay:** `pay_not_on_page`（予算欄は空。応募者コメントに金額が出ても **git に書かない**）。
- **Why fit:** Python 一式 + 起動スクリプト + 手順書。Whisper / Claude / VOICEVOX / FFmpeg で **mp4 を出す**仕事。このオペレータの公開物は投稿ゲート付き CLI だが、**制作パイプライン（ローカル Python）**は隣接。**YouTube へ上げる部分はこの依頼文に無い**（生成まで）。
- **Out:** 権利のない素材、ブラウザ投稿、コメント自動化。
- **Draft angle (DO NOT SEND):**  
  依頼は「台本/音声 → テロップ同期 mp4」までと読む。納品はソース + `.bat` + 手順。外部 API 鍵は依頼者側。投稿（Data API）が必要なら **別見積・公式 API のみ**。Playwright は使わない。金額・納期は画面の別欄。`{{PRICE_YEN_DRAFT}}` / `{{LEAD_TIME_DRAFT}}`。公開根拠は yutalab.dev と GitHub CLI。**送信しない。**

---

## 2. JP-COCO-5259006 — LINE / Lステップ（apply, stretch）

- **URL:** https://coconala.com/requests/5259006
- **Status:** `open_read`. 締切 **2026-09-22**。応募 42 / 契約 0（この fetch）。
- **Pay:** ページ表記 **5万円〜8万円**（listing band, not GMV）。
- **Why fit:** 「Python での自動化」が歓迎。公式 Messaging API なら隣接。
- **Out / stretch:** **必須が Lステップ / エルメ構築経験**。未経験なら見送る。Instagram 運用代行・広告運用は本業の API 投稿 CLI と別物。
- **Draft angle (DO NOT SEND):**  
  必須の Lステップ実績が無いなら **応募しない**。ある場合だけ: LINE 公式の公式 API 範囲、送信は承認後、スクレイピング無し。金額はページ帯を復唱せず `{{PRICE_YEN_DRAFT}}`。**送信しない。**

---

## 3. JP-LAN-N8N — Lancers `keyword=n8n`

- **URL:** https://www.lancers.jp/work/search?keyword=n8n
- **Status:** `read_search`. このスキャンの一覧は **「募集終了」混在**。カード例（タイトルのみ。ID はクリック時に取る）: 「n8nを使った請求書自動化」「n8n 初期構築・セットアップ」「n8nとTwitter API」「n8n ワークフロー実装とGoogle Sheets」。詳細 ID 5459128 等は [CLOSED.md](CLOSED.md) で終了確認済み → **一覧の新しい行だけ**を開く。
- **Pay:** カードに 10,000〜20,000 円 / 100,000〜200,000 円 などの **band** が出る。未クリックの ID には数字を付けない。
- **Why fit:** n8n + Sheets + メール/PDF は、公式コネクタと失敗時人手再実行という Wave 2 提案文の形。Twitter/X は **公式 API + レート制限**だけ。
- **Draft angle:** 請求・初期構築なら「JSON エクスポート + README + 送信は下書きまで」。ループ/レート制限は API ドキュメント準拠。スクレイピングしない。**ID 確定後に Wave 2 の n8n テンプレをローカルで埋める。この PR からは送らない。**

---

## 4. JP-LAN-AIAGENT — Lancers AI エージェント category

- **URL:** https://www.lancers.jp/work/search/system/ai_agent
- **Status:** `read_search`. FAQ BOT+LINE/Gmail 一元管理などのカード。多くは当選済み/終了。
- **Pay:** カード band のみ（例: 200,000〜300,000 円 on one **ended** card — do not reuse as a live bid).
- **Why fit:** FAQ → AI 下書き → 人が送る、は CLI の「公開スイッチは人」と同じ思想。
- **Skip on this page:** 「AIが画面を認識しながらブラウザを操作」不動産ポータル入力（カテゴリ内カード）。Playwright UI 操作は拒否。
- **Draft angle:** 下書きまで。自動送信しない。出典のない回答は未確定。**開いている ID だけ。送らない。**

---

## 5. JP-LAN-YT — Lancers `keyword=YouTube`

- **URL:** https://www.lancers.jp/work/search?keyword=YouTube
- **Status:** `read_search`. このページの先頭は **動画編集・台本・ナレ** が多い（1本3,000円台本、縦型編集など）。API 構築は稀。
- **Pay:** カード band のみ。編集単価を「API 案件の相場」にしない。
- **Why fit:** 薄い。編集そのものは非コア。同じ検索で **公式 API / n8n / GAS** がタイトルに入った行だけ残す。
- **Draft angle:** 編集案件は原則スキップ。API 投稿が出たら「自作ファイル + Data API + 非公開デフォルト + コメント自動は対象外」。**送らない。**

---

## 6. JP-CW-N8N — CrowdWorks n8n search

- **URL:** https://crowdworks.jp/public/jobs?search%5Bkeywords%5D=n8n
- **Status:** **`needs_check`**. Fetch はタイトルのみでカード無し（ログイン/JS の可能性）。
- **Pay:** —
- **Why fit:** 過去に公開ジョブ 12757544 / 12911355 が n8n+Dify だった（今は CLOSED.md）。同キーワードは再掲されやすい。
- **Draft angle:** ブラウザで **募集中** だけ開く。非公開ページに応募しない。角度は「n8n 公式ノード / Webhook / 失敗通知 / 鍵は依頼者」。**送らない。**

---

## 7. JP-CW-YTAPI — CrowdWorks YouTube API / Dify

- **URLs:**  
  https://crowdworks.jp/public/jobs?search%5Bkeywords%5D=YouTube+API  
  https://crowdworks.jp/public/jobs?search%5Bkeywords%5D=Dify
- **Status:** **`needs_check`** (same thin HTML). Search index still has closed IDs (13444091 Data API Excel ツール — 非公開).
- **Pay:** —
- **Why fit:** Data API で title/views を Excel に出す仕事は、公開 CLI の API 面と直結（upload ではなく list）。Dify は RAG/ノード。
- **Draft angle:** クォータと API キーは依頼者プロジェクト。スクレイピング代替を提案しない。Playwright 投稿案件は分割して API 部分だけ。**送らない。**

---

## 8. JP-COCO-REQ232 — Coconala システム開発 依頼

- **URL:** https://coconala.com/requests/categories/232
- **Status:** `read_search`. 2026-09-16 前後まで残るカードあり（例: マークテック 5239457 は **既に終了** — CLOSED.md）。ダンススタジオのシート集計、GAS 予約ページ遷移、Cursor 小規模開発などが **同じ一覧に混在**。個別 URL はこの HTML に ID が無い行が多い → タイトル検索で開く。
- **Pay:** カードによる。マークテックは 30,000円だったが **closed**。生きている行の数字だけ使う。
- **Why fit:** GAS / Sheets / GitHub / Claude Code 歓迎の小規模はオペレータの道具と近い。
- **Skip:** 問い合わせフォーム一括自動送信、TikTok Shop 自動購入（規約・害）。このカテゴリに両方あった。
- **Draft angle:** 公式 API と人が確認する公開。フォーム爆撃は請けない。**開いている request URL を SCOREBOARD 外のローカル台帳に書く。git に実名を足さない。送らない。**

---

## 9. JP-COCO-N8N-KW — Coconala catalog `n8n`

- **URL:** https://coconala.com/search?keyword=n8n
- **Status:** `catalog_read`. カード例: 「n8nで小さな自動化を1本」「見積PDF」「経費レシート」「VPS 上の n8n」「Threads 公式 API」。
- **Pay:** 出品者表示価格（9,500円〜など）。**応募額ではない。GMV ではない。**
- **Why fit:** 日本語の買い手が今検索している言葉。JOBS ではなく **出品キーワード**（別パック）。ここからの「apply」は見積り相談の受信。
- **Draft angle:** 売らない。キーワード控え: `n8n 1本`, `公式API`, `送信は人`, `JSON納品`. **この PR から出品しない。**

---

## 10. JP-COCO-4268304 — competitor gig (YouTube Data API)

- **URL:** https://coconala.com/services/4268304
- **Status:** `catalog_read`.
- **Pay:** 出品文「通常50,000円 / 実績公開協力で30,000円」。**seller list, not our bid.**
- **Why fit:** 文言がほぼコア: 台本・VOICEVOX・字幕・**YouTube Data API 予約投稿**・品質確認。競合の言い方を知るため。
- **Draft angle:** 自分が出すなら「パスワード不要 / 鍵は購入者 / 非公開テスト / コメント自動なし」。**出品・応募しない（catalog）。**

---

## 11. JP-COCO-4268246 — competitor gig (n8n drop-folder)

- **URL:** https://coconala.com/services/4268246
- **Status:** `catalog_read`.
- **Pay:** ページに 20,000円オプション帯。seller list.
- **Why fit:** 「フォルダに mp4 → 自動投稿」は公開 CLI の使い方そのもの（n8n ベースと書いてある）。
- **Draft angle:** ローカル起動・OAuth 一度・ゲート。ブラウザ操作しない、と差別化。**出品しない。**

---

## 12. EN-UW-OPENCLAW — Upwork n8n / OpenClaw / social

- **URL:** https://www.upwork.com/freelance-jobs/apply/Automation-Engineer-n8n-OpenClaw-Agents-Social-Media-Automation_~022036758903426954516/
- **Status:** Search snippet **read** (stack: n8n, OpenClaw, Claude/Gemini, Runway, ElevenLabs, FFmpeg, Meta Graph, LinkedIn API, Sheets, Hetzner/Docker). Full page fetch **timed out** → **`needs_check`** (still open?).
- **Pay:** Title metadata said more than 30 hrs/week, more than 6 months. **No dollar amount in the snippet used here.** Do not invent.
- **Why fit:** n8n + official publish APIs + logging. Overlap with CLI discipline (OAuth, quotas).
- **Out:** Scope is huge (Runway, D-ID, Canva…). Do not claim all of it. Meta/LinkedIn APIs are not the YouTube CLI.
- **Draft angle:** Open with what you **will** do: n8n pipeline Telegram→generate→**official API publish**→Sheet log; fail closed; client holds keys. Name out: unaudited public YouTube via API, browser posting, engagement bots. Cover letter from EN proposal pack **after** live recheck. **Do not send from here.**

---

## 13. EN-UW-HERMES — Upwork Hermes / X / LinkedIn

- **URL:** https://www.upwork.com/freelance-jobs/apply/Expert-needed-Deploy-Hermes-Agent-Nous-Research-VPS-for-Automated-LinkedIn-Posting_~022046505514799669205/
- **Status:** snippet `read`; full page **`needs_check`**.
- **Pay:** Title/snippet **$300.00 Fixed Price** (listing, not GMV). Posted date in SERP: April 21, 2026 — **may be stale**. Recheck open.
- **Why fit:** VPS, Docker, OAuth, SOP, dummy keys then client `.env` — same security story as the CLI keystore.
- **Out:** “Scrape news” if it means ToS-breaking crawl; prefer documented RSS/API. Start word “NVIDIA” is on the snippet — only use if the live page still says so.
- **Draft angle:** Official X/LinkedIn APIs, sandbox accounts, SOP for key handoff, no password sharing. **Do not send until open.**

---

## 14. EN-UW-CRM — Zapier/Make CRM, n8n nice-to-have

- **URL:** https://www.upwork.com/freelance-jobs/apply/CRM-Automation-Specialist-Zapier-Make-HubSpot-Zoho-Real-Workflow-Builds_~022038133362948951578/
- **Status:** snippet `read`; page **`needs_check`**.
- **Pay:** `pay_not_on_snippet`.
- **Why fit:** Hands-on workflows, webhooks, n8n listed as nice-to-have. Paid test of 1–2 flows.
- **Stretch:** HubSpot/Zoho admin is not the YouTube CLI. Only if human wants iPaaS work.
- **Draft angle:** One real workflow (form→sheet→notify, send stays human). Tools honestly listed. No income claims. **Do not send.**

---

## 15. EN-UW-DOCS — Zapier/Make document + e-sign

- **URL:** https://www.upwork.com/freelance-jobs/apply/Zapier-Make-Automation-Specialist-CRM-Project-Management-Document-Workflow-Integration_~022036552586123938781/
- **Status:** snippet `read`; page **`needs_check`**.
- **Pay:** snippet asks for a fixed-price proposal — **no number to copy**.
- **Why fit:** REST when native Zapier is thin — same as “official API or don’t”.
- **Draft angle:** API/webhook path; no browser RPA. Similar past workflow in one paragraph, no fake metrics. **Do not send.**

---

## 16. EN-UW-N8N-BOARD — Upwork n8n jobs index

- **URL:** https://www.upwork.com/freelance-jobs/n8n/
- **Status:** **`needs_check`** (timeout this scan).
- **Pay:** —
- **Why fit:** Canonical EN bid desk for the same JP n8n keywords.
- **Draft angle:** Open in a browser; pick jobs that name **official APIs**. Skip growth-hacking. **Do not send from an unread index.**

---

## 17. EN-FV-N8N-YT — Fiverr search (keyword)

- **URL:** https://www.fiverr.com/search/gigs?query=n8n%20youtube%20automation
- **Status:** **`needs_check`**. PX challenge `ERRCODE PXCR10002539`.
- **Pay:** —
- **Why fit:** EN catalog demand language for n8n + YouTube. Apply path on Fiverr is **buyer request** (login) or **your own gig** (other packs).
- **Draft angle:** Do not bid on someone else’s gig. Use keywords for a later Fiverr draft. **No publish from this PR.**

---

## 18. EN-FV-JBENJAMIN — indexed Fiverr gig (keyword)

- **URL:** https://www.fiverr.com/j_benjamin1/build-n8n-youtube-automation-ai-video-workflow-faceless-channel-n8n-ai-agent
- **Also indexed:** https://www.fiverr.com/gigpilot_33/setup-youtube-automation-using-make-com-n8n-veo3-n8n-automation-made-com · https://www.fiverr.com/orichaagency/automate-n8n-posting-youtube-videos-to-multiple-social-media-yt-n8n-automation
- **Status:** SERP copy `read`; live gig page **PX `needs_check`**.
- **Pay:** competitor packages in SERP — **not our price**. Do not invent USD.
- **Why fit:** Titles cluster on n8n + YouTube upload + AI agent. Shows what EN buyers type.
- **Draft angle:** Mirror **API upload + human QA**, drop “guaranteed passive income”. **Do not apply to a seller gig; do not publish.**

---

## 19. EN-CONTRA-KAJABI — Contra opportunity (apply)

- **URL:** https://contra.com/opportunity/UBkkYMmW-kajabi-portal-and-automation-developer-needed
- **Status:** `open_read` via public JobPosting JSON (`directApply: true`, datePosted 2025-08-18 — **age `needs_check` for still hiring**).
- **Pay:** `pay_not_on_page` (asks applicant to name rates).
- **Why fit:** Email/funnel automation, remote. Weak vs YouTube CLI — only if human wants Kajabi.
- **Draft angle:** Honest: Kajabi is not the public repo. Offer API-ish automation + docs, or **skip**. No rate in git. **Do not send.**

---

## 20. EN-CONTRA-YT-N8N — Contra project (keyword)

- **URL:** https://contra.com/p/ZBRmocol-youtube-automation
- **Related:** https://contra.com/p/oLr7bOEv-viral-ai-video-creation-and-distribution-or-veo-3-n8n-automation
- **Status:** `catalog_read` (independent’s project, not a job post).
- **Pay:** `pay_not_on_page`.
- **Why fit:** n8n + YouTube Data API + Sheets — same nouns as the CLI. Use as **EN keyword / portfolio language**, not apply.
- **Draft angle:** For a Contra profile later: “aggregation / official API / no scrape”. **Do not apply to a portfolio page.**

---

## Click-time `needs_check` (do these first)

1. CrowdWorks keyword HTML in a logged-out browser (rows 6–7).
2. Lancers n8n/ai_agent: open only rows that are **not** 募集終了 (row 3–5).
3. Upwork apply URLs 12–16 (timeout/JS this scan).
4. Fiverr search/gigs (PX).
5. Contra Kajabi opportunity still accepting? (datePosted 2025-08-18).
6. Coconala 5258870 / 5259006 still あと N 日? (were open this fetch).

## Apply later (human)

1. Recheck URL. If closed, stop.
2. Pick **one** angle. Fill `{{PRICE_*}}` / `{{LEAD_TIME_DRAFT}}` only on the local machine.
3. Use JP/EN proposal packs if the desk matches. **Do not send from this PR.**
