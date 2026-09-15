# CHECKLIST — クラウディア live register (field-by-field)

> **DRAFT_ONLY.** JP OK. No secrets.  
> Computer-use（CU）直列用。このフォルダを書いているエージェントは **登録していない / POST していない**。  
> Live form wins. 公開ヘルプに無いラベルは `needs_check`。

Pack date: **2026-09-16**  
Folder: `ops/earn/craudia-live-checklist-20260916/`  
Desk: クラウディア / Craudia — **ワーカー（出品者側）**  
CU serial: **CU-09** / QUEUE **A9**  
Host: `www.craudia.com` / `app.craudia.com`（誤綴り `craudia.jp` は使わない）  
Google: **PREFER_GOOGLE**（MAIN のみ）  
OTP: [OTP-NOTE.md](OTP-NOTE.md) — **Gmail OTP allowed. SMS skip.**  
Desk box: [STATUS.md](STATUS.md)

Ordered pass: **register-temp → 基本情報 / プロフィール → スキル下書き**  
Hard stop: **公開 / 本人確認 / NDA**（入らない。誘導されたら閉じる）

Tick boxes on a **local** copy. Do not commit filled legal name, phone, OTP, ID, or a live Craudia skill URL.

---

## Complement (do not copy sibling bodies)

This pack is the **live field order**. Paste fences live in siblings. Point, do not duplicate.

| Sibling | Path | PR | This pack adds |
|---|---|---|---|
| Thin CU-09 | `earn-timeticket-contra-craudia-handoff-20260916/09-craudia.md` | [#18](https://github.com/rimone0511/autopilot-log/pull/18) | Ordered ticks; skill **draft** fill |
| Deep worker paste | `earn-craudia-deep-paste-20260916/` | [#51](https://github.com/rimone0511/autopilot-log/pull/51) | Live register order; SMS **skip** (sibling may wait SMS if draft is blocked) |
| Seller CU handoff | `ops/earn/craudia-cu-handoff-20260916/` | [#60](https://github.com/rimone0511/autopilot-log/pull/60) | Skill-form fields through ステップ7; stop at ステップ8 **公開** |
| Morning KYC 1枚 | `earn-kyc-morning-checklist-20260916/` | [#4](https://github.com/rimone0511/autopilot-log/pull/4) | This pack does **not** open 本人確認 even to “note the type” |

Siblings say スキル出品しない. This pack **enters** the skill form, fills a **draft**, and **stops before 公開**. If the live form has no 下書き保存, fill then leave without 公開 (`skill_draft_no_save_path`).

---

## 0. Hard stop (read before opening Craudia)

- [ ] Role = **ワーカー / 仕事を受ける**. クライアント「仕事を依頼」に入らない。
- [ ] MAIN Google only (`{{GOOGLE_ACCOUNT_EMAIL}}`). Twitter / Facebook / Yahoo を新規身分にしない。
- [ ] **Gmail OTP allowed** via parent MCP. CU は `mail.google.com` を開かない。[OTP-NOTE.md](OTP-NOTE.md)
- [ ] **SMS skip.** 電話認証・050 発信・番号入力をこのパックではやらない。止められたら park。
- [ ] **公開**しない（プロフィール公開トグル / スキル **公開** / ワーカー一覧の露出操作）。
- [ ] **本人確認**に入らない（書類・自撮り・マイナンバー）。
- [ ] **NDA** に同意しない（秘密保持契約 / クローズド案件承諾 / オプション非公開の閲覧同意 / スカウト受諾に付く機密）。
- [ ] 参加申請しない。見積もり提案しない。Craudia PRO に入らない。口座・出金しない。
- [ ] 手数料％・時給円額を創作してコミットしない。`{{HOURLY_JPY}}` は空。
- [ ] この authoring エージェントは `register-temp` を **POST しない**。CU serial だけがタイプする。

やらない（一覧）: 第二アカウント、クライアント募集、納品する、紹介料オン、カード、連絡先をプロフィールに書く、手数料シミュレータの数字を bio に貼る。

---

## 1. Preflight

- [ ] You are the **CU serial** for this desk, not the pack-author.
- [ ] Viewport desktop ≥ 1280px. One marketplace profile. Do not also live in Gmail in that profile.
- [ ] Previous CU left a different Google user → sign **out**, then `rimone0511`.
- [ ] Timebox 15–25 min. 1モーダル 10 min 超えたら park.
- [ ] `/signup` と `/app/signup` は 404。入口は **register-temp**。
- [ ] 既存会員なら **ログイン**（`already_member_draft`）。二件目を作らない。

Confirmed public GET (authoring session 2026-09-16, **no POST**):

| What | URL |
|---|---|
| 会員登録（仮登録） | https://www.craudia.com/app/auth/register-temp |
| ログイン | https://www.craudia.com/login → `app.craudia.com/auth/login-form` |
| 会員登録の方法 | https://www.craudia.com/app/faq/contents/151 |
| 登録に必要なもの | https://www.craudia.com/app/faq/contents/103 |
| 年齢 | https://www.craudia.com/app/faq/contents/47 |
| プロフィール編集（FAQ 見出し） | https://www.craudia.com/app/faq/contents/92 |
| ポートフォリオ | https://www.craudia.com/app/faq/contents/78 |
| 電話認証（**skip**） | https://www.craudia.com/app/faq/contents/156 |
| 本人確認（**入らない**） | https://www.craudia.com/app/faq/contents/93 |
| スキル出品方法（下書きまで） | https://www.craudia.com/app/faq/contents/175 |
| スキル出品ガイド | https://www.craudia.com/app/guide/service/sell |
| スキル手数料（**cited unused**） | https://www.craudia.com/app/guide/skill-price |
| 参加申請（**送らない**） | https://www.craudia.com/app/faq/contents/89 |
| 直接取引 | https://www.craudia.com/faq/contents/164 |
| 規約 | https://www.craudia.com/app/agreement |
| ガイドライン | https://www.craudia.com/project_guideline |
| Crarepo プロフィール | https://www.craudia.com/crarepo/archives/3678 |

Guess only — do not type unless the live page shows them:

```
{{URL_GUESS_CRAUDIA_PROFILE_EDIT}}      # FAQ 92: マイページ設定「プロフィール編集」
{{URL_GUESS_CRAUDIA_BASIC_INFO}}        # 「基本情報はこちら / 基本情報更新」
{{SIGNUP_URL_GUESS_CRAUDIA_CLIENT}}     # mypage/work/register — 選ばない
{{SIGNUP_URL_GUESS_CRAUDIA_SKILL_ADD}}  # mypage/services/add — 入って下書きのみ。公開しない
{{URL_GUESS_CRAUDIA_PRO_SIGNUP}}        # 使わない
{{URL_GUESS_CRAUDIA_PERSON_CONFIRM}}    # mypage/setting/person — 入らない
```

---

## 2. register-temp（STEP1 仮登録）

Open: https://www.craudia.com/app/auth/register-temp  

画面ウィザード（GET 200、2026-09-16）:

| STEP | ラベル | このパック |
|---|---|---|
| STEP1 | 仮登録 約10秒 | **いまここ**（Google 優先） |
| STEP2 | 会員登録 約20秒 | i2i 後に通る。ライブを正とする |
| STEP3 | 基本情報登録 約30秒 | 次セクション |
| STEP4 | 取引開始 スタート | **STOP** — 応募・出品公開・取引を始めない |

### Fields (STEP1)

| 画面の項目 | 操作 | 必須 | Evidence |
|---|---|---|---|
| メールアドレスで登録する | Google が使えるなら **使わない**（フォールバック専用） | メール経路のみ | `input#email` / `name="email"` / placeholder `例 info@craudia.com` |
| 無料で会員登録する（仮登録） | メール経路のときだけ。押す前に親 OTP 待ちを用意 | メール経路 | submit ボタン文言（GET） |
| SNSアカウントで登録する → **Google** | **押す**（PREFER） | 必須（このパック） | `signin_btn_google.svg` / i2i `login_auth.php?auth=3` |
| Twitter | **skip** | — | `auth=1` |
| Facebook | **skip** | — | `auth=2` |
| Yahoo! | **skip** | — | `auth=4` |
| 注記「連携先は i2i ID と表示されます。」 | 読む。i2i を別人格にしない | — | register-temp 本文 |
| 規約みなし | 人が一度読む。エージェントは箱を捏造しない | 登録行為で同意みなし | クラウディア利用規約 / [i2iID利用規約](https://id.i2i.jp/usr/pages/policy.html) / [個人情報保護方針](https://www.craudia.com/app/privacy) |
| reCAPTCHA | チェック/画像は人待ち。Press & Hold なら `holdDurationMs`（例 1800、再試行 2500） | 画面次第 | register-temp に recaptcha あり |
| ログインはこちら | 既存会員ならこちら | 既存時 | `/app/auth/login-form` |

- [ ] Worker LP の「仕事を依頼したい方はこちら」を踏まない。
- [ ] Google picker = `{{GOOGLE_ACCOUNT_EMAIL}}` のみ。Use another account で新規 Google を足さない。
- [ ] OAuth 同意は basic profile / email。Gmail-read-all / Drive / Contacts dump → `oauth_overreach` STOP。
- [ ] Unverified / blocked app → STOP. Morning user. “unsafe” を独断で通さない。
- [ ] メール経路フォールバック: 同じ MAIN Gmail。パスワードは `{{PASSWORD_DO_NOT_STORE}}`。git に残さない。
- [ ] 認証メール / コードが出たら [OTP-NOTE.md](OTP-NOTE.md) の Gmail 手順。SMS は skip。
- [ ] 既に会員: ログインして §4 へ。`already_member_draft`。

Authoring agent: do **not** POST `register-temp`. CU only.

---

## 3. After i2i — STEP2 会員登録（ライブ）

FAQ 151: 認証メール → クリック（**i2iID の登録が完了**）→ クラウディアでプロフィール → 登録完了。

ログイン後フォームは未観測 → ラベルは **needs_check** + ライブ。

- [ ] 戻った先が `mypage/top` 相当ならワーカー側か確認。クライアント登録に落ちたら戻る。
- [ ] Craudia PRO / 有料マッチング CTA は閉じる。
- [ ] 電話認証モーダル → **skip**。[OTP-NOTE.md](OTP-NOTE.md)。スキップ不能なら park `sms_skip_blocked`。
- [ ] 本人確認へ直行 → §8 STOP。アップロードしない。
- [ ] NDA / クローズド案件の初回モーダル → §8 STOP。同意しない。

パスワードを画面が再要求しても git / 成功ログに書かない。

---

## 4. STEP3 基本情報 — field order

出典: FAQ 151 / 103 / 47、規約第4条（満18歳以上）、register-temp ウィザード。必須マークは画面を正とする。  
Paste values: sibling `ops/earn/craudia-cu-handoff-20260916/FIELD-MAP.md`（[#60](https://github.com/rimone0511/autopilot-log/pull/60)）。ここには実氏名を書かない。

| # | 画面の項目（見込み） | 貼る値 | 必須見込み | CU tick |
|---|---|---|---|---|
| 4.1 | 氏名 | `{{LEGAL_NAME_KANJI}}` | 高 | [ ] 後の KYC と一致する実名。今は上げない |
| 4.2 | 氏名カナ | `{{LEGAL_NAME_KANA}}` | 高 | [ ] ライブに無ければ skip |
| 4.3 | ニックネーム / 表示名 | `{{DISPLAY_NAME}}`（推奨 `石田祐太`） | 高 | [ ] 資格を創作して括弧付けしない |
| 4.4 | 生年月日 | `{{BIRTH_YEAR}}` / `{{BIRTH_MONTH}}` / `{{BIRTH_DAY}}` | 高 | [ ] 満18歳以上。偽らない |
| 4.5 | 居住地 | `{{PREFECTURE}}` `{{CITY}}` | 高 | [ ] 番地は出さなくてよい画面なら市区まで。git に番地を書かない |
| 4.6 | 電話 | **空 / skip** | このパックでは触らない | [ ] SMS skip。必須で止まったら `sms_skip_blocked` |
| 4.7 | 業種 / 職種 | エンジニア / 自動化 / 業務改善の最寄り | 高 | [ ] 「AI」だけにしない。ライブチップのみ |
| 4.8 | 個人 / 法人 | **個人** | 高 | [ ] 法人を名乗らない |
| 4.9 | 今の状況 | 要相談（ライブが一致するとき） | needs_check | [ ] 応募しないので「作業可能」を無理に選ばない。未選択可 |
| 4.10 | 性別 / その他 | ライブ必須だけ | needs_check | [ ] 無い欄は空 |
| 4.11 | 保存 / 次へ | **基本情報を保存** | 高 | [ ] 「取引開始」ではない |

- [ ] STEP4「取引開始」をゴールにしない。
- [ ] 公開プロフィール用の表示名と、口座・KYC 用の氏名欄が分かれていたら混ぜない。

---

## 5. プロフィール編集 — field order

出典: FAQ 92 / 78、Crarepo 2025-11-12。ログイン後フォームは未観測。  
自己紹介の公式字数は FAQ に無い（**needs_check**）。画面カウンターを正とする。超過したら sibling の短いフェンスへ。

Crarepo: 自己紹介欄に **画像・URL 不可**。職歴 / 資格 / ポートフォリオ / プロフィール画像 / サムネイル / ポートフォリオ画像は **別欄**。

| # | 画面の項目 | 貼る値 | 必須見込み | CU tick |
|---|---|---|---|---|
| 5.1 | キャッチ / ひとこと | `公式API自動化と手順書。支払いはサイト内です`（**23**）。更に短ければ `公式API自動化と手順書`（12） | 任意〜高 | [ ] 連絡先を足さない |
| 5.2 | 自己紹介 | Sibling **URL 無し** 150 / 200 / 255 / 800（PR#60 FIELD-MAP §C） | 高 | [ ] URL 無しを先に。職歴を詰め込まない |
| 5.3 | 得意種別 | **プログラム・開発系** | 高 | [ ] user_list meta。無いラベルは最寄り。「IT」「システム」可 |
| 5.4 | 得意カテゴリ / タグ | IT・自動化の公式チップだけ | 任意 | [ ] 無いチップを作らない |
| 5.5 | 検索キーワード | ライブに欄があるときだけ: 業務自動化 / n8n / Python / 公式API / 手順書 | needs_check | [ ] 無い語を足さない |
| 5.6 | スキル（プロフィール） | 業務自動化, n8n, Python, Claude Code, Codex, YouTube Data API v3, TikTok Content Posting API, 手順書, 公式API | 高 | [ ] **出品ではない**。実務があるものだけ |
| 5.7 | 職歴 | `{{YEARS_AUTOMATION_PUBLIC}}` が空なら空 | 任意 | [ ] 年数創作禁止 |
| 5.8 | 資格 | 空（未確認） | 任意 | [ ] 持っていない資格を書かない |
| 5.9 | ポートフォリオ | `{{PORTFOLIO_URL}}` `https://yutalab.dev/` / `{{GITHUB_REPO_AUTOPILOT}}` | 任意〜高 | [ ] FAQ 78: 公開可能なもの。身分証を置かない。URL はここ |
| 5.10 | プロフィール画像 | `{{PHOTO_LOCAL_PATH}}` | 任意 | [ ] KYC 自撮りは不可 |
| 5.11 | サムネイル | ジャンルが分かる公開可画像 | 任意 | [ ] 他人の権利・ID 写真は不可 |
| 5.12 | 稼働時間 | 空、または「案件ごとに相談・リモート」 | 任意 | [ ] 週次時間を創作しない |
| 5.13 | 時給 | `{{HOURLY_JPY}}` **empty** | 完成チェック用なら | [ ] 必須で台帳が空なら `rate_empty`。数字を発明しない |
| 5.14 | SNS / LINE / メール本文 | **空** | STOP | [ ] ガイドライン: 連絡先投稿 NG |
| 5.15 | 公開設定 | **非公開 / 非表示** | 必須（あれば） | [ ] トグルが無ければ needs_check。露出を増やす操作をしない |
| 5.16 | プロフィールを更新 / 保存 | **保存** | 高 | [ ] 「公開する」ではない |

- [ ] 自己紹介で URL が弾かれたらポートフォリオ欄へ。URL ありフェンスは sibling FIELD-MAP §D。
- [ ] ワーカー検索の「見つけてもらう」ブースター / 有料オプションを買わない。

---

## 6. スキル下書き — field order（公開の直前で止める）

出典: FAQ 175、出品ガイド https://www.craudia.com/app/guide/service/sell （ステップ1–8）。  
規約: 「スキルの出品」= 詳細情報等を **公開** し購入者を募ること。このパックの「下書き」は **公開前の入力**。

ガイドはステップ8まで **公開ボタン** しか書いていない。ライブに 下書き保存 / 一時保存 / 保存 があればそれを使う。無ければ入力して **公開を押さず** 戻る。

入口: マイページ（ワーカーメニュー）「スキルを出品する」（FAQ 175）。推測 URL `mypage/services/add` はライブメニューを正とする。

### 6.A 入る / 入らない

- [ ] プロフィールが少なくとも一度 **保存** されている。
- [ ] クライアントの仕事登録（FAQ 53 の案件「下書き」）と混ぜない。あれは発注者側。
- [ ] 「スキルを探す」カタログに自分の商品を出さない。
- [ ] 出品画面が本人確認を要求したら §8。スキル下書きを捨ててよい。

### 6.B Fields (ガイド ステップ1–7)

| # | ガイド | 画面の項目 | このパックの値 | CU tick |
|---|---|---|---|---|
| 6.1 | ステップ1 | スキルを出品する | 入る（下書きのため） | [ ] 公開導線だと理解した上で進む |
| 6.2 | ステップ2 | カテゴリ（約170） | **プログラム・開発系** 配下の最寄り（自動化 / システム / IT）。無いラベルは最寄り | [ ] ライティングやデザインを満点にしない |
| 6.3 | ステップ3 | スキルタイトル **25文字以内** | 下記 A（15字）または B（13字）。末尾「ます」は自動追加・字数に含まない | [ ] カウンター超過なら短い方へ |
| 6.4 | ステップ3 | キャッチコピー | `公式API自動化と手順書。支払いはサイト内です`（23） | [ ] 詳細画面用。連絡先なし |
| 6.5 | ステップ4 | スキルの内容 | 下記本文（156字）。長い bio は sibling 自己紹介を流用可だが URL は画面ルールに従う | [ ] 未確認の件数・円額を書かない |
| 6.6 | ステップ4 | スキル価格 | **空**。必須なら `{{HOURLY_JPY}}` 台帳のみ。無ければ `rate_empty` して **公開しない** | [ ] ガイド例の 10,000円 / 紹介料計算を貼らない |
| 6.7 | ステップ4 | 納品予定日 | 空、または「要相談と表示する」にチェック | [ ] 日数を創作しない |
| 6.8 | ステップ5 | 購入者への必須質問 | `目的・範囲・合格条件・公式APIの有無を先に書いてください。ブラウザ自動操作は対象外です。`（45字） | [ ] 個人情報・口座を聞かない |
| 6.9 | ステップ6 | イメージ画像（最大5） | **スキップ可**。上げるならオリジナルのみ | [ ] ID / 自撮り / クライアント機密 / 他社ロゴをパートナーバッジにしない |
| 6.10 | ステップ6 | 有料オプション | **オフ / 空** | [ ] 追加料金を創作しない |
| 6.11 | ステップ6 | よくある質問 | 任意。例: 自動操作は対象外 / 支払いはサイト内 | [ ] 公開しなくても入力してよい |
| 6.12 | ステップ7 | 紹介料を設定する | **チェックしない** | [ ] 5–50% を触らない。ガイドの利益例を bio に貼らない |
| 6.13 | — | 下書き保存 / 一時保存 / 保存 | **あれば押す** | [ ] ライブに無ければ押さない（公開と別であることを確認してから） |
| 6.14 | ステップ8 | **公開** | **押さない** | [ ] 次セクション |

#### タイトル（25字以内。末尾「ます」自動）

A（15字）— 既定:

```
公式API自動化の手順を提供し
```

B（13字）— カウンターが厳しいとき:

```
業務自動化と手順書を設計し
```

表示は「…します」になる。タイトルに URL・価格・連絡先を入れない。

#### スキル内容（156字。下書き用。公開しない一文を含む）

```
公式APIだけを使い、繰り返し作業を人が検品できる形に自動化します。対象は業務フロー設計、手順書、YouTube/TikTokの公式投稿API。ブラウザ自動操作・スクレイピング・いいね自動化はしません。やり取りと支払いはクラウディア内です。秘密・連絡先は書きません。この画面は下書きまで。公開ボタンは押しません。
```

手数料は **cited unused**: スキル販売者 3–15%（1円〜5万 15% …）。https://www.craudia.com/app/guide/skill-price — フォームに貼らない。

---

## 7. STOP — 公開 / 本人確認 / NDA

ここから先は **入らない**。誘導されたら閉じる。ファイルを選ばない。同意しない。

### 7.A 公開

見た目の例（ライブラベルを正とする）:

- スキル出品ガイド ステップ8「公開ボタン」
- 『利用規約および 受発注ガイドラインに同意する』にチェックして公開
- プロフィール「公開する」
- 受付中 / 見積もり相談が可能 / スキル販売機能で公開中
- Discover 相当の露出オン、ワーカー一覧への掲載を増やす有料

- [ ] 公開チェックを入れない。
- [ ] 公開ボタンを押さない。
- [ ] 公開に必要な同意箱を、下書き保存と勘違いして入れない。
- [ ] 自分のスキル詳細 URL を git / X / プロフィール外に貼らない。

公開してしまったら: エージェントは取り消さない。`already_published` を [STATUS.md](STATUS.md) に書いて morning user。独断で非公開にしない。

### 7.B 本人確認

- FAQ 103: 登録そのものに本人確認は **不要**（PC メールがあれば可）。出金時に必要。
- FAQ 93: マイページ設定 → 本人確認。顔付き公的書類 + **自撮り必須**。
- FAQ 156: 電話認証ができないとき本人確認 URL を出す → それでも **上げない**。このパックは電話も skip。

- [ ] `mypage/setting/person` を開かない（自動遷移したら閉じる）。
- [ ] 免許 / マイナンバーカード / パスポート / 在留 / 特別永住者証明書を選ばない。
- [ ] 自撮りを撮らない・選ばない。カメラ権限を KYC に渡さない。
- [ ] 番号をタイプしない。サポートに書類を送らない。
- [ ] 海外在住の追加証明（領事館・公共料金）も今のオペレーター想定外 → 止める。

Log `kyc_wait`（秘密なし）。朝の本人は sibling KYC 1枚（PR#4）。このパックでは種類確認のためのオープンもしない。

### 7.C NDA / 機密

プラットフォーム規約 **第18条** の会員間機密保持は、登録みなしの一部であり、**追加の NDA 画面に同意することではない**。このパックが止めるのは **取引・閲覧・スカウトのための追加同意**。

止める画面の例:

- 秘密保持契約 / NDA に同意する
- クローズド案件（運営スカウト）の受諾
- オプション非公開案件の詳細を見るための同意
- 参加申請・見積もり相談の前に付く機密チェック
- クライアントがメッセージで送った NDA PDF への署名
- 「契約前のNDA締結が必須」と書いた仕事への応募

- [ ] 応募しないので NDA は不要。
- [ ] NDA 本文を git / チャットに貼らない。
- [ ] クローズド案件スカウトを「プロフィールが埋まったから」受けない。
- [ ] 規約第18条5「必要に応じ別途機密保持契約」は取引開始前の話。取引しない。

---

## 8. Success line (secret-free)

Valid outcomes: `done-draft` | `already_member_draft` | `skill_draft_saved` | `skill_draft_no_save_path` | `kyc_wait` | `sms_skip_blocked` | `nda_stop` | `no_draft_path` | `otp_missing` | `hold_failed` | `card_wall` | `oauth_overreach` | `rate_empty`.

Not success: 「応募した」「スキル公開した」「本人確認済み」「自撮り上げた」「NDA に同意した」「PRO にした」。

```
desk: Craudia
pack: ops/earn/craudia-live-checklist-20260916/
auth: google-main | email-same-mailbox | already_member | blocked
otp: gmail-parent | none | otp_missing
sms: skipped | sms_skip_blocked
kyc: none | wait-morning (no open)
nda: none | nda_stop
draft_profile: yes/no
skill_draft: saved | filled-no-save | not-entered | no
skill_listing_public: no
apply: no
publish: no
pro_upgrade: no
rate: empty | placeholder-from-ledger | rate_empty
holdDurationMs_used: <e.g. 1800 or none>
next: stop
```

Copy the same keys into [STATUS.md](STATUS.md). Do not put OTP digits, passwords, ID numbers, or a live phone there.

`thin_site_skip: false` — FAQ / 出品ガイド / register-temp が 200。Google は FAQ 151 と `auth=3`。

---

## 9. Out of scope

- この markdown を書いているエージェントからの signup POST
- ID / 自撮り / 銀行 / マイナンバー
- 参加申請 / スキル **公開** / Craudia PRO
- NDA 署名・クローズド案件受諾
- SMS / 050 発信
- TimeTicket / Contra / Wave B desks
- Sibling 本文の複製、`earn-packs/craudia/` へのコピー
- Python posting-gate の変更
