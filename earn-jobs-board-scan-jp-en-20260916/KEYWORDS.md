# KEYWORDS — JP+EN jobs scan (2026-09-16)

Public search strings and **login-free browse URLs**.  
Do not treat result **counts** as inventory. Boards paginate and hide closed jobs behind filters.

**DRAFT_ONLY.** Strings are for a human search box, not for a scraper.

---

## JP — CrowdWorks (bid)

Browse (this scan: listing HTML was thin / login-shaped → job cards **`needs_check`**):

- https://crowdworks.jp/public/jobs?search%5Bkeywords%5D=n8n
- https://crowdworks.jp/public/jobs?search%5Bkeywords%5D=Dify
- https://crowdworks.jp/public/jobs?search%5Bkeywords%5D=YouTube+API
- https://crowdworks.jp/public/jobs?search%5Bkeywords%5D=GAS+自動化
- Intended category (errored on a prior earn-ops scan): https://crowdworks.jp/public/jobs/search?category_id=311

**Keywords:** `n8n`, `Dify`, `Make`, `GAS`, `YouTube Data API`, `TikTok API`, `自動化`, `ワークフロー`, `Python`.

**Skip tokens (do not chase as this operator):** `PlaywrightでSNS投稿`, `コメント欄自動`, `いいね自動化`, `スクレイピングで切り抜き転載`.

---

## JP — Lancers (bid)

Public search/category (cards **read** this scan; many rows were already 募集終了):

- https://www.lancers.jp/work/search?keyword=n8n
- https://www.lancers.jp/work/search/system/ai_agent
- https://www.lancers.jp/work/search?keyword=YouTube
- https://www.lancers.jp/work/search?keyword=Dify
- https://www.lancers.jp/work/search?keyword=GAS

**Keywords:** `n8n`, `AIエージェント`, `Dify`, `GAS`, `請求書自動化`, `初期構築`, `YouTube Data API`, `Google Sheets`, `公式API`.

**Skip:** `Playwright`, `UI自動操作でポータル入力` (Lancers AI-agent category had a WordPress→不動産ポータル **browser-agent** card — out of scope).

---

## JP — Coconala (request = apply; service = catalog keyword)

Requests (apply):

- https://coconala.com/requests/categories/232 (システム開発・制作 — live cards **read**)
- https://coconala.com/requests/categories/28 (生成AI)
- https://coconala.com/requests/categories/779 (その他 AI)

Catalog keyword (not a bid; demand language):

- https://coconala.com/search?keyword=n8n (**read**)
- https://coconala.com/search?keyword=Dify
- https://coconala.com/search?keyword=YouTube+自動化

**Keywords:** `n8n`, `Dify`, `GAS`, `YouTube Data API`, `予約投稿`, `VOICEVOX`, `Python`, `見積り相談`.

---

## EN — Upwork (bid)

Public apply URLs are `/freelance-jobs/apply/...`. Hire/search UI is often JS-gated.

- https://www.upwork.com/freelance-jobs/n8n/ (**`needs_check`** — timeout)
- https://www.upwork.com/freelance-jobs/scripting/ (**`needs_check`** — JS wait)
- https://www.upwork.com/hire/n8n-experts/ (**`needs_check`** — prior scan JS)

**Keywords:** `n8n`, `YouTube Data API`, `self-hosted n8n`, `OpenClaw`, `AI agent`, `Google Sheets API`, `OAuth`, `workflow specialist`.

**Skip:** `TikTok Shop ads manager`, `engagement growth`, `scrape and repost`.

---

## EN — Fiverr (catalog keyword; buyer-request apply is login)

Search/gig pages this scan: **PX JS challenge** (`ERRCODE PXCR…`) → treat live inventory as **`needs_check`**. Titles below come from **search-indexed** public gig URLs.

- https://www.fiverr.com/search/gigs?query=n8n%20youtube%20automation
- https://www.fiverr.com/search/gigs?query=n8n%20ai%20agent
- Indexed examples (not this operator’s gigs):  
  https://www.fiverr.com/j_benjamin1/build-n8n-youtube-automation-ai-video-workflow-faceless-channel-n8n-ai-agent  
  https://www.fiverr.com/gigpilot_33/setup-youtube-automation-using-make-com-n8n-veo3-n8n-automation-made-com  
  https://www.fiverr.com/orichaagency/automate-n8n-posting-youtube-videos-to-multiple-social-media-yt-n8n-automation

**Keywords:** `n8n youtube automation`, `youtube data api upload`, `n8n ai agent`, `faceless channel workflow`, `I will build n8n`.

Buyer requests UI: **`needs_check`** (signup). Do not invent request IDs.

---

## EN — Contra (opportunity = apply; project = catalog keyword)

- Opportunities (apply): https://contra.com/opportunity/UBkkYMmW-kajabi-portal-and-automation-developer-needed
- Keyword/portfolio (not a bid):  
  https://contra.com/p/ZBRmocol-youtube-automation  
  https://contra.com/p/oLr7bOEv-viral-ai-video-creation-and-distribution-or-veo-3-n8n-automation  
  https://contra.com/community/t2uCkTki-build-robust-ai-chat-agents-with (prior earn-ops scan)

**Keywords:** `n8n`, `YouTube Data API`, `automation`, `AI agent`, `Google Sheets`.

---

## Pairings (how to search, not a promise)

| If the card says… | Search with… | Angle hinge |
|---|---|---|
| YouTube/TikTok 自動投稿 + Playwright | `公式API` `YouTube Data API` `Content Posting API` | Split: API upload yes; browser/comments no |
| n8n + Sheets + notify | `n8n` `Google Sheets` `Webhook` | Fail-closed send; human approval |
| Dify / RAG bot | `Dify` `RAG` `出典` | Draft answers; no auto-send |
| Fiverr “faceless YouTube” | `youtube data api` `n8n` | Catalog keyword only until buyer request is visible |
