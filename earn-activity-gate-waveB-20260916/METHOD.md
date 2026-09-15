# 観測メモ（方法だけ）

日時: 2026-09-16 JST  
UA: 通常のブラウザ相当。ログイン Cookie なし。

やったこと: 公式の公開 URL に GET。Skill Shift のみ、求人検索ページが呼ぶ公開 `GET /api/jobs` を見た（HTML が空だったため）。登録フォームの送信はしていない。

やらなかったこと: アカウント作成、OAuth 完走、有料、KYC、応募。

## 公開 GET の結果（要約）

| URL | HTTP | メモ |
|---|---|---|
| sokudan.work/ | 200 | 案件カード |
| sokudan.work/signup/pro | 200 | 無料新規登録。Google パス |
| sokudan.work/top/projects | 200 | 「案件が見つかりませんでした」 |
| goworkship.com/portal/search | 200 | 案件カード |
| goworkship.com/signup | 200 | |
| talent.aw-anotherworks.com/ | 200 | SPA |
| crowdlinks.jp/worker/signup/ | 200 | シェル |
| help.crowdlinks.jp/ | 200 | FAQ 2026/8/1 |
| app.any-crew.com/ | 200 | Google ログイン文言 |
| app.any-crew.com/offers | 200 | 空シェル |
| menta.work/plan | 202 | WAF |
| street-academy.com/teach | 200 | 講師フォーム |
| support.street-academy.com/hc/ja | 403 | |
| skillshift.jp/ | 失敗 | QUEUE URL |
| www.skill-shift.com/api/jobs | 200 | created_at あり |
| ai.crowdworks.jp/ | 200 | 依頼者向け |
| crowdworks.jp/aicw/register/new_email | 200 | メール登録 |
| crowdworks.co.jp/news/akdv13x1sf/ | 200 | 2026-08-20 リリース |
| itpropartners.com/ | 200 | 案件カード |
| itpropartners.com/register | 200 | 職種選択 |
| itpropartners.com/signup | 404 | |
| youtrust.jp/api/recruitment_posts | 401 | 未ログイン |
| offers.jp/jobs/engineer/side-job | 200 | 業務委託カード |
| app.shufti.jp/jobs/search | 200 | 空シェル |

署名付き URL や Cookie は保存していない。
