> DRAFT-ONLY paste pack. NO secrets. NO browser signup. NO publish.
> Human paste only. Agent does not create accounts.
> `thin_site_skip: false` unless public evidence shows the product is dead.
> Stop at KYC: do not upload ID, My Number, bank, Stripe identity, or e-sign identity contracts.

# CU-16 PACK — MENTA（メンター登録）

| キー | 値 |
|---|---|
| cu_serial | CU-16 |
| inventory | 06 |
| official | https://menta.work/ |
| register | https://menta.work/index.php/register/choose |
| google_oauth | https://menta.work/index.php/oauth/google |
| mentor | https://menta.work/about_mentor |
| kyc_help | https://intercom.help/mentajp/ja/articles/3025561 |
| tokutei | https://menta.work/tokutei |
| google_signup_preference | **PREFER_GOOGLE** |
| thin_site_skip | **false** |
| stop_at_kyc | **STOP**（Stripe本人確認の直前） |
| fee_public | 特商法: メンター手数料は報酬の20%税別（利用15%+決済5%）。出金都度300円 |
| draft | true |

## Google signup preference

優先: 「Googleアカウントで登録する」。

他経路（メール / X / Facebook / Apple / Lancers）は使わない。Googleで揃える。

メンタープランの提出はプロフィール後。プラン公開は運営チェック。**プラン提出はKYCではない**が、公開＝出品なので、このパックの完了条件は「プロフィール保存まで」。プラン提出は本人が別判断。エージェントは出品しない。

## Field map（プレースホルダ）

| 画面の項目（公開情報ベース） | 貼る値 | 必須見込み | メモ |
|---|---|---|---|
| 登録経路 | Google | 必須 | |
| ユーザー名 | `{{DISPLAY_NAME}}` または画面の英数制限に合わせる | 高 | |
| アイコン | `{{PHOTO_LOCAL_PATH}}` | 任意 | |
| 自己紹介 | 下記 200 / 800 | 必須に近い | メンター向け公式が詳細記入を案内 |
| 経歴・実績 | 公開記事と公開リポジトリのみ | 高 | 受講者数を作らない |
| 教えられること | Claude Code, Codex, 自動化の始め方, 公式API投稿, 検品 | 高 | |
| 教え方 | テキスト中心、宿題を小さく切る、公開スイッチは受講者 | 高 | |
| プラン名 | このパックでは空。出品しない | STOP | |
| プラン料金 | 空 | STOP | |
| Stripe本人確認 | やらない | STOP | |
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
石田祐太。個人サイト「ユタラボ」（https://yutalab.dev/）で、AI自動化の手順を初心者向け日本語で公開しています。公式APIの動画投稿も扱います。ブラウザ自動操作は教えません。最初の1回を、人が確認できる形で安全に動かすところまで伴走します。公開スイッチは受講者本人が持ちます。未確認の数字は書きません。リモート可。宿題は小さく先に切ります。秘密は貼りません。必ず根拠だけ教えます。
```

## JA bio 800（800字）

```
石田祐太（Yuta Ishida）です。個人サイト「ユタラボ」（https://yutalab.dev/）で、AI自動化の手順を初心者向けの日本語で公開しています。教える範囲は、道具の入れ方から「最初の1回を安全に動かす」までです。専門用語は後回しにし、つまずきやすい場所を先に書きます。教えられること：（1）Claude Code / Codex のはじめ方と、対象ファイル・完成条件・禁止事項を入れた指示の書き方。（2）毎日の作業を自動化してよいかの見分け。秘密・公開・課金が絡む仕事は外す判断。（3）公式APIだけを使う動画投稿の考え方。ブラウザ自動操作やスクレイピングは教えません。（4）動いたあとの検品。仕様、境界値、秘密情報、権限、再現性の順に見ます。公開している教材の土台：ユタラボの実録記事と、Autopilot Log（https://github.com/rimone0511/autopilot-log）。投稿の門番は壊れても非公開側に倒れる設計です。受けないこと：代行ログイン、本人確認の代理、権利のない投稿、未確認の公開、いいね自動化。進め方はチャットまたは非同期テキストです。宿題は小さく切り、合格条件を先に合意します。公開スイッチは受講者本人が持ちます。未確認の受講者数や収益は書きません。公開記事と公開リポジトリを教材の根拠にします。秘密はチャットへ貼らず、本人の画面で入力してもらいます。レッスンはオンライン想定です。録画の外部公開はしません。課題の提出物に秘密を含めないよう、提出前チェックを宿題にします。料金と回数はプラン欄で別途示し、プロフィール本文では約束しません。初回は環境確認から始め、いきなり本番公開へ進みません。止める条件も先に書きます。画面共有なしでも進められます。質問はテキストで残します。未確認の効果は言いません。料金はプラン欄だけに書きます。
```

## STOP-AT-KYC

ここまでやってよい: Google登録、プロフィール、自己紹介。

ここで止める:

- 設定 → 本人確認ページ（Stripe）
- 銀行口座
- 出金申請
- プラン公開（出品）。本人が別途決めるまで触らない

公式: 出金は売上1,000円超かつ入金から30日、事前に本人確認と口座が必要。だから登録パックはプロフィールで終わり。

## thin_site_skip

false。2026-09-15 に register/choose が HTTP 200。Google OAuth リンクあり。運営はランサーズ株式会社（特商法）。
