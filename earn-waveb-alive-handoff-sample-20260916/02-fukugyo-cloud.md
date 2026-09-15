> DRAFT_ONLY paste pack. NO secrets. NO browser signup from this PR. NO publish.
> CU-ready field map for a later human/CU session. Agent that wrote this pack did not create an account.
> `thin_site_skip: false` unless public evidence shows the product is dead.
> Stop at KYC: do not upload ID, My Number, bank, Stripe identity, or e-sign identity contracts.

# CU-12 PACK — 複業クラウド（旧 Another Works）

| キー | 値 |
|---|---|
| sample_inventory | 02 |
| cu_serial | CU-12（本番直列は Workship の次。このサンプルでは SOKUDAN のあと） |
| activity_gate | **needs_check**（人材トップは SPA。案件の公開日が読めない） |
| self_serve | **yes**（人材ドメイン。面談必須と公開トップに書いていない） |
| cu_ready | **true**（パックあり。登録済みではない） |
| talent | https://talent.aw-anotherworks.com/ |
| company | https://anotherworks.co.jp/ |
| tos | https://cl.aw-anotherworks.com/user_tos |
| google_signup_preference | **PREFER_GOOGLE** ※クリック時にアイコン目視。このGETでは未描画 |
| worker_fee_public | **needs_check**。公開 TOS は事業者の利用料金条。ワーカー％は公式HTMLに出ていない。作らない |
| thin_site_skip | **false** |
| stop_at_kyc | **STOP** |
| draft | true |
| observed | 2026-09-16 公開 GET |

## needs_check

1. **活動** — 個別 `/projects/{id}` のタイトルは求人。本文はローダー。新着日付なし → pass にしない
2. **Google** — 第三者解説は Google / Apple。この環境の人材トップHTMLにボタンなし。CUはサインイン面で Google を目視。無ければメール `{{EMAIL}}`。無いSNSを新規作成しない
3. **ワーカー手数料** — 公式 TOS から％を取れていない。Play / ブログの「無料」をこのパックの確定値にしない

人が公開案件の日付を1画面見てから CU を進める。

## CU handoff（この机）

やってよい（下書きのみ・後続CU）:

1. **人材** https://talent.aw-anotherworks.com/ だけ。`cl.aw-anotherworks.com` の企業デモ・資料は閉じる
2. Google が見えたら Google。初回と違うSNSで入らない
3. プロフィール下書き。公開スイッチがあれば非公開／下書き側
4. エントリーしない

使わない: 企業向け「無料で人材データベースを見てみる」。法人デモ。

## Field map（プレースホルダ）

| 画面の項目（公開情報ベース） | 貼る値 | 必須見込み | メモ |
|---|---|---|---|
| 登録経路 | Google（目視できれば） | 必須 | 見えなければメール |
| メール | `{{EMAIL}}` | 高 | |
| 氏名 | `{{LEGAL_NAME_KANJI}}` | 高 | 公開解説: 氏名欄あり。選考では本名推奨 |
| ニックネーム | `{{DISPLAY_NAME}}` | 画面による | |
| 自己紹介 | 下記 200 / 800 | 高 | テンプレ画面でも自前文 |
| 職種・経験 | 業務自動化 / エンジニア寄り | 高 | |
| スキル | Claude Code, Codex, Python, API, 技術記事, 自動化設計 | 高 | |
| 希望単価 | 空または要相談 | 任意 | 未確認の月額を書かない |
| 稼働 | リモート、週次は要相談 | 任意 | |
| 顔写真 | `{{PHOTO_LOCAL_PATH}}` | 任意 | |
| ポートフォリオ | `{{PORTFOLIO_URL}}` `{{GITHUB_REPO_AUTOPILOT}}` | 任意〜高 | |
| 居住地 | `{{PREFECTURE}}` | 任意 | |
| 転職意向 | 複業・業務委託（転職ではない） | 任意 | 画面の選択肢に合わせる |
| 非表示企業 | `{{BLOCK_COMPANY_NAMES}}` | 任意 | 実名をこのPRに書かない |

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

ここまでやってよい: 人材側の登録、プロフィール下書き、ブロック企業、ポートフォリオURL。

ここで止める:

- 身分証アップロード
- 口座
- 源泉・マイナンバー
- 企業からの契約書で本人確認が必須になった時点
- 案件エントリー

マッチング後の直接契約でも、発注者の本人確認は STOP。

## thin_site_skip

false。2026-09-16 に talent ドメイン HTTP 200。企業 TOS も公開中。SPA で日付が読めないだけ。
