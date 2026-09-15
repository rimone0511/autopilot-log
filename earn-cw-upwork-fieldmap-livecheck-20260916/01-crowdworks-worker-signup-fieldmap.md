> DRAFT_ONLY paste hints. NO login. NO secrets. NO 応募. Live labels after email-verify are **`needs_check`**.
> Placeholders: [PLACEHOLDERS.md](PLACEHOLDERS.md). KYC: [STOP-KYC.md](STOP-KYC.md).

# CrowdWorks — worker signup field map

Desk: CrowdWorks（クラウドワークス） worker / 仕事を受注する  
Livecheck: 2026-09-16, logged-out public HTML + official help/docs/blog only  
Host: `crowdworks.jp` only (reject `crowdworks.com`, `crowd-works.jp`)

This is a **field map**, not a CU serial desk. Do not send 応募. Do not open PARK / AI CrowdWorks.

---

## A. Public signup (step 1) — livechecked

**URL (confirmed):** https://crowdworks.jp/user/new_email  
**HTML title:** 会員登録【クラウドワークス】  
**POST (from public JS, no submit performed):** `POST /user/send_email_verification` field name `email_verification_key[email]`

Public JS (`packs/raw_pages/user/new_email.ts-*.js`, gzip-decompressed 2026-09-16) and the rendered help-fetch of the same URL agree on these **labels**:

| UI label (as shown / in JS) | `required_guess` | DRAFT_ONLY paste hint | Evidence |
|---|---|---|---|
| カンタン新規会員登録 | heading | — | JS string + help-fetch of `/user/new_email` |
| メールアドレスではじめる | `required (docs)` if this path is used | `{{EMAIL}}` (MAIN Google mailbox). **Do not submit** from this agent | JS `label-text` + 利用規約 第4条(2) 電子メールアドレスを保有 |
| 会員登録する（無料） | submit control | Do not click in this livecheck | JS + https://crowdworks.jp/for-employee 「登録・仕事への応募：0円」 |
| 他のアカウントではじめる | heading | Prefer Google | JS |
| `{provider}ではじめる` | `needs_check` which providers still render | Help-fetch of the live page (2026-09-16) listed **Googleではじめる** and **Yahoo! JAPAN IDではじめる**. Yahoo: ignore. Facebook: ignore if it appears. Click **Googleではじめる** only when a human is doing signup later | Help-fetch of https://crowdworks.jp/user/new_email ; JS interpolates `` `${value}ではじめる` `` |
| 利用規約 | `required (docs)` to become 会員 | Human reads. Agent does not check the box | JS + https://crowdworks.jp/pages/agreement 第4条(4) |
| 個人情報の取り扱い | `required (docs)` (paired with 利用規約 on this screen) | Human reads https://crowdworks.jp/pages/privacy_policy | JS: 「利用規約および個人情報の取り扱いについて同意の上、登録してください。」 |
| ログインはこちら | n/a | If already a member: login, do not duplicate (規約 第4条(3)(7) 既会員・複数アカウント禁止) | JS |
| ホームに戻る | n/a | — | JS |

**Not on this public step (needs_check later):** password, ユーザー名, 氏名, 住所, 職種, reCAPTCHA. Those appear only after email/OAuth — we did not send email or start Google OAuth.

Help for Google/Yahoo/Facebook as existing login methods (password set at 退会 time):  
https://crowdworks-help.zendesk.com/hc/ja/articles/5006115447198

---

## B. Membership eligibility (not form labels, but they constrain signup)

From 利用規約 第4条 https://crowdworks.jp/pages/agreement

| Constraint | `required_guess` | Paste hint |
|---|---|---|
| 本人が手続（代理人不可） | `required (docs)` | Operator only |
| 登録情報は全て真実 | `required (docs)` | No US name, no fake DOB |
| 満18歳以上（個人） | `required (docs)` | `{{BIRTH_*}}` honest |
| 電子メールアドレス | `required (docs)` | `{{EMAIL}}` |
| 未会員 / アカウント1つ | `required (docs)` | Do not create a second worker identity |
| 利用規約に同意 | `required (docs)` | Human |
| 適法に就労できること | `required (docs)` | Japan-resident worker is fine; do not claim a work-visa you do not have |

「登録情報」= 会員登録手続で入力・提供された一切の情報（第2条(14)）. That is a **legal definition**, not a field list.

---

## C. After email / Google — member-info form

**Not livechecked.** Completing this step would send a verification mail or start OAuth (forbidden here).

Help names these **screens** after you are a member (so they exist; whether they are on the first post-email wizard is `needs_check`):

| Screen / control named in official help | `required_guess` | DRAFT_ONLY paste hint | Cite |
|---|---|---|---|
| プロフィール編集 | navigation | Start here after login | 退会ヘルプ steps 1–2: 表示名 → プロフィール編集 → 共通情報の「基本情報編集」 https://crowdworks-help.zendesk.com/hc/ja/articles/5006115447198 |
| 基本情報編集 | `needs_check` (exists; which widgets are required to save unknown) | Legal identity fields if present: `{{LEGAL_NAME_KANJI}}` `{{LEGAL_NAME_KANA}}` `{{BIRTH_*}}` `{{POSTAL_CODE}}` `{{PREFECTURE}}` `{{CITY}}`. Prefer 非公開 if a toggle exists (`needs_check`) | same 退会 article |
| 表示名 | `needs_check` required-to-save | `{{DISPLAY_NAME}}` | ユーザー名ヘルプ treats 表示名 as a later setting: https://crowdworks-help.zendesk.com/hc/ja/articles/5158870018974 |
| ユーザー名 | `needs_check` (immutable once set) | Do not treat as a nickname you can fix later. Help: 変更することはできません。表示名設定後はサイト上で確認できない | same |
| メールアドレス・パスワード編集 → パスワード / パスワード確認 | email-path or before 退会 | **Do not paste.** Local ledger only | 退会ヘルプ (Google/Yahoo/Facebook 登録者) |
| 個人 / 法人 | `needs_check` on wizard; help documents 切替 | **個人** for this operator. 法人 KYC is a different document set — STOP | アカウント登録セクション title 「個人アカウントと法人アカウントの切替方法」 https://crowdworks-help.zendesk.com/hc/ja/sections/4988001693854 · 法人本人確認 https://crowdworks-help.zendesk.com/hc/ja/articles/5006083877150 |
| 主な利用方法 / 仕事を受注する | `needs_check` (label not in official help body we retrieved; worker vs client **roles** are defined in 規約 第2条) | Choose **ワーカー / 仕事を受注する** if the live wizard shows it. Do not register as クライアント | 規約 第2条(4)(5) · https://crowdworks.jp/pages/guides/new_user |

### Collected-data **types** (privacy policy) — not proven form labels

https://crowdworks.jp/pages/privacy_policy lists 住所・氏名・電話番号・電子メールアドレス、クレジットカード情報、ログインID、パスワード、ニックネーム and, under 共同利用, 生年月日・性別.

| Privacy-policy name | Map to live label? | `required_guess` | Paste hint |
|---|---|---|---|
| 電子メールアドレス | step 1 メールアドレスではじめる | `required (docs)` on email path | `{{EMAIL}}` |
| ログインID | likely ユーザー名 (`needs_check`) | `needs_check` | `{{DISPLAY_NAME}}` is the wrong token if the field is the immutable ユーザー名 |
| パスワード | パスワード / パスワード確認 | email path | do not write |
| ニックネーム | maybe 表示名 (`needs_check`) | `needs_check` | `{{DISPLAY_NAME}}` |
| 氏名 | unknown live label (氏名 / お名前) | `needs_check` | `{{LEGAL_NAME_KANJI}}` |
| 住所 | unknown | `needs_check` | `{{POSTAL_CODE}}` `{{PREFECTURE}}` `{{CITY}}` — skip extra 番地 if the form allows |
| 電話番号 | unknown | `needs_check` | skip unless blocked; `{{PHONE}}` |
| 生年月日 | unknown | `needs_check` (18+ is required by 規約) | `{{BIRTH_*}}` |
| 性別 | unknown | `needs_check` | skip / 非公開 if offered |
| クレジットカード情報 | STOP | `STOP` | client-side; not worker draft |

---

## D. Worker profile screens (login-gated)

https://crowdworks.jp/employee/new redirected to `/login` on 2026-09-16. Labels below are from **official blog + help**, not from a filled form.

### D1. ワーカー情報編集

Path named officially: **プロフィール編集 > ワーカー情報編集**

| UI label | `required_guess` | DRAFT_ONLY paste hint | Cite |
|---|---|---|---|
| ひとことアピール | `needs_check` (feature exists; not called 必須 in the launch post) | Short public line. Hint (count on-screen; no official cap in the post): `AI業務自動化と手順書。公式APIのみ。` Do not put email/phone | https://blog.crowdworks.jp/archives/4855/ (2022-07-15). Shown on 公開ページ and クラウドワーカーを探す |
| 職種 | `needs_check` | Nearest live values: エンジニア / IT / 開発 / 業務効率化. Help exists for missing 職種 choices | https://blog.crowdworks.jp/archives/6180/ 「プロフィール編集」の「ワーカー情報編集」から職種変更 · ヘルプ title 【ワーカー】職種選択項目がない場合の対応について https://crowdworks-help.zendesk.com/hc/ja/sections/4988001693854 |
| ウェブ会議 | `needs_check` | Official values in 2022-07 blog roundup: **できる / できない**. Hint: できる (text-first is for 自己PR, not this control) | https://blog.crowdworks.jp/archives/date/2022/07/ |
| 自己PR | `needs_check` as form-required; **used in client search** | Paste from sibling CU pack, or the 800-class block in that pack. Keep secrets out. Help: 表示名検索では出ないことがあり、**自己PRのキーワード**で探す | https://crowdworks-help.zendesk.com/hc/ja/articles/5006084347294 |
| ステータス | `needs_check` (named on 公開プロフィール in **2012** blog) | If still present: 対応可能です **or** 仕事内容によります — pick live radio. Do not invent busyness | https://blog.crowdworks.jp/archives/date/2012/10/ |
| スキル / スキルの一覧 | `needs_check` | Names only: n8n, 業務自動化, API連携, 技術文書. No fake 年数. Skip スキル検定 | 2012 blog + worker guide 「経歴やスキル」 https://crowdworks.jp/pages/guides/employee/index |
| 希望時間単価 | `needs_check` | **`{{PRICE_YEN_DRAFT}}` empty.** Do not type 5–20% システム利用料 into this box | 2012 blog · fee page is https://crowdworks.jp/pages/guides/employee/fee |
| 稼働可能時間/週 | `needs_check` | Empty or 要相談. Do not invent hours | 2012 blog |

2012 labels are **`needs_check`** because the post is old. If the 2026 editor dropped a control, skip it.

### D2. Other profile menus named in official help/blog

| UI label | `required_guess` | DRAFT_ONLY paste hint | Cite |
|---|---|---|---|
| ポートフォリオ / コンペ採用作品 | `optional (docs)` as a destination for コンペ作品; adding extra items `needs_check` | `{{PORTFOLIO_URL}}` `{{GITHUB_REPO_AUTOPILOT}}`. No ID files | Help title 【ワーカー/コンペ形式】コンペ採用作品がポートフォリオに掲載されない場合 https://crowdworks-help.zendesk.com/hc/ja/sections/4988001693854 |
| 公開プロフィール | public page | 個人情報の開示は任意. 公開ページは **未ログインでも閲覧可能** | https://crowdworks-help.zendesk.com/hc/ja/articles/5006098829982 |
| 本人確認書類提出 | `STOP` | Confirm label, close | [STOP-KYC.md](STOP-KYC.md) |
| 振込先口座 / ゆうちょ銀行 | `STOP` | Payout, not draft | 規約 第17条5項 · fee page 個人口座 |

---

## E. What worker signup is **not**

Official worker flow is 探す → 応募 → 契約 → 仮払い → 納品  
https://crowdworks.jp/pages/guides/employee/index · https://crowdworks.jp/for-employee

| Do not | Why |
|---|---|
| 応募する / 提案を送る / コンペ提出 / タスク開始 | Commerce, not a field map |
| Type システム利用料 % into 自己PR or 時間単価 | Fee table is https://crowdworks.jp/pages/guides/employee/fee — re-read live before any human prices a job |
| Fill インボイス登録番号 | 規約 第5条; STOP |
| Use PARK / AI CrowdWorks | Different products |

---

## F. Source list (CrowdWorks)

- Signup: https://crowdworks.jp/user/new_email
- はじめての方へ: https://crowdworks.jp/pages/guides/new_user
- 仕事を受注する方法: https://crowdworks.jp/pages/guides/employee/index
- 受注したい方: https://crowdworks.jp/for-employee
- ワーカーシステム利用料: https://crowdworks.jp/pages/guides/employee/fee
- 利用規約: https://crowdworks.jp/pages/agreement
- 個人情報保護方針: https://crowdworks.jp/pages/privacy_policy
- ユーザー名: https://crowdworks-help.zendesk.com/hc/ja/articles/5158870018974
- 退会 / 基本情報編集 / Googleパスワード: https://crowdworks-help.zendesk.com/hc/ja/articles/5006115447198
- 個人情報の開示: https://crowdworks-help.zendesk.com/hc/ja/articles/5006098829982
- ワーカー検索と自己PR: https://crowdworks-help.zendesk.com/hc/ja/articles/5006084347294
- アカウント登録セクション: https://crowdworks-help.zendesk.com/hc/ja/sections/4988001693854
- 本人確認セクション: https://crowdworks-help.zendesk.com/hc/ja/sections/4987979705374
- ひとことアピール: https://blog.crowdworks.jp/archives/4855/
- 職種変更: https://blog.crowdworks.jp/archives/6180/
- マイナンバーカード書類: https://blog.crowdworks.jp/archives/5685/
- デジタル認証アプリ: https://blog.crowdworks.jp/archives/6465/
