> DRAFT-ONLY paste pack. NO secrets. NO browser signup. NO publish.
> Human paste only. Agent does not create accounts.
> `thin_site_skip: false` unless public evidence shows the product is dead.
> Stop at KYC: do not upload ID, My Number, bank, Stripe identity, or e-sign identity contracts.

# CU-26 PACK — AI CrowdWorks（AIクラウドワークス）

| キー | 値 |
|---|---|
| cu_serial | CU-26（QUEUE B15） |
| inventory | 04 |
| activity_gate | **needs_check**（PR#12。公開仕事詳細は「読み込み中」） |
| official | https://ai.crowdworks.jp/ |
| talent_register | https://crowdworks.jp/aicw/register/new_email |
| login | https://crowdworks.jp/aicw/login |
| projects | https://ai.crowdworks.jp/projects/ |
| news_release | https://crowdworks.co.jp/news/akdv13x1sf/ （正式リリース **2026-08-20**） |
| privacy | https://crowdworks.co.jp/privacy_policy/ |
| google_signup_preference | **EMAIL_ONLY**（公開 HTML に Google 登録ボタン未確認） |
| thin_site_skip | **false** |
| stop_at_kyc | **STOP** |
| draft | true |
| observed | 2026-09-16 JST 公開 GET |

## needs_check

QUEUE: **売り手入口が開いているかを登録前に目視。** この観測:

- 事前登録キャンペーンはニュース上「終了」。正式リリース記事は **2026-08-20**。
- 人材登録 URL は HTTP 200。この環境の HTML は「JavaScript を有効に」エラーシェルで、フォームラベルは未描画。PR#12 は同 URL を「カンタン無料会員登録」（メールまたは既存 CrowdWorks ID）と記録。
- `https://ai.crowdworks.jp/projects/` は「読み込み中」。日付付きの公開ボードは未読。
- トップの「現在募集中の仕事」はカテゴリ例（Claude Code 利用支援、n8n は未出。広告レポート自動化、ルーチンワーク自動化など）。件数は書かない。

**人が登録面と仕事一覧を1画面見てから** CU を進める。ボードが空のままならプロフィール下書き可否だけ本人が決める。見えないことを薄いと決めない。

## Google signup preference

この観測の公開 HTML では Google OAuth ボタンは確認できない。PR#12 も「Google 未確認（メール登録）」。

経路: メール `{{EMAIL}}`（MAIN Google のメール）。既存クラウドワークス ID があればそれを使う（新規 CW アカウントを増やさない）。

画面に Google が出たらそのとき PREFER_GOOGLE に切り替える。出ないと決めつけて invent しない。

## Field map（プレースホルダ）

フォーム本文がこの環境では未描画。以下は PR#12 + トップの売り手向けコピーに基づく下書き。ライブフォームを正とする。

| 画面の項目（公開情報ベース） | 貼る値 | 必須見込み | メモ |
|---|---|---|---|
| 登録経路 | メール（または既存 CW ID） | 必須 | Google は未確認 |
| メール | `{{EMAIL}}` | 必須 | |
| 氏名 | `{{LEGAL_NAME_KANJI}}` | 高 | |
| 表示名 | `{{DISPLAY_NAME}}` | 高 | |
| 専門 | AI を使った業務自動化・実装。ブラウザ自動操作はしない | 高 | トップの仕事例に寄せる |
| スキル | Claude Code, n8n, Python, 公式 API, 運用ドキュメント | 高 | カテゴリ例に Claude Code 利用支援がある。未経験を書かない |
| 自己紹介 | 下記 200 / 800 | 高 | |
| ポートフォリオ | `{{PORTFOLIO_URL}}` `{{GITHUB_REPO_AUTOPILOT}}` | 任意 | |
| 稼働 | リモート可。週次は要相談 | 高 | 数字の創作禁止 |

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

ここまでやってよい（人が入口を辿ったあと）: 無料会員のメール登録、プロフィール下書き。

ここで止める:

- 事前登録が閉じたフォームを探して無理に送ること
- 仕事への「興味がある」/ 応募（一覧が読めてもこのパックでは送らない）
- 身分証・口座・マイナンバー
- 依頼者（発注）側の「仕事を依頼する」「無料相談」導線に入ること
- マーケの事前登録人数をプロフィールに書くこと

## thin_site_skip

false。正式リリース記事 2026-08-20。トップ 200。人材登録 URL 200。仕事一覧シェル 200。公開ボードが読めないのでゲートは needs_check のまま。SKIP thin にしない。
