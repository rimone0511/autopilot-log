> **MAIN Google mailbox only.** Register HTML has **no** Google signup control (GTM ≠ OAuth). Use `{{EMAIL}}`. Do not open Facebook (login ended) or a desk-only address.
> **DRAFT_ONLY.** Profile **draft / input only**. **No interview booking.** No 応募. No 担当電話.
> **Interview-heavy.** Official flow is 無料登録 → **エージェント面談** → **企業面談** → 契約. Early CU **stops before 面談予約**.
> **STOP.** See [STOP.md](STOP.md). Identity / NDA / 口座 / マイナンバー: do not upload.
> **No secrets.** No passwords, OTP, CSRF/`_token`, phones, or ID photos in git or chat.
> **No invented fees.** Official copy: 登録・利用は無料. 仲介マージン％ is **not** on official HTML → do not invent (do not paste third-party 10–25%).
> **This PR does not sign up.** Public GET only.

# NOTE — B07 ITプロパートナーズ (profile-only early CU)

Stamp: **2026-09-16 JST**  
Folder: `ops/earn/itpropartners-profile-only-20260916/`  
Gate here: **`profile_only`** (interview-heavy). **Not** skip-agent. **Not** a live register GO.

This is an **early CU note** for one desk. Allowed later action (human GO only) is **profile draft**. Booking エージェント面談 / 電話ヒアリング / 企業面談 is **out of scope**.

| キー | 値 |
|---|---|
| this_folder | **B07** |
| QUEUE | **B17** (not QUEUE B7 ストアカ) |
| leftover-folder B17 | Freelancermap — **different desk** ([PR#69](https://github.com/rimone0511/autopilot-log/pull/69)) |
| cu_serial | **CU-28** |
| activity_gate (sibling) | **pass** ([PR#12](https://github.com/rimone0511/autopilot-log/pull/12)) |
| gate **this folder** | **`profile_only`** — live public cards **and** the seller path is 面談 |
| Google | **NOT_OFFERED_OAUTH** → MAIN mailbox + email form |
| self_serve | **partial** (web register open; then agent) |
| official | https://itpropartners.com/ |
| signup | https://itpropartners.com/register |
| login | https://itpropartners.com/login |
| jobs | https://itpropartners.com/job |
| jobs_example | https://itpropartners.com/job/sale-4 |
| flow | https://itpropartners.com/blog/flow-itpropartners/ |
| CU hint | `pack_ready` + `pending` (see [STATUS.md](STATUS.md)) |

Do **not** use `/signup` as the register entry (this GET: 200 + 「お探しのページは見つかりませんでした」. Cases shell).  
`www.itpropartners.com` **DNS fail** this env. Official host is **itpropartners.com**.

## Why `profile_only` (interview-heavy)

Public listings are alive (this GET). That does **not** make this a self-serve bid desk.

Home 「ご利用の流れ」 (this GET, logged out):

1. **会員登録** — サイト上から「無料」会員登録
2. **エージェント面談** — 「電話、もしくは**面談予約**にてヒアリング」
3. **案件紹介・企業面談** — 専属エージェントが紹介。企業との面談
4. **契約・業務開始** — 契約締結。参画後フォロー

Blog flow (https://itpropartners.com/blog/flow-itpropartners/ 200):

1. ご登録（Web。**登録・利用は無料**。登録後「担当者からご連絡」）
2. **プロ面談**（カウンセリング。オフィスで担当エージェント）
3. **ご推薦と企業面談**（日程調整は担当エージェント）
4. **内定・ご契約**（個別契約書 / 秘密保持契約書）
5. 参画中サポート

`unknown` 仲介％ does **not** override `profile_only`. Official 面談 / ヒアリング / 面談予約 copy is enough.

Marketing totals and 「週2、3日の案件数は…随一」 are **not** activity proof.

## Early CU — allowed (human GO only; not this PR)

Do **not** start from this folder while Wave A `pending` / `blocked_skip` is open, and do **not** treat this as next CU after Freelancer.com ([PR#72](https://github.com/rimone0511/autopilot-log/pull/72) **REGISTER-CU-CUT** / jobs-first). If a **human GO** later names this desk:

1. Open https://itpropartners.com/register — 職種 **エンジニア** (nearest. Do not pick AI-only if that label is absent). This GET choices: エンジニア / マーケター / デザイナー / 事業責任者・プロデューサー / 人事・総務 / 経理・財務 / 広報・PR / 営業・コンサルタント / ディレクター / 経営者・CXO.
2. メール = `{{EMAIL}}` (MAIN Google mailbox). Password **not** stored in git. Login copy: Facebook ログイン終了 → 登録アドレスからパスワード設定リンク.
3. Skills / bio / URLs from sibling paste pack (**do not copy bodies here**). **Draft / input only.**
4. If the UI has 下書き保存, save unpublished. If 「登録を完了する」 creates the account, **stop unless** parent Gmail OTP is available; still **no 応募 / no 面談**.
5. **Stop.** Close the tab. Do not book 面談. Do not take the 担当者 phone path.

Placeholders only: `{{EMAIL}}` `{{LEGAL_NAME_KANJI}}` `{{LEGAL_NAME_KANA}}` `{{PHONE}}` `{{PREFECTURE}}` `{{CITY}}` `{{PORTFOLIO_URL}}` `{{GITHUB_REPO_AUTOPILOT}}`. 希望単価 empty. **Do not copy card 月額 bands into 希望単価.**

## Early CU — forbidden (see STOP.md)

- **面談予約** / 電話ヒアリングの日程確定 / オフィス来訪の確定
- 企業面談の調整を CU が確定すること
- 案件カードの **応募** / **気になる** / 詳細からのエントリー送信
- 営業電話・チャットに CU が出ること（朝メモだけ）
- 身分証 / NDA / 個別契約書の代行署名 / 口座 / マイナンバー
- `/signup` を登録入口にする。採用担当者導線。新規 Facebook

## Pointers (do not copy paste bodies)

| Sibling | What it is | Use |
|---|---|---|
| [PR#12 `records/10-itpropartners.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-activity-gate-waveb-jp-fced/earn-activity-gate-waveB-20260916/records/10-itpropartners.md) | JP Wave B activity-gate **pass** | Freshness already judged. This folder does not re-score `pass` → `dead` |
| [PR#30 `03-itpropartners.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-waveb-cu-handoff-batch2-87d0/earn-waveb-cu-handoff-batch2-20260916/03-itpropartners.md) | Thick CU-28 field map + JA bios | Paste source **if** a human GO happens. Bios **not** duplicated here |
| [PR#30 STOP-KYC CU-28](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-waveb-cu-handoff-batch2-87d0/earn-waveb-cu-handoff-batch2-20260916/STOP-KYC.md) | Identity / 契約 | Long KYC rows. This folder adds **面談予約 STOP** |
| [PR#72 `b07-itpropartners/CU-NOTE.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/waveb-alive-cu-serial-5788/ops/earn/waveb-alive-cu-serial-20260916/b07-itpropartners/CU-NOTE.md) | Wave B alive serial play 5/6 | Serial is **REGISTER-CU-CUT**. Do not chain Freelancer → this desk |
| [PR#34 `06-itpropartners.md`](https://github.com/rimone0511/autopilot-log/pull/34) | Week2-rest paste | Pointer only |

This folder does **not** rewrite those PRs.

## This GET (2026-09-16, no login)

- `/` 200 — title「ITプロパートナーズ｜フリーランス専門エージェント」。CTA「まずは、Emailで無料登録」。Flow 01–04 as above. フルリモート / 週2日 copy. **POST not sent.**
- `/register` 200 — title includes「週2回」からの…。見出し「あなたの職種を教えてください」。Form has POST + hidden `_token` — **not submitted. Token not recorded.** Google signup control: **none** (GTM only).
- `/login` 200 — 「facebookログインの提供は終了致しました。登録アドレスよりパスワード設定リンクの発行をお願いいたします」。Google でログイン: **none**.
- `/signup` 200 — body「お探しのページは見つかりませんでした」。**Not** the register entry.
- `/job` 200 — 公開カード 最終更新日 **2026/09/15** 例「【TypeScript】CXM領域におけるCREエンジニア…」「【Python/JavaScript】介護DX開発における要件定義エンジニア…」。Also **2026/09/14…08**. 件数は数えない。月額は案件表示であり GMV / 希望単価ではない。
- `/job/sale-4` 200 — 最終更新日 **2026/09/08**「【プロジェクトマネジメント】コーポレートIT／社内情報システム…」; **2026/09/05**「【営業】M&A事業部立ち上げにおけるアポ獲得…」
- `/blog/flow-itpropartners/` 200 — ①無料登録 → ②プロ面談 → ③企業面談 → ④契約（個別契約書 / 秘密保持契約書）
- `/terms` 200 — 同系統の「お探しのページは見つかりませんでした」シェル。規約本文はこのGETで薄い → 貼る直前に画面で開く
- Home link 個人情報: `https://hajimari.inc/policy` (運営。本文は本フォルダでは未引用)

`thin_site_skip`: **false**. Desk is live. Early action remains **profile-only**.

## Skip / park this desk if

面談予約 UI / 電話必須で本人不在 / OTP 欠 / 身分証アップロード / NDA 同意画面. Then **do not** invent a next Wave B register desk from here (cut; prefer JOBS). Record only secret-free keys in [STATUS.md](STATUS.md).
