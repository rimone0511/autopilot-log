# 観測メモ（方法だけ）

日時: 2026-09-16  
UA: 通常のブラウザ相当。ログイン Cookie なし。

やったこと: 公式の公開 URL に GET。HTML / 公開ヘルプ / 公開 JS に出た見出し・リンク・ラベルだけ記録。  
やらなかったこと: アカウント作成、OAuth 完走、有料、KYC、応募、出品、パスワード入力。

件数・「○万人」・ホームページのマーケ％（例: SOKUDAN「リモート案件 92%」）は活動証明に使わない。  
手数料％は公式ページに数字があるときだけ **cited**。無ければ **needs_check**。

| URL | HTTP | メモ |
|---|---|---|
| https://www.skill-shift.com/ | 200 | SPA シェル。canonical あり |
| https://www.skill-shift.com/sign-up | 200 | meta description「Skill Shiftの個人登録ページ」。公開 JS `name:"sign-up"` |
| https://www.skill-shift.com/login | 200 | SPA |
| https://www.skill-shift.com/terms-of-service | 200 | みらいワークス。第9条 個人会員の登録・提案は無料（2020年4月現在） |
| https://www.skill-shift.com/api/jobs | 200 | 公開 JSON。`created_at` 例 2026-09-14。**total は書かない** |
| https://skillshift.jp/ | DNS fail | QUEUE 旧 URL。使わない |
| https://sokudan.work/ | 200 | FAQ「すべて無料でご利用いただけます」（人材） |
| https://sokudan.work/signup/pro | 200 | 「無料新規登録」。Google / Facebook / LinkedIn / X / GitHub / メール |
| https://sokudan.work/login | 200 | 「Google で ログイン」 |
| https://sokudan.work/pages/terms | 200 | CAMELORS。第4条 審査書類。第10条 利用料の **料率なし** |
| https://sokudan.work/pages/policy | 200 | プライバシー（`/pages/privacy` は 404） |
| https://app.any-crew.com/ | 200 | 「FacebookかGoogle」「一切費用はかかりません」 |
| https://www.any-crew.com/terms | 200 | 第5条 基本無料。求人事業者の有料プラン |
| https://www.any-crew.com/privacy | 200 | 収集: 氏名・メール・職歴・生年月日等 |
| https://menta.work/index.php/register/choose | 200 | 「Googleアカウントで登録する」 |
| https://menta.work/tokutei | 200 | メンター手数料 20%税別（15+5）。振込都度 300円 |
| https://menta.work/about_mentor | 200 | 出金: 売上1,000円超かつ入金から30日。事前に本人確認と口座 |
| https://intercom.help/mentajp/ja/articles/3025561 | 200 | Stripe 本人確認 |
| https://intercom.help/mentajp/ja/articles/3025582 | 200 | 運用案内「手数料22%（20%+消費税10%）」— 特商法と併記 |
| https://www.street-academy.com/ | 405 | AWS WAF Human Verification |
| https://www.street-academy.com/register | 405 | 同上 |
| https://www.street-academy.com/teach | 405 | 同上 |
| https://support.street-academy.com/hc/ja/articles/200700579 | 403 | Cloudflare challenge。料率は公式 URL として引用し、本文 GET は **needs_check** |
| https://teach.street-academy.com/ | 200 | 講師向けメディア。登録フォームではない |

SPA の Skill Shift 個人登録ラベルは、公開 `app.js` の Vue 文字列から取った（フォーム送信はしていない）。
