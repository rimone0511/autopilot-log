# INDEX — Contra Independent + TimeTicket host deep CU

観測: 2026-09-16（公開 GET。登録なし）  
状態: **DRAFT_ONLY** / `cu_ready` はパックがあること。登録済みではない。

本番の Wave A 直列は兄弟 `earn-cu-runbook-20260916/RUNBOOK.md` と `earn-register-pack-index-20260916/` を正とする。  
**このフォルダの貼る順**は深掘り 2 机だけ。A7 → A8。

| 順 | Pack | INDEX CU | QUEUE | Google | 止める場所 |
|---|---|---|---|---|---|
| 1 | [01-timeticket.md](01-timeticket.md) | CU-07 | A7 | **EMAIL = MAIN Gmail**（OAuth は this env 未確認。Google ボタンが目視できたら PREFER_GOOGLE） | 本人確認アップロード。チケット **発行完了**。電話相談チケット |
| 2 | [02-contra.md](02-contra.md) | CU-08 | A8 | **PREFER_GOOGLE** | Wallet / Persona。**Pro 購入**。Discoverable をオン |

## Fee / rate citation rule（両机）

| ラベル | 意味 |
|---|---|
| **cited** | 公式の公開ページに数字または「無料」が出た。URL と引用をパックに残した |
| **needs_check** | 公式ページに料率・字数が無い、またはこの環境で本文が空（TimeTicket www の HTTP 202）。創作しない。画面カウンター / 現行 pricing を正とする |
| **placeholder** | `{{TICKET_PRICE_JPY}}` / `{{HOURLY_USD}}`。git に実額なし。空で保存できるなら空 |

机ごとの表は各 desk カードと [STOP-KYC.md](STOP-KYC.md) を見よ。

## Bio length rule

| 机 | 公式に出た上限 | このパックのフェンス |
|---|---|---|
| TimeTicket キャッチ | **needs_check**（ヘルプに字数なし） | 23 字の短文。画面で切る |
| TimeTicket 自己紹介 | **needs_check**（ヘルプに字数なし） | **200 / 255 / 800**（測済み）。カウンター超過なら短い方へ |
| Contra one-liner | **needs_check**（ヘルプは「brief」。数字なし） | 63 字と 68 字の 2 本。画面で切る |
| Contra About / bio | **cited 400 characters** | **200** と **400**（測済み）。800 は公式上限を超えるので **置かない** |

## 共通プレースホルダ

実値はローカルの本人台帳だけ。このリポジトリには書かない。README の Shared placeholders と同じ。

公開してよい URL:

- https://yutalab.dev/
- https://github.com/rimone0511
- https://github.com/rimone0511/autopilot-log

## このPRでやらないこと

- アカウント作成
- 本人確認
- 出品完了・応募・公開・Pro 購入
- 秘密・実メール・実電話のコミット
- 案件数・GMV・登録者数の創作
- チケット円額・Contra 時給の創作
