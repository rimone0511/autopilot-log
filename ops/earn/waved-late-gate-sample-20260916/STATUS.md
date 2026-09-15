# STATUS — Wave D-late activity-gate sample (interview-heavy)

Stamp: **2026-09-16 JST** (public GET ~05:41–05:50 JST / 20:41–20:50 UTC 2026-09-15)  
Folder: `ops/earn/waved-late-gate-sample-20260916/`  
State: **DRAFT_ONLY**

Starting operator label: interview-heavy desks, **profile-only early**.  
This file is the **after-GET** box. Signup was not performed. Interviews were not booked.

## Counts

| Bucket | n | Desks |
|---|---|---|
| **profile_only** (interview-heavy; live public pages) | **5** | シューマツワーカー, レバテックフリーランス, ギークスジョブ, Midworks, サーキュレーション |
| keep-as-catalog (`alive`) | **0** | — |
| **skip_log** (`dead`) | **0** | — |
| **needs_check** | **0** | — |
| `thin` | **0** | — |

5 + 0 + 0 + 0 + 0 = **5**.

`thin` / `dead` only where this GET showed it. Interview flow ≠ thin. Public cards without ISO dates ≠ dead.

This is **not** the PR#20 skip-agent bucket. Those two (ココナラテック / Findy Freelance) stay SKIP there. These five stay **profile_only** here.

## profile_only (5)

Still behind Wave A/B. **Not a CU GO from this PR.** Profile draft only if a later serial pass reaches them. 面談 / ヒアリング予約 / 商談 / 応募 → stop. KYC → stop, no upload.

| # | Desk | QUEUE wave | Interview cue (this GET) | Freshness seen this GET | Stop |
|---|---|---|---|---|---|
| D21 | シューマツワーカー | D-ext (not QUEUE D1–D8) | `/projects` flow: プロフィール登録 → 応募 → **初回のみ弊社スタッフとの面談** → **企業と面談**. Home: 登録後ヒアリング | `/projects` **更新日：2026-09-15**. NEW card copy (titles unread as ISO dates) | Do not 応募. Facebook / GitHub / メール signup only — **Google button not on `/signup`**. Individual `/projects/18941` **403** this IP |
| D23 | レバテックフリーランス | C (C3) | Home「ご利用の流れ」: 無料会員登録 → **希望条件をヒアリング** → **案件申込・商談**. `/consultation/detail/2/` **個別相談会** 1時間 | Home copy「2026年3月時点」is a marketing footnote for 掲載数 — unused. `/project/aps-1/` has public skill cards (Tomcat). Card calendar dates unread | Do not submit `/member/input/chat/`. Do not 個別相談会. Do not 商談 |
| D24 | ギークスジョブ | D-ext | `/guide`: エントリー後 **電話もしくはメール** → **個別説明会**（専任キャリア担当）→ 案件紹介 → 顧客**商談**. `/entry`「弊社担当よりご連絡」 | Home News **2026/08/18**. `/news/6` title 2026年8月22日 event. `/project` h3 skill cards (Java / AWS / TypeScript…) — listing ISO dates unread | Do not submit `/entry`. 独立相談会 / 個別説明会 off |
| D25 | Midworks | D-ext | `/about` flow: 登録 → **コンサルタントとの面談（1〜3回）** → **参画先企業様との商談**. `/users/registration` repeats ヒアリング → 商談 | `/projects/` public NEW titles (e.g. Copilot Studio PMO / Vue.js 損害システム). Listing count heading unused | Do not submit register. Do not 面談申込. Login URL unread in static HTML |
| D32 | サーキュレーション | D-ext | `/pro-sharing/` client flow: **プレ面談（スクリーニング）** + プロ人材との面談. Talent `/pro-sharing/professional/`: 追加ヒアリング → **企業との面談打診 / 実施** | Company `/news/` **2026.9.10** (北海道新聞掲載 / 札幌市受託). Talent register is email, not Google | Do not submit `pro.circu.info/register/basic`. Do not 法人問い合わせ. Do not treat PROBASE (`probase.work`) as this desk |

## skip_log / needs_check / thin

None this GET.

Wrong host `shmatsu-worker.jp` / `shu-matsu-worker.jp` **DNS fail** — not evidence of dead. Official host is `shuuumatu-worker.jp`.

## Live CU pointer (not this folder)

This sample does **not** move the Wave A live box. Current serial CU is tracked in sibling STATUS / REGISTER-BOARD PRs. Do not start D-late interview-desk CU while Wave A `pending` / `blocked_skip` rows are open.

レバテック (QUEUE C3) is still **after Wave B**. This PR does not promote it.

## Not done

Account create · OAuth finish · KYC upload · publish · bid · 面談予約 · paid subscribe · secret commit · traffic invention.
