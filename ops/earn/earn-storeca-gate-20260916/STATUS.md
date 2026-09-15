# STATUS — B12 ストアカ (gate + thin CU)

> ## NO-GO / DEFER — NOT A LIVE GO
>
> **2026-09-16.** This folder is an **activity-gate + thin CU note** for one desk.
> Gate this GET: **`pass`** (course dates **read**).
> Early CU: **NO-GO / defer.** Allowed later action (human GO only): teacher **profile draft**. **No class publish.**
> **Do not** treat this pack as next live CU after Freelancer.com (A10 / CU-10).
> Wave B register serial remains **REGISTER-CU-CUT** ([PR#72](https://github.com/rimone0511/autopilot-log/pull/72)). Prefer JOBS phase (do-not-send).
> Keep **DRAFT_ONLY**.

Snapshot: **2026-09-16 JST**  
Folder: `ops/earn/earn-storeca-gate-20260916/`  
State: **DRAFT_ONLY** / gate **`pass`** / early CU **defer**  
Authoring: logged-out public GET only. **No signup. No OAuth. No POST. No cookies saved.**

Forbidden: secrets, live phones/passwords/OTP/CSRF, KYC files, signup from this authoring agent, 講座公開, paid plans, invented traffic/GMV/fee % from unread help.

Python posting-gate tests were **not** edited.

---

## Verdict

| Item | Status |
|---|---|
| This pack | **ready · draft** (markdown only) |
| Gate this folder | **`pass`** ( `/online/all` session dates readable ) |
| If course dates had been unread | would be **`needs_check`** — not guessed |
| Early CU (register / profile draft) | **NO-GO / defer** · **not_run** |
| Class submitted / 掲載審査 | **no** |
| Account claimed | **no** |
| WAF on top `/` this GET | **no** (200). Sibling GETs: 405 possible |
| Help | www `/help` **404**; Zendesk **403**; www `/faq` **403** |

## CU hint (this desk)

| Hint | Meaning here |
|---|---|
| `pack_ready` | GATE + CU-NOTE + STOP exist. **Not** a play GO |
| `pending` | Live CU has **not** marked a draft from **this** folder |
| `draft_saved` | Fill only after a real CU run that parked an unpublished teacher profile |
| `listing_stop` | 講座作成 / 掲載審査 UI. Do not submit |
| `kyc_wait` | 本人確認書類 / 顔撮影. Morning user. No upload |
| `waf_park` | www 405 or Cloudflare 403 unsolved. Park. Not dead |
| `register_cu_cut` | Wave B register serial cut. **Not** next live CU. Prefer JOBS |

Current row (authoring time):

| ID | Desk | QUEUE | CU | Google | Gate | Early CU | CU hint | Next |
|---|---|---|---|---|---|---|---|---|
| B12 | ストアカ | **B7** | CU-17 | NOT_OFFERED_OAUTH (mailbox) | **`pass`** | **NO-GO / defer** | `pack_ready` + `pending` | Do **not** CU-play from this folder. If a human later GOs: `/register` email → teacher profile **draft** → **STOP before 本人確認 / 掲載審査** |

Do **not** confuse:

| Label | Desk |
|---|---|
| this folder **B12** | ストアカ |
| QUEUE **B7** | ストアカ |
| QUEUE **B12** | Freelancermap |
| leftover-folder **B17** | Freelancermap ([PR#69](https://github.com/rimone0511/autopilot-log/pull/69)) |
| this-folder **B07** in [PR#97](https://github.com/rimone0511/autopilot-log/pull/97) | ITプロパートナーズ — different desk |

## Pack files

| File | Role |
|---|---|
| [README.md](README.md) | Banner + id crosswalk |
| [GATE.md](GATE.md) | `/teach` · WAF/403 · unread-date rule |
| [CU-NOTE.md](CU-NOTE.md) | Thin CU. **NO-GO / defer** |
| [STOP.md](STOP.md) | KYC / 講座公開 / SNS |
| [METHOD.md](METHOD.md) | HTTP log |
| [STATUS.md](STATUS.md) | This box |

## Complement (bodies not copied)

| PR | Relation |
|---|---|
| [#12](https://github.com/rimone0511/autopilot-log/pull/12) | First JP Wave B: ストアカ **`needs_check`** (dates unread) |
| [#61](https://github.com/rimone0511/autopilot-log/pull/61) | Batch2 re-GET ストアカ **`pass`** |
| [#39](https://github.com/rimone0511/autopilot-log/pull/39) | Gap-fill CU-17 thick paste |
| [#33](https://github.com/rimone0511/autopilot-log/pull/33) | Deep pack while www 405 |
| [#72](https://github.com/rimone0511/autopilot-log/pull/72) | **REGISTER-CU-CUT**; ストアカ not in that alive serial |
| [#94](https://github.com/rimone0511/autopilot-log/pull/94) | Morning-loop: ストアカ not this pass |
| [#97](https://github.com/rimone0511/autopilot-log/pull/97) | Same shape (one-desk early note). Different desk |

---

## This GET (logged out)

UA: ordinary desktop Chrome string (Safari re-GET same statuses). No login cookie. CSRF / `authenticity_token` values were **not** stored.

| URL | HTTP | Note |
|---|---|---|
| https://www.street-academy.com/ | 200 | No WAF body this GET. Session labels include **9月16日** |
| https://www.street-academy.com/teach | 200 | 講師/主催団体登録フォーム. 無料ではじめられる. LINE/FB login. メールアドレスで登録 present. Google OAuth **none**. 本人確認書類 ※1 |
| https://www.street-academy.com/register | 200 | LINE / Facebook / メールアドレスで登録. **POST not sent** |
| https://www.street-academy.com/fee | 200 | 登録・月額 0円. 自己集客 10% / 送客 30%（対面 20%）/ リピート 10% |
| https://www.street-academy.com/online/all | 200 | Cards + **9月16日(水) 10:00 / 21:20**. JSON **2026-09-16** |
| https://www.street-academy.com/myclass/99028 | 200 | Detail readable this GET (sibling 405 possible) |
| https://www.street-academy.com/help | **404** | www. Not Zendesk |
| https://www.street-academy.com/faq | **403** | Cloudflare「Just a moment...」 |
| https://support.street-academy.com/hc/ja | **403** | Cloudflare. Help unread |
| https://teach.street-academy.com/ | 200 | Media. PickUp **2026.06.18**. Not signup |

`alive` catalog / `dead` / `thin`: **0 extra labels** (single desk; `pass`).  
`needs_check` **not** applied to the desk this GET (dates read). Help article remains unread.

---

## After live CU (leave blank until a run)

Fill only secret-free keys. Do not paste OTP, ID, a phone, or `authenticity_token`.

```
desk: ストアカ
pack: ops/earn/earn-storeca-gate-20260916/
auth:
otp:
kyc:
class_submitted: no
draft_profile:
publish: no
waf:
next:
```

Outcome so far: **not_run**. Early CU: **defer**.

---

## Next (human)

1. **Do not CU-play this desk from this PR.** Keep draft. Wave B register serial is cut; prefer JOBS on desks that already have `draft_saved`.
2. If a human later GOs **this** desk: follow [CU-NOTE.md](CU-NOTE.md) then [STOP.md](STOP.md). Profile draft only. **No 掲載審査.**
3. If www is WAF 405 at click-time: human verification or park. Do not relabel `dead`.
4. If `/online/all` dates are unread on a later GET: relabel gate **`needs_check`**. Do not keep `pass` by memory.
5. Do not merge until Yuta reviews.
6. Do not rewrite QUEUE B7 / QUEUE B12 (Freelancermap).

## This PR / pack will not

- Copy sibling paste bios or field-map tables
- Create a marketplace account
- Complete LINE / Facebook / email signup
- Upload ID / selfie / bank
- Publish a class or buy paid plans
- Invent fee % from 403 help, or listing counts
- Change Python posting-gate tests
- Start Wave B register CU after Freelancer (cut; prefer JOBS)
