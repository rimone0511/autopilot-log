# 観測メモ（方法だけ）

日時: 2026-09-16 JST  
UA: 通常のブラウザ相当。ログイン Cookie なし。

やったこと: 公式の公開 URL に GET。ヘルプ記事を読む。登録フォームの送信はしていない。OAuth を完走していない。

やらなかったこと: アカウント作成、有料、KYC、応募、出品公開。

12机の選び方: Fit-Med のうち本人専用／面接エージェント専用ではない机。プロダクト化・リモートを優先。現地労働・寄せ集め専用・閉鎖は **数えずに** 切る（[SKIP.md](SKIP.md)）。

## 公開 GET の結果（要約）

| URL | HTTP | メモ |
|---|---|---|
| skima.jp/ | 200 | 価格付きカード |
| skima.jp/guide/sell | 200 | 出品ガイド |
| skima.jp/entry | 200 | Google / メール |
| payhip.com/ | 403 | Cloudflare |
| help.payhip.com/article/164-how-to-sell-your-first-product-on-payhip | 200 | Invisible 下書き |
| help.payhip.com/article/351-product-visibility | 200 | 更新 2025-11-06 |
| ko-fi.com/ | 200（WebFetch） / 403（このIPの curl） | トップ本文 |
| ko-fi.com/shop | 403 | Cloudflare |
| twine.net/jobs | 200 | 直投稿 Remote + Ari |
| twine.net/signup | 200 | Sign Up |
| fastwork.co/en | 200 | マーケット |
| fastwork.co/en/ai-automation | 200 | n8n / make |
| truelancer.com/ | 200（WebFetch） | トップ |
| truelancer.com/freelance-jobs | 200（WebFetch） / 429（curl） | September 2026、2 hours ago |
| 99designs.com/ | 200 | コンテスト寄り |
| 99designs.com/how-it-works | 200 | 1-to-1 と contest |
| www.shufti.jp/ | 200 | SPA 空 |
| app.shufti.jp/jobs/search | 200 | SPA 空 |
| app.shufti.jp/signup | 200 | シェル |
| help.shufti.jp/ | 200 | ヘルプ索引 |
| workshift-sol.com/ | 200 | 案件カード |
| workshift-sol.com/jobs/view/13758 | 200 | 公開日 2026-09-11 |
| workshift-sol.com/registration/mail_start | 200 | メール／Facebook |
| workshift-sol.com/pages/term | 200 | 2026-04-11 改定 |
| workshift-sol.com/job/search | 404 | 使わない |
| workshift-sol.com/jobs/search | 200 | CAPTCHA |
| mamaworks.jp/ | 200 | 在宅カード |
| mamaworks.jp/entry | 200 | メール仮登録 |
| dribbble.com/services | 200 | 価格付きサービス |
| dribbble.com/jobs | 200 | 求人ボード（使わない） |
| wellfound.com/ | 200 | 求人／採用 |
| wellfound.com/jobs | 200 | 求人ボード |

署名付き URL、Cookie、CSRF、Ray ID は保存していない。
