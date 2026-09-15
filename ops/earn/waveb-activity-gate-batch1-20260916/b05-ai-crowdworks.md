# B05 — AI CrowdWorks（AIクラウドワークス）

**DRAFT_ONLY.** Logged out. Did not register. Did not apply. No secrets.

This is **not** main CrowdWorks (`crowdworks.jp` job board). Do not copy main-site 5–20% system fees onto this desk.

```
date (JST): 2026-09-16
desk: AI CrowdWorks / AIクラウドワークス
official_url: https://ai.crowdworks.jp/
public_pages_opened: yes
logged_in: no
signup_path: /aicw/register/new_email — CrowdWorks ID or email (register JS). Login JS also lists Google / Yahoo / Facebook. Direct /aicw/auth/google = 404.
fee_notes: Register JS heading「カンタン無料会員登録」. Pre-reg news Q5 (2026.5.14) worker 登録 is 無料. Formal-release news (2026.8.20) has no worker %.
cu_tip: Do not submit the form from this note. Human opens /projects/ in a browser. Do not click 興味がある. Pre-reg is closed.
gate: needs_check
published: no
```

## Official URL

- Product: https://ai.crowdworks.jp/ — 200. Title「AIクラウドワークス - AI特化版人材マッチングプラットフォーム」
- Job list: https://ai.crowdworks.jp/projects/ — 200
- Expert list: https://ai.crowdworks.jp/ai-workers/ — 200
- Worker register: https://crowdworks.jp/aicw/register/new_email — 200
- Login: https://crowdworks.jp/aicw/login — 200, title「ログイン - AIクラウドワークス」
- Formal release news: https://crowdworks.co.jp/news/akdv13x1sf/ — **2026.8.20**
- Pre-reg news: https://crowdworks.co.jp/news/oo-gssosbypi/ — **2026.5.14**
- Pre-reg LP https://ai.crowdworks.jp/lp/pre-registration/ → **redirects to home** (form closed)

Nav on the product origin (this GET): ログイン, 会員登録, 仕事一覧, AI技術者・専門家一覧, 仕事依頼, 無料相談. Client consult is out of scope.

## Public jobs / dates — what this GET actually saw

https://ai.crowdworks.jp/projects/ visible text:

- Heading「仕事一覧」
- 「『興味がある』ボタンを押していただいた会員の方から、優先的に仕事をご案内いたします。」
- **「読み込み中」「読み込み中」**
- **No job titles, no dates**

https://ai.crowdworks.jp/ai-workers/ : same pattern — heading「AI技術者・専門家一覧」then「読み込み中」. No cards.

Home「現在募集中の仕事」block is **category examples** (Claude Code利用支援, Gemini Enterprise構築, 請求書／支払AI自動化, …), not a dated board. Do not treat those bullets as open jobs.

Official news https://crowdworks.co.jp/news/akdv13x1sf/ dated **2026.8.20**: formal release of the service. The same article’s「事前登録10,000名」is a **marketing headcount**. Not used as activity or traffic.

Home also shows「事前登録AI技術者・専門家 10,000名以上」. Same rule: not activity proof.

No public job API (`/api/projects`, `/projects.json`) — 404.

So: the product origin is live and the company published a **2026-08-20** release, but **this GET did not see dated public job cards**. Gate stays `needs_check`. Not `dead` (register URL and news are up). Not `thin` (unread list ≠ empty catalogue).

## Signup path

Curl of `/aicw/register/new_email` and `/aicw/login` printed the site’s noscript / “enable JavaScript” error in this environment. The **public register JS** for that page (asset path `vite/2026-09/1/.../register/new_email.ts-….js`) still loaded. Labels in that file:

- Heading **「カンタン無料会員登録」**
- **「すでにクラウドワークスをご利用の方」** → **「クラウドワークスIDで登録する」**
- **「クラウドワークスIDをお持ちでない方」** → field **「メールアドレス」** + button **「メールアドレスで登録する」**
- Note that after register, main CrowdWorks services may also be available
- Agree to CrowdWorks 利用規約 + 個人情報の取り扱い

**No Google control in the register JS.**

Login JS (`.../aicw/login.ts-….js`):

- Email + password +「ログイン」
- Copy「クラウドワークスのアカウントでログインが可能です。」
- Section **「他のアカウントでログイン」** with `serviceName: "Google"`, `"Yahoo! JAPAN ID"`, `"Facebook"`

Direct https://crowdworks.jp/aicw/auth/google returned **404**. OAuth was **not** completed. Cookie names from that JS are not stored here.

CU: seller entry is **email or existing CrowdWorks ID** on the register URL. Google is listed on **login** JS, not on register JS. Do not start OAuth from an agent. Do not create Yahoo / Facebook for this desk.

## Fee notes (official pages only)

1. Register JS heading: **「カンタン無料会員登録」** (current register surface, asset folder `2026-09/1`).
2. Pre-registration news (2026.5.14) Q5:「『AIクラウドワークス』のワーカー登録に費用はかかりますか？」**「一切かかりません。完全無料です。」** That article’s signup URL is the **closed** pre-reg LP. Cite it as that news page, not as a live form.
3. Formal-release news (2026.8.20): **no worker fee %** in the text this GET read.
4. Home client FAQ「費用はどのくらいかかりますか？」is **client / 依頼** copy (budget / お見積り). Not a worker rate.
5. https://crowdworks.jp/pages/agreement is **main CrowdWorks** TOS (updated 2026年7月14日 in the text). **Do not** copy main-site worker system fees onto AI CrowdWorks unless an AI-CW page states them. This GET did not see that %.

## CU tip

1. Different desk from CrowdWorks CU field maps. Do not paste a CrowdWorks catalog bid here.
2. Do **not** submit `/aicw/register/new_email` from this agent.
3. Human: load https://ai.crowdworks.jp/projects/ in a browser. If cards + dates appear, re-label then. If still「読み込み中」or empty, park.
4. Do not press「興味がある」(member-gated per the list copy).
5. Pre-reg is closed; do not hunt the old LP form.
6. If login offers Google, MAIN Google only — and only after a human decides the board is worth a draft.
7. STOP-KYC. No paid boost.

## Gate

**needs_check**
