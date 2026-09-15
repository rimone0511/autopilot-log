> **MAIN Google only.** Same mailbox as QUEUE. `{{EMAIL}}` / `{{GOOGLE_ACCOUNT_EMAIL}}`. No Facebook / Apple / LINE just for this desk.
> **DRAFT_ONLY.** Profile save only. No エントリー, スカウト返信, 成約報告, 公開トグル.
> **STOP-KYC.** 契約署名・前払い本人確認・口座は上げない。See [STOP-KYC.md](STOP-KYC.md).
> **No secrets.** Passwords, OTP, phone digits, CSRF stay off git.
> **No invented fees.** 前払いの手数料％は画面で確認。このGETでは数字なし → 作らない。
> **No publish. No signup from this PR.**

# Serial 1 / CU-11 — Workship（ワークシップ）

This card is a **pointer + this-run GET**. Full field map and JA bio 200/800 live in the thick pack — **do not copy them here**.

| キー | 値 |
|---|---|
| this_serial | 1 / 3 |
| cu_serial | CU-11（INDEX Week2 先頭 = この直列の先頭） |
| activity_gate | **pass**（PR#12 `/portal/search`。この GET でも 200 + リモ可カード） |
| self_serve | **yes**（公開「フリーランス登録」。面談必須と書いていない） |
| cu_ready | **true**（厚いパックあり。登録済みではない） |
| official | https://goworkship.com/ |
| signup | https://goworkship.com/signup |
| help_signup | https://goworkship.com/help/how_to/44 |
| search | https://goworkship.com/portal/search |
| google_signup_preference | **PREFER_GOOGLE** |
| worker_fee_public | ヘルプは前払いを「手数料・利用規約を確認の上」。**％未記載 → 作らない** |
| thin_site_skip | **false** |
| stop_at_kyc | **STOP** |
| draft | true |
| observed | 2026-09-16 この PR の公開 GET |

## Pointers (paste from these, do not duplicate secrets)

- **Thick:** [PR#30 `01-workship.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-waveb-cu-handoff-batch2-87d0/earn-waveb-cu-handoff-batch2-20260916/01-workship.md) — Field map, JA bio, 自己紹介ヘルプ
- Thin inventory: [PR#3 `02-workship.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/jp-earn-register-packs-8df7/earn-register-packs-jp-20260916/02-workship.md)
- Gate: [PR#12 `records/02-workship.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-activity-gate-waveb-jp-fced/earn-activity-gate-waveB-20260916/records/02-workship.md)
- KYC help rows: [PR#30 STOP-KYC](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-waveb-cu-handoff-batch2-87d0/earn-waveb-cu-handoff-batch2-20260916/STOP-KYC.md)

## needs_check (click-time only)

- 登録面 FirebaseUI は静的 HTML に Google 文字列が無い。**アイコンに Google と書いてあることだけ確認する。** 無ければメール登録に倒す（メールは `{{EMAIL}}`）。
- ワーカー手数料の％は公式ヘルプに数字なし。雑誌の「マージンが発生しない」はマーケコピー。このカードの手数料欄に貼らない。

マーケの件数見出しは **活動証明に使わない**。

## CU steps（この直列）

1. https://goworkship.com/signup 。企業向け `enterprise.goworkship.com` は閉じる。
2. 「SNSで登録」の **Google**。公式ヘルプは「SNSのアイコン」。
3. 厚いパックの Field map どおり。**下書き保存**。
4. エントリーしない。スカウトに返信しない。成約報告しない。
5. Success line → next **SOKUDAN**.

フォールバック: メールで無料登録。確認 URL は24時間（公式ヘルプ）。reCAPTCHA は人が解く。招待コード空。

## This-run GET (cite)

2026-09-16, no login:

- `/signup` HTTP 200, 見出し「SNSで登録」, `#firebaseui-auth-container`
- help/44 HTTP 200, SNS アイコン + URL 有効期限 24時間
- help/agreement/95 HTTP 200, 「本人確認が必要です」（前払い）
- `/portal/search` HTTP 200, リモート可フィルタ + 業務委託カード見出し

CSRF hidden は **記録しない**。

## STOP-AT-KYC

ここまでやってよい: SNS登録、メール確認、プロフィール、職歴、スキル、ポートフォリオ URL。下書き保存。

ここで止める: 契約署名の身分証、前払いオプション、口座、マイナンバー、エントリー。

## thin_site_skip

false。この GET で signup 200。活動ゲート pass。
