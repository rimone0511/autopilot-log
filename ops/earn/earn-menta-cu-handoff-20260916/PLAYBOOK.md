> DRAFT_ONLY CU handoff. NO secrets. NO invented credentials. NO live signup from this authoring agent.  
> Human / CU paste only. Live form wins.  
> Desk: MENTA（メンター） / **B11** (this-folder local) · QUEUE **B6** · **CU-16**.  
> Auth: **MAIN Google** on public https://menta.work/index.php/register/choose (`Googleアカウントで登録する`).  
> This pass: **profile + unpublished course/plan paste**. **Do not 提出. Do not publish. Do not pay. Do not KYC.**  
> Stop: [STOP.md](STOP.md). Fields: [FIELD-MAP.md](FIELD-MAP.md). Session box: [STATUS.md](STATUS.md).

# PLAYBOOK — MENTA mentor listing (B11)

| Key | Value |
|---|---|
| Desk | MENTA（menta.work） / **mentor**. Not mentee-only. Not Lancers-as-identity |
| IDs | **B11** (Wave B batch2 local) · QUEUE **B6** · **CU-16** |
| Not | QUEUE **B11** = Workana. Local **B06** = Skill Shift (QUEUE B16 / CU-27). **ストアカ** = B12 / QUEUE B7 / CU-17 |
| Shape | **Mentor listing** (プラン). **Not gig escrow**. See §0 |
| Mode | **DRAFT_ONLY** |
| Language | **日本語** |
| Google | **PREFER_GOOGLE** — MAIN only. Public choose page label **Googleアカウントで登録する** (sibling GET). This authoring GET: origin **WAF 202** — confirm the label at click-time |
| Email fallback | Same MAIN mailbox 「メールアドレスで登録する」. OTP = parent Gmail. Do not invent a mailbox |
| Plan / course | **Draft paste only.** 金額 empty. **提出 = 公開審査.** Never press |
| This pass | Account (if needed) → プロフィール / 「できること」 → optional プラン行 with **empty 金額** → status **表示しない** if visible → **stop before 提出** |
| Hard no | **提出** · 公開 · 相談できます（契約可） · 有料プラン購入 · Stripe 本人確認 · 口座 · 出金 · 月契約の有料化 |
| `thin_site_skip` | **false** — WAF challenge is not a dead site. Sibling same-day public GET was 200 on home / `/plan` / `register/choose` / 特商法 |
| Authoring session | Public GET + Intercom Help only. **Did not create an account. Did not POST. Did not complete OAuth** |

Sibling packs (bodies **not** required to open this runner; paste fences live in [FIELD-MAP.md](FIELD-MAP.md)):

| Sibling | Path / PR |
|---|---|
| Thick mentor paste | `earn-skillshift-sokudan-menta-deep-20260916/04-menta.md` ([#33](https://github.com/rimone0511/autopilot-log/pull/33)) |
| Alive sample | `earn-waveb-alive-handoff-sample-20260916/04-menta.md` ([#21](https://github.com/rimone0511/autopilot-log/pull/21)) |
| Thin Week2 | `earn-register-packs-jp-20260916/06-menta.md` ([#3](https://github.com/rimone0511/autopilot-log/pull/3)) |
| Gate (first; WAF unread catalog) | `earn-activity-gate-waveB-20260916/records/06-menta.md` ([#12](https://github.com/rimone0511/autopilot-log/pull/12)) **needs_check** |
| Gate batch2 (catalog **pass**) | `ops/earn/waveb-activity-gate-batch2-20260916/records/b11-menta.md` ([#61](https://github.com/rimone0511/autopilot-log/pull/61)) **pass** |
| QUEUE row B6 | `earn-register-expand-20260916/QUEUE.md` ([#1](https://github.com/rimone0511/autopilot-log/pull/1)) — メンター登録 → プラン下書き。公開しない |
| CU serial INDEX | `earn-register-pack-index-20260916/INDEX.md` ([#8](https://github.com/rimone0511/autopilot-log/pull/8)) CU-16 |
| Alive serial (REGISTER-CU-CUT) | [PR#72](https://github.com/rimone0511/autopilot-log/pull/72) skips MENTA in that Wave B alive list. **This folder is the MENTA runner when the desk is opened** |
| Morning KYC 1枚 | `earn-kyc-morning-checklist-20260916/` ([#4](https://github.com/rimone0511/autopilot-log/pull/4)) |

This playbook is the **step order**. Placeholders stay empty of secrets in git.

---

## 0. Mentor listing vs gig escrow (read first)

MENTA is a **mentor marketplace**. The sellable object is a **メンタープラン** (course / ongoing consult), not a job bid and not an escrowed gig.

| | **MENTA (this desk)** | **Gig escrow** (CrowdWorks / Lancers / Coconala / Fiverr / Freelancer.com) |
|---|---|---|
| What you list | A **mentor plan**: タイトル + できること + プラン名 / 内容 / 金額. 月契約（既定・自動更新） or 単発 | A **service gig** or a **proposal on a buyer job** |
| How money moves | Mentee **contracts the plan**. Platform takes a **commission on that payment**, then payout later | Buyer **escrows** for a deliverable; release on acceptance |
| How you go public | **提出** → ops review (help: 2–3 営業日) → 一般公開. That is **出品** | Publish gig / 提案送信 / 応募 |
| Apply button | Mentees contract **you**. You do **not** 応募 to jobs here | 応募 / 提案 = the usual STOP on those desks |
| This pack | Profile + **unpublished** course paste. **提出しない.** 金額 empty | Do not paste Coconala / Gumroad / Fiverr yen onto a MENTA 金額 |

Official shape ([MENTAとは](https://intercom.help/mentajp/ja/articles/3025296)): 「いつでも相談できるメンターをさがせるサービス」「メンターは月額制で自由に料金とプランをつくる」. Help also documents **単発** as a checkbox on the plan row ([メンターとして登録したい](https://intercom.help/mentajp/ja/articles/3025349)).

Do **not**:

- Treat **提出** as “save draft”. Help: 提出 = 運営確認のあと **一般に公開** ([提出について](https://intercom.help/mentajp/ja/articles/5252569))
- Copy a Coconala / Gumroad SKU price into 金額
- 応募 / 気になる / bid on a MENTA card (wrong product)
- Use homepage 「約7,400名」「8万人」 or help 「7,500名」「平均契約価格帯1.4万円」 as activity proof **or** as a yen to type
- Mix this desk with **ストアカ** (講座公開) or **Lancers アカウントで登録する** (separate identity)

Help calls a live plan **出品中** ([出品中のプランを中止](https://intercom.help/mentajp/ja/articles/3025564)). If it is 出品中, this pack already went too far.

---

## Hard rules (read before the first click)

1. **MAIN Google.** Open [register/choose](https://menta.work/index.php/register/choose). Click **Googleアカウントで登録する**. Use `{{GOOGLE_ACCOUNT_EMAIL}}` — MAIN mailbox only. X / Facebook / Apple / **Lancers** as a new identity: no.
2. **Email is the same person.** If Google is missing, unlabeled, or OAuth fails: **メールアドレスで登録する** with `{{EMAIL}}` = MAIN mailbox. OTP / magic link = **parent Gmail**. Do not paste codes into git.
3. **Mentor side, not mentee-only.** After login, help path is メニュー → **メンター** → **メンタープラン編集**. A mentee-only box is not success. Do not stay a student account and call the desk done.
4. **DRAFT_ONLY.** Paste タイトル / できること / optional プラン内容. Leave **金額 empty**. Prefer status **表示しない**. **Do not 提出.**
5. **提出 is publish.** New mentors: 提出 is required **to start mentoring** and is **無料** ([提出について](https://intercom.help/mentajp/ja/articles/5252569)). Free-to-submit is **not** permission to submit. This pack ends **before** that button.
6. **STOP before paid / KYC.** Do not buy a featured slot. Do not open 設定 → **本人確認ページ** (Stripe). Do not 口座 / 出金. See [STOP.md](STOP.md).
7. **No invented 円 or 手数料％.** Two official commission wordings exist (特商法 20％税別 vs help 22％込). Cite only. Do not invent a third ％. Do not type either ％ into the profile. Do not type a plan price.
8. **WAF is expected.** This authoring GET: `menta.work` returned **HTTP 202** `x-amzn-waf-action: challenge` (AWS WAF JS). A real browser may pass. If it does not: park. Do not POST through a challenge page. Do not copy WAF keys / cookies / `gokuProps` into git.
9. **No credentials in git.** OTP, passwords, Stripe IDs, bank digits, government ID, CSRF, WAF tokens — none of those belong in this repo.

Already a member on MAIN: **ログイン** (same Google). Do not open a second MENTA account. Outcome `already_member_draft`.

---

## WAF (this desk’s special risk)

| Fact | Detail |
|---|---|
| This authoring GET (2026-09-16) | `https://menta.work/` and `/index.php/register/choose`, `/plan`, `/about_mentor`, `/tokutei`, `/index.php/oauth/google` → **202**, `server: awselb/2.0`, header **`x-amzn-waf-action: challenge`**, ~2KB challenge HTML. **No page copy read.** Challenge internals **not saved** |
| Sibling GET same calendar day ([#61](https://github.com/rimone0511/autopilot-log/pull/61)) | Home / `/plan` / `register/choose` / `about_mentor` / `tokutei` **200**. **`/index.php/plan?order=2` (新着 sort) 202 WAF** |
| Earlier gate ([#12](https://github.com/rimone0511/autopilot-log/pull/12)) | `/plan` + register **WAF 202** in that environment; top sometimes 200 |
| Intercom Help this GET | **200** (after 301 slug). Fee / KYC / 提出 / ステータス / 登録手順 were readable |

CU handling:

1. Open the URL in a **real browser**. If a human-verification / press-and-hold / JS challenge appears: wait. Example `holdDurationMs` **1800**, retry **2500**. Then **park** (`waf_challenge` / `hold_failed`).
2. Prefer catalog **without query**: `/plan` or `/index.php/plan`. Do **not** use `/index.php/plan?order=2` as a freshness proof (sibling WAF).
3. Do **not** hammer. Do not change UA in a loop. Do not POST login through the challenge HTML.
4. WAF **does not** mean `thin_site_skip`. It does mean this datacenter GET is **not** a live field dump.
5. Live wizard labels **win** over this pack when the challenge clears.

If register/choose never leaves the challenge: stop. Write STATUS. Do not create a throwaway email to “get around” WAF.

---

## Step order

Live wizard order wins if it differs. Timebox: 15–25 minutes. Stuck > 10 minutes on one modal (including WAF): park and write [STATUS.md](STATUS.md).

Help path after account: ログイン後 → **メンター** → **メンタープラン編集** ([メンターとして登録したい](https://intercom.help/mentajp/ja/articles/3025349)). **This pack ends before step 7 提出.**

### A. Create or open the account

Public choose page (sibling GET 2026-09-16, **not** this WAF GET): https://menta.work/index.php/register/choose — 「メールアドレスで登録する」「**Googleアカウントで登録する**」 plus X / Facebook / Apple / Lancers. OAuth start: https://menta.work/index.php/oauth/google (**do not complete** from authoring).

| # | Do | Do not |
|---|---|---|
| 1 | Open https://menta.work/index.php/register/choose (member: login on the same origin) | Lancers で登録する. ストアカ. Workana (QUEUE B11) |
| 2 | If WAF challenge: wait / hold 1800 / retry 2500 / park | POST through challenge HTML. Copy WAF cookies into git |
| 3 | **Googleアカウントで登録する**. MAIN `{{GOOGLE_ACCOUNT_EMAIL}}` | X / Facebook / Apple / Lancers as a new identity. Guest. Invented Gmail |
| 4 | OAuth consent: basic profile / email. Deny Gmail-read-all / Drive / Contacts dump | Extra scopes “to finish signup” |
| 5 | Fallback: **メールアドレスで登録する**, `{{EMAIL}}` = MAIN, password `{{PASSWORD_DO_NOT_STORE}}` | New mailbox. Password in git |
| 6 | OTP / confirm = **parent Gmail**. Resend at most once | Paste OTP into git / STATUS |
| 7 | Role: continue toward **メンター** / メンタープラン編集. Mentee-only home is not done | Stay 受講者-only and mark success |
| 8 | 招待コード: `{{INVITE_CODE}}` empty unless the ledger has one | Invent an invite |

Agent does **not** tick 利用規約 for the user in the authoring session. Live CU: the **human** reads, then the runner may tick if the human already said GO for this desk.

This authoring agent does **not** follow `/oauth/google` into Google.

### B. Profile + course draft (this pass ends here)

Help labels: [FIELD-MAP.md](FIELD-MAP.md). Paste **石田祐太 / AI自動化**.

| # | Do | Do not |
|---|---|---|
| 1 | ユーザー名 / 表示: `{{DISPLAY_NAME}}` 推奨 **石田祐太**. Live charset wins | Fake 屋号 if the live field is a legal name |
| 2 | **できること** / 自己紹介: paste **200** or **800** from FIELD-MAP | Unverified 受講者数 / 収益 / 「稼げる」 |
| 3 | 経歴・実績: public URLs only (`{{PORTFOLIO_URL}}`, `{{GITHUB_REPO_AUTOPILOT}}`) | Client names under NDA. Invented years |
| 4 | タイトル (listing): FIELD-MAP course **タイトル** fence | A Coconala gig title with a yen |
| 5 | Optional **プラン** row: プラン名 + 内容 from FIELD-MAP. **金額 empty** (`{{PLAN_PRICE_YEN}}`). If 金額 is required to save the row → skip the row (`rate_empty` / `plan_skipped`). Profile-only is still success | Type 10000 / 1.4万 / any sibling SKU. Check **月契約** with a price (auto-renew) |
| 6 | 単発 vs 月契約: prefer **leave default untouched and 金額 empty**. Do not enable a priced 月契約 | “Just put 1000円 to test publish” |
| 7 | ステータス: **表示しない** if the control is there ([ステータス](https://intercom.help/mentajp/ja/articles/3751409)) | **相談できます** (契約が可能な状態) |
| 8 | 契約承認「承認有り」: optional, **not** a substitute for skipping 提出 | Publish with 承認有り “because it is safer” |
| 9 | メインイメージ: `{{PHOTO_LOCAL_PATH}}` optional. Help: 画像なしでも登録可. Not an ID | Passport / license / Stripe selfie |
| 10 | カテゴリ / タグ: nearest **existing** chips. Tags **max 5** (help). Skip unknown | Invent a category. 5+ tags |
| 11 | Save / 更新 if a **non-提出** save exists. Live label wins. If the only button is **提出** → **do not press**. `no_draft_path` | **提出する** / 提出 |

**プラン提出は KYC ではない**が、**提出＝出品審査**。このパックの完了はプロフィール（と未提出の下書き）。プラン提出は本人の別判断。エージェントは出品しない。

### C. Stop (do not continue the official mentor flow)

Do **not**:

- Press **提出** ([提出について](https://intercom.help/mentajp/ja/articles/5252569) — 確認後 **一般に公開**)
- Set ステータス **相談できます**
- Buy anything / 有料ブースト / 運営と一緒に企画 (help CTA on スクールガイド — do not inquire this pass)
- 設定 → **本人確認ページ** (Stripe) ([本人確認](https://intercom.help/mentajp/ja/articles/3025561))
- 口座情報 / 出金申請 ([出金](https://intercom.help/mentajp/ja/articles/3025575) — 本人確認・口座が事前必須)
- Contract a **menteeship** as a student to “test”
- Message random mentors / reply as if selling

Write the success line. Stop. Next desk is **not** automatic (sibling serial said ストアカ; morning jobs-first said JOBS — operator chooses). **REGISTER-CU-CUT:** do not auto-play this desk after Freelancer.com.

---

## Fees (cite only — do not pay, do not type into the form)

Do **not** invent a third percentage to “reconcile” 20％税別 vs 22％込. Do **not** paste these numbers into 自己紹介 or プラン内容. Live 特商法 was **WAF unread** this GET; re-read [https://menta.work/tokutei](https://menta.work/tokutei) in the browser before any later priced GO (not this pass).

| Claim | Status | Source |
|---|---|---|
| メンター手数料 20％税別（利用15％+決済5％）。メンティー側 10％税別。振込都度 300円 | **cited in sibling GET** ([#61](https://github.com/rimone0511/autopilot-log/pull/61) `/tokutei` 200). **This GET: origin WAF 202 — not re-read** | https://menta.work/tokutei · also sibling quotes on `/about_mentor` |
| 手数料22％（手数料20％ + 消費税10％）。例: 10,000円プラン → 手数料 2,200円、報酬 7,800円。出金1回 振込 300円 | **cited this GET** (help 2022-08-31) | https://intercom.help/mentajp/ja/articles/3025582 |
| 旧料率（2022-06-13 以前の月額階段） | **cited, unused** | Same help. Do not use for a new plan |
| メンタープランの**提出は無料** | **cited** | https://intercom.help/mentajp/ja/articles/5252569 「費用もかかりません」— **still do not 提出** |
| 出金: 売上 1,000円超 **かつ** 入金日から30日。事前に本人確認・口座。申請から1～2週間。都度 300円 | **cited (KYC reason, not a GO)** | https://intercom.help/mentajp/ja/articles/3025575 |
| Plan 円 | **placeholder empty** | `{{PLAN_PRICE_YEN}}` only. Empty save, else skip row |

Marketing averages (help 「平均契約価格帯1.4万円」) are **not** a price to type.

---

## Explicit do-not

- Live signup / OAuth completion **from this authoring agent**
- X / Facebook / Apple / Lancers as a new identity
- Second MENTA account
- **提出** / 公開 / 相談できます
- Priced 月契約 (auto-renew) or any typed 金額
- Copying Coconala / Gumroad / Fiverr / ストアカ prices
- Stripe 本人確認 / 口座 / 出金
- Buying boosts or “運営と企画” intake
- Inventing 手数料％ or GMV or 受講者数
- Using WAF challenge keys in git
- Treating QUEUE B11 (Workana) or B06 (Skill Shift) as this desk
- Browser automation / scraper as a MENTA operator bot
- That Autopilot Log posts TikTok unattended (inbox upload is the default; direct post is gated)

---

## Success line (secret-free)

Valid outcomes: `done-draft` | `already_member_draft` | `plan_skipped` | `rate_empty` | `waf_challenge` | `hold_failed` | `kyc_wait` | `submit_stop` | `sms_wait_user` | `no_draft_path` | `otp_missing` | `oauth_overreach` | `google_icon_missing`.

Not success: “提出した,” “公開された,” “相談できます,” “本人確認した,” “口座登録,” “出金申請,” “有料プラン購入.”

```
desk: MENTA
pack: ops/earn/earn-menta-cu-handoff-20260916/
ids: B11 / QUEUE-B6 / CU-16
auth: google-main | email-same-mailbox | already_member | blocked | google_icon_missing | waf_challenge
otp: gmail-parent | none | otp_missing | sms_wait_user
kyc: none | wait-morning + stripe_identity | bank
draft_profile: yes/no
draft_plan: none | saved-unpublished | skipped | rate_empty
submit: no
publish: no
status_control: hidden | busy | consult | unseen
paid_plan: no
bank: no
waf: challenge-passed | parked | unseen
holdDurationMs_used: <e.g. 1800 or none>
next: stop
```

Copy the same keys into [STATUS.md](STATUS.md) after a live run. Do not put OTP digits, passwords, ID numbers, a live phone, a bank amount, or WAF tokens there.

---

## URLs (public; re-open before CU)

| What | URL |
|---|---|
| Home | https://menta.work/ |
| Signup choose (**this pack**) | https://menta.work/index.php/register/choose |
| Google OAuth start (do not complete from authoring) | https://menta.work/index.php/oauth/google |
| Plan catalog (look only; no query) | https://menta.work/plan · https://menta.work/index.php/plan |
| 新着 sort (**skip** — sibling WAF) | https://menta.work/index.php/plan?order=2 |
| Mentor pitch | https://menta.work/about_mentor |
| 特商法 (re-read in browser; this GET WAF) | https://menta.work/tokutei |
| Help: MENTAとは | https://intercom.help/mentajp/ja/articles/3025296 |
| Help: メンターとして登録したい（プラン編集の項目） | https://intercom.help/mentajp/ja/articles/3025349 |
| Help: プラン提出 = 公開審査 **STOP** | https://intercom.help/mentajp/ja/articles/5252569 |
| Help: ステータス（表示しない / 忙しい / 相談できます） | https://intercom.help/mentajp/ja/articles/3751409 |
| Help: 手数料 22％込 | https://intercom.help/mentajp/ja/articles/3025582 |
| Help: Stripe 本人確認 **STOP** | https://intercom.help/mentajp/ja/articles/3025561 |
| Help: 出金 **STOP** | https://intercom.help/mentajp/ja/articles/3025575 |
| Help: 出品中の中止（already too far） | https://intercom.help/mentajp/ja/articles/3025564 |
| Help: スクールプランの作り方（tips only; not a publish GO） | https://intercom.help/mentajp/ja/articles/6591930 |
| Mentor help collection | https://intercom.help/mentajp/ja/collections/1769840 |

Guess only — do not type unless the live page shows them:

```
{{URL_GUESS_MENTA_LOGIN}}
{{URL_GUESS_MENTA_PROFILE}}
{{URL_GUESS_MENTA_PLAN_EDIT}}   # help: メニュー → メンター → メンタープラン編集
{{URL_GUESS_MENTA_SUBMIT}}      # 提出 — 入らない
{{URL_GUESS_MENTA_KYC}}         # 設定 → 本人確認ページ — 開いて種類だけ / 上げない
{{URL_GUESS_MENTA_BANK}}        # 口座 — 開けない
```

---

## 日本語（運用だけ）

下書きのみ。このエージェントは登録しない。入口は https://menta.work/index.php/register/choose 。**MAIN Google**（「Googleアカウントで登録する」）。無ければ同じメール。WAF の challenge が出たら待って、ダメなら park（鍵は git に残さない）。メンター側の **できること / 自己紹介** と、任意の **プラン下書き（金額は空）** まで。**提出は押さない**（公式ヘルプでは提出＝運営確認のあと一般公開＝出品）。ステータスは **表示しない**。本人確認（Stripe）・口座・出金・有料プラン購入はしない。手数料％と円額は捏造しない。ココナラ等のギグ価格を転記しない。
