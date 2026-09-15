# Deep CU paste — Skill Shift / SOKUDAN / MENTA / Anycrew / ストアカ

Pack date: 2026-09-16  
Public-page check: 2026-09-16（公開 HTML・公式ヘルプ・公開 JS ラベル。**ブラウザ登録はしていない**）  
Audience: Computer-use（CU）直列の **後続エージェント**、および人が貼る下書き  
Operator: 石田祐太 / Yuta Ishida (`rimone0511`)  
Mode: **DRAFT_ONLY**. このフォルダは手渡しパック。アカウントではない。KYC ではない。公開 GO ではない。

対象 5 机（QUEUE Wave B。INDEX の CU 番号は兄弟索引を正とする）:

```
Skill Shift（skill-shift.com）  = this pack, desk 1  / CU-27  / activity_gate pass
SOKUDAN（ソクダン）              = this pack, desk 2  / CU-13  / activity_gate pass
Anycrew                          = this pack, desk 3  / CU-15  / activity_gate needs_check
MENTA                            = this pack, desk 4  / CU-16  / activity_gate needs_check
ストアカ（Street Academy）        = this pack, desk 5  / CU-17  / activity_gate needs_check
```

これは JP Week2 薄パック（`earn-register-packs-jp-20260916/`）と Wave B サンプル（`earn-waveb-alive-handoff-sample-20260916/`）の **深掘り**。本文は複製せず、プロフィール欄・Google メモ・KYC 停止・手数料の公式引用を厚くする。

QUEUE の `https://skillshift.jp/` は 2026-09-16 に **ホスト解決失敗**。開いた公式は **https://www.skill-shift.com/**（活動ゲート PR#12 と同じ）。

これらのファイルは貼り付け文法である。Skill Shift / SOKUDAN / MENTA / Anycrew / ストアカ / n8n / xAI / Google との雇用・提携ではない。

---

## Hard rules

- No secrets in these files or in git（実パスワード、API 鍵、身分証番号、OTP 数字、口座なし）。
- PLACEHOLDER のみ。ローカル台帳で置換。埋めた値をコミットしない。
- **MAIN Google only**（`{{GOOGLE_ACCOUNT_EMAIL}}` = `rimone0511@gmail.com`）。机専用メールを作らない。
- **Gmail OTP = parent**（Gmail MCP）。CU は `mail.google.com` を開かない。
- **SMS OTP = user chat.** 推測しない。二台目の電話を使わない。
- **STOP at KYC.** [STOP-KYC.md](STOP-KYC.md)。
- **Do not publish.** 応募しない。プラン／講座を公開しない。スカウト返信で契約しない。
- Press & Hold: 必ず **`holdDurationMs`**。[00-google-otp-hold.md](00-google-otp-hold.md)。
- **手数料％は公式の公開ページに出た文言だけ。** 出ていなければ `needs_check`。ブログ・記憶・他机の料率を転記しない。
- この markdown を書いているエージェントは **登録しない**。CU 直列だけが、これらの規則の下でブラウザに入力してよい。

## Files

| File | What it is |
|---|---|
| [CU-PROMPT.md](CU-PROMPT.md) | 後続 CU への貼りスタブ |
| [00-google-otp-hold.md](00-google-otp-hold.md) | MAIN Google、Gmail 親、SMS=user、`holdDurationMs` |
| [01-skill-shift.md](01-skill-shift.md) | B16 / CU-27。メール登録（Google OAuth は公開 JS に無い） |
| [02-sokudan.md](02-sokudan.md) | B1 / CU-13。PREFER_GOOGLE |
| [03-anycrew.md](03-anycrew.md) | B5 / CU-15。PREFER_GOOGLE。人材側のみ |
| [04-menta.md](04-menta.md) | B6 / CU-16。PREFER_GOOGLE。プラン公開は出品 |
| [05-street-academy.md](05-street-academy.md) | B7 / CU-17。NOT_OFFERED_OAUTH。講座公開しない |
| [STOP-KYC.md](STOP-KYC.md) | 身分証 / マイナンバー / Stripe / 口座 / eKYC |
| [INDEX.md](INDEX.md) | このパック内の貼る順 |
| [METHOD.md](METHOD.md) | 観測方法と HTTP |

## Shared placeholders

Replace locally. Never commit filled values.

```
{{FULL_LEGAL_NAME}}
{{LEGAL_NAME_KANJI}}
{{LEGAL_NAME_KANA}}
{{DISPLAY_NAME}}
{{EMAIL}}
{{GOOGLE_ACCOUNT_EMAIL}}
{{PASSWORD_DO_NOT_STORE}}
{{COUNTRY}}
{{CITY}}
{{PREFECTURE}}
{{POSTAL_CODE}}
{{STREET_ADDRESS}}
{{BIRTHPLACE}}
{{TIMEZONE}}
{{PHONE}}
{{PHONE_E164}}
{{BIRTH_YEAR}}
{{BIRTH_MONTH}}
{{BIRTH_DAY}}
{{PROFILE_PHOTO_LOCAL_PATH}}
{{PHOTO_LOCAL_PATH}}
{{PORTFOLIO_URL}}
{{WEBSITE_URL}}
{{GITHUB_URL}}
{{GITHUB_REPO_AUTOPILOT}}
{{YEARS_AUTOMATION_PUBLIC}}
{{FAV_AREA}}
{{INVITE_CODE}}
{{GENDER_FORM_VALUE}}
{{PRICE_YEN_DRAFT}}
```

Suggested public URLs（すでに公開。机に打ってよい）:

- Site: `https://yutalab.dev/`
- GitHub: `https://github.com/rimone0511`
- Tooling example: `https://github.com/rimone0511/autopilot-log`

Do not type a real phone, ID number, or tax ID into git.

Public defaults（CU チャットに出してよい）:

| Token | Public default |
|---|---|
| `{{GOOGLE_ACCOUNT_EMAIL}}` / `{{EMAIL}}` | `rimone0511@gmail.com`（ログイン識別。受信箱の中身は秘密） |
| `{{DISPLAY_NAME}}` | `石田祐太` / `Yuta Ishida` |
| `{{COUNTRY}}` | `Japan` |
| `{{TIMEZONE}}` | `Asia/Tokyo` |
| `{{PORTFOLIO_URL}}` / `{{WEBSITE_URL}}` | `https://yutalab.dev/` |
| `{{GITHUB_URL}}` | `https://github.com/rimone0511` |
| `{{GITHUB_REPO_AUTOPILOT}}` | `https://github.com/rimone0511/autopilot-log` |
| `{{PRICE_YEN_DRAFT}}` | **empty** — 円額を創作しない |

## Signup URLs — confirmed vs guess

**Use confirmed URLs first.** Guess 行はプレースホルダ。発明した OAuth コールバックを打たない。

| Desk | Status | URL |
|---|---|---|
| Skill Shift home | confirmed | https://www.skill-shift.com/ |
| Skill Shift 個人登録 | confirmed（canonical / 公開 title） | https://www.skill-shift.com/sign-up |
| Skill Shift login | confirmed（公開シェル） | https://www.skill-shift.com/login |
| Skill Shift terms | confirmed | https://www.skill-shift.com/terms-of-service |
| skillshift.jp | **dead DNS**（2026-09-16 `Could not resolve host`） | 使わない |
| SOKUDAN home | confirmed | https://sokudan.work/ |
| SOKUDAN 人材登録 | confirmed | https://sokudan.work/signup/pro |
| SOKUDAN Google signup | confirmed（登録 HTML） | `/users/auth/google?category=signup&usage_type_id=1` |
| Anycrew 人材 | confirmed | https://app.any-crew.com/ |
| Anycrew 案内 | confirmed | https://www.any-crew.com/ |
| Anycrew 企業 | confirmed — **閉じる** | https://biz.any-crew.com/ |
| MENTA home | confirmed | https://menta.work/ |
| MENTA 登録経路選択 | confirmed | https://menta.work/index.php/register/choose |
| MENTA Google OAuth | confirmed（登録 HTML） | https://menta.work/index.php/oauth/google |
| ストアカ home / register / teach | **WAF 405** this env | https://www.street-academy.com/ |
| ストアカ 講師メディア | confirmed 200 | https://teach.street-academy.com/ |
| ストアカ 手数料ヘルプ | confirmed URL。this env GET **403** | https://support.street-academy.com/hc/ja/articles/200700579 |

Reject lookalikes: `skillshift.jp`, `skillshift.global`（別法人の NL コンサル）, `anycrew.com` 誤綴り, `menta.jp` vs `menta.work`, `storeka` 非公式ドメイン.

## Activity note

| Desk | activity_gate (PR#12) | This pack |
|---|---|---|
| Skill Shift | **pass**（公開 `GET /api/jobs` に 2026-09-14 前後の `created_at`） | 現場のみの行は応募しない。机全体は現地労働 SKIP にしない |
| SOKUDAN | **pass**（トップに案件見出し） | マーケ「リモート 92%」は活動証明に使わない |
| Anycrew | **needs_check**（`/offers` は SPA 空） | 人が 1 画面見てから進める |
| MENTA | **needs_check**（プラン一覧が環境により WAF） | 登録面は 2026-09-16 に HTTP 200 |
| ストアカ | **needs_check**（www WAF。ヘルプ Cloudflare） | 死滅ではない。人がヘルプを再読 |

件数・GMV・「○万人」は書かない。`pagination.total` も書かない。

## Seller one-liners

English: n8n / AI automation + operator docs. Official APIs only. No browser scraping. No engagement bots.

日本語: AI業務自動化と手順書。公式APIのみ。ブラウザ自動操作・いいね自動化はしない。公開は人が決める。

## Sibling packs（複製しない。あれば参照）

| Placeholder | Expected path |
|---|---|
| `{{QUEUE}}` | `earn-register-expand-20260916/QUEUE.md` |
| `{{CU_RUNBOOK}}` | `earn-cu-runbook-20260916/RUNBOOK.md` |
| `{{JP_WEEK2}}` | `earn-register-packs-jp-20260916/` |
| `{{WAVEB_SAMPLE}}` | `earn-waveb-alive-handoff-sample-20260916/` |
| `{{WAVEB_GATE}}` | `earn-activity-gate-waveB-20260916/` |
| `{{KYC_MORNING}}` | `earn-kyc-morning-checklist-20260916/` |
| `{{MASTER_INDEX}}` | `earn-register-pack-master-index-20260916/` |

兄弟が無くても **このフォルダだけで 5 机を走れる**。ライブフォームを正とする。

## What this pack will not do

- Wave A（Fiverr / Lancers / CrowdWorks 等）を再開する
- Workship / 複業クラウド / CrowdLinks / Shufti をこの直列に入れる
- Skill Shift の **企業会員・パートナー** 画面
- Anycrew / SOKUDAN の発注者コンソール
- 提案送信・応募・プラン公開・講座公開
- 有料プラン購入
- 手数料％の創作

## Verification (this PR)

Markdown handoff only. Python posting-gate tests are unchanged. No account was created from this authoring agent.
