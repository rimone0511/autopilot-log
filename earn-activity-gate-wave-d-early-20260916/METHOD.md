# 観測メモ（方法だけ）

日時: 2026-09-16 JST  
UA: 通常のブラウザ相当。ログイン Cookie なし。

やったこと: 公式の公開 URL に GET。ヘルプ記事と公式ブログを読む。登録フォームの送信はしていない。OAuth を完走していない。

やらなかったこと: アカウント作成、有料、KYC、応募、出品公開。

数値を作らない。公式が出していない件数・GMV・成約率・「月収」を書かない。トップのマーケ数字（登録者○万人、完了プロジェクト数など）は活動証明に使わない。

カタログ照合: 親キュー `earn-register-expand-20260916/QUEUE.md` と、先行 PR の Shufti / Twine / Fastwork 記録。先行記録と食い違う公開 GET は **今回開いた URL を正** とする。

## 公開 GET の結果（要約）

| URL | HTTP | メモ |
|---|---|---|
| www.shufti.jp/ | 200 → app.shufti.jp/ | SPA シェル約 2KB |
| app.shufti.jp/signup | 200 | シェル。ボタン未描画 |
| app.shufti.jp/jobs/search | 200 | シェル。カード未読 |
| help.shufti.jp/ | 200 | ナレッジベース |
| help …/手数料一覧 | 200 | 振込手数料の見出し |
| help …/2026年シルバーウィークの営業について | 200 | 休業案内 |
| kaikoku.blam.co.jp/ | 200 | LP。案件事例。無料登録 CTA |
| app.kaikoku.blam.co.jp/user/register/before | 200 | タイトル「会員登録前」 |
| kaikoku.blam.co.jp/entry | 404 | 使わない |
| note.com/ | 200 | トップ。公開ノートの `publishAt` |
| note.com/signup | 200 | タイトル「会員登録」 |
| www.help-note.com/hc/ja | 403 | Cloudflare。料率本文は未読 |
| blog.note.com/ | 500 | このIP。未使用 |
| usebraintrust.com/ | 200 | 企業向けトップ |
| usebraintrust.com/for-talent | 200 | Talent。$0 fees コピー |
| usebraintrust.com/jobs | 200 | 役割カード（投稿日なし） |
| usebraintrust.com/blog | 200 | 日付付き記事 |
| app.usebraintrust.com/ | 200 | アプリシェル |
| twine.net/ | 200 | マーケット LP |
| twine.net/jobs | 200 | 直投稿 Remote + Ari |
| twine.net/signup | 200 | Sign Up |
| twine.net/pricing | 200 | Standard $0 / service fee from 5% |
| twine.net/blog | 200 | 2026-08 の記事見出し |
| fastwork.co/en | 200 | TH マーケット |
| fastwork.co/en/ai-automation | 200 | n8n / make.com カテゴリ |
| fastwork.co/en/signup | 404 | SPA。売り手入口は人が辿る |
| blog.fastwork.co/ | 200 | ブログ索引 |
| twago.com/ | 200 → talent-pool.com | 企業向け Talent Pool |
| twago.com/jobs | 200 → talent-pool.com | 仕事ボードではない |
| twago.de/ | 404 | |
| 99freelas.com.br/ | 200 | クライアント向けトップ |
| 99freelas.com.br/projects | 200 | 公開プロジェクト見出し |
| 99freelas.com.br/register/freelancer | 403 | Cloudflare。本文未読 |
| 99freelas.com.br/como-funciona | 200 | 手数料コピー |
| blog.99freelas.com.br/ | 200 | ブログ索引 |
| gulp.de/ | 200 | Randstad Professional（旧 GULP） |
| gulp.de/freelancing/projekte | 200 | プロジェクトカード |
| gulp.de/registrieren | 200 | Freelancer 登録枠 |
| gulp.de/ueber-gulp/presse | 200 | プレス案内。日付付きリリースは未読 |
| xing.com/projects | 404 | 「404 - Not Found \| XING」 |
| xing.com/en | 200 | jobs network。Projects 専用机ではない |

署名付き URL、Cookie、CSRF、Ray ID は保存していない。
