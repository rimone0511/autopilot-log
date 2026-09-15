# METHOD — public GET only

Stamp: **2026-09-16 JST**  
UA: ordinary desktop Chrome string. **No login cookies.** No POST. No OAuth.

Did: GET official public URLs (follow redirects unless noted). Read titles, visible copy, listing headings, help/blog dates that appeared in HTML.

Did not: create accounts, complete Google login, buy plans, apply, publish, store secrets, cookies, CSRF tokens, or Cloudflare Ray IDs.

Do not treat homepage marketing totals (members, “○件突破”, category “4,800 +”) as activity proof.

Catalog: parent QUEUE `earn-register-expand-20260916/QUEUE.md`. D-early IDs follow the D01–D10 list used in [PR#22](https://github.com/rimone0511/autopilot-log/pull/22). This GET is independent; **the URL opened here is source of truth**.

## GET log (this IP)

| Desk | URL | HTTP | Note |
|---|---|---|---|
| D02 | https://kaikoku.blam.co.jp/ | 200 | Title マーケティング特化型複業（副業）マッチングサービス \| KAIKOKU（カイコク） |
| D02 | https://app.kaikoku.blam.co.jp/user/register/before | 200 | Title 会員登録前 \| KAIKOKU(カイコク). Form not submitted. Google ボタンは未確定（gtag のみ） |
| D02 | https://kaikoku.blam.co.jp/entry | 404 | Unused |
| D02 | https://kaikoku.blam.co.jp/news | 404 | Unused |
| D03 | https://note.com/ | 200 | Embedded notes; `publishAt` 2026-09-12…15 (+09:00) |
| D03 | https://note.com/signup | 200 | Title 会員登録｜note（ノート） |
| D03 | https://note.com/login | 200 | Title ログイン｜note. Button `aria-label="Googleでログイン"`（未クリック） |
| D03 | https://note.com/help | 200 | 有料記事 / 有料マガジン / メンバーシップ / 定期購読案内 |
| D03 | https://www.help-note.com/hc/ja | 403 | Cloudflare “Just a moment…”. Fee % unread |
| D03 | https://blog.note.com/ | DNS fail this env | Unused |
| D04 | https://www.usebraintrust.com/ | 200 | Not braintrust.com (eval SaaS). Title AI-Powered Talent Network for Enterprise |
| D04 | https://www.usebraintrust.com/for-talent | 200 | $0 fees for talent. Create Your Profile / Join the Network |
| D04 | https://www.usebraintrust.com/jobs | 200 | Role cards with $/hr. No post dates |
| D04 | https://www.usebraintrust.com/blog | 200 | Headings dated Sep 14, 2026 (and other 2026 dates) |
| D04 | https://app.usebraintrust.com/ | 200 | App shell. Not signed in |
| D04 | https://app.usebraintrust.com/auth/sign_up/goals | 200 | Linked from Talent CTA. Shell only. **Form not submitted** |
| D07 | https://www.twago.com/ | 301 → 200 | Location `https://www.talent-pool.com`. Title Talent-Pool.com \| Talent is family |
| D07 | https://www.twago.com/jobs | 301 → 200 | Same Talent Pool LP. Not a freelance board |
| D07 | https://www.twago.de/ | 404 | Title 404 Not Found (nginx) |
| D07 | https://www.talent-pool.com/ | 200 | White-label Talent Pool / Official Fieldglass Partner |

Redirects recorded as 301 Location only. No cookies saved.

D05 Twine / D06 Fastwork: **not GET** this run (already `alive` in PR#22 / PR#13).
