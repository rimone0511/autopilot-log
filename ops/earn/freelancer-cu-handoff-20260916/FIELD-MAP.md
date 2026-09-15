> **DRAFT_ONLY.** Paste-ready EN. No secrets. Live form wins.  
> Seller-brand = Yuta Ishida / ユタラボ / official APIs only / operator docs / pay on Freelancer.com.  
> Real passwords, OTP, phone, street address, bank, ID numbers are **not** in this repository.

CU steps: [PLAYBOOK.md](PLAYBOOK.md)  
Money walls: [MONEY-FLAGS.md](MONEY-FLAGS.md)  
KYC: [STOP-KYC.md](STOP-KYC.md)

Official profile help lists **Hourly Rate, Professional Headline, Top Skills, Summary**. Support bodies often fail in a plain GET — the **live counter and dropdown** win. If a fence is too long, cut; do not wrap a second bio into the headline.

---

## Shared placeholders

Replace locally. Never commit filled private values.

```
{{FULL_LEGAL_NAME}}
{{DISPLAY_NAME}}
{{FREELANCER_USERNAME}}
{{EMAIL}}
{{GOOGLE_ACCOUNT_EMAIL}}
{{PASSWORD_DO_NOT_STORE}}
{{COUNTRY}}
{{CITY}}
{{PREFECTURE}}
{{TIMEZONE}}
{{PHONE}}
{{HOURLY_RATE_USD}}
{{PROFILE_PHOTO_LOCAL_PATH}}
{{PORTFOLIO_URL}}
{{GITHUB_URL}}
{{GITHUB_REPO_AUTOPILOT}}
{{YEARS_AUTOMATION_PUBLIC}}
```

Public defaults (login identity + already-public URLs only. Inbox contents are secret):

| Token | Public default |
|---|---|
| `{{GOOGLE_ACCOUNT_EMAIL}}` / `{{EMAIL}}` | `rimone0511@gmail.com` |
| `{{DISPLAY_NAME}}` | `Yuta Ishida` |
| `{{COUNTRY}}` | `Japan` |
| `{{TIMEZONE}}` | `Asia/Tokyo` |
| `{{PORTFOLIO_URL}}` | `https://yutalab.dev/` |
| `{{GITHUB_URL}}` | `https://github.com/rimone0511` |
| `{{GITHUB_REPO_AUTOPILOT}}` | `https://github.com/rimone0511/autopilot-log` |
| `{{HOURLY_RATE_USD}}` | **empty** — do not invent USD |
| `{{YEARS_AUTOMATION_PUBLIC}}` | **empty** — skip if unconfirmed |
| `{{PHONE}}` | **do not use** unless draft save is blocked and the **user** already placed a number in chat |
| `{{PASSWORD_DO_NOT_STORE}}` | local only — never git |
| `{{FREELANCER_USERNAME}}` | pick once at paste time — do not commit a retry alias |
| `{{CITY}}` / `{{PREFECTURE}}` | ledger (no street) |

---

## A. Signup / login (MAIN Google, then email)

Evidence: public GET 2026-09-15 of `/signup` and `/login` (no POST). Required marks = live form.

| UI field (this GET) | Paste value | `required_guess` | Notes |
|---|---|---|---|
| Continue with Google | MAIN `{{GOOGLE_ACCOUNT_EMAIL}}` | **prefer** | PLAYBOOK path A. Tracking-style control: LoginSignupMethod Google |
| Continue with Facebook | **do not** | n/a | Do not create a new identity |
| First Name | given name from `{{FULL_LEGAL_NAME}}` | email path | `/signup` `DetailsForm-FirstNameInput` |
| Last Name | family name from `{{FULL_LEGAL_NAME}}` | email path | `DetailsForm-LastNameInput` |
| Email | `{{EMAIL}}` (same MAIN mailbox) | email path | `DetailsForm-EmailInput`. Placeholder **Email** |
| Password | `{{PASSWORD_DO_NOT_STORE}}` | email path | Hint on this GET: *Min 6 characters of lower and uppercase or a number.* Never commit |
| User Agreement + Privacy Policy checkbox | agree if prompted | email path | `DetailsForm-TermsOfUseCheckbox`. Do not paste legal text into chat |
| Login: Email or Username | `{{EMAIL}}` or `{{FREELANCER_USERNAME}}` | login | `CredentialsForm-EmailInput` |
| Login: Password | `{{PASSWORD_DO_NOT_STORE}}` | login | Do not use Forgot Password unless the user asks |
| Remember me | optional | n/a | Not a second account |
| Account type / role | **Freelancer** / seller | if asked | Not on the first `/signup` GET this session — **live wizard wins**. Not Employer |
| Username | `{{FREELANCER_USERNAME}}` | if asked | Pick once |
| Country / city | `{{COUNTRY}}` / `{{CITY}}` | if asked | Honest Japan. No US/EU spoof |
| Phone | skip | skip | Security phone sits on KYC — [STOP-KYC.md](STOP-KYC.md) |

reCAPTCHA may appear on signup/login. That is **not** KYC. If it blocks the pass, park `hold_failed` and hand the **screen type** to morning human. Do not invent a bypass.

---

## B. Profile (this CU pass — paste these)

| UI field | Paste value | Notes |
|---|---|---|
| Hourly Rate | `{{HOURLY_RATE_USD}}` | USD **form field**. Empty/skip if allowed. Never invent in git. **Not** in the summary fence |
| Professional Headline | Headline fence below | Skills + docs. No metric claim |
| Top Skills | Skills list below | Live dropdown is source of truth. Stay at or under the **free** cap (sibling help: up to 20). Do not buy extra slots |
| Summary | Summary fence below | English. No live rate in the letter |
| Profile photo | `{{PROFILE_PHOTO_LOCAL_PATH}}` | Portrait only. Never an ID scan |
| Cover photo | **skip** | Official help: cover photo **requires a paid membership**. Do not pay |
| Extra / multiple profiles | **skip** | Official help: extra profiles are Plus or higher. Do not buy |
| Portfolio item | optional later | Help’s last step is **Publish**. Skip Publish. No Hire-Me-only items |
| Website | `{{PORTFOLIO_URL}}` | Only in a field that asks for a work sample. User Agreement: URL must relate to the user / service on the site |
| GitHub | `{{GITHUB_REPO_AUTOPILOT}}` | Same rule |

### Resume (optional)

Fill only if the live form shows the block. No fake employers. No invented years.

| UI field | Paste value |
|---|---|
| Experience title | `Independent automation + operator docs` |
| Experience summary | One workflow + SOP + official APIs. Public example: Autopilot Log |
| Education / Qualification | leave blank unless true |

Do not put email, phone, WhatsApp, or “pay me off-site” in any profile slot.

---

## C. Skills (profile chips only — not a catalog listing)

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

## D. Paste fences

Contact lines stay out. After substituting placeholders, **recount** against the live counter.

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

### One-liner (if the wizard is shorter than Headline)

```
Official-API automation plus operator docs. Pay on Freelancer.com.
```

---

## E. STOP rows (not paste targets)

Appearance = close the dialog. Do not map “how to fill.”

| Screen / control | Action |
|---|---|
| Verify my Identity | Close — [STOP-KYC.md](STOP-KYC.md) |
| Keycode photo (face + ID + code) | Close |
| Proof of address / utility / bank statement | Close |
| Security Phone Number inside that KYC wizard | Close |
| Site wallet / deposit / Minimum Account Balance | Close — [MONEY-FLAGS.md](MONEY-FLAGS.md) |
| Bid / Place Bid / Submit proposal | Close this pass (surgical = later) |
| Contest / Submit entry | Close — **no contests** |
| Sponsored / Highlight / Sealed | Skip |
| Preferred Freelancer / Recruiter apply | Close |
| Membership / Plus / extra skill slots / cover unlock | Close (`card_wall` if it demands a card) |
| Facebook as a new identity | Close |

---

## F. Bid amount fields (later GO only — empty in git)

Do **not** fill these on this CU pass. Listed so a later human does not invent numbers into git.

| Field | Placeholder | This pack |
|---|---|---|
| Bid amount | `{{BID_AMOUNT_USD}}` | empty; park `rate_required` rather than invent |
| Hourly bid | `{{HOURLY_RATE_USD}}` | empty |
| Delivery days | `{{DELIVERY_DAYS}}` | empty |
| `{{ONE_SPECIFIC_DETAIL}}` | required to send later | skip the listing if it cannot be filled from that page |

Templates: siblings [#47](https://github.com/rimone0511/autopilot-log/pull/47) / [#57](https://github.com/rimone0511/autopilot-log/pull/57). Not copied here.

---

## Do not paste

- Years of experience, GMV, Job Completion Rate, “Preferred Freelancer,” or traffic counts
- A US/EU address you do not live in
- Email / phone / WhatsApp / Telegram / “pay me outside”
- That Autopilot Log posts TikTok unattended
- n8n Expert / Zapier Partner / Make Partner / xAI affiliation
- A live USD rate, wallet balance, leftover bid count, or fee-table numbers
- Contest / Hire-Me spam, or a second account

---

## 日本語（運用だけ）

貼るのは見出し・要約・スキル。時給はフォーム欄だけ。本文に金額・残高・入札残を書かない。Google が無いときだけ同じメール。Facebook で新身分を作らない。入札文はこのフォルダに置かない。
