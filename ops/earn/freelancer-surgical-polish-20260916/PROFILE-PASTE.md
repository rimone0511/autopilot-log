> **DRAFT_ONLY.** Profile paste for a human.  
> No signup from this PR. No bids. No contests. No wallet funding. No secrets.  
> Agent does not create the account. Hourly rate stays a form-field placeholder.

# Freelancer.com — profile paste (polish)

Desk: [Freelancer.com](https://www.freelancer.com/) (QUEUE Wave A10 / CU-10)  
Role: **Freelancer / Seller** (not Employer / Buyer)  
Google: **PREFER_GOOGLE** · MAIN Google only  
Language: English paste for a Japan-based operator  
Pack: `ops/earn/freelancer-surgical-polish-20260916/`  
Checked: 2026-09-15 public GET (no login). Re-open the live form before paste.

This file is **headline / summary / skills / optional work-terms**. Bids live in [BID-TEMPLATES.md](BID-TEMPLATES.md) and stay **do-not-send**. Money walls: [MONEY-FLAGS.md](MONEY-FLAGS.md). Identity: [STOP-KYC.md](STOP-KYC.md). Desk box: [STATUS.md](STATUS.md).

Sibling CU still says: profile + skills draft; **no bids; no contests; no “Verify my Identity.”** This polish does not override that.

Public pages (re-verify; do not treat git as the live form):

- Home: https://www.freelancer.com/
- Signup: https://www.freelancer.com/signup
- Edit profile help: https://www.freelancer.com/support/profile/how-to-edit-your-profile
- Skills help: https://www.freelancer.com/support/Profile/how-to-edit-your-list-of-skills
- Portfolio help: https://www.freelancer.com/support/Profile/how-to-add-a-portfolio
- Fees (URL only): https://www.freelancer.com/feesandcharges
- Identity Policy: https://www.freelancer.com/page.php?p=info%2Fkyc_policy
- User Agreement: https://www.freelancer.com/about/terms
- Code of Conduct: https://www.freelancer.com/info/codeofconduct
- Membership (do not buy): https://www.freelancer.com/membership
- Preferred Freelancer (do not apply): https://www.freelancer.com/preferred-freelancer-program

---

## Operator steps (human browser — agent does not sign up)

1. Open https://www.freelancer.com/signup
2. Prefer **Continue with Google** as `{{GOOGLE_ACCOUNT_EMAIL}}` (MAIN Google). Fallback: `{{EMAIL}}` + `{{PASSWORD_DO_NOT_STORE}}`. OTP stays in the mailbox, not in git.
3. Choose **Freelancer** / work-and-get-paid. If you land on Employer / hire, switch. If you cannot switch without KYC or a paid wall, **stop**.
4. Stay on **free** membership. Close upgrade / Preferred / Verified upsells. See [MONEY-FLAGS.md](MONEY-FLAGS.md).
5. Paste headline, summary, and ≤ live free skill cap from this file. Hourly rate = `{{HOURLY_RATE_USD}}` in the **rate field**, or leave empty if the form allows. **Do not invent a rate in git. Do not put a number in the summary paste.**
6. Location: Japan / `{{CITY}}` / `{{COUNTRY}}`. Do not spoof a US/EU flag.
7. **STOP.** Do not Verify my Identity. Do not add a card. Do not fund the Site wallet. Do not bid. Do not enter a contest.

---

## Field map (placeholders only)

Official “Editing my profile” help lists **Hourly Rate, Professional Headline, Top Skills, Summary**. Resume blocks on the same page may include Experience, Reference, Education, Qualification, Publication, Certification, Article. Paste only what the live form asks.

### Account / identity-adjacent

| UI field (typical) | Paste value | Notes |
|---|---|---|
| Signup path | Google | PREFER_GOOGLE |
| Email | `{{EMAIL}}` | Same mailbox as MAIN Google |
| Password | `{{PASSWORD_DO_NOT_STORE}}` | Email path only. Never commit |
| Account type | Freelancer | Not Employer |
| Username | `{{FREELANCER_USERNAME}}` | Pick once. Do not create a second account to retry |
| Full name | `{{FULL_LEGAL_NAME}}` | Must later match ID if KYC is ever done. Do not KYC now |
| Country / flag | `{{COUNTRY}}` | Honest Japan is fine |
| City | `{{CITY}}` | Do not invent a US city |
| Phone | skip | Security phone sits on the KYC path — see [STOP-KYC.md](STOP-KYC.md) |

### Profile

| UI field | Paste value | Notes |
|---|---|---|
| Hourly Rate | `{{HOURLY_RATE_USD}}` | USD **form field**. Empty/skip if allowed. Never invent in git |
| Professional Headline | Headline fence below | Skills + docs. No metric claim |
| Top Skills | Skills list below | Live dropdown is the source of truth. Stay at or under the **free** cap (sibling help: up to 20). Do not buy extra slots |
| Summary | Summary fence below | English. **No live rate in the letter** |
| Profile photo | `{{PROFILE_PHOTO_LOCAL_PATH}}` | Portrait only. Never an ID scan |
| Cover photo | **skip** | If the UI requires paid membership, close it |
| Extra / multiple profiles | **skip** | If the UI requires Plus or higher, close it |
| Portfolio item | optional later | Help’s last step is **Publish**. Skip Publish. No Hire-Me-only items |

### Resume (optional)

Fill only if the live form shows the block. No fake employers. No invented years.

| UI field | Paste value |
|---|---|
| Experience title | `Independent automation + operator docs` |
| Experience summary | One workflow + SOP + official APIs. Public example: Autopilot Log |
| Education / Qualification | leave blank unless true |
| Website / portfolio URL | `{{PORTFOLIO_URL}}` |
| GitHub if a field exists | `{{GITHUB_REPO_AUTOPILOT}}` |

User Agreement: do not advertise an unrelated external website; any URL must relate to the user / service on the site. Public portfolio / GitHub only in fields that ask for work samples. Do not put email, phone, WhatsApp, or “pay me off-site” in the profile.

### Skills (stay at or under the live free cap)

Paste the **nearest live skill names**. Skip a token if the dropdown has no match. Do not invent hidden skill IDs. Do not buy extra slots.

```
n8n
API Integration
Python
Technical Writing
Documentation
Google Workspace
Zapier
Make (Integromat)   ← pick the live label
Automation
Webhooks
Workflow
ChatGPT / AI        ← pick the live label; do not claim a lab affiliation
```

---

## Paste blocks

### Headline

```
n8n and AI automation with operator docs (official APIs, no scraping)
```

### Summary

```
I help small teams stop copy-pasting between tools.

I build n8n workflows and light AI steps (classify, summarize, draft) on official APIs or documented connectors: forms, sheets, CRMs, inboxes, internal APIs. Then I write the docs a non-engineer can follow: what the workflow does, what to do when it fails, and which values are secrets vs. safe to edit.

Typical deliverable:
- One production workflow with retries and a failure alert
- A short SOP / README for the operator
- A change log so the next edit is not guesswork

Public example of that posture: Autopilot Log (YouTube Data API v3 + TikTok Content Posting API; posting gate fails closed) — {{GITHUB_REPO_AUTOPILOT}}. Field notes: {{PORTFOLIO_URL}}.

I am {{DISPLAY_NAME}}, based in Japan, async in {{TIMEZONE}}. English is fine. Keep scoping on Freelancer.com messages. I do not scrape platforms that have no official API. I do not ship likes, follows, or fake views. I do not publish social posts without your own approve/gate step.

I do not take payment or files off Freelancer.com. Hourly rate stays in the rate field, not in this summary.
```

### Work Terms (only if a free-text box exists)

```
Availability: weekdays in {{TIMEZONE}}, async-first.
Payment: Freelancer Milestone / on-platform only. No off-platform payment.
Communication: Freelancer messages first. English. Written requirements before build.
Revisions: scoped in the milestone. Extra scope is a new milestone.
```

---

## Do not paste

- Years of experience, GMV, Job Completion Rate, “Preferred Freelancer,” or traffic counts
- A US/EU address you do not live in
- Email / phone / WhatsApp / Telegram / “pay me outside”
- That Autopilot Log posts TikTok unattended (inbox upload is the default; direct post is gated)
- n8n Expert / Zapier Partner / Make Partner / xAI affiliation
- A live USD rate, wallet balance, or leftover bid count
- Contest / Hire-Me spam, or a second account

---

## After paste (still draft)

- [ ] Headline + summary + skills on the free profile
- [ ] Portrait from a local path (not ID), if you add a photo
- [ ] Membership still free
- [ ] No bid sent, no contest entered, no wallet funded
- [ ] No Verify my Identity — [STOP-KYC.md](STOP-KYC.md)

---

## Placeholders

Replace locally. Never commit filled secrets.

```
{{FULL_LEGAL_NAME}}
{{DISPLAY_NAME}}                 recommended: Yuta Ishida
{{FREELANCER_USERNAME}}
{{EMAIL}}
{{GOOGLE_ACCOUNT_EMAIL}}
{{PASSWORD_DO_NOT_STORE}}
{{COUNTRY}}
{{CITY}}
{{TIMEZONE}}
{{HOURLY_RATE_USD}}              rate field only; do not invent in git
{{PROFILE_PHOTO_LOCAL_PATH}}
{{PORTFOLIO_URL}}                public: https://yutalab.dev/
{{GITHUB_REPO_AUTOPILOT}}        public: https://github.com/rimone0511/autopilot-log
```

## 日本語（運用だけ）

下書きのみ。登録・本人確認・入札・コンテスト・ウォレット入金はしない。時給はフォーム欄。本文に金額を書かない。スキルは無料枠のライブ上限まで。カバー写真や追加プロフィールが有料なら閉じる。
