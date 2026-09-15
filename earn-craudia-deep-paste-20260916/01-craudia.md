# CU-09 — クラウディア（Craudia）worker desk

Desk: クラウディア / Craudia  
Role: **ワーカー**。クライアント募集画面に入らない  
Official: https://www.craudia.com/  
Worker LP: https://www.craudia.com/worker  
CU serial: **CU-09**（QUEUE **A9**）  
Checked: 2026-09-16（公開 HTML / 公式 FAQ / 手数料ガイド HTTP 200。**登録していない**）  
Mode: **DRAFT_ONLY** — fill, save, **never apply / never スキル出品 / never KYC upload**  
Language: **日本語**  
Google: **PREFER_GOOGLE**  
OTP: Rare with Google. Else **Gmail parent**（i2iID 認証メール）  
plan: 会員登録は公式「無料」。**Craudia PRO に入らない**  
`thin_site_skip: false`

---

## 0. How far to go (then stop)

1. https://www.craudia.com/worker または https://www.craudia.com/app/auth/register-temp — **ワーカー**。クライアント CTA「仕事を依頼」は使わない。
2. **Google**（MAIN）。ダメなら同じ MAIN メールで仮登録。Twitter / Facebook / Yahoo を新規身分にしない。
3. **この authoring セッションでは「無料で会員登録する（仮登録）」を押さない。** CU 直列だけ。reCAPTCHA は人待ち。
4. プロフィール / 基本情報 / 自己紹介 / **スキル欄**（実務があるものだけ）。FAQ 92: マイページ設定「プロフィール編集」。
5. 公開設定があれば非公開。無ければ埋めるだけにして、ワーカー一覧への露出を増やす操作（出品・応募）をしない。
6. **仕事に応募しない。スキルを出品しない。** ワーカー LP の3系統（公募応募 / スキル出品 / PRO オファー）はすべてこのパックの外。
7. 本人確認画面は **開いて種類だけ確認して閉じる**。書類も**自撮り**も上げない。朝の本人へパス。[STOP-KYC.md](STOP-KYC.md)。
8. 口座・出金・電話認証が取引チャット必須でも、今は取引しない。SMS が登録そのものを止めるときだけユーザーチャット待ち。

やらない: 参加申請、納品する、スキル公開、紹介料設定、Craudia PRO、クライアント仮払い画面。

Timebox: 15–25 minutes. Stuck > 10 minutes: park.

---

## 1. URLs

### Confirmed (use these)

| What | URL |
|---|---|
| Home | https://www.craudia.com/ |
| Worker LP | https://www.craudia.com/worker |
| 会員登録（仮登録） | https://www.craudia.com/app/auth/register-temp |
| ログイン | https://www.craudia.com/login |
| 会員登録の方法 | https://www.craudia.com/app/faq/contents/151 |
| 登録に必要なもの | https://www.craudia.com/app/faq/contents/103 |
| プロフィール編集 | https://www.craudia.com/app/faq/contents/92 |
| ポートフォリオ | https://www.craudia.com/app/faq/contents/78 |
| 本人確認 | https://www.craudia.com/app/faq/contents/93 |
| 手数料 FAQ | https://www.craudia.com/app/faq/contents/72 |
| 手数料ガイド（cited 階段） | https://www.craudia.com/app/guide/crowdsourcing-price |
| スキル販売手数料（出品しない） | https://www.craudia.com/app/guide/skill-price |
| 直接取引 | https://www.craudia.com/faq/contents/164 |
| 直接連絡 | https://www.craudia.com/app/faq/contents/140 |
| 参加申請（送らない） | https://www.craudia.com/app/faq/contents/89 |
| スキル出品方法（入らない） | https://www.craudia.com/app/faq/contents/175 |
| スキル出品ガイド（公開しない） | https://www.craudia.com/app/guide/service/sell |
| ワーカーガイド | https://www.craudia.com/app/guide/crowd-sourcing/worker |
| 規約 | https://www.craudia.com/app/agreement |
| ガイドライン | https://www.craudia.com/project_guideline |
| 出金（開かない） | https://www.craudia.com/app/faq/contents/110 |
| 振込手数料（cited, unused） | https://www.craudia.com/app/faq/contents/39 |
| 電話認証 | https://www.craudia.com/app/faq/contents/156 |
| 年齢 | https://www.craudia.com/app/faq/contents/47 |
| ワーカー一覧（SPA。件数は書かない） | https://www.craudia.com/app/user_list |

### Guess only

```
{{URL_GUESS_CRAUDIA_PROFILE_EDIT}}     # FAQ 92: マイページ設定「プロフィール編集」。ライブメニューを正とする
{{URL_GUESS_CRAUDIA_I2I_CALLBACK}}     # i2i OAuth コールバックを発明しない
{{SIGNUP_URL_GUESS_CRAUDIA_CLIENT}}    # mypage/work/register — 選ばない
{{SIGNUP_URL_GUESS_CRAUDIA_SKILL_ADD}} # mypage/services/add — 選ばない
{{URL_GUESS_CRAUDIA_PRO_SIGNUP}}       # LP は confirmed。登録完了 URL は発明しない
```

`/signup` と `/app/signup` は this env **404**。register-temp を使う。

---

## 2. Google MAIN notes (this desk)

公開観測:

- FAQ 151: PC メール **または** Twitter / facebook / Google / Yahoo!。外部サービスの写真もプロフィールに使える、とある。Google 写真を身分証の代わりにしない。
- register-temp GET 200: 「SNSアカウントで登録する」に Google ボタン（`auth=3`）。注記「連携先はi2i IDと表示されます。」規約・i2iID 規約・個人情報保護方針への同意みなし。
- メール経路の公式フロー: 認証メール → クリック（i2iID）→ クラウディアでプロフィール → 登録完了。
- 画面 STEP4 は「取引開始」。このパックは STEP3 基本情報 / プロフィールで止まる。

方針:

1. https://www.craudia.com/app/auth/register-temp
2. **Google** as `rimone0511@gmail.com`
3. フォールバック: メール = 同じ MAIN Gmail。OTP は親 Gmail。
4. Twitter / Facebook / Yahoo を新規紐付けしない。
5. パスワード経路なら `{{PASSWORD_DO_NOT_STORE}}`。git に残さない。
6. **この authoring セッションでは仮登録ボタンを押さない。** CU 直列だけ。
7. Already a member: ログイン。二件目を作らない。
8. クライアント / PRO / スキル出品に落ちたらワーカープロフィールへ戻す。

---

## 3. Profile paste fields (JP)

出典: FAQ 92 / 78 / 103 / 151、ワーカー LP、user_list meta、規約。**カウンターと必須マークは画面を正とする**。公開ワーカー詳細は this env が SPA シェルのため、個別欄名はライブフォーム。

| 画面の項目 | 貼る値 | 必須見込み | メモ |
|---|---|---|---|
| 登録経路 | Google | 必須 | PREFER_GOOGLE。i2i `auth=3` |
| メール | `{{GOOGLE_ACCOUNT_EMAIL}}` | Google から / メール経路 | FAQ 103: PC メールがあれば登録可 |
| パスワード | `{{PASSWORD_DO_NOT_STORE}}` | メール経路 | git に書かない |
| 氏名 | `{{LEGAL_NAME_KANJI}}` | 高 | 規約: 会員連絡先情報 |
| 氏名カナ | `{{LEGAL_NAME_KANA}}` | 高 | |
| ニックネーム / 表示 | `{{DISPLAY_NAME}}` | 高 | 推奨: `石田祐太` |
| 生年月日 | `{{BIRTH_YEAR}}` / `{{BIRTH_MONTH}}` / `{{BIRTH_DAY}}` | 高 | FAQ 47: 満18歳以上 |
| 居住地 | `{{PREFECTURE}}` `{{CITY}}` | 高 | 番地は出さなくてよい画面なら市区まで。git に番地を書かない |
| 電話 | `{{PHONE}}` | 画面が必須なら | git に実番号を残さない。OTP なら SMS=user |
| 業種 / 職種 | エンジニア / 自動化 / 業務改善の最寄り | 高 | 「AI」だけにしない |
| 状況 | 個人・副業など画面の事実 | 高 | 法人を名乗らない。雇用を創作しない |
| キャッチ | 下記 **23** | 任意〜高 | 公式字数 **needs_check** |
| 自己紹介 | 下記 200 / 255 / 800 を画面上限で切る | 高 | 公式字数 **needs_check** |
| 得意種別 | **プログラム・開発系** が最寄り | 高 | user_list meta の分類。ライブに同じラベルが無ければ最寄り |
| 得意カテゴリ / タグ | IT・自動化の公式チップだけ | 任意 | `https://www.craudia.com/app/user_list/tags/IT` はタグページとして存在。無いチップを作らない |
| スキル（プロフィール） | 下記スキルリスト | 高 | **出品ではない。** 未経験を経験と書かない |
| 職歴 | 公開実録の期間だけ。`{{YEARS_AUTOMATION_PUBLIC}}` | 任意 | 空可。年数創作禁止 |
| 資格 | 空（未確認なら） | 任意 | 持っていない資格を書かない |
| ポートフォリオ | `{{PORTFOLIO_URL}}` `{{GITHUB_REPO_AUTOPILOT}}` | 任意〜高 | FAQ 78: 公開可能なもの。身分証を置かない |
| サムネイル | `{{PHOTO_LOCAL_PATH}}` | 任意 | 身分証・自撮り KYC 写真は不可 |
| 稼働時間 | 空、または「案件ごとに相談・リモート」 | 任意 | 週次時間を創作しない |
| 時給 | `{{HOURLY_JPY}}` | 完成チェック用なら | **git に実額を書かない。** 空で保存。必須で台帳が空なら `rate_empty` |
| SNS / LINE / メール本文 | 空 | STOP | ガイドライン: 連絡先投稿 NG |
| 公開設定 | 非公開 / 非表示 | 必須（あれば） | トグルが無ければ needs_check。露出を増やす操作はしない |
| スキル出品 | 作らない | STOP | FAQ 175。タイトル 25 字ルールは使わない |
| 参加申請 | 送らない | STOP | FAQ 89 |
| 本人確認 | やらない | STOP | パスだけメモ。自撮り含む |
| 口座 / 出金 | やらない | STOP | FAQ 110 |
| Craudia PRO | やらない | STOP | LP の時給例を貼らない |

共通プレースホルダ（実値はローカル台帳。このリポジトリには書かない）は README と同じ。

---

## 4. Paste — bio lengths（測済み）

公式 FAQ に自己紹介の最大字数は無い（**needs_check**）。CU は画面カウンターを正とする。超過したら短いフェンスへ降りる。URL も字数に含む。

### キャッチ（23 字。短い欄）

```
公式API自動化と手順書。支払いはサイト内です
```

画面が更に短いときは「公式API自動化と手順書」まで。連絡先を足さない。

### JA bio 200（自己紹介の既定）

```
石田祐太。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIによる業務自動化の手順・つまずき・確認できた結果を、むずかしい言葉を避けて公開しています。公式APIだけを使う動画アップロード道具も公開中です。ブラウザ自動操作はしません。人が検品できる形で、繰り返し作業を自動化します。リモート可。未確認の数字は書きません。やり取りはクラウディア内です。秘密は貼りません。方針です。
```

### JA bio 255（カウンターが 255 前後のとき）

```
石田祐太。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIによる業務自動化の手順・つまずき・確認できた結果を公開しています。公式APIだけを使う動画アップロード道具も公開中です。ブラウザ自動操作・いいね自動化はしません。人が検品できる形で、繰り返し作業を自動化します。リモート可。未確認の数字は書きません。やり取りと支払いはクラウディア内です。直接取引はしません。秘密は貼りません。公開は人が決めます。スキル出品と応募はしません。検品できる形です。作業記録を残す方針です。下書きです。
```

### JA bio 800（カウンターがそれ以上のときだけ。切って使う）

```
石田祐太（Yuta Ishida）です。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIを使って毎日の作業を自動化する手順、つまずいた点、確認できた結果を、むずかしい言葉を避けて公開しています。売り物は「動いたように見える自動化」ではなく、人が検品できる仕組みです。公開している実録と道具を、業務委託の成果物の根拠にします。提供できること：（1）繰り返し作業の自動化設計。目的・範囲・合格条件・停止条件を先に切り、実装後に回帰確認まで残します。（2）Claude CodeやCodexなど、AIに実装を任せるときの指示の書き方、検品、失敗時の切り分け。（3）YouTubeとTikTokへの公式API投稿の仕組みづくり。ブラウザ自動操作とスクレイピングは対象外です。（4）鍵の扱い、公開事故、トークン期限など、自動化が止まりやすい箇所の点検。公開している道具の例：Autopilot Log（https://github.com/rimone0511/autopilot-log）。YouTube Data API v3 と TikTok Content Posting API のみを使い、投稿の門番は壊れても非公開側に倒れます。受けないこと：いいねやフォローの自動化、権利のない投稿代行、本人確認書類・口座・マイナンバーの代理入力、クラウディア外の直接支払い、未確認のままの公開。進め方はテキスト中心です。根拠と反証を残し、公開スイッチは依頼者または本人の手に置きます。リモート可。週次の稼働時間は案件ごとに相談します。未確認の件数や年数は書きません。確認できた公開物だけを貼ります。秘密はチャットに出さず、本人の安全な入力経路だけを使います。日本語でのやり取りを標準にします。契約前に範囲外を一文で確定します。納期は着手前に合意します。支払いはクラウディア内のみです。
```

`{{TIMEZONE}}` を画面が別欄で求めるときは `Asia/Tokyo`。git に住所を足さない。

---

## 5. Skills（プロフィール欄のみ。出品しない）

二つの「スキル」を混ぜない。

| 系統 | このパック | 公式 |
|---|---|---|
| プロフィールの得意種別・スキル・特技 | **貼ってよい** | user_list meta の得意種別。FAQ 78 は実績の見せ方 |
| スキル販売（商品として出品・公開） | **STOP** | FAQ 175。ガイド: タイトル 25 文字以内、ステップ8 公開。手数料は skill-price（同じ階段）だが払う取引を始めない |

### 5a. 得意種別

公開一覧 meta（2026-09-16）: ライティング系、デザイン・クリエイティブ系、**プログラム・開発系**、事務系、その他。

選ぶ: **プログラム・開発系**。ライブのラベルが「IT」「システム」ならその最寄り。複数可なら業務改善寄りの公式チップだけ追加。未経験カテゴリを満点にしない。

### 5b. プロフィールに書くスキル（実務があるものだけ）

画面がチップ選択なら存在するチップだけ。自由記述なら次を **1行ずつ**。無いものは書かない。

```
業務自動化
n8n
Python
Claude Code
Codex
YouTube Data API v3
TikTok Content Posting API
手順書
公式API
```

英語ラベルしか無い画面:

```
Automation
n8n
Python
Claude Code
Official APIs
```

年数・「○件納品」は `{{YEARS_AUTOMATION_PUBLIC}}` が空なら書かない。

### 5c. ポートフォリオ1行（FAQ 78）

| Sample | URL | Title line |
|---|---|---|
| 1 | `{{PORTFOLIO_URL}}` | ユタラボ — AI業務自動化の手順と確認できた結果（公開） |
| 2 | `{{GITHUB_REPO_AUTOPILOT}}` | Autopilot Log — YouTube Data API v3 + TikTok Content Posting API（公開ゲートは非公開側に倒れる） |

Do not upload private videos, client files, ID, or a KYC selfie.

### 5d. スキル出品画面に入ったら

1. 戻る。公開しない。
2. タイトル 25 字の下書きを作らない（公開導線）。
3. Log `skill_listing: no`。
4. プロフィールに戻れるなら戻る。戻れなければ `done-draft` if profile already saved, else `no_draft_path`.

---

## 6. Fees and rate placeholders — official public pages only

時給欄に入れるのは **`{{HOURLY_JPY}}` だけ**。業界平均・PRO LP の例時給をこのパックが決めてはいけない。この GO は採用も出金もしないので、手数料入力欄は触らない。

| Claim | Status | Source | Quote / note |
|---|---|---|---|
| 会員登録は無料 | **cited** | トップ「会員登録(無料)」。規約第10条1 https://www.craudia.com/app/agreement | 「会員登録、仕事の依頼・登録、仕事の提案、納品物の提供をすべて無料」 |
| システム利用料は採用時のみ | **cited** | FAQ 72 https://www.craudia.com/app/faq/contents/72 | 「ワーカーが仕事を納品し採用された場合にのみ発生」 |
| 5万円まで一律 15% | **cited** | FAQ 72 | 「金額は5万円までは一律15%」 |
| ワーカー負担 3〜15%（税込） | **cited** | 規約第10条3 | 「報酬の3～15%（消費税込）」 |
| 階段（クラウドソーシング） | **cited** | https://www.craudia.com/app/guide/crowdsourcing-price | 1円〜5万 **15%** / 5万1円〜10万 **10%** / 10万1円〜100万 **5%** / 100万1円以上 **3%**。時間制 **一律 10%**。税込。％計算は四捨五入。改訂あり得る |
| クライアントのシステム手数料 0円 | **cited** | 同ガイド | ワーカー側の話として読む。クライアント有料オプションは触らない |
| スキル販売者も同じ階段 | **cited but unused** | https://www.craudia.com/app/guide/skill-price | 出品しないので「今払う額」にしない |
| 出金振込 一律 300円 | **cited but unused** | FAQ 39 https://www.craudia.com/app/faq/contents/39 | 出金しない。詳細ページはログイン後 |
| 仮払い（エスクロー） | **cited but unused** | FAQ 66 | 取引開始前。このパックは取引しない |
| 直接取引の違約金 | **cited (warning only)** | 規約第12条5 | 報酬の 30%、下限 100万円。プロフィールに数字を貼らない |
| Craudia PRO のプラン価格 | **needs_check** | LP https://www.craudia.com/app/lp/professional | 「時給5,000円以上」等は案件例。プラン料金としては使わない。**買わない** |
| 自己紹介の字数 | **needs_check** | FAQ 92 / 78 | 数字なし。画面カウンター |
| スキル出品タイトル 25 字 | **cited, unused** | 出品ガイド | 出品しない |
| 時給の実額 | **placeholder** | 時間制の提案欄など | `{{HOURLY_JPY}}`。空で保存。必須で台帳が空なら **`rate_empty`** |

Do not paste the fee ladder into the bio. Do not use PRO LP sample rates as a recommended price.

---

## 7. Explicit do-not (this desk)

- クライアントとして仕事を依頼する
- 参加申請 / 納品する / 見積もり提案
- スキルを出品する / スキルを公開する / 紹介料を設定する
- Craudia PRO に登録する
- 本人確認アップロード（書類・自撮り）
- 口座・振込依頼・出金
- プロフィールにメール・電話・LINE・「この口座へ」
- 手数料％や時給を創作してコミットすること
- Twitter / Facebook / Yahoo を新規身分にする
- この authoring エージェントが `register-temp-post` を送ること

---

## 8. What success looks like **before stop**

| Outcome | Meaning |
|---|---|
| `done-draft` | MAIN Google（または同じメール）。ワーカープロフィール下書き。スキル欄のみ。応募なし。出品なし。KYC なし |
| `already_member_draft` | 同じメールで既存。プロフィール確認。PRO に上げない |
| `kyc_wait` | 本人確認（書類+自撮り）。閉じて朝へ |
| `rate_empty` | 時給必須で台帳が空。円を創作せず停止 |
| `card_wall` | PRO / 有料オプションがカードを要求。閉じる |
| `otp_missing` | メール確認なし |
| `sms_wait_user` | 電話認証が下書きを止める。ユーザー待ち |

```
desk: Craudia
pack: earn-craudia-deep-paste-20260916/01-craudia.md
auth: google-main | email-same-mailbox | already_member | blocked
otp: gmail-parent | sms-chat | none | otp_missing | sms_wait_user
kyc: none | wait-morning + person_confirm_selfie
draft_profile: yes/no
ticket_or_page: craudia-worker-profile
skill_listing: no
async_only: n/a
pro_upgrade: no
publish: no
apply: no
rate: empty | placeholder-from-ledger | rate_empty
next: stop
```
