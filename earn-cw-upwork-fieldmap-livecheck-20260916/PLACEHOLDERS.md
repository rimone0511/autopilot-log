> DRAFT_ONLY. Real values live in the operator’s local ledger only. This repository must not contain live emails, phones, passwords, ID numbers, or bank details.

# Shared placeholders

Reuse these tokens in both field maps. If a live form splits a field (first/last, 漢字/かな), split the same token the form asks for. Do not invent a US/EU identity.

| Token | Meaning | DRAFT_ONLY paste hint |
|---|---|---|
| `{{GOOGLE_ACCOUNT_EMAIL}}` | MAIN Google mailbox | Prefer Google button on CrowdWorks / Continue with Google on Upwork. Do not create a second mailbox for this work |
| `{{EMAIL}}` | Same mailbox if the form shows an email field | Do not type a different address |
| `{{PASSWORD}}` | Local ledger only | **Never write a password in git or chat.** Email-path CrowdWorks only |
| `{{LEGAL_NAME_KANJI}}` | Legal name in kanji | Must be able to match later KYC; **do not upload ID now** |
| `{{LEGAL_NAME_KANA}}` | Legal name in kana | CrowdWorks if the live form shows かな |
| `{{FULL_LEGAL_NAME}}` | Latin-script legal name | Upwork first/last split as the form asks |
| `{{DISPLAY_NAME}}` | Public display name | Hint: `石田祐太` / `Yuta Ishida` — confirm live label (表示名 vs ユーザー名 vs profile name) |
| `{{BIRTH_YEAR}}` `{{BIRTH_MONTH}}` `{{BIRTH_DAY}}` | Date of birth | CrowdWorks 利用規約: 満18歳以上. Do not fake |
| `{{COUNTRY}}` | Country of residence | Honest Japan. Do not spoof US/EU |
| `{{POSTAL_CODE}}` | Postal code | Only if the live form requires it for a **draft** save |
| `{{PREFECTURE}}` `{{CITY}}` | Region / city | Prefer 非公開 when a public/private toggle exists (`needs_check` on CrowdWorks) |
| `{{PHONE}}` | Mobile | Skip unless the form blocks save. SMS OTP → user chat, not this file |
| `{{TIMEZONE}}` | Time zone | Upwork account Location section |
| `{{HOURLY_USD}}` | Upwork profile hourly | **Empty in git.** If save is blocked, park `rate_required` — do not invent USD |
| `{{PRICE_YEN_DRAFT}}` | CrowdWorks 時間単価 | **Empty.** Do not paste official fee % into a rate field |
| `{{PORTFOLIO_URL}}` | Public site | Hint: `https://yutalab.dev/` |
| `{{GITHUB_URL}}` | Public GitHub | Hint: `https://github.com/rimone0511` |
| `{{GITHUB_REPO_AUTOPILOT}}` | Public tool repo | `https://github.com/rimone0511/autopilot-log` |
| `{{PROFILE_PHOTO_LOCAL_PATH}}` | Local portrait file | Do not commit. Upwork: real face, not logo/AI. Skip if the picker is an ID flow |
| `{{INVITE_CODE}}` | Invite / referral | Leave empty unless the operator supplies one |

Do not paste `{{EMAIL}}`, `{{PHONE}}`, or off-platform contact into Upwork overview, title, or portfolio files ([contact-info rule in profile essentials](https://support.upwork.com/hc/en-us/articles/360016252373-How-to-build-your-freelancer-profile-the-essentials)).
