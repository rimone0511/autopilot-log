# ココナラ初出品フルペースト — n8n 小さな自動化 1本（DRAFT）

Pack date: 2026-09-16  
Public-page check: 2026-09-16  
Desk: ココナラ（Wave A / QUEUE `done-draft` の **JOBS** 初サービス）  
Operator: 石田祐太 / Yuta Ishida (`rimone0511`)  
Mode: **DRAFT_ONLY — 下書き保存まで。公開するな**

These files are paste packs for a human or CU agent. They are not a live service, not an identity submission, and not a claim of employment or partnership with n8n, xAI, OpenAI, Google, or Coconala.

## Hard rules

- No secrets in these files or in git (no real passwords, API keys, IDs, tax numbers, OTP digits).
- Use PLACEHOLDER tokens only. Yen stays `{{TIER_*_YEN}}` / `{{OPTION_*_YEN}}` / `{{YEN}}`.
- **Stop before KYC.** See [STOP-KYC.md](STOP-KYC.md).
- **Do not publish.** See [DRAFT_ONLY.md](DRAFT_ONLY.md).
- MAIN Google only. Honest country. No partner logos.
- Do not invent traffic counts. Activity is `alive`, `thin`, or `needs_check`.
- Do not create the Coconala account from this authoring session. CU may type under [CU-PROMPT.md](CU-PROMPT.md).

## Files

| File | What to paste / do |
|---|---|
| [SERVICE-PASTE.md](SERVICE-PASTE.md) | Title, category guess, TOC, description, FAQ, tiers, days, options, お願い |
| [PLACEHOLDERS.md](PLACEHOLDERS.md) | Yen tokens |
| [CU-PROMPT.md](CU-PROMPT.md) | Next CU agent stub |
| [00-google-otp-hold.md](00-google-otp-hold.md) | Login / OTP / Press & Hold |
| [STOP-KYC.md](STOP-KYC.md) | Identity / tax / 口座 |
| [HANDS-AND-TOS.md](HANDS-AND-TOS.md) | On-site only |
| [METHOD.md](METHOD.md) | Public GET log |
| [DRAFT_ONLY.md](DRAFT_ONLY.md) | Stop list |
| [INDEX.md](INDEX.md) | This folder map |

## Shared placeholders

See [PLACEHOLDERS.md](PLACEHOLDERS.md). Never commit filled values.

Suggested public URLs (already public, OK to type on Coconala):

- Site: `https://yutalab.dev/`
- Tooling example: `https://github.com/rimone0511/autopilot-log`

Do not type a real phone, ID number, or tax ID into git.

## Activity note

Verdict: **alive**

Evidence from public pages on 2026-09-16 (no GMV or job-count invented):

- Homepage https://coconala.com/ loads.
- Category tree includes 業務自動化・効率化支援 (`/categories/230`) and API連携・開発 (`/categories/230/739`). Both list current services; some titles mention n8n.
- Official news for title split, 1500-character サービス内容, and 下書き/公開 UI are live.

Not used: category marketing totals (“4.3万件”, 料金相場 tables). Those are vendor UI copy.

## Official pages used for this pack

- Creating a service page: https://mag.coconala.com/articles/knowhow-the-basics-of-service-pages
- Add service: https://coconala.com/services/add
- Title + catch copy: https://coconala.com/news/170
- Character limits 2026-09-01: https://coconala.com/news/1372
- Seller fee help (403 from this env): https://help.coconala.com/hc/ja/articles/230180287

## Sibling packs (do not duplicate)

| Placeholder | Expected path |
|---|---|
| `{{QUEUE}}` | `earn-register-expand-20260916/QUEUE.md` — Coconala register = `done-draft` |
| `{{JP_PROPOSAL_DRAFTS}}` | `earn-jp-proposal-drafts-20260916/03-llm-ops-coconala-estimate.md` — **DO NOT SEND** |
| `{{FIVERR_GIG_PACK}}` | `earn-fiverr-gig-draft-20260916/` — English Gig; do not copy USD onto this yen form |
| `{{KYC_MORNING}}` | `earn-kyc-morning-checklist-20260916/` |

If a sibling file is absent, **this folder is enough** to draft the first Coconala service. Live form wins over paste.

## What this pack will not do

- Re-register Coconala
- Publish, accept an order, or send an estimate
- Buy セラーサクセス for extra characters
- Copy a competitor n8n listing body
- Invent yen

## Verification (this PR)

Markdown paste pack only. Python posting-gate tests are unchanged. No Coconala service was published from this authoring agent.
