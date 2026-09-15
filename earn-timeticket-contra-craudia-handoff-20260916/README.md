# CU handoff — TimeTicket / Contra / クラウディア（DRAFT 2026-09-16）

Pack date: 2026-09-16  
Public-page check date: 2026-09-15  
GO: earn-ops Wave A remaining (`A7` → `A8` → `A9`)  
Mode: **DRAFT_ONLY**. Human paste. Computer-use may fill forms from these files. Nobody publishes.

These files are the missing Top10 paste packs for:

| CU直列 | QUEUE | 机 | このフォルダ |
|---|---|---|---|
| CU-07 | A7 | TimeTicket | [07-timeticket.md](07-timeticket.md) |
| CU-08 | A8 | Contra | [08-contra.md](08-contra.md) |
| CU-09 | A9 | クラウディア Craudia | [09-craudia.md](09-craudia.md) |

They resolve the runbook placeholders `{{PASTE_PACK_TIMETICKET}}` / `{{PASTE_PACK_CONTRA}}` / `{{PASTE_PACK_CRAUDIA}}` while sibling INDEX still lists `earn-packs/timeticket/` etc. as `unknown`. Do not copy this folder into those legacy paths in this PR.

Not a live listing. Not KYC. Not a bid. Not a claim of employment with TimeTicket, Contra, Craudia, n8n, Google, or xAI.

## Hard rules (all three desks)

- **MAIN Google only.** Same identity as QUEUE / CU runbook. Placeholder: `{{GOOGLE_ACCOUNT_EMAIL}}`. Do not create a second mailbox, `+desk@…`, LINE, Apple, Facebook, Yahoo, or X just for this GO.
- **DRAFT_ONLY.** Save profile / ticket / Independent page. Do not Publish / 公開する / 発行手続きを完了する / Submit for review if that equals public. Do not apply, bid, or send proposals from this folder (EN proposal paste lives in a sibling pack).
- **Stop KYC.** No ID, My Number reverse, selfie-with-ID, address proof, bank, Stripe, Persona, or tax number. Hand the desk name and screen type to the **morning user**. See [STOP-KYC.md](STOP-KYC.md).
- **No off-platform pay.** No 中抜き, 直接取引, cash, bank transfer, PayPal, crypto wallet, or “email me instead”. Stay in each site’s official message / escrow path. See [HANDS-AND-TOS.md](HANDS-AND-TOS.md).
- **No secrets** in git or session logs (no passwords, OTP, phone digits, ID images, account numbers).
- **No invented fees.** Cite the live help/pricing page. Put amounts only in placeholders (`{{TICKET_PRICE_JPY}}`, `{{HOURLY_USD}}`). Do not invent GMV, guest counts, or “you can earn”.
- Live form wins over this pack. Patch nothing in git during a CU session except a secret-free session line.

## Desk one-liners

| 机 | CU がやること | ここで止める |
|---|---|---|
| TimeTicket | ホスト側のプロフィール下書き。チケットは **非同期（メッセージ）優先**。対面・電話・電話相談チケットは作らない | 本人確認アップロード。チケットの **発行完了**（公開相当） |
| Contra | **Independent / Share work** のページ。サインアップは **Free**。Pro は買わない（クライアントが付くまで Free） | Wallet / Persona。Discover を意図してオンにしない |
| クラウディア | ワーカー登録 → プロフィール下書き。応募しない。スキル出品しない | マイページ「本人確認」（書類+自撮り）。口座・出金 |

## Files

| File | Use |
|---|---|
| [07-timeticket.md](07-timeticket.md) | CU-07 field map + ticket draft (async) |
| [08-contra.md](08-contra.md) | CU-08 Independent page (Free) |
| [09-craudia.md](09-craudia.md) | CU-09 worker profile + KYC path note |
| [STOP-KYC.md](STOP-KYC.md) | Morning-user slip. Agents do not upload |
| [HANDS-AND-TOS.md](HANDS-AND-TOS.md) | Off-platform / 中抜き / 直接取引 |

## Shared placeholders

Replace locally. Never commit filled values.

```
{{GOOGLE_ACCOUNT_EMAIL}}
{{EMAIL}}
{{PASSWORD_DO_NOT_STORE}}
{{LEGAL_NAME_KANJI}}
{{LEGAL_NAME_KANA}}
{{DISPLAY_NAME}}
{{HANDLE}}
{{BIRTH_YEAR}} / {{BIRTH_MONTH}} / {{BIRTH_DAY}}
{{PREFECTURE}}
{{CITY}}
{{PHONE}}
{{PHOTO_LOCAL_PATH}}
{{PORTFOLIO_URL}}
{{GITHUB_URL}}
{{GITHUB_REPO_AUTOPILOT}}
{{TICKET_PRICE_JPY}}
{{HOURLY_USD}}
{{ONE_SPECIFIC_DETAIL}}
```

Suggested **public** URLs (already public, OK to type on the desks):

- Site: `https://yutalab.dev/`
- Tooling example: `https://github.com/rimone0511/autopilot-log`

Do not type a real phone, ID number, tax ID, or OTP into git.

## Activity (no invented counts)

| 机 | Verdict | Public evidence on 2026-09-15 |
|---|---|---|
| TimeTicket | **alive** | Category index https://www.timeticket.jp/categories/ lists live categories including `IT/プログラミング`. Help articles for 通常チケット and ホスト禁止行為 load. |
| Contra | **alive** | https://contra.com/pricing (“Join Contra for free”). Help: onboarding Independent, identity via Persona, paid projects. |
| クラウディア | **alive** | https://www.craudia.com/ FAQ 151 (signup Google/Yahoo/Facebook/Twitter or email), FAQ 103 (KYC at withdrawal), FAQ 72 (fees after採用), FAQ 164 (直接取引禁止). |

Not used: marketing member totals, PR earnings stories, or third-party “how much you can earn” tables.

## Sibling packs (do not duplicate)

- QUEUE: `earn-register-expand-20260916/QUEUE.md` (PR#1)
- CU serial: `earn-cu-runbook-20260916/RUNBOOK.md` (PR#7)
- INDEX: `earn-register-pack-index-20260916/INDEX.md` (PR#8) — these three desks were `unknown`
- Morning KYC 1枚: `earn-kyc-morning-checklist-20260916/` (PR#4)
- EN proposal (Contra apply/reply only): `earn-en-proposal-drafts-20260916/` (PR#5)

## Out of scope

- Creating accounts from an unattended agent with no human OTP path
- Buying Contra Pro / TimeTicket ads / Craudia PRO paid upsell
- Fiverr Gig, Upwork Catalog, JP/EN proposal send
- Wave B desks
- Autopilot Log YouTube/TikTok upload
