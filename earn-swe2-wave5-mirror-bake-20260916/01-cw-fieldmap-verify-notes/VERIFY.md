> DRAFT_ONLY. No login. No email-verification POST. Live form after OAuth is **LIVE_DEVIN_NEEDED**.

# Verify notes — CrowdWorks + Upwork field maps

Mirror-bake: 2026-09-16. Sibling livecheck: same calendar date, different host (PR 32).

## CrowdWorks — re-proved this bake

| Claim in fieldmap | This bake | Verdict |
|---|---|---|
| Signup URL `https://crowdworks.jp/user/new_email` | HTTP **200**, title `会員登録【クラウドワークス】` | **Holds** |
| Worker guide `…/pages/guides/employee/index` | HTTP **200**, title `仕事を受注する方法【クラウドワークス】` | **Holds** |
| 利用規約 `…/pages/agreement` | HTTP **200**, title `クラウドワークス利用規約【クラウドワークス】` | **Holds** |
| Step-1 labels (メールアドレスではじめる, Googleではじめる, 利用規約) | Not re-decompressed JS this bake | **Keep sibling JS livecheck.** Devin should still confirm providers on screen |
| `/employee/new` login-gated | Not re-hit (would only bounce to login) | **Still LIVE_DEVIN_NEEDED** for ワーカー情報編集, ひとことアピール, 職種, 自己PR |
| 2012 blog labels (希望時間単価, 稼働可能時間) | Not re-read | Remain **`needs_check`** (old post) |

**Do not submit** `POST /user/send_email_verification`. Prefer Google (`{{GOOGLE_ACCOUNT_EMAIL}}`). Ignore Yahoo / Facebook if shown.

## Upwork — still blocked here

| Claim | This bake | Verdict |
|---|---|---|
| www.upwork.com / `/nx/signup/` / `/catalog` | Sibling **403**; this bake Help + catalog **403** | **Unchanged.** Wizard labels `needs_check` |
| Required 50%: photo, overview, ≥1 employment, ≥1 skill | Help essentials **403** this bake | **Do not invent a new table.** Keep sibling Help copy. Devin confirms editor |
| Skills cap 15 vs 20 | Conflict remains | **`needs_check` — live picker wins** |
| Title 70-char cap; sibling title 47 chars | Not live-checked | Devin counts in the box |
| Hourly `{{HOURLY_USD}}` empty | Still empty in git | If save blocks: park `rate_required`. Do not invent USD |

## LIVE_DEVIN_NEEDED

1. CrowdWorks: after Google, capture **actual** required asterisks on 基本情報 / ユーザー名 / 表示名. Do not set ユーザー名 casually (help: immutable).
2. CrowdWorks: ワーカー情報編集 — confirm ひとことアピール / ウェブ会議 / ステータス still exist.
3. Upwork: signup role = freelancer; Continue with Google; stop if identity Visual starts.
4. Upwork: skills picker cap; category (up to four at create); whether hourly is required to save.

## Still STOP

本人確認, デジタル認証アプリ, 振込先口座, インボイス, Upwork government ID / Visual / tax / payout / 35-Connects badge. See [STOP-KYC.md](STOP-KYC.md).
