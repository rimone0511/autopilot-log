> DRAFT-ONLY paste pack. NO secrets. NO browser signup. NO publish.
> Human paste only. Agent does not create accounts.
> `thin_site_skip: false` unless public evidence shows the product is dead.
> Stop at KYC: do not upload ID, My Number, bank, Stripe identity, or e-sign identity contracts.

# CU-18 PACK — Shufti / シュフティ（Optional Med）

| キー | 値 |
|---|---|
| cu_serial | CU-18 |
| inventory | 08 |
| priority | **Optional Med** — Top10 と CU-11〜17 の後。売り物（AI自動化）との一致は弱い |
| app | https://app.shufti.jp/ |
| signup | https://app.shufti.jp/signup |
| login | https://app.shufti.jp/login |
| kyc_help | https://help.shufti.jp/support/solutions/articles/158000411414 |
| google_signup_preference | **PREFER_GOOGLE** |
| thin_site_skip | **false** |
| stop_at_kyc | **STOP** |
| draft | true |

## 位置づけ

主婦・在宅ワーク寄りのクラウドソーシング。AI自動化の売り手としては応募対象が細い。Google登録はできるので、Week2の末尾に「任意」で置く。事務入力だけの募集は見送り。

## Google signup preference

優先: 「Googleで登録」。ログイン面も Google / Yahoo! JAPAN ID。

Yahooは使わない。Facebookログインは公開情報では終了済み。

フォールバック: メール登録。メール `{{EMAIL}}`、ユーザー名 `{{DISPLAY_NAME_ASCII}}`（4〜50文字、半角@不可）。ご利用方法は「仕事に参加したい」。ご登録は「個人」。

## Field map（プレースホルダ）

| 画面の項目（公開情報ベース） | 貼る値 | 必須見込み | メモ |
|---|---|---|---|
| 登録経路 | Google | 必須 | |
| メール | `{{EMAIL}}` | メール経路なら必須 | |
| ユーザー名 | `{{DISPLAY_NAME_ASCII}}` | メール経路なら必須 | |
| ご利用方法 | 仕事に参加したい | 必須 | 依頼側にしない |
| 個人/法人 | 個人 | 必須 | |
| 自己紹介 | 下記 200 / 800 | 高 | 事務ではなく自動化設計と書く |
| スキル | 業務自動化, 手順書, API, 技術記事 | 高 | データ入力スキルを盛らない |
| 本人確認資料 | やらない | STOP | |
| 口座 | やらない | STOP | |


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
石田祐太。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIによる業務自動化の手順・つまずき・確認できた結果を、むずかしい言葉を避けて公開しています。公式APIだけを使う動画アップロード道具も公開中です。ブラウザ自動操作はしません。人が検品できる形で、繰り返し作業を自動化します。リモート可。未確認の数字は書きません。公開は人が決めます。秘密は貼りません。根拠を残す方針です。
```

## JA bio 800（800字）

```
石田祐太（Yuta Ishida）です。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIによる業務自動化の手順と失敗談を日本語で公開しています。シュフティでは、在宅の単純事務そのものより、繰り返し作業の自動化設計・手順書・検品を主に出します。ブラウザ自動操作はしません。提供できること：依頼票の切り方、Claude Code / Codex の使い方整理、公式API投稿の仕組み、失敗しやすい鍵と公開設定の点検。公開例：Autopilot Log（https://github.com/rimone0511/autopilot-log）。YouTube Data API と TikTok Content Posting API のみ。門番が壊れたら非公開側に倒れます。受けないこと：スクレイピング、いいね自動化、本人確認書類の代理提出、口座入力の代行、未確認の公開。進め方はテキスト中心、リモート可です。カテゴリが事務中心の案件は、自動化の設計・手順書に読み替えられるものだけ応募します。未確認の件数は書きません。確認できた公開物だけを根拠にします。秘密はチャットに出さず、本人の安全な入力経路だけを使います。日本語でのやり取りを標準にします。納品物は手順書・チェックリスト・動かし方の記録を優先し、ログイン代行はしません。募集文がデータ入力のみで自動化余地がない場合は見送ります。見送り理由は応募文に書きません。単価は募集条件に従い、プロフィールでは約束しません。本人確認と口座登録は出金直前まで進めません。週次の稼働時間は案件ごとに相談します。公開物と矛盾する経歴は書きません。作業記録を残し、公開スイッチは依頼者の手に置きます。未確認のまま納品しません。英語資料は要約して渡します。応募前に募集文と売り物が一致するかだけ見ます。一致しなければ見送ります。これが条件。
```

## STOP-AT-KYC

ここまでやってよい: Google登録、プロフィール、スキル。

ここで止める（公式ヘルプ「本人確認を行う」）:

- ユーザー設定 > 本人確認資料の提出
- 身分証を持った本人画像
- 補助書類（公共料金・住民票）
- 法人用の登記書類
- 口座・出金（振込手数料の公開値あり。出金しない）

## thin_site_skip

false。2026-09-15 に signup HTTP 200。Google登録あり。ヘルプにお知らせ（2026-07 メンテ等）。トップはSPAシェル（約2KB）だが更新日 2026-08-26。死滅ではない。
