> **MAIN Google only.** 「Google で登録」。Facebook「推奨」は使わない。
> **DRAFT_ONLY.** プロフィール下書き。応募しない。スカウト返信しない。
> **STOP-KYC.** 規約第4条の審査書類は上げない。See [STOP-KYC.md](STOP-KYC.md).
> **No secrets.** OTP とパスワードは git に書かない。
> **No invented fees.** FAQ「すべて無料」（人材）。マージン％は規約に語だけ → `needs_check`。
> **No publish. No signup from this PR.**

# Serial 2 / CU-13 — SOKUDAN（ソクダン）

This card is a **pointer + this-run GET**. Full field map, キャッチ, JA bio 200/800, fee table live in the thick pack — **do not copy them here**.

| キー | 値 |
|---|---|
| this_serial | 2 / 3 |
| cu_serial | CU-13（INDEX。QUEUE B1 順ではない） |
| activity_gate | **pass**（PR#12 トップ案件カード。この GET でも outsourcing `createdAt` 2026-09-15） |
| self_serve | **yes**（公開「無料新規登録」。面談必須と書いていない） |
| cu_ready | **true**（厚いパックあり。登録済みではない） |
| official | https://sokudan.work/ |
| signup | https://sokudan.work/signup/pro |
| login | https://sokudan.work/login |
| terms | https://sokudan.work/pages/terms |
| google_signup_preference | **PREFER_GOOGLE** |
| worker_fee_public | トップ FAQ 人材「すべて無料」。**％未記載 → 作らない** |
| thin_site_skip | **false** |
| stop_at_kyc | **STOP** |
| draft | true |
| observed | 2026-09-16 この PR の公開 GET |

## Pointers (paste from these, do not duplicate secrets)

- **Thick:** [PR#33 `02-sokudan.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-skillshift-sokudan-menta-deep-0734/earn-skillshift-sokudan-menta-deep-20260916/02-sokudan.md)
- Sample: [PR#21 `01-sokudan.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-waveb-alive-handoff-a6eb/earn-waveb-alive-handoff-sample-20260916/01-sokudan.md) — サンプル直列は SOKUDAN 先頭。**このフォルダでは 2 番目**
- Thin: [PR#3 `01-sokudan.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/jp-earn-register-packs-8df7/earn-register-packs-jp-20260916/01-sokudan.md) — 在庫01 ≠ CU-13
- Gate: [PR#12 `records/01-sokudan.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-activity-gate-waveb-jp-fced/earn-activity-gate-waveB-20260916/records/01-sokudan.md)

## needs_check

- 仲介マージン％（規約に「料率」とあるが数字なし）
- ライブフォームの必須ラベル（ログイン壁の向こう）— 画面を正とする

マーケ「リモート案件 92%」は **活動証明に使わない**。自己紹介にコピーしない。

## CU steps（この直列）

1. https://sokudan.work/signup/pro — フリーランス・副業。企業の方は閉じる。
2. `alt="Google で登録"`。Facebook 推奨は無視。
3. 厚いパックの Field map + bio。下書き保存。
4. 応募しない。
5. 審査書類 UI = STOP。
6. Success line → next **Offers**.

フォールバック: 「メールで無料登録」= `{{EMAIL}}`。GitHub は Google の次点（公開リポジトリと一致するなら可）。

規約: 代理人による会員登録は認められない。CU は本人同席前提。この markdown の著者は登録しない。

## This-run GET (cite)

2026-09-16, no login:

- `/signup/pro` HTTP 200, 「無料新規登録」, `href="/users/auth/google?category=signup&usage_type_id=1"`
- `/` HTTP 200, カード alt 例「【フルリモ／週10h〜】TikTok Shop…」。埋め込み JSON に `contractType":"outsourcing"` + `createdAt` **2026-09-15**
- `/pages/terms` HTTP 200, 審査書類の提出を求めることがある、代理人登録不可、手数料％なし
- FAQ 人材「すべて無料でご利用いただけます」

件数は書かない。

## STOP-AT-KYC

ここまでやってよい: Google登録、プロフィール、スキル、公開 URL。下書き保存。

ここで止める: 第4条書類、免許・マイナンバーカード・住民票、口座、本人確認アプリ、応募、発注者申込。

## thin_site_skip

false。この GET で signup/pro 200。Google 登録リンクあり。トップに案件あり。
