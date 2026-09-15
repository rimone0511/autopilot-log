> DRAFT-ONLY paste pack. NO secrets. NO publish. NO KYC upload.
> Human / CU paste only. Live form wins.
> `thin_site_skip: false`
> Stop at KYC: マイページ設定 → 本人確認（書類 + 自撮り）。朝の本人へパスだけ残す。

# CU-09 PACK — クラウディア（Craudia）

| キー | 値 |
|---|---|
| cu_serial | CU-09（QUEUE **A9**） |
| role | **ワーカー**。クライアント募集画面に入らない |
| official | https://www.craudia.com/ |
| worker | https://www.craudia.com/worker |
| signup_faq | https://www.craudia.com/app/faq/contents/151 |
| need_faq | https://www.craudia.com/app/faq/contents/103 |
| kyc_faq | https://www.craudia.com/app/faq/contents/93 |
| fee_faq | https://www.craudia.com/app/faq/contents/72 |
| direct_pay_faq | https://www.craudia.com/faq/contents/164 |
| worker_guide | https://www.craudia.com/app/guide/crowd-sourcing/worker |
| agreement | https://www.craudia.com/app/agreement |
| google_signup_preference | **PREFER_GOOGLE** |
| thin_site_skip | **false** |
| stop_at_kyc | **STOP**（パスメモだけ朝へ） |
| draft | true |

## Google / signup preference

優先: **Google**（FAQ 151: Twitter / Facebook / Google / Yahoo **または** メール）。

フォールバック: 同じ MAIN メール。流れは公式: 認証メール → i2iID → クラウディアでプロフィール → 登録完了。認証メールは **親 Gmail**。

使わない: この GO のための Twitter/X 新規、Yahoo 新規。Google が通るなら X を縛らない。

## CU 手順（プロフィール下書き）

1. https://www.craudia.com/ — 会員登録。ワーカー。
2. Google（MAIN）。ダメなら MAIN メール。
3. プロフィール / 基本情報 / 自己紹介 / スキル（実務があるものだけ）。
4. 公開設定があれば非公開。
5. **仕事に応募しない。スキルを出品しない。** ガイドは応募とスキル出品の二系統。どちらも公開・取引開始なのでこのパックの外。
6. 本人確認画面は **開いて種類だけ確認して閉じる**。アップロードしない。下記「KYC path note」を朝の本人へ。
7. 口座・出金・電話認証が取引チャット必須でも、今は取引しないので電話を git に書かない。SMS が登録そのものを止めるときだけユーザーチャット待ち。

## Field map（プレースホルダ）

公式 FAQ は登録に **連絡可能な PC メール** があれば足りると書く。以降の項目名はワーカー画面 + 公開ガイド。無い欄は空。

| 画面の項目 | 貼る値 | 必須見込み | メモ |
|---|---|---|---|
| 登録経路 | Google | 必須 | PREFER_GOOGLE |
| メール | `{{GOOGLE_ACCOUNT_EMAIL}}` | Google から | |
| 氏名 | `{{LEGAL_NAME_KANJI}}` | 高 | |
| 氏名カナ | `{{LEGAL_NAME_KANA}}` | 高 | |
| ニックネーム / 表示 | `{{DISPLAY_NAME}}` | 高 | 推奨: `石田祐太` |
| 生年月日 | `{{BIRTH_YEAR}}` 月日 | 高 | |
| 居住地 | `{{PREFECTURE}}` `{{CITY}}` | 高 | 番地は出さなくてよい画面なら市区まで |
| 電話 | `{{PHONE}}` | 画面が必須なら | git に実番号を残さない |
| 業種 / 職種 | エンジニア / 自動化 / 業務改善の最寄り | 高 | 「AI」だけにしない |
| 状況 | 個人・副業など画面の事実 | 高 | 法人を名乗らない |
| 自己紹介 | 下記 200 / 800 を画面上限で切る | 高 | |
| 得意カテゴリ | システム・業務改善・ドキュメントの最寄り | 任意 | 未経験カテゴリを満点にしない |
| スキル | Claude Code, Codex, Python, n8n, YouTube Data API, TikTok Content Posting API, 業務自動化 | 高 | 未経験を経験と書かない |
| 職歴 | 公開実録の期間だけ。`{{YEARS_AUTOMATION_PUBLIC}}` | 任意 | 空可 |
| ポートフォリオ | `{{PORTFOLIO_URL}}` `{{GITHUB_REPO_AUTOPILOT}}` | 任意〜高 | ファイルはローカル。リポジトリに身分証を置かない |
| サムネイル | `{{PHOTO_LOCAL_PATH}}` | 任意 | |
| スキル出品 | 作らない | STOP | |
| 参加申請 | 送らない | STOP | |
| 本人確認 | やらない | STOP | パスだけメモ |
| 口座 | やらない | STOP | |

共通プレースホルダ（実値はローカル台帳。このリポジトリには書かない）:

- `{{LEGAL_NAME_KANJI}}` `{{LEGAL_NAME_KANA}}` `{{DISPLAY_NAME}}`
- `{{GOOGLE_ACCOUNT_EMAIL}}` `{{PHONE}}`
- `{{PREFECTURE}}` `{{CITY}}`
- `{{PORTFOLIO_URL}}` 推奨公開: `https://yutalab.dev/`
- `{{GITHUB_URL}}` `https://github.com/rimone0511`
- `{{GITHUB_REPO_AUTOPILOT}}` `https://github.com/rimone0511/autopilot-log`
- `{{PHOTO_LOCAL_PATH}}` コミット禁止
- `{{YEARS_AUTOMATION_PUBLIC}}` 未確認なら空

## JA bio 200

```
石田祐太。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIによる業務自動化の手順・つまずき・確認できた結果を、むずかしい言葉を避けて公開しています。公式APIだけを使う動画アップロード道具も公開中です。ブラウザ自動操作はしません。人が検品できる形で、繰り返し作業を自動化します。リモート可。未確認の数字は書きません。やり取りはクラウディア内です。秘密は貼りません。
```

## JA bio 800

```
石田祐太（Yuta Ishida）です。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIを使って毎日の作業を自動化する手順、つまずいた点、確認できた結果を、むずかしい言葉を避けて公開しています。売り物は「動いたように見える自動化」ではなく、人が検品できる仕組みです。公開している実録と道具を、業務委託の成果物の根拠にします。提供できること：（1）繰り返し作業の自動化設計。目的・範囲・合格条件・停止条件を先に切り、実装後に回帰確認まで残します。（2）Claude CodeやCodexなど、AIに実装を任せるときの指示の書き方、検品、失敗時の切り分け。（3）YouTubeとTikTokへの公式API投稿の仕組みづくり。ブラウザ自動操作とスクレイピングは対象外です。（4）鍵の扱い、公開事故、トークン期限など、自動化が止まりやすい箇所の点検。公開している道具の例：Autopilot Log（https://github.com/rimone0511/autopilot-log）。YouTube Data API v3 と TikTok Content Posting API のみを使い、投稿の門番は壊れても非公開側に倒れます。受けないこと：いいねやフォローの自動化、権利のない投稿代行、本人確認書類・口座・マイナンバーの代理入力、クラウディア外の直接支払い、未確認のままの公開。進め方はテキスト中心です。根拠と反証を残し、公開スイッチは依頼者または本人の手に置きます。リモート可。週次の稼働時間は案件ごとに相談します。未確認の件数や年数は書きません。確認できた公開物だけを貼ります。秘密はチャットに出さず、本人の安全な入力経路だけを使います。日本語でのやり取りを標準にします。契約前に範囲外を一文で確定します。納期は着手前に合意します。
```

## KYC path note（朝の本人へ。エージェントはここで終わる）

登録そのものに本人確認は **必須ではない**（FAQ 103: メールがあれば登録可。**出金**するとき本人確認が必要）。

朝に本人がやるときだけ、この順:

1. ログイン後、**マイページ設定メニュー → 本人確認**（FAQ 93）。
2. 日本の公的機関が発行した有効期限内の、顔付き書類 **いずれか1つ**: 運転免許証 / マイナンバーカード / パスポート / 在留カード / 特別永住者証明書。
3. **自撮り顔写真データは必須**（FAQ 93）。保存画像の使い回し可否は画面の指示。エージェントは撮らない。
4. 目安: 提出後 **3営業日程度**（FAQ 93）。完了するとプロフィールに本人確認済みアイコン。
5. 海外在住の追加書類は今のオペレーター想定外。出たら止めて本人。

エージェントが書いてよいログ（秘密なし）:

```
desk: Craudia
screen: マイページ設定 → 本人確認
action: STOP no upload
morning: user
docs_hint: 顔付き公的書類 + 自撮り（FAQ 93）
when: 出金の前。登録完了には不要（FAQ 103）
```

書類写真・番号・口座は git / チャットに置かない。

## Fees（発明しない）

- FAQ 72: システム利用料は **納品して採用されたときのみ**。**5万円までは一律 15%**。それより上は金額に応じて変わる。詳細は公式「システム手数料について」。
- 利用規約: ワーカー負担のシステム利用手数料は報酬の **3〜15%（消費税込）** の範囲、採用確定時に報酬から控除。
- 階段の中間レートをこのパックで表にしない。現行ページを正とする。
- この GO は採用も出金もしないので、手数料入力欄は触らない。

## STOP-AT-KYC

ここまでやってよい: Google 登録、プロフィール、スキル、公開 URL。

ここで止める:

- 本人確認アップロード（書類・自撮り）
- 口座・振込先・出金
- 参加申請、スキル出品、見積もり公開
- サイト外メール/電話/口座の交換（直接取引。FAQ 164 / 規約）

## thin_site_skip

false。2026-09-15 に craudia.com の FAQ 151 / 103 / 93 / 72 / 164 とワーカーガイドが HTTP で読める。Google 登録を FAQ が明記。
