> **MAIN Google only.** Official help: Googleアカウント連携。Facebook / LINE は使わない。メール登録と Google 連携は別物（ヘルプ注記）。
> **DRAFT_ONLY.** プロフィール下書き。ジョブ投稿しない。「話を聞きたい」を送らない。つながり申請をばらまかない。
> **STOP-KYC.** 身分証・公式リクルーター有料・出金は上げない／買わない。See [STOP-KYC.md](STOP-KYC.md).
> **No secrets.** Google連絡先の一括インポートをしない（他人のメールがログに乗る）。
> **No invented fees.** ユーザーのジョブ投稿はヘルプ上「1投稿まで無料」。応募手数料％はこのGETでは未記載 → 作らない。公式リクルーター有料は買わない。
> **No publish.** `/recruitment_posts` はSPA。カード日付未読のまま pass にしない。Agent did not sign up.

# CU-24 PACK — YOUTRUST

| キー | 値 |
|---|---|
| inventory | 05 |
| cu_serial | CU-24（本番 INDEX B13。このフォルダの貼る順では 5番＝needs_check） |
| activity_gate | **needs_check**（PR#12。ジョブAPIは未ログイン401。カード日付未読。ヘルプはジョブがユーザーに公開と書く） |
| self_serve | **yes**（Webでアカウント作成可。実名SNS） |
| cu_ready | **true**（パックあり。登録済みではない） |
| official | https://youtrust.jp/ （公開GETは `/lp` へ） |
| sign_in | https://youtrust.jp/sign_in |
| jobs_list | https://youtrust.jp/recruitment_posts |
| help_create | https://help.youtrust.jp/user/account/create/ |
| help_jobs | https://help.youtrust.jp/user/message/search-jobs/ |
| google_signup_preference | **PREFER_GOOGLE**（公式ヘルプ。`/sign_in` 静的HTMLはシェル → ボタン目視） |
| worker_fee_public | 投稿ヘルプ: ジョブは1件まで無料公開（**投稿する側**。CUは投稿しない）。応募％ **needs_check** |
| thin_site_skip | **false** |
| stop_at_kyc | **STOP** |
| draft | true |
| observed | 2026-09-16 公開 GET |

## needs_check

- 活動: ジョブカードの日付が公開HTMLに出ない。人が1画面見てから CU。見えないまま pass にしない。
- `/sign_in` はSPA。ヘルプは「Googleで登録」経路を書く。ボタンが無ければメール（`{{EMAIL}}`）。メール登録は Google OAuth とは別（公式ヘルプ）。
- 副業・転職意欲の公開範囲。同僚に見えない設定があれば **閉じる側**。設定が分からなければ公開トグルを触らない。

## CU handoff（この机）

やってよい（下書きのみ・後続CU）:

1. https://youtrust.jp/sign_in の **新規会員登録** → **Googleで登録**
2. 氏名は Google から入ったら `{{LEGAL_NAME_KANJI}}` / `{{DISPLAY_NAME}}` に直す（ヘルプ: 編集可）
3. プロフィール・できること・職歴・紹介コメント。**下書き**
4. ジョブを探しても「話を聞きたい」は送らない。ジョブを作らない。Google連絡先インポートをしない

フォールバック: メールで登録。メールは `{{EMAIL}}`。パスワード条件は公式ヘルプ（このファイルに実パスワードを書かない）。登録後にメール＋パスワードを足す案内があるが、パスワードは台帳のみ。

使わない: Facebook / LINE。招待コードのばらまき。公式リクルーター課金。`/signup`（404）。

SNS 実名連携を求められたら記録。KYC なら停止。

## Field map（プレースホルダ）

| 画面の項目（公開情報ベース） | 貼る値 | 必須見込み | メモ |
|---|---|---|---|
| 登録経路 | Google | 優先 | ヘルプ「Googleアカウント連携」 |
| メール | `{{EMAIL}}` | 高 | 連携後も MAIN Google で揃える |
| 氏名 | `{{LEGAL_NAME_KANJI}}` / `{{DISPLAY_NAME}}` | 必須 | Google名が来たら編集 |
| 生年月日 | `{{BIRTH_YEAR}}-{{BIRTH_MONTH}}-{{BIRTH_DAY}}` | 高 | ヘルプに「生年月日について知りたい」あり。画面を正 |
| 紹介コメント | 下記 200 | 高 | |
| できること / 自己紹介 | 下記 800 | 高 | |
| 職歴 | 公開実録のみ | 高 | `{{YEARS_AUTOMATION_PUBLIC}}` が空なら空 |
| スキル | 業務自動化, Python, API, Claude Code, Codex | 高 | |
| ポートフォリオ | `{{PORTFOLIO_URL}}` `{{GITHUB_URL}}` | 高 | |
| 顔写真 | `{{PHOTO_LOCAL_PATH}}` | 任意 | コミット禁止 |
| 招待コード | `{{INVITE_CODE}}` | 任意 | 空 |
| 副業・転職意欲 | 閉じる側の画面値 | 高 | 分からなければ触らない |
| Google連絡先 | 使わない | 禁止（このパック） | |

共通プレースホルダは [README.md](README.md)。

## JA bio 200（200字）

```
石田祐太。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIによる業務自動化の手順・つまずき・確認できた結果を、むずかしい言葉を避けて公開しています。公式APIだけを使う動画アップロード道具も公開中です。ブラウザ自動操作はしません。人が検品できる形で、繰り返し作業を自動化します。リモート可。未確認の数字は書きません。公開は人が決めます。秘密は貼りません。根拠を残す方針です。
```

## JA bio 800（800字）

```
石田祐太（Yuta Ishida）です。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIを使って毎日の作業を自動化する手順、つまずいた点、確認できた結果を、むずかしい言葉を避けて公開しています。売り物は「動いたように見える自動化」ではなく、人が検品できる仕組みです。公開している実録と道具を、業務委託の成果物の根拠にします。提供できること：（1）繰り返し作業の自動化設計。目的・範囲・合格条件・停止条件を先に切り、実装後に回帰確認まで残します。（2）Claude CodeやCodexなど、AIに実装を任せるときの指示の書き方、検品、失敗時の切り分け。（3）YouTubeとTikTokへの公式API投稿の仕組みづくり。ブラウザ自動操作とスクレイピングは対象外です。（4）鍵の扱い、公開事故、トークン期限など、自動化が止まりやすい箇所の点検。公開している道具の例：Autopilot Log（https://github.com/rimone0511/autopilot-log）。YouTube Data API v3 と TikTok Content Posting API のみを使い、投稿の門番は壊れても非公開側に倒れます。受けないこと：いいねやフォローの自動化、権利のない投稿代行、本人確認書類・口座・マイナンバーの代理入力、未確認のままの公開。進め方はテキスト中心です。根拠と反証を残し、公開スイッチは依頼者または本人の手に置きます。リモート可。週次の稼働時間は案件ごとに相談します。未確認の件数や年数は書きません。確認できた公開物だけを貼ります。秘密はチャットに出さず、本人の安全な入力経路だけを使います。日本語でのやり取りを標準にします。英語の一次資料は必要なら要約して渡します。契約前に範囲外を一文で確定します。納期は着手前に合意します。作業の記録を残す。
```

## STOP-AT-KYC

ここまでやってよい: Google登録、プロフィール、職歴、できること、公開URL。下書き保存。

ここで止める:

- 「話を聞きたい」送信
- ジョブ投稿（無料枠でも今は出さない）
- 公式リクルーター有料
- 本人確認書類
- 口座・出金
- Google連絡先の再取得／一括追加

## thin_site_skip

false。2026-09-16 にホーム・`/sign_in`・公式ヘルプ・ジョブ一覧URLが HTTP 200。カード日付が取れないので活動は needs_check のまま。死滅証拠ではない。
