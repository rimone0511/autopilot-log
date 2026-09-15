> **MAIN Google only.** Use 「Google で登録する」 (`/oauth/worker_signup/google`). GitHub は任意のあと。X / LinkedIn を新規に作らない。
> **DRAFT_ONLY.** ワーカープロフィール下書き。求人に応募しない。スカウト返信しない。
> **STOP-KYC.** 面談・契約・出金の本人確認は上げない。See [STOP-KYC.md](STOP-KYC.md).
> **No secrets.** OTP とパスワードは git に書かない。
> **No invented fees.** 規約: マッチング成功報酬は **クライアントが** 当社指定の手数料を払う。ユーザー側の％はこのGETでは未記載 → 作らない。LPの「35,000人」は活動証明に使わない。
> **No publish.** Jobs の「登録して求人に応募する」は押さない。Agent did not sign up.

# CU-25 PACK — Offers

| キー | 値 |
|---|---|
| inventory | 04 |
| cu_serial | CU-25（本番 INDEX B14。このフォルダの貼る順では 3番＝pass） |
| activity_gate | **pass**（PR#12。Jobs 業務委託カード更新日 2026-09-10。このGETでも同日カード） |
| self_serve | **yes**（`/worker/signup` が開いている。トップは転職コピーが強いが Jobs は業務委託が残る） |
| cu_ready | **true**（パックあり。登録済みではない） |
| official | https://offers.jp/ |
| worker_signup | https://offers.jp/worker/signup |
| jobs_side | https://offers.jp/jobs/engineer/side-job |
| terms | https://offers.jp/terms |
| google_signup_preference | **PREFER_GOOGLE** |
| worker_fee_public | [利用規約](https://offers.jp/terms) マッチング成功報酬はクライアント負担。**％未記載 → 作らない**。有料ブースは買わない |
| thin_site_skip | **false** |
| stop_at_kyc | **STOP** |
| draft | true |
| observed | 2026-09-16 公開 GET |

## needs_check

- ユーザーが払うマージン％は公式規約に数字なし。第三者記事の「ワーカー無料・マージンなし」を手数料欄に固定しない。
- トップは「ハイクラスエンジニア**転職**」。QUEUE の「転職導線だけなら再判定」は、Jobs の業務委託を見て **pass**（PR#12）。応募はしない。
- 案件カードの時給レンジは **その求人の提示**。プロフィール希望単価にコピーしない。

## CU handoff（この机）

やってよい（下書きのみ・後続CU）:

1. ワーカー https://offers.jp/worker/signup （`/signup` は 404）
2. **Google で登録する**。企業 `/client/login` は閉じる
3. プロフィール・経歴・スキル・公開URL。GitHub 連携は任意（公開リポジトリと一致するなら可）。**下書き**
4. 業務委託意欲は画面値の最寄り。転職意欲を盛らない。Jobs を見ても **応募しない**

フォールバック: 「メールアドレスで登録する」。メールは `{{EMAIL}}`。

使わない: 新規 X アカウント。有料ブース。年収診断の送信が必須なら空で進むか park。

## Field map（プレースホルダ）

| 画面の項目（公開情報ベース） | 貼る値 | 必須見込み | メモ |
|---|---|---|---|
| 登録経路 | Google | 必須 | `/oauth/worker_signup/google` が公開HTMLにある |
| メール | `{{EMAIL}}` | Googleから来る | |
| 氏名 | `{{LEGAL_NAME_KANJI}}` | 高 | |
| 生年月日 | `{{BIRTH_YEAR}}-{{BIRTH_MONTH}}-{{BIRTH_DAY}}` | 高 | 第三者解説が基本情報に言及。画面を正とする |
| 活動拠点 | `{{PREFECTURE}}` `{{CITY}}` | 高 | |
| 電話 | `{{PHONE}}` | 高 | SMSなら park |
| 経歴 | 下記 800 を短縮 | 高 | 年数創作禁止 |
| スキル | Claude Code, Codex, Python, API, 業務自動化, YouTube Data API | 高 | |
| 働ける職種 | エンジニア / 自動化の最寄り | 高 | |
| 業務委託（副業）意欲 | 検討する、の最寄り | 高 | 盛らない |
| 転職意欲 | 急いでいない / 良い話があれば の最寄り | 任意 | 転職だけに振り切らない |
| 自己紹介 | 下記 200 / 800 | 高 | |
| GitHub | `{{GITHUB_URL}}` `{{GITHUB_REPO_AUTOPILOT}}` | 任意 | Googleのあと |
| ポートフォリオ | `{{PORTFOLIO_URL}}` | 高 | |
| 希望単価 | `{{HOURLY_YEN_DRAFT}}` | 任意 | 空。カードの 4,000〜12,000 を貼らない |

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

ここまでやってよい: Google登録、プロフィール、スキル、公開URL。下書き保存。

ここで止める:

- 「登録して求人に応募する」
- ヘッドハント面談の日程確定（CU）
- 本人確認書類
- 口座・出金
- 有料ブース / 優先掲載

## thin_site_skip

false。2026-09-16 に `/worker/signup` が HTTP 200。「Google で登録する」可視。Jobs 業務委託カードに 2026-09-10 の更新日。
