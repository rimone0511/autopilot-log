# METHOD — public GET only (no marketplace login)

Datetime: 2026-09-16  
UA: ordinary desktop browser string. **No login cookies. No OAuth. No account create.**

Did: GET official public URLs. Record HTTP status, visible headings, and help/FAQ text that arrived in HTML.  
Did not: marketplace login, Google OAuth completion, paid checkout, KYC, proposals, applications, inventing job counts or GMV.

Vendor marketing totals (note急上昇ラベル, Braintrust “2M+ members” / “10K+ roles”, Twine “390,000” network, Fastwork “No.1”, 99freelas “144354 projetos concluídos”, カイコク “登録者数 12,000”, Gulp “714 Jobs 876 Projekte”) are **not** activity proof.

WAF is a fact of this environment, not a proof the product is dead.

Catalog: sibling PR#22 records. If this GET disagrees, **the URL opened here is source of truth** for this folder.

| URL | HTTP | Memo |
|---|---|---|
| https://note.com/ | 200 | Title “note ――つくる、つながる、とどける。” Top HTML still carries public `publishAt` in sibling gate (this pack does not recount). |
| https://note.com/signup | 200 | Title “会員登録｜note（ノート）”. Body is SPA (visible text ≈ title only). |
| https://note.com/login | 200 | Buttons: **Googleでログイン**, X, Apple, メールアドレス / note ID. Buttons `disabled` until JS. |
| https://note.com/help | 200 | Title “note活用術”. 有料記事 / 有料マガジン / メンバーシップ / 定期購読の案内. **No fee % in this HTML.** |
| https://www.help-note.com/hc/ja | 403 | Cloudflare “Just a moment…”. Creator fee table **unread**. Do not invent %. |
| https://note.com/guide | 404 | Unused. |
| https://www.usebraintrust.com/ | 200 | Title “Braintrust — AI-Powered Talent Network for Enterprise”. Not braintrust.com eval SaaS. |
| https://www.usebraintrust.com/for-talent | 200 | “$0 fees for talent”. “Keep 100% of your earnings.” “Create Your Profile” then “AI Skills Interview” then “Get Certified” (ID-verified). Join → `app.usebraintrust.com/auth/sign_up/goals`. |
| https://www.usebraintrust.com/jobs | 200 | Role cards e.g. “Senior Full-Stack Engineer $150–200/hr”. Posted dates not shown. Category totals are marketing. |
| https://www.usebraintrust.com/blog | 200 | Sibling: “What Is AI Interview Software? … (2026)” heading date Sep 14, 2026. |
| https://app.usebraintrust.com/auth/sign_up/goals | 200 | SPA shell. Title “Braintrust \| Transforming Hiring with AI Recruiting”. **No Google button in this HTML.** |
| https://app.usebraintrust.com/auth/login | 200 | SPA shell. Title “Braintrust Marketplace Login…”. Google **needs_check**. |
| https://www.usebraintrust.com/site-service-fees-terms | 200 | Freelancer payout: banking info to Stripe or Wise. **STOP — do not fill.** Last updated July 19, 2023. |
| https://www.usebraintrust.com/talent-terms | 200 | Independent contractor terms. Not a fee table. |
| https://www.twine.net/ | 200 | Marketplace LP. |
| https://www.twine.net/jobs | 200 | “Jobs posted directly onto the Twine platform”. Sibling example still the activity proof (Remote, “Posted 4 days ago”). Ari is aggregator — skip. |
| https://www.twine.net/signup | 200 | Title “Sign Up”. Noscript warning. JS state includes `signingUpViaGoogle`. |
| https://www.twine.net/pricing | 200 | Standard **$ 0.00 per month**. “Service fee from 5%” (client hire fee). Business **$ 139.99 per project** — do not buy. |
| https://www.twine.net/blog | 200 | Sibling: “7 Smart Side Hustles…” August 21, 2026. |
| https://help.twine.net/en/ | 200 | Help Center. Freelancer / Client / AI Collectors categories. |
| https://fastwork.co/en | 200 | Title Thailand freelancer marketplace. “Sign up as a freelancer” → `/start-selling`. Copy: “Freelancers verify their identity in the system before hiring begins.” |
| https://fastwork.co/en/ai-automation | 200 | Title “รับทำและออกแบบ AI Automation / n8n / make.com”. Online category. Starting prices on cards are pack floors, not GMV. |
| https://fastwork.co/en/signup | 404 | SPA. Do not treat as dead. |
| https://fastwork.co/en/start-selling | 200 | Title “Join as a Freelancer \| Fastwork.co”. Step 1: “Register with your ID and bank details for verification.” Sign Up button `disabled` in this HTML. |
| https://fastwork.co/en/terms | 200 → static.fastwork.co/contents/terms | Body empty in this GET (~0.9KB). Fee % unread. |
| https://www.99freelas.com.br/ | 200 | Client-facing home. Footer Cadastro de freelancer. Marketing totals ignored. |
| https://www.99freelas.com.br/projects | 200 | Public project headings (Laravel 12 etc. in sibling). `Publicado:` empty in static HTML. |
| https://www.99freelas.com.br/register | 200 | Title “Cadastre-se”. **Eu quero Trabalhar** vs Contratar. |
| https://www.99freelas.com.br/register/freelancer | 403 | Cloudflare. Form unread. |
| https://www.99freelas.com.br/como-funciona | 200 | Cadastro grátis. “taxa de 5% a 20% (R$ 10,00 no mínimo)”. Premium “R$ 54,90 a R$ 89,90 por mês” — do not buy. |
| https://www.99freelas.com.br/termos | 200 | Freelancer: no contact/links in profile; no off-platform pay; do not mention commission in proposals. |
| https://www.gulp.de/ | 200 | Randstad Professional (vormals GULP). GULP Direkt: platform free for companies until hire; **7 Euro Servicegebühr pro Freelancer-Stunde** at Beauftragung (client). Freelancer: “kostenloses Profil”. |
| https://www.gulp.de/registrieren | 200 | Freelancer box “Jetzt kostenlos registrieren” → `/gulp2/g/neu/experten/registrieren`. **No Google OAuth control** in this HTML. |
| https://www.gulp.de/gulp2/g/neu/experten/registrieren | 200 | JS-required (“JavaScript ist in Ihrem Browser deaktiviert”). Form unread. |
| https://www.gulp.de/freelancing/projekte | 200 | Cards with **NEU** and Start ab **01.09.2026** / **14.09.2026** / **02.11.2026**. Several CH cities. Start dates ≠ post dates. |
| https://www.gulp.de/freelancing/gulp-membership | 200 | Basisprofil **kostenlos**. Membership **120 Euro netto / 6 Monate**, **180 Euro netto / 12 Monate**. Do not buy. |
| https://www.shufti.jp/ | 200 → app.shufti.jp/ | SPA shell ~2KB. |
| https://app.shufti.jp/signup | 200 | Shell. Buttons not painted. |
| https://app.shufti.jp/jobs/search | 200 | Shell. Job names unread. |
| https://help.shufti.jp/ | 200 | Knowledge base. |
| https://help.shufti.jp/support/solutions/articles/158000411223-手数料一覧 | 200 | 変更日 2025-11-05. 振込手数料 **330円**, 組戻 **33円**, 最低振込 **363円**. Not a job count. |
| https://kaikoku.blam.co.jp/ | 200 | LP. 「無料登録で案件をみる」. 案件事例 with no dates. Marketing 12,000人 unused. |
| https://app.kaikoku.blam.co.jp/user/register/before | 200 | Title “会員登録前 \| KAIKOKU(カイコク)”. SPA. Google button unread. |
| https://www.twago.com/ | 200 → talent-pool.com | Enterprise Talent Pool. No freelance board. |
| https://www.xing.com/projects | **404** | “404 - Not Found \| XING”. |

Signed URLs, cookies, CSRF, Ray IDs, and third-party OAuth **client IDs / API keys** that appeared in marketplace HTML are **not stored**.

## Gate labels used in this folder

| Label | Meaning |
|---|---|
| `alive` / KEEP | Public page showed a living surface (recent timestamps or a working public catalog). Still **DRAFT_ONLY**. |
| `needs_check` | Listing dates unread (SPA/WAF) or a control (Google button) is unconfirmed. Do not promote to pass by guessing. **NOTES only for Shufti / カイコク.** |
| `dead` / SKIP | Public product surface is gone (Twago → Talent-Pool; Xing Projects 404). |
| `blocked_paid_plan` | Next click is subscribe. **Do not subscribe.** |
| `kyc_wait` | ID / bank / liveness required. **Do not upload.** |

No desk is marked dead from a WAF page.
