# PLAYBOOK — Offers（B19）worker CU

> ## REGISTER-CU-CUT / jobs-first
>
> **Do not** treat Offers as next live CU after Freelancer.com (A10 / CU-10).  
> Prefer JOBS phase. Default hint: `register_cu_cut`. This file is archive + paste order, **not a signup GO.**  
> Keep draft. No secrets. **No apply.**

> **DRAFT_ONLY.** No secrets. **No apply.**  
> このフォルダを書いているエージェントは **登録していない。応募していない。**  
> Live form wins. 公開 HTML / 規約に無いラベルは `needs_check`。

| キー | 値 |
|---|---|
| Desk | Offers（offers.jp） |
| Local ID | **B19** |
| QUEUE | **B14**（PR#59 のローカル B14 = PPH ではない） |
| CU serial | **CU-25** |
| Role | **ワーカー**。企業 `/client/` に入らない |
| Host | `offers.jp` |
| Language | **日本語** |
| Google | **PREFER_GOOGLE**（MAIN のみ） |
| Mode | **REGISTER-CU-CUT.** Archive paste order. Not next live CU. If a human re-opens register CU: 会員登録（必要なら）→ ワーカープロフィール **下書き保存** |
| Stop | [STOP.md](STOP.md) — **応募しない。** KYC / 有料ブース / クライアント登録もしない |
| Timebox | 15–25 min。1モーダルで 10 min 超えたら park |
| `thin_site_skip` | **false**（この GET: `/worker/signup` 200） |

Paste values: [FIELD-MAP.md](FIELD-MAP.md)  
Desk box: [STATUS.md](STATUS.md)

Sibling bodies are **not copied** here (pointers only):

| Sibling | PR |
|---|---|
| Thick field+bio | [#30 `04-offers.md`](https://github.com/rimone0511/autopilot-log/pull/30) |
| Week2-rest paste | [#34 `03-offers.md`](https://github.com/rimone0511/autopilot-log/pull/34) |
| Serial card | [#50 `03-offers.md`](https://github.com/rimone0511/autopilot-log/pull/50) |
| Activity gate | [#12 `records/12-offers.md`](https://github.com/rimone0511/autopilot-log/pull/12) |
| B19 CU-NOTE | [#72 `b19-offers/CU-NOTE.md`](https://github.com/rimone0511/autopilot-log/pull/72) |

**REGISTER-CU-CUT（PR#72）:** Wave B 登録直列は jobs-first に譲る。Freelancer.com（A10）の次に **Offers を開かない。** 下の手順は人が register CU を明示的に再オープンしたときだけ。既定は **cut**。再オープンしても **応募はしない。**

---

## 0. How far to go (then stop)

1. Open **worker** signup: https://offers.jp/worker/signup — **not** `/signup` (this GET: **404**).
2. **Google で登録する** (`{{GOOGLE_ACCOUNT_EMAIL}}`). Else same MAIN mailbox 「メールアドレスで登録する」.
3. If already a member on MAIN Google: **ログイン** (`/worker/login` → Google でログインする). Do not create a second account.
4. Fill プロフィール from [FIELD-MAP.md](FIELD-MAP.md). **下書き保存.** 公開トグルがあれば **非公開**.
5. Jobs は **見るだけ。** 「登録して求人に応募する」は押さない。[STOP.md](STOP.md).
6. 本人確認 / 面談確定 / 有料ブース / 年収診断の送信が壁なら park. 書類は上げない.
7. Write the secret-free success line (section 6). Stop.

やらない: 求人応募、スカウト返信、ヘッドハント日程確定、クライアント登録、有料ブース、手数料％の創作、この authoring エージェントからの POST / OAuth 完走.

---

## 1. URLs

### Confirmed (public GET on 2026-09-16 JST; this authoring agent did not POST)

| What | URL | This GET |
|---|---|---|
| Home | https://offers.jp/ | 200。転職コピー + メタ「登録35,000人」は活動証明に使わない |
| Worker signup | https://offers.jp/worker/signup | 200。`data-testid="auth-google"`。ラベル **「Googleで登録する」**。`/oauth/worker_signup/google` |
| Bare `/signup` | https://offers.jp/signup | **404** — 使わない |
| Worker login | https://offers.jp/worker/login | 200。「Googleでログインする」。`/oauth/worker_login/google` |
| Jobs 業務委託 | https://offers.jp/jobs/engineer/side-job | 200。「副業・業務委託可」。更新日文字列 **2026-09-10** あり。CTA「登録して求人に応募する」= **STOP** |
| Jobs 一覧 | https://offers.jp/jobs | 200。見出しだけ。応募しない |
| 利用規約 | https://offers.jp/terms | 200。第3条 業務委託 + 求職。第11条 システム利用料は **クライアント**。第12条 マッチング成功報酬は **クライアント**。％未記載 → 作らない |
| 個人情報 | https://offers.jp/privacypolicy | 200。この GET に「本人確認」文字列なし |
| Client LP | https://offers.jp/client | 200。**開いたら閉じる。** 採用側 |
| Client login | https://offers.jp/client/login | 企業。選ばない |
| Google OAuth start | https://offers.jp/oauth/worker_signup/google | **302**（この GET はフォローしていない）。クリックは後続 CU + 人の MAIN Google だけ |

Guess only — do not type unless the live page shows them:

```
{{URL_GUESS_OFFERS_PROFILE_EDIT}}     # ログイン後「プロフィール編集」。ライブメニューを正とする
{{URL_GUESS_OFFERS_RESUME}}           # 職務経歴。任意。年数創作禁止
{{URL_GUESS_OFFERS_APPLY}}            # 応募確認 — 入らない
{{URL_GUESS_OFFERS_BOOTH}}            # 有料ブース — 買わない
{{URL_GUESS_OFFERS_KYC}}              # 本人確認ウィザード — 開いて種類だけ / 上げない
{{SIGNUP_URL_GUESS_OFFERS_CLIENT}}    # /client/ — 選ばない
```

Worker support がクライアント LP から `https://support-worker.offers.jp/hc/ja` にリンクする。このエージェントの GET は **403** → 記事本文は **needs_check**。記事 ID を発明しない。

Reject: 企業 CTA、Jobs の応募ボタン、GitHub / X / LinkedIn をこの机のためだけに新規作成。

---

## 2. Google MAIN notes

公開観測（`/worker/signup` GET 200）:

- SNS リスト: Google / GitHub / X(Twitter) / LinkedIn。**MAIN Google を優先。**
- ラベル: `<strong>Google</strong>で登録する`（`data-ovf-value="google"`）。
- フォールバック見出し: 「メールアドレスで登録する」（`data-ovf-value="email"`）。
- 既存: 「既にアカウントをお持ちの方はコチラ」→ `/worker/login`。
- GitHub は **任意のあと。** 公開リポジトリと一致するときだけ。X / LinkedIn を新規身分にしない。
- サイドコピーは「転職プラットフォーム」。QUEUE の「転職導線だけ」再判定は Jobs 業務委託を見て **pass**（PR#12）。応募はしない。

手順:

1. https://offers.jp/worker/signup （既存なら `/worker/login`）
2. **Google で登録する** as MAIN only. Picker: `{{GOOGLE_ACCOUNT_EMAIL}}`。
3. Consent: basic profile / email. Deny Gmail-read-all / Drive / Contacts dump.
4. Fallback: メール = 同じ MAIN Gmail。OTP = **親 Gmail MCP**。CU は `mail.google.com` を開かない。再送は 1 回まで。
5. パスワード経路なら `{{PASSWORD_DO_NOT_STORE}}`。git / 成功ログに残さない。
6. Already a member: ログイン。`already_member_draft`。
7. 企業 `/client/` に落ちたらワーカーへ戻す。
8. SMS / 電話が **下書き保存** を止めるときだけユーザーチャット待ち。本人確認へ誘導されたら [STOP.md](STOP.md)。
9. Press & Hold なら `holdDurationMs` をセット（例 1800、再試行 2500）。hold でなければ人待ち。

---

## 3. Profile pass (what CU types)

Live labels win. Paste table + fences: [FIELD-MAP.md](FIELD-MAP.md).

Order:

1. Role = ワーカー / 人材。個人。法人・採用担当を名乗らない。
2. 氏名 `{{LEGAL_NAME_KANJI}}`。表示名 `{{DISPLAY_NAME}}`（推奨: `石田祐太`）。資格名を創作して括弧付けしない。
3. 生年月日 / 活動拠点は台帳。番地は出さなくてよい画面なら市区まで。git に番地を書かない。
4. 自己紹介 — **URL 無しフェンスを先に**（safe paste）。画面が URL を受け、カウンターが足りるときだけ URL あり 200/800。公式字数は公開 GET に無い → **needs_check**。超過したら短いフェンスへ降りる。
5. スキル = 実務があるチップだけ。無いチップを作らない。
6. 働ける職種 = エンジニア / 自動化の最寄り。
7. 業務委託（副業）意欲 = 画面値の最寄り（検討する、等）。**盛らない。**
8. 転職意欲 = 急いでいない / 良い話があれば、の最寄り。転職専願に振り切らない。
9. GitHub 連携は任意（`{{GITHUB_URL}}` / `{{GITHUB_REPO_AUTOPILOT}}` が公開と一致するとき）。
10. ポートフォリオ URL は専用欄。`{{PORTFOLIO_URL}}`。
11. 希望単価 `{{HOURLY_YEN_DRAFT}}` = **空。** Jobs カードの時給レンジ（例 4,000〜12,000）をプロフィールにコピーしない。必須で台帳が空なら `rate_empty`。
12. 年収診断の送信が必須なら空で進むか park。数値を創作しない。
13. 公開設定 = 非公開 / 下書き。トグルが無ければ `needs_check`。

連絡先（メール・電話・SNS）を自己紹介本文に足さない。

---

## 4. Jobs look-don't-apply

Jobs は activity-gate の根拠。**応募導線ではない。**

この GET で確認したもの（見出しのみ。本文に入らない）:

- ラベル「副業・業務委託可」
- カード例「【フルリモート】AI×FDE｜事業課題を解くフルスタックエンジニア募集」
- カード例「【フルリモート／業務委託】AI×新規事業を牽引するシニアエンジニア募集」
- 更新日文字列 **2026-09-10**（他に 2026-09-08 / 09-07 等。最新だけを活動証明にしない）
- 繰り返し CTA「**登録して求人に応募する**」→ [STOP.md](STOP.md)

やってよい: 一覧の見出しを目視して `pass` を再確認する。  
やってはいけない: 応募、気になる、スカウトへの返信、カジュアル面談の申込。

---

## 5. Hard stop

詳細: [STOP.md](STOP.md)。

即停止:

- 「登録して求人に応募する」/ 応募確認 / 送信
- ヘッドハント・カジュアル面談の日程確定
- スカウト返信
- 本人確認書類・自撮り・マイナンバー・口座
- 有料ブース / 優先掲載 / カード
- クライアント登録
- 規約の成功報酬％を第三者記事から埋める

---

## 6. Success line (secret-free)

Fill [STATUS.md](STATUS.md) after a live run. Do not paste OTP, phone, or a password.

```
desk: Offers
id: B19
queue: B14
cu: CU-25
pack: ops/earn/offers-cu-handoff-20260916/
auth: google_ok | already_member | email_fallback | not_run
otp: none | parent_gmail | sms_wait_user
kyc: none | shown_closed | kyc_wait
draft_profile: yes | no | unknown
apply: no
scout_reply: no
publish: no
paid_booth: no
client: no
rate: empty | ledger | rate_empty
next: stop
```

Valid later outcomes: `done-draft` | `already_member_draft` | `kyc_wait` | `sms_wait_user` | `no_draft_path` | `otp_missing` | `hold_failed` | `card_wall` | `oauth_overreach` | `rate_empty` | `apply_wall` | `not_run`.

---

## 7. Out of scope (this folder)

- この authoring エージェントからのアカウント作成 / OAuth 完走 / POST
- 求人応募・提案送信（JOBS フェーズの他机ドラフトも **ここからは送らない**）
- Workship / SOKUDAN / Skill Shift の直列再生
- 先パックの秘密や長文の二重管理（ポインタを使う）
- Python posting-gate 試験の変更
