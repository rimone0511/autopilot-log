# STATUS — Offers（B19）CU handoff desk

> ## REGISTER-CU-CUT
>
> **2026-09-16.** Prefer **JOBS phase** (`register-winddown` / jobs-first).
> **Do not** treat Offers (B19 / CU-25) as next live CU after Freelancer.com (A10 / CU-10).
> After Freelancer parks: stay on JOBS (do-not-send). Do **not** open `/worker/signup` from this folder as the next serial step.
> This folder stays **DRAFT_ONLY**. Archive + paste pointers. **Not a signup GO.** Hint: `register_cu_cut`.

Snapshot: **2026-09-16**（JST folder stamp）  
Folder: `ops/earn/offers-cu-handoff-20260916/`  
State: **DRAFT_ONLY** / **REGISTER-CU-CUT** (not next CU)  
Authoring: 公開 GET / 利用規約のみ。**アカウント作成なし。OAuth 未完走。POST なし。応募なし。**

This file is a desk box for **B19 / QUEUE B14 / CU-25 Offers worker**. It does not claim an Offers account exists. It does not rewrite Wave B serial STATUS in sibling PRs. **Cut overrides play.**

Forbidden: secrets, live phones/passwords/OTP, KYC files, signup from this authoring agent, **apply**, paid booths, invented traffic/GMV/fee %.

---

## CU hint (this desk)

| Hint | Meaning here |
|---|---|
| `pack_ready` | Files exist. **Not** a play GO. Default `register_cu_cut` |
| `pending` | Live CU has **not** marked a draft on this desk from **this** folder |
| `draft_saved` | Worker profile parked unpublished (fill after a real CU run) |
| `blocked_skip` | Skip this pass. Do not retry the listed reason |
| `kyc_wait` | 本人確認画面。朝の本人。アップロードなし |
| `apply_wall` | Save required apply — **do not apply** |
| `register_cu_cut` | Register serial cut. **Not** next live CU. Prefer JOBS phase |

Current row (authoring time):

| # | desk | CU hint | reason | next action |
|---|---|---|---|---|
| B19 / B14 / CU-25 | Offers | `pack_ready` + `register_cu_cut` | Handoff written. Cut overrides play. No live signup / apply | **Do not CU-play.** Prefer JOBS. Keep draft |

Do **not** chain: Freelancer.com → Offers. Prefer JOBS siblings: [PR#68](https://github.com/rimone0511/autopilot-log/pull/68) Freelancer bid DRAFTs (do-not-send), [PR#76](https://github.com/rimone0511/autopilot-log/pull/76) JOBS week on `draft_saved` desks, [PR#88](https://github.com/rimone0511/autopilot-log/pull/88) TODAY apply queue. Freelancer register handoff remains [PR#66](https://github.com/rimone0511/autopilot-log/pull/66). Wave B serial cut: [PR#72](https://github.com/rimone0511/autopilot-log/pull/72).

IDs: **B19 ≠ PPH**（PPH は別ゲートのローカル番号）。QUEUE **B14** = Offers。CU-**25**。Workshift（B09）ではない。

---

## Pack files

| File | What CU does |
|---|---|
| [PLAYBOOK.md](PLAYBOOK.md) | Archive paste order. **Default: do not play.** If register CU is re-opened: MAIN Google → draft → stop |
| [FIELD-MAP.md](FIELD-MAP.md) | JA bio **safe paste**（URL 無し 150/200/255/800 + URL あり 200/800）+ field table |
| [STOP.md](STOP.md) | **No apply.** KYC / 有料 / クライアントも停止 |
| [STATUS.md](STATUS.md) | This box. Fill the success line after a live run |

---

## Public GET (this authoring session)

`thin_site_skip: false`. No login. No POST. Google OAuth 302 はフォローしていない.

| URL | HTTP | Note |
|---|---|---|
| https://offers.jp/ | 200 | タイトル「ハイクラスエンジニア転職」。メタ登録 35,000人は活動証明に使わない |
| https://offers.jp/worker/signup | 200 | `auth-google`。「**Google**で登録する」。`/oauth/worker_signup/google`。メール「メールアドレスで登録する」 |
| https://offers.jp/signup | **404** | 使わない |
| https://offers.jp/worker/login | 200 | 「Googleでログインする」`/oauth/worker_login/google` |
| https://offers.jp/oauth/worker_signup/google | **302** | 開始 URL の確認のみ。Google 同意画面へ入っていない |
| https://offers.jp/jobs/engineer/side-job | 200 | 「副業・業務委託可」。更新日 **2026-09-10**。見出し「【フルリモート】AI×FDE｜…」「【フルリモート／業務委託】AI×新規事業を牽引する…」。CTA「登録して求人に応募する」= STOP |
| https://offers.jp/jobs | 200 | 一覧。応募していない |
| https://offers.jp/terms | 200 | 第3条 業務委託+求職。第11・12条はクライアント負担。％なし |
| https://offers.jp/privacypolicy | 200 | この HTML に「本人確認」なし |
| https://offers.jp/client | 200 | 採用 LP。ワーカーではない |
| https://support-worker.offers.jp/hc/ja | **403** | クライアント LP からのリンク。本文未取得 → needs_check |

Gate context (not re-run as a new verdict): PR#12 `pass` on Jobs 業務委託. This GET still shows 業務委託カードと 2026-09-10 更新日。

---

## After live CU (leave blank until a run)

Fill only the secret-free keys. Do not paste OTP, ID, or a phone.

```
desk: Offers
id: B19
queue: B14
cu: CU-25
pack: ops/earn/offers-cu-handoff-20260916/
auth:
otp:
kyc:
draft_profile:
apply: no
scout_reply: no
publish: no
paid_booth: no
client: no
rate:
next: stop
saved_draft: yes/no/unknown
kyc_shown: yes/no
upload: none
apply_clicked: no
```

Outcome so far: **not_run** / **register_cu_cut**. Default next: JOBS phase, not this desk. Valid later values (only if a human re-opens register CU): `done-draft` | `already_member_draft` | `kyc_wait` | `sms_wait_user` | `no_draft_path` | `otp_missing` | `hold_failed` | `card_wall` | `oauth_overreach` | `rate_empty` | `apply_wall`.

---

## This PR / pack will not

- Create an Offers account from the authoring agent
- Click 「登録して求人に応募する」 or send a scout reply
- Upload ID / selfie / bank / My Number
- Buy a booth or invent fee %
- Open `/client/` as the worker path
- Copy sibling pack bodies into `earn-packs/`
- Play Workship → SOKUDAN → Offers serial as live CU
- Treat Offers as next live CU after Freelancer.com (cut; prefer JOBS)
- Change Python posting-gate tests
