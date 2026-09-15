# CU handoff — Lancers + CrowdWorks (after Fiverr)

Pack date: 2026-09-16  
Public-page check: 2026-09-15 / 2026-09-16（公開HTMLと公式ヘルプ。ブラウザ登録はしていない）  
Audience: the **next computer-use (CU) serial agent** after Fiverr  
Operator: 石田祐太 / Yuta Ishida (`rimone0511`)  
Mode: **DRAFT_ONLY**. This folder is a playbook. It is not a live account, not a KYC packet, and not a publish GO.

Serial (Wave A remaining, from sibling runbook / QUEUE):

```
Fiverr (already in progress / park it first)
  → Lancers（ランサーズ）     = this pack, desk 1
  → CrowdWorks（クラウドワークス） = this pack, desk 2
  → Upwork                   = NOT this pack. Stop after CrowdWorks.
```

Coconala and Gumroad are QUEUE `done-draft`. Do not reopen them to publish.

These files are paste + CU input grammar. They are not employment or partnership with Lancers, CrowdWorks, n8n, xAI, OpenAI, or Google.

---

## Hard rules

- No secrets in these files or in git (no real passwords, API keys, IDs, tax numbers, OTP digits).
- Use PLACEHOLDER tokens only. Replace locally. Never commit filled values.
- **MAIN Google only** (`{{GOOGLE_ACCOUNT_EMAIL}}` = `rimone0511@gmail.com`). No second mailbox.
- **Gmail OTP = parent** (Gmail MCP). CU does not open `mail.google.com`.
- **SMS OTP = user chat.** Do not guess. Do not use a second phone.
- **STOP at KYC.** See [STOP-KYC.md](STOP-KYC.md).
- **Do not publish.** No 公開する / 完了-as-publish / 応募 / 提案送信.
- Press & Hold: always set **`holdDurationMs`**. See [00-google-otp-hold.md](00-google-otp-hold.md).
- Do not invent traffic counts, GMV, years of experience, or **fees**. Fee % belongs on the live official help page at paste time, not in this pack.
- Do not create accounts from an agent session that is **authoring** this markdown. The CU serial agent may type in a browser under these rules.

## Files

| File | What it is |
|---|---|
| [CU-PROMPT.md](CU-PROMPT.md) | Paste stub for the next CU agent |
| [00-google-otp-hold.md](00-google-otp-hold.md) | MAIN Google, Gmail parent, SMS=user, `holdDurationMs` |
| [01-lancers.md](01-lancers.md) | A3 desk: signup, JP profile paste, パッケージ DRAFT |
| [02-crowdworks.md](02-crowdworks.md) | A4 desk: signup, JP profile paste, worker-service DRAFT |
| [STOP-KYC.md](STOP-KYC.md) | Identity / マイナンバー / 口座 / 出金 hard stop |

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
{{LANCERS_USERNAME}}
{{COUNTRY}}
{{CITY}}
{{PREFECTURE}}
{{POSTAL_CODE}}
{{TIMEZONE}}
{{PHONE_E164}}
{{BIRTH_YEAR}}
{{BIRTH_MONTH}}
{{BIRTH_DAY}}
{{PROFILE_PHOTO_LOCAL_PATH}}
{{PORTFOLIO_URL}}
{{WEBSITE_URL}}
{{GITHUB_URL}}
{{GITHUB_REPO_AUTOPILOT}}
{{PRICE_YEN_DRAFT}}
{{LEAD_TIME_DRAFT}}
{{INVITE_CODE}}
```

Suggested public URLs (already public, OK to type on the desks):

- Site: `https://yutalab.dev/`
- GitHub: `https://github.com/rimone0511`
- Tooling example: `https://github.com/rimone0511/autopilot-log`

Do not type a real phone, ID number, or tax ID into git.

Public defaults (safe to show in CU chat):

| Token | Public default |
|---|---|
| `{{GOOGLE_ACCOUNT_EMAIL}}` / `{{EMAIL}}` | `rimone0511@gmail.com` (login identity; inbox contents stay secret) |
| `{{DISPLAY_NAME}}` | `石田祐太` / `Yuta Ishida` |
| `{{COUNTRY}}` | `Japan` |
| `{{TIMEZONE}}` | `Asia/Tokyo` |
| `{{PORTFOLIO_URL}}` / `{{WEBSITE_URL}}` | `https://yutalab.dev/` |
| `{{GITHUB_URL}}` | `https://github.com/rimone0511` |
| `{{GITHUB_REPO_AUTOPILOT}}` | `https://github.com/rimone0511/autopilot-log` |
| `{{PRICE_YEN_DRAFT}}` | **empty** — do not invent a yen amount |

## Signup URLs — confirmed vs guess

**Use confirmed URLs first.** Guess rows are placeholders only. Do not type an invented OAuth callback.

| Desk | Status | URL |
|---|---|---|
| Lancers home | confirmed (QUEUE + public) | https://www.lancers.jp/ |
| Lancers 新規会員登録 | confirmed (public title 2026-09-16) | https://www.lancers.jp/user/sign_up/ |
| Lancers login | confirmed (public title 2026-09-16) | https://www.lancers.jp/user/login |
| Lancers Google OAuth deep link | **GUESS only** | `{{SIGNUP_URL_GUESS_LANCERS_GOOGLE}}` — follow the visible **Google** button on the confirmed signup page. Do not invent `/auth/google`. |
| CrowdWorks home | confirmed (QUEUE + public) | https://crowdworks.jp/ |
| CrowdWorks 会員登録（メール画面。Googleボタンあり） | confirmed (public HTML 2026-09-16: 「Googleではじめる」) | https://crowdworks.jp/user/new_email |
| CrowdWorks ワーカー案内 | confirmed | https://crowdworks.jp/for-employee |
| CrowdWorks Google OAuth deep link | **GUESS only** | `{{SIGNUP_URL_GUESS_CW_GOOGLE}}` — click **Googleではじめる** on the confirmed page. |
| Post-login profile / 出品 URLs | **GUESS only** | See each desk card. Live in-app menu wins. |

Reject lookalikes: `lancers.com` vs `lancers.jp`, `crowd-works` typos, `crowdworks.com` vs `crowdworks.jp`.

## Activity note

Verdict: **alive** (both desks)

Evidence from public pages (no GMV or job-count invented):

- Lancers homepage and `/user/sign_up/` load. Help articles for 会員登録, ソーシャルログイン, 本人確認, パッケージ出品 are live on `lancers.jp/faq`.
- CrowdWorks homepage registration screen `/user/new_email` loads and lists **Googleではじめる**. Worker guide `crowdworks.jp/pages/guides/employee/index` and `/for-employee` load.

Not used: marketing totals (“日本最大級”, worker-count banners). Those are vendor UI copy, not a measured gate count.

## Seller one-liners (if a field is missing from the desk card)

English: n8n / AI automation + operator docs. Official APIs only. No browser scraping. No engagement bots.

日本語: AI業務自動化と手順書。公式APIのみ。ブラウザ自動操作・いいね自動化はしない。公開は人が決める。

## Sibling packs (do not duplicate; resolve if present)

| Placeholder | Expected path |
|---|---|
| `{{QUEUE}}` | `earn-register-expand-20260916/QUEUE.md` |
| `{{CU_RUNBOOK}}` | `earn-cu-runbook-20260916/RUNBOOK.md` |
| `{{FIVERR_GIG_PACK}}` | `earn-fiverr-gig-draft-20260916/` |
| `{{JP_PROPOSAL_DRAFTS}}` | `earn-jp-proposal-drafts-20260916/` — **do not send** |
| `{{KYC_MORNING}}` | `earn-kyc-morning-checklist-20260916/` |
| `{{PASTE_PACK_LANCERS}}` | `earn-register-packs-top10-20260916/03-lancers.md` or `earn-packs/lancers/` (may be missing) |
| `{{PASTE_PACK_CROWDWORKS}}` | `earn-register-packs-top10-20260916/04-crowdworks.md` or `earn-packs/crowdworks/` (may be missing) |

If a sibling file is absent, **this folder is enough** to run the two desks. Live form wins over paste.

## What this pack will not do

- Start Upwork, LinkedIn Services, or later Wave A desks
- Wander into **AI CrowdWorks** (QUEUE B15) from the CrowdWorks hostname
- Open CrowdWorks **PARK** (`park.jp`) — different product, not this serial
- Send proposals / 応募 (JP proposal drafts are a different folder)
- Buy paid plans, featured listings, or Fast-Track KYC
- Invent fee percentages into price fields

## Verification (this PR)

Markdown handoff only. Python posting-gate tests are unchanged. No Lancers or CrowdWorks account was created from this authoring agent.
