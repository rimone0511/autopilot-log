> DRAFT_ONLY field map. NO login in the authoring session. NO secrets. NO invented credentials.
> Paste values: [PLAYBOOK.md](PLAYBOOK.md). KYC: [STOP-KYC.md](STOP-KYC.md).
> Labels come from **Contra Help Center** + public signup HTML (2026-09-16). Live wizard wins.

# FIELD-MAP — Contra Independent / Share work

Desk: Contra Independent (CU-08)  
Livecheck: 2026-09-16, public help + https://contra.com/sign-up (no account created)

`required_guess` is **not** a logged-in required-field dump. Values:

| Token | Meaning |
|---|---|
| `required (docs)` | Help or public signup names the control as part of creating / completing the Independent path |
| `high` | Help lists it on the profile-complete checklist; draft save may still work without it |
| `optional (docs)` | Help documents a skip / draft / unpublished path |
| `needs_check` | Help is silent or the live widget was not opened logged-in |
| `STOP` | Do not fill. Not a paste target |

Placeholders stay empty in git. Fill only from the operator’s local ledger at paste time.

---

## A. Sign up (public page + onboarding help)

Public signup (https://contra.com/sign-up, retrieved 2026-09-16): heading **Sign up to Contra**; primary button **Continue with Google**; secondary **Or sign up with** / **Continue**; **Already using Contra? Sign in**.

| UI label (help / public HTML) | `required_guess` | DRAFT_ONLY paste | Cite / gap |
|---|---|---|---|
| Continue with Google | preferred path | MAIN `{{GOOGLE_ACCOUNT_EMAIL}}` only. Same Google every later login | Public `/sign-up` |
| Email “Or sign up with” / Continue | fallback | Same MAIN email. No new mailbox. Password not in git | Public `/sign-up`. Exact email-field labels **`needs_check`** (SPA) |
| Already using Contra? Sign in | control | If MAIN already has Contra → Sign in. No second account | Public `/sign-up` |
| What brings you to Contra? | `required (docs)` | **Share work** (Independent). Not **Hire creative talent** | [Onboarding](https://help.contra.com/en/articles/9322381-onboarding-and-completing-your-profile) |
| Profile photo (onboarding Step 2) | `high` | `{{PHOTO_LOCAL_PATH}}` local face photo. Skip if wizard allows | Onboarding. Not an ID |
| One-liner (onboarding Step 3) | `required (docs)` | PLAYBOOK One-liner A or B. Cut to live cap. Character cap **`needs_check`** (help says “brief”, no number) | Onboarding · [One-liner](https://help.contra.com/en/articles/9322675-writing-your-one-liner-on-contra) |
| Create account: Pro vs free | `required (docs)` | **Proceed with a free account** | Onboarding Step 4 |
| Topics (onboarding Step 5) | `high` | Existing chips nearest automation / APIs / documentation. Do not invent tags | Onboarding |

Google / email / password values are **never** committed. Do not write a sample password.

---

## B. Profile after account (help labels)

Onboarding says account exists after topics; Discoverable complete requires more, **including wallet**. This map fills only the non-KYC rows.

### B1. Identity on the public profile (not wallet)

| Help label | `required_guess` | DRAFT_ONLY paste | Cite |
|---|---|---|---|
| First Name / Last Name (display) | `required (docs)` as display identity | `{{DISPLAY_NAME}}` split as the form asks. Everyday name from ledger. Not a job title | [Change name / email / profile](https://help.contra.com/en/articles/16275340-how-to-change-your-name-email-and-profile-information-on-contra) |
| Email (Settings → Account) | account field | MAIN only. Do not “fix” it to a different inbox this pass. Verification OTP = parent Gmail | Same article · [Update email](https://help.contra.com/en/articles/9322385-updating-your-email-address-a-step-by-step-guide) |
| About / Description / bio | `high` | PLAYBOOK 200 or **400**. Official **400-character limit** | [Bios](https://help.contra.com/en/articles/9322626-bios-on-contra) · change-profile article |
| One-liner (profile, under name) | `high` | Same paste as signup if the profile still shows “Add a professional one-liner” | One-liner help |
| Location (city / region) | `high` | `{{COUNTRY}}` / `{{PREFECTURE}}` or city from ledger. **No street**. Do not start a **country-change** support email (that path asks for proof of residence / ID) | [Location](https://help.contra.com/en/articles/13465157-how-to-change-your-location-on-contra) |
| Public profile URL / Share Profile | n/a this pass | May copy later. Do not paste it into git with a session token | Change-profile article |
| Switch Workspace (Freelancer ↔ Client) | skip | Stay on Independent / Share work. Do not switch to Client to “test hire” | [Switching account types](https://help.contra.com/en/articles/9322386-switching-account-types-on-contra) |

### B2. Official “complete your profile” checklist (minus wallet)

| Help label | `required_guess` | DRAFT_ONLY paste | Cite |
|---|---|---|---|
| Profile cover image or video | `high` (complete-profile Step 1) | Public, no-secret image, or skip | Onboarding complete-profile |
| 4 pieces of work | `high` (complete-profile Step 2) | Public URLs. Case study **Save as draft**. Import **public** links only. **Do not Publish / Post to feed** | Onboarding · [Case study](https://help.contra.com/en/articles/9322393-how-to-build-a-case-study-from-scratch-on-contra) · [Import](https://help.contra.com/en/articles/9322427-how-to-import-existing-work-on-contra) |
| Rate / hourly | `high` (complete-profile Step 3) | `{{HOURLY_USD}}` or empty. If save blocks and ledger empty → `rate_empty`. Do not invent | Onboarding |
| Social link | `high` (complete-profile Step 4) | `{{PORTFOLIO_URL}}`, `{{GITHUB_URL}}`. LinkedIn only if URL already exists | Onboarding · [Social links](https://help.contra.com/en/articles/11758863-how-to-update-social-links-on-your-profile) |
| Verify identity & set up your wallet | **STOP** | Do not open. See [STOP-KYC.md](STOP-KYC.md) | Onboarding complete-profile Step 5 |
| Discoverable / public toggle | `needs_check` (wording) | **Off** if a toggle exists. Do not treat “profile complete” as a goal this pass | Onboarding closing copy says complete (incl. identity) → discoverable |

---

## C. Work / case study editor (draft only)

Help: Work → Create → Case Study. Dropdown next to **Publish** → **save as draft**. Import: “add existing project link” + public URL.

| Help label | `required_guess` | DRAFT_ONLY paste | Cite |
|---|---|---|---|
| Visuals / cover | optional for draft | Public only. Rec. **1600 × 1200**; max **200MB** (help). No ID | Case study help |
| Description | optional for draft | Process, not credentials. No client secrets | Case study help |
| Title | `needs_check` for draft save | PLAYBOOK sample titles | Case study Step 7 |
| Preview description | `needs_check` | One line, no contact | Case study Step 7 |
| Project link | optional | `{{PORTFOLIO_URL}}` or `{{GITHUB_REPO_AUTOPILOT}}` | Case study Step 8 · Import help |
| Collaborators / client company | skip unless true | Do not invent a client on Contra | Case study Step 8 |
| Tools / skills / industry tags | optional | Live picker only. Prefer n8n, APIs, documentation if listed | Case study Step 9 |
| Verify case study (Contra-completed work) | skip | No Contra-paid project this pass | Case study Step 6 |
| Publish / Post to feed | **do not** | Draft only | Case study Steps 10–11 |

If “4 pieces of work” cannot be saved except by **Publish to feed**, park with public URLs in About/social and stop. Do not publish to complete a checklist.

---

## D. Services (optional, unpublished)

Not required to create the account. If the CU opens Services:

| Help label | `required_guess` | DRAFT_ONLY paste | Cite |
|---|---|---|---|
| Service name & cover | n/a unless opened | Skip this pass, **or** title from ledger + public cover. Example shape in help: “60-Minute Product Strategy Call” — do not copy that title if it is untrue | [Services](https://help.contra.com/en/articles/9322412-how-to-add-services-to-your-contra-profile) |
| Tags: Role 1–3, Tools 1–5, Industry 0–3 | n/a | Picker only | Services help |
| Description / FAQ / calendar | n/a | No calendar-for-calls if that is a live booking link you cannot honor. No off-platform pay | Services help |
| Payment details | n/a | Prefer **Contact for pricing** if a number would be invented. Do not type a fake `$100/hour` | Services help (“Contact for pricing” is official) |
| Publish vs Save as unpublished | **unpublished** | Help: “Save as unpublished.” Do **not** Publish | Services Step 5 |

---

## E. STOP rows (not paste targets)

Do not map “how to fill” these. Appearance = close the dialog.

| Screen / control | Action |
|---|---|
| Wallet / independent wallet | Close |
| Add account / Add an account | Close |
| Persona (or any ID vendor) | Close |
| Government ID / selfie / liveness | Close |
| Bank / PayPal / USDC / Payoneer / Airwallex | Close |
| Tax / W-8 / SSN / My Number | Close |
| Expert verification that asks for ID | Close |
| Get Pro / Max / add card | Close (`card_wall`) |
| Apply / invoice / proposal/new paid project | Close |
| Country-change support email with proof of residence | Do not send |

---

## F. Placeholder ledger (empty in git)

| Placeholder | Allowed fill at paste time | Never |
|---|---|---|
| `{{GOOGLE_ACCOUNT_EMAIL}}` | MAIN Google | A newly invented Gmail |
| `{{DISPLAY_NAME}}` | Everyday name from ledger | Fake brand alias as legal identity |
| `{{PHOTO_LOCAL_PATH}}` | Local path on the CU machine | A file committed here |
| `{{PORTFOLIO_URL}}` | Already-public site | Staging with auth |
| `{{GITHUB_URL}}` / `{{GITHUB_REPO_AUTOPILOT}}` | Already-public repo | Private repo |
| `{{HOURLY_USD}}` | Local ledger or empty | Guessed “market rate” |
| `{{COUNTRY}}` / `{{PREFECTURE}}` / `{{TIMEZONE}}` | Ledger (no street) | Full address, building, room |
| `{{PHONE}}` | Do not use unless live form blocks **draft** save and the **user** placed a number in chat | Invented SMS identity |

---

## G. Source list

- https://contra.com/sign-up
- https://contra.com/how-it-works/independents
- https://contra.com/pricing
- https://help.contra.com/en/articles/9322381-onboarding-and-completing-your-profile
- https://help.contra.com/en/articles/9322675-writing-your-one-liner-on-contra
- https://help.contra.com/en/articles/9322626-bios-on-contra
- https://help.contra.com/en/articles/16275340-how-to-change-your-name-email-and-profile-information-on-contra
- https://help.contra.com/en/articles/9322385-updating-your-email-address-a-step-by-step-guide
- https://help.contra.com/en/articles/11758863-how-to-update-social-links-on-your-profile
- https://help.contra.com/en/articles/13465157-how-to-change-your-location-on-contra
- https://help.contra.com/en/articles/9322393-how-to-build-a-case-study-from-scratch-on-contra
- https://help.contra.com/en/articles/9322427-how-to-import-existing-work-on-contra
- https://help.contra.com/en/articles/9322412-how-to-add-services-to-your-contra-profile
- https://help.contra.com/en/articles/9322386-switching-account-types-on-contra
