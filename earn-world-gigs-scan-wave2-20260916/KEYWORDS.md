# KEYWORDS — world gigs scan wave2 (2026-09-16)

Companion to [SCOREBOARD.md](SCOREBOARD.md). Public-web only. **No signup. No secrets. No invented GMV.**

Use these strings on the **cited public search/category URLs**. If a board requires login to see results, stop and mark `needs_check`. Do not create accounts from this pack.

Status key: `read` = used successfully this scan; `needs_check` = URL known but live results unread or blocked.

---

## EN — buyer / gig-title language

Observed on Upwork jobs, Fiverr gigs/categories, Freelancer.com skill boards, PPH, Malt, Contra, Kwork (see SCOREBOARD citations).

### Core (run first)

| Keyword | Where it hit this scan | Status |
|---|---|---|
| `n8n` | Upwork jobs, Fiverr gigs, Freelancer `/jobs/n8n/`, PPH Hourlie, Malt profiles, Kwork | `read` |
| `n8n ai agent` | Fiverr titles, PPH Hourlie | `read` |
| `AI agent` / `AI agents` | Upwork titles, Freelancer `/jobs/ai-agents` | `read` |
| `ai automation` | Fiverr cost guide titles, Kwork | `read` |
| `workflow automation` | Fiverr, Malt | `read` |

### Orchestration tools

| Keyword | Notes |
|---|---|
| `zapier` | Fiverr “ai automation expert” titles; CrowdWorks JP jobs also use it |
| `make.com` / `Make` | Fiverr, Malt, Kwork, JP Dify×Make LINE bots |
| `OpenClaw` | Upwork job title; Fiverr AI integrations (“setup openclaw”) |
| `pipedream` | Malt profile skills (not a board search this scan) → board hit `needs_check` |

### Agent / LLM stack

| Keyword | Notes |
|---|---|
| `langchain` | Fiverr category `/buy/ai-coding/langchain` |
| `crewai` | Fiverr custom-GPT / chatbot gig copy |
| `custom gpt` / `custom gpts` | Fiverr `/ai-coding/custom-gpts` |
| `RAG` | Upwork chatbot hire copy; Contra; Malt; JP Dify |
| `Anthropic` / `Claude` | Contra production stack; Freelancer CRM+Claude |
| `OpenAI` / `GPT` | Universal |
| `Gemini` | Upwork content-pipeline job; Lancers Sheets+Gemini |
| `MCP` | Coconala MCPサービス; SOKUDAN welcome skills |

### Voice / messaging (EN demand cluster)

| Keyword | Notes |
|---|---|
| `Vapi` / `Retell` / `Twilio` | Upwork chatbot hire seller copy; Fiverr n8n gig FAQs |
| `WhatsApp` / `WhatsApp Business API` | Freelancer n8n + AI Development jobs |
| `Wati` / `Evolution API` | Freelancer n8n job copy |
| `Instagram Messaging API` | Freelancer setter job |
| `voice agent` / `AI receptionist` | Upwork chatbot hire |

### CRM / ops (EN)

`HubSpot` · `GoHighLevel` / `GHL` · `Salesforce` · `Pipedrive` · `Airtable` · `Notion` · `Slack` · `Google Sheets` · `Supabase` · `webhook` · `self-hosted` · `Docker`

### Fiverr title fragments (catalog SEO)

Copy these as **gig-title tokens**, not as traffic claims:

- `I will build n8n ai agent`
- `n8n automation n8n workflow`
- `ai automation expert`
- `zapier make n8n`
- `openclaw setup`
- `rag chatbot`

Source pages: [Fiverr AI automation cost guide](https://www.fiverr.com/resources/guides/costs/ai-automation-experts), [LangChain category](https://www.fiverr.com/categories/programming-tech/buy/ai-coding/langchain), [AI integrations](https://www.fiverr.com/categories/programming-tech/ai-coding/ai-integrations).

---

## JP — 検索語 / 出品語

Observed on Lancers, CrowdWorks, Coconala, MENTA, SOKUDAN, Workship, TimeTicket, AI CrowdWorks landing.

### Core (先にこれを)

| 語 | 当たった机 | Status |
|---|---|---|
| `n8n` | ランサーズ検索, クラウドワークス案件, ココナラ検索, MENTA, SOKUDAN, Workship | `read` |
| `Dify` | クラウドワークス, ココナラ, MENTA, TimeTicketタグ, AIクラウドワークス職種 | `read` |
| `AIエージェント` | ランサーズカテゴリ, ココナラ, TimeTicketタグ, ビザスクセミナー | `read` |
| `AI自動化` | ランサーズ `/system/ai_automation`, クラウドワークス案件タイトル | `read` |
| `業務自動化` | ランサーズメニュータグ, SOKUDAN, ココナラ | `read` |
| `生成AI` | クラウドワークス, SOKUDAN, MENTA | `read` |

### ツール（JPで併記されやすい）

| 語 | 典型パターン |
|---|---|
| `GAS` / `Google Apps Script` | ランサーズメニュー, クラウドワークス歓迎スキル, ココナラ |
| `Make` | クラウドワークス, ココナラ Dify×Make LINE |
| `Zapier` | クラウドワークス歓迎スキル, SOKUDAN歓迎 |
| `Power Automate` | ランサーズ kintone連携メニュー; SOKUDAN RPA |
| `UiPath` | SOKUDAN n8n RPA 案件の併記 |
| `kintone` | ランサーズ GAS/AI メニュー |
| `Claude Code` | MENTA, SOKUDAN FDE |
| `ChatGPT` / `Claude` / `Gemini` | 全JP机 |

### 納品物・業務名（JPカタログ）

| 語 | 机 |
|---|---|
| `LINE BOT` / `LINEbot` / `LINEボット` | ランサーズメニュー, ココナラ, ランサーズEC CS案件 |
| `FAQ BOT` | ランサーズ AIエージェントカテゴリ |
| `RAG` / `社内ナレッジ` / `セルフホスト` | ココナラ Dify, クラウドワークス n8n/Dify |
| `請求書自動化` | ランサーズ n8n |
| `初期構築` / `セットアップ` | ランサーズ n8n; ココナラ VPS |
| `見積` + `PDF` | ココナラ n8n |
| `経費` / `レシート` | ココナラ n8n |
| `伴走` | MENTA, クラウドワークス「パートナー」 |
| `ワークフロー` / `ノード開発` | クラウドワークス Dify |
| `MCP` | ココナラ |
| `OpenClaw` | Workship EVENT（講座。案件ではない） |

### カテゴリ名そのもの（JP）

- ランサーズ: `AI自動化・エージェント開発` · `生成AI・機械学習・ChatGPT` · `業務効率化・RPA・システム開発` · `AIチャットボット開発` · `ChatGPT開発`
- クラウドワークス: `AI・チャットボット開発` · `AI（人工知能）・機械学習`（`category_id=311` の一覧はこのスキャンでエラー → **`needs_check`**）
- タイムチケット: `AI/機械学習/ディープラーニング`（タグ `Dify` `AIエージェント`）
- AIクラウドワークス職種コピー: `ノーコードAI自動化エンジニア（Dify、Make、n8n等）` · `AIエージェント開発者` · `社内データ活用AI（RAG）`

---

## Public search / category URLs (copy-paste)

Do not add login, cookies, or `?token=`. If the page challenges JS, mark `needs_check` and stop.

### EN

| Board | URL | Status |
|---|---|---|
| Upwork n8n hire | https://www.upwork.com/hire/n8n-experts/ | UI `needs_check` |
| Upwork scripting jobs | https://www.upwork.com/freelance-jobs/scripting/ | `read` |
| Upwork chatbot hire | https://www.upwork.com/hire/chatbot-developers/ | `read` (copy) |
| Fiverr LangChain | https://www.fiverr.com/categories/programming-tech/buy/ai-coding/langchain | `read` |
| Fiverr Custom GPTs | https://www.fiverr.com/categories/programming-tech/ai-coding/custom-gpts | `read` |
| Fiverr AI integrations | https://www.fiverr.com/categories/programming-tech/ai-coding/ai-integrations | `read` |
| Fiverr AI chatbot | https://www.fiverr.com/categories/programming-tech/chatbots/ai-chatbot-development | `read` |
| Fiverr AI coding | https://www.fiverr.com/categories/programming-tech/ai-coding | `read` |
| Fiverr AI services hub | https://www.fiverr.com/categories/programming-tech/ai-services | **`needs_check`** (PX challenge) |
| Freelancer n8n | https://www.freelancer.com/jobs/n8n/ | `read` |
| Freelancer AI agents | https://www.freelancer.com/jobs/ai-agents/0 | `read` |
| Freelancer AI development | https://www.freelancer.com/jobs/ai-development | `read` |
| PPH Hourlie n8n | https://www.peopleperhour.com/hourlie/build-n8n-ai-agent-n8n-workflow-automation-api-integration/1067325 | `read` |
| Malt (profile examples) | https://www.malt.com/profile/andrasivanyi | `read` |
| Contra example | https://contra.com/community/t2uCkTki-build-robust-ai-chat-agents-with | `read` |
| Kwork n8n gig | https://kwork.com/scripting/54334545/i-will-build-ai-automation-with-n8n-make-zapier-and-openai-api | `read` |
| LinkedIn Services | https://www.linkedin.com/services | hub `needs_check` |
| Guru n8n jobs | https://www.guru.com/d/jobs/q/n8n/ | **`needs_check`** (timeout) |
| n8n Experts (LATE) | https://n8n.io/expert-partners/ | `read` |

### JP

| Board | URL | Status |
|---|---|---|
| ランサーズ AIエージェント | https://www.lancers.jp/work/search/system/ai_agent | `read` |
| ランサーズ AI自動化 | https://www.lancers.jp/work/search/system/ai_automation | `read` |
| ランサーズ `n8n` | https://www.lancers.jp/work/search?keyword=n8n | `read` |
| ランサーズ 自動化メニュー | https://www.lancers.jp/menu/tag/%E8%87%AA%E5%8B%95%E5%8C%96 | `read` |
| ココナラ `n8n` | https://coconala.com/search?keyword=n8n | `read` |
| ココナラ `Dify` | https://coconala.com/search?keyword=Dify | `read` |
| クラウドワークス例 (n8n/Dify) | https://crowdworks.jp/public/jobs/12757544 | `read` |
| クラウドワークス AIカテゴリ | https://crowdworks.jp/public/jobs/search?category_id=311 | **`needs_check`** |
| MENTA n8n/Dify伴走 | https://menta.work/plan/19730 | `read` |
| SOKUDAN n8n RPA | https://sokudan.work/top/projects/17434 | `read` |
| Workship n8n RPA | https://goworkship.com/portal/cri/job/5669 | `read` |
| TimeTicket AI | https://www.timeticket.jp/items/c_6/sc_86/ | `read` |
| AIクラウドワークス | https://ai.crowdworks.jp/ | `read` (landing) |

Suggested JP queries not isolated this scan → **`needs_check`**:

- ココナラ / ランサーズ: `OpenClaw` · `Vapi` · `CrewAI` · `LangChain`
- タイムチケット: `n8n`
- クラウディア / Skill Shift / 複業クラウド: `n8n` · `Dify` · `AIエージェント`

---

## Pairings that showed up as **one** offer (do not split in titles)

These combinations appeared as a single gig/job, so search/title them together:

| Pairing | Markets |
|---|---|
| n8n + AI agent + error/retry/alerts | EN Fiverr |
| n8n + OpenClaw + social publish | EN Upwork |
| n8n + WhatsApp + lead qualification | EN Freelancer |
| n8n + Anthropic + CRM upsert | EN Contra |
| Dify + n8n + RAG + セルフホスト | JP Coconala / CrowdWorks |
| Dify + Make/GAS + LINE Bot | JP Coconala |
| GAS + LINE + Sheets/kintone | JP Lancers |
| kintone + 生成AI OCR/分類 | JP Lancers |
| n8n + Dify + GAS + Make（one 募集 lists the whole stack） | JP CrowdWorks |
| n8n + Power Automate / UiPath（RPA内製化） | JP SOKUDAN / Workship |

---

## Negative / skip tokens (this studio)

Do not chase these as “AI agent gigs” for earn-ops. They collide with Autopilot Log’s own rules or with thin/ops work:

| Token | Why |
|---|---|
| browser RPA / Selenium-as-the-product / “無人SNS運用” | This repo refuses browser automation and engagement bots |
| Upwork/Fiverr **social posting via unofficial APIs** | Official YouTube/TikTok APIs only in-product; freelance copy that implies scraping is a compliance stop |
| `AIコールセンターの音声確認・データ修正` (Lancers category noise) | Labeling work, not agent build |
| Partner apply: Zapier / Make / n8n Experts | **LATE**; waitlist/directory only |
| SOKUDAN/Workship **週5・出社** | Staffing, not a packaged gig |

---

## Operator search order (no signup)

1. JP catalog: Coconala `n8n` then `Dify` (already dense).
2. JP bid: Lancers `ai_agent` category + keyword `n8n`.
3. JP bid: CrowdWorks individual jobs cited in SCOREBOARD (category UI `needs_check`).
4. EN catalog: Fiverr categories in KEYWORDS table (if PX-blocked, use cited gig URLs only).
5. EN bid: Freelancer `/jobs/n8n/` then `/jobs/ai-agents`.
6. EN bid: Upwork **specific** `/freelance-jobs/apply/...` URLs; do not trust blocked search UI.
7. Mentoring: MENTA plans if catalog/bid is not the desk.
8. Stop before Guru / Workana / Craudia jobs / AI CrowdWorks seller entry until `needs_check` is cleared in a browser.

No GMV column. If a later pass adds counts, they must be **on-page integers** with date + URL, or they stay out.