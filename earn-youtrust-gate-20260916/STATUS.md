# STATUS — B18 YOUTRUST (activity gate)

> ## SKIP LIVE CU / NOT THIN / NOT A LIVE GO
>
> **2026-09-16 06:07 JST.** Public GET only.
> Activity gate stays **`needs_check`** (logged-out jobs API **401**; card dates unread).
> Product shape: **warm intro / scout** (「話を聞きたい」→カジュアル面談; recruiter スカウト).
> **This pass: `skip_live_cu`.** Do **not** `skip_log`. If a later human GO: **`profile_only`**.
> **DRAFT_ONLY.** No signup.

Snapshot: **2026-09-16 06:07 JST** (GET ~21:07 UTC 2026-09-15)  
Folder: `earn-youtrust-gate-20260916/`  
State: **DRAFT_ONLY** / **`needs_check`** + **`skip_live_cu`**  
Authoring: logged-out public GET only. **No signup. No OAuth. No POST. No cookie values saved.**

Forbidden: secrets, live phones/passwords/OTP/CSRF values, KYC files, signup from this authoring agent, 「話を聞きたい」, ジョブ投稿, 公式リクルーター購入, invented traffic/GMV/fee %.

Python posting-gate tests were **not** edited.

---

## Verdict

| Item | Status |
|---|---|
| This note | **ready · draft** (markdown only) |
| Activity gate this GET | **`needs_check`** (API 401; cards unread). Matches [PR#12](https://github.com/rimone0511/autopilot-log/pull/12) / [PR#59](https://github.com/rimone0511/autopilot-log/pull/59) |
| Product shape | **warm_intro_scout** |
| Live CU register / profile draft | **not_run** · **`skip_live_cu` this pass** |
| Skip desk as thin/dead | **no** (`SKIP thin: no`) |
| Later CU cap | **`profile_only`** (human GO only) |
| 「話を聞きたい」 / job post / recruiter buy | **no** |
| Account claimed | **no** |

## CU hint (this desk)

| Hint | Meaning here |
|---|---|
| `needs_check` | Job recency unread. Do not guess `pass` |
| `skip_live_cu` | Do not open CU this pass. REGISTER-CU-CUT / jobs-first |
| `profile_only` | Later GO: profile **draft** only. Not interview-agent |
| `pack_ready` | NOTE + STOP exist on sibling [PR#30](https://github.com/rimone0511/autopilot-log/pull/30). **Not** a play GO |
| `pending` | Live CU has **not** marked a draft from **this** folder |
| `register_cu_cut` | Wave B register serial cut. Prefer JOBS |

Current row (authoring time):

| ID | Desk | QUEUE | CU | Google | Gate | CU hint | Next |
|---|---|---|---|---|---|---|---|
| B18 | YOUTRUST | **B13** | CU-24 | help PREFER_GOOGLE; `/sign_in` button **needs_check** (SPA) | **`needs_check`** | `skip_live_cu` + later `profile_only` | Do **not** CU-play from this folder. Human may view one job card date. If later GO: `/sign_in` → profile **draft** → **STOP before 「話を聞きたい」** |

Do **not** confuse:

| Label | Desk |
|---|---|
| this folder **B18** | YOUTRUST |
| QUEUE **B13** | YOUTRUST (canonical WAVE letter) |
| PR#59 local **B18** | same desk (this folder continues that label) |
| QUEUE **B14** / this-ecosystem B19 | Offers — different desk |
| PR#59 local **B14** | PeoplePerHour — different desk |

## Pack files

| File | Role |
|---|---|
| [NOTE.md](NOTE.md) | Shape + 401 + profile-only vs skip |
| [METHOD.md](METHOD.md) | HTTP log |
| [STOP.md](STOP.md) | Warm-intro / scout / KYC stops |
| [STATUS.md](STATUS.md) | This box |

## This GET (logged out) — short

| URL | HTTP | Note |
|---|---|---|
| https://youtrust.jp/ | 302→200 `/lp` | 仕事専用SNS |
| https://youtrust.jp/sign_in | 200 | SPA. Google button unread in HTML |
| https://youtrust.jp/signup | 404 | Unused |
| https://youtrust.jp/recruitment_posts | 200 | SPA. Meta: 「話を聞きたい」→カジュアル面談. Dates unread |
| https://youtrust.jp/api/recruitment_posts | **401** | `You need to sign in or sign up before continuing.` |
| https://help.youtrust.jp/user/message/want-to-talk/ | 200 | Logged-out button → 新規登録 then notify |
| https://help.youtrust.jp/user/post/cost/ | 200 | ジョブ1つまで無料（poster）. Applicant % unread |

`alive` catalog / `dead` / `thin` / `pass`: **0 this folder** (single desk; `needs_check`).

---

## After live CU (leave blank until a run)

Fill only secret-free keys. Do not paste OTP, ID, a phone, CSRF, or Set-Cookie.

```
desk: YOUTRUST
pack: earn-youtrust-gate-20260916/
auth:
otp:
kyc:
want_to_talk_sent: no
job_posted: no
draft_profile:
publish: no
next:
```

Outcome so far: **not_run**.

---

## Next (human)

1. **Do not CU-play this desk from this PR.** Keep draft. Wave B register serial is cut; prefer JOBS on `draft_saved` desks.
2. Optional: view **one** job card date on `/recruitment_posts` (browser). If a date is recent, a later note may move `needs_check` → `pass`. Still **not** a CU GO by itself.
3. If a human later GOs **this** desk: [NOTE.md](NOTE.md) then [STOP.md](STOP.md). Profile draft only. **No 「話を聞きたい」.**
4. Do not merge until Yuta reviews.
5. Do not rewrite QUEUE B13 or INDEX CU-24.

## This PR / pack will not

- Copy sibling paste bios
- Create a marketplace account
- Send 「話を聞きたい」 / つながり申請 / ジョブ投稿
- Buy 公式リクルーター / extra job slots / scout 通数
- Upload ID / selfie / bank / My Number
- Invent fee % or listing counts
- Change Python posting-gate tests
- Start Wave B register CU after Freelancer (cut; prefer JOBS)
