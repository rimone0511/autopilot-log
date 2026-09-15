# METHOD — public GET only

Datetime: **2026-09-15 20:41 UTC / 2026-09-16 05:41 JST**  
UA: ordinary desktop Chrome string. **No login cookies. No OAuth. No account create. No POST.**

Did: GET official public URLs. Record HTTP status, `<title>`, and sentences that arrived in the body.  
Did not: marketplace login, Google OAuth, form submit, paid checkout, KYC, proposals, applications, inventing job counts or GMV, inventing fee amounts not on a 200 page.

Vendor marketing totals are **not** activity proof.  
DNS fail / embed-empty is a fact of this environment, not proof the product is dead.  
CSRF tokens, Set-Cookie values, GTM/conversion ids, and signed query strings were **not** saved.

Peraichi CSS `?1789432822` on the DMM LP is a cache-buster, **not** a listing date.

## DMM生成AI人材バンク (this-folder B08)

| URL | HTTP | Note |
|---|---|---|
| https://algoage.co.jp/jinzaibanktouroku | 200 | Title「DMM生成AI人材バンク会員登録ページ」. Peraichi LP. Copyright 2026. No `<input>` in static HTML |
| https://algoage.co.jp/jinzaibanktouroku/ | 200 | Same document as slash-less URL |
| https://algoage.co.jp/ | 404 | Title「お探しのページは見つかりませんでした」. Register path still 200 |
| https://dmm-businessai.com/ | 200 | Title「【DMMビジネスAI】 AIで日々の業務を劇的に効率化」. Client training/engineering. No talent-board cards |
| https://dmm-businessai.com/about-us/ | 200 | 会社名 **株式会社DMMビジネスAI**. デジタル人材の育成実績「10,000名+」= marketing, unused |
| https://dmm-businessai.com/faq/ | 200 | Section「DMM生成AI人材バンクについて」is **依頼者向け**支援Q&A. 「生成AI人材バンクの費用」→ ご支援内容により…初回相談・お見積りは無料 |
| https://dmm-businessai.com/jinzaibank/ | 404 | Path guessed from slug; **not** a live talent board |
| https://dmm-businessai.com/privacy-policy/ | 200 | Joint handling: 株式会社Algoage / 合同会社DMM.com / 株式会社インフラトップ |
| https://generative-ai.web-camp.io/bank/talents/ | DNS fail | Linked from the register LP (`href` present). Host unread here |
| https://generative-ai.web-camp.io/terms/resources/ | DNS fail | TOS href on the register LP. Body unread |
| https://generative-ai.web-camp.io/ | DNS fail | Same host |
| https://www.dmm.com/ | 200 | General DMM portal. **Not** used as talent-bank activity |

`www.dmm.com` was opened once to confirm it is not the seller desk. Do not treat DMM TV/games home as 人材バンク.

## Freelancermap (this-folder B17 / QUEUE B12)

| URL | HTTP | Note |
|---|---|---|
| https://www.freelancermap.com/ | 200 | Title “Freelancer jobs & IT projects worldwide — 0% commission”. Marketing totals on page **ignored** |
| https://www.freelancermap.com/projects | 200 | Title “Freelance Jobs & IT Projects Worldwide”. HTML payload `created` ISO **2026-09-15**. Example titles recorded; payload size is not traffic |
| https://www.freelancermap.com/registration | 200 | Title “Sign up to freelancermap”. Account type: Freelancer/Agency vs Project provider. Google strings = Analytics/GTM/ads conversion, **not** OAuth buttons |
| https://www.freelancermap.com/login | 200 | Email/username + password. “Login link by email”. No Google OAuth button in HTML |
| https://www.freelancermap.com/pricing/freelancer | 200 | Basis **0,00 €**/月; Premium **13,99 €**/月 (Jährlich toggle). Persona verify 50€/75€ per year |
| https://www.freelancermap.com/help.html | 200 | Basic free; Premium from €13.99/month billed annually; no commission fees; apply requires active profile |
| https://www.freelancermap.com/for-freelancer | 200 | Marketing. Same €13.99 / 0% commission copy |
| https://www.freelancermap.com/data-privacy.html | 200 | Privacy page 200. Body not mined for fees |
| https://www.freelancermap.com/blog/freelance-profile-tips-examples/ | 200 | Title includes “(2026)”. Blog, **not** a job-card date |
| https://www.freelancermap.com/robots.txt | 200 | `User-agent: *` Disallow empty. Sitemap declared |
| https://www.freelancermap.com/sitemap.xml | 200 | Sitemap index (profiles + projects locs). Not used as a count |
| https://www.freelancermap.com/projectSearch.json | 404 | Not a public JSON catalog |
| https://www.freelancermap.com/api/projects | 200 → `/login` | Unauthenticated API is not a listing |

## Gate labels used in this folder

| Label | Meaning |
|---|---|
| `pass` | Public page showed a living surface (recent timestamps). Still **DRAFT_ONLY** |
| `needs_check` | Embed/DNS/missing dates. Do not guess |
