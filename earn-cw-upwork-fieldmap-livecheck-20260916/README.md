> DRAFT_ONLY field maps. NO login. NO secrets. NO account create. NO KYC upload. NO 応募 / proposal / Catalog submit.
> Built 2026-09-16 from **public help/docs and public HTML only**. Live form after login is out of scope.
> Required vs optional guesses that were not proven on a live, logged-out form are marked **`needs_check`**.

# CrowdWorks worker signup + Upwork freelancer profile — field map livecheck

Folder: `earn-cw-upwork-fieldmap-livecheck-20260916/`

This pack is **not** a computer-use playbook. Sibling CU paste packs (`earn-lancers-cw-cu-handoff-20260916/`, `earn-upwork-linkedin-cu-handoff-20260916/`) stay the paste source of truth for bios. This folder only maps **label names**, **required vs optional (with `needs_check`)**, **DRAFT_ONLY paste hints**, and **cited URLs**.

| File | Purpose |
|---|---|
| `01-crowdworks-worker-signup-fieldmap.md` | CrowdWorks: public signup step + worker-profile screens named in official help/blog |
| `02-upwork-freelancer-profile-fieldmap.md` | Upwork: signup (help-only) + freelancer profile sections from Help Center |
| `PLACEHOLDERS.md` | Shared `{{…}}` tokens. Real PII stays off git |
| `STOP-KYC.md` | Identity / tax / payout / My Number hard stop |

## Livecheck (this environment, 2026-09-16)

No CrowdWorks or Upwork session. No Google OAuth. No email send.

| URL | Result | Used as |
|---|---|---|
| https://crowdworks.jp/user/new_email | HTTP 200. Title `会員登録【クラウドワークス】`. Vue app; public JS names the email field | Confirmed signup step 1 labels |
| https://crowdworks.jp/user/new | Redirects to `/user/new_email` | Same as above |
| https://crowdworks.jp/employee/new | Redirects to `/login` (not a public form) | Worker-profile editor is **login-gated** → remaining labels from help/blog only |
| https://crowdworks.jp/pages/guides/new_user | 200 | Worker vs client overview |
| https://crowdworks.jp/pages/guides/employee/index | 200 | 応募 uses 経歴 / スキル; 登録 0円 |
| https://crowdworks.jp/for-employee | 200 | 登録・応募 0円; システム利用料 5–20% |
| https://crowdworks.jp/pages/agreement | 200 | Age 18+, email, true 登録情報 |
| https://crowdworks.jp/pages/privacy_policy | 200 | Collected-data **types**, not live form labels |
| https://blog.crowdworks.jp/archives/4855/ | 200 | Official label **ひとことアピール** |
| https://www.upwork.com/ and `/nx/signup/` | HTTP **403** from this host (Cloudflare) | Signup wizard labels **not** live-checked here |
| Upwork Help Center articles listed in `02-…` | Some articles returned body via help fetch; some later 403/Cloudflare | Profile section names from Help copy, not from a logged-in editor |

## How to read the tables

| `required_guess` value | Meaning |
|---|---|
| `required (docs)` | Official help/docs say you must have this to register, to reach 100% profile, or to submit proposals |
| `optional (docs)` | Official help/docs list it as optional or as one of several ways to fill remaining completion % |
| `needs_check` | Label or required-state is inferred (privacy-policy data types, old blog, conflicting help numbers, or a form we could not open without login). **Live screen wins.** |
| `STOP` | Identity / tax / payout. Do not paste, upload, or submit |

Paste hints are placeholders only. Do not invent hourly USD, yen rates, years of experience, or client counts.

## Out of scope

- Logging in, completing email OTP, or creating an account
- Uploading ID, My Number, liveness, tax forms, bank, Payoneer, Wise
- 応募 / 提案 / Connects / Catalog Submit
- Copying third-party blog “must fill these 6 boxes” lists as facts (excluded; public **official** help/docs only)

## Verification

Markdown only. Existing Python posting-gate tests are unchanged. No marketplace account was created from this agent.
