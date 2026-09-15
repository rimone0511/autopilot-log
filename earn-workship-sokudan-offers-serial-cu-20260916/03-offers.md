> **MAIN Google only.** Use 「Googleで登録する」 (`/oauth/worker_signup/google`). GitHub は任意のあと。X / LinkedIn を新規に作らない。
> **DRAFT_ONLY.** ワーカープロフィール下書き。求人に応募しない。スカウト返信しない。
> **STOP-KYC.** 面談・契約・出金の本人確認は上げない。See [STOP-KYC.md](STOP-KYC.md).
> **No secrets.** OTP とパスワードは git に書かない。
> **No invented fees.** 規約: マッチング成功報酬は **クライアントが** 払う。ユーザー側の％はこの GET では未記載 → 作らない。LP の「35,000人」は活動証明に使わない。
> **No publish. No signup from this PR.** Jobs の「登録して求人に応募する」は押さない。

# Serial 3 / CU-25 — Offers

This card is a **pointer + this-run GET**. Full field map and JA bio 200/800 live in the thick pack — **do not copy them here**.

| キー | 値 |
|---|---|
| this_serial | 3 / 3（このフォルダの最後） |
| cu_serial | CU-25（INDEX B14。QUEUE 順ではない） |
| activity_gate | **pass**（PR#12 Jobs 業務委託カード。この GET でも更新日 **2026-09-10**） |
| self_serve | **yes**（`/worker/signup` が開いている。トップは転職コピーが強いが Jobs は業務委託が残る） |
| cu_ready | **true**（厚いパックあり。登録済みではない） |
| official | https://offers.jp/ |
| worker_signup | https://offers.jp/worker/signup |
| jobs_side | https://offers.jp/jobs/engineer/side-job |
| terms | https://offers.jp/terms |
| google_signup_preference | **PREFER_GOOGLE** |
| worker_fee_public | [利用規約](https://offers.jp/terms) 成功報酬はクライアント負担。**％未記載 → 作らない**。有料ブースは買わない |
| thin_site_skip | **false** |
| stop_at_kyc | **STOP** |
| draft | true |
| observed | 2026-09-16 この PR の公開 GET |

## Pointers (paste from these, do not duplicate secrets)

- **Thick:** [PR#30 `04-offers.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-waveb-cu-handoff-batch2-87d0/earn-waveb-cu-handoff-batch2-20260916/04-offers.md)
- Week2-rest: [PR#34 `03-offers.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-week2-rest-cu-paste-e6ce/earn-week2-rest-cu-paste-20260916/03-offers.md)
- Gate: [PR#12 `records/12-offers.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-activity-gate-waveb-jp-fced/earn-activity-gate-waveB-20260916/records/12-offers.md)

PR#30 五机フォルダの貼る順では Offers は 3 番（pass 先行で ITプロパートナーズの次）。**この直列では SOKUDAN の次 = 最後。** ITプロパートナーズは入れない。

## needs_check

- ユーザーが払うマージン％は公式規約に数字なし。第三者記事の「ワーカー無料・マージンなし」を手数料欄に固定しない。
- 案件カードの時給レンジは **その求人の提示**。プロフィール希望単価にコピーしない。

QUEUE の「転職導線だけなら再判定」は、Jobs の業務委託を見て **pass**（PR#12）。応募はしない。

## CU steps（この直列）

1. ワーカー https://offers.jp/worker/signup （`/signup` は **404**）。
2. **Google で登録する**。企業 `/client/` は閉じる。
3. 厚いパックの Field map + bio。GitHub 連携は任意（公開リポジトリと一致するなら可）。**下書き**。
4. 業務委託意欲は画面値の最寄り。転職意欲を盛らない。Jobs を見ても **応募しない**。
5. Success line → **stop** (end of this serial).

フォールバック: 「メールアドレスで登録する」。メールは `{{EMAIL}}`。

使わない: 新規 X アカウント。有料ブース。年収診断の送信が必須なら空で進むか park。

## This-run GET (cite)

2026-09-16, no login:

- `/worker/signup` HTTP 200, `data-testid="auth-google"`, ラベル「**Google**で登録する」, `/oauth/worker_signup/google`
- `/jobs/engineer/side-job` HTTP 200, 「副業・業務委託可」, カード「【フルリモート】AI×FDE｜…」, 更新日文字列 **2026-09-10**
- `/terms` HTTP 200, 第12条 クライアントが成功報酬を払う。％なし。業務委託と求職の両方
- `/signup` HTTP **404**
- トップ HTTP 200, 転職コピー + `/worker/signup` リンク。メタ「35,000人」は活動証明に使わない

公開 HTML のスキル `workerCount` はカタログであり GMV ではない。書かない。

## STOP-AT-KYC

ここまでやってよい: Google登録、プロフィール、スキル、公開 URL。下書き保存。

ここで止める: 求人応募、ヘッドハント面談の日程確定、本人確認書類、口座・出金、有料ブース。

## thin_site_skip

false。この GET で `/worker/signup` 200。「Googleで登録する」可視。Jobs 業務委託カードに 2026-09-10 の更新日。
