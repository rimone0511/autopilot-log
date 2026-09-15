# A3 — Lancers（ランサーズ）CU desk

Desk: Lancers  
CU serial: **A3 / CU-03** (after Fiverr, before CrowdWorks)  
Checked: 2026-09-15/16 (public help + public signup HTML)  
Mode: **DRAFT ONLY** — fill, save, **never publish**  
Paid plans: NO  
Language: **日本語** profile and package. Honest `{{COUNTRY}}` = Japan.  
Google: **PREFER_GOOGLE**  
OTP: magic-link / 本登録メール → **Gmail parent**. SMS → **user chat**.

---

## 0. How far to go (then stop)

1. Confirmed URL → MAIN Google. Do not invent a second account.
2. Role = **仕事を受けたい / ランサー / フリーランス・副業・在宅**. Not 仕事を依頼したい / クライアント.
3. Username + 利用方法. Username **cannot be changed** (official FAQ). Use `{{LANCERS_USERNAME}}` from the local ledger. If empty in chat, ask the user once. Do not invent a joke handle.
4. Paste profile fields (section 3). Save. If a 公開する toggle exists, leave **非公開 / hidden**.
5. Optional: パッケージ DRAFT (section 4). **保存する**. Do **not** click **完了** if help says that publishes.
6. **STOP** at 本人確認, 口座, マイナンバー, かんたん税金. See [STOP-KYC.md](STOP-KYC.md).
7. Write the success line (section 6). Open CrowdWorks only after that.

If KYC appears before a profile can be saved, stop. This paste is still the pack (`kyc_wait`).

Timebox: 15–25 minutes. Stuck > 10 minutes on one modal: park, next.

---

## 1. URLs

### Confirmed (use these)

| What | URL |
|---|---|
| Home | https://www.lancers.jp/ |
| 新規会員登録 | https://www.lancers.jp/user/sign_up/ |
| Login | https://www.lancers.jp/user/login |
| ソーシャルログイン後のパスワード（触らない） | https://www.lancers.jp/faq/A1011/649 |
| ユーザー名は変更できない | https://www.lancers.jp/faq/A1021/29 |
| ユーザー名と表示名 | https://www.lancers.jp/faq/A1021/36 |
| 自己紹介の書き方 | https://www.lancers.jp/faq/A1028/57 |
| パッケージ出品手順（ランサー向け） | https://www.lancers.jp/faq/S000/850 |
| 本人確認とは（出金時必須 — このパックではやらない） | https://www.lancers.jp/faq/A1023/60 |

Google social login is documented in official FAQ (Google / Yahoo / Facebook / LinkedIn). The signup HTML fetched 2026-09-16 did not reliably surface the button label in markdown. **CU must visually confirm a Google control on `/user/sign_up/` or `/user/login`.** If it is missing, register with **email = MAIN Gmail**. Do not bind Yahoo/Facebook/Apple.

### Guess only (placeholders — do not type unless the live page shows them)

```
{{SIGNUP_URL_GUESS_LANCERS_GOOGLE}}   # e.g. an /auth/google redirect — UNCONFIRMED
{{URL_GUESS_LANCERS_PROFILE_EDIT}}    # in-app: プロフィール編集. Live menu wins.
{{URL_GUESS_LANCERS_PACKAGE_NEW}}     # in-app: 出品管理 → 出品する. Live menu wins.
```

Do not open `lancers.com`. Official host is **`www.lancers.jp`**.

---

## 2. Google MAIN notes (this desk)

1. Land on https://www.lancers.jp/user/sign_up/ (or login if already a member).
2. Confirm you are not on a client-only campaign LP that skips ランサー.
3. Click **Google**. Picker: **`rimone0511@gmail.com` only**.
4. Consent: basic profile/email. Deny Gmail-read-all / Drive / Contacts dump.
5. If “this Google is already registered”: **ログイン**, do not duplicate.
6. 仮登録メール: parent Gmail MCP. CU does not open Gmail. 再送は **1回まで**.
7. Password: Google path often **has none** (FAQ A1011/649). Do not invent `{{PASSWORD_DO_NOT_STORE}}` on this path. Do not run パスワード再設定.
8. Press & Hold / Cloudflare: `holdDurationMs: 1800`, one retry `2500`. See [00-google-otp-hold.md](00-google-otp-hold.md).

Already a member with MAIN Google: do not duplicate. Open profile, confirm unpublished packages, mark `already_member_draft`. Still no publish.

---

## 3. Profile paste fields (JP)

Live form wins. Skip optional legal / payout / 電話 unless SMS play requires it.

| 画面の項目（公開情報ベース） | 貼る値 | 必須見込み | メモ |
|---|---|---|---|
| Google | `{{GOOGLE_ACCOUNT_EMAIL}}` | 優先 | |
| メール | `{{EMAIL}}` | メール経路なら必須 | 確認URLは親が開かせない。CUへ渡す |
| パスワード | 書かない | Google経路では出ないことが多い | ローカル台帳のみ |
| ユーザー名 | `{{LANCERS_USERNAME}}` | 必須 | **変更不可**（FAQ）。空ならユーザーに一度聞く |
| 主な利用方法 | フリーランス・副業・在宅で働きたい（画面の文言に合わせる） | 必須 | 依頼者にしない |
| 区分 | 個人 | 高 | 法人コンソールは閉じる |
| 氏名（漢字） | `{{LEGAL_NAME_KANJI}}` | 高 | 公開チェックを外す |
| 氏名カナ | `{{LEGAL_NAME_KANA}}` | 高 | |
| 表示名 | `{{DISPLAY_NAME}}`（推奨: `石田祐太`） | 高 | 表示名はプロフィール用。ユーザー名とは別（FAQ A1021/36） |
| 表示名に本名を利用する | **オフ** unless the user said otherwise in chat | 任意 | |
| 性別 | 空または画面の任意 | 任意 | |
| 生年月日 | `{{BIRTH_YEAR}}/{{BIRTH_MONTH}}/{{BIRTH_DAY}}` | 高 | |
| 都道府県 / 市区町村 | `{{PREFECTURE}}` `{{CITY}}` | 下書きに必要なら | 郵便番号・番地は KYC 手前なら空でよい |
| 職業 / 職種 | エンジニア / システム開発 / 業務効率化の最寄り | 高 | ライブの選択肢を正とする |
| キャッチフレーズ | 下記 ひとこと | 高 | |
| 自己紹介 | 下記 300+ / 800 | 高 | 認定条件の「300文字以上」は公式FAQに出てくる。件数は書かない |
| 主な利用用途 | **受注する** | 高 | 発注しない |
| 稼働状況 | 仕事できます（または最寄り） | 任意 | |
| 希望時間単価 / 最低招待金額 | **空** または 要相談 | 任意 | **金額を創作しない** |
| 報酬額の公開設定 | **非公開** if the control exists | 任意 | |
| 招待 | 空でよい。変な低額自動承諾はしない | 任意 | |
| ポートフォリオ | `{{PORTFOLIO_URL}}` `{{GITHUB_REPO_AUTOPILOT}}` | 高 | |
| 顔写真 | `{{PROFILE_PHOTO_LOCAL_PATH}}` | 任意 | ポートレートのみ。身分証禁止。コミット禁止 |
| スキル | n8n, 業務自動化, API連携, 技術文書, Google Workspace | 高 | `xAI` / `Grok` をスキルにしない |
| 電話 | SMS play のときだけ | 通常スキップ | |

### キャッチフレーズ（貼る）

画面カウンタを正とする。短く。

```
AI業務自動化と手順書。公式APIのみ。ブラウザ自動操作なし
```

### JA bio 200（短い欄・予備）

```
石田祐太。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIによる業務自動化の手順・つまずき・確認できた結果を、むずかしい言葉を避けて公開しています。公式APIだけを使う動画アップロード道具も公開中です。ブラウザ自動操作はしません。人が検品できる形で、繰り返し作業を自動化します。リモート可。未確認の数字は書きません。公開は人が決めます。秘密は貼りません。根拠を残す方針です。
```

### JA bio 自己紹介（主ペースト。300字超 / 800字級）

公式ヘルプは経歴・できる仕事・連絡を書けと案内する。年数と件数は書かない。

```
石田祐太（Yuta Ishida）です。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIを使って毎日の作業を自動化する手順、つまずいた点、確認できた結果を、むずかしい言葉を避けて公開しています。売り物は「動いたように見える自動化」ではなく、人が検品できる仕組みです。公開している実録と道具を、業務委託の成果物の根拠にします。

▼可能な業務／スキル
・繰り返し作業の自動化設計（目的・範囲・合格条件・停止条件を先に切る）
・n8n / Make / Zapier など、依頼者が継続できる側への寄せ（勝手に乗り換えない）
・Claude Code や Codex に実装を任せるときの指示、検品、失敗時の切り分け
・YouTube Data API v3 と TikTok Content Posting API だけの投稿の仕組みづくり
・鍵の扱い、公開事故、トークン期限など、自動化が止まりやすい箇所の点検

▼公開している道具の例
Autopilot Log（https://github.com/rimone0511/autopilot-log）。公式APIのみ。投稿の門番は壊れても非公開側に倒れます。

▼受けないこと
ブラウザ自動操作・スクレイピング、いいねやフォローの自動化、権利のない投稿代行、本人確認書類・口座・マイナンバーの代理入力、未確認のままの公開。

▼活動時間／連絡
テキスト中心。リモート可。週次の稼働時間は案件ごとに相談します。秘密はチャットに出さず、本人の安全な入力経路だけを使います。日本語でのやり取りを標準にします。

独立した個人です。n8n や AI ラボの社員・認定ではありません。未確認の件数や年数は書きません。
```

Do not keyword-stuff xAI / Grok.

---

## 4. Package DRAFT fields（出品 — 公開しない）

Official help: https://www.lancers.jp/faq/S000/850

Help’s click path (login required; **GUESS** that the logged-in URL is under マイページ):

1. 出品管理 → 受付中のパッケージ → **出品する**
2. タイトル（「〜します / 〜を作ります」）とカテゴリ → 次へ
3. 料金表・オプション → 次へ
4. 業務内容・よくある質問 → 次へ
5. 注文時のお願い → 次へ
6. 画像・動画 → **保存する**
7. 必須を埋めたら **完了** → **「パッケージが公開されます」**

**This pack stops at step 6.** Do not click **完了**.

If the live wizard has **no** 保存 without 完了 (the next click is always public), **do not create the package**. Profile text only. Record `no_draft_path` for the package.

If 出品する is behind 本人確認: **STOP**. Do not upload. Profile-only is success.

### 4.1 Title（ますで終わる。貼る）

Help: 「●●●をします」「〇〇〇を作ります」.

```
止まっても再開できる業務自動化と手順書を作ります
```

Do not replace with keyword-stuffed「n8n AI xAI Grok 代行」titles.

### 4.2 Category (pick in the live dropdown; do not invent IDs)

Prefer the closest **IT / システム開発 / 業務効率化 / プログラミング** node.  
If the tree differs, pick automation / API / コンサル of software.  
Do not put this in 動画編集 mill, 恋愛, 占い, or いいね代行.

### 4.3 料金表 — DRAFT, amounts empty

**Do not invent fees or yen prices.** Leave numeric cells empty or `{{PRICE_YEN_DRAFT}}`. Official system-fee % is **not** pasted here; re-read live help if a human later prices this.

| プラン名（案） | 内容（短） | 金額 | 納期目安 |
|---|---|---|---|
| 調査と手順 | 対象業務の切り分け、公式APIの有無、止まらない条件のメモ | `{{PRICE_YEN_DRAFT}}` | `{{LEAD_TIME_DRAFT}}` |
| 実装と手順書 | フロー1本 + 再実行手順 + 秘密を書かない接続一覧 | `{{PRICE_YEN_DRAFT}}` | `{{LEAD_TIME_DRAFT}}` |
| 実装と回帰 | 上に加え、失敗通知と合格条件のチェック表 | `{{PRICE_YEN_DRAFT}}` | `{{LEAD_TIME_DRAFT}}` |

If the form allows only **one** price, use the middle row’s text and still leave the number empty.

オプション（名前だけ。金額空）:

- 追加のアプリ接続 `{{PRICE_YEN_DRAFT}}`
- 追加の手順書（別フロー） `{{PRICE_YEN_DRAFT}}`
- 急ぎ対応 `{{PRICE_YEN_DRAFT}}`

Do not add “手数料込 XX%” lines. Do not type CrowdWorks 5–20% or any remembered rate onto Lancers.

### 4.4 業務内容（貼る）

```
依頼者の手元で止まっても再開できる業務自動化と、非エンジニアが読める手順書を作ります。

対象の例: フォームやメールや表をまたぐ転記、承認が付くまで次へ進まないフロー、公式APIでの投稿の仕組み（YouTube Data API v3 / TikTok Content Posting API）。道具は n8n / Make / Zapier のうち、依頼者がすでに使える側に寄せます。新しい有料プランの加入は、この下書きでは提案しません。

進め方:
1. 入口・出口・失敗時の行き先を先に合意する
2. 本番データを使わず、ダミーで1本動かす
3. 失敗したときに人へ戻す経路を残す（黙って再送しない）
4. 接続の鍵は依頼者のアカウントに置く。こちらは手順だけ渡す

納品の目安: 動くシナリオ（依頼者テナント内）、接続一覧（秘密の値は書かない）、停止・再開の手順、合格条件のチェック表。

受けないこと: ブラウザ自動操作、スクレイピング、いいね／フォロー／閲覧の自動化、権利のない投稿代行、パスワードやAPI鍵や本人確認書類の代理入力、未確認のままの公開。

独立した個人です。n8n や AI ラボの社員・認定ではありません。公開の根拠: https://yutalab.dev/ と https://github.com/rimone0511/autopilot-log
```

Sibling proposal pack `earn-jp-proposal-drafts-20260916/02-ipaas-workflow-lancers.md` is **応募文**. Do not send it from this desk.

### 4.5 よくある質問（任意。あれば貼る）

1. AI を使いますか？  
   人が設計・検品します。分類・要約・下書きの軽いモデル利用は依頼者が希望したときだけです。使わない指定があれば従います。

2. n8n や xAI の公式ですか？  
   いいえ。独立した個人です。公式パートナーでも社員でもありません。

3. ブラウザでクリックする自動化はしますか？  
   しません。公式APIと、依頼者が入れる接続だけです。

4. 鍵はどこに置きますか？  
   依頼者の画面です。チャットに貼らないでください。

### 4.6 注文時のお願い（任意）

Keep questions short. Do not ask for passwords or ID.

1. 自動化したい手作業を一文で書いてください。
2. つなぐ道具と、公式APIの有無を書いてください。
3. n8n / Make / Zapier / 未導入のどれですか。
4. 軽いAIステップ（分類・要約・下書き）は可ですか。不可ですか。
5. 鍵はご自身の画面で入れます。ここに秘密を貼らないでください（はい / いいえ）。

### 4.7 画像・動画

Skip for this draft if 完了 needs an image. Do not download random marketplace images. Do not use n8n / xAI / Google / Lancers logos as fake partnership. Later human publish decision: original screenshot of **your** workflow canvas, owned by you.

---

## 5. Explicit do-not (this desk)

- パッケージ **完了**（公開）
- 提案・メッセージの送信（JP proposal drafts are a different folder）
- 本人確認申請
- 口座 / かんたん税金
- Yahoo / Facebook / Apple を Google の代わりに新規紐付け
- ユーザー名の再抽選のために退会
- 認定ランサー条件を満たすための KYC 先行

---

## 6. What success looks like **before CrowdWorks**

Park Lancers and open CrowdWorks only when **one** of these is true:

| Outcome | Meaning |
|---|---|
| `done-draft` | MAIN Google ランサー. Username set. 自己紹介 pasted. Package absent **or** saved unpublished (no 完了). Publish = no. KYC = none. |
| `already_member_draft` | Same mailbox already in. Profile checked. Still no publish. |
| `kyc_wait` | ID/口座/マイナ screen appeared. Closed without files. Morning user has desk + screen type. |
| `sms_wait_user` | Draft blocked on SMS. User not in chat. Do not burn resends. |
| `no_draft_path` | Next click would publish. Stopped. Profile-only if that saved. |
| `otp_missing` / `hold_failed` / `card_wall` / `oauth_overreach` | Parked with reason. |

**Not** success: “認定ランサーになった”, “パッケージが公開された”, “提案を1件送った”, “本人確認済みバッジ”.

Secret-free log line (no OTP digits):

```
desk: Lancers
pack: earn-lancers-cw-cu-handoff-20260916/01-lancers.md
auth: google-main | email-same-mailbox | already_member | blocked
otp: gmail-parent | sms-chat | none | otp_missing | sms_wait_user
kyc: none | wait-morning + type
draft_profile: yes/no
draft_package: saved-unpublished | skipped-no-draft | skipped-kyc | none
publish: no
holdDurationMs_used: <e.g. 1800 or none>
next: CrowdWorks
```

Then open [02-crowdworks.md](02-crowdworks.md). Do not start Upwork.
