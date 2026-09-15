> DRAFT-ONLY paste pack. NO secrets. NO browser signup. NO publish.
> Human paste only. Agent does not create accounts.
> `thin_site_skip: false` unless public evidence shows the product is dead.
> Stop at KYC: do not upload ID, My Number, bank, Stripe identity, or e-sign identity contracts.

# CU-24 PACK — YOUTRUST（ユートラスト）

| キー | 値 |
|---|---|
| cu_serial | CU-24（QUEUE B13） |
| inventory | 02 |
| activity_gate | **needs_check**（PR#12。ジョブカード日付は未ログインで未読） |
| official | https://youtrust.jp/ （公開 GET は `/lp` へ 302） |
| jobs_list | https://youtrust.jp/recruitment_posts （200。SPA。カード本文なし） |
| help_create | https://help.youtrust.jp/user/account/create/ |
| help_jobs | https://help.youtrust.jp/user/message/search-jobs/ |
| help_profile | https://help.youtrust.jp/user/profile/ |
| google_signup_preference | **PREFER_GOOGLE**（ヘルプ。サインアップ直URLは LP。クリック時にボタン目視） |
| thin_site_skip | **false** |
| stop_at_kyc | **STOP** |
| draft | true |
| observed | 2026-09-16 JST 公開 GET |

## needs_check

公開ジョブ一覧 `/recruitment_posts` はタイトル「副業・転職のジョブ（募集）一覧」まで。カードと日付は SPA。`GET /api/recruitment_posts` は PR#12 で未ログイン 401。

**人が1画面、ジョブの日付または「話を聞きたい」可能なカードを見てから** CU を進める。見えないまま pass にしない。製品自体はヘルプがアカウント作成・ジョブ検索を案内しているので SKIP thin にしない。

## Google signup preference

公式ヘルプ「アカウントを作成したい」の経路:

- 【推奨】メールアドレス連携 — `{{EMAIL}}`（Googleメール。ヘルプ注: Googleメールでの登録は Googleアカウント連携とは別）
- 【推奨】Facebookアカウント連携 — **新規 Facebook を作らない**
- Googleアカウント連携 — 「お手持ちのGoogleアカウントと連携して登録できます」
- LINE連携 — 使わない（MAIN Google 方針）

優先: 画面に **Googleアカウント連携** が出たらそれを押す（MAIN Google）。出なければメール連携（`{{EMAIL}}`）。Facebook 推奨ボタンは新規作成しない。

`https://youtrust.jp/signup` と `/register` は 2026-09-16 に 404。`/users/sign_up` は `/lp` へ飛ぶ。登録ボタンは LP 上で人が目視する。

## Field map（プレースホルダ）

ヘルプ TOC ベース。ライブフォームを正とする。

| 画面の項目（公開情報ベース） | 貼る値 | 必須見込み | メモ |
|---|---|---|---|
| 登録経路 | Googleアカウント連携（無ければメール） | 必須 | PREFER_GOOGLE |
| メール | `{{EMAIL}}` | 必須 | 認証メールのリンクは人が開く。コードをチャットに貼らない |
| 表示プロフィール名 | `{{DISPLAY_NAME}}` | 高 | ヘルプ「表示プロフィール名を変更したい」 |
| 氏名 | `{{LEGAL_NAME_KANJI}}` | 高 | 公開名と戸籍名が分かれる画面なら公開は Display |
| 生年月日 | `{{BIRTH_YEAR}}-{{BIRTH_MONTH}}-{{BIRTH_DAY}}` | 高 | ヘルプに独立記事あり |
| 職歴・学歴 | 公開実録の範囲だけ | 高 | 未確認の年数は空 |
| 「できること」 | 業務自動化 / n8n / 公式API投稿の仕組み / 運用ドキュメント | 高 | |
| 紹介コメント | 下記 200 / 800 | 高 | |
| プロフィール写真 | `{{PHOTO_LOCAL_PATH}}` | 任意 | コミット禁止。身分証写真ではない |
| SNS | `{{GITHUB_URL}}` | 任意 | 実名SNSの強制が出たら記録して停止判断 |
| 招待コード | `{{INVITE_CODE}}` | 任意 | 空でよい |
| 副業・転職意欲 | 複業・業務委託（転職だけにしない） | 高 | ヘルプ: 同僚への公開範囲がある。広く「転職中」にしない |
| プロフィール公開範囲 | 最小。下書き相当 | 必須 | 公開トグルは人が決めるまで触らない |

共通プレースホルダは [INDEX.md](INDEX.md)。

## JA bio 200（200字）

```
石田祐太。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIによる業務自動化の手順・つまずき・確認できた結果を、むずかしい言葉を避けて公開しています。公式APIだけを使う動画アップロード道具も公開中です。ブラウザ自動操作はしません。人が検品できる形で、繰り返し作業を自動化します。リモート可。未確認の数字は書きません。公開は人が決めます。秘密は貼りません。根拠を残す方針です。
```

## JA bio 800（800字）

```
石田祐太（Yuta Ishida）です。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIを使って毎日の作業を自動化する手順、つまずいた点、確認できた結果を、むずかしい言葉を避けて公開しています。売り物は「動いたように見える自動化」ではなく、人が検品できる仕組みです。公開している実録と道具を、業務委託の成果物の根拠にします。提供できること：（1）繰り返し作業の自動化設計。目的・範囲・合格条件・停止条件を先に切り、実装後に回帰確認まで残します。（2）Claude CodeやCodexなど、AIに実装を任せるときの指示の書き方、検品、失敗時の切り分け。（3）YouTubeとTikTokへの公式API投稿の仕組みづくり。ブラウザ自動操作とスクレイピングは対象外です。（4）鍵の扱い、公開事故、トークン期限など、自動化が止まりやすい箇所の点検。公開している道具の例：Autopilot Log（https://github.com/rimone0511/autopilot-log）。YouTube Data API v3 と TikTok Content Posting API のみを使い、投稿の門番は壊れても非公開側に倒れます。受けないこと：いいねやフォローの自動化、権利のない投稿代行、本人確認書類・口座・マイナンバーの代理入力、未確認のままの公開。進め方はテキスト中心です。根拠と反証を残し、公開スイッチは依頼者または本人の手に置きます。リモート可。週次の稼働時間は案件ごとに相談します。未確認の件数や年数は書きません。確認できた公開物だけを貼ります。秘密はチャットに出さず、本人の安全な入力経路だけを使います。日本語でのやり取りを標準にします。英語の一次資料は必要なら要約して渡します。契約前に範囲外を一文で確定します。納期は着手前に合意します。作業の記録を残す。
```

## STOP-AT-KYC

ここまでやってよい（ゲート合格後）: Google またはメール登録、プロフィール下書き、スキル。

ここで止める:

- 身分証・顔写真付き証明書
- SNS 実名連携を「必須」と言われたとき（任意なら記録して続行可否を本人へ。強制なら停止）
- 「話を聞きたい」/ ジョブ応募
- プロフィールを全公開にする
- 認証コードをチャットや git に貼る

## thin_site_skip

false。2026-09-16 に LP 200、ジョブ一覧シェル 200、ヘルプがアカウント作成とジョブ検索を案内。カード日付が無いことは薄い証拠ではない。
