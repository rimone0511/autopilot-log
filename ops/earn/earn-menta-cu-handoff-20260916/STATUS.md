# STATUS — MENTA (B11) CU handoff

Snapshot: **2026-09-16** (folder stamp)  
Folder: `ops/earn/earn-menta-cu-handoff-20260916/`  
State: **DRAFT_ONLY**

This file is the desk box for **B11 / QUEUE B6 / CU-16 MENTA（メンター）**. It is not a signup log and **does not claim an account exists**.

Authoring session: public Intercom Help (200) + `menta.work` GET (this run: **AWS WAF 202 challenge**). **No login. No 登録. No OAuth complete. No credentials invented or stored.**

---

## Desk hint

| Field | Value |
|---|---|
| Desk | MENTA mentor listing（menta.work） |
| IDs | **B11** (this-folder / gate-batch2 local) · QUEUE **B6** · **CU-16** |
| Not | QUEUE **B11** = Workana. Local **B06** = Skill Shift. **ストアカ** = B12 / QUEUE B7 / CU-17 |
| Shape | Mentor **plan** listing. **Not** gig escrow |
| CU hint | `pending` — pack ready; live CU has **not** run this folder |
| Activity gate | Sibling [#61](https://github.com/rimone0511/autopilot-log/pull/61) catalog **pass** (NEW cards). Sibling [#12](https://github.com/rimone0511/autopilot-log/pull/12) **needs_check** (WAF unread). This GET: origin challenge → **do not flip the gate** |
| Google | MAIN only (`Googleアカウントで登録する` on sibling `/register/choose`; **confirm at click-time** after WAF) |
| Plan | **Unpublished draft only.** 金額 empty. **提出 = STOP** |
| Stop | **提出 / 公開 / 有料 / Stripe / 口座** — [STOP.md](STOP.md) |
| Runner | [PLAYBOOK.md](PLAYBOOK.md) · [FIELD-MAP.md](FIELD-MAP.md) |
| Morning context | Sibling [PR#72](https://github.com/rimone0511/autopilot-log/pull/72) **REGISTER-CU-CUT** (jobs-first; that serial skips MENTA). This folder is still the MENTA runner **when** this desk is opened |

Sibling paste (bodies not merged here except fences already in FIELD-MAP):

| Pack | PR |
|---|---|
| Thick mentor + fees | [#33](https://github.com/rimone0511/autopilot-log/pull/33) |
| Alive sample | [#21](https://github.com/rimone0511/autopilot-log/pull/21) |
| Thin Week2 | [#3](https://github.com/rimone0511/autopilot-log/pull/3) |
| Gate first | [#12](https://github.com/rimone0511/autopilot-log/pull/12) |
| Gate batch2 B11 | [#61](https://github.com/rimone0511/autopilot-log/pull/61) |
| QUEUE B6 | [#1](https://github.com/rimone0511/autopilot-log/pull/1) |
| CU INDEX CU-16 | [#8](https://github.com/rimone0511/autopilot-log/pull/8) |

---

## Public livecheck (authoring, 2026-09-16, no login, no POST)

| URL | HTTP | Result used |
|---|---|---|
| https://menta.work/ | **202** | `server: awselb/2.0`. Header **`x-amzn-waf-action: challenge`**. ~2KB JS challenge. Home copy **unread this GET** |
| https://menta.work/index.php/register/choose | **202** | Same challenge. **No** Google-button HTML this GET. Sibling [#61](https://github.com/rimone0511/autopilot-log/pull/61): 200 + 「Googleアカウントで登録する」 |
| https://menta.work/index.php/oauth/google | **202** | Not followed into Google (would not have been followed even on 302) |
| https://menta.work/about_mentor | **202** | Sibling [#61](https://github.com/rimone0511/autopilot-log/pull/61): 200 + fee copy 20%+消費税 / 出金都度300円 |
| https://menta.work/tokutei | **202** | Sibling [#61](https://github.com/rimone0511/autopilot-log/pull/61): 200. メンター手数料 **20％税別**（15％+5％）+ 振込 **300円**. **Not re-read this GET** |
| https://menta.work/plan · `/index.php/plan` | **202** | Sibling [#61](https://github.com/rimone0511/autopilot-log/pull/61): 200 + named cards + **NEW**. Do not record catalog counts as GMV |
| https://menta.work/index.php/plan?order=2 | **202** | Sibling [#61](https://github.com/rimone0511/autopilot-log/pull/61): **202 WAF**. Do not use 新着 sort as proof |
| https://intercom.help/mentajp/ja/articles/3025296 | 200 | MENTA = メンタープラットフォーム。月額制でプラン作成。Marketing 人数 / 平均1.4万円 **ignored as paste** |
| https://intercom.help/mentajp/ja/articles/3025349 | 200 | メニュー → メンター → メンタープラン編集. Steps 1–7. **Step 7 提出 = STOP** |
| https://intercom.help/mentajp/ja/articles/5252569 | 200 | 提出 = 運営確認後 **公開**. 新規必須. **提出費用なし** ≠ GO |
| https://intercom.help/mentajp/ja/articles/3751409 | 200 | 相談できます / 今、忙しいです / **表示しない** |
| https://intercom.help/mentajp/ja/articles/3025582 | 200 | 手数料 **22％**（20％+消費税10％）+ 出金都度 **300円** (2022-08-31) |
| https://intercom.help/mentajp/ja/articles/3025561 | 200 | 支払いには本人確認. **Stripe**. STOP |
| https://intercom.help/mentajp/ja/articles/3025575 | 200 | 出金: 1,000円超 + 30日 + **本人確認・口座**. STOP |
| https://intercom.help/mentajp/ja/articles/3025564 | 200 | Live plans = **出品中** |
| https://intercom.help/mentajp/ja/articles/6591930 | 200 | スクールプラン tips. **Not** a publish GO. Do not invent 指導件数 |

Challenge keys, cookies, CSRF, and OAuth `state` are **not** recorded here.

`thin_site_skip: false` (WAF challenge ≠ parking domain; sibling origin 200 the same day).

---

## ID crosswalk (do not mix)

| ID | Means | This desk? |
|---|---|---|
| **B11** (this folder / PR#61 records) | MENTA | **yes** |
| QUEUE **B6** (PR#1) | MENTA | **yes** |
| **CU-16** (PR#8 / PR#3) | MENTA | **yes** |
| QUEUE **B11** (PR#1) | **Workana** | no |
| Local **B06** (PR#72 / PR#95) | **Skill Shift** (QUEUE B16 / CU-27) | no |
| B12 / QUEUE B7 / CU-17 | **ストアカ** | no |

---

## Live CU outcome (empty until a human/CU runs the playbook)

Do not pre-fill success. Valid later values match PLAYBOOK:

```
desk: MENTA
pack: ops/earn/earn-menta-cu-handoff-20260916/
ids: B11 / QUEUE-B6 / CU-16
auth:
otp:
kyc:
draft_profile:
draft_plan:
submit: no
publish: no
status_control:
paid_plan: no
bank: no
waf:
next: stop
```

Current: **not run**.

---

## This PR does not

- Create or log into a MENTA account
- Invent or commit Google / email / password / OTP / phone / bank / Stripe / WAF tokens
- Press **提出** or set **相談できます**
- Type a プラン 金額 or copy a gig SKU
- Open Stripe 本人確認 / 口座 / 出金
- Buy anything or invent 手数料％
- Mix MENTA with Workana, Skill Shift, or ストアカ
- Merge sibling pack folders
- Change Python posting-gate tests
