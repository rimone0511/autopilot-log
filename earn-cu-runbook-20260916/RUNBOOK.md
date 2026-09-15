# CU serial runbook — earn-ops register (2026-09-16)

Audience: a **computer-use (CU)** Cursor agent running a browser for **one human operator**.
Operator: 石田祐太 / Yuta Ishida (`rimone0511`).
Repo: [autopilot-log](https://github.com/rimone0511/autopilot-log).
Mode: **DRAFT_ONLY**. This file is a playbook. It is not a live account, not a KYC packet, and not a publish GO.

Sibling queue (source of wave order): `{{QUEUE}}` = `earn-register-expand-20260916/QUEUE.md`.

---

## 0. One-screen GO / NO-GO

### 日本語（朝の本人）

- 認証は **MAIN Google `rimone0511@gmail.com` だけ**。別アカウントを作らない。
- プロフィール・出品・サービス・SNS はすべて **下書き**。公開しない。
- 本人確認（免許・パス・マイナンバー・顔写真・住民票・口座）が出たら **即停止**。アップロードしない。朝の本人へ机名と画面の種類だけ渡す。
- Gmail のワンタイムコードは **親エージェントの Gmail MCP** が読む。CU ブラウザで Gmail を開かない。
- SMS コードは **ユーザーチャット待ち**。推測しない。
- 長押し UI は連打しない。**Press & Hold に `holdDurationMs` を必ず付ける。**

### English (CU must obey)

| Switch | Value | If you cannot keep it |
|---|---|---|
| Account | MAIN Google `rimone0511@gmail.com` only | STOP. Do not create a second identity. |
| Publish | `DRAFT_ONLY` (profiles, gigs, tickets, LinkedIn Services, SNS) | STOP. Do not toggle public / submit / post. |
| KYC | Stop. Morning user. No uploads | Hand off. Do not continue the desk. |
| Email OTP | Parent Gmail MCP | Do not open `mail.google.com` in the CU profile. |
| SMS OTP | User chat | Wait. Do not guess. Do not use a second phone. |
| Press & Hold | `holdDurationMs` required | Do not fake a hold with click+sleep+click. |
| Secrets | Never in git, never in this runbook, never in screenshots of codes | Redact. |

**Start here:** Wave A remaining serial (Coconala and Gumroad are already `done-draft` — do not reopen them to publish).

```
Fiverr → Lancers → CrowdWorks → Upwork → LinkedIn Services
  → TimeTicket → Contra → Craudia → Freelancer.com
  → Wave B desks that already have an activity-gate pass
```

One desk per loop. Do not parallelize logins.

---

## 1. What this runbook is

A **thick CU serial** for marketplace **seller/worker registration** under earn-ops GO 2026-09-16.

You will:

1. Open the seller/worker entry URL.
2. Sign in or sign up with **MAIN Google** (or the same mailbox if Google OAuth is absent).
3. Fill a **draft** profile / gig / ticket / service from a paste pack (placeholders only).
4. Stop before identity verification, payout, paid plans, and publish.
5. Write a secret-free session line, then open the next desk.

You will **not**:

- Publish gigs, tickets, Services pages, proposals, or social posts.
- Upload ID, My Number, selfie-with-ID, address proof, or bank/Stripe identity.
- Buy Connects, memberships, featured listings, or Fast-Track KYC.
- Invent traffic counts, GMV, or “how much you can earn”.
- Scrape, like, follow, or message clients.
- Operate YouTube/TikTok posting. That is Autopilot Log CLI + posting-gate, fail-closed, and out of this serial.

---

## 2. Hard policies (do not “interpret around”)

### 2.1 MAIN Google `rimone0511`

- The only Google account is **`rimone0511@gmail.com`**.
- If the Google account picker lists several rows, click **that address only**.
- Never click **Use another account** to add a new Google user.
- Never create a marketplace-only mailbox (`+desk@…` is forbidden in this GO).
- Prefer **Continue with Google / Googleで登録** whenever the button is visible.
- If Google OAuth is **not** offered (TimeTicket is the likely case): register with **email = the same MAIN Gmail**. Do not invent Facebook/LINE/Apple as a new identity. If the site forces LINE/Apple and email is impossible, **STOP** and ask the morning user — do not bind a random social.
- Apple / Facebook / Yahoo are **fallback only** when Google is missing **and** the fallback is an identity the operator already owns **and** the morning user has said so in chat. Default: stop and ask.

### 2.2 Draft only

Draft means:

- Profile visibility = hidden / private / 非公開 / not discoverable, when the control exists.
- Gigs, tickets, Catalog projects, LinkedIn Services: **save**, never **Publish** / **公開する** / **Submit for review** if review equals public.
- Proposals, bids, quotes, Connects spend: **do not send**.
- Partner applications (Zapier / Make / n8n / Toptal): **out of this serial** (`late`, morning user).

If the site has no draft (the next click is always public), **STOP** and record `no_draft_path`. Do not publish “just this once”.

### 2.3 SNS `DRAFT_ONLY`

SNS here means X, LinkedIn **feed**, Instagram, Facebook, TikTok, Threads, and any in-app “share that you joined”.

| Allowed | Forbidden |
|---|---|
| Paste **already-public** URLs into a profile field (`https://yutalab.dev/`, `https://github.com/rimone0511`) | New posts, tweets, stories, “I’m now on Fiverr” |
| LinkedIn **Services** draft (see A6) | LinkedIn **Jobs** applications; feed posts; newsletter send |
| Saving a social composer as **draft** if the UI has it | Opening Autopilot Log posting-gate; TikTok/YouTube publish |
| Recording “site asked to tweet, I refused” | Using X MCP / Gmail send / Calendar public invites as promo |

Autopilot Log’s `posting-gate.json` stays **closed**. This CU serial does not post video or social.

If onboarding **blocks** until you post to SNS: stop, screenshot the **blocker text only** (no OTP, no ID), mark `sns_block`, morning user.

### 2.4 KYC → morning user

KYC is any of:

- Government photo ID, passport, residence card, driver’s license
- My Number / マイナンバー / 通知カード
- Selfie, liveness, “hold your ID next to your face”
- Proof of address, utility bill, juminhyo
- Bank account, 口座, Stripe Identity, payout tax forms (W-8, invoice-registered number) **when they are identity checks**
- Credit-card microcharge “to verify you”
- Paid identity review fees

**Agent action:** close the upload widget **without** files. Do not crop ID out of a screenshot. Chat the morning user: desk name + which of the bullets above. Leave the desk as `kyc_wait` (not SKIP). Continue the **next** desk only if KYC is not a hard lock on the whole browser session.

### 2.5 No secrets in artifacts

Never commit or paste into git:

- Passwords, refresh tokens, cookies, session strings
- Full OTP codes
- Full phone numbers (mask to last 2–4 on-screen digits if you must describe SMS)
- ID numbers, bank, tax IDs
- Gmail message bodies (parent may read them; you log `otp_received=yes` only)

---

## 3. Operator identity (public / placeholder)

Replace from the local ledger. **Do not fill real private values into this repo.**

| Token | Meaning | Public default (safe) |
|---|---|---|
| `{{GOOGLE_ACCOUNT_EMAIL}}` | MAIN Google | `rimone0511@gmail.com` (login identity; still treat inbox contents as secret) |
| `{{EMAIL}}` | Same mailbox | same as Google |
| `{{DISPLAY_NAME}}` | Profile display | `石田祐太` / `Yuta Ishida` |
| `{{LEGAL_NAME_KANJI}}` | Legal name | ledger only |
| `{{LEGAL_NAME_KANA}}` | Kana | ledger only |
| `{{FULL_LEGAL_NAME}}` | Latin legal name for EN desks | ledger only |
| `{{PHONE}}` / `{{PHONE_E164}}` | Mobile for SMS | ledger only; CU never types a second number |
| `{{COUNTRY}}` | | `Japan` |
| `{{TIMEZONE}}` | | `Asia/Tokyo` |
| `{{PREFECTURE}}` `{{CITY}}` `{{POSTAL_CODE}}` | Address | ledger only; skip if not required for draft |
| `{{PORTFOLIO_URL}}` | | `https://yutalab.dev/` |
| `{{GITHUB_URL}}` | | `https://github.com/rimone0511` |
| `{{GITHUB_REPO_AUTOPILOT}}` | | `https://github.com/rimone0511/autopilot-log` |
| `{{PHOTO_LOCAL_PATH}}` | Face photo | local path; **do not commit** |
| `{{PASSWORD_DO_NOT_STORE}}` | Email-path password | never git, never chat |
| `{{INVITE_CODE}}` | | empty unless user supplies |

**Seller one-liner (English, public):** n8n / AI automation + operator docs. Official APIs only. No browser scraping. No engagement bots.

**Seller one-liner (日本語, public):** AI業務自動化と手順書。公式APIのみ。ブラウザ自動操作・いいね自動化はしない。公開は人が決める。

If a paste pack is missing, use the one-liners + public URLs only. Do not invent years of experience or rates. Leave rate fields empty or “要相談” / “Contact”.

---

## 4. Document map and paste-pack path placeholders

Paste packs are written by sibling agents and may not be merged yet. **Resolve paths. Do not invent file contents.**

### 4.1 Root placeholders

| Placeholder | Expected path (repo-relative) | What lives there |
|---|---|---|
| `{{QUEUE}}` | `earn-register-expand-20260916/QUEUE.md` | Wave order, `done-draft` / `next` |
| `{{ACTIVITY_GATE}}` | `earn-register-expand-20260916/ACTIVITY-GATE.md` | Checklist; no invented counts |
| `{{SKIP}}` | `earn-register-expand-20260916/SKIP.md` | Closed / identity-only / aggregators / local / thin |
| `{{PASTE_PACK_ROOT_TOP10}}` | `earn-register-packs-top10-20260916/` | Wave A desk packs (may be empty) |
| `{{PASTE_PACK_ROOT_LEGACY}}` | `earn-packs/` | QUEUE’s older pack hint (`earn-packs/fiverr/` …) |
| `{{PASTE_PACK_ROOT_JP_WEEK2}}` | `earn-register-packs-jp-20260916/` | Wave B JP packs + `JP-WEEK2-INDEX.md` |
| `{{PASTE_PACK_ROOT_GLOBAL_WEEK2}}` | `earn-register-packs-20260916/` | Guru / PPH / Malt / Workana + gate |
| `{{REGISTER_PACK_INDEX}}` | `earn-register-pack-index-20260916/` | Sibling INDEX agent (may land later) |
| `{{FIVERR_GIG_PACK}}` | `earn-register-packs-top10-20260916/02-fiverr.md` **or** sibling Fiverr gig folder | Gig field map |
| `{{UPWORK_CATALOG_PACK}}` | `earn-register-packs-top10-20260916/05-upwork.md` **or** sibling Catalog folder | Catalog drafts; still unpublished |
| `{{KYC_MORNING}}` | `earn-kyc-morning-20260916/` | Morning-user KYC checklist (sibling) |
| `{{WAVE_B_JP_GATE}}` | `earn-activity-gate-wave-b-jp-20260916/` | Sibling JP Wave B pass/fail notes |
| `{{WAVE_B_GLOBAL_GATE}}` | `earn-register-packs-20260916/ACTIVITY-GATE-week2-global.md` | Global pass / needs_check / paid-plan |
| `{{EN_PROPOSAL_DRAFTS}}` | `earn-proposal-drafts-en-20260916/` | **Do not send.** Draft text only |
| `{{JP_PROPOSAL_DRAFTS}}` | `earn-proposal-drafts-jp-20260916/` | **Do not send.** Draft text only |
| `{{SESSION_LOG_DIR}}` | `earn-cu-runbook-20260916/sessions/` | Optional logs; create only if secret-free |

If a folder is absent on the branch you checked out, treat the placeholder as **unresolved**. Continue with this runbook’s desk card. Record `pack_status: missing`.

### 4.2 Resolution order (every desk)

1. Exact file in the desk card’s **Pack paths** list, first hit on disk.
2. Glob: `**/NN-<slug>*.md` under the roots above.
3. `{{REGISTER_PACK_INDEX}}` if present (follow its table, do not reorder Wave A).
4. This runbook’s inline field map + public one-liners.
5. If the live form contradicts the pack, **the live form wins**. Patch nothing in git during the CU session except the session log.

Never block the serial solely because a pack PR is still draft. Packs are paste hints, not licenses to publish.

### 4.3 Wave A pack path table (placeholders)

| Serial | Desk | Placeholders (try in order) |
|---|---|---|
| A2 | Fiverr | `{{PASTE_PACK_FIVERR}}` → `{{PASTE_PACK_ROOT_TOP10}}/02-fiverr.md` → `{{PASTE_PACK_ROOT_LEGACY}}/fiverr/` → `{{FIVERR_GIG_PACK}}` |
| A3 | Lancers | `{{PASTE_PACK_LANCERS}}` → `{{PASTE_PACK_ROOT_TOP10}}/03-lancers.md` → `{{PASTE_PACK_ROOT_LEGACY}}/lancers/` |
| A4 | CrowdWorks | `{{PASTE_PACK_CROWDWORKS}}` → `{{PASTE_PACK_ROOT_TOP10}}/04-crowdworks.md` → `{{PASTE_PACK_ROOT_LEGACY}}/crowdworks/` |
| A5 | Upwork | `{{PASTE_PACK_UPWORK}}` → `{{PASTE_PACK_ROOT_TOP10}}/05-upwork.md` → `{{UPWORK_CATALOG_PACK}}` → `{{PASTE_PACK_ROOT_LEGACY}}/upwork/` |
| A6 | LinkedIn Services | `{{PASTE_PACK_LINKEDIN_SERVICES}}` → `{{PASTE_PACK_ROOT_TOP10}}/06-linkedin-services.md` → `{{PASTE_PACK_ROOT_LEGACY}}/linkedin-services/` |
| A7 | TimeTicket | `{{PASTE_PACK_TIMETICKET}}` → `{{PASTE_PACK_ROOT_TOP10}}/07-timeticket.md` → `{{PASTE_PACK_ROOT_LEGACY}}/timeticket/` |
| A8 | Contra | `{{PASTE_PACK_CONTRA}}` → `{{PASTE_PACK_ROOT_TOP10}}/08-contra.md` → `{{PASTE_PACK_ROOT_LEGACY}}/contra/` |
| A9 | Craudia | `{{PASTE_PACK_CRAUDIA}}` → `{{PASTE_PACK_ROOT_TOP10}}/09-craudia.md` → `{{PASTE_PACK_ROOT_LEGACY}}/craudia/` |
| A10 | Freelancer.com | `{{PASTE_PACK_FREELANCER}}` → `{{PASTE_PACK_ROOT_TOP10}}/10-freelancer.md` → `{{PASTE_PACK_ROOT_LEGACY}}/freelancer/` |

### 4.4 Wave B pack path table (placeholders)

QUEUE Wave B order. **CU-11 numbering in `JP-WEEK2-INDEX.md` is inventory, not this serial.** After A10, use QUEUE order **filtered by activity-gate pass** (§13).

| QUEUE | Desk | Pack placeholders |
|---|---|---|
| B1 | SOKUDAN | `{{PASTE_PACK_ROOT_JP_WEEK2}}/01-sokudan.md` |
| B2 | Workship | `{{PASTE_PACK_ROOT_JP_WEEK2}}/02-workship.md` |
| B3 | 複業クラウド | `{{PASTE_PACK_ROOT_JP_WEEK2}}/03-fukugyo-cloud.md` |
| B4 | CrowdLinks | `{{PASTE_PACK_ROOT_JP_WEEK2}}/04-crowdlinks.md` |
| B5 | Anycrew | `{{PASTE_PACK_ROOT_JP_WEEK2}}/05-anycrew.md` |
| B6 | MENTA | `{{PASTE_PACK_ROOT_JP_WEEK2}}/06-menta.md` |
| B7 | ストアカ | `{{PASTE_PACK_ROOT_JP_WEEK2}}/07-street-academy.md` |
| B8 | Guru | `{{PASTE_PACK_ROOT_GLOBAL_WEEK2}}/01-guru-com-seller-profile-draft.md` |
| B9 | PeoplePerHour | `{{PASTE_PACK_ROOT_GLOBAL_WEEK2}}/02-peopleperhour-hourlies-draft.md` |
| B10 | Malt | `{{PASTE_PACK_ROOT_GLOBAL_WEEK2}}/03-malt-com-eu-draft.md` |
| B11 | Workana | `{{PASTE_PACK_ROOT_GLOBAL_WEEK2}}/04-workana-draft.md` |
| B12 | Freelancermap | `{{PASTE_PACK_FREELANCERMAP}}` → `{{PASTE_PACK_ROOT_GLOBAL_WEEK2}}/05-freelancermap.md` → `{{PASTE_PACK_ROOT_TOP10}}/wait-wave-b/` |
| B13 | YOUTRUST | `{{PASTE_PACK_YOUTRUST}}` → `{{PASTE_PACK_ROOT_JP_WEEK2}}/09-youtrust.md` |
| B14 | Offers | `{{PASTE_PACK_OFFERS}}` → `{{PASTE_PACK_ROOT_JP_WEEK2}}/10-offers.md` |
| B15 | AI CrowdWorks | `{{PASTE_PACK_AI_CROWDWORKS}}` — **gate first**; no pack required to skip |
| B16 | Skill Shift | `{{PASTE_PACK_SKILLSHIFT}}` → `{{PASTE_PACK_ROOT_JP_WEEK2}}/11-skillshift.md` |
| B17 | ITプロパートナーズ | `{{PASTE_PACK_ITPRO}}` → `{{PASTE_PACK_ROOT_JP_WEEK2}}/12-itpropartners.md` |
| B+ | Shufti (optional Med) | `{{PASTE_PACK_ROOT_JP_WEEK2}}/08-shufti.md` — only if Wave D/Med gate **pass** |

Unresolved B12–B17 packs: still allowed **if** `{{WAVE_B_JP_GATE}}` / `{{ACTIVITY_GATE}}` says `pass`. Use this runbook’s generic Wave B loop.

---

## 5. CU environment preflight (before the first URL)

Do this once per session.

1. **Confirm you are the CU serial agent**, not a pack-author. You may type in a browser. You may not publish.
2. **Viewport:** desktop width ≥ 1280px for Fiverr / Upwork / LinkedIn. JP desks work at 1280 as well. Do not switch to a phone emulator mid-serial unless a site dead-ends on desktop (record it).
3. **Browser profile:** one profile for marketplaces. **Do not** also live in Gmail in that profile.
4. **Language:** accept JP UI on JP desks, EN UI on EN desks. Do not change the operator’s Google language as a side effect.
5. **Cookies:** if a previous CU left a **different** Google user signed in, sign **out** of that Google user, then sign in `rimone0511`. If you cannot tell which user, STOP and ask.
6. **Paid-plan / wallet:** no credit card on file should be added in this serial. If a site demands a card for “free signup”, STOP (`card_wall`).
7. **Extensions / password managers:** do not save marketplace passwords into a shared vault from CU.
8. **Timebox:** 15–25 minutes per desk (QUEUE). KYC stop ends the desk immediately, even at minute 2.
9. **Captcha:** human-in-the-loop. If CU cannot solve it, chat the user. Do not outsource captcha to a third-party farm.
10. **reCAPTCHA / “Press and hold”:** see §6.3. Use `holdDurationMs`. Never hammer the checkbox.

If preflight fails, do not start Fiverr.

---

## 6. Computer-use input grammar

### 6.1 Default actions

| Intent | Action | Notes |
|---|---|---|
| Open a control | **Click** (short) | Buttons, links, checkboxes, radios |
| Enter text | **Type** / paste | Prefer paste from pack; then tab out so validation runs |
| Clear a field | Select-all + type | Do not send 50 Backspaces if select-all works |
| Scroll | Wheel / key | Confirm the target is in view before click |
| File picker | Stop if the file is ID/KYC | Profile photo from `{{PHOTO_LOCAL_PATH}}` is allowed if not an ID scan |
| New tab | Avoid | OAuth popups are the exception; wait for them |

### 6.2 What is not a click

These are **Press & Hold** (or drag), not clicks:

- Labels: `Press and Hold`, `Press & Hold`, `長押し`, `押し続ける`, `Hold to confirm`, `Hold the button`
- Cloudflare / some bot walls: **Press & Hold** to continue
- Long-press to open a context menu (Windows-style)
- Slider thumbs that only move after a grab
- Some Google identity / device prompts on touch-styled webviews
- Drag-and-drop avatar: **press (hold) → move → release**

### 6.3 Press & Hold — `holdDurationMs` is mandatory

When the UI needs a hold, the CU tool call **must** include **`holdDurationMs`** (integer, milliseconds).

Do **not**:

- Click, `sleep`, click again
- Repeat `mouse_down` without a duration
- Hold with `keyDown` on Space unless the site documents that, and still set `holdDurationMs` on the pointer hold if both exist
- Assume 100ms is enough because a click is 100ms

**Starting values (adjust once, then record):**

| UI class | `holdDurationMs` | Then |
|---|---|---|
| Long-press menu | `800` | Release; click the menu item separately |
| Cloudflare / bot “Press & Hold” | `1800` | If it fails, retry **once** at `2500`. Second fail → STOP (`hold_failed`) |
| “Hold to confirm” submit | `2000` | Watch for progress ring; do not release early |
| Drag start (avatar / slider) | `400` hold, then move | Release on drop target |
| Mobile-style tab bar long-press | `600` | Rare on desktop; still set the param |

**Tool-call shape (logical; map onto the live CU schema):**

```yaml
action: press_and_hold          # or mouse_down / pointer_down — live schema wins
target: <visible button whose label is Press & Hold / 長押し>
holdDurationMs: 1800            # REQUIRED — never omit on hold intents
# optional:
reason: "Cloudflare press-and-hold on CrowdWorks signup"
```

If the current CU schema has **no** `holdDurationMs` field, **STOP**. Write `tool_missing_holdDurationMs`. Do not emulate. The morning user must switch the CU tool, not you.

After a successful hold, log:

```
hold: yes | target: "Press & Hold" | holdDurationMs: 1800 | result: passed
```

### 6.4 Typing OTP

- Click the OTP field.
- Type the code **once** (no leading spaces).
- Do not paste OTP into chat, git, or a second site.
- If the field is one box per digit, type sequentially; do not click the first box 6 times without characters.

---

## 7. MAIN Google login play (every desk)

1. Land on the official host (desk card). Reject lookalike domains (`lancers.com` vs `lancers.jp`, `crowd-works` typos, `fiverrgigs.example`).
2. Confirm **seller / ランサー / ワーカー / Independent / Freelancer**, not client / 依頼者 / Employer / 企業管理.
3. Click Google. On the picker, **`rimone0511@gmail.com`**.
4. Consent screen: allow only the marketplace’s requested basic profile/email. If it asks for Gmail **read all mail**, Drive, Contacts dump — **Deny** and STOP (`oauth_overreach`).
5. If Google says **this app is blocked / unverified**: STOP. Morning user. Do not click through advanced “unsafe” unless the user types GO in chat for **that desk**.
6. If the site says the Google address is already registered: **Sign in**, do not create a second user.
7. After login, if you land on a buyer home: switch role (Become a Seller / 仕事を受けたい / Freelancer). If you cannot switch without KYC, stop as KYC.

---

## 8. OTP

Two pipes. Do not mix them. Do not use phone-as-email, and do not use Gmail to receive SMS.

### 8.1 Gmail OTP — **parent** (not the CU browser)

**Parent** = the cloud agent that holds **Gmail MCP** as `rimone0511@gmail.com` (or a parent orchestrator with that MCP). **CU child does not open Gmail.**

Sequence:

1. CU triggers “send code / 認証メール” on the marketplace.
2. CU chats the parent (or the same agent, **out of band of the browser**):

   ```
   otp_request:
     desk: Fiverr
     channel: gmail
     to: MAIN Google (do not print if you already know)
     from_hint: fiverr.com / notifications@fiverr.com
     requested_at_jst: <timestamp>
     field: 6-digit | magic-link | unknown
   ```

3. Parent searches Gmail MCP, for example:

   ```
   newer_than:1d (from:fiverr.com OR from:lancers.jp OR from:crowdworks.jp OR subject:(code OR verify OR 確認 OR 認証 OR ワンタイム))
   ```

   Narrow to the desk. Open **the thread**, not spam-looking lookalikes.

4. Parent extracts the code or magic-link. Parent **types or hands the code to CU in the CU session**. Parent does **not** commit it. Parent does **not** forward the whole mail to a third party.

5. CU enters the code. CU logs `gmail_otp: entered` without digits.

6. If nothing arrives in **3 minutes**: parent searches again once (Promotions / Updates tabs via query, not by CU clicking Gmail). If still empty: STOP (`otp_missing`). User chat.

**Forbidden:** `mail.google.com` in the marketplace browser; downloading `.eml` into the repo; using a second Gmail.

Magic-link exception: if the mail is **only** a link, parent returns the URL to CU. CU opens it **in the same marketplace profile**. Parent still does not click it from a different IP if the site binds sessions — prefer CU.

### 8.2 SMS OTP — **user chat only**

Sequence:

1. CU reaches phone verify. Prefer **skip** if the site allows selling later without it (Fiverr often does **not** allow publish without SMS — that is fine: we are not publishing).
2. If skip exists, skip. Record `sms: skipped`.
3. If the form **blocks draft save** without SMS:
   - Fill `{{PHONE}}` from the ledger **only if the user already placed it in chat this session**.
   - If the ledger is not in chat, ask: “SMS for {desk}. Reply with the E.164 number to use, or say SKIP desk.”
4. After send, CU chats:

   ```
   sms_otp_wait:
     desk: Fiverr
     masked_on_screen: ***1234   # only what the page shows
     action_needed: paste the SMS code in this chat
     do_not_send: full number, ID photos
   ```

5. Wait. Do not poll the phone. Do not use SMS-to-email gateways. Do not use a “virtual number” service.
6. User pastes the code. CU enters it once. Log `sms_otp: entered` without digits.
7. If the user is asleep / unavailable: **park the desk** (`sms_wait_user`). Continue to the **next** desk that does not need SMS. Do not burn the number with extra resends (max **one** resend, then park).

Voice-call fallback: treat as SMS (user must listen). CU does not place the call.

---

## 9. Per-desk loop (the serial)

```
for desk in [A2..A10] then Wave-B-passes:
  1. Read this desk card + resolve paste pack (§4).
  2. Open official URL. Activity sniff (alive? closed? employer-only?).
     Closed → SKIP.md language, do not register.
  3. Seller/worker path. Google (or same-mailbox email).
  4. OTP via §8.
  5. Stop lights: KYC, paid plan, SNS publish, card wall.
  6. Paste draft fields. Save. Do not publish.
  7. Session log line (§14). Next desk.
```

**Already registered** with MAIN Google: do not duplicate. Open profile, confirm draft/hidden, mark `done-draft` / `already_member_draft`. Still no publish.

**Captcha hold:** §6.3.

**Stuck > 10 minutes** on one modal: screenshot **non-secret** UI, park desk, next.

---

## 10. Wave A desk cards (serial)

Skip **A1 ココナラ** and **A+ Gumroad** (`done-draft` as of 2026-09-16 JST). Do not publish them “while you are here”.

Shared stop line for every card: KYC, payout, paid boost, public toggle.

### A2 — Fiverr

| | |
|---|---|
| Role | **Seller**. After join: Become a Seller. |
| Entry | https://www.fiverr.com/join — Google: **Continue with Google** |
| Help | https://help.fiverr.com/hc/en-us/articles/360050063113-Creating-your-Fiverr-account |
| KYC help | https://help.fiverr.com/hc/en-us/articles/22582440968849-Personal-business-information-verification |
| Google | **PREFER_GOOGLE** |
| OTP | Email code → **Gmail parent**. Phone verify → **SMS user chat**. Skip phone if seller draft can exist without it. |
| Draft artifact | Username chosen; seller onboarding **stopped before** Personal & Business Info / Identity; Gig **saved unpublished** if the UI allows. If Gig save requires ID, **do not create the Gig**. Profile text only. |
| Pack | `{{PASTE_PACK_FIVERR}}` / `{{FIVERR_GIG_PACK}}` |
| Hold | Cloudflare on join is common. `holdDurationMs: 1800`. |
| Do not | Publish Gig; Fiverr Pro apply; Promoted Gigs; ID upload before first Gig (help says new sellers may be asked **before publish** — that is a stop, not a GO). |

Field hints (if pack missing): title around “n8n / AI automation / operator docs”; EN; no fake social proof.

### A3 — Lancers（ランサーズ）

| | |
|---|---|
| Role | 仕事を受けたい / ランサー. Not 仕事を依頼したい. |
| Entry | https://www.lancers.jp/user/sign_up/ — **Google** |
| Home | https://www.lancers.jp/ |
| Google | **PREFER_GOOGLE** (Yahoo / Facebook / Apple exist — ignore) |
| OTP | Mail magic-link → **Gmail parent**. Do not open mail in CU. |
| Draft artifact | ユーザー名; 利用方法 = フリーランス/副業; プロフィール自己紹介 **下書き**. 出品公開しない. |
| Pack | `{{PASTE_PACK_LANCERS}}` |
| KYC stop | 本人確認、源泉、口座、マイナンバー、ランサーズかんたん税金 |
| Notes | 仮登録メールの期限を過ぎたら親が再送指示。CU は再送ボタンを1回まで. |

### A4 — CrowdWorks（クラウドワークス）

| | |
|---|---|
| Role | ワーカー. Not クライアント. |
| Entry | https://crowdworks.jp/ — **会員登録** → **Googleで始める** |
| Google | **PREFER_GOOGLE** |
| OTP | メール確認 → **Gmail parent** |
| Draft artifact | プロフィール / 自己PR 下書き. 応募しない. |
| Pack | `{{PASTE_PACK_CROWDWORKS}}` |
| KYC stop | 本人確認、口座、マイナンバー（出金時）. ワーカー登録の途中で出たら停止. |
| Hold | WAF / Press & Hold possible. `holdDurationMs`. |
| Notes | AI CrowdWorks (B15) is a **different** later desk. Do not wander into it from here. |

### A5 — Upwork

| | |
|---|---|
| Role | **Freelancer. Work and get paid.** Not client. |
| Entry | https://www.upwork.com/ — Sign up → Continue with **Google** |
| Help | https://support.upwork.com/hc/en-us/articles/24492534968211-Register-as-a-freelancer |
| Google | **PREFER_GOOGLE**. Help: if you Google-signup, always Google-login later. |
| OTP | Unusual if Google succeeds. Mail → parent. Phone → user chat. |
| Draft artifact | Profile **in progress** / not submitted for special vetting if submit = ID. Catalog/Project drafts from `{{UPWORK_CATALOG_PACK}}` stay **unpublished**. **0 Connects spent.** |
| Pack | `{{PASTE_PACK_UPWORK}}` |
| KYC stop | Photo ID, facial, payment setup, “verify to submit profile” if it is ID. |
| Do not | Buy Connects; boost; send proposals; Agency creation. |
| Language | EN name fields. Do not put kanji in First/Last if the form rejects it. |

### A6 — LinkedIn Services

| | |
|---|---|
| Role | **Services marketplace** on the **existing** LinkedIn for MAIN Google. Not a new LinkedIn. Not **Jobs**. |
| Entry | https://www.linkedin.com/services — open **Provide services** / Service Page draft |
| Google | Same LinkedIn session as `rimone0511`. If signed out, Google that mailbox. **Do not** create a second LinkedIn. |
| OTP | LinkedIn challenge email → **Gmail parent**. SMS → **user chat**. |
| Draft artifact | Service page / offering **saved as draft or not published**. Profile headline may be edited; **no feed post**. |
| Pack | `{{PASTE_PACK_LINKEDIN_SERVICES}}` |
| SNS | **`DRAFT_ONLY`**. No “share to feed”, no newsletter, no connection blast. |
| KYC stop | ID for ads wallet, Premium force-pay, verification badge that demands government ID. |
| Do not | Easy Apply jobs; Recruiter; Sales Nav trial card. |

### A7 — TimeTicket（タイムチケット）

| | |
|---|---|
| Role | ホスト / チケット販売. Not ゲスト-only. |
| Entry | https://www.timeticket.jp/ — **ユーザー登録（無料）** |
| Google | **Often NOT offered** (LINE / Apple / Facebook / email per public app listing). **Use email = MAIN Gmail.** Do not create LINE for this GO unless the user says LINE is already the operator’s and email is impossible. |
| OTP | Email link → **Gmail parent**. |
| Draft artifact | Handle / ユーザーURL / プロフィール. **Ticket saved unpublished** if possible. If ticket **requires** ID before save, **do not create the ticket**. Profile only. |
| Pack | `{{PASTE_PACK_TIMETICKET}}` |
| KYC stop | 本人確認書類（販売・出金・一部カテゴリ・対面）. Public writeups say selling may require ID — **that is a stop**, not a workaround. |
| SNS | LINE 公式連携やシェアはしない (`DRAFT_ONLY`). |
| Notes | Prefer **オンライン** categories aligned with automation consulting. Skip 恋愛/占い. Skip 対面. |

### A8 — Contra

| | |
|---|---|
| Role | Independent / **Share work**. Not Hire. |
| Entry | https://contra.com/ — sign up **Google** |
| Help | https://help.contra.com/en/articles/9322381-onboarding-and-completing-your-profile |
| Google | **PREFER_GOOGLE** |
| OTP | Rare with Google. Else parent Gmail. |
| Draft artifact | Independent profile. Discoverable toggle **off** if present. **No Contra Pro.** No wallet / payout. |
| Pack | `{{PASTE_PACK_CONTRA}}` |
| SNS | Onboarding may ask a social link — paste `{{PORTFOLIO_URL}}` / GitHub. **Do not** post on X/LinkedIn that you joined. |
| KYC stop | Expert verification, government ID, payout method. |

### A9 — Craudia（クラウディア）

| | |
|---|---|
| Role | ワーカー. |
| Entry | https://www.craudia.com/ — 会員登録. FAQ: Google / Yahoo / Facebook / Twitter **or** email. **PREFER_GOOGLE**. |
| FAQ | https://www.craudia.com/app/faq/contents/151 |
| OTP | i2iID / 認証メール → **Gmail parent** (email path). Google path may skip. |
| Draft artifact | プロフィール下書き. 応募しない. |
| Pack | `{{PASTE_PACK_CRAUDIA}}` |
| KYC stop | 本人確認、口座. |
| Notes | Twitter/X bind: **do not** if Google works. SNS draft-only. |

### A10 — Freelancer.com

| | |
|---|---|
| Role | Freelancer, not Employer. |
| Entry | https://www.freelancer.com/ — Sign up **Google** |
| KYC policy (stop text) | https://www.freelancer.com/page.php?p=info%2Fkyc_policy — photo ID, **keycode selfie with ID**, proof of address. **Never do this in CU.** |
| Google | **PREFER_GOOGLE** |
| OTP | Mail/SMS as shown → parent / user chat. |
| Draft artifact | Profile + skills. **No bids.** **No contests.** **No KYC “Verify my Identity”.** |
| Pack | `{{PASTE_PACK_FREELANCER}}` |
| Do not | Preferred Freelancer paid exams; sponsored bids; uploading the keycode photo. |

When A10 is `done-draft` or `kyc_wait` / `sms_wait_user`, **do not start Wave C**. Go to §13 Wave B **passes only**.

---

## 11. Generic field map (when a pack is missing)

Paste only what the live form asks. Skip optional legal/payout.

| Theme | Paste |
|---|---|
| Display name | `{{DISPLAY_NAME}}` |
| Headline EN | `n8n and AI automation with operator docs (official APIs, no scraping)` |
| Headline JA | `AI業務自動化と手順書（公式APIのみ。ブラウザ自動操作なし）` |
| Bio | Pack 200/800 if present; else one-liners + `{{PORTFOLIO_URL}}` + `{{GITHUB_REPO_AUTOPILOT}}` |
| Skills | n8n, workflow automation, API integration, technical writing, Google Workspace, Claude/Codex **operator** docs |
| Rate | empty / 要相談 / Contact — **do not invent** |
| Location | Japan / `{{PREFECTURE}}` only if required |
| Website | `{{PORTFOLIO_URL}}` |
| Phone | only for SMS play §8.2 |
| Photo | `{{PHOTO_LOCAL_PATH}}` if a **portrait**, never an ID |

---

## 12. Stop-light cheat sheet

| You see | You do |
|---|---|
| Continue with Google | Click; pick `rimone0511@gmail.com` |
| Press & Hold / 長押し | `holdDurationMs` §6.3 |
| Email code | Parent Gmail MCP §8.1 |
| SMS code | User chat §8.2 |
| Passport / 免許 / マイナンバー / selfie+ID | Stop. Morning user. |
| Credit card / paid membership | Stop. `card_wall` / `blocked_paid_plan` |
| Publish / 公開する / Share to feed | Do not click. `DRAFT_ONLY` |
| Become a Client / 依頼者 | Back out. Seller path only |
| LinkedIn Easy Apply | Close. Wrong product |
| Toptal / Zapier partner apply | Out of serial (`late`) |
| “Buy Connects” | Close |
| Second Google account | Stop |

---

## 13. Wave B — **passes only**

Do **not** run all of Wave B blindly. After A10:

1. Open `{{WAVE_B_JP_GATE}}` if present, else `{{ACTIVITY_GATE}}`.
2. Open `{{WAVE_B_GLOBAL_GATE}}` if present (`ACTIVITY-GATE-week2-global.md`).
3. Build the **pass list** in **QUEUE Wave B order** (B1→B17), including a desk only when:

| Gate label | This serial |
|---|---|
| `pass` | **Run** (draft, same policies) |
| `needs_check` | **Do not register yet.** 5-minute public-page check per `{{ACTIVITY_GATE}}`. If that check is `pass`, run. If `unknown`, skip to next pass. |
| `blocked_paid_plan` | **Do not subscribe.** Open only to see a free path. If the next click is pay, close. (PeoplePerHour as of 2026-09-15.) |
| `fail-*` / SKIP | Do not open |
| missing gate note | Treat as `needs_check`, not as pass |

**Known global notes (2026-09-15, sibling pack; re-read the file):**

- Guru.com — `pass` (stay free Basic)
- Malt.com — `pass` for EN draft; Google button `needs_check` at click-time
- Workana — draft profile `pass`; jobs list `needs_check` (Cloudflare)
- PeoplePerHour — marketplace alive; seller path `blocked_paid_plan`

**JP Wave B:** prefer sibling `{{WAVE_B_JP_GATE}}`. Until it exists, you may still run B1–B7 **only after** a public-page alive check (HTTP + 売り手登録 visible). `thin_site_skip: false` in JP packs is **not** a publish GO and **not** a KYC GO.

Talent vs company: 複業クラウド / Anycrew / CrowdLinks — **人材側 only**. Close `/client/` and `biz.` hosts.

B15 AI CrowdWorks: **look** whether seller pre-register is open. If closed, `gate`, do not force.

Shufti is Optional Med: only if a pass note exists. Default: skip in this serial.

Wave C / D / LATE partners: **out of this runbook’s serial**. Stop after Wave B passes (or when the session timebox ends).

---

## 14. Session log (secret-free)

If you write a file, use `{{SESSION_LOG_DIR}}/<YYYYMMDD-HHMM>-jst.md`. Otherwise paste the table into the agent summary.

```
date_jst:
cu_agent: earn-cu-serial-20260916
google: MAIN rimone0511 (yes/no)
sns_mode: DRAFT_ONLY
holdDurationMs_used: [e.g. 1800 on Cloudflare @ CrowdWorks]

| desk | pack_path_resolved | auth | otp | kyc | draft | publish | next |
|---|---|---|---|---|---|---|---|
| Fiverr | {{PASTE_PACK_FIVERR}} or missing | google-main | gmail-parent / sms-chat / none | none / wait-morning | yes/no | no | Lancers |
```

Allowed cell values:

- `auth`: `google-main` \| `email-same-mailbox` \| `blocked` \| `already_member`
- `otp`: `gmail-parent` \| `sms-chat` \| `none` \| `otp_missing` \| `sms_wait_user`
- `kyc`: `none` \| `wait-morning` + type (`photo_id`/`my_number`/`selfie`/`address`/`bank`/`card_microcharge`)
- `publish`: always `no` in this GO

Do not attach OTP digits, mail quotes, or ID crops.

QUEUE.md status edits (`next` → `done-draft`) are allowed **without secrets**. Do not fight sibling PRs; prefer session log if QUEUE is locked.

---

## 15. Failures, retries, parking

| Symptom | Retry | Then |
|---|---|---|
| Hold widget ignores short click | 1× with `holdDurationMs: 2500` | `hold_failed` |
| Google picker wrong user | Sign out once | STOP if still wrong |
| OTP not in Gmail at 3 min | Parent search once more | `otp_missing` → user |
| SMS not in chat | One resend | `sms_wait_user`; next desk |
| WAF / 403 | Once, different wait + hold | Park desk |
| Pack missing | Use §11 | Continue |
| Site closed / parking | Do not register | Language for SKIP.md, morning user merges |
| Tool has no `holdDurationMs` | Zero retries | STOP session |

Do not rotate IPs, do not use anti-detect browsers, do not create burner mails. Those are out of policy, not “clever CU”.

---

## 16. Done criteria for **this** serial

The CU serial is **complete** when:

1. A2–A10 each have one of: `done-draft`, `already_member_draft`, `kyc_wait`, `sms_wait_user`, `no_draft_path`, `card_wall`, `sns_block`, `otp_missing` (parked), or `skipped_dead`.
2. **No** desk was published. **No** KYC file left the machine via the agent.
3. Wave B **pass** desks were either drafted the same way or explicitly left for a later session with a reason (`timebox`, `sms_wait_user`).
4. A secret-free log exists.
5. Morning user has a list of `kyc_wait` desks (names + screen types only).

The serial is **not** a success metric on “accounts fully verified” or “gigs live”. Those are later human GOs.

---

## 17. Out of scope (explicit)

- Wave C High remainder (ビザスク, クラウドテック, レバテック, note, BOOTH, Kwork, Codementor, Braintrust)
- Wave C LATE: Zapier / Make / n8n partners, Toptal
- Wave D Med (`needs_activity_check` until a **pass** file exists)
- Mercor / Outlier / DataAnnotation (本人専用)
- Autopilot Log YouTube/TikTok upload
- Sending `{{EN_PROPOSAL_DRAFTS}}` / `{{JP_PROPOSAL_DRAFTS}}`
- Paying PeoplePerHour Basic / TopAccess / Freelancer preferred / Contra Pro / LinkedIn Premium
- Opening Gmail in the CU profile
- Any Press & Hold **without** `holdDurationMs`

---

## 18. Prompt stub (paste into a future CU agent)

```
Follow earn-cu-runbook-20260916/RUNBOOK.md exactly.
Serial: Fiverr → Lancers → CrowdWorks → Upwork → LinkedIn Services →
TimeTicket → Contra → Craudia → Freelancer.com → Wave B activity-gate PASSES only.
MAIN Google: rimone0511@gmail.com. No second accounts.
DRAFT_ONLY for profiles, gigs, tickets, LinkedIn Services, and SNS.
KYC: stop, no uploads, morning user.
Gmail OTP: parent Gmail MCP. Do not open Gmail in the CU browser.
SMS OTP: wait in user chat.
Press & Hold: always set holdDurationMs (start 1800; one retry 2500).
Resolve paste packs from the placeholder table; if missing, use the runbook field map.
Do not publish. Do not invent traffic numbers. Do not spend Connects or paid plans.
```

---

## 19. Changelog

| Date (JST) | Note |
|---|---|
| 2026-09-16 | Initial thick CU serial. Pack paths are placeholders; sibling PRs fill files. Queue order from `earn-register-expand-20260916`. |
