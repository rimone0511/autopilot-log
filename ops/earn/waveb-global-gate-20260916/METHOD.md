# METHOD — public GET only (no marketplace login)

Datetime: **2026-09-15 20:30 UTC / 2026-09-16 05:30 JST**  
UA: ordinary desktop Chrome string. **No login cookies. No OAuth. No account create. No POST.**

Did: GET official public URLs. Record HTTP status, `<title>`, and help/Terms sentences that arrived in the body.  
Did not: marketplace login, Google OAuth, paid checkout, KYC, proposals, applications, inventing job counts or GMV, inventing fee amounts not on a 200 page.

Vendor marketing totals are **not** activity proof.  
WAF is a fact of this environment, not proof the product is dead.  
CSRF tokens and Set-Cookie values were **not** saved.

## PeoplePerHour

| URL | HTTP | Memo |
|---|---|---|
| https://www.peopleperhour.com/ | 200 | Title “Hire Freelancers Online & Find Freelance Work”. Register links. Hourlie URLs in HTML |
| https://www.peopleperhour.com/site/register | 200 | Title “Register with PeoplePerHour.com”. **Continue with GOOGLE** / Facebook / email |
| https://www.peopleperhour.com/site/login | 200 | Continue with GOOGLE; Log In with Facebook; Log In with LinkedIn |
| https://www.peopleperhour.com/freelance-jobs | 200 | Title includes **Sep 2026**. `posted_dt` on **2026-09-15**. Payload card count is not copied as traffic |
| https://www.peopleperhour.com/static/terms | 200 | last modified September 11, 2026. PPH Basic + TopAccess annual non-refundable language |
| https://www.peopleperhour.com/hourlie/ | 301 → 404 | Directory slash is not a catalog |
| https://www.peopleperhour.com/hourlie/be-your-wordpress-ninja-for-30-minutes/304215 | 200 | Sample Hourlie/Offer still serves. Not used as a sales total |
| https://www.peopleperhour.com/pricing | 404 | No public pricing path here |
| https://support.peopleperhour.com/hc/en-us/articles/4408655983633-Freelancer-Application-Process | 403 | Cloudflare “Just a moment…” |
| https://support.peopleperhour.com/hc/en-us/articles/205217517-Posting-Offers | 403 | Cloudflare |

## Workana

| URL | HTTP | Memo |
|---|---|---|
| https://www.workana.com/ | 403 | Cloudflare |
| https://www.workana.com/en/ | 403 | Cloudflare |
| https://www.workana.com/en/signup | 403 | Cloudflare |
| https://www.workana.com/en/signup?type=freelancer | 403 | Cloudflare |
| https://www.workana.com/en/login | 403 | Cloudflare |
| https://www.workana.com/en/jobs | 403 | Job recency unread |
| https://www.workana.com/how-it-works/freelancer | 403 | Cloudflare |
| https://www.workana.com/robots.txt | **200** | `User-agent: *` disallows `/api/` and some login/signup queries. Sitemap declared |
| https://www.workana.com/sitemap_index.xml | 403 | Cloudflare HTML, not XML |
| https://blog.workana.com/ | 403 | Cloudflare |
| https://help.workana.com/hc/en-us | 403 | Cloudflare |
| https://help.workana.com/hc/en-us/articles/360041477394-How-can-I-create-edit-my-worker-profile | 403 | Cloudflare |
| https://help.workana.com/hc/en-us/articles/360041401194-Why-do-we-review-profiles | 403 | Cloudflare |
| https://help.workana.com/hc/en-us/articles/360041359554-My-payment-is-on-Verification-What-is-this | 403 | Cloudflare |

## YOUTRUST

| URL | HTTP | Memo |
|---|---|---|
| https://youtrust.jp/ | 302 → `/lp` 200 | Title `YOUTRUST｜仕事専用SNS` |
| https://youtrust.jp/lp | 200 | Same LP |
| https://youtrust.jp/sign_in | 200 | Title ログイン. SPA shell. Google button not in static HTML |
| https://youtrust.jp/signup | 404 | Title ページが見つかりません |
| https://youtrust.jp/recruitment_posts | 200 | Title 副業・転職のジョブ（募集）一覧. No card dates in HTML |
| https://youtrust.jp/api/recruitment_posts | 401 | JSON error requiring sign in / sign up. Not a listing |
| https://help.youtrust.jp/user/account/create/ | 200 | Mail / Facebook / **Google** / LINE create paths |
| https://help.youtrust.jp/user/message/search-jobs/ | 200 | Jobs public to all users; Web「ジョブ」menu |
| https://help.youtrust.jp/user/post/how-to-post/ | 200 | ジョブは1投稿まで無料（poster side） |
| https://help.youtrust.jp/user/post/manage-applicants/ | 200 | 1アカウント1件無料、掲載30日。複数同時は有料契約 |
| https://help.youtrust.jp/users/post-paid-or-free | 404 | Old path; do not cite as live |

## Gate labels used in this folder

| Label | Meaning |
|---|---|
| `pass` | Public page showed a living surface (recent timestamps). Still **DRAFT_ONLY** |
| `needs_check` | WAF / SPA / missing dates. Do not guess |
| `blocked_paid_plan` | Seller submit appears paid in public Terms. **Do not subscribe** |
