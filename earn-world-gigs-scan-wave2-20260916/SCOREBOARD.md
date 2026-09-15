# SCOREBOARD — world gigs scan wave2 (2026-09-16)

Public-web scan only. **No signup. No secrets. No invented GMV.**

Scan date: 2026-09-15 UTC (folder date 2026-09-16, same GO wave as other earn-ops packs).  
Scope: JP + EN freelance boards, **AI-agent / automation** opportunity patterns (board + gig type + keywords).  
This is a **pattern map**, not a revenue forecast. Listing prices below are **seller- or buyer-stated on the cited page**, not market GMV.

## How to read this file

| Field | Meaning |
|---|---|
| `read` | This agent retrieved listing/category copy from a public URL this scan. |
| `needs_check` | URL is public (search index or known desk), but this agent did **not** fully read the live page (JS challenge, timeout, empty/error body, or login wall). Recheck in a browser before treating inventory as current. |
| Fit | Qualitative only: catalog-buy vs bid-job vs staffing vs mentor/hourly. **Not a money rank.** |

Hard rules carried from earn-ops queue:

- Do not invent job counts, take rates, or GMV.
- Partner directories (Zapier / Make / n8n Experts) stay **LATE** — directory browse is allowed; applications are not.
- SOKUDAN / Workship n8n RPA cards can be **on-site / 準委任**. Flag before treating as remote gig work.

---

## Scoreboard (30 patterns)

| # | ID | Market | Board | Gig type (what buyers ask for) | Status | Fit |
|---|---|---|---|---|---|---|
| 1 | EN-UW-N8N | EN | Upwork | n8n workflow + AI agent (self-host, CRM, content pipeline) | `read` (specific jobs) / hire UI `needs_check` | Bid / contract |
| 2 | EN-UW-CHAT | EN | Upwork | AI chatbot / RAG / voice agent (Vapi, Retell, Twilio) | `read` (hire page snippets) | Bid / contract |
| 3 | EN-FV-N8N | EN | Fiverr | Packaged “I will build n8n AI agent / workflow” gigs | `read` (gig + cost-guide pages) | Catalog gig |
| 4 | EN-FV-AICODING | EN | Fiverr | LangChain / custom GPTs / AI integrations / OpenClaw setup | `read` (category pages) | Catalog gig |
| 5 | EN-FV-CHAT | EN | Fiverr | AI chatbot + calling agent + n8n automation combo gigs | `read` (category page) | Catalog gig |
| 6 | EN-FL-N8N | EN | Freelancer.com | n8n WhatsApp/Instagram setter, CRM, pet-clinic workflows | `read` | Bid job |
| 7 | EN-FL-AGENTS | EN | Freelancer.com | AI Agents / AI Development (voice + WhatsApp MVPs) | `read` | Bid job |
| 8 | EN-CONTRA | EN | Contra | Portfolio/catalog: production n8n + Anthropic chat agents | `read` | Independent catalog |
| 9 | EN-PPH-HOURIE | EN | PeoplePerHour | Hourlie: n8n AI agent / workflow / API (node-count tiers) | `read` | Catalog offer |
| 10 | EN-PPH-JOB | EN | PeoplePerHour | Project post: “AI Agent N8N” for design/art-working | `read` | Bid job |
| 11 | EN-MALT | EN/EU | Malt | Profile positioning: n8n + Make + AI agents + RAG | `read` (profiles) | Profile inbound |
| 12 | EN-KWORK | EN | Kwork | Catalog: n8n/Make/Zapier + OpenAI; autonomous n8n agents | `read` (gig titles) | Catalog gig |
| 13 | EN-LI-SVC | EN | LinkedIn Services | No-code stack listed on seller cards (n8n, Make, Zapier) | `read` (one regional page) | Services listing |
| 14 | EN-GURU | EN | Guru.com | n8n / AI automation jobs browse | **`needs_check`** (fetch timeout) | Bid job |
| 15 | EN-N8N-EXPERTS | EN | n8n.io | Experts Partner waitlist (agency SI; closed pilot) | `read` | **LATE** partner |
| 16 | JP-LAN-CAT | JP | Lancers | Category「AI自動化・エージェント開発」 | `read` | Bid project |
| 17 | JP-LAN-N8N | JP | Lancers | Keyword `n8n`: 請求自動化, 初期構築, Sheets+Gemini, X API | `read` | Bid project |
| 18 | JP-LAN-CS | JP | Lancers | EC FAQ BOT + AI BOT + LINE/Gmail 一元管理 | `read` | Bid project |
| 19 | JP-LAN-GAS-LINE | JP | Lancers | Catalog menu: GAS × LINE BOT 業務システム | `read` | Catalog menu |
| 20 | JP-LAN-KINTONE | JP | Lancers | kintone × AI 転記/OCR; kintone × Power Automate | `read` | Catalog menu |
| 21 | JP-CW-N8NDIFY | JP | CrowdWorks | n8n / Dify 構築パートナー（GWS, Slack, RAG bot） | `read` (job cards) | Bid job |
| 22 | JP-CW-DIFY | JP | CrowdWorks | Dify ノード/ワークフロー開発（文字起こし・資料生成） | `read` (job cards) | Bid job |
| 23 | JP-COCO-N8N | JP | Coconala | Packaged n8n: 1本自動化, 見積PDF, 経費, サーバー構築 | `read` (search) | Catalog gig |
| 24 | JP-COCO-DIFY | JP | Coconala | Dify chatbot / RAG / レッスン / セルフホスト | `read` (search) | Catalog gig |
| 25 | JP-COCO-LINE | JP | Coconala | Dify×Make/GAS LINE Bot; AI LINE 常時対応 | `read` (search) | Catalog gig |
| 26 | JP-MENTA | JP | MENTA | Mentor plans: n8n / Dify 伴走, Claude Code, RAG | `read` (plan pages) | Mentor / retainer |
| 27 | JP-SOKU | JP | SOKUDAN | n8n RPA内製化; Claude Code AIエージェント FDE | `read` | Staffing (**onsite risk**) |
| 28 | JP-WS | JP | Workship | Same n8n RPA 内製化 card syndicated | `read` | Staffing (**onsite risk**) |
| 29 | JP-TT | JP | TimeTicket | Hourly AI導入相談 (tags include Dify / AIエージェント) | `read` (category) | Hourly ticket |
| 30 | JP-AICW | JP | AI CrowdWorks | AI特化マッチング（ノーコード自動化・エージェント職種） | `read` (landing) | Matching **seller-entry `needs_check`** |

---

## Pattern notes (concrete, cited)

### 1. EN-UW-N8N — Upwork n8n + AI agent jobs

Public jobs (not the logged-in search UI):

- [AI Automation Engineer (n8n, OpenClaw, AI Agents, Social Media Automation)](https://www.upwork.com/freelance-jobs/apply/Automation-Engineer-n8n-OpenClaw-Agents-Social-Media-Automation_~022036758903426954516/) — n8n + OpenClaw + Claude/Gemini/OpenAI + Telegram trigger + social publish.
- [n8n Workflow Specialist: Automate Content Creation (Self-Hosted)](https://www.upwork.com/freelance-jobs/apply/n8n-Workflow-Specialist-Automate-Content-Creation-Self-Hosted_~021911833256194838039/) listed on [Scripting jobs](https://www.upwork.com/freelance-jobs/scripting/).
- Hire landing (live freelancer inventory **`needs_check`** — JS challenge on fetch): [Best Freelance N8N Experts for Hire](https://www.upwork.com/hire/n8n-experts/).

**Keywords:** `n8n`, `AI agent`, `OpenClaw`, `self-hosted`, `OpenAI API`, `workflow specialist`.

### 2. EN-UW-CHAT — Upwork chatbot / voice / RAG

- [Best Freelance Chatbot Developers for Hire](https://www.upwork.com/hire/chatbot-developers/) — seller copy names RAG, LangChain, n8n, CrewAI, **VAPI / SynthFlow / Twilio** voice, appointment agents, CRM automation.
- Live search counts on that hire page: **`needs_check`**.

**Keywords:** `AI receptionist`, `Vapi`, `Retell`, `RAG chatbot`, `lead qualification agent`.

### 3. EN-FV-N8N — Fiverr packaged n8n agents

Gig titles observed on public pages:

- [Build n8n automations and ai agents that actually work](https://www.fiverr.com/crissenpai/create-advanced-ai-automation-agents-and-workflows-using-n8n) — flow + error/retry + RAG/Vapi tiers (prices are **that seller’s**, not GMV).
- [Build n8n ai automation workflows and custom ai agents](https://www.fiverr.com/arkstudio2k3/build-n8n-ai-automation-workflows-and-custom-ai-agents-for-your-business)
- Fiverr’s own cost guide listing dozens of “n8n ai agent / zapier / make” gig titles: [AI Automation Experts Cost Guide](https://www.fiverr.com/resources/guides/costs/ai-automation-experts)

Category hub fetch was challenged (`ERRCODE PXCR…`). Treat `/categories/...` inventory as **`needs_check`** at click-time even though search returned titles.

**Keywords:** `I will build n8n ai agent`, `n8n workflow`, `ai automation expert`.

### 4. EN-FV-AICODING — Fiverr AI coding categories

Public category URLs (titles visible in search):

- [Langchain Development](https://www.fiverr.com/categories/programming-tech/buy/ai-coding/langchain) — includes “I will build ai agents, ai automations and ai workflows using n8n”.
- [Custom GPT Apps](https://www.fiverr.com/categories/programming-tech/ai-coding/custom-gpts)
- [AI Integrations](https://www.fiverr.com/categories/programming-tech/ai-coding/ai-integrations) — n8n/Zapier/GHL; “I will setup openclaw on cloud or local”.
- Parent: [AI coding and development](https://www.fiverr.com/categories/programming-tech/ai-coding)

**Keywords:** `langchain`, `custom gpt`, `openclaw`, `ai integrations`, `crewai`.

### 5. EN-FV-CHAT — Fiverr AI chatbot development

- [AI chatbot development services](https://www.fiverr.com/categories/programming-tech/chatbots/ai-chatbot-development) — gig copy pairs chatbot + calling agent + RAG + n8n.

**Keywords:** `ai chatbot`, `calling agent`, `rag`, `n8n automation`.

### 6. EN-FL-N8N — Freelancer.com n8n skill board

- [n8n Jobs](https://www.freelancer.com/jobs/n8n/) — WhatsApp AI agent in n8n; Instagram+WhatsApp setter; pet-clinic workflow; n8n/Make CRM + Claude.

**Keywords:** `n8n WhatsApp agent`, `Wati`, `Evolution API`, `lead qualification`, `Make`.

### 7. EN-FL-AGENTS — Freelancer.com AI Agents / AI Development

- [AI Agents Jobs](https://www.freelancer.com/jobs/ai-agents/0)
- [AI Development Jobs](https://www.freelancer.com/jobs/ai-development) — AI Voice + WhatsApp MVP; n8n + Azure OpenAI agents.

**Keywords:** `ai agents`, `voice agent`, `WhatsApp Business API`, `n8n`, `Azure OpenAI`.

### 8. EN-CONTRA — Contra independent catalog

- [Build Robust AI Chat Agents with n8n & Anthropic API Solutions](https://contra.com/community/t2uCkTki-build-robust-ai-chat-agents-with) — webhook → history → Anthropic → CRM upsert; production stack names JWT, Pinecone, HubSpot, Slack.

**Keywords:** `n8n`, `Anthropic`, `AI chat agent`, `HubSpot`, `Pinecone`.

### 9–10. EN-PPH — PeoplePerHour Hourlie + job

- Hourlie: [Build n8n ai agent, n8n workflow, automation, API integration](https://www.peopleperhour.com/hourlie/build-n8n-ai-agent-n8n-workflow-automation-api-integration/1067325) — node-count packages (seller-stated starter £90; not GMV).
- Job: [N8n Automation Tool](https://www.peopleperhour.com/freelance-jobs/design/graphic-design/n8n-automation-tool-4450043)
- Generic `/freelance-jobs?q=n8n` first page this scan showed **unrelated** jobs (video, ads). Treat unfiltered PPH browse as **`needs_check`** for n8n density.

**Keywords:** `n8n ai agent`, `workflow`, `API integration`, Hourlie vs project post.

### 11. EN-MALT — Malt EN/EU profiles

Public profiles using the same offer language as EN boards:

- [András Iványi — n8n, Make, AI Agents](https://www.malt.com/profile/andrasivanyi)
- [Ludwig W. — Workflows n8n, AI Agents](https://www.malt.com/profile/ludwigwourms)
- [Juri Gorskiy — AI Automation & n8n Expert](https://www.malt.com/profile/jurigorskiy)

**Keywords (profile/skills):** `n8n`, `Make`, `Zapier`, `AI agents`, `RAG`, `agentic workflows`.

### 12. EN-KWORK — Kwork catalog

- [I will build AI automation with n8n, Make, Zapier and OpenAI API](https://kwork.com/scripting/54334545/i-will-build-ai-automation-with-n8n-make-zapier-and-openai-api)
- [I will build autonomous AI agents and business automations in n8n](https://kwork.com/scripting/54356608/i-will-build-autonomous-ai-agents-and-business-automations-in-n8n)

Prices on those titles are **seller list prices**, not GMV. Category index **`needs_check`**.

### 13. EN-LI-SVC — LinkedIn Services

- Example regional browse: [Software Developers — Princeton NJ](https://www.linkedin.com/services/software-developers/us/princeton-nj) — seller card listed “No-code tools: n8n, Make.com, Google Agentspace, Zapier”.
- Desk URL: [linkedin.com/services](https://www.linkedin.com/services). Global n8n search inside Services: **`needs_check`**.

### 14. EN-GURU — Guru.com **`needs_check`**

Intended public browse: `https://www.guru.com/d/jobs/q/n8n/` — fetch timed out this scan. Do not claim listings.

Desk home: [guru.com](https://www.guru.com/).

### 15. EN-N8N-EXPERTS — n8n Experts Partner (**LATE**)

- [n8n expert partners](https://n8n.io/expert-partners/) — closed pilot; waitlist; regions named UK & Ireland, Northern Europe, North America; “at least three customers actively using n8n”.
- Related: [n8n partners](https://n8n.io/partners/), [affiliates](https://n8n.io/affiliates/) (affiliate ≠ expert partner).

Do not apply from this pack.

### 16–18. JP-LAN — Lancers category + n8n + CS agent

- Category: [AI自動化・エージェント開発](https://www.lancers.jp/work/search/system/ai_agent) (alias [ai_automation](https://www.lancers.jp/work/search/system/ai_automation)).
  - Observed card: **FAQ BOT＋AI BOT＋LINE/Gmail一元管理｜EC問い合わせ自動化** (project band 200,000–300,000 円 on the card — listing, not GMV).
  - Also low-pay “AIコールセンター音声確認” under the same category — **different gig type** (ops labeling, not agent build).
- Keyword search: [lancers.jp/work/search?keyword=n8n](https://www.lancers.jp/work/search?keyword=n8n)
  - **n8nを使った請求書自動化** (100,000–200,000 円 band)
  - **n8n 初期構築・セットアップ（小規模／検証用途）** (10,000–20,000 円 band)
  - **n8nとTwitter APIを活用した自動化ワークフロー**
  - **n8n ワークフロー実装とGoogle Sheets作成** (Cron → Sheets → Gemini → 画像 → Typefully)

**Keywords:** `AIエージェント`, `n8n`, `FAQ BOT`, `LINE`, `請求書自動化`, `初期構築`.

### 19–20. JP-LAN menus — GAS/LINE and kintone

- Tag hub: [自動化](https://www.lancers.jp/menu/tag/%E8%87%AA%E5%8B%95%E5%8C%96)
- [GASでLINEBOTと連携システムを開発します](https://www.lancers.jp/menu/detail/1325595)
- [GASでスプレッドシートとSlack/Gmail/kintoneを自動連携します](https://www.lancers.jp/menu/detail/1323968)
- [kintoneとPower Automateで手間ゼロ運用](https://www.lancers.jp/menu/detail/1300080)
- [kintone×AIで転記・集計・仕分けの手作業をなくします](https://www.lancers.jp/menu/detail/1338813)

**Keywords:** `GAS`, `LINE BOT`, `kintone`, `Power Automate`, `OCR`, `Chatwork`.

### 21–22. JP-CW — CrowdWorks n8n/Dify jobs

Public job URLs (category search UI errored this scan → browse **`needs_check`**):

- [【副業歓迎】AI自動化（n8n / Dify）構築パートナー](https://crowdworks.jp/public/jobs/12757544) — GWS + Slack/Discord + RAG chatbot.
- [【AIワークフロー構築のプロ募集｜n8n, Dify, GAS, Make】](https://crowdworks.jp/public/jobs/12911355)
- [生成AI×業務自動化エンジニア募集](https://crowdworks.jp/public/jobs/12905108) — Claude / Dify / Zapier / Make / n8n / GAS.
- [【月額契約】Dify/GPT-4oを活用したAIワークフロー](https://crowdworks.jp/public/jobs/12518483)
- [[継続案件] Difyのワークフロー開発(一連のノード開発)](https://crowdworks.jp/public/jobs/12660582)

Intended browse: [AI・機械学習 jobs](https://crowdworks.jp/public/jobs/search?category_id=311) returned an error page this scan → **`needs_check`**.

**Keywords:** `n8n`, `Dify`, `GAS`, `Make`, `Zapier`, `RAG`, `GPT-4o Vision`.

### 23–25. JP-COCO — Coconala catalog (n8n / Dify / LINE)

Search pages **read**:

- [coconala.com/search?keyword=n8n](https://coconala.com/search?keyword=n8n) — 1本自動化, 見積PDF, 経費レシート, VPS上の n8n, Threads公式API, LINE予約+GCal.
- [coconala.com/search?keyword=Dify](https://coconala.com/search?keyword=Dify) — Dify導入レッスン, Dify×Make LINE bot, RAG社内ナレッジ, EntraID付きセルフホスト, Gシート連携.
- Example service pages: [Dify×n8nで社内AIエージェント](https://coconala.com/services/4227980), [AIエージェント・MCPサーバー](https://coconala.com/services/3713179), [Difyとn8nを1台のVPSに](https://coconala.com/services/4265835).

**Keywords:** `n8n`, `Dify`, `LINE Bot`, `セルフホスト`, `RAG`, `MCP`, `見積自動化`.

### 26. JP-MENTA — mentor / 伴走 (not a job board)

Plans **read**:

- [n8n / Difyを活用した「AI自動化・業務効率化」伴走サポート](https://menta.work/plan/19730)
- [【n8n × 生成AI】定型業務を自動で回るワークフローにする](https://menta.work/index.php/plan/15588?login_time=within_24_hours)
- [Claude Code・Dify・n8n で生産性を引き上げる継続支援](https://menta.work/plan/20357)
- [AIエージェント/ワークフロー構築サポート](https://menta.work/plan/15815)

**Keywords:** `伴走`, `n8n`, `Dify`, `Claude Code`, `RAG`, `VPS`.

### 27–28. JP-SOKU / JP-WS — staffing (n8n RPA / AI FDE)

- SOKUDAN: [RPA内製化・業務自動化推進プロジェクトでn8n経験者](https://sokudan.work/top/projects/17434) — 月額帯は案件カード記載。**東京都渋谷区・一部リモート・準委任**.
- SOKUDAN: [ClaudeCode・AIエージェントで業務変革を実装](https://sokudan.work/top/projects/19023) — welcome: n8n / Dify / Zapier.
- Workship: [同一タイトルの n8n RPA 案件](https://goworkship.com/portal/cri/job/5669)

Treat as **Wave B staffing**, not Fiverr-style gigs. Do not flatten into “remote n8n gig”.

### 29. JP-TT — TimeTicket hourly AI consult

- Category: [AI/機械学習/ディープラーニング](https://www.timeticket.jp/items/c_6/sc_86/) — sidebar tags include `Dify`, `AIエージェント`, `チャットボット`, `プロンプトエンジニアリング`.
- Example tickets: [ChatGPT、GPT-4の生活、業務導入活用サポート](https://www.timeticket.jp/items/137996/), [AIコンサルティングサービス](https://www.timeticket.jp/items/115764/).
- Dedicated `n8n` ticket search: **`needs_check`** (not isolated this scan).

### 30. JP-AICW — AI CrowdWorks landing

- [ai.crowdworks.jp](https://ai.crowdworks.jp/) lists worker types: ノーコードAI自動化エンジニア（Dify、Make、n8n等）, LLM×業務システム連携（LINE、Slack、Salesforce、Kintone、HubSpot等）, AIエージェント開発者, RAG.
- Company news: [事前登録開始](https://crowdworks.co.jp/news/oo-gssosbypi/), [「マルっとAI」](https://prtimes.jp/main/html/rd/p/000000323.000050142.html).
- **Seller entry path this scan: `needs_check`** (landing is buyer/consult oriented; do not register from this pack).

---

## Nearby desks not in the 30 (still public, not scored)

Do not invent extra patterns. These were seen but not given a scoreboard row:

| Desk | URL | Note |
|---|---|---|
| Craudia seller profile (n8n×Gmail, Dify, multi-agent) | https://www.craudia.com/app/user_detail/McyBHb | Supply-side only; **jobs browse `needs_check`** |
| ビザスク | https://visasq.co.jp/seminar/aiagent0527 | Seminar/spot-consult **demand language**, not a freelance job card |
| Zapier Solution Partners | https://zapier.com/partnerdirectory | **LATE** — not opened this scan (`needs_check`) |
| Make Partners | https://www.make.com/en/partners | **LATE** — `needs_check` |
| Workana / Freelancermap | https://www.workana.com/ / https://www.freelancermap.com/ | Wave B desks; n8n slice **`needs_check`** |

---

## What this scan did **not** do

- No account creation, no Google login, no KYC, no proposals, no gig publish.
- No scraping behind login walls.
- No GMV, TAM, “jobs per week”, or take-rate invention.
- Fiverr/Upwork **category search UIs** were often JS-challenged; titles above come from public gig/job/category URLs that search already indexed.

## Next click-time checks (`needs_check` first)

1. Guru n8n jobs browse (timeout).
2. Upwork `/hire/n8n-experts/` live inventory (JS).
3. Fiverr category pages in a real browser (PX challenge).
4. CrowdWorks `category_id=311` search UI.
5. AI CrowdWorks **worker** signup vs consult-only.
6. Craudia / SkillShift / Workana n8n keyword pages.
7. TimeTicket keyword `n8n` vs AI category only.
