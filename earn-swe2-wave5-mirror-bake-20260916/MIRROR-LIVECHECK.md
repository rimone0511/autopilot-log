> Public GET only. No cookies as auth. No form POST. No Google OAuth.  
> UA: `AutopilotLogMirrorBake/2026-09-16`. Date: 2026-09-16.

# Mirror-bake livecheck log

Used to stamp verify notes. **Live screen still wins** when Devin opens a logged-in editor.

## This environment could read (HTTP 200)

| Label | Final URL | Title / note |
|---|---|---|
| CW_signup | https://crowdworks.jp/user/new_email | 会員登録【クラウドワークス】 |
| CW_employee_guide | https://crowdworks.jp/pages/guides/employee/index | 仕事を受注する方法【クラウドワークス】 |
| CW_agreement | https://crowdworks.jp/pages/agreement | クラウドワークス利用規約 |
| LI_offer_services | https://www.linkedin.com/help/linkedin/answer/a569554 | 個人プロフィールを使用してLinkedInでサービスを提供する |
| LI_edit_service | https://www.linkedin.com/help/linkedin/answer/a570566 | LinkedInサービスページを編集する |
| LI_unpublish | https://www.linkedin.com/help/linkedin/answer/a1362963 | Unpublish your LinkedIn Service Page |
| LI_services | https://www.linkedin.com/services | Discover Trusted Providers on LinkedIn |
| TT_id_help | https://help.timeticket.jp/articles/19398 | 本人確認資料の提出 |
| Contra_id_help | https://help.contra.com/en/articles/9322955-how-to-verify-your-identity-on-contra | How to Verify Your Identity on Contra |
| Craudia_faq_103 | https://www.craudia.com/app/faq/contents/103 | 会員登録に必要なものを教えてください。 |
| Craudia_faq_93 | https://www.craudia.com/app/faq/contents/93 | 本人確認書類の提出方法を教えてください。 |
| FL_home | https://www.freelancer.com/ | Hire Freelancers & Find Freelance Jobs Online |
| FL_fees | https://www.freelancer.com/feesandcharges | Freelancer Fees and Charges (cite, do not copy a table into a bid) |
| WORLD_fl_n8n | https://www.freelancer.com/jobs/n8n/ | n8n Jobs for September 2026 |
| WB_sokudan | https://sokudan.work/ | SOKUDAN マッチングサイト |
| WB_workship | https://goworkship.com/portal/search | フリーランス・業務委託案件｜Workship |
| WB_skillshift | https://www.skill-shift.com/ | 【Skill Shift】地方副業で貢献を |
| WB_itpro | https://itpropartners.com/ | ITプロパートナーズ |
| WB_offers_jobs | https://offers.jp/jobs/engineer/side-job | 200 (title empty in first 40k) |
| WB_anycrew | https://app.any-crew.com/ | Anycrew フリーランス・副業マッチングサービス |
| WB_youtrust | https://youtrust.jp/lp | YOUTRUST｜仕事専用SNS (home redirected to LP) |
| WB_shufti | https://app.shufti.jp/ | redirected from www.shufti.jp |
| WB_aicw_email | https://crowdworks.jp/aicw/register/new_email | AIクラウドワークス (**do not submit**) |

## Blocked / degraded (stay `needs_check`)

| Label | Result | Meaning for Devin |
|---|---|---|
| UW_catalog_home | **403** https://www.upwork.com/catalog | Catalog UI unread. Paste is draft only |
| UW_catalog_create | **403** Upwork Help Create-a-project | Help body not re-fetched this bake; sibling cites stand |
| UW_profile_essentials | **403** Upwork Help essentials | Fieldmap required-vs-optional still from sibling help fetch |
| WORLD_fiverr_ai | **403** Fiverr AI integrations category | World-scan Fiverr rows stay `needs_check` for click-time |
| WB_menta | **202** https://menta.work/ | WAF. Do not mark thin/dead |
| TT_home | **202** https://www.timeticket.jp/ | Use help.timeticket.jp until a browser that is not challenged |
| WB_storeka | **405** https://www.street-academy.com/teach | Lecturer form not confirmed this bake |

## Explicitly not attempted

- Any `POST` (CrowdWorks `send_email_verification`, marketplace signup, Catalog submit)
- Google OAuth, Apple, Yahoo, Facebook account create
- X search API / x.com authenticated Latest
- Logged-in HTML for `/employee/new`, Upwork profile editor, LinkedIn Service editor
