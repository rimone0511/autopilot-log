> DRAFT-ONLY paste pack. NO secrets. NO browser signup. NO publish.
> Human paste only. Agent does not create accounts.
> `thin_site_skip: false` unless public evidence shows the product is dead.
> Stop at KYC: do not upload ID, My Number, bank, Stripe identity, or e-sign identity contracts.

# CU-27 PACK — Skill Shift

| キー | 値 |
|---|---|
| cu_serial | CU-27（QUEUE B16） |
| inventory | 05 |
| activity_gate | **pass**（PR#12。公式ドメイン読み替え） |
| official | https://www.skill-shift.com/ |
| queue_url_dead | https://skillshift.jp/ （2026-09-16 DNS 失敗。机の閉鎖ではない） |
| signup | https://www.skill-shift.com/signup （SPA シェル 200。ルート名 `sign-up` / 文言「個人登録」） |
| login | https://www.skill-shift.com/login |
| jobs | https://www.skill-shift.com/jobs |
| jobs_api | https://www.skill-shift.com/api/jobs （公開。サイトの求人検索が使う） |
| terms | https://www.skill-shift.com/terms （SPA） |
| google_signup_preference | **NOT_OFFERED_OAUTH** |
| thin_site_skip | **false** |
| stop_at_kyc | **STOP** |
| draft | true |
| observed | 2026-09-16 JST 公開 GET |

## Google signup preference

公開 `app.js` を GET して確認した範囲:

- 個人登録 CTA はルーター `name: "sign-up"`
- サインアップ CSS に `.btn-fb` と `.btn-register`（Facebook + 通常登録）
- `btn-google` / 「Googleで」登録は **0件**
- フォームラベル: 「メールアドレス (必須)」「お名前(姓)」「お名前(名)」「パスワード」

経路: メール `{{EMAIL}}` + `{{PASSWORD_DO_NOT_STORE}}`。Facebook は新規作成しない。画面に Google が出たらそのとき切り替える（invent しない）。

企業登録（`employer-registration` / company-signup）は使わない。人材の個人登録だけ。

## 現地労働について

QUEUE: 「地域案件が現場のみなら SKIP の現地労働へ」。この観測の公開 API 先頭行は **全部が現場ではない**。

例（見出しと `side_job_style` のみ。件数合計は書かない）:

- 2026-09-13「AI活用で業務効率化！業務棚卸しから始めるAIアドバイザー」— 基本的にオンラインでの打ち合わせを想定
- 2026-09-11「【建設業×SNS】窓・ドアの魅力を届ける集客パートナー」— リモート基本
- 2026-09-08「IC・宇宙機器部品工場のボトルネックを解消する業務改善支援」— 基本リモート（状況に応じて出社有）

対面ミックス・倉庫確認の行もある。**その行には応募しない。** 机全体は現地労働 SKIP にしない。

## Field map（プレースホルダ）

公開 JS のバリデーション文言ベース。ライブフォームを正とする。

| 画面の項目（公開情報ベース） | 貼る値 | 必須見込み | メモ |
|---|---|---|---|
| 登録経路 | メール個人登録 | 必須 | Google 未確認 |
| メールアドレス | `{{EMAIL}}` | 必須 | 確認メールのリンクは人が開く |
| お名前(姓) | `{{LEGAL_NAME_KANJI}}` の姓 | 必須 | JS: 「お名前(姓)を入力してください」 |
| お名前(名) | `{{LEGAL_NAME_KANJI}}` の名 | 必須 | |
| パスワード | `{{PASSWORD_DO_NOT_STORE}}` | 必須 | コミット禁止 |
| 電話 | `{{PHONE}}` | 高 | 規約の連絡先項目 |
| 居住地 | `{{PREFECTURE}}` `{{CITY}}` | 高 | 地方副業机。現場必須の行は応募しない |
| スキル（企業が見る欄） | 業務自動化, n8n, Claude Code, 公式API, 運用ドキュメント | 高 | JS コピー: 「出来ることを絞って記入」 |
| 自己紹介 | 下記 200 / 800 | 高 | |
| ポートフォリオ | `{{PORTFOLIO_URL}}` `{{GITHUB_REPO_AUTOPILOT}}` | 任意 | |
| 稼働 | リモート／オンライン打ち合わせ可。現地常駐は不可と書く | 高 | 数字の創作禁止 |

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

ここまでやってよい: 個人登録、スキル下書き。

ここで止める:

- 身分証・履歴書の必須提出
- 求人への応募（現場のみの行は特に）
- 企業コンソール
- 規約が本人以外の代理登録を禁じているので、エージェントが本人の代わりに完走しない（このPRはパックのみ）

公開 JS の本登録メッセージ: 「ご登録確認メールに記載されているリンクをクリックし、本登録を完了してください」。リンクは人が開く。

## thin_site_skip

false。公式 skill-shift.com 200。公開 jobs API の `created_at` **2026-09-14, 09-13, 09-12, 09-11, 09-10, 09-08**、`is_recruiting: true`。`pagination.total` は活動証明に使わない。
