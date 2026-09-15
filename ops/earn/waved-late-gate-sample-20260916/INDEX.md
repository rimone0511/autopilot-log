# INDEX — Wave D-late activity-gate sample (interview-heavy)

Stamp: **2026-09-16 JST**  
Folder: `ops/earn/waved-late-gate-sample-20260916/`  
State: **DRAFT_ONLY** / `gate` ≠ registered

Public pages only. Login: **no**. Signup: **no**. Paid plan: **not opened to purchase**. Traffic/GMV: **not invented**.

Desk IDs are Wave D-late sample **D21 / D23 / D24 / D25 / D32**. QUEUE Wave D’s D1–D8 is a different list (PR#1). Sibling D-late D11–D20 is [PR#20](https://github.com/rimone0511/autopilot-log/pull/20) (keep 0; skip-agent there is ココナラテック / Findy Freelance). **This sample does not copy that folder.**

レバテックフリーランス remains Wave **C** (C3) in the parent QUEUE. The D23 ID here is the sample row only.

## Labels

| Label | Use here |
|---|---|
| `profile_only` | Public desk is live **and** the seller path is interview / 担当ヒアリング / 面談 / 商談. Early action = profile draft only. No 面談, no apply, no agent call. **Not** skip-agent. |
| `alive` | Direct catalog / bid desk with a freshness clue. **0 this sample** (these five are interview-heavy). |
| `dead` | Closed URL, 404 on the dedicated desk, or the brand is a different product. Evidence required. **0 this sample.** |
| `thin` | Public listings missing **and** the desk does not match the seller line. Evidence required. **0 this sample.** |
| `needs_check` | Signup or LP is open, but we cannot tell live vs interview-heavy. Do not guess. **0 this sample.** |

`unknown` on a required freshness field does **not** override `profile_only` when the official flow copy already shows 面談 / ヒアリング / 個別説明会.

Marketing totals (登録者○万人, 掲載○件, プロ○名) are **not** activity proof.

## Desks (this sample)

| # | Desk | Note | Opened URL (this GET) | signup_open | Gate | Next |
|---|---|---|---|---|---|---|
| D21 | シューマツワーカー | [notes/d21-shumatsu-worker.md](notes/d21-shumatsu-worker.md) | https://shuuumatu-worker.jp/ | yes (`/signup` 200; Facebook / GitHub / メール. **No Google button**) | **profile_only** | Do not register. Do not 応募. First-time スタッフ面談 + 企業面談 are STOP. MAIN Google path unread. |
| D23 | レバテックフリーランス | [notes/d23-levtech-freelance.md](notes/d23-levtech-freelance.md) | https://freelance.levtech.jp/ | yes (`/member/input/chat/` 200「無料サポート登録」. Form not submitted) | **profile_only** | Parent QUEUE = Wave C (C3). Behind A/B. ヒアリング / 商談 / 個別相談会 are STOP. Do not apply. |
| D24 | ギークスジョブ | [notes/d24-geechs-job.md](notes/d24-geechs-job.md) | https://geechs-job.com/ | yes (`/entry` 200「無料エントリーフォーム」. Not submitted) | **profile_only** | Do not entry. 担当連絡 / 個別説明会 / 独立相談会 / 顧客商談 are STOP. |
| D25 | Midworks | [notes/d25-midworks.md](notes/d25-midworks.md) | https://mid-works.com/ | yes (`/users/registration` 200. Email + reCAPTCHA. Not submitted) | **profile_only** | Do not register. コンサルタント面談 1〜3回 + 参画先商談 are STOP. Not skip-agent. |
| D32 | サーキュレーション | [notes/d32-circulation.md](notes/d32-circulation.md) | https://circu.co.jp/ | yes (talent `https://pro.circu.info/register/basic` 200. Email form. Not submitted) | **profile_only** | Talent portal only. プレ面談 / 企業面談 are STOP. Do not open 法人問い合わせ. PROBASE is a client ops tool — not this desk. |

Not in this INDEX: D22, D26–D31.

## Counts (see STATUS.md)

`profile_only` **5** · keep-as-catalog (`alive`) **0** · skip_log (`dead`) **0** · `needs_check` **0** · `thin` **0** · total **5**

## This PR does not

- Create accounts, complete OAuth, or send MAIN Google
- Upload KYC / bank / tax IDs / 履歴事項全部証明書
- Publish profiles or listings
- Bid / apply / 応募 / エントリー送信 / 面談予約
- Copy sibling paste-pack bodies
- Invent listing counts, GMV, or “○万人”
- Reclassify PR#20 skip-agent rows
