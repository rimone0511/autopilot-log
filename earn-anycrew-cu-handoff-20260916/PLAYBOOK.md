# PLAYBOOK — Anycrew（B10）talent CU

> **DRAFT_ONLY.** No secrets. **No apply. No publish.**  
> Computer-use（CU）直列用。このフォルダを書いているエージェントは **登録していない。応募していない。公開していない。**  
> Live form wins. 公開 HTML / 規約に無いラベルは `needs_check`。

| キー | 値 |
|---|---|
| Desk | Anycrew（エニィクルー） |
| Local ID | **B10**（PR#61 フォルダ番号。QUEUE の Malt **B10** ではない） |
| QUEUE | **B5**（PR#1） |
| CU serial | **CU-15** |
| Role | **人材 / 登録ユーザー**（仕事を受ける側）。`biz.any-crew.com` は閉じる |
| Hosts | 人材アプリ `app.any-crew.com` · 共通 ID `id.any-crew.com` · マーケ `www.any-crew.com` |
| Language | **日本語** |
| Google | **PREFER_GOOGLE**（MAIN のみ） |
| Mode | 会員登録（必要なら）→ 人材プロフィール **下書き保存**。検索結果は **非公開** |
| Stop | [STOP.md](STOP.md) — **応募しない。公開しない。** KYC / 電話壁 / 法人コンソールもしない |
| Timebox | 15–25 min。1モーダルで 10 min 超えたら park |
| `thin_site_skip` | **false**（この GET: アプリトップ 200、ブランド一致、閉鎖文なし） |
| activity_gate | **needs_check**（`/offers` SPA 空。案件カード未読。pass にしない） |

Paste values: [FIELD-MAP.md](FIELD-MAP.md)  
Desk box: [STATUS.md](STATUS.md)

Sibling bodies are **not copied** here (pointers only):

| Sibling | PR |
|---|---|
| Activity gate (local B10) | [#61 `records/b10-anycrew.md`](https://github.com/rimone0511/autopilot-log/pull/61) |
| Wave B gate sheet | [#12 `records/05-anycrew.md`](https://github.com/rimone0511/autopilot-log/pull/12) |
| Thin sample paste | [#21 `03-anycrew.md`](https://github.com/rimone0511/autopilot-log/pull/21) |
| Deep paste | [#33 `03-anycrew.md`](https://github.com/rimone0511/autopilot-log/pull/33) |
| Gap-fill | [#39 `02-anycrew.md`](https://github.com/rimone0511/autopilot-log/pull/39) |
| Week2 pack | [#3 `05-anycrew.md`](https://github.com/rimone0511/autopilot-log/pull/3) |
| Alive serial (skips this desk) | [#72](https://github.com/rimone0511/autopilot-log/pull/72) |

**REGISTER-CU-CUT（PR#72）:** Wave B 登録直列の自動再生は jobs-first に譲る。このフォルダは Anycrew 机のランナー。Freelancer.com（A10）の次に **勝手に開かない。** 人が GO したときだけ PLAYBOOK を踏む。GO しても **応募・公開はしない。** ゲートは `needs_check` のまま。

この机の `/offers` は Anycrew の案件 SPA である。Offers.jp（B19 / CU-25）ではない。

---

## 0. How far to go (then stop)

1. Open talent home: https://app.any-crew.com/ — **not** https://biz.any-crew.com/ .
2. Signup URL: https://id.any-crew.com/signup?auth_entry_source=front — 公開 CTA「会員登録」「会員登録(無料)」「新規会員登録はこちら」。SPA のラベルは **Googleで登録する**。
3. Already a member on MAIN Google: アプリの「ログイン」→ **Googleでログイン**. Do not create a second account.
4. Role = **個人向け**. 「法人向けログイン」は選ばない。
5. Fill プロフィール from [FIELD-MAP.md](FIELD-MAP.md). **下書き保存.** FAQ: 検索結果への表示を「非公開／公開」から選ぶ → **非公開**.
6. `/offers` は **見るだけ。** 応募・スカウト返信はしない。[STOP.md](STOP.md). この GET ではカードが空。日付が見えないまま gate を `pass` にしない.
7. 電話 / SMS / 本人確認書類が壁なら park. 番号も書類も上げない.
8. Write the secret-free success line (section 6). Stop.

やらない: 求人応募、スカウト返信、プロフィール公開、Facebook 新規、法人コンソール、GraphQL POST、手数料％の創作、この authoring エージェントからの POST / OAuth 完走。

---

## 1. URLs

### Confirmed (public GET on 2026-09-16 JST; this authoring agent did not POST)

| What | URL | This GET |
|---|---|---|
| Talent home | https://app.any-crew.com/ | **200** 59625B。Last-Modified **Tue, 15 Sep 2026 10:51:28 GMT**。CTA「会員登録」→ ID signup。流れ「FacebookかGoogleのアカウントで利用登録」。モーダル **Googleでログイン** |
| Signup (ID) | https://id.any-crew.com/signup?auth_entry_source=front | **200** 481B React シェル（`<div id="root">` のみ）。Last-Modified **Tue, 15 Sep 2026 10:50:44 GMT**。ラベルはバンドル JS: **Googleで登録する** / Facebookで登録する / メールアドレスで登録する / 個人向けログイン / 法人向けログイン |
| ID home | https://id.any-crew.com/ | **200** 同じ 481B シェル。`noindex,nofollow` |
| ID login | https://id.any-crew.com/login | **200** 同じ 481B シェル |
| App `/signup` `/login` `/register` | https://app.any-crew.com/signup ほか | **200** 429B — アプリ SPA 空。登録 CTA は ID signup を正とする |
| Offers SPA | https://app.any-crew.com/offers | **200** **429B** React シェル。案件タイトル・掲載日 **なし** |
| Offers 職種 | https://app.any-crew.com/offers/_software_engineer | **301** → `/offers/professions/software_engineer` → **200 429B** 同じ空シェル |
| Offers リモート | https://app.any-crew.com/offers/_remote | **301** → `/offers/workstyles/remote` → **200 429B** 同じ空シェル |
| Marketing | https://www.any-crew.com/ | **200**。人材アプリへリンク |
| 利用規約 | https://www.any-crew.com/terms | **200**。第3条 登録は外部 SNS。第5条 基本無料。改定 **2024-11-14**。Google 文字列なし（公開面 HTML が Google を明示） |
| プライバシー | https://www.any-crew.com/privacy | **200**。登録時: 氏名・メール・職歴等。**電話番号は応募・契約の収集項目。** 利用目的に「本人確認」 |
| FAQ on www | https://www.any-crew.com/faq | **404**。FAQ 本文はアプリトップを正とする |
| News | https://www.any-crew.com/news | **200**。メディア掲載 **2026-08-31** あり。**案件カードの日付ではない** |
| Blog | https://blog.any-crew.com/ | **200**。新着 **2026.08.26**。**案件カードの日付ではない** |
| Employer | https://biz.any-crew.com/ | **200** 採用 LP。**使わない** |
| Employer login | https://biz.any-crew.com/login | **200** 429B SPA。**使わない** |
| Google OAuth start (form action) | https://base.any-crew.com/auth/google_oauth2?state=auth_entry_source_front | ログインモーダルは **POST**。この authoring の **GET は 404**。POST していない。同意画面へ入っていない |
| Password reset | https://id.any-crew.com/user/password_reset/request?reset_referrer=front | リンク確認のみ。触らない |

Guess only — do not type unless the live page shows them:

```
{{URL_GUESS_ANYCREW_PROFILE_EDIT}}   # ログイン後「プロフィール」。ライブメニューを正とする
{{URL_GUESS_ANYCREW_GOOGLE_OAUTH}}   # 実クリックは POST google_oauth2。deep link を発明しない
{{URL_GUESS_ANYCREW_OFFER_CARD}}     # /offers カード。この GET では未読
{{URL_GUESS_ANYCREW_APPLY}}          # 応募確認 — 入らない
{{URL_GUESS_ANYCREW_KYC}}            # 本人確認ウィザード — 開いて種類だけ / 上げない
{{URL_GUESS_ANYCREW_PHONE}}          # 電話・SMS — 下書きを止めるときだけユーザー待ち
{{SIGNUP_URL_GUESS_ANYCREW_BIZ}}     # biz.any-crew.com — 選ばない
```

JS に `/user/new/oauth` がある。ライブ URL として発明して打ち込まない。画面のボタンを正とする。

Reject: 法人 CTA、応募ボタン、Facebook 新規、Offers.jp との取り違え、GraphQL `base.any-crew.com/graphql` への POST（CSRF が要る）。

---

## 2. Google MAIN notes

公開観測（アプリ HTML + ID バンドル。OAuth 未完走）:

- アプリ流れ: 「**FacebookかGoogleのアカウントで利用登録**」
- アプリ登録 CTA: `id.any-crew.com/signup?auth_entry_source=front`（**会員登録** / **会員登録(無料)**）
- アプリログインモーダル: ラベル **Googleでログイン**。`method="POST"` `action="https://base.any-crew.com/auth/google_oauth2?state=auth_entry_source_front"`
- ID signup バンドル: **Googleで登録する**（Facebookで登録する / メールアドレスで登録する も文字列あり）
- 規約第3条1: **登録には外部 SNS サービスで登録されたアカウントを使用**。第2条(11) の例示は Facebook「その他当社が定めるもの」。公開面は Google を明示 → **PREFER_GOOGLE**
- 個人向け / 法人向け: **個人向け**。法人向けログインは閉じる
- メール+パスワード欄はアプリモーダルと ID JS の両方にある。規約が SNS 登録を主経路と書く。Google が死んだら **park**（メールだけで通るかは `needs_check`）。通る画面でもメール = 同じ MAIN mailbox だけ
- Facebook を新規作成・新規紐付けしない

手順:

1. https://app.any-crew.com/ → **会員登録**（既存なら **ログイン**）
2. https://id.any-crew.com/signup?auth_entry_source=front で **個人向け** を確認して **Googleで登録する** as MAIN only. Picker: `{{GOOGLE_ACCOUNT_EMAIL}}`。
3. Consent: basic profile / email. Deny Gmail-read-all / Drive / Contacts dump.
4. Fallback: メール = 同じ MAIN Gmail。OTP = **親 Gmail MCP**。CU は `mail.google.com` を開かない。再送は 1 回まで。ID JS: 「確認用のメールを送りました」「メール内にあるリンクをクリックして」
5. パスワード経路なら `{{PASSWORD_DO_NOT_STORE}}`。git / 成功ログに残さない。CSRF `authenticity_token` をコピーしない。
6. Already a member: ログイン。`already_member_draft`。
7. 法人 / biz に落ちたら人材へ戻す。
8. SMS / 電話が **下書き保存** を止めるときだけユーザーチャット待ち。番号を git に書かない。本人確認へ誘導されたら [STOP.md](STOP.md)。
9. Press & Hold なら `holdDurationMs` をセット（例 1800、再試行 2500）。hold でなければ人待ち。

---

## 3. Profile pass (what CU types)

Live labels win. Paste table + fences: [FIELD-MAP.md](FIELD-MAP.md). Seller = **石田祐太 / n8n / AI**.

Order:

1. Role = 人材 / 登録ユーザー。個人。求人事業者・採用担当を名乗らない。
2. 氏名 `{{LEGAL_NAME_KANJI}}`。表示名 `{{DISPLAY_NAME}}`（推奨: `石田祐太`）。資格名を創作して括弧付けしない。
3. 生年月日 / 活動拠点は台帳。番地は出さなくてよい画面なら市区まで。git に番地を書かない。
4. 自己紹介 — **URL 無しフェンスを先に**（safe paste）。画面が URL を受け、カウンターが足りるときだけ URL あり 200/800。公式字数は公開 GET に無い → **needs_check**。超過したら短いフェンスへ降りる。
5. スキル = 実務があるチップだけ（n8n / AI / 業務自動化）。無いチップを作らない。
6. 職業 = 業務自動化 / エンジニアの最寄り。
7. 転職意向 = **複業・業務委託** の最寄り。転職エージェント化しない。
8. 稼働可能時間 = 空または要相談。**数字の創作禁止。**
9. ポートフォリオ URL は専用欄。`{{PORTFOLIO_URL}}`。
10. 公開設定 = **非公開**（FAQ: 検索結果への表示を「非公開」「公開」から選ぶ）。公開スイッチを押さない。
11. 職務経歴書は通常スキップ（公式 FAQ）。仲介案件で必須なら応募しないので触らない。

連絡先（メール・電話・SNS）を自己紹介本文に足さない。

---

## 4. /offers SPA — activity evidence only

`/offers` は activity-gate の根拠枠である。**応募導線ではない。**

この GET で確認したもの（**カード本文は無い**）:

- https://app.any-crew.com/offers → 429 バイト。`<div id="root"></div>` + `/assets/react-12a6720f.js`
- 職種・働き方リライトも同じ空シェル（エンジニア / リモート）
- アプリナビ「案件一覧」は `/offers` を指す。一覧 HTML にタイトルも日付も無い
- 企業ニュース **2026-08-31** とブログ **2026.08.26** は宣伝。**job-board freshness に使わない**
- アプリ Last-Modified 2026-09-15 は静的シェルが生きていること。掲載案件の更新日ではない
- コピー「案件が豊富」を件数にしない
- GraphQL を叩いてカードを埋めない

やってよい: 人が 1 枚、日付付きカードを目視したら STATUS に `card_seen` と日付を書く。  
やってはいけない: 応募、気になる、スカウトへの返信、見えないまま `pass`。

---

## 5. Hard stop

詳細: [STOP.md](STOP.md)。

即停止:

- 応募する / この案件に応募 / 応募を確定
- スカウトに返信 / メッセージを送る
- 検索結果の「公開」
- 電話番号の本番入力（git 禁止）/ SMS を CU が推測
- 本人確認書類・自撮り・マイナンバー・口座
- 法人コンソール / 求人掲載
- 人材成果報酬％を第三者記事から埋める
- Facebook 新規身分
- `base.any-crew.com/graphql` への POST

---

## 6. Success line (secret-free)

Fill [STATUS.md](STATUS.md) after a live run. Do not paste OTP, phone, or a password.

```
desk: Anycrew
id: B10
queue: B5
cu: CU-15
pack: earn-anycrew-cu-handoff-20260916/
auth: google_ok | already_member | email_fallback | not_run
otp: none | parent_gmail | sms_wait_user
kyc: none | shown_closed | kyc_wait
phone: none | sms_wait_user | phone_wall
draft_profile: yes | no | unknown
search_visibility: private | unknown | public_blocked
apply: no
scout_reply: no
publish: no
biz: no
offers_spa: empty | card_seen
next: stop
```

Valid later outcomes: `done-draft` | `already_member_draft` | `kyc_wait` | `sms_wait_user` | `phone_wall` | `no_draft_path` | `otp_missing` | `hold_failed` | `oauth_overreach` | `apply_wall` | `needs_check_offers` | `not_run`.

---

## 7. Out of scope (this folder)

- この authoring エージェントからのアカウント作成 / OAuth 完走 / POST
- 求人応募・提案送信（JOBS フェーズの他机ドラフトも **ここからは送らない**）
- `/offers` を GraphQL で埋める
- Workship / SOKUDAN / Offers.jp の直列再生
- 先パックの秘密や長文の二重管理（ポインタを使う）
- Python posting-gate 試験の変更
