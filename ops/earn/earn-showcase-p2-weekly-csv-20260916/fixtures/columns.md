# 入力CSVの列（合成）

対象ファイル: `inbound-ops-synthetic-w37.csv`

すべて架空の文具店オペレーションである。実在の注文・顧客・売上ではない。

| 列 | 必須 | 説明 |
|---|---|---|
| `row_id` | はい | 行の安定ID。ファイル内で重複したら **両方とも除外**（`id_collision`） |
| `occurred_at` | はい | ISO 8601。タイムゾーン付きを推奨。週の半開区間 `[start, end)` の外は除外 |
| `channel` | はい | 許可: `store` / `web` / `phone` / `wholesale` |
| `sku` | はい | 許可: `NB-A5` / `PEN-BK` / `CLIP-20` |
| `qty` | はい | 整数。`0` と負数は除外 |
| `unit_amount_jpy` | はい | 整数円。行金額 = qty × unit_amount_jpy |
| `status` | はい | `fulfilled`（確定） / `cancelled` / `hold`。それ以外は除外 |
| `note` | いいえ | 人間向けメモ。集計には使わない |

除外理由のコードは週報の除外明細と `*-exceptions.csv` に出る。
