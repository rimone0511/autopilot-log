> DRAFT_ONLY paste pack. NO secrets. NO browser signup from this PR. NO publish.
> CU-ready field map for a later human/CU session. Agent that wrote this pack did not create an account.
> `thin_site_skip: false` unless public evidence shows the product is dead.
> Stop at KYC: do not upload ID, My Number, bank, Stripe identity, or e-sign identity contracts.

# PACK — note（ノート）— this-folder play 1

| キー | 値 |
|---|---|
| inventory | 01 |
| cu_serial | **unindexed**（INDEX CU-01–CU-28 の外。CU番号を作らない） |
| queue | C4 Wave C（日本語デジタル販売。Gumroad の JP 補完） |
| activity_gate | **alive**（PR#22 + このGET: `/` 200, `/signup` 200 タイトル「会員登録」） |
| self_serve | **yes**（公開会員登録面） |
| cu_ready | **true**（パックあり。**登録済みではない**） |
| official | https://note.com/ |
| signup | https://note.com/signup |
| login | https://note.com/login |
| help | https://note.com/help |
| fee_help | https://www.help-note.com/hc/ja → このIPで **403** |
| google_signup_preference | **PREFER_GOOGLE** |
| worker_fee_public | **unknown**。`/help` に有料記事・有料マガジン・メンバーシップの案内のみ。料率表は help-note.com が Cloudflare 403。**率を書かない** |
| thin_site_skip | **false** |
| stop_at_kyc | **STOP** |
| draft | true |
| observed | 2026-09-16 公開 GET |

## needs_check

- `/signup` はこのGETでタイトル以外ほぼ SPA。Google ボタンの確定ラベルは `/login`（`aria-label="Googleでログイン"`、並び: Google / X / Apple / メール）。クリック時に登録面でも同じか目視。
- クリエイター料率（有料記事の分配）。公式ヘルプ本体が 403 のままなら `unknown` のまま。第三者ブログの％を貼らない。
- 有料記事の最低価格。空の必須なら `rate_required`。作らない。

## CU handoff（この机）

やってよい（下書きのみ・後続CU）:

1. https://note.com/signup 。SPA なら https://note.com/login → 「会員登録はこちら」
2. **Googleで登録 / Googleでログイン** as `{{GOOGLE_ACCOUNT_EMAIL}}`。X / Apple は新規作成しない。フォールバック: メール `{{EMAIL}}`
3. 表示名・自己紹介を Field map どおり。プロフィールは **非公開寄り**（公開スイッチがあればオフ）
4. 有料記事を **下書き** まで。価格はプレースホルダ。**公開しない**
5. メンバーシップ / 定期購読マガジンは作っても下書き。**開始しない**
6. **STOP.** 口座・本人確認・振込。応募ものはない（仕事ボードではない）

使わない: 法人向け営業、アフィリエイト専用アカウントの新規作成。

## Field map（プレースホルダ）

| 画面の項目（公開情報ベース） | 貼る値 | 必須見込み | メモ |
|---|---|---|---|
| 登録経路 | Google | 必須 | PREFER_GOOGLE。見えなければメール |
| メール | `{{EMAIL}}` | Googleから来る | 別アドレスを新規作成しない |
| ニックネーム / 表示名 | `{{DISPLAY_NAME}}` | 高 | 公開名 |
| note ID | 画面が自動なら触らない | 画面による | 既存IDをこのPRに書かない |
| 自己紹介 | 下記 200 / 800 | 高 | |
| ウェブサイト | `{{WEBSITE_URL}}` | 任意 | `https://yutalab.dev/` |
| ヘッダー / アイコン | `{{PROFILE_PHOTO_LOCAL_PATH}}` | 任意 | 顔。身分証の切り抜き禁止 |
| 有料記事タイトル | 下記 | 下書き | **公開しない** |
| 有料記事本文 | 下記 | 下書き | 秘密・鍵・実メールを書かない |
| 価格 | `{{NOTE_PAID_PRICE_JPY}}` | 画面が必須なら | 空なら `rate_required` |
| メンバーシップ料金 | 空 | 起動しない | |

共通プレースホルダは [INDEX.md](INDEX.md)。

## JA bio 200（200字）

```
石田祐太。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIによる業務自動化の手順・つまずき・確認できた結果を、むずかしい言葉を避けて公開しています。公式APIだけを使う動画アップロード道具も公開中です。ブラウザ自動操作はしません。人が検品できる形で、繰り返し作業を自動化します。リモート可。未確認の数字は書きません。公開は人が決めます。秘密は貼りません。根拠を残す方針です。
```

## JA bio 800（800字）

```
石田祐太（Yuta Ishida）です。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIを使って毎日の作業を自動化する手順、つまずいた点、確認できた結果を、むずかしい言葉を避けて公開しています。売り物は「動いたように見える自動化」ではなく、人が検品できる仕組みです。公開している実録と道具を、業務委託の成果物の根拠にします。提供できること：（1）繰り返し作業の自動化設計。目的・範囲・合格条件・停止条件を先に切り、実装後に回帰確認まで残します。（2）Claude CodeやCodexなど、AIに実装を任せるときの指示の書き方、検品、失敗時の切り分け。（3）YouTubeとTikTokへの公式API投稿の仕組みづくり。ブラウザ自動操作とスクレイピングは対象外です。（4）鍵の扱い、公開事故、トークン期限など、自動化が止まりやすい箇所の点検。公開している道具の例：Autopilot Log（https://github.com/rimone0511/autopilot-log）。YouTube Data API v3 と TikTok Content Posting API のみを使い、投稿の門番は壊れても非公開側に倒れます。受けないこと：いいねやフォローの自動化、権利のない投稿代行、本人確認書類・口座・マイナンバーの代理入力、未確認のままの公開。進め方はテキスト中心です。根拠と反証を残し、公開スイッチは依頼者または本人の手に置きます。リモート可。週次の稼働時間は案件ごとに相談します。未確認の件数や年数は書きません。確認できた公開物だけを貼ります。秘密はチャットに出さず、本人の安全な入力経路だけを使います。日本語でのやり取りを標準にします。英語の一次資料は必要なら要約して渡します。契約前に範囲外を一文で確定します。納期は着手前に合意します。作業の記録を残す。
```

## 有料記事下書き（公開しない）

タイトル:

```
人が検品できる業務自動化の残し方（n8n / 公式API）
```

本文（短文。価格はプレースホルダ）:

```
ユタラボの石田祐太です。このノートは下書きです。公開は人が決めます。

内容の予定:
- 繰り返し作業を自動化するときの切り方（目的・範囲・合格条件・停止）
- n8n や公式APIで残すものと、ブラウザ自動操作でやらないもの
- 公開している道具 Autopilot Log の門番（壊れても非公開側）

価格は {{NOTE_PAID_PRICE_JPY}}。未確認の「月収」は書きません。秘密と鍵は貼りません。
```

## STOP-AT-KYC

ここまでやってよい: Google登録、プロフィール、有料記事の下書き保存。

ここで止める:

- 口座・振込先・本人確認書類
- 有料記事 / プロフィール / メンバーシップの **公開**
- help-note.com が読めないまま料率を書くこと
- 別 Google / 別メールの新規作成

書類提出を求められたらパック完了扱い。

## thin_site_skip

false。2026-09-16 に `/signup` HTTP 200。`/login` に Google ボタン。トップは公開ノートの生存面（PR#22 `publishAt` 2026-09-14 / 15）。
