> DRAFT-ONLY paste pack. NO secrets. NO browser signup. NO publish.
> Human paste only. Agent does not create accounts.
> `thin_site_skip: false` unless public evidence shows the product is dead.
> Stop at KYC: do not upload ID, My Number, bank, Stripe identity, or e-sign identity contracts.

# CU-17 PACK — ストアカ（Street Academy）講師

| キー | 値 |
|---|---|
| cu_serial | CU-17 |
| inventory | 07 |
| official | https://www.street-academy.com/ |
| register | https://www.street-academy.com/register |
| teach | https://www.street-academy.com/teach |
| help_register | https://support.street-academy.com/hc/ja/articles/360011723660 |
| help_fee | https://support.street-academy.com/hc/ja/articles/200700579 |
| google_signup_preference | **NOT_OFFERED_OAUTH** → Googleメールで「メールアドレスで登録」 |
| thin_site_skip | **false** |
| stop_at_kyc | **STOP**（顔写真付き公的証明書の提出画面） |
| draft | true |

## Google signup preference

公式ヘルプ（PC/スマホ）の新規登録経路: **LINE / Facebook / メールアドレス**。Google OAuth は見当たらない。

このパックの方針:

1. 「メールアドレスで登録」を選ぶ
2. メールは `{{EMAIL}}`（Googleメール）
3. パスワードはローカル台帳。このファイルに書かない
4. LINE と Facebook は、Googleメール経路が死んでいるときだけ

アプリは先生機能なし。ブラウザで登録する（人がやる）。

## 自己集客手数料ノート（公式ヘルプ要約）

出典: [ストアカの手数料・利用料はいくらですか？](https://support.street-academy.com/hc/ja/articles/200700579)  
貼る直前に公式を再読する。ここは下書き。

生徒が**初めて**その先生のサービスを買うとき:

| 経路 | 手数料（公式） |
|---|---|
| **自己集客** | **10%** ※「自己集客URL」経由に限る |
| ストアカ送客・オンライン | 30% |
| ストアカ送客・対面講座 | 20% |

2回目以降（リピーター）: 経路を問わず **一律10%**（公式Q&A）。

運用メモ（登録後、KYC前でもURL発行だけ見るのは可。講座公開は本人判断）:

- 自己集客10%は、SNSやサイトに **自己集客URL** を貼った購入に限る
- 自己集客URLをストアカ内やストアカユーザーへ送って送客手数料を避けることは、公式が禁止
- ユタラボからの流入は自己集客URL前提。ストアカ内SEO流入は30%/20%側

初期費用・月額は、公式の講師募集面では「開催時の手数料のみ」。

## Field map（プレースホルダ）

| 画面の項目（公開情報ベース） | 貼る値 | 必須見込み | メモ |
|---|---|---|---|
| 登録経路 | メールアドレスで登録 | 必須 | Google OAuthなし |
| メール | `{{EMAIL}}` | 必須 | |
| パスワード | ローカルのみ | 必須 | |
| 名前 | `{{DISPLAY_NAME}}` / 先生登録は実名 `{{LEGAL_NAME_KANJI}}` | 必須 | |
| 性別 | `{{GENDER_FORM_VALUE}}` | 生徒登録で出る | 未設定可なら空 |
| 地域 | `{{PREFECTURE}}` | 生徒登録で出る | |
| 興味カテゴリ | ビジネス / IT・プログラミング の最寄り | 任意 | |
| 先生登録: 顔写真 | `{{PHOTO_LOCAL_PATH}}` 本人が特定できる顔 | 必須に近い | コミット禁止 |
| 先生登録: SNSまたはHP | `{{PORTFOLIO_URL}}` | 必須に近い | 顔が確認できる公開ページ |
| 自己紹介 | 下記 200 / 800 | 高 | |
| 本人確認書類 | やらない | STOP | 免許証・マイナンバーカード等 |
| 講座ページ | やらない | 出品STOP | |

公式ヘルプ: 講座作成の前にプロフィール、本人確認、先生ページ。このパックはプロフィール更新まで。本人確認画面は開いたら閉じる。


共通プレースホルダ（実値はローカルの本人台帳だけ。このリポジトリには書かない）:

- `{{LEGAL_NAME_KANJI}}` 戸籍上の氏名（漢字）
- `{{LEGAL_NAME_KANA}}` 氏名カナ
- `{{DISPLAY_NAME}}` 表示名。推奨: `石田祐太`
- `{{EMAIL}}` Googleメール（ログイン用）
- `{{PHONE}}` 日本の携帯電話
- `{{POSTAL_CODE}}` 郵便番号
- `{{PREFECTURE}}` 都道府県
- `{{CITY}}` 市区町村以下
- `{{BIRTH_YEAR}}` / `{{BIRTH_MONTH}}` / `{{BIRTH_DAY}}` 生年月日
- `{{PORTFOLIO_URL}}` 推奨公開: `https://yutalab.dev/`
- `{{GITHUB_URL}}` 推奨公開: `https://github.com/rimone0511`
- `{{GITHUB_REPO_AUTOPILOT}}` `https://github.com/rimone0511/autopilot-log`
- `{{PHOTO_LOCAL_PATH}}` 顔写真のローカルパス（コミット禁止）
- `{{INVITE_CODE}}` 招待コード。無ければ空


## JA bio 200（200字）

```
石田祐太。個人サイト「ユタラボ」（https://yutalab.dev/）で、AI自動化の手順を初心者向け日本語で公開しています。公式APIの動画投稿も扱います。ブラウザ自動操作は教えません。最初の1回を、人が確認できる形で安全に動かすところまで伴走します。公開スイッチは受講者本人が持ちます。未確認の数字は書きません。リモート可。宿題は小さく先に切ります。秘密は貼りません。必ず根拠だけ教えます。
```

## JA bio 800（800字）

```
石田祐太（Yuta Ishida）です。個人サイト「ユタラボ」（https://yutalab.dev/）で、AI自動化の手順を初心者向けの日本語で公開しています。教える範囲は、道具の入れ方から「最初の1回を安全に動かす」までです。専門用語は後回しにし、つまずきやすい場所を先に書きます。教えられること：（1）Claude Code / Codex のはじめ方と、対象ファイル・完成条件・禁止事項を入れた指示の書き方。（2）毎日の作業を自動化してよいかの見分け。秘密・公開・課金が絡む仕事は外す判断。（3）公式APIだけを使う動画投稿の考え方。ブラウザ自動操作やスクレイピングは教えません。（4）動いたあとの検品。仕様、境界値、秘密情報、権限、再現性の順に見ます。公開している教材の土台：ユタラボの実録記事と、Autopilot Log（https://github.com/rimone0511/autopilot-log）。投稿の門番は壊れても非公開側に倒れる設計です。受けないこと：代行ログイン、本人確認の代理、権利のない投稿、未確認の公開、いいね自動化。進め方はチャットまたは非同期テキストです。宿題は小さく切り、合格条件を先に合意します。公開スイッチは受講者本人が持ちます。未確認の受講者数や収益は書きません。公開記事と公開リポジトリを教材の根拠にします。秘密はチャットへ貼らず、本人の画面で入力してもらいます。レッスンはオンライン想定です。録画の外部公開はしません。課題の提出物に秘密を含めないよう、提出前チェックを宿題にします。料金と回数はプラン欄で別途示し、プロフィール本文では約束しません。初回は環境確認から始め、いきなり本番公開へ進みません。止める条件も先に書きます。画面共有なしでも進められます。質問はテキストで残します。未確認の効果は言いません。料金はプラン欄だけに書きます。
```

## STOP-AT-KYC

ここまでやってよい: メール登録、生徒アカウント、先生プロフィール（名前・顔写真・公開URL・自己紹介）。

ここで止める:

- 本人確認（顔写真付き公的証明書 + 顔撮影）
- 口座
- 講座の公開申請（出品）

公開解説では講座3回までに本人確認、という記述もある。登録パックは提出しない。

## thin_site_skip

false。この環境から www.street-academy.com を開くと AWS WAF の Human Verification になる。死滅証拠ではない。公式ヘルプと teach.street-academy.com の講師募集は公開されている。人がブラウザで開けないときだけ SKIP を true に上げる。
