> **DRAFT_ONLY.** This is a queue, not a GO to start Computer Use.  
> Devin = logged-in computer-use on a live form. Morning KYC is **not** Devin.  
> No signup from a cloud agent. MAIN Google only when a human later authorizes a desk.

# Live Devin still needed (wave5 mirror)

Date: 2026-09-16. Public GET only from this bake. Login-gated and WAF/403 surfaces stay **unproven**.

## Do this first (if a human later GO’s CU serial)

CU mutex = **1 always**. One desk at a time. Stop at KYC. Do not spray.

| Order | Desk | Why Devin is still required | Stop lights | Pack |
|---|---|---|---|---|
| A | CrowdWorks worker editor | `/employee/new` → login. Post-email labels (`ユーザー名`, 氏名, 住所, 職種) are help/blog names, not a filled wizard | 応募, 本人確認, 口座, インボイス | [01](01-cw-fieldmap-verify-notes/) |
| B | Upwork freelancer profile + Catalog **draft** | www.upwork.com + Help **403** here. Skills cap 15 vs 20, category picker, hourly save-block, Catalog image/tag picker: live screen wins | ID / Visual / tax / payout / **Submit** / Connects | [01](01-cw-fieldmap-verify-notes/) + [02](02-upwork-catalog-verify/) |
| C | LinkedIn **personal** Service Page | Help is public; editor is login. Confirm unpublished control. Official help: **Save makes the page viewable** | Company Page, Premium, Jobs, feed Share, Save-if-no-draft | [03](03-linkedin-services/) |
| D | TimeTicket ticket **draft** (メッセージ / async) | Home HTML **202** here; help article 200. Live ticket editor + 非公開 toggle unproven | 発行完了, 対面/電話, ID upload | [04](04-tt-contra-craudia-stop/) |
| E | Contra Independent / Share work (Free) | Help identity article 200; page editor is login. Confirm Free until client | Wallet / Persona / Pro | [04](04-tt-contra-craudia-stop/) |
| F | クラウディア worker **profile** | FAQ 103/93 public 200. Profile widgets login-gated | 応募, スキル出品, マイページ本人確認 + 自撮り | [04](04-tt-contra-craudia-stop/) |
| G | Freelancer.com profile draft | Public home + fees 200. Editor login. **No bids / No contests / No Verify my Identity** | Wallet fund, sponsored bid, Preferred exam | [05](05-freelancer-notes/) |

## Wave B JP — Devin only after activity-gate pass

Sibling gate: **pass** SOKUDAN, Workship, Skill Shift (official domain), ITプロパートナーズ, Offers (Jobs 業務委託).  
**needs_check (8):** 複業クラウド, CrowdLinks, Anycrew, MENTA, ストアカ, AI CrowdWorks, YOUTRUST, Shufti.

This bake re-GET:

| Desk | This bake | Devin? |
|---|---|---|
| SOKUDAN | 200, title マッチングサイト | Profile CU **after** human GO. Not this PR |
| Workship | `/portal/search` 200 | Same |
| Skill Shift | `skill-shift.com` 200 (`skillshift.jp` was DNS-fail in sibling) | Same. Use official domain |
| ITプロパートナーズ | 200 | Same |
| Offers Jobs | `/jobs/engineer/side-job` 200 | Same. Jobs 業務委託, not 転職 LP only |
| MENTA | **202** WAF again | **Devin in a browser that is not WAF-blocked**, or park |
| ストアカ `/teach` | **405** this bake (sibling had a form title) | **Devin** to confirm lecturer form |
| Anycrew app | 200 shell | **Devin** — `/offers` was SPA-empty in sibling |
| YOUTRUST | 200 but landed `/lp` | **Devin** — jobs API was 401 unauthenticated |
| Shufti | 200 → `app.shufti.jp` | **Devin** — search SPA-empty in sibling |
| AI CrowdWorks email register | 200 title `AIクラウドワークス` | **Do not submit.** Public job cards still unread → `needs_check` |
| 複業クラウド / CrowdLinks | not re-opened beyond sibling | Remain `needs_check` |

Catalog-gap four (AI CrowdWorks, Skill Shift, DMM 生成AI人材バンク, Workshift): still **`needs_check`**. Do not CU-register DMM / Workshift from this pack (not in QUEUE). Notes: [05/waveb-catalog-gap](05-freelancer-notes/waveb-catalog-gap/NOTES.md).

## Not Devin

| Goal | Who | Why |
|---|---|---|
| 08 X rubric | Human pastes queries into x.com **Latest** | No X API. No Devin scrape. Rubric is fail-closed. No replies from this pack |
| 09 parallel-cap | Live **observation** of shared Grok×SWE-2 cap | Not a marketplace form. Keep `{{UNKNOWN}}`. CU stays 1. No wait-only Pro workers |
| 10 grok-head placeholders | Pro reply + Yuta “この文面で焼け” | Do not fill `{{PRO_RULE}}`. Effort max = GrokBOT本体, **not** Cursor Grok 4.6 |
| KYC on any desk | Morning operator | Devin records `kyc_shown: yes` and **closes**. No uploads |

## Devin session log (secret-free)

Copy one block per desk. Real OTP / phone / ID never go here.

```
date: 2026-09-16
desk:
pack: earn-swe2-wave5-mirror-bake-20260916
google: MAIN
draft_saved: yes/no/unknown
published: no
kyc_shown: yes/no
upload: none
connects_spent: 0
bids_sent: 0
needs_check_remaining:
next: morning-user | park | next-desk
```
