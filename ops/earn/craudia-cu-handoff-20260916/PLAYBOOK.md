# PLAYBOOK — クラウディア（Craudia）seller / worker CU

> **DRAFT_ONLY.** JP OK. No secrets. Stop-at-KYC only.  
> Computer-use（CU）直列用。このフォルダを書いているエージェントは **登録していない**。  
> Live form wins. 公開ヘルプに無いラベルは `needs_check`。

| キー | 値 |
|---|---|
| Desk | クラウディア / Craudia |
| Role | **ワーカー（出品者側）**。クライアント「仕事を依頼」に入らない |
| CU serial | **CU-09** / QUEUE **A9** |
| Host | `www.craudia.com` / `app.craudia.com`（誤綴り `craudia.jp` は使わない） |
| Language | **日本語** |
| Google | **PREFER_GOOGLE**（MAIN のみ） |
| Mode | 会員登録（必要なら）→ 基本情報 / プロフィール **下書き保存** |
| Stop | [STOP-KYC.md](STOP-KYC.md) — 本人確認（書類 + **自撮り**）で終わる |
| Timebox | 15–25 min。1モーダルで 10 min 超えたら park |

Paste values: [FIELD-MAP.md](FIELD-MAP.md)  
Desk box: [STATUS.md](STATUS.md)

Sibling bodies are **not copied** here. If a thicker paste is needed after this run:

| Sibling | Path / PR |
|---|---|
| Thin CU-09 | `earn-timeticket-contra-craudia-handoff-20260916/09-craudia.md` ([#18](https://github.com/rimone0511/autopilot-log/pull/18)) |
| Deep worker paste | `earn-craudia-deep-paste-20260916/` ([#51](https://github.com/rimone0511/autopilot-log/pull/51)) |
| Morning KYC 1枚 | `earn-kyc-morning-checklist-20260916/` ([#4](https://github.com/rimone0511/autopilot-log/pull/4)) |

---

## 0. How far to go (then stop)

1. Open **worker** entry, not client.
2. **Google** (`{{GOOGLE_ACCOUNT_EMAIL}}`). Else same MAIN mailbox + i2i 認証メール. Twitter / Facebook / Yahoo を新規身分にしない。
3. If already a member on MAIN Google: **ログイン**. Do not create a second account.
4. Fill 基本情報 + プロフィール from [FIELD-MAP.md](FIELD-MAP.md). Save. 公開トグルがあれば **非公開**.
5. プロフィールの得意種別 / スキル欄だけ。**スキル出品しない。参加申請しない。**
6. 本人確認画面は **開いて種類だけ確認して閉じる**。書類も自撮りも上げない。[STOP-KYC.md](STOP-KYC.md)。
7. Write the secret-free success line (section 6). Stop. Next Wave A desk is Freelancer.com — **not this folder**.

やらない: クライアント募集、参加申請、納品する、スキル公開、紹介料、Craudia PRO、口座・出金、手数料％の創作、この authoring エージェントからの POST。

---

## 1. URLs

### Confirmed (public GET 200 on 2026-09-16; this authoring agent did not POST)

| What | URL |
|---|---|
| Home | https://www.craudia.com/ |
| Worker LP | https://www.craudia.com/worker |
| 会員登録（仮登録） | https://www.craudia.com/app/auth/register-temp |
| ログイン | https://www.craudia.com/login |
| 会員登録の方法 | https://www.craudia.com/app/faq/contents/151 |
| 登録に必要なもの | https://www.craudia.com/app/faq/contents/103 |
| プロフィール編集（FAQ 見出し） | https://www.craudia.com/app/faq/contents/92 |
| ポートフォリオ | https://www.craudia.com/app/faq/contents/78 |
| 本人確認 | https://www.craudia.com/app/faq/contents/93 |
| 手数料 FAQ | https://www.craudia.com/app/faq/contents/72 |
| 手数料ガイド | https://www.craudia.com/app/guide/crowdsourcing-price |
| スキル販売手数料（**出品しない**） | https://www.craudia.com/app/guide/skill-price |
| 直接取引 | https://www.craudia.com/faq/contents/164 |
| 直接連絡 | https://www.craudia.com/app/faq/contents/140 |
| 参加申請（**送らない**） | https://www.craudia.com/app/faq/contents/89 |
| スキル出品方法（**入らない**） | https://www.craudia.com/app/faq/contents/175 |
| スキル出品ガイド（**公開しない**） | https://www.craudia.com/app/guide/service/sell |
| ワーカーガイド | https://www.craudia.com/app/guide/crowd-sourcing/worker |
| プロフィールの書き方（公式 Crarepo） | https://www.craudia.com/crarepo/archives/3678 |
| 規約 | https://www.craudia.com/app/agreement |
| ガイドライン | https://www.craudia.com/project_guideline |
| 年齢 | https://www.craudia.com/app/faq/contents/47 |
| 電話認証 | https://www.craudia.com/app/faq/contents/156 |
| 出金（**開かない**） | https://www.craudia.com/app/faq/contents/110 |

`/signup` と `/app/signup` は 404。**register-temp** を使う。

### Guess only — do not type unless the live page shows them

```
{{URL_GUESS_CRAUDIA_PROFILE_EDIT}}     # FAQ 92: マイページ設定「プロフィール編集」。ライブメニューを正とする
{{URL_GUESS_CRAUDIA_BASIC_INFO}}       # 「基本情報はこちら / 基本情報更新」。ライブを正とする
{{SIGNUP_URL_GUESS_CRAUDIA_CLIENT}}    # mypage/work/register — 選ばない
{{SIGNUP_URL_GUESS_CRAUDIA_SKILL_ADD}} # mypage/services/add — 選ばない
{{URL_GUESS_CRAUDIA_PRO_SIGNUP}}       # PRO 登録完了 URL は発明しない
{{URL_GUESS_CRAUDIA_I2I_CALLBACK}}     # OAuth コールバックを発明しない
```

Reject: client CTA「仕事を依頼」、スキル LP からの出品、Craudia PRO 有料マッチング。

---

## 2. Google MAIN notes

公開観測（register-temp GET 200）:

- 「SNSアカウントで登録する」に Google（`auth=3`）。注記「連携先は i2i ID と表示されます。」
- FAQ 151: PC メール **または** Twitter / facebook / Google / Yahoo!。
- メール経路: 認証メール → クリック（i2iID）→ クラウディアでプロフィール → 登録完了。
- 画面 STEP4 は「取引開始」。このパックは STEP3 基本情報 / プロフィールで止まる。
- reCAPTCHA あり。hold でなければ人待ち。Press & Hold なら `holdDurationMs` を必ずセット（例 1800、再試行 2500）。

手順:

1. https://www.craudia.com/app/auth/register-temp （既存なら `/login`）
2. **Google** as MAIN only. Picker: `{{GOOGLE_ACCOUNT_EMAIL}}`。
3. Consent: basic profile / email. Deny Gmail-read-all / Drive / Contacts dump.
4. Fallback: メール = 同じ MAIN Gmail。OTP = **親 Gmail MCP**。CU は `mail.google.com` を開かない。再送は 1 回まで。
5. Twitter / Facebook / Yahoo を新規紐付けしない。
6. パスワード経路なら `{{PASSWORD_DO_NOT_STORE}}`。git / 成功ログに残さない。
7. Already a member: ログイン。`already_member_draft`。
8. クライアント / PRO / スキル出品に落ちたらワーカープロフィールへ戻す。
9. SMS / 電話認証が **下書き保存** を止めるときだけユーザーチャット待ち。本人確認へ誘導されたら KYC STOP。

---

## 3. Profile pass (what CU types)

Live labels win. Paste table + fences: [FIELD-MAP.md](FIELD-MAP.md).

Order:

1. Role = ワーカー / 仕事を受ける。個人。法人を名乗らない。
2. 基本情報（氏名・かな・生年月日・居住地）。番地は出さなくてよい画面なら市区まで。git に番地を書かない。
3. 表示名 `{{DISPLAY_NAME}}`（推奨: `石田祐太`）。資格名を創作して括弧付けしない。
4. キャッチ / 自己紹介 — **自己紹介は URL 無しフェンスを先に**（Crarepo: 自己紹介欄に画像・URL 不可）。画面が URL を受け、カウンターが足りるときだけ URL ありフェンス。
5. 得意種別 **プログラム・開発系**（user_list meta）。無いラベルは最寄り。未経験カテゴリを満点にしない。
6. スキル欄 = 実務があるチップだけ。**出品画面に入ったら戻る。**
7. 職歴 / 資格 / ポートフォリオは専用欄。年数は `{{YEARS_AUTOMATION_PUBLIC}}` が空なら書かない。
8. 時給は `{{HOURLY_JPY}}` のみ。空で保存。必須で台帳が空なら `rate_empty`。
9. サムネイル / 顔写真は `{{PHOTO_LOCAL_PATH}}`。身分証・KYC 自撮りは不可。
10. 公開設定があれば非公開。無ければ埋めるだけ。ワーカー一覧の露出を増やす操作をしない。
11. **プロフィールを更新 / 保存**。公開する・出品する・応募するは押さない。

Crarepo（2025-11-12）が別欄と書くもの: 職歴、資格、ポートフォリオ、プロフィール画像、サムネイル画像、ポートフォリオ画像。自己紹介に詰め込まない。

---

## 4. Explicit do-not

- クライアントとして仕事を依頼する
- 参加申請 / 納品する / 見積もり提案
- スキルを出品する / スキルを公開する / 紹介料を設定する
- Craudia PRO に登録する / 買う
- 本人確認アップロード（書類・自撮り）
- 口座・振込依頼・出金・カード
- プロフィールにメール・電話・LINE・「この口座へ」
- 手数料％・時給円額・GMV・「○万人」を創作してコミット
- Twitter / Facebook / Yahoo を新規身分にする
- 第二アカウント
- NDA / クローズド案件スカウトへの応諾（下書き保存に不要なら触らない）
- この markdown を書いているエージェントが `register-temp` を POST すること

---

## 5. Fees (do not type into the form)

Cited only. Do not paste the ladder into the bio.

| Claim | Status | Source |
|---|---|---|
| 会員登録は無料 | cited | 規約第10条1 / トップ「会員登録(無料)」 |
| 採用時のみシステム利用料 | cited | FAQ 72 |
| 5万円まで一律 15% | cited | FAQ 72 |
| ワーカー 3〜15%（税込） | cited | 規約第10条3 |
| 階段 15/10/5/3% + 時間制 10% | cited | https://www.craudia.com/app/guide/crowdsourcing-price |
| スキル販売も同じ階段 | cited, unused | skill-price ガイド。出品しない |
| 出金振込 300円 | cited, unused | FAQ 39。出金しない |
| 直接取引の違約金 | cited, warning only | 規約第12条5。プロフィールに数字を貼らない |
| 自己紹介の公式字数 | needs_check | FAQ 92/78 に数字なし。画面カウンター |
| スキル出品タイトル 25 字 | cited, unused | 出品ガイド。出品しない |
| 時給実額 | placeholder | `{{HOURLY_JPY}}` empty |

---

## 6. Success line (secret-free)

Valid outcomes: `done-draft` | `already_member_draft` | `kyc_wait` | `sms_wait_user` | `no_draft_path` | `otp_missing` | `hold_failed` | `card_wall` | `oauth_overreach` | `rate_empty`.

Not success: 「応募した」「スキル出品した」「本人確認済み」「自撮り上げた」「PRO にした」。

```
desk: Craudia
pack: ops/earn/craudia-cu-handoff-20260916/
auth: google-main | email-same-mailbox | already_member | blocked
otp: gmail-parent | sms-chat | none | otp_missing | sms_wait_user
kyc: none | wait-morning + person_confirm_selfie
draft_profile: yes/no
ticket_or_page: craudia-worker-profile
skill_listing: no
apply: no
publish: no
pro_upgrade: no
rate: empty | placeholder-from-ledger | rate_empty
holdDurationMs_used: <e.g. 1800 or none>
next: stop
```

Copy the same keys into [STATUS.md](STATUS.md) after the run. Do not put OTP digits, passwords, ID numbers, or a live phone there.

`thin_site_skip: false` — FAQ / 手数料ガイド / register-temp が 200。Google 登録は FAQ 151 と登録面のボタンが明記。
