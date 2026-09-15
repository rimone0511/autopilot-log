> **DRAFT_ONLY.** Desk box for this resume card.  
> Not a signup log. Does not claim an account exists.  
> No secrets. No bids. No wallet fund. No invented balances.

# STATUS — Freelancer.com username resume card

Snapshot: **2026-09-16** (folder stamp `freelancer-resume-card-20260916`)  
Folder: `ops/earn/freelancer-resume-card-20260916/`  
State: **DRAFT_ONLY — resume card landed; live spinner-resume not run**

Desk: Freelancer.com / Seller (CU-10 / QUEUE A10). Sibling Wave A boxes still treat this desk as `pending` (profile draft after Craudia; **no bids / no contests**). This file does **not** rewrite [PR#49](https://github.com/rimone0511/autopilot-log/pull/49) or [PR#54](https://github.com/rimone0511/autopilot-log/pull/54).

Authoring session: markdown + public GET of Freelancer URLs (no POST, no login). **Did not clear a spinner. Did not accept a username on the live form. Did not Bid. Did not fund.**

Forbidden in this PR: secrets, OTP, phones, passwords, KYC files, Bid, contest entry, wallet top-up, leftover-bid counts, fee-table amounts, GMV, a live `freelancer.com/u/...` profile URL.

---

## Verdict

| Item | Status |
|---|---|
| This resume card (spinner → `yutaautomates`) | **ready · draft** (markdown only) |
| Live spinner-resume pass | **not run** from this agent |
| Username on this card | **`yutaautomates`** — operator-supplied **already accepted**; letters/numbers only |
| Live seller account in git | **not claimed** |
| Bid / Place Bid | **forbidden** |
| Site wallet / Minimum Account Balance fund | **forbidden** |
| Username-change purchase | **forbidden** |
| CU-10 full signup runner | sibling [PR#66](https://github.com/rimone0511/autopilot-log/pull/66) — not this folder |
| Wave A Freelancer.com box | leave **`pending`** — do not jump the serial |

---

## Resume fact (do not upgrade into “account exists”)

Operator instruction for this pack:

1. When the Freelancer **spinner clears later**, resume.
2. Username = **`yutaautomates`** (already accepted).
3. **Letters and numbers only** (alphanumeric, starts with a letter, 16 characters at most). This handle is 13 letters, starts with `y`.

That is a **resume handle**, not a livecheck that the string is still free, and not a public profile URL. If a later live check rejects it: park `username_rejected_after_spinner`. Do not invent a retry alias in git.

---

## What exists

In **this** PR:

- [OPERATOR-CARD.md](OPERATOR-CARD.md) — park while spinning; resume with `yutaautomates`; no Bid; no fund
- [STATUS.md](STATUS.md) — this file

On sibling earn-ops desks (bodies not copied; paths on **those** branches):

| Pack | Path (PR branch) | PR |
|---|---|---|
| CU handoff (MAIN Google/email, profile draft, stop) | `ops/earn/freelancer-cu-handoff-20260916/` | [#66](https://github.com/rimone0511/autopilot-log/pull/66) |
| Profile + gap notes | `earn-freelancer-waveb-gap-notes-20260916/` | [#19](https://github.com/rimone0511/autopilot-log/pull/19) |
| Surgical-bid templates (do-not-send) | `earn-freelancer-surgical-bid-templates-20260916/` | [#47](https://github.com/rimone0511/autopilot-log/pull/47) |
| Profile/bid polish | `ops/earn/freelancer-surgical-polish-20260916/` | [#57](https://github.com/rimone0511/autopilot-log/pull/57) |
| JOBS bid-ready (precondition: account already exists) | `earn-jobs-freelancer-bid-ready-20260916/` | [#68](https://github.com/rimone0511/autopilot-log/pull/68) |
| Wave A STATUS snapshot | `earn-register-status-snapshot-20260916-0519/` | [#49](https://github.com/rimone0511/autopilot-log/pull/49) |
| Wave A morning-loop STATUS | `ops/earn/register-wave-a-status-20260916/` | [#54](https://github.com/rimone0511/autopilot-log/pull/54) |
| TODAY apply queue | `earn-jobs-apply-queue-today-20260916/` | [#88](https://github.com/rimone0511/autopilot-log/pull/88) |

`{{FREELANCER_USERNAME}}` in sibling field maps stays a placeholder there. This card is the **one** place that names `yutaautomates` as the resume handle. Do not spray that string into bid letters.

---

## Public livecheck (authoring, 2026-09-15/16 GET, no POST)

`thin_site_skip: false` (public pages returned HTTP 200). Help bodies are often SPA — **do not freeze article prose**. Username charset is cited from public getting-started / username-guidelines titles already used in sibling CU packs; **live widget wins**.

| URL | HTTP | Note |
|---|---|---|
| https://www.freelancer.com/ | 200 | Home. Marketing totals are vendor copy — not a gate count |
| https://www.freelancer.com/signup | 200 | Resume starts here if the wizard is still signup. **No POST** |
| https://www.freelancer.com/login | 200 | Existing member path. MAIN Google / same email |
| https://www.freelancer.com/support/general/how-to-get-started-at-freelancer-com | 200 | Username: alphanumeric, starts with a letter, 16 max (help; live form wins) |
| https://www.freelancer.com/support/general/username-guidelines | 200 | Same charset. SPA body may be empty on GET |
| https://www.freelancer.com/support/employer/profile/username-change-request | 200 | **Do not file.** Paid extra — skip |
| https://www.freelancer.com/feesandcharges | 200 | Cite URL only. **Do not copy amounts** |
| https://www.freelancer.com/page.php?p=info%2Fkyc_policy | 200 | Identity Policy. STOP, not a fill guide |
| https://www.freelancer.com/about/terms | 200 | User Agreement (min balance rule exists; this card does not Bid) |
| https://www.freelancer.com/info/codeofconduct | 200 | No spam, no off-site pay, no multiple accounts |

This GET did **not** observe the live username spinner. Do not invent a screenshot. Spinner protocol is for the **later** human/CU pass.

---

## Live resume outcome (empty until a human/CU runs the card)

Do not pre-fill success.

```
desk: Freelancer.com
pack: ops/earn/freelancer-resume-card-20260916/
spinner:
username_on_screen:
username_accepted:
letters_numbers_only:
second_username_tried: no
bid: no
contest: no
wallet_fund: no
kyc_upload: no
username_change_purchased: no
next: park | sibling_profile_draft | morning_human
```

Current: **not run**. Valid later outcomes: `spinner_wait` | `username_accepted` | `username_rejected_after_spinner` | `username_step_already_past` | `hold_failed` | `wallet_stop` | `kyc_wait` | `oauth_overreach`.

---

## Next (parent / later CU)

1. If the spinner is still up: **do not resume.** Keep this card. No Bid. No fund.
2. When it **clears**: open [OPERATOR-CARD.md](OPERATOR-CARD.md). Handle = **`yutaautomates`**. Letters/numbers only. Pick once.
3. After username: sibling CU profile **draft** only ([PR#66](https://github.com/rimone0511/autopilot-log/pull/66)). Still no Bid.
4. JOBS bid letters ([PR#68](https://github.com/rimone0511/autopilot-log/pull/68) / queue [PR#88](https://github.com/rimone0511/autopilot-log/pull/88)) stay **do-not-send** until a later human GO **and** a seller account actually exists.
5. Do not rewrite Wave A STATUS from this folder.

---

## This PR / pack will not

- Create or log into a Freelancer account from this authoring agent
- Claim the live spinner was seen or cleared
- Invent or commit Google / email secrets / password / OTP / phone / bank
- Click Bid, enter contests, or fund the Site wallet
- Buy membership, bid upgrades, or a username-change extra
- Open Verify my Identity, or write KYC how-to beyond STOP
- Copy fee amounts, leftover bid counts, or a live wallet balance into git
- Merge sibling pack folders or rewrite QUEUE / Wave A STATUS
- Change Python posting-gate tests

## Verification (this PR)

- [x] Two markdown files under `ops/earn/freelancer-resume-card-20260916/`
- [x] `DRAFT_ONLY` / no secrets / no Bid / no fund / letters-numbers-only / `yutaautomates` in pack headers
- [x] No live phones/passwords/OTP; no invented profile URL; no fee amounts
- [x] Public GET 200 on signup/login/help/fees/KYC policy (no POST)
- [x] Python posting-gate tests untouched
- [ ] Human/CU: run OPERATOR-CARD when the spinner clears; do not merge as an auto-bidder
- [ ] Do not merge until Yuta reviews; keep draft

## 日本語（運用だけ）

スピナーが消えるまで待つ。消えたらユーザー名は **`yutaautomates`**（accepted 済み）。英数字のみ。入札しない。入金しない。アカウント有を捏造しない。Wave A の箱は書き換えない。
