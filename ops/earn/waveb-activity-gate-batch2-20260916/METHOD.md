# METHOD — public GET only

Datetime: **2026-09-16 JST** (requests ~20:29–20:32 UTC)  
UA: ordinary browser string. No login cookie. No form POST.

Did: GET official public URLs. Record status, titles, visible copy, dates that appeared in HTML.  
Did not: account create, OAuth complete, paid plan, KYC, apply, publish, password input.

Do not treat category counts (例: オンライン「すべてのカテゴリー (37,014)」) or 「約7,400名」「8万人」 as activity proof.  
Fee % only when the official page showed a number. Missing → `needs_check`.

CSRF / `authenticity_token` / OAuth `state` appeared in some HTML. **Not saved here.**

## HTTP (this GET)

| URL | HTTP | Note |
|---|---|---|
| https://www.any-crew.com/ | 200 | Marketing. News teasers. Last-Modified Fri, 11 Sep 2026 |
| https://www.any-crew.com/news | 200 | Media-mention dates through **2026-08-31** |
| https://www.any-crew.com/terms | 200 | 第5条 基本無料。求人事業者の有料プラン |
| https://blog.any-crew.com/ | 200 | 新着記事 **2026.08.26** |
| https://www.any-crew.com/blog | 404 | Blog lives on `blog.any-crew.com` |
| https://app.any-crew.com/ | 200 | Talent app. 「Googleでログイン」「会員登録 (無料)」. Last-Modified Tue, 15 Sep 2026 |
| https://app.any-crew.com/offers | 200 | React shell 429 bytes. No cards |
| https://id.any-crew.com/signup?auth_entry_source=front | 200 | SPA shell. Labels unread |
| https://biz.any-crew.com/ | 200 | **Employer. Do not use** |
| https://menta.work/ | 200 | Home. Mentor plan titles. Marketing counts ignored |
| https://menta.work/plan | 200 | Plan cards + **NEW** labels |
| https://menta.work/index.php/plan | 200 | Same catalog |
| https://menta.work/index.php/plan?order=2 | 202 | AWS WAF. 新着 sort not read |
| https://menta.work/index.php/register/choose | 200 | 「Googleアカウントで登録する」 |
| https://menta.work/about_mentor | 200 | Mentor pitch + fee copy on page |
| https://menta.work/tokutei | 200 | 特商法. Mentor fee 20%税別 (15%+5%) + 振込 300円 |
| https://intercom.help/mentajp/ja/articles/3025582 | 200 | Help: 手数料22%（20%+消費税10%）— 2022-08-31 |
| https://intercom.help/mentajp/ja/articles/3025561 | 200 | Help: 本人確認 = Stripe. STOP |
| https://www.street-academy.com/ | 200 or **405** | 405 = AWS WAF Human Verification (first UA). 200 with a second browser UA |
| https://www.street-academy.com/teach | 200 or 405 | 200: 講師登録フォーム。「無料ではじめられる」 |
| https://www.street-academy.com/register | 200 or 405 | 200: LINE / Facebook / 「メールアドレスで登録」。Google button = GTM only |
| https://www.street-academy.com/fee | 200 or 405 | 200: 自己集客 10% / 送客 30%（対面 20%）/ リピート 10%。登録・月額 0円 |
| https://www.street-academy.com/online/all | 200 or 405 | 200: class cards + session times. Date filter JSON includes **2026-09-16** |
| https://support.street-academy.com/hc/ja | 403 | Cloudflare challenge. Help body unread |
| https://teach.street-academy.com/ | 200 | Lecturer media. Article **2026.06.18**. Not the signup form |

No signed URLs or cookies stored.
