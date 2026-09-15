> **MAIN Google only.** Same mailbox as QUEUE. `{{EMAIL}}` / `{{GOOGLE_ACCOUNT_EMAIL}}`. No Facebook / Apple / LINE just for this desk.
> **DRAFT_ONLY.** Profile save only. No エントリー, スカウト返信, 成約報告, 公開トグル.
> **STOP-KYC.** 契約署名・前払い本人確認・口座は上げない。See [STOP-KYC.md](STOP-KYC.md).
> **No secrets.** Passwords, OTP, phone digits stay off git.
> **No invented fees.** 前払いの手数料％は画面で確認。このGETでは数字なし → 作らない。
> **No publish.** This pack is not a live listing. Agent that wrote it did not create an account.

# CU-11 PACK — Workship（ワークシップ）

| キー | 値 |
|---|---|
| inventory | 01 |
| cu_serial | CU-11（本番直列の Week2 先頭。このフォルダの貼る順でも先頭） |
| activity_gate | **pass**（PR#12。`/portal/search` に案件カード） |
| self_serve | **yes**（公開「フリーランス登録」。面談必須と書いていない） |
| cu_ready | **true**（パックあり。登録済みではない） |
| official | https://goworkship.com/ |
| signup | https://goworkship.com/signup |
| help_signup | https://goworkship.com/help/how_to/44 |
| flow | https://goworkship.com/flow |
| search | https://goworkship.com/portal/search |
| google_signup_preference | **PREFER_GOOGLE**（SNSアイコン。貼る人が Google ラベルを目視） |
| worker_fee_public | ヘルプは前払いを「手数料・利用規約を確認の上」と書く。**％はこのGETでは未記載 → 作らない**。お祝い金1万円は成約後（今はやらない） |
| thin_site_skip | **false** |
| stop_at_kyc | **STOP** |
| draft | true |
| observed | 2026-09-16 公開 GET |

## needs_check

- 登録面の FirebaseUI は静的HTMLに Google 文字列が無い。**アイコンに Google と書いてあることだけ確認する。** 無ければメール登録に倒す（メールは `{{EMAIL}}`）。
- ワーカー手数料の％は公式ヘルプに数字なし。雑誌の「マージンが発生しない」はマーケコピーであり、このパックの手数料欄に貼らない。

マーケの件数見出し（検索結果の「全○件」）は **活動証明に使わない**。

## CU handoff（この机）

やってよい（下書きのみ・後続CU）:

1. 人材登録 https://goworkship.com/signup 。企業向け `enterprise.goworkship.com` は閉じる
2. 「SNSで登録」の **Google**。公式ヘルプは「SNSのアイコン」
3. プロフィール・職歴・スキル・公開URLを Field map どおり。**下書き保存**（ヘルプ: 自己紹介は「更新する」で保存）
4. エントリーしない。スカウトに返信しない。成約報告しない

フォールバック: メールで無料登録。メールは `{{EMAIL}}`。確認URLは24時間（公式ヘルプ）。reCAPTCHA は人が解く。

使わない: この仕事のためだけの新規 SNS。招待コード `{{INVITE_CODE}}` は空でよい。

## Field map（プレースホルダ）

| 画面の項目（公開情報ベース） | 貼る値 | 必須見込み | メモ |
|---|---|---|---|
| SNS / Google | Googleアカウント `{{EMAIL}}` | 優先 | ラベル目視 |
| メール | `{{EMAIL}}` | メール経路なら必須 | 確認URLは24時間 |
| パスワード | メール経路のみ。このファイルに書かない | メール経路 | ローカル台帳 |
| 招待コード | `{{INVITE_CODE}}` | 任意 | 空 |
| 利用規約同意 | 本人が読む | 必須 | エージェントは同意しない |
| 生年月日 | `{{BIRTH_YEAR}}-{{BIRTH_MONTH}}-{{BIRTH_DAY}}` | 高 | 公式ヘルプはこのGETで年齢条を未記載。画面が18歳未満不可なら従う |
| 職種 | エンジニア / 業務自動化 / ディレクター系の最寄り | 高 | |
| 働き方 | フリーランスまたは複業の画面値 | 高 | 本業の就業規則は本人判断 |
| 自己紹介 | 下記 200 / 800 | 高 | https://goworkship.com/flow と [自己紹介ヘルプ](https://goworkship.com/help/edit_profile/52) |
| 職歴 | 公開実録の範囲のみ | 高 | 年数創作禁止。`{{YEARS_AUTOMATION_PUBLIC}}` が空なら空 |
| スキル | Claude Code, Codex, Python, API連携, 業務自動化, 技術記事 | 高 | |
| ポートフォリオ | `{{PORTFOLIO_URL}}` `{{GITHUB_REPO_AUTOPILOT}}` | 高 | |
| 希望単価 | `{{HOURLY_YEN_DRAFT}}` または「要相談」 | 任意 | 未確認の時給を書かない |
| 顔写真 | `{{PHOTO_LOCAL_PATH}}` | 任意 | コミット禁止 |
| プライバシー企業 | `{{BLOCK_COMPANY_NAMES}}` | 任意 | 実名を git に書かない |

公式ヘルプ: 成約後に機密保持契約と三者間の準委任契約。[契約について](https://goworkship.com/help/agreement/105)。**署名画面に本人確認が乗ったら止める**。

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

ここまでやってよい: SNS登録、メール確認、プロフィール、職歴、スキル、ポートフォリオURL。下書き保存。

ここで止める:

- 契約管理の署名で身分証や印鑑証明を求められたとき
- 前払いオプション（ヘルプ: 本人確認が必要）
- 口座・振込先（報酬受け取り / 帳票の振込先）
- マイナンバー
- 成約報告の先の本人確認
- 募集へのエントリー

お祝い金や成約フローは、KYCが出た時点でパック完了。

## thin_site_skip

false。2026-09-16 に https://goworkship.com/signup が HTTP 200。公式ヘルプがアカウント作成手順を掲載。活動ゲート pass。
