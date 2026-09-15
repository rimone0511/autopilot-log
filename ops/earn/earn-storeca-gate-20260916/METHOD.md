# METHOD — public GET only (B12 ストアカ)

Datetime: **2026-09-16 JST** (this authoring GET)  
UA: ordinary desktop Chrome string, then a Safari string on the same URLs. No login cookie. No form POST.

Did: GET official public URLs. Record status, titles, visible copy, dates that appeared in HTML.  
Did not: account create, OAuth complete (`/auth/line`, `/auth/facebook` not followed), paid plan, KYC, class create, publish, password input.

Do not treat category counts (例: オンライン「すべてのカテゴリー (37,014)」) or 「累計受講者数 209 万人」 as activity proof.  
Fee % only from `/fee` when the official page showed a number. Help body unread this GET → do not cite help rates.

CSRF / `authenticity_token` appeared in some HTML. **Not saved here.**

## HTTP (this GET)

Both UAs returned the same status codes on these hosts.

| URL | HTTP | Note |
|---|---|---|
| https://www.street-academy.com/ | **200** | Title「ストアカ \| 教えたいと学びたいをつなぐまなびのマーケット」。**No AWS WAF body this GET.** Home cards include session labels **9月16日** … **9月19日**. nginx |
| https://www.street-academy.com/teach | **200** | Title「ストアカ講師/主催団体登録フォーム」。Teacher LP + login/signup controls. See [GATE.md](GATE.md) |
| https://www.street-academy.com/register | **200** | 無料登録。LINE / Facebook / `user[email]` + submit「メールアドレスで登録」。**not submitted** |
| https://www.street-academy.com/fee | **200** | Title「ストアカの利用料について｜先生・主催団体向け」。Rates on page |
| https://www.street-academy.com/online/all | **200** | Title「オンライン習い事レッスン・講座の一覧 - 全てのジャンル」。Class cards + session times + date-filter JSON including **2026-09-16** |
| https://www.street-academy.com/online/all?order=new | **200** | Same catalog host. 新着 sort HTML returned (not used as a count) |
| https://www.street-academy.com/myclass/99028 | **200** | Detail title「伝わる話し方が身に付くコミュニケーション練習会…」。**This GET not WAF.** Sibling GETs had 405 — do not assume always 200 |
| https://www.street-academy.com/help | **404** | www path. Not 403. Short not-found HTML (no `<title>`) |
| https://www.street-academy.com/top | **404** | www path. Same not-found shell |
| https://www.street-academy.com/support | **404** | www path |
| https://www.street-academy.com/faq | **403** | Title「Just a moment...」。Cloudflare challenge this GET |
| https://www.street-academy.com/guideline | **200** | Guideline HTML present. Body not used as activity proof |
| https://support.street-academy.com/hc/ja | **403** | Cloudflare. Title「Just a moment...」。Help index unread |
| https://support.street-academy.com/hc/ja/articles/200700579 | **403** | Cloudflare. Fee-help article unread |
| https://teach.street-academy.com/ | **200** | Lecturer media「教えルン」。PickUp **2026.06.18**. **Not** the `/teach` signup form |

No signed URLs or cookies stored.

## vs sibling GETs (not copied; contrast only)

| Source | www `/` | `/teach` | catalog dates | help |
|---|---|---|---|---|
| [PR#12](https://github.com/rimone0511/autopilot-log/pull/12) | WAF on top (that GET) | 200 | unread (`needs_check`) | support **403** |
| [PR#33](https://github.com/rimone0511/autopilot-log/pull/33) | www **405** WAF | 405 | unread | support URL listed; GET 403 |
| [PR#61](https://github.com/rimone0511/autopilot-log/pull/61) | 200 **or** 405 | 200 or 405 | `/online/all` 200 second UA | support **403** |
| **This GET** | **200** no WAF body | **200** | **read** (`pass`) | www `/help` **404**; support **403**; www `/faq` **403** |

WAF / Cloudflare on a later click is **not** a dead site. Park if a human cannot pass the challenge.
