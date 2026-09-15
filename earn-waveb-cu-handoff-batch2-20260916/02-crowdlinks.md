> **MAIN Google only.** Same mailbox as QUEUE. `{{EMAIL}}`. Google認証の付け替えは公式FAQで不可 → 初回を間違えない。
> **DRAFT_ONLY.** 無料会員のプロフィール下書きのみ。有料会員化しない。応募しない。
> **STOP-KYC.** 有料審査の追加書類・企業直接契約の身分証・口座は上げない。See [STOP-KYC.md](STOP-KYC.md).
> **No secrets.** Passwords stay off git. 連絡用とログイン用メールは両方 `{{EMAIL}}`。
> **No invented fees.** FAQはワーカー側「すべて無料」／掲載報酬から手数料は引かれない、と書く。有料会員の料金表はこのGETでは未記載 → 作らない。
> **No publish.** プロフィール公開範囲は「クラウドリンクス内」まで。一般公開は後回し。Agent did not sign up.

# CU-14 PACK — CrowdLinks / クラウドリンクス

| キー | 値 |
|---|---|
| inventory | 02 |
| cu_serial | CU-14（本番 INDEX。このフォルダの貼る順では 4番＝needs_check） |
| activity_gate | **needs_check**（PR#12。個別タイトルは見える。一覧・本文はログイン誘導。カード日付未読） |
| self_serve | **yes**（ワーカー新規登録 URL あり。企業 `/client/` は使わない） |
| cu_ready | **true**（パックあり。登録済みではない） |
| marketing | https://start.crowdlinks.jp/ （`crowdlinks.jp/` トップから遷移） |
| worker_signup | https://crowdlinks.jp/worker/signup/ |
| worker_login | https://crowdlinks.jp/worker/login/ |
| help | https://help.crowdlinks.jp/ |
| faq_worker | https://help.crowdlinks.jp/0029649d31534622a6d95ffe53df18dd |
| terms | https://crowdlinks.jp/terms |
| google_signup_preference | **PREFER_GOOGLE** |
| worker_fee_public | FAQ（2026/8/3 更新表示）: ワーカー利用は無料（企業から利用料）。掲載報酬から手数料は引かれない。**％なし。有料会員の金額は未記載 → 作らない** |
| thin_site_skip | **false** |
| stop_at_kyc | **STOP** |
| tos_note | 無料会員条件: 満18歳、学生でない、**プロフィール上の業務について実務経験が2年以上**。未確認なら年数を盛らない。該当しないと判断したらこのパックは登録しない |
| draft | true |
| observed | 2026-09-16 公開 GET |

## needs_check

- 活動: 公開一覧の新着日付が未読。人が1件クリックして日付を見てから CU を進める。HTML 内の `20260915` は AWS 署名日時であり案件日ではない。
- 登録SPA: Google ボタンは静的HTMLに未描画。FAQは Google認証を前提に書く。クリック時に「Googleでログイン / 新規登録」が無ければメール。
- 有料会員の利用料額は規約に定義があるが **数字はこのGETでは未記載**。画面に金額が出ても買わない。

## CU handoff（この机）

やってよい（下書きのみ・後続CU）:

1. ワーカー https://crowdlinks.jp/worker/signup/ 。企業ページは閉じる
2. **Google**（FAQ: Google認証。別アカウントへの付け替え不可）
3. 経歴1件以上、スキル、概要、自己紹介。公開範囲は **クラウドリンクス内**（一般公開は後回し）
4. 「話を聞きたい」／応募フォームへ進まない。マッチング報告フォームも今は送らない

フォールバック: メール。パスワードは英数字と指定記号を含む8文字以上（FAQ）。パスワードはファイルに書かない。

使わない: Facebook 新規。Googleアカウントの付け替え。

## Field map（プレースホルダ）

| 画面の項目（公開情報ベース） | 貼る値 | 必須見込み | メモ |
|---|---|---|---|
| 登録経路 | Google | 必須 | 変更できないので初回を間違えない |
| 氏名 | `{{LEGAL_NAME_KANJI}}` | 推奨 | FAQ: 本名必須ではないが推奨 |
| 生年月日 | `{{BIRTH_YEAR}}-{{BIRTH_MONTH}}-{{BIRTH_DAY}}` | 高 | 規約: 満18歳 |
| 連絡用メール | `{{EMAIL}}` | 高 | ログイン用と連絡用が分かれうる。両方 Googleメールで揃える |
| 経歴 | 1件以上必須（FAQ） | 必須 | 公開実録の範囲。2年条件は本人判断。`{{YEARS_AUTOMATION_PUBLIC}}` が空なら盛らない |
| スキル | 業務自動化, API, Python, Claude Code, Codex, 技術執筆 | 高 | |
| キャリア概要 | 下記 200 | 高 | |
| 自己紹介 | 下記 800 | 高 | |
| ポートフォリオ | `{{PORTFOLIO_URL}}` `{{GITHUB_REPO_AUTOPILOT}}` | 高 | |
| 稼働可能時間 | リモート、週次は要相談 | 任意 | |
| プロフィール公開範囲 | クラウドリンクス内公開 | 任意 | 一般公開は後回し |
| 企業ブロック | `{{BLOCK_COMPANY_NAMES}}` | 任意 | 実名を git に書かない |
| 希望単価 | `{{HOURLY_YEN_DRAFT}}` | 任意 | 空 |

共通プレースホルダは [README.md](README.md)。

CrowdLinks は契約・報酬が企業と直接（FAQ）。プラットフォーム外のKYCも STOP。

## JA bio 200（200字）

```
石田祐太。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIによる業務自動化の手順・つまずき・確認できた結果を、むずかしい言葉を避けて公開しています。公式APIだけを使う動画アップロード道具も公開中です。ブラウザ自動操作はしません。人が検品できる形で、繰り返し作業を自動化します。リモート可。未確認の数字は書きません。公開は人が決めます。秘密は貼りません。根拠を残す方針です。
```

## JA bio 800（800字）

```
石田祐太（Yuta Ishida）です。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIを使って毎日の作業を自動化する手順、つまずいた点、確認できた結果を、むずかしい言葉を避けて公開しています。売り物は「動いたように見える自動化」ではなく、人が検品できる仕組みです。公開している実録と道具を、業務委託の成果物の根拠にします。提供できること：（1）繰り返し作業の自動化設計。目的・範囲・合格条件・停止条件を先に切り、実装後に回帰確認まで残します。（2）Claude CodeやCodexなど、AIに実装を任せるときの指示の書き方、検品、失敗時の切り分け。（3）YouTubeとTikTokへの公式API投稿の仕組みづくり。ブラウザ自動操作とスクレイピングは対象外です。（4）鍵の扱い、公開事故、トークン期限など、自動化が止まりやすい箇所の点検。公開している道具の例：Autopilot Log（https://github.com/rimone0511/autopilot-log）。YouTube Data API v3 と TikTok Content Posting API のみを使い、投稿の門番は壊れても非公開側に倒れます。受けないこと：いいねやフォローの自動化、権利のない投稿代行、本人確認書類・口座・マイナンバーの代理入力、未確認のままの公開。進め方はテキスト中心です。根拠と反証を残し、公開スイッチは依頼者または本人の手に置きます。リモート可。週次の稼働時間は案件ごとに相談します。未確認の件数や年数は書きません。確認できた公開物だけを貼ります。秘密はチャットに出さず、本人の安全な入力経路だけを使います。日本語でのやり取りを標準にします。英語の一次資料は必要なら要約して渡します。契約前に範囲外を一文で確定します。納期は着手前に合意します。作業の記録を残す。
```

## STOP-AT-KYC

ここまでやってよい: Google登録、経歴1件、スキル、概要、公開範囲（内公開）。下書き保存。

ここで止める:

- 有料会員化（規約第4条の審査）
- 規約が言う追加書類
- 口座・本人確認
- 企業との直接契約で身分証を求められたとき
- 応募 / 「話を聞きたい」

## thin_site_skip

false。2026-09-16 に worker signup が HTTP 200。ヘルプFAQ更新 2026-08-01（見出し）/ FAQ本文ページは 2026/8/3 表示。トップが Studio LP に飛ぶのは死滅ではなくマーケ導線。
