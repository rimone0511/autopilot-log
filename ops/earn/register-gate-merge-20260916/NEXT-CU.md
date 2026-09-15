# NEXT-CU — Wave B after Freelancer.com

Stamp: **2026-09-16 JST**  
Folder: `ops/earn/register-gate-merge-20260916/`  
State: **DRAFT_ONLY**  
Rollup: [MERGE.md](MERGE.md) · box: [STATUS.md](STATUS.md)

Recommended **Wave B** open path **after** Freelancer.com parks. Desk set: [PR#1](https://github.com/rimone0511/autopilot-log/pull/1) QUEUE. CU labels: [PR#8](https://github.com/rimone0511/autopilot-log/pull/8). Gate labels: this morning merge (#58/#59/#61/#62) plus the earlier JP Wave B `pass` set in [PR#12](https://github.com/rimone0511/autopilot-log/pull/12). Pack pointers are **folder-bearing sibling PRs only** (bodies not copied).

This page is **not** a signup log and does not claim an account exists. **MAIN Google only. DRAFT_ONLY.** Forbidden: secrets, OTP values, phones, passwords, KYC files, publish, paid plans, bids/proposals, invented traffic/GMV.

It does **not** rewrite Wave A [PR#54](https://github.com/rimone0511/autopilot-log/pull/54). Until Freelancer.com is `draft_saved` (or a documented stop that is not a retry of a Wave A skip), the live box stays:

```
Contra (A8 / CU-08) → Craudia (A9 / CU-09) → Freelancer.com (A10 / CU-10)
```

Wave B CU does not start while those three Wave A `pending` rows are still open ([PR#7](https://github.com/rimone0511/autopilot-log/pull/7), [PR#54](https://github.com/rimone0511/autopilot-log/pull/54)).

## Rule for Wave B

After Freelancer parks: open **activity-gate `alive` / `pass` desks only**. Do not promote `needs_check`. Do not treat `thin` (none this morning). Do not subscribe `blocked_paid_plan`.

JP-WEEK2-INDEX CU-11 numbers are **inventory**, not this serial ([PR#7](https://github.com/rimone0511/autopilot-log/pull/7), [PR#8](https://github.com/rimone0511/autopilot-log/pull/8)). Production Google serial for already-`pass` JP desks is [PR#50](https://github.com/rimone0511/autopilot-log/pull/50):

```
Workship (CU-11) → SOKUDAN (CU-13) → Offers (CU-25)
```

This merge **adds** two morning `pass` desks after that Google chain. It does **not** insert Anycrew, 複業クラウド, CrowdLinks, AI CrowdWorks, Workana, YOUTRUST, or PeoplePerHour checkout.

## Serial (after Freelancer parks)

```
Workship (CU-11)
  → SOKUDAN (CU-13)
  → Offers (CU-25)
  → MENTA (CU-16)
  → ストアカ (CU-17)
```

| Order | desk | Gate source | Gate | This pass | pack PR (pointer only) |
|---|---|---|---|---|---|
| 1 | Workship (CU-11) | [PR#12](https://github.com/rimone0511/autopilot-log/pull/12) `pass` (not in #58–#62) | `alive` | **First Wave B desk.** Worker signup. PREFER_GOOGLE (FirebaseUI label at click-time). Profile **draft**. エントリー 0. Stop at 本人確認. | [#3](https://github.com/rimone0511/autopilot-log/pull/3) [#30](https://github.com/rimone0511/autopilot-log/pull/30) [#50](https://github.com/rimone0511/autopilot-log/pull/50) |
| 2 | SOKUDAN (CU-13) | PR#12 `pass` | `alive` | After Workship parks. `/signup/pro`. PREFER_GOOGLE. Profile **draft**. 応募 0. | [#3](https://github.com/rimone0511/autopilot-log/pull/3) [#33](https://github.com/rimone0511/autopilot-log/pull/33) [#50](https://github.com/rimone0511/autopilot-log/pull/50) |
| 3 | Offers (CU-25) | PR#12 `pass` | `alive` | After SOKUDAN. Worker `/worker/signup` (`/signup` is 404). PREFER_GOOGLE. Profile **draft**. 応募 0. | [#30](https://github.com/rimone0511/autopilot-log/pull/30) [#50](https://github.com/rimone0511/autopilot-log/pull/50) |
| 4 | MENTA (CU-16) | **[#61](https://github.com/rimone0511/autopilot-log/pull/61) `pass`** | `alive` | After Offers. Profile **draft** only. Do not submit a mentor plan. Do not complete Stripe identity. | [#3](https://github.com/rimone0511/autopilot-log/pull/3) [#21](https://github.com/rimone0511/autopilot-log/pull/21) [#61](https://github.com/rimone0511/autopilot-log/pull/61) |
| 5 | ストアカ (CU-17) | **[#61](https://github.com/rimone0511/autopilot-log/pull/61) `pass`** | `alive` | After MENTA. Teacher profile **draft**. Email = MAIN Google mailbox (OAuth not offered). No 講座公開. No face-photo certificate. If www WAF 405, park — WAF ≠ dead. | [#3](https://github.com/rimone0511/autopilot-log/pull/3) [#21](https://github.com/rimone0511/autopilot-log/pull/21) [#61](https://github.com/rimone0511/autopilot-log/pull/61) |

Do not start this chain from the markdown-authoring agent. Freelancer.com this pass remains: profile + skills **draft**, **no bids / contests / Verify Identity** ([PR#19](https://github.com/rimone0511/autopilot-log/pull/19), [PR#57](https://github.com/rimone0511/autopilot-log/pull/57)).

## Later / not this Google chain

| desk | Why not next after Freelancer |
|---|---|
| Skill Shift · ITプロパートナーズ | PR#12 `pass`, but [PR#50](https://github.com/rimone0511/autopilot-log/pull/50) left them out (`NOT_OFFERED_OAUTH`). Email-register later, same MAIN mailbox. Not inserted between Offers and MENTA. |
| PeoplePerHour (CU-20) | [#59](https://github.com/rimone0511/autopilot-log/pull/59): marketplace recency **and** seller **`blocked_paid_plan`**. **Do not subscribe** Basic / TopAccess. Zero-cost path = click-time only; if next click is pay, close. |
| Anycrew (CU-15) | [#61](https://github.com/rimone0511/autopilot-log/pull/61) `needs_check`. Human must see one offer-card date first. |
| 複業クラウド · CrowdLinks · AI CrowdWorks | [#62](https://github.com/rimone0511/autopilot-log/pull/62) all `needs_check`. Glance at one rendered listing date (B05: browser `/projects/`; park if still empty — not `dead`). |
| Workana (CU-22) · YOUTRUST (CU-24) | [#59](https://github.com/rimone0511/autopilot-log/pull/59) `needs_check`. Human after Cloudflare / one job-card date. No Priority Moderation. No 公式リクルーター. |
| note · Braintrust · 99freelas · Gulp | [#58](https://github.com/rimone0511/autopilot-log/pull/58) `alive` **keep_queue**, behind Wave A/B. Not next after Freelancer. |
| カイコク | [#58](https://github.com/rimone0511/autopilot-log/pull/58) `needs_check`. Do not SKIP thin. |
| Twago · Xing Projects | [#58](https://github.com/rimone0511/autopilot-log/pull/58) `dead`. skip_log. Do not return unless operator GO. |
| Shufti | QUEUE Wave D `gate` ([PR#8](https://github.com/rimone0511/autopilot-log/pull/8)). Not in #58 sample. Do not register from this sheet. |

`thin`: **0** in #58/#59/#61/#62. Do not invent a thin skip.

## Open-desk rules (Wave B, after Freelancer)

1. One browser profile. MAIN Google picker only. Do not open Gmail in that profile.
2. Worker / 人材 / フリーランス / 講師 face only. Close 企業 / client / enterprise consoles.
3. Profile **draft save**. Discoverable / public toggle **off** if present.
4. 応募 / エントリー / plan publish / 講座公開 / bids = **STOP**.
5. KYC / liveness / Stripe identity / 口座 / 前払い本人確認 = **STOP**. Desk name + screen type to morning operator. No upload.
6. Gmail OTP = parent (CU does not open Gmail). SMS = wait on user chat; if away, park the live desk and keep going to the next **alive** desk only after park.
7. Press & Hold: `holdDurationMs` 1800, one retry 2500. Do not fake hold with click+sleep.
8. Live form wins. Do not invent a third bio, 円, %, or traffic number.
9. Do not buy paid plans (including PPH Basic / TopAccess, CrowdLinks 有料会員, Gulp Membership, Workana Priority, YOUTRUST 公式リクルーター).

## This sheet does not

- Copy or merge sibling PR bodies
- Create marketplace accounts or complete signup from this PR
- Store secrets, OTP, phone, bank, or ID
- Send proposals / invites / bids / 応募
- Start Wave C/D CU (keep_queue from #58 stays behind)
- Retry Wave A `blocked_skip` desks (Fiverr Press&Hold / Lancers captcha / CrowdWorks 403 / Upwork Google access block / LinkedIn reCAPTCHA / TimeTicket DOB missing)
- Open PPH checkout
