> DRAFT_ONLY paste stub. NO secrets. NO browser signup from this PR. NO publish.
> Gap-fill for CU-15 where prior packs left `/offers` dates and talent take-rate % as needs_check.
> Agent that wrote this pack did not create an account.
> `thin_site_skip: false`. Stop at KYC.

# CU-15 GAP-FILL — Anycrew（エニィクルー）

| キー | 値 |
|---|---|
| cu_serial | CU-15 |
| activity_gate | **needs_check**（`/offers` は React 空シェル 429B。案件カード未読。pass にしない） |
| self_serve | **yes**（公開 FAQ: Web プロフィールのみ。通常は面談・職務経歴書不要） |
| cu_ready | **true** |
| app | https://app.any-crew.com/ |
| marketing | https://www.any-crew.com/ |
| terms | https://www.any-crew.com/terms |
| privacy | https://www.any-crew.com/privacy |
| google_signup_preference | **PREFER_GOOGLE** |
| worker_fee_public | アプリ FAQ **cited**: 「仕事を受けるフリーランス・副業人材の方には一切費用はかかりません。」規約第5条 基本無料。**人材％は FAQ / 規約に無し → needs_check。作らない** |
| thin_site_skip | **false** |
| stop_at_kyc | **STOP** |
| draft | true |
| observed | 2026-09-16 公開 GET |

## Gap vs prior packs

| 穴（PR#12 / PR#21 / PR#33） | この GET |
|---|---|
| `/offers` SPA 空 | 再現。429 バイトの React シェル。カード日付 **needs_check のまま** |
| `www.any-crew.com/faq` | **404**（先行深掘りと同じ）。FAQ 本文はアプリトップを正とする |
| Google | アプリ HTML に「FacebookかGoogleのアカウントで利用登録」「Googleでログイン」。再確認 |
| 人材％ | 依然として数字なし。**作らない** |

人が案件を 1 件開いて日付を見てから CU を進めてよい。見えないまま pass にしない。

## CU handoff（この机）

やってよい（下書きのみ・後続 CU）:

1. 人材アプリ https://app.any-crew.com/ 。`biz.any-crew.com` は閉じる
2. 「Googleでログイン」。Facebook は新規作成しない
3. 規約第3条: 登録には外部 SNS。Google で始めたら以後 Google。メール欄だけで通るかは `needs_check`。Google が死んだら park
4. プロフィール入力。FAQ: 検索結果への表示は「非公開／公開」から選ぶ。**公開にしない**
5. 応募しない。エージェント仲介案件の職務経歴書が「必須」なら停止

## Field map（プレースホルダ）

| 画面の項目（公開情報ベース） | 貼る値 | 必須見込み | メモ |
|---|---|---|---|
| 登録経路 | Google | 必須 | |
| 氏名 | `{{LEGAL_NAME_KANJI}}` | 高 | ポリシー収集項目に氏名 |
| メール | `{{EMAIL}}` | 高 | Google から来る。確認メールは人が開く |
| 生年月日 | `{{BIRTH_YEAR}}-{{BIRTH_MONTH}}-{{BIRTH_DAY}}` | 任意〜高 | ポリシーに生年月日 |
| 所属・職歴 | 公開実録の範囲 | 高 | 通常は職務経歴書不要 |
| 職業 | 業務自動化 / エンジニア | 高 | |
| 転職意向 | 複業・業務委託 | 任意 | 転職エージェント化しない |
| 自己紹介 | 下記 200 / 800 | 高 | |
| ポートフォリオ | `{{PORTFOLIO_URL}}` | 任意 | |
| 検索結果の表示 | 非公開 | 高 | 公開スイッチを押さない |
| 職務経歴書 | スキップ | 任意 | 仲介必須なら応募しないので通常出ない |

共通プレースホルダは [INDEX.md](INDEX.md)。

公式 FAQ（アプリ）: 「Web上でプロフィールを入力頂くだけで、面談や職務経歴書は不要です。ただし、エージェントが仲介をする一部の案件では応募時に、面談や職務経歴書が必要になります。」  
このパックは応募しない。

## JA bio 200（200字）

```
石田祐太。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIによる業務自動化の手順・つまずき・確認できた結果を、むずかしい言葉を避けて公開しています。公式APIだけを使う動画アップロード道具も公開中です。ブラウザ自動操作はしません。人が検品できる形で、繰り返し作業を自動化します。リモート可。未確認の数字は書きません。公開は人が決めます。秘密は貼りません。根拠を残す方針です。
```

## JA bio 800（800字）

```
石田祐太（Yuta Ishida）です。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIを使って毎日の作業を自動化する手順、つまずいた点、確認できた結果を、むずかしい言葉を避けて公開しています。売り物は「動いたように見える自動化」ではなく、人が検品できる仕組みです。公開している実録と道具を、業務委託の成果物の根拠にします。提供できること：（1）繰り返し作業の自動化設計。目的・範囲・合格条件・停止条件を先に切り、実装後に回帰確認まで残します。（2）Claude CodeやCodexなど、AIに実装を任せるときの指示の書き方、検品、失敗時の切り分け。（3）YouTubeとTikTokへの公式API投稿の仕組みづくり。ブラウザ自動操作とスクレイピングは対象外です。（4）鍵の扱い、公開事故、トークン期限など、自動化が止まりやすい箇所の点検。公開している道具の例：Autopilot Log（https://github.com/rimone0511/autopilot-log）。YouTube Data API v3 と TikTok Content Posting API のみを使い、投稿の門番は壊れても非公開側に倒れます。受けないこと：いいねやフォローの自動化、権利のない投稿代行、本人確認書類・口座・マイナンバーの代理入力、未確認のままの公開。進め方はテキスト中心です。根拠と反証を残し、公開スイッチは依頼者または本人の手に置きます。リモート可。週次の稼働時間は案件ごとに相談します。未確認の件数や年数は書きません。確認できた公開物だけを貼ります。秘密はチャットに出さず、本人の安全な入力経路だけを使います。日本語でのやり取りを標準にします。英語の一次資料は必要なら要約して渡します。契約前に範囲外を一文で確定します。納期は着手前に合意します。作業の記録を残す。
```

## Fees — official public pages only

| Claim | Status | Source | Quote / note |
|---|---|---|---|
| 仕事を受ける側は費用なし | **cited** | https://app.any-crew.com/ FAQ | 「仕事を受けるフリーランス・副業人材の方には一切費用はかかりません。」 |
| 基本無料 | **cited** | 規約第5条 https://www.any-crew.com/terms | 「利用者は、本サービスを基本的に無料で利用することが出来ます。」求人事業者は希望により有料プラン |
| 人材側の成果報酬％ | **needs_check** | 公開規約・人材 FAQ に％なし | 企業向け成功報酬を人材プロフィールに転記しない |

## STOP-AT-KYC

ここまでやってよい: Google 登録、メール確認、プロフィール（非公開）。

ここで止める:

- 検索結果の「公開」
- エージェント仲介案件の職務経歴書が必須のとき
- 身分証・口座・面談用の個人書類パック

公式: 一部案件は応募時に面談・職務経歴書。身分証が乗ったら STOP。

## thin_site_skip

false。2026-09-16 に https://app.any-crew.com/ が HTTP 200。Google ログイン文言あり。`/offers` が空なのは薄い証拠ではない。
