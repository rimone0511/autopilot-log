# STATUS — B07 ITプロパートナーズ (profile-only early CU)

> ## PROFILE-ONLY / NOT A LIVE GO
>
> **2026-09-16.** This folder is an **early CU note** for one interview-heavy desk.
> Allowed later action: **profile draft only**. **No interview booking.**
> **Do not** treat this pack as next live CU after Freelancer.com (A10 / CU-10).
> Wave B register serial remains **REGISTER-CU-CUT** ([PR#72](https://github.com/rimone0511/autopilot-log/pull/72)). Prefer JOBS phase (do-not-send).
> Keep **DRAFT_ONLY**.

Snapshot: **2026-09-16 JST**  
Folder: `ops/earn/itpropartners-profile-only-20260916/`  
State: **DRAFT_ONLY** / **`profile_only`**  
Authoring: logged-out public GET only. **No signup. No OAuth. No POST. No cookies saved.**

This is a **desk box**, not a live CU log and not an activity-gate re-judge. Sibling [PR#12](https://github.com/rimone0511/autopilot-log/pull/12) already marked the desk `pass` (public cards). This folder adds the **interview-heavy → profile-only** early-CU rule.

Forbidden: secrets, live phones/passwords/OTP/CSRF, KYC files, signup from this authoring agent, 面談予約, 応募, paid plans, invented traffic/GMV/fee %.

Python posting-gate tests were **not** edited.

---

## Verdict

| Item | Status |
|---|---|
| This 3-file note | **ready · draft** (markdown only) |
| Gate this folder | **`profile_only`** (interview-heavy; not skip-agent) |
| Sibling activity-gate | **pass** (PR#12; this GET still shows 最終更新日 **2026/09/15**) |
| Live CU register / profile draft | **not_run** from this agent |
| Interview booked | **no** |
| Apply / 応募 | **no** |
| Account claimed | **no** |

## CU hint (this desk)

| Hint | Meaning here |
|---|---|
| `pack_ready` | NOTE + STOP exist. **Not** a play GO |
| `pending` | Live CU has **not** marked a draft from **this** folder |
| `draft_saved` | Fill only after a real CU run that parked an unpublished profile |
| `interview_stop` | 面談予約 / 電話ヒアリング / 企業面談 UI. Do not book |
| `kyc_wait` | Identity / NDA / 契約書類. Morning user. No upload |
| `blocked_skip` | Skip this pass for the listed reason |
| `register_cu_cut` | Wave B register serial cut. **Not** next live CU. Prefer JOBS |

Current row (authoring time):

| ID | Desk | QUEUE | CU | Google | Gate | CU hint | Next |
|---|---|---|---|---|---|---|---|
| B07 | ITプロパートナーズ | **B17** | CU-28 | NOT_OFFERED_OAUTH (mailbox) | **`profile_only`** | `pack_ready` + `pending` | Do **not** CU-play from this folder. If a human later GOs: `/register` 職種エンジニア → profile **draft** → **STOP before 面談予約** |

Do **not** confuse:

| Label | Desk |
|---|---|
| this folder **B07** | ITプロパートナーズ |
| QUEUE **B7** | ストアカ ([PR#61](https://github.com/rimone0511/autopilot-log/pull/61)) |
| QUEUE **B17** | ITプロパートナーズ (canonical WAVE letter) |
| leftover-folder **B17** | Freelancermap ([PR#69](https://github.com/rimone0511/autopilot-log/pull/69)) |

## Pack files

| File | Role |
|---|---|
| [NOTE.md](NOTE.md) | Profile-only early CU. Pointers; no bios copied |
| [STOP.md](STOP.md) | 面談予約 / 応募 / KYC / NDA |
| [STATUS.md](STATUS.md) | This box. Fill the success line after a live run |

## Complement (bodies not copied)

| PR | Relation |
|---|---|
| [#12](https://github.com/rimone0511/autopilot-log/pull/12) | JP Wave B gate `pass` |
| [#30](https://github.com/rimone0511/autopilot-log/pull/30) | Thick CU-28 paste + STOP-KYC |
| [#34](https://github.com/rimone0511/autopilot-log/pull/34) | Week2-rest paste pointer |
| [#50](https://github.com/rimone0511/autopilot-log/pull/50) | Wave B Google serial — ITプロ **excluded** (`NOT_OFFERED_OAUTH`) |
| [#72](https://github.com/rimone0511/autopilot-log/pull/72) | Alive CU serial prep; **REGISTER-CU-CUT** |
| [#77](https://github.com/rimone0511/autopilot-log/pull/77) | D-late interview-heavy **sample** (different desks). Same `profile_only` label |

---

## This GET (logged out)

UA: ordinary desktop Chrome string. No login cookie. CSRF / `_token` values were **not** stored.

| URL | HTTP | Note |
|---|---|---|
| https://itpropartners.com/ | 200 | Title フリーランス専門エージェント. Flow 無料登録 → エージェント面談（電話 or **面談予約**）→ 企業面談 → 契約. CTA Emailで無料登録 |
| https://itpropartners.com/register | 200 | 「あなたの職種を教えてください」。エンジニア…CXO. POST exists — **not submitted** |
| https://itpropartners.com/login | 200 | Facebook ログイン終了。パスワード設定リンク。Google ボタンなし |
| https://itpropartners.com/signup | 200 | 「お探しのページは見つかりませんでした」。Not the register entry |
| https://itpropartners.com/job | 200 | 最終更新日 **2026/09/15** ほか 09/14…08。例 TypeScript CRE / Python 要件定義。件数未記載 |
| https://itpropartners.com/job/sale-4 | 200 | 最終更新日 **2026/09/08** コーポレートIT；**2026/09/05** M&A アポ獲得 |
| https://itpropartners.com/blog/flow-itpropartners/ | 200 | 登録・利用は無料。②プロ面談 ③企業面談 ④個別契約書 / 秘密保持契約書 |
| https://itpropartners.com/terms | 200 | 見つかりませんでした シェル。規約本文薄い |
| https://www.itpropartners.com/ | **fail** | Could not resolve host. Unused |

Fees: official 「ご登録やサービスのご利用は無料」(flow blog). 仲介マージン％ **needs_check** → 作らない.  
Card 月額 bands are **that job’s listed pay**, not a profile rate and not GMV.

`alive` catalog / `dead` / `thin` / `needs_check`: **0 this folder** (single desk; `profile_only`).

---

## After live CU (leave blank until a run)

Fill only secret-free keys. Do not paste OTP, ID, a phone, or `_token`.

```
desk: ITプロパートナーズ
pack: ops/earn/itpropartners-profile-only-20260916/
auth:
otp:
kyc:
interview_booked: no
draft_profile:
publish: no
apply: no
next:
```

Outcome so far: **not_run**.

---

## Next (human)

1. **Do not CU-play this desk from this PR.** Keep draft. Wave B register serial is cut; prefer JOBS on desks that already have `draft_saved`.
2. If a human later GOs **this** desk: follow [NOTE.md](NOTE.md) then [STOP.md](STOP.md). Profile draft only. **No 面談予約.**
3. Do not merge until Yuta reviews.
4. Do not rewrite QUEUE letters or leftover-folder B17 (Freelancermap).

## This PR / pack will not

- Copy sibling paste bios or field-map tables
- Create a marketplace account
- Book エージェント面談 / 企業面談 / 電話ヒアリング
- Upload ID / selfie / bank / My Number
- Apply / publish / buy paid plans
- Invent fee % or listing counts
- Change Python posting-gate tests
- Start Wave B register CU after Freelancer (cut; prefer JOBS)
