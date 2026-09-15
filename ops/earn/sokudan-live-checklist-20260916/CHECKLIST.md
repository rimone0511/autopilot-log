# CHECKLIST — SOKUDAN live register (Google → profile draft)

> ## REGISTER-CU-CUT
>
> **2026-09-16. Do not play.** This file is field-order archive, not next live CU.  
> Prefer **JOBS phase**. Do **not** open `/signup/pro`. See [STATUS.md](STATUS.md).  
> A later **human GO** is required before any tick below. Default is **cut**.

> **DRAFT_ONLY.** JP OK. No secrets.  
> Computer-use（CU）直列用の **手順書**。このフォルダを書いているエージェントは **登録していない / OAuth 未完走 / POST していない**。  
> Live form wins. 公開ページに無いラベルは `needs_check`。

Pack date: **2026-09-16**  
Folder: `ops/earn/sokudan-live-checklist-20260916/`  
Desk: SOKUDAN（ソクダン）— **フリーランス・副業（人材 / 受注者側）**  
CU serial: **CU-13** / QUEUE **B1** — **REGISTER-CU-CUT** (not next CU)  
Host: `sokudan.work`（発注者 LP は `business.sokudan.work` — **入らない**）  
Operator: CAMELORS株式会社（規約前文）  
Google: **PREFER_GOOGLE**（MAIN のみ）  
Paste: [FIELD-MAP.md](FIELD-MAP.md) — **生年月日・電話は創作しない**  
Desk box: [STATUS.md](STATUS.md)

Ordered pass: **Google で登録 → プロフィール下書き保存**  
Hard stop: **電話必須 / 生年月日必須 / 審査書類(KYC) / 応募ボタン**

Tick boxes on a **local** copy. Do not commit filled legal name, phone, DOB, OTP, ID, or a live SOKUDAN profile URL.

---

## Complement (do not copy sibling bodies)

This pack is the **live field order** plus a **tighter PII stop** than the thick paste. Paste fences live here in [FIELD-MAP.md](FIELD-MAP.md). Point at siblings; do not duplicate their tables into git twice.

| Sibling | Path | PR | This pack adds |
|---|---|---|---|
| Thick CU-13 paste | `earn-skillshift-sokudan-menta-deep-20260916/02-sokudan.md` | [#33](https://github.com/rimone0511/autopilot-log/pull/33) | Ordered ticks; **STOP if phone/DOB required** (sibling maps `{{PHONE}}` / `{{BIRTH_*}}` — this pack does **not** type them) |
| Serial card | `earn-workship-sokudan-offers-serial-cu-20260916/02-sokudan.md` | [#50](https://github.com/rimone0511/autopilot-log/pull/50) | Standalone Google → draft; this folder does **not** continue to Offers |
| Sample handoff | `earn-waveb-alive-handoff-sample-20260916/01-sokudan.md` | [#21](https://github.com/rimone0511/autopilot-log/pull/21) | Live GET 2026-09-16 + phone/DOB stop |
| Thin inventory | `earn-register-packs-jp-20260916/01-sokudan.md` | [#3](https://github.com/rimone0511/autopilot-log/pull/3) | Field order. 在庫01 ≠ this live run |
| Activity gate | `earn-activity-gate-waveB-20260916/records/01-sokudan.md` | [#12](https://github.com/rimone0511/autopilot-log/pull/12) | Gate stays **pass**. This pack does not rewrite it |
| Wave B serial note | `ops/earn/waveb-alive-cu-serial-20260916/b01-sokudan/` | [#72](https://github.com/rimone0511/autopilot-log/pull/72) | This folder is the **field checklist**, not the 6-desk ORDER |
| Morning KYC 1枚 | `earn-kyc-morning-checklist-20260916/` | [#4](https://github.com/rimone0511/autopilot-log/pull/4) | This pack does **not** open 審査書類 even to “note the type” |

Siblings say 応募しない / 審査書類 STOP. This pack **also** parks if 電話 or 生年月日 is required to save a draft. Do not invent a number or a date to get past the wall.

---

## 0. Hard stop (read before opening SOKUDAN)

- [ ] **REGISTER-CU-CUT.** Default: **do not open** this desk. Prefer JOBS. Human GO required to continue.
- [ ] Role = **フリーランス・副業**. 発注者 / 採用担当 / `business.sokudan.work` に入らない。
- [ ] MAIN Google only (`{{GOOGLE_ACCOUNT_EMAIL}}`). Facebook「推奨」/ LinkedIn / X / GitHub を新規身分にしない。
- [ ] **Gmail OTP allowed** via parent MCP. CU は `mail.google.com` を開かない。
- [ ] **Phone: do not type.** 任意なら空。必須で止まったら park `phone_required_stop`。SMS しない。050 発信しない。
- [ ] **DOB: do not type.** 任意なら空。必須で止まったら park `dob_required_stop`。偽の生年月日を作らない。
- [ ] **審査書類 / KYC に入らない**（規約第4条・第14条）。免許・マイナンバー・住民票・自撮り・口座を上げない。
- [ ] **応募しない。** 案件カードの 応募 / エントリー / 話を聞く / オファー返信 / スカウト承諾を押さない。
- [ ] 公開トグルを「公開する」側へ増やさない。発注機能を申し込まない。福利厚生ストアを買わない。
- [ ] 手数料％・時給円額・「リモート 92%」・マッチング日数を自己紹介に貼らない。
- [ ] 規約第4条: 代理人による会員登録は認められない。CU は本人同席前提。この authoring エージェントは登録しない。
- [ ] この authoring エージェントは `/signup` を **POST しない**。Google OAuth の `data-method="post"` も踏まない。CU serial だけがタイプする。

やらない（一覧）: 第二アカウント、企業コンソール、案件応募、審査書類、電話番号の創作、生年月日の創作、マーケ件数の実績化、連絡先を bio に書く、Python posting-gate の変更。

---

## 1. Preflight

- [ ] **REGISTER-CU-CUT check.** Default = **do not open SOKUDAN**. If you do not have a human GO in chat for *this* desk *this* day, stop. Prefer JOBS.
- [ ] You are the **CU serial** for this desk **only after that GO**, not the pack-author.
- [ ] Viewport desktop ≥ 1280px. One marketplace profile. Do not also live in Gmail in that profile.
- [ ] Previous CU left a different Google user → sign **out**, then MAIN (`rimone0511`).
- [ ] Timebox 15–25 min. 1モーダル 10 min 超えたら park.
- [ ] Entry is **`/signup/pro`**. Bare `/signup` redirected to **ログイン** on 2026-09-16 GET. `/signup/client` `/signup/company` もログインへ落ちた。人材面以外を入口にしない。
- [ ] 既存会員なら **ログイン**（`already_member_draft`）。二件目を作らない（規約第4条: 既会員は承諾しないことがある）。
- [ ] Internet Explorer 不可（登録面の注記）。現行デスクトップブラウザ。

Confirmed public GET (authoring session 2026-09-16, **no POST**, **no OAuth start**):

| What | URL |
|---|---|
| Home | https://sokudan.work/ |
| 人材 無料新規登録 | https://sokudan.work/signup/pro |
| Login（全ユーザー共通） | https://sokudan.work/login |
| Google signup | `/users/auth/google?category=signup&usage_type_id=1` |
| Google login | `/users/auth/google?category=login` |
| 認証メールの再送 | https://sokudan.work/users/confirmation/new |
| パスワード再設定 | https://sokudan.work/users/password/new |
| 利用規約 | https://sokudan.work/pages/terms |
| プライバシー | https://sokudan.work/pages/policy |
| FAQ（トップ内アコーディオン） | https://sokudan.work/ （`/pages/faq` は Notion 転送。トップ HTML を正とする） |
| 発注者 LP（**入らない**） | https://business.sokudan.work/ （フッター「発注者の方はこちら」=`/business`） |
| `/pages/privacy` | **404** — 使わない。ポリシーは `/pages/policy` |

Guess only — do not type unless the live page shows them:

```
{{URL_GUESS_SOKUDAN_PROFILE_EDIT}}     # ログイン後「プロフィール編集」。画面メニューを正とする
{{URL_GUESS_SOKUDAN_BASIC_INFO}}       # 基本情報。未観測
{{URL_GUESS_SOKUDAN_APPLY}}            # 案件の応募ボタン。見ても押さない
{{URL_GUESS_SOKUDAN_KYC}}              # 審査書類 UI。入らない
```

---

## 2. Google で登録（公開 STEP）

Open: https://sokudan.work/signup/pro  

見出し（GET 200、2026-09-16）: **無料新規登録** ─ **フリーランス・副業の方向け** ─

### Fields (logged-out)

| 画面の項目 | 操作 | 必須 | Evidence |
|---|---|---|---|
| Facebook で無料登録 **推奨** | **skip** | — | `href="/users/auth/facebook?category=signup&usage_type_id=1"`。ラベル「推奨」でも使わない |
| **Google で登録** | **押す**（PREFER） | 必須（このパック） | `alt="Google で登録"` / `href="/users/auth/google?category=signup&usage_type_id=1"` / `data-method="post"` |
| LinkedIn で登録 | **skip** | — | `/users/auth/linkedin?category=signup&usage_type_id=1` |
| X で登録 | **skip** | — | `/users/auth/twitter?category=signup&usage_type_id=1` |
| GitHub で登録 | **skip**（次点でもこのパックでは使わない。新しい身分にしない） | — | `/users/auth/github?category=signup&usage_type_id=1` |
| メールアドレス | Google が使えるなら **使わない**（フォールバック専用） | メール経路のみ | `input#user_email` / `name="user[email]"` / placeholder `メールアドレス` / `required` |
| パスワード（英数含む8文字以上） | メール経路のときだけ。`{{PASSWORD_DO_NOT_STORE}}`。git に残さない | メール経路 | `input#user_password` / `name="user[password]"` / pattern 英数混在 8–128 |
| メールで無料登録 | メール経路のときだけ。押す前に親 OTP 待ちを用意 | メール経路 | submit。`form action="/signup" method="post"`。**authoring は POST しない** |
| hidden `user[usage_type_id]` | 触らない（ページが `1` = 人材） | 人材面 | signup/pro GET |
| 利用規約 ・ プライバシーポリシー | 人が一度読む。エージェントは箱を捏造しない | 登録行為で「上記に同意してご利用ください」 | `/pages/terms` `/pages/policy` |
| reCAPTCHA | メール経路。チェック/画像は人待ち。Press & Hold なら `holdDurationMs`（例 1800、再試行 2500） | メール経路 | 登録面に `g-recaptcha`。sitekey を git にコピーしない |
| アカウントをお持ちの方はログイン | 既存ならこちら | 既存時 | `/login` |
| 認証メールの再送 | メール経路で届かないとき。再送 **1 回まで** | 任意 | `/users/confirmation/new` |

- [ ] ヒーローやフッターの「発注者の方はこちら」を踏まない。
- [ ] Google picker = `{{GOOGLE_ACCOUNT_EMAIL}}` のみ。Use another account で新規 Google を足さない。
- [ ] OAuth 同意は basic profile / email。Gmail-read-all / Drive / Contacts dump → `oauth_overreach` STOP。
- [ ] Unverified / blocked app → STOP. Morning user. “unsafe” を独断で通さない。
- [ ] メール経路フォールバック: 同じ MAIN Gmail。パスワードはローカル。CSRF / `authenticity_token` をログや git に貼らない。
- [ ] 認証メールが出たら親 Gmail MCP。CU は受信箱を開かない。コードを成功ログに書かない。
- [ ] 既に会員: https://sokudan.work/login → **Google でログイン**。§3 へ。`already_member_draft`。

Authoring agent: do **not** POST `/signup` and do **not** start `/users/auth/google`. CU only.

---

## 3. After Google — 会員側（ライブ。ログイン壁の向こう）

公開 GET ではプロフィール編集フォームは **未観測** → ラベルは **needs_check** + ライブ。貼る値は [FIELD-MAP.md](FIELD-MAP.md)。

- [ ] 戻った先が人材 / 受注者側か確認。発注者・採用担当コンソールに落ちたら戻る。戻れなければ park（KYC 無しでも発注者登録はしない）。
- [ ] 電話番号欄 → **空のまま**。スキップ可なら skip。必須マーク / 保存不能なら §5 `phone_required_stop`。
- [ ] 生年月日 / 生年月 / 年齢確認 → **空のまま**。任意なら skip。必須で止まったら §5 `dob_required_stop`。
- [ ] 審査書類・本人確認・アップロード → §6 STOP。ファイルを選ばない。
- [ ] 応募 CTA / おすすめ案件の「今すぐ応募」→ §7 STOP。
- [ ] 規約第7条の AI 自己紹介生成を使うなら **保存前に人が直す**。件数・年数・円額を足させない。使わない方がよい。
- [ ] 有料プラン / 福利厚生（FAQ: ログイン後 `/pages/benefits`）を開いて買わない。

パスワードを画面が再要求しても git / 成功ログに書かない。

---

## 4. プロフィール下書き — field order

出典: 登録面 GET、プライバシー第2条（取得しうる項目の **種類**。必須ラベルではない）、規約第4条 / 第7条、トップ FAQ。必須マークは **画面を正**とする。

Paste: [FIELD-MAP.md](FIELD-MAP.md)。ここには実氏名・電話・生年月日を書かない。

| # | 画面の項目（見込み） | 貼る値 | 必須見込み | CU tick |
|---|---|---|---|---|
| 4.1 | 登録経路 | Google（済） | 必須 | [ ] Facebook 推奨に切り替えない |
| 4.2 | メール | Google から来る / `{{EMAIL}}` | Googleから | [ ] 別アドレスを足さない |
| 4.3 | 氏名（漢字） | `{{LEGAL_NAME_KANJI}}` | 高 | [ ] 後の KYC と一致する実名。**今は書類を上げない** |
| 4.4 | 氏名カナ | `{{LEGAL_NAME_KANA}}` | needs_check | [ ] ライブに無ければ skip |
| 4.5 | 表示名 / ニックネーム | `{{DISPLAY_NAME}}`（推奨 `石田祐太`） | 高 | [ ] 資格を創作して括弧付けしない |
| 4.6 | **生年月日 / 生年月** | **空。打たない** | 任意なら skip / 必須なら STOP | [ ] §5。偽らない代わりに **創作もしない** |
| 4.7 | 性別 | ライブ必須だけ。無ければ空 | needs_check | [ ] ポリシーに「性別」とあるのは取得しうる種類。欄が無ければ作らない |
| 4.8 | 居住地 | `{{PREFECTURE}}` `{{CITY}}` | 高 | [ ] 番地は出さなくてよい画面なら市区まで。git に番地を書かない |
| 4.9 | **電話番号** | **空。打たない** | 任意なら skip / 必須なら STOP | [ ] §5。SMS しない |
| 4.10 | 職種 | エンジニア / 自動化 / 業務改善の最寄り | 高 | [ ] 「AI」だけにしない。ライブチップのみ。FAQ の職種マーケを bio にコピーしない |
| 4.11 | 所有スキル | [FIELD-MAP.md](FIELD-MAP.md) スキルリスト | 高 | [ ] 未経験を経験と書かない。`xAI` / `Grok` を詰め込まない |
| 4.12 | 経験年数 | `{{YEARS_AUTOMATION_PUBLIC}}` **empty** | 高〜任意 | [ ] 未確認なら空。数字を創作しない |
| 4.13 | キャッチ / ひとこと | FIELD-MAP キャッチ（30字 / 短い欄は12字） | 任意〜高 | [ ] 連絡先・92% を足さない |
| 4.14 | 自己紹介 / 職務経歴 | FIELD-MAP JA 200（既定）または 800 | 高 | [ ] カウンター超過なら短い方。URL が弾かれたら nourl フェンス |
| 4.15 | 職務経歴書ファイル | 任意。ローカル PDF | 任意 | [ ] リポジトリに置かない。必須＋身分証扱いなら §6 |
| 4.16 | ポートフォリオ | `https://yutalab.dev/` / `https://github.com/rimone0511/autopilot-log` | 任意〜高 | [ ] 公開 URL のみ |
| 4.17 | 稼働条件 | リモート可。週次は要相談 | 高 | [ ] 週時間・単価を創作しない |
| 4.18 | SNS | `https://github.com/rimone0511` | 任意 | [ ] LINE / 携帯 / 個人メールを bio に書かない |
| 4.19 | 現所属 / 会社名 | 人が決める。git に社名を書かない | 任意 | [ ] FAQ: 同じ会社名同士は互いに見えない。就業規則は人が確認 |
| 4.20 | 招待コード | `{{INVITE_CODE}}` 空でよい | 任意 | [ ] 空 |
| 4.21 | 公開設定 | **非公開 / 下書き** があればそれを選ぶ | 必須（あれば） | [ ] 露出を増やす操作をしない |
| 4.22 | 保存 / 更新 | **下書き保存 / 保存** | 高 | [ ] 「応募する」「公開する」「審査に進む」ではない |

- [ ] 保存できた。応募 0。電話・DOB は空のまま（または未表示）。
- [ ] ライブに 下書き保存 が無く、通常保存がプロフィール更新だけなら、それを使い **公開トグルは触らない**。応募はしない。
- [ ] 保存不能の理由が電話必須 / DOB 必須 / KYC / 応募前提なら、該当 STOP へ。無理に埋めない。

---

## 5. STOP — 電話必須 / 生年月日必須

このパックは **プレースホルダを埋めて突破しない**。台帳に実値があっても、CU はこのフォルダのルールでは打たない。朝の本人が別 GO を出すまで空。

### 5.A `phone_required_stop`

見た目の例（ライブラベルを正とする）:

- 電話番号 *必須
- SMS 認証 / 確認コードを送信
- 番号を入力しないと「保存できない」
- 050 発信で本人確認

- [ ] 番号をタイプしない。
- [ ] SMS を完了しない。親チャットに実番号をログしない。
- [ ] 固定電話や勤務先電話で逃げない。
- [ ] Log `phone_required_stop`（秘密なし）。次の机へ進んでよい。この机は park。

任意の電話欄を空で保存できたなら、これは STOP ではない。空のまま §8。

### 5.B `dob_required_stop`

見た目の例:

- 生年月日 *必須 / 生年月 *必須
- 年齢確認チェックが日付入力を要求
- 満○歳の証明として日付が要る

- [ ] 日付を創作しない。`1990-01-01` などのダミー禁止。
- [ ] 年だけ埋めて日を捏造しない。
- [ ] 規約第13条の「未成年者…同意等を得ていない」は **年齢を偽る許可ではない**。このパックは打たない。
- [ ] Log `dob_required_stop`（秘密なし）。実 DOB は git / 成功ログに書かない。

任意なら空で保存してよい。プライバシーポリシー第2条が「生年月日を取得します」と書いていても、**公開フォームで必須と観測したことにはならない**。

Sibling #33 の `{{BIRTH_*}}` / `{{PHONE}}` 行は、このパックでは **参照しないで打つな**。

---

## 6. STOP — KYC / 審査書類

ここから先は **入らない**。誘導されたら閉じる。ファイルを選ばない。

規約:

- **第4条**: 会員登録申請の審査に **必要な書類の提出を求めることがあり**、提出しない場合は登録を拒否できる。拒否されても ID を上げて通さない。
- **第14条** 期中審査: 必要書類の提供を求めることがある。同じく STOP。
- 代理人登録不可（第4条）。この authoring エージェントは登録しない。

止める画面の例:

- 本人確認 / eKYC / 本人確認アプリ
- 免許証・マイナンバーカード・パスポート・住民票・顔写真付き証明書
- 自撮り / カメラ権限
- 口座・振込先・クレジットカード「本人確認のため」
- インボイス登録番号の入力
- サポートへ書類メール

- [ ] ファイル選択を開かない。カメラを KYC に渡さない。
- [ ] 番号面をタイプしない。
- [ ] Log `kyc_wait`（机名 + 画面種類だけ。秘密なし）。朝の本人は PR#4。このパックでは種類確認のためのオープンもしない。

登録そのものが書類なしで進むなら、プロフィール下書きまでやってよい。書類が出た時点でパック完了扱い。

---

## 7. STOP — 応募ボタン

一覧を **見る** のは可（activity gate と同じ）。**送る** のは不可。

止めるコントロールの例（ライブラベルを正とする）:

- 応募する / この案件に応募 / 登録して応募
- エントリー / 話を聞く / 興味あり
- オファーに返信 / スカウトを受ける / 面談日程を確定
- 案件詳細の送信・提案フォームの submit

ログイン前の案件カード（例 `/top/projects/20955`）は SPA で本文に「▼応募後の流れ」と出る。それを **手順書として実行しない**。ボタンが出たら押さない。

- [ ] 応募 0。
- [ ] スカウト返信 0。
- [ ] 「応募やオファー…即日で面談」（トップ FAQ）を成功条件にしない。
- [ ] 誤って応募してしまったら取り消さない。`already_applied` を [STATUS.md](STATUS.md) に書いて morning user。独断で撤回しない。

---

## 8. Success line (secret-free)

Valid outcomes: `done-draft` | `already_member_draft` | `phone_required_stop` | `dob_required_stop` | `kyc_wait` | `apply_stop` | `no_draft_path` | `otp_missing` | `hold_failed` | `oauth_overreach` | `already_applied`.

Not success: 「応募した」「公開した」「本人確認済み」「電話登録した」「生年月日を入れた」。

```
desk: SOKUDAN
pack: ops/earn/sokudan-live-checklist-20260916/
auth: google-main | email-same-mailbox | already_member | blocked
otp: gmail-parent | none | otp_missing
phone: skipped | phone_required_stop
dob: skipped | dob_required_stop
kyc: none | wait-morning (no open)
draft_profile: yes/no
publish: no
apply: no
holdDurationMs_used: <e.g. 1800 or none>
next: stop
```

Copy the same keys into [STATUS.md](STATUS.md). Do not put OTP digits, passwords, ID numbers, a live phone, or a date of birth there.

`thin_site_skip: false` — `/signup/pro` 200、Google 登録リンクあり、トップに 2026-09-15 更新の案件カードあり。

---

## 9. Out of scope

- この markdown を書いているエージェントからの signup POST / Google OAuth 開始
- 電話番号・生年月日の入力（必須なら STOP。任意でもこのパックでは打たない）
- ID / 自撮り / 銀行 / マイナンバー
- 案件応募 / スカウト返信 / 発注者申込
- Facebook / LinkedIn / X / GitHub を新規身分にする
- Workship / Offers / Skill Shift など他机（Wave B serial は [PR#72](https://github.com/rimone0511/autopilot-log/pull/72) で **REGISTER-CU-CUT**）
- このフォルダを次の live CU として開くこと（default **cut**。JOBS-first）
- Sibling 本文の二重貼り、`earn-packs/` へのコピー
- Python posting-gate の変更
