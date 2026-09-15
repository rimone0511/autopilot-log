# A4 — CrowdWorks（クラウドワークス）CU desk

Desk: CrowdWorks  
CU serial: **A4 / CU-04** (after Lancers, before Upwork)  
Checked: 2026-09-15/16 (public HTML + official worker pages)  
Mode: **DRAFT ONLY** — fill worker profile, **never 応募 / never publish a listing**  
Paid plans: NO  
Language: **日本語** profile. Honest `{{COUNTRY}}` = Japan.  
Google: **PREFER_GOOGLE**（公開画面に **Googleではじめる** を確認）  
OTP: メール確認 → **Gmail parent**. SMS → **user chat**.

Start this desk only after Lancers is parked (see `01-lancers.md` §6).

---

## 0. How far to go (then stop)

1. Confirmed URL → MAIN Google. Same mailbox as Lancers. No second identity.
2. Role = **仕事を受注する / ワーカー**. Not 仕事を依頼する / クライアント.
3. Paste worker profile fields (section 3). Save.
4. Paste skills / 職種 / ひとこと as the **service DRAFT** (section 4). CrowdWorks **has no Lancers-style パッケージ出品** on the main site (community + worker guide: 応募 or スカウト). Do not invent a gig catalog.
5. Do **not** 応募する, 提案送信, コンペ提出, タスク開始.
6. **STOP** at 本人確認書類提出, 口座, マイナンバー, インボイス登録番号. See [STOP-KYC.md](STOP-KYC.md).
7. Write the success line (section 6). **Stop the session.** Next serial desk is Upwork — not this folder.

If KYC appears before a profile can be saved, stop (`kyc_wait`).

Do not wander into **AI CrowdWorks** (QUEUE B15) from this hostname. Do not open **PARK** (`park.jp`) — different CrowdWorks-group product, not Wave A.

Timebox: 15–25 minutes. Stuck > 10 minutes: park, do not start Upwork from this pack.

---

## 1. URLs

### Confirmed (use these)

| What | URL |
|---|---|
| Home | https://crowdworks.jp/ |
| 会員登録（メール画面。**Googleではじめる** あり） | https://crowdworks.jp/user/new_email |
| ワーカー向け案内 | https://crowdworks.jp/for-employee |
| 仕事を受注する方法 | https://crowdworks.jp/pages/guides/employee/index |
| はじめての方へ | https://crowdworks.jp/pages/guides/new_user |
| 本人確認ブログ（上げない。停止テキスト） | https://blog.crowdworks.jp/archives/5685/ |
| デジタル認証アプリ本人確認（上げない） | https://blog.crowdworks.jp/archives/6465/ |

Public HTML on `/user/new_email` (2026-09-16) listed:

- メールアドレスではじめる
- **Googleではじめる**
- Yahoo! JAPAN IDではじめる

Yahoo: ignore. Facebook if it appears later: ignore.

### Guess only (placeholders — do not type unless the live page shows them)

```
{{SIGNUP_URL_GUESS_CW_GOOGLE}}     # OAuth deep link — UNCONFIRMED. Click the visible Google button instead.
{{URL_GUESS_CW_SIGNUP_ALT}}        # e.g. /user/new — UNCONFIRMED. Prefer /user/new_email.
{{URL_GUESS_CW_PROFILE_EDIT}}      # in-app: プロフィール編集 / ワーカー情報編集. Live menu wins.
{{URL_GUESS_CW_SKILL_EDIT}}        # in-app: スキル登録. Live menu wins.
{{URL_GUESS_CW_IDENTITY}}          # 本人確認書類提出 — OPEN ONLY TO CONFIRM THE LABEL, THEN CLOSE. No files.
```

Reject lookalikes: `crowdworks.com`, `crowd-works.jp`, extra hyphens. Official host is **`crowdworks.jp`**.

WAF / 「ページを正しく表示できませんでした」/ Press & Hold: common on this host. `holdDurationMs: 1800`, one retry `2500`. If the schema lacks the field, STOP the session.

---

## 2. Google MAIN notes (this desk)

1. Land on https://crowdworks.jp/user/new_email (or home → 会員登録).
2. Click **Googleではじめる**. Picker: **`rimone0511@gmail.com` only**.
3. Consent: basic profile/email. Deny Gmail-read-all / Drive / Contacts dump (`oauth_overreach`).
4. 主な利用方法 = **仕事を受注する**（画面文言の最寄り）。仕事を依頼する を選ばない。
5. Signup 利用規約のチェックは、MAIN Google の **無料会員登録** に必要なときだけ。有料プラン・本人確認・口座の規約は触らない。KYC 条項が同じ画面に混ざっていたら止める。
6. If Google address already registered: **ログイン**, do not duplicate.
7. 確認メール: parent Gmail MCP. CU does not open Gmail.
8. After login, if you land on a **クライアント** dashboard: switch to ワーカー. If switch requires KYC, stop.

Already a member with MAIN Google: `already_member_draft`. Still no 応募.

---

## 3. Profile paste fields (JP)

Live form wins. Third-party blogs mention 自己PR **1024字**・ひとこと **35字** — **unconfirmed official caps**. Use the on-screen counter. Skip optional legal / payout.

| 画面の項目（公開ガイド + 通説。画面を正） | 貼る値 | 必須見込み | メモ |
|---|---|---|---|
| Google | `{{GOOGLE_ACCOUNT_EMAIL}}` | 優先 | |
| メール | `{{EMAIL}}` | メール経路 | |
| パスワード | 書かない | メール経路のみ | |
| 主な利用方法 | **仕事を受注する** | 必須 | |
| 氏名 | `{{LEGAL_NAME_KANJI}}` | 高 | 後のKYCと一致させる必要あり、だが **今は上げない** |
| 氏名カナ | `{{LEGAL_NAME_KANA}}` | 高 | |
| 表示 / ユーザー名 | `{{DISPLAY_NAME}}` | 高 | |
| 生年月日 | `{{BIRTH_YEAR}}-{{BIRTH_MONTH}}-{{BIRTH_DAY}}` | 高 | |
| 郵便番号・住所 | `{{POSTAL_CODE}}` `{{PREFECTURE}}` `{{CITY}}` | 下書きに必要なら | 公開/非公開があれば **非公開** |
| 電話 | SMS play のときだけ | 通常スキップ | |
| 職種 | エンジニア / IT / 業務効率化 / 開発の最寄り | 高 | 詳細職種は複数可なら自動化・API・ドキュメント |
| 受注可能な仕事 | システム開発、業務効率化、ITコンサル、技術文書の最寄り | 高 | ライティング mill だけに寄せない |
| ステータス | 対応可能です（または 仕事内容によります） | 任意 | |
| 稼働可能時間/週 | 空 または 要相談 | 任意 | 数字を創作しない |
| 時間単価 | **空** | 任意 | **創作しない**。案件ごとに決まる、と通説。空が無理ならユーザーに聞く |
| ウェブ会議 | 可（テキスト優先の旨は自己PRへ） | 任意 | |
| 年齢層の公開 | オフ if possible | 任意 | |
| ひとことアピール | 下記 | 高 | 一覧に出る。短く |
| 自己PR | 下記 800 字級 | 高 | |
| ポートフォリオ | `{{PORTFOLIO_URL}}` `{{GITHUB_REPO_AUTOPILOT}}` | 高 | |
| 経歴 | 公開実録の範囲のみ | 任意 | 年数創作禁止 |
| 顔写真 | `{{PROFILE_PHOTO_LOCAL_PATH}}` | 任意 | ポートレートのみ |
| インボイス登録番号 | **空。触らない** | KYC/税 | STOP |
| 口座 | **空。触らない** | KYC | STOP |

### ひとことアピール（貼る）

第三者は 35 字以内と書く。カウンタを正とする。

```
AI業務自動化と手順書。公式APIのみ。
```

（20字。余白があれば「ブラウザ自動操作なし」を足してよい。件数は足さない。）

### JA bio 200（予備・短い自己PR）

```
石田祐太。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIによる業務自動化の手順・つまずき・確認できた結果を、むずかしい言葉を避けて公開しています。公式APIだけを使う動画アップロード道具も公開中です。ブラウザ自動操作はしません。人が検品できる形で、繰り返し作業を自動化します。リモート可。未確認の数字は書きません。公開は人が決めます。秘密は貼りません。根拠を残す方針です。
```

### 自己PR（主ペースト）

```
石田祐太（Yuta Ishida）です。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIを使って毎日の作業を自動化する手順、つまずいた点、確認できた結果を、むずかしい言葉を避けて公開しています。売り物は「動いたように見える自動化」ではなく、人が検品できる仕組みです。

【対応できること】
・繰り返し作業の自動化設計（目的・範囲・合格条件・停止条件を先に切る）
・表計算・GAS・公式APIをつなぐフロー（n8n / Make / Zapier は依頼者が継続できる側）
・Claude Code や Codex に実装を任せるときの指示、検品、失敗時の切り分け
・YouTube Data API v3 / TikTok Content Posting API だけの投稿の仕組み（TikTok を無人投稿とは書きません）
・鍵の扱い、公開事故、トークン期限など、止まりやすい箇所の点検

【公開している道具】
Autopilot Log（https://github.com/rimone0511/autopilot-log）。公式APIのみ。投稿の門番は壊れても非公開側に倒れます。

【受けないこと】
ブラウザ自動操作・スクレイピング、いいねやフォローや閲覧の自動化、権利のない投稿代行、パスワード・API鍵・本人確認書類の代理入力、未確認のままの公開。

テキスト中心。リモート可。週次の稼働時間は案件ごとに相談します。未確認の件数や年数は書きません。秘密はチャットに貼らないでください。独立した個人です。クラウドワークスや n8n、AI ラボの社員・認定ではありません。
```

Do not paste sibling **提案文** (`earn-jp-proposal-drafts-20260916/01-spreadsheet-gas-crowdworks.md`) into a job. That folder is **DO NOT SEND**.

---

## 4. Package / service DRAFT fields

### 4.1 What exists on CrowdWorks (do not invent a gig shop)

Official worker pages describe **探す → 応募 → 契約 → 仮払い → 納品**. Three request types: プロジェクト / コンペ / タスク.

A 2025 community thread on-site says **「クラウドワークスにはランサーズの様な出品機能はありません」**. Treat **worker 職種・受注可能な仕事・スキル・自己PR** as the catalog.

**Do not:**

- Open PARK (`https://park.jp/` or `*.park.jp`) to “make up” a package
- Open AI CrowdWorks seller pre-register
- Click 応募する / 提案を送る / 見積もりを出す on a live job
- Start タスク形式 work (that is commerce, not draft)

### 4.2 Skills DRAFT（貼る名前。経験年数は空）

Register only names. If the form demands 年数, leave empty or 未経験に近い正直な画面値 — **do not inflate**.

- n8n
- 業務自動化
- API連携
- Google Workspace
- 技術文書 / 手順書
- Python（任意。実録の範囲）
- GAS（任意）

Do not add `xAI` or `Grok` as skills.  
Do not take スキル検定 in this session (timebox; not KYC, but not required for draft).

### 4.3 If a live “サービス出品 / パッケージ / 商品登録” appears anyway

Then it is a **new UI**. Rules:

- Fill title/body from Lancers package draft in `01-lancers.md` §4 (same product).
- Amounts stay `{{PRICE_YEN_DRAFT}}` empty.
- Save as draft. Do not 公開 / 掲載.
- If save = publish, **skip** (`no_draft_path`).

### 4.4 Fees — do not invent, do not paste into fields

Official worker FAQ on 2026-09-16 public pages says registration/応募 is **0円**, and that a **システム利用料** is taken from received reward (the marketing page currently prints a percent range).

- Cite only: https://crowdworks.jp/for-employee and https://crowdworks.jp/pages/guides/employee/index
- **Do not copy a percent into git as a fact we set.** Re-read live help before any human prices a job.
- Do not type that range into 時間単価, 自己PR, or a made-up listing.

---

## 5. Explicit do-not (this desk)

- 応募 / 提案送信 / コンペ作品アップロード / タスク開始
- 本人確認書類提出 / デジタル認証アプリ
- 口座登録 / クイック出金
- インボイス登録番号
- PARK 出品
- AI CrowdWorks 入口を辿る
- クライアントとして仕事を依頼
- 有料ブースト / 有料会員

---

## 6. What success looks like **before the next desk (Upwork)**

This pack is **complete** when CrowdWorks has **one** of:

| Outcome | Meaning |
|---|---|
| `done-draft` | MAIN Google ワーカー. 自己PR + ひとこと pasted. Skills named if the form allowed. **0 応募**. Publish/listing = no. KYC = none. |
| `already_member_draft` | Same mailbox already in. Profile checked. Still no 応募. |
| `kyc_wait` | 本人確認 / 口座 / マイナ / インボイス screen. Closed without files. Morning user has desk + type. |
| `sms_wait_user` | Draft blocked on SMS. User not in chat. |
| `no_draft_path` | Next click would 応募 or publish a listing. Stopped. |
| `otp_missing` / `hold_failed` / `card_wall` / `oauth_overreach` | Parked with reason. |

**Not** success: “応募1件送った”, “仮払い案件を取った”, “本人確認済み”, “PARK ショップを作った”.

Secret-free log line:

```
desk: CrowdWorks
pack: earn-lancers-cw-cu-handoff-20260916/02-crowdworks.md
auth: google-main | email-same-mailbox | already_member | blocked
otp: gmail-parent | sms-chat | none | otp_missing | sms_wait_user
kyc: none | wait-morning + type
draft_profile: yes/no
draft_skills: yes/no
applications_sent: 0
park_or_ai_cw: not-opened
publish: no
holdDurationMs_used: <e.g. 1800 or none>
next: STOP this pack. Upwork is the following Wave A desk (sibling runbook), not these files.
```

Do not start Upwork from this folder. Hand the CU serial back to `earn-cu-runbook-20260916/RUNBOOK.md` A5 if that sibling exists.

---

## 7. Stop-light (this desk)

| You see | You do |
|---|---|
| Googleではじめる | Click; pick `rimone0511@gmail.com` |
| Press & Hold / 長押し / WAF | `holdDurationMs` 1800 → retry 2500 |
| 認証メール | Parent Gmail MCP |
| SMS | User chat |
| 仕事を依頼する | Back out. 受注する |
| 応募する | Do not click |
| 本人確認 / 口座 | Stop. Morning user |
| PARK / AI CrowdWorks | Close. Wrong product |
