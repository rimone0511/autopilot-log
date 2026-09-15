# METHOD — public GET only

Stamp: **2026-09-16 JST**  
UA: ordinary desktop Chrome string. **No login cookies.** No POST. No OAuth.

Did: GET official public URLs (follow redirects unless noted). Read titles, visible copy, listing headings, help/blog dates that appeared in HTML.

Did not: create accounts, complete Google login, buy plans, apply, publish, store secrets, cookies, CSRF tokens, or Cloudflare Ray IDs.

Do not treat homepage marketing totals (members, “○件突破”, “projetos concluídos”, category “4,800 +”) as activity proof.

Catalog: parent QUEUE `earn-register-expand-20260916/QUEUE.md`. D-early IDs follow the D01–D10 list used in [PR#22](https://github.com/rimone0511/autopilot-log/pull/22). This GET is independent; **the URL opened here is source of truth**.

## GET log (this IP)

| Desk | URL | HTTP | Note |
|---|---|---|---|
| D02 | https://kaikoku.blam.co.jp/ | 200 | Title マーケティング特化型複業… \| KAIKOKU. CTA 無料登録で案件をみる |
| D02 | https://app.kaikoku.blam.co.jp/user/register/before | 200 | Title 会員登録前 \| KAIKOKU. Form not submitted. Google button unread (gtag only in HTML) |
| D02 | https://kaikoku.blam.co.jp/entry | 404 | Unused |
| D03 | https://note.com/ | 200 | Embedded notes; `publishAt` 2026-09-12…15 (+09:00) |
| D03 | https://note.com/signup | 200 | Title 会員登録｜note（ノート） |
| D03 | https://note.com/login | 200 | Title ログイン｜note. Button `aria-label="Googleでログイン"` (not clicked) |
| D03 | https://note.com/help | 200 | 有料記事 / 有料マガジン / メンバーシップ / 定期購読案内 |
| D03 | https://www.help-note.com/hc/ja | 403 | Cloudflare challenge. Fee % unread |
| D03 | https://blog.note.com/ | DNS fail this env | Unused |
| D04 | https://www.usebraintrust.com/ | 200 | Not braintrust.com (eval SaaS) |
| D04 | https://www.usebraintrust.com/for-talent | 200 | $0 fees for talent. Create Your Profile |
| D04 | https://www.usebraintrust.com/jobs | 200 | Role cards with $/hr. No post dates |
| D04 | https://www.usebraintrust.com/blog | 200 | Headings dated Sep 14, 2026 (and other 2026 dates) |
| D04 | https://app.usebraintrust.com/ | 200 | App shell. Not signed in |
| D07 | https://www.twago.com/ | 301 → 200 | Location `https://www.talent-pool.com`. Title Talent-Pool.com \| Talent is family |
| D07 | https://www.twago.com/jobs | 301 → 200 | Same Talent Pool LP. Not a freelance board |
| D07 | https://www.twago.de/ | 404 | Title 404 Not Found |
| D07 | https://www.talent-pool.com/ | 200 | White-label Talent Pool / Fieldglass Partner |
| D08 | https://www.99freelas.com.br/ | 200 | Cadastre-se / Quero Trabalhar. Marketing totals unused |
| D08 | https://www.99freelas.com.br/projects | 200 | Public project headings |
| D08 | https://www.99freelas.com.br/register/freelancer | 403 | Cloudflare “Just a moment…” this IP. Body unread |
| D08 | https://www.99freelas.com.br/como-funciona | 200 | taxa 5%–20% (R$ 10,00 mínimo). É grátis |
| D08 | https://blog.99freelas.com.br/ | 200 | Index titles. Per-post dates not in index HTML |
| D08 | one public project URL (Laravel 12 heading) | 200 | Description HTML. No ISO `Publicado` date. **No proposal sent** |
| D09 | https://www.gulp.de/ | 200 | Randstad Professional (vormals GULP). 7 Euro client-side fee copy |
| D09 | https://www.gulp.de/freelancing/projekte | 200 | NEU cards; Start ab dates |
| D09 | https://www.gulp.de/registrieren | 200 | Freelancer / Projekte für Freelancer. Not completed |
| D09 | https://www.gulp.de/freelancing/gulp-membership | 200 | 120 Euro netto / 6 Monate; 180 / 12. **Not purchased** |
| D09 | https://www.gulp.de/ueber-gulp/presse | 200 | Press hub. Dated releases unread |
| D10 | https://www.xing.com/projects | 404 | Title 404 - Not Found \| XING |
| D10 | https://www.xing.com/en | 200 | Jobs network. Freelance jobs chip ≠ Projects desk |
| D10 | `/jobs/search?keywords=freelance` | 301 → 200 | `/jobs/search/ki?keywords=freelance`. Jobs class. **Not used to revive Projects** |

Redirects recorded as 301 Location only. No cookies saved.
