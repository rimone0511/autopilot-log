> **MAIN Google mailbox only.** `/teach` and `/register` have **no** Google signup control (GTM ≠ OAuth). Use `{{EMAIL}}`. Do not create LINE / Facebook for this desk.
> **DRAFT_ONLY.** Teacher profile **draft** only — and **not this pass**.
> **Early CU = NO-GO / defer.** Gate `pass` is not a play GO.
> **STOP.** See [STOP.md](STOP.md). 本人確認 / 講座公開 / 掲載審査: do not.
> **No secrets. No invented fees. No signup from this PR.**

# CU-NOTE — B12 ストアカ (thin)

Short note. Thick paste lives in sibling PRs — **do not copy bios here.** Shared box: [STATUS.md](STATUS.md). Gate: [GATE.md](GATE.md).

| キー | 値 |
|---|---|
| this_folder | **B12** |
| QUEUE | **B7** (not QUEUE B12 Freelancermap) |
| cu_serial | **CU-17** |
| activity_gate **this folder** | **`pass`** (`/online/all` session **9月16日(水)** + JSON **2026-09-16**) |
| Google | **NOT_OFFERED_OAUTH** → MAIN mailbox +「メールアドレスで登録」 |
| self_serve | **yes** (email register HTML present; LINE/FB also present — skip) |
| official | https://www.street-academy.com/ |
| teach | https://www.street-academy.com/teach |
| register | https://www.street-academy.com/register |
| fee | https://www.street-academy.com/fee |
| listing | https://www.street-academy.com/online/all |
| help | https://support.street-academy.com/hc/ja （this GET **403** → unread） |
| CU hint | `pack_ready` + `pending` |
| **early CU** | **NO-GO / defer** |

## GO / NO-GO (early CU vs defer)

| Question | This folder |
|---|---|
| Play CU-17 now (email register → teacher profile draft)? | **NO-GO.** Defer |
| Why | Wave B register serial is **REGISTER-CU-CUT** ([PR#72](https://github.com/rimone0511/autopilot-log/pull/72)). Prefer JOBS on desks that already have `draft_saved`. Morning-loop STATUS ([PR#94](https://github.com/rimone0511/autopilot-log/pull/94)): ストアカ is **not this pass**. This authoring agent **did not sign up** |
| Does gate `pass` override the cut? | **No.** Readable catalog ≠ live GO |
| If a **human** later types GO for **this** desk | Profile draft only. **No class.** Follow [STOP.md](STOP.md) |

Do **not** chain Freelancer.com → ストアカ from this folder.

## `/teach` path (later human GO only)

Default: **do not play.**

If a human GO names this desk:

1. Open https://www.street-academy.com/teach — confirm title「ストアカ講師/主催団体登録フォーム」. If AWS WAF / Human Verification: human solves it, or **park**. Not dead.
2. Prefer https://www.street-academy.com/register → **メールアドレスで登録**. メール = `{{EMAIL}}` (MAIN mailbox). Password **local ledger only**.
3. LINE / Facebook = skip unless the email path is dead. Do not create a desk-only SNS account.
4. Teacher profile (name / face photo / public URL / bio) from sibling thick pack. **Draft.** **Do not create or submit a class. 掲載審査 = STOP.**
5. 「本人確認書類の提出」screen → close. Morning user.
6. Park. Do not invent a next Wave B register desk from here.

Timebox if a human GO happens: 15–25 min. Stuck > 10 min on WAF / OTP → park.

Placeholders only (no values): `{{EMAIL}}` `{{LEGAL_NAME_KANJI}}` `{{DISPLAY_NAME}}` `{{PHOTO_LOCAL_PATH}}` `{{PORTFOLIO_URL}}`.

## Fees — `/fee` only (help unread)

出典 this GET: https://www.street-academy.com/fee HTTP **200**. Re-read at click time. Do **not** cite Zendesk (403 here).

| 経路（公式 `/fee` の項目名） | 公式ページの率 | Status |
|---|---|---|
| 登録費・掲載費・月額費 | 0 円（「利用料はずっと0円」） | **cited this GET** |
| 自己集客手数料（生徒が初めて） | 10% | **cited this GET** |
| ストアカ送客手数料（初めて） | 30%（対面講座は 20%） | **cited this GET** |
| リピート手数料（2 回目以降） | 10% | **cited this GET** |

同ページ: 各手数料には別途消費税。未開催・キャンセル時は手数料は発生しない.  
自己集客・送客の判定基準リンク先: **not followed this GET** → that logic stays `needs_check`.  
Help https://support.street-academy.com/hc/ja/articles/200700579 : **403**. Do not invent a second table from help.

Do not write fee % into a profile. Do not buy paid support.

## Pointers (do not copy paste bodies)

| Sibling | What it is | Use |
|---|---|---|
| [PR#12 `records/07-street-academy.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-activity-gate-waveb-jp-fced/earn-activity-gate-waveB-20260916/records/07-street-academy.md) | First JP Wave B gate **`needs_check`** (dates unread / WAF) | Contrast. Unread → `needs_check` |
| [PR#61 `records/b12-street-academy.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/waveb-activity-gate-batch2-d9c7/ops/earn/waveb-activity-gate-batch2-20260916/records/b12-street-academy.md) | Batch2 re-GET `pass` | Sibling catalog. Body not copied |
| [PR#39 `03-street-academy.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-fukugyo-anycrew-storeka-gapfill-02a2/earn-fukugyo-anycrew-storeka-gapfill-20260916/03-street-academy.md) | Gap-fill CU-17 (bios + `/fee`) | Thick paste **if** a later human GO. Bios **not** duplicated here |
| [PR#33 `05-street-academy.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-skillshift-sokudan-menta-deep-0734/earn-skillshift-sokudan-menta-deep-20260916/05-street-academy.md) | Deep pack while www was 405 | Pointer. Gate then `needs_check` |
| [PR#3 `07-street-academy.md`](https://github.com/rimone0511/autopilot-log/pull/3) | Week2 paste CU-17 | Pointer |
| [PR#72](https://github.com/rimone0511/autopilot-log/pull/72) | Wave B alive serial **REGISTER-CU-CUT**; ストアカ skipped | Why this note defers |

This folder does **not** rewrite those PRs.

## Skip / park this desk if

www WAF unsolved / OTP missing / 本人確認 upload / 掲載審査 / paid wall / no human GO. Then **stop**. Do not invent a next register desk from here (cut; prefer JOBS).
