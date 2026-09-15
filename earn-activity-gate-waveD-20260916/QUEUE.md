# QUEUE-ready — Wave D Fit-Med 活動ゲート

案件: earn-ops Wave D  
観測: 2026-09-16 JST  
枝: `earn-activity-gate-waveD-20260916/`

親キュー: `earn-register-expand-20260916/QUEUE.md`（Wave D は `needs_activity_check` のまま登録禁止）。  
この表はゲート結果の **昇格／SKIP／gate** だけ。Wave A には上げない。合格しても **下書きのみ**。公開しない。

認証: MAIN Google のみ（メール登録なら MAIN Google のメール）。別アカウントを作らない。  
KYC: 免許・パスポート・顔写真・住所証明が出たらアップロードせず停止。朝の本人。

## 状態記号

| 記号 | 意味 | 次の手 |
|---|---|---|
| `week-2` 後 | ゲート合格。A/B と既存 C の後ろ | MAIN Google（またはメール）→ 下書き → 停止 |
| `gate` | 公開一覧が未読 | 人が1画面見てから。推測で登録しない |
| `skip` | やらない | [SKIP.md](SKIP.md) |

---

## 合格 → Wave C 末尾 Med（A/B/C の後ろ・下書きのみ）

順序はプロダクト化／リモート寄せ。パックが無くてもこの順は変えない。

| # | 机 | URL（売り手入口） | 状態 | 認証 | KYC | いまやること |
|---|---|---|---|---|---|---|
| D-P1 | SKIMA | https://skima.jp/entry | `week-2` 後 | MAIN Google（`/account/social/login/google`）。メール可 | 出ていない | 出品は下書き。公開・新着表示（有料）はしない |
| D-P2 | Payhip | ヘルプ https://help.payhip.com/article/164-how-to-sell-your-first-product-on-payhip （トップ https://payhip.com/ はこのIPで Cloudflare 403） | `week-2` 後 | Google 未確認。メール想定 | PayPal/Stripe 接続で身分が出たら停止 | 商品は **Invisible**（または Course の Draft）。Visible にしない |
| D-P3 | Ko-fi | https://ko-fi.com/ | `week-2` 後 | 公開面ではボタン未描画。メール／PayPal 想定 | PayPal/Stripe 接続で停止 | Shop / Commissions は下書き。公開しない。Shop URL はこのIPで CF 403 |
| D-P4 | Dribbble Services | https://dribbble.com/services | `week-2` 後 | サービス面に Google サインイン用スクリプト | 出ていない | **Services 出品のみ**。`/jobs` 求人ボードには逃げない |
| D-P5 | Fastwork | https://fastwork.co/en | `week-2` 後 | 公開HTMLでは Google 未確認 | **雇う前に本人確認**と明記。画面が出たら停止 | AI Automation 等のオンライン出品のみ。マッサージ／家政は触らない |
| D-P6 | Truelancer | https://www.truelancer.com/freelance-jobs | `week-2` 後 | signup はこのIPで Vercel 429。人が入口を辿る | 出ていない | プロフィール下書き。`$5` 複製ギグに合わせない。応募しない |
| D-P7 | Twine | https://www.twine.net/jobs | `week-2` 後 | `/signup` あり。アプリ状態に Google OAuth フラグ | 出ていない | **Twine 直投稿の Remote のみ**。Ari（他社求人の束ね）は使わない |
| D-P8 | ワークシフト | https://workshift-sol.com/registration/mail_start | `week-2` 後 | **メール**（Facebook / LinkedIn / GitHub あり。Google ログインは未確認） | 案件により「本人確認: Yes」。出たら停止 | プロフィール下書き。現地ブース／現地営業カードは応募しない |
| D-P9 | ママワークス | https://mamaworks.jp/entry | `week-2` 後 | 仮登録はメール。Google 未確認 | 出ていない | 応募型。カタログ出品ではない。プロフィール下書き。応募しない |

Wave A の `next` と Wave B の `week-2` が全部 `done-draft` になってから手を付ける。

---

## gate のまま（登録しない）

| # | 机 | 元タグ | 判定 | 次 |
|---|---|---|---|---|
| D1 | シュフティ | `needs_activity_check` | `needs_check` | `/jobs/search` は SPA 空。ヘルプは生きている。カードを見ていないので SKIP thin にしない。JP Wave B と同じ |

---

## SKIP（QUEUE に戻さない）

| # | 机 | 判定 | SKIP節 |
|---|---|---|---|
| D4 | 99designs | `fail-thin` | 薄い机（コンテスト中心。自動化／デジタル配布のカタログではない） |
| D8 | Wellfound | `fail-aggregator` | 寄せ集め専用（スタートアップ求人／採用ボードのみ） |

詳細は [SKIP.md](SKIP.md)。

---

## 元 Wave D 対照（D1–D8）

| 元# | 机 | このゲート |
|---|---|---|
| D1 | シュフティ | `gate` |
| D2 | ママワークス | 合格 → D-P9 |
| D3 | Twine | 合格 → D-P7 |
| D4 | 99designs | SKIP thin |
| D5 | Truelancer | 合格 → D-P6 |
| D6 | Fastwork | 合格 → D-P5 |
| D7 | Dribbble | 合格（Services）→ D-P4 |
| D8 | Wellfound | SKIP aggregator |

D-P1〜P3 と D-P8 は元 Wave D 8机の外。Fit-Med のプロダクト化／リモートで 12 に足した。

---

## やらないこと

- 出品公開、プロフィール公開、コンテスト投稿、パートナー申請の送信
- KYC 書類のアップロード
- 秘密のコミット
- ゲート不合格・未読机の先回り登録
- 案件数・GMV・「稼げる額」の創作
