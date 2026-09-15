# METHOD — public GET only (no marketplace login)

Datetime: 2026-09-15  
UA: ordinary desktop browser string. **No login cookies. No OAuth. No account create.**

Did: GET official public URLs. Record HTTP status, visible headings, and help/FAQ text that arrived in HTML.  
Did not: marketplace login, Google OAuth completion, paid checkout, KYC, proposals, applications, inventing job counts or GMV.

Vendor marketing totals (Guru “1 Million Paid Invoices”, Malt “1M+ freelancers”, Freelancermap homepage “110,500+ experts”, PPH “Trusted globally by over 1 mil…”) are **not** activity proof.

WAF is a fact of this environment, not a proof the product is dead.

| URL | HTTP | Memo |
|---|---|---|
| https://www.guru.com/ | 403 | Incapsula challenge. No jobs HTML this GET. |
| https://www.guru.com/d/jobs/ | 403 | Same. Recency **not re-read**. Sibling PR#2 (2026-09-15) recorded 2026-dated job cards including “Posted 1 hr ago”. This run: `needs_check` to re-open in a human browser. |
| https://www.guru.com/help/freelancer/create-an-account-freelancer/ | 403 | Incapsula |
| https://www.guru.com/help/freelancer/membership/ | 403 | Incapsula |
| https://www.guru.com/help/freelancer/submitting-your-documents-freelancer/ | 403 | Incapsula. KYC+fee text stays on sibling/help citation, not re-fetched. |
| https://www.peopleperhour.com/ | 200 | Home loads. Register links. Hourlie tiles present. |
| https://www.peopleperhour.com/site/register | 200 | Title “Register with PeoplePerHour.com”. Buttons: **Continue with GOOGLE**, Sign up with Facebook, Sign up with email. Role: I want to (buyer vs freelancer). |
| https://www.peopleperhour.com/freelance-jobs | 200 | Title includes **Sep 2026**. HTML included `posted_dt` values on **2026-09-15** (examples in page: `11:26:06`, `17:45:14`). Do not treat as a traffic total. |
| https://www.peopleperhour.com/static/terms | 200 | **PPH Basic Subscription**: freelancer access under a subscription plan; **non-refundable annual** fee (full or monthly for the Annual Term). **TopAccess** is a second non-refundable annual subscription. |
| https://www.malt.com/ | 403 | Cloudflare “Just a moment…”. Directory not re-read. |
| https://www.malt.com/c/freelancers | 403 | Same |
| https://help.malt.com/hc/en-150/articles/30748346951826-How-do-I-get-started-as-a-freelancer-on-Malt | 403 | Same |
| https://help.malt.com/hc/en-150/articles/29943035945106-How-to-validate-your-legal-documents-on-Malt | 403 | Same |
| https://help.malt.com/hc/en-150/articles/29511599491090-I-am-a-freelancer-registered-abroad-For-which-countries-does-Malt-authorize-registration-in-this-situation | 403 | Same. JP-on-open-list stays sibling citation. |
| https://www.workana.com/ | 403 | Cloudflare |
| https://www.workana.com/en/signup | 403 | Cloudflare |
| https://www.workana.com/en/login | 403 | Cloudflare. Sibling PR#2: Continue with Google / Facebook / Apple in login HTML. |
| https://www.workana.com/en/jobs | 403 | Job recency **unread** (same class of block as sibling). |
| https://www.freelancermap.com/ | 200 | Title “Freelancer jobs & IT projects worldwide — 0% commission”. Sign up / Log in. Membership types Basic / Premium / Business / Enterprise in page JSON. |
| https://www.freelancermap.com/registration | 200 | “Create your free account”. Account types: **Freelancer / Agency** vs **Project provider**. Fields include Email address, Password, Country, salutation, first/last name, optional birthdate. **No Continue-with-Google control** in this HTML. |
| https://www.freelancermap.com/login | 200 | Email login / email-login. No Google OAuth control in this HTML. |
| https://www.freelancermap.com/pricing/freelancer | 200 | Free Basic vs Premium. Public JSON: lowest Premium **13.99** EUR/month; `PM12/12` annual. Profile verification text: **€50/year** Premium, **€75/year** Basic (Persona). Do not buy. |
| https://www.freelancermap.com/help.html | 200 | FAQ: Basic free; apply up to **10** projects/month; respond up to **3** contact requests from paying clients; Premium from €13.99/month billed annually; signup = email activation link. |
| https://www.freelancermap.com/data-privacy.html | 200 | §18 SILT and §19 Persona: identity documents + selfie biometrics for optional profile verification. |
| https://www.freelancermap.com/projects | 200 | Title “Freelance Jobs & IT Projects Worldwide”. Listing HTML included `2026-09-15T19:36` and other **2026-09-15** ISO timestamps. Heading text also showed a job/project count; **that number is not copied as a traffic metric**. |
| https://www.freelancermap.com/projects.html | 404 | Wrong path. Use `/projects`. |
| https://www.freelancermap.com/for-freelancer | 200 | Freelancer pitch. Free profile. Premium marketing — ignore as activity proof. |
| https://www.freelancermap.com/blog/freelance-profile-tips-examples/ | 200 | 2026 profile-visibility article (public / private / anonymous). Not a login. |

## Gate labels used in this folder

| Label | Meaning |
|---|---|
| `pass` | Public page showed a living surface (recent timestamps or a working free draft path). Still **DRAFT_ONLY**. |
| `needs_check` | This environment could not read the page (WAF) or a control (Google button) is unconfirmed. Do not promote to pass by guessing. |
| `blocked_paid_plan` | Marketplace may be alive; seller submit appears paid. **Do not subscribe.** |

No desk is marked dead from a WAF page.
