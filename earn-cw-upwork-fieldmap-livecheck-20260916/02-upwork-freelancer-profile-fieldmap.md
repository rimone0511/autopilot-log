> DRAFT_ONLY paste hints. NO login. NO secrets. NO proposals. NO Connects. NO Catalog Submit.
> This host returned **403** on www.upwork.com and `/nx/signup/` (2026-09-16). Signup **wizard** labels are therefore **`needs_check`**. Profile **section** names below are from Upwork Help Center copy.
> Placeholders: [PLACEHOLDERS.md](PLACEHOLDERS.md). KYC: [STOP-KYC.md](STOP-KYC.md).

# Upwork — freelancer profile field map

Desk: Upwork freelancer profile  
Livecheck: 2026-09-16, public Help / Resources only (marketplace HTML blocked here)

Bios, title, and Catalog copy for paste live in sibling `earn-upwork-linkedin-cu-handoff-20260916/`. This file maps **labels** and **required vs optional**.

---

## A. Sign up as a freelancer

Official steps (no field-by-field list):

1. Go to https://www.upwork.com
2. Select **Sign up**
3. Complete the form and start working on your profile

Cite: https://support.upwork.com/hc/en-us/articles/24492534968211-How-to-sign-up-as-a-freelancer-on-Upwork  
(same article also at `…/24492534968211-Register-as-a-freelancer`)

| UI label (help wording) | `required_guess` | DRAFT_ONLY paste hint | Cite / gap |
|---|---|---|---|
| Sign up | control | Do not complete in this livecheck | signup article |
| Continue with Google | preferred path if shown | MAIN Google `{{GOOGLE_ACCOUNT_EMAIL}}`. Help: if you choose Apple or Google, **log in that way every time**. If you sign up with email (even a Google address), use email/username every time | signup article |
| Continue with Apple | ignore | Do not create an Apple ID for this work | signup article |
| email / username path | fallback | `{{EMAIL}}` only. Password not in git | signup article |
| “Complete the form” (unnamed fields) | `needs_check` | Likely first/last name, country, role. **Live wizard wins.** This environment could not open `/nx/signup/` (HTTP 403) | signup article says only “complete the form” |
| Work as a freelancer vs Hire vs Agency | `needs_check` on exact label | Choose **freelancer / find work**, not Hire, not Agency | not enumerated in the signup article; confirm live |
| Freelancer Service Fee / Connects (cost, not a profile field) | n/a | Do not buy Connects. Do not paste a fee % into overview | signup article: fee on earnings; Connects to submit most jobs |

After signup, help says the profile must be **approved** before searching projects (`How does Upwork work` in the same article). Treat “submit profile for review” as `needs_check`: if it opens ID, **STOP**.

---

## B. What is required to apply vs required for 100% complete

Two official layers. Do not collapse them.

### B1. To start submitting proposals

Help (essentials): **you must upload a profile portrait photo** to complete the profile and start submitting proposals.

Beginner resource: to start applying you are required to add:

- A profile photo
- A profile overview
- At least one employment history item
- At least one skill

Cites:

- https://support.upwork.com/hc/en-us/articles/360016252373-How-to-build-your-freelancer-profile-the-essentials
- https://www.upwork.com/resources/upwork-for-beginners

`needs_check`: beginner page and 100%-complete article agree on the same four items; we did not confirm the logged-in editor still blocks proposals without all four.

### B2. 100% complete profile scoring

https://support.upwork.com/hc/en-us/articles/211063188-How-do-I-create-a-100-complete-freelancer-profile  
Help text (retrieved 2026-09-16 via public search/help fetch): you cannot reach 100% if any **Required (50%)** item is missing. Remaining 50% is any mix of optional items.

| Profile item (help table label) | `required_guess` | Weight (help) | DRAFT_ONLY paste hint |
|---|---|---|---|
| Profile Photo | `required (docs)` for 50% + proposals | part of required 50% | `{{PROFILE_PHOTO_LOCAL_PATH}}`. Real current face. Not logo, not AI. Skip if picker is ID/liveness |
| Profile Overview | `required (docs)` | part of required 50% | Sibling overview block. No `{{EMAIL}}` / `{{PHONE}}` |
| At least one Employment History item | `required (docs)` | part of required 50% | Independent / ユタラボ **only if true**. No invented employer or dates |
| At least one Skill tag | `required (docs)` | part of required 50% | Live picker only. Preference: n8n, API Integration, Automation, Technical Writing / Documentation |
| Portfolio Item | `optional (docs)` | 5% each, max 20% | Skip for draft minimum. Title/description rules in enhance article |
| Additional Employment History item(s) | `optional (docs)` | 10% each, max 20% | Skip unless true |
| Additional Skill tags | `optional (docs)` | 10% | Fill toward cap if the picker allows; see §C skills 15 vs 20 |
| Education | `optional (docs)` | 10% each, max 20% | Skip unless a real school. Do not invent degrees |
| Profile Video | `optional (docs)` | 10% | Skip |
| At least one other Linked Account | `optional (docs)` | 10% max 10% | Skip (OAuth overreach risk) |
| Certification | `optional (docs)` | 5% each, max 10% | Skip unless a real current cert |
| At least one Other Experience item | `optional (docs)` | 5% max 5% | Skip |

Help: “How you complete your profile is up to you, there's many different combinations… However, some things are required.”

---

## C. Profile editor sections (help labels)

Edit most sections from **Your profile** with the ✎ or + control. Name and some account fields: **Account settings**. Visibility: **Profile settings**.

https://support.upwork.com/hc/en-us/articles/360000403687-Edit-freelancer-profile  
https://support.upwork.com/hc/en-us/articles/360016252373-How-to-build-your-freelancer-profile-the-essentials

| Help label | `required_guess` | DRAFT_ONLY paste hint | Cite |
|---|---|---|---|
| Profile title | `needs_check` (not in the 100% table; help still documents a title field, 70-character cap) | Sibling title only: `n8n automation with operator docs you can rerun` (47/70). No xAI/Grok keyword stuffing | https://support.upwork.com/hc/en-us/articles/34925678839827-Your-profile-title-and-overview · essentials “How to create your profile title and URL” |
| Profile Link / custom URL | `optional (docs)` Freelancer Plus only | Skip. Do not buy Plus. 4–20 chars A–Z 0–9; may not include “Upwork” | essentials |
| Profile photo | `required (docs)` to propose | See B. Must be an actual picture of you | essentials · https://support.upwork.com/hc/en-us/articles/360053305673-How-to-choose-a-good-profile-picture |
| Overview | `required (docs)` | First **~250 characters** show in search (essentials). No contact info | essentials · title/overview article |
| Hourly rate | `needs_check` (documented as editable starting point; **not** in the 100% required table) | `{{HOURLY_USD}}` empty in git. If save blocks, park `rate_required`. Form also shows Freelancer Service Fee example — do not copy a % into git as our number | essentials “How to add your hourly rate” · https://support.upwork.com/hc/en-us/articles/34926076728467-Determine-your-rate |
| Skills | `required (docs)` at least one | Type-to-search, English spelling, marketplace list only. **Cap conflict:** essentials say **up to 15**; skills article says **up to 20**. **`needs_check` — live picker wins** | essentials · https://support.upwork.com/hc/en-us/articles/211060318-How-do-I-add-skills-to-my-profile |
| English proficiency / Languages | `needs_check` required-at-create | Help: “We’ll ask you about your English proficiency when you create your profile.” Honest self-assess. Hint if picker exists: English (professional working) + Japanese (native). Do not buy IELTS/Duolingo for this pack | essentials · enhance article languages |
| Employment history | `required (docs)` at least one | Title, dates, description as the live form asks. Up to **100** entries. Chronological. Student/volunteer OK if true | essentials |
| Education | `optional (docs)` | Standardized degree list or Other | essentials |
| Experience level | `needs_check` (settings field; not in 100% table) | Live values: **Entry Level, Intermediate, Expert**. Be truthful. Do not pick Expert without public evidence | essentials “How to set your experience level” · Profile settings |
| Categories / service categories | `needs_check` | Help: **up to four categories when you first create** the freelancer account. Strongest services only | essentials · https://support.upwork.com/hc/en-us/articles/360024526754-Profile-categories-and-skills |
| Hours per week | `optional (docs)` (help presents it as recommended, not as 100% required) | Side panel **Hours per week**. Do not promise 40h. Prefer a modest live range or skip if optional | https://support.upwork.com/hc/en-us/articles/211063008-How-to-display-your-available-hours-on-Upwork |
| Availability status | n/a (Find Work, not profile editor) | Do not open Find Work to hunt jobs in this pack | edit-profile article |
| Portfolio | `optional (docs)` | Role **up to 100** chars; project description **up to 600**; up to **five** skill tags per item. Images 400×300 min, 1000×750 recommended, 4000×4000 max. **No contact details in files** | https://support.upwork.com/hc/en-us/articles/360016144974-How-to-enhance-your-freelancer-profile |
| Other Experience | `optional (docs)` | Skip. Cap 100 with employment | essentials |
| Certifications | `optional (docs)` | Skip unless real | enhance article |
| Linked accounts | `optional (docs)` | Skip | 100% table |
| Profile video | `optional (docs)` | Skip | 100% table |
| Profile visibility | settings | If “submit” or Public forces ID, STOP. Saving in-progress is OK | https://support.upwork.com/hc/en-us/articles/211060298-Set-your-profile-visibility |

### Photo constraints (help)

https://support.upwork.com/hc/en-us/articles/360053305673-How-to-choose-a-good-profile-picture  
https://www.upwork.com/resources/upwork-for-beginners (pixel/format bullets; `needs_check` if the live uploader still prints 250×250–4000×4000 JPEG/PNG)

Must: close-up head and shoulders, face visible, professional (passport-like is OK).  
Must not (photo article): distant shot, effects, sunglasses/coverings (except religious/medical), side view, text/watermark, closed/averted eyes, unprofessional attire, GIF, barcode/QR, logo (freelancer).  
Beginner resource also: real photo of you, **not AI-generated**.

---

## D. Account settings (name, location) — not the public profile bio

| Help label | `required_guess` | DRAFT_ONLY paste hint | Cite |
|---|---|---|---|
| First name / last name (account information) | `required (docs)` as account identity | `{{FULL_LEGAL_NAME}}` split as asked. Real name, nickname, or shortened everyday name. Last name displays as **initial** on the public profile. Single legal name: enter it as both first and last. Do not use job titles (“SEO Expert”) as the profile name | https://support.upwork.com/hc/en-us/articles/115003658388-Change-your-profile-name |
| Verified name (ID) vs profile name | STOP to change via ID | Profile name need not equal passport; **contracts/invoices use verified name**. Do not start ID to “fix” display | same |
| Location: time zone, country, address, phone | `needs_check` which of these block profile save | Honest `{{COUNTRY}}` `{{CITY}}` `{{TIMEZONE}}`. Address/phone: skip if optional. Changing country later forces tax + maybe ID again | https://support.upwork.com/hc/en-us/articles/34397755511955-Identity-verification-Frequently-asked-questions |
| Contact info | Account settings | Do **not** put contact info on the public profile | essentials “What shouldn't I include” |

Account information hub: https://support.upwork.com/hc/en-us/articles/211067528

---

## E. Explicit do-not (profile pack)

- Open a job and paste the overview as a proposal (Connects)
- Catalog **Submit** (sibling catalog file is draft)
- Buy Freelancer Plus / identity badge (35 Connects)
- Linked accounts that request Gmail/Drive/Contacts dump
- Invent employment, education, hours, or USD rates
- Off-platform contact in title, overview, or portfolio

---

## F. Source list (Upwork)

- Sign up: https://support.upwork.com/hc/en-us/articles/24492534968211-How-to-sign-up-as-a-freelancer-on-Upwork
- Beginner: https://www.upwork.com/resources/upwork-for-beginners
- 100% complete: https://support.upwork.com/hc/en-us/articles/211063188-How-do-I-create-a-100-complete-freelancer-profile
- Essentials: https://support.upwork.com/hc/en-us/articles/360016252373-How-to-build-your-freelancer-profile-the-essentials
- Title and overview: https://support.upwork.com/hc/en-us/articles/34925678839827-Your-profile-title-and-overview
- Edit profile: https://support.upwork.com/hc/en-us/articles/360000403687-Edit-freelancer-profile
- Skills: https://support.upwork.com/hc/en-us/articles/211060318-How-do-I-add-skills-to-my-profile
- Categories: https://support.upwork.com/hc/en-us/articles/360024526754-Profile-categories-and-skills
- Enhance / portfolio / languages: https://support.upwork.com/hc/en-us/articles/360016144974-How-to-enhance-your-freelancer-profile
- Profile photo: https://support.upwork.com/hc/en-us/articles/360053305673-How-to-choose-a-good-profile-picture
- Name: https://support.upwork.com/hc/en-us/articles/115003658388-Change-your-profile-name
- Hourly rate: essentials + https://support.upwork.com/hc/en-us/articles/34926076728467-Determine-your-rate
- Hours per week: https://support.upwork.com/hc/en-us/articles/211063008-How-to-display-your-available-hours-on-Upwork
- Visibility: https://support.upwork.com/hc/en-us/articles/211060298-Set-your-profile-visibility
- Account information: https://support.upwork.com/hc/en-us/articles/211067528
- Identity: https://support.upwork.com/hc/en-us/articles/360001176427-How-to-verify-your-identity-as-a-freelancer
- Identity FAQ: https://support.upwork.com/hc/en-us/articles/34397755511955-Identity-verification-Frequently-asked-questions
- Government ID: https://support.upwork.com/hc/en-us/articles/360000563227-How-to-verify-your-identity-with-a-government-ID
