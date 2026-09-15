> **DRAFT_ONLY.** Human later only.  
> This authoring agent does **not** retry Freelancer signup or the Earn-money spinner.  
> No secrets. No second account. No bids / fund / KYC from this pack.

# RETRY-LATER — Freelancer.com after `blocked_signup`

Snapshot: **2026-09-16**  
Folder: `ops/earn/freelancer-spinner-block-20260916/`  
Live box: [STATUS.md](STATUS.md)

One later pass, on the operator’s **own** browser and network. MAIN Google (else the same MAIN email). Live form wins.

Observed (do not re-run from this agent): username **`yutaautomates` accepted** → **Earn money** account-type **spinner hung ~35s** → parked. Profile / bids / wallet / KYC were **not** reached.

---

## Do not retry from this agent

| Action | This environment |
|---|---|
| Reload / re-click Earn money while the spinner is up | **No.** Parked. Do not hammer |
| New `/signup` POST from this authoring agent | **No** |
| Second Freelancer account / second Google / Facebook | **No** (Code of Conduct) |
| New username invented in git | **No** |
| Bid / contest / wallet top-up / Verify my Identity | **No** |

Stuck > ~35s on that spinner was enough to park. Playbook sibling also parks a modal after 10 minutes ([PR#66](https://github.com/rimone0511/autopilot-log/pull/66)). Either way: **leave**.

---

## Username tip (letters / numbers)

Freelancer usernames are **letters and numbers** only. No spaces. No `@`. No emoji. Hyphens / underscores / dots: **only if the live wizard accepts them** — do not invent punctuation. Live counter / error text wins.

| Case | What to do later (human) |
|---|---|
| Wizard still offers `yutaautomates` and it stays **accepted** | Keep it. Do not rotate the name “to unstick” the spinner |
| `yutaautomates` is **taken** | **Login first** — MAIN Google, or Email or Username = that handle + local password. Taken name is a hint the hang **may** have created a member. It is **not** a reason to mint a second identity |
| Login fails **and** the operator confirms no mail / no session | Only then pick a **new** handle. Mix **letters + numbers** in the same brand (locally). Example shape: letters the wizard already liked + digits. **Do not commit** the new alias |
| Letters-only retry that collides | Add **digits**. Do not add a second mailbox or Facebook to “get a free name” |

Do not write a filled retry alias into git. Placeholder in the runner remains `{{FREELANCER_USERNAME}}` ([PR#66](https://github.com/rimone0511/autopilot-log/pull/66) FIELD-MAP). This folder records **one** observed accepted name (`yutaautomates`) and the charset tip. Nothing else.

Employer / “hire” is still wrong. Stay **Earn money** / Freelancer / seller.

---

## Human later — order

Live wizard order wins if it differs.

1. **Login first** on [freelancer.com/login](https://www.freelancer.com/login): **Continue with Google** (MAIN). Else Email or Username + local password for the **same** mailbox. If you are already in: do not open `/signup` again.
2. If still mid-wizard: one calm wait. If the Earn-money spinner hangs again (~35s or the 10-minute sibling cap): **park** and write a new observation. Do not loop.
3. Username: letters / numbers per the table above. One name. No second account.
4. Role = **Earn money** / Freelancer. Free membership. Close Plus / extra bids / extra skill slots.
5. If the wizard **finishes**: seller **profile draft only** (headline / summary / skills from sibling paste). **Save draft. Stop.**
6. **No Bid. No contests. No Verify my Identity. No wallet top-up.** Surgical bids stay in siblings until a **later human GO**.

OTP / verify-link = parent Gmail. Do not paste codes into git. SMS / KYC / liveness → close the tab; hand **screen type** (not documents) to morning human. Stop text: sibling [PR#66](https://github.com/rimone0511/autopilot-log/pull/66) STOP-KYC / MONEY-FLAGS — bodies not copied here.

reCAPTCHA may appear. That is **not** KYC. Checkbox / Press & Hold: human on own box. Image puzzle: human only. Do not invent a bypass.

---

## Still forbidden on the later pass

- Second Freelancer account
- Profile URL, leftover bid count, or wallet amount committed to git
- Bid / Place Bid / contest entry (including “free to enter”)
- Sponsored / Highlight / Sealed, Preferred exam, Verified application
- Site-wallet funding / Minimum Account Balance top-up
- Off-platform pay, US/EU location spoof, invented USD / GMV
- Retrying other desks’ `blocked_skip` walls from this folder

Success line if a later human actually saves a profile (secret-free; copy into a **new** STATUS snapshot — do not quietly rewrite this hang):

```
desk: Freelancer.com
cu_hint: draft_saved | already_member_draft | blocked_signup | kyc_wait | wallet_stop
username_wizard: <letters+numbers; do not invent in git unless observed>
draft_profile: yes/no
bid: no
contest: no
wallet_fund: no
kyc: none | wait-morning
next: stop
```

Until that snapshot exists, the desk stays **`blocked_signup`**.

---

## This pack will not

- Complete signup from this authoring agent
- Store passwords, OTP, phone, bank, or ID
- Send bids or fund a wallet
- Merge sibling runner / bid folders

## 日本語（運用だけ）

今はこのエージェントから再試行しない。後で人のブラウザ。まずログイン（MAIN Google / 同じメール）。ユーザー名は **英数字のみ**。`yutaautomates` が取られていたら第二アカウントを作らずログインを先に。新しい名前が要るときだけ英字+数字を混ぜる（git に書かない）。通ってもプロフィール下書きまで。入札・入金・本人確認はしない。
