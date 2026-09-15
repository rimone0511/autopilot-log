# 週報 2026-W37 — ハーバー文具（合成）

> SYNTHETIC / 合成データ。販売者の売上・顧客実績・時短・精度の証拠ではない。自主制作サンプル。

## 対象

- 週: `2026-W37`（ISO、Asia/Tokyo）
- 期間: `2026-09-07T00:00:00+09:00` 以上、`2026-09-14T00:00:00+09:00` 未満（半開）
- 入力: `fixtures/inbound-ops-synthetic-w37.csv`
- 入力 SHA-256: `8c9638a9bebb8e8d96c26e08968e303fa0ba78658750cd887aa5c31d614ba96b`
- 生成時刻（固定）: `2026-09-16T12:00:00+09:00`
- エンジン: `src/weekly_report.py`（n8n JSON は inactive の見本。正本はこのスクリプト）

## 要約（各行が入力行へ戻れる）

| 行ID | 指標 | 件数 | 数量 | 合成円 | 根拠（row_id → CSV行） |
|---|---|---:|---:|---:|---|
| L01 | 確定件数（fulfilled） | 14 | 38 | 9600 | [ROW-W37-001](../fixtures/inbound-ops-synthetic-w37.csv#L2), [ROW-W37-002](../fixtures/inbound-ops-synthetic-w37.csv#L3), [ROW-W37-003](../fixtures/inbound-ops-synthetic-w37.csv#L4), [ROW-W37-004](../fixtures/inbound-ops-synthetic-w37.csv#L5), [ROW-W37-005](../fixtures/inbound-ops-synthetic-w37.csv#L6), [ROW-W37-006](../fixtures/inbound-ops-synthetic-w37.csv#L7), [ROW-W37-007](../fixtures/inbound-ops-synthetic-w37.csv#L8), [ROW-W37-008](../fixtures/inbound-ops-synthetic-w37.csv#L9), [ROW-W37-009](../fixtures/inbound-ops-synthetic-w37.csv#L10), [ROW-W37-010](../fixtures/inbound-ops-synthetic-w37.csv#L11), [ROW-W37-011](../fixtures/inbound-ops-synthetic-w37.csv#L12), [ROW-W37-012](../fixtures/inbound-ops-synthetic-w37.csv#L13), [ROW-W37-013](../fixtures/inbound-ops-synthetic-w37.csv#L14), [ROW-W37-027](../fixtures/inbound-ops-synthetic-w37.csv#L30) |
| L02 | 確定数量合計 | 14 | 38 | 9600 | [ROW-W37-001](../fixtures/inbound-ops-synthetic-w37.csv#L2), [ROW-W37-002](../fixtures/inbound-ops-synthetic-w37.csv#L3), [ROW-W37-003](../fixtures/inbound-ops-synthetic-w37.csv#L4), [ROW-W37-004](../fixtures/inbound-ops-synthetic-w37.csv#L5), [ROW-W37-005](../fixtures/inbound-ops-synthetic-w37.csv#L6), [ROW-W37-006](../fixtures/inbound-ops-synthetic-w37.csv#L7), [ROW-W37-007](../fixtures/inbound-ops-synthetic-w37.csv#L8), [ROW-W37-008](../fixtures/inbound-ops-synthetic-w37.csv#L9), [ROW-W37-009](../fixtures/inbound-ops-synthetic-w37.csv#L10), [ROW-W37-010](../fixtures/inbound-ops-synthetic-w37.csv#L11), [ROW-W37-011](../fixtures/inbound-ops-synthetic-w37.csv#L12), [ROW-W37-012](../fixtures/inbound-ops-synthetic-w37.csv#L13), [ROW-W37-013](../fixtures/inbound-ops-synthetic-w37.csv#L14), [ROW-W37-027](../fixtures/inbound-ops-synthetic-w37.csv#L30) |
| L03 | 確定・合成金額(円) | 14 | 38 | 9600 | [ROW-W37-001](../fixtures/inbound-ops-synthetic-w37.csv#L2), [ROW-W37-002](../fixtures/inbound-ops-synthetic-w37.csv#L3), [ROW-W37-003](../fixtures/inbound-ops-synthetic-w37.csv#L4), [ROW-W37-004](../fixtures/inbound-ops-synthetic-w37.csv#L5), [ROW-W37-005](../fixtures/inbound-ops-synthetic-w37.csv#L6), [ROW-W37-006](../fixtures/inbound-ops-synthetic-w37.csv#L7), [ROW-W37-007](../fixtures/inbound-ops-synthetic-w37.csv#L8), [ROW-W37-008](../fixtures/inbound-ops-synthetic-w37.csv#L9), [ROW-W37-009](../fixtures/inbound-ops-synthetic-w37.csv#L10), [ROW-W37-010](../fixtures/inbound-ops-synthetic-w37.csv#L11), [ROW-W37-011](../fixtures/inbound-ops-synthetic-w37.csv#L12), [ROW-W37-012](../fixtures/inbound-ops-synthetic-w37.csv#L13), [ROW-W37-013](../fixtures/inbound-ops-synthetic-w37.csv#L14), [ROW-W37-027](../fixtures/inbound-ops-synthetic-w37.csv#L30) |
| L04 | チャネル 店頭（store） | 6 | 11 | 2840 | [ROW-W37-001](../fixtures/inbound-ops-synthetic-w37.csv#L2), [ROW-W37-003](../fixtures/inbound-ops-synthetic-w37.csv#L4), [ROW-W37-006](../fixtures/inbound-ops-synthetic-w37.csv#L7), [ROW-W37-009](../fixtures/inbound-ops-synthetic-w37.csv#L10), [ROW-W37-012](../fixtures/inbound-ops-synthetic-w37.csv#L13), [ROW-W37-027](../fixtures/inbound-ops-synthetic-w37.csv#L30) |
| L05 | チャネル Web（web） | 5 | 14 | 4080 | [ROW-W37-002](../fixtures/inbound-ops-synthetic-w37.csv#L3), [ROW-W37-005](../fixtures/inbound-ops-synthetic-w37.csv#L6), [ROW-W37-008](../fixtures/inbound-ops-synthetic-w37.csv#L9), [ROW-W37-011](../fixtures/inbound-ops-synthetic-w37.csv#L12), [ROW-W37-013](../fixtures/inbound-ops-synthetic-w37.csv#L14) |
| L06 | チャネル 電話（phone） | 2 | 3 | 880 | [ROW-W37-004](../fixtures/inbound-ops-synthetic-w37.csv#L5), [ROW-W37-010](../fixtures/inbound-ops-synthetic-w37.csv#L11) |
| L07 | チャネル 卸（wholesale） | 1 | 10 | 1800 | [ROW-W37-007](../fixtures/inbound-ops-synthetic-w37.csv#L8) |
| L08 | SKU NB-A5 / A5ノート | 6 | 11 | 5280 | [ROW-W37-001](../fixtures/inbound-ops-synthetic-w37.csv#L2), [ROW-W37-004](../fixtures/inbound-ops-synthetic-w37.csv#L5), [ROW-W37-005](../fixtures/inbound-ops-synthetic-w37.csv#L6), [ROW-W37-009](../fixtures/inbound-ops-synthetic-w37.csv#L10), [ROW-W37-011](../fixtures/inbound-ops-synthetic-w37.csv#L12), [ROW-W37-027](../fixtures/inbound-ops-synthetic-w37.csv#L30) |
| L09 | SKU PEN-BK / 黒ボールペン | 4 | 11 | 1320 | [ROW-W37-002](../fixtures/inbound-ops-synthetic-w37.csv#L3), [ROW-W37-006](../fixtures/inbound-ops-synthetic-w37.csv#L7), [ROW-W37-008](../fixtures/inbound-ops-synthetic-w37.csv#L9), [ROW-W37-012](../fixtures/inbound-ops-synthetic-w37.csv#L13) |
| L10 | SKU CLIP-20 / ダブルクリップ（20個入） | 4 | 16 | 3000 | [ROW-W37-003](../fixtures/inbound-ops-synthetic-w37.csv#L4), [ROW-W37-007](../fixtures/inbound-ops-synthetic-w37.csv#L8), [ROW-W37-010](../fixtures/inbound-ops-synthetic-w37.csv#L11), [ROW-W37-013](../fixtures/inbound-ops-synthetic-w37.csv#L14) |
| L11 | キャンセル件数（確定合計に含めない） | 2 | 3 | 720 | [ROW-W37-015](../fixtures/inbound-ops-synthetic-w37.csv#L16), [ROW-W37-016](../fixtures/inbound-ops-synthetic-w37.csv#L17) |
| L12 | キャンセル・合成金額(円)（確定合計に含めない） | 2 | 3 | 720 | [ROW-W37-015](../fixtures/inbound-ops-synthetic-w37.csv#L16), [ROW-W37-016](../fixtures/inbound-ops-synthetic-w37.csv#L17) |
| L13 | 確認待ち件数（確定合計に含めない） | 2 | 21 | 8200 | [ROW-W37-017](../fixtures/inbound-ops-synthetic-w37.csv#L18), [ROW-W37-018](../fixtures/inbound-ops-synthetic-w37.csv#L19) |
| L14 | 確認待ち・合成金額(円)（確定合計に含めない） | 2 | 21 | 8200 | [ROW-W37-017](../fixtures/inbound-ops-synthetic-w37.csv#L18), [ROW-W37-018](../fixtures/inbound-ops-synthetic-w37.csv#L19) |
| L15 | 除外件数（失敗は成功に混ぜない） | 11 | 17 | 7040 | [ROW-W37-014](../fixtures/inbound-ops-synthetic-w37.csv#L15), [ROW-W37-019](../fixtures/inbound-ops-synthetic-w37.csv#L20), [ROW-W37-020](../fixtures/inbound-ops-synthetic-w37.csv#L21), [ROW-W37-021](../fixtures/inbound-ops-synthetic-w37.csv#L22), [ROW-W37-022](../fixtures/inbound-ops-synthetic-w37.csv#L23), [ROW-W37-023](../fixtures/inbound-ops-synthetic-w37.csv#L24), [ROW-W37-024](../fixtures/inbound-ops-synthetic-w37.csv#L25), [ROW-W37-DUP](../fixtures/inbound-ops-synthetic-w37.csv#L26), [ROW-W37-DUP](../fixtures/inbound-ops-synthetic-w37.csv#L27), [ROW-W37-025](../fixtures/inbound-ops-synthetic-w37.csv#L28), [ROW-W37-026](../fixtures/inbound-ops-synthetic-w37.csv#L29) |

件数・数量・合成円は、根拠列の行だけを足した値である。根拠に無い行は足していない。

## 除外明細（成功件数に混ぜない）

| CSV行 | row_id | 理由 | リンク |
|---:|---|---|---|
| 15 | `ROW-W37-014` | `zero_qty` | [L15](../fixtures/inbound-ops-synthetic-w37.csv#L15) |
| 20 | `ROW-W37-019` | `out_of_week` | [L20](../fixtures/inbound-ops-synthetic-w37.csv#L20) |
| 21 | `ROW-W37-020` | `out_of_week` | [L21](../fixtures/inbound-ops-synthetic-w37.csv#L21) |
| 22 | `ROW-W37-021` | `missing_sku` | [L22](../fixtures/inbound-ops-synthetic-w37.csv#L22) |
| 23 | `ROW-W37-022` | `negative_qty` | [L23](../fixtures/inbound-ops-synthetic-w37.csv#L23) |
| 24 | `ROW-W37-023` | `unknown_channel` | [L24](../fixtures/inbound-ops-synthetic-w37.csv#L24) |
| 25 | `ROW-W37-024` | `unknown_status` | [L25](../fixtures/inbound-ops-synthetic-w37.csv#L25) |
| 26 | `ROW-W37-DUP` | `id_collision` | [L26](../fixtures/inbound-ops-synthetic-w37.csv#L26) |
| 27 | `ROW-W37-DUP` | `id_collision` | [L27](../fixtures/inbound-ops-synthetic-w37.csv#L27) |
| 28 | `ROW-W37-025` | `bad_unit_amount` | [L28](../fixtures/inbound-ops-synthetic-w37.csv#L28) |
| 29 | `ROW-W37-026` | `missing_or_bad_occurred_at` | [L29](../fixtures/inbound-ops-synthetic-w37.csv#L29) |

## 根拠索引（入力の全行）

見出しの `row_id` から、どの要約行に使われたかを辿れる。

### ROW-W37-001 · L2

- CSV: [行 2](../fixtures/inbound-ops-synthetic-w37.csv#L2)
- occurred_at: `2026-09-07T09:12:00+09:00`
- channel: `store` / sku: `NB-A5` / status: `fulfilled`
- qty: `2` / unit_amount_jpy: `480`
- 分類: `fulfilled`
- 載っている要約行: L01, L02, L03, L04, L08
- note: 合成・店頭

### ROW-W37-002 · L3

- CSV: [行 3](../fixtures/inbound-ops-synthetic-w37.csv#L3)
- occurred_at: `2026-09-07T11:40:00+09:00`
- channel: `web` / sku: `PEN-BK` / status: `fulfilled`
- qty: `3` / unit_amount_jpy: `120`
- 分類: `fulfilled`
- 載っている要約行: L01, L02, L03, L05, L09
- note: 合成・Web

### ROW-W37-003 · L4

- CSV: [行 4](../fixtures/inbound-ops-synthetic-w37.csv#L4)
- occurred_at: `2026-09-07T14:05:00+09:00`
- channel: `store` / sku: `CLIP-20` / status: `fulfilled`
- qty: `1` / unit_amount_jpy: `200`
- 分類: `fulfilled`
- 載っている要約行: L01, L02, L03, L04, L10
- note: 合成・店頭

### ROW-W37-004 · L5

- CSV: [行 5](../fixtures/inbound-ops-synthetic-w37.csv#L5)
- occurred_at: `2026-09-08T10:22:00+09:00`
- channel: `phone` / sku: `NB-A5` / status: `fulfilled`
- qty: `1` / unit_amount_jpy: `480`
- 分類: `fulfilled`
- 載っている要約行: L01, L02, L03, L06, L08
- note: 合成・電話

### ROW-W37-005 · L6

- CSV: [行 6](../fixtures/inbound-ops-synthetic-w37.csv#L6)
- occurred_at: `2026-09-08T16:10:00+09:00`
- channel: `web` / sku: `NB-A5` / status: `fulfilled`
- qty: `4` / unit_amount_jpy: `480`
- 分類: `fulfilled`
- 載っている要約行: L01, L02, L03, L05, L08
- note: 合成・Web

### ROW-W37-006 · L7

- CSV: [行 7](../fixtures/inbound-ops-synthetic-w37.csv#L7)
- occurred_at: `2026-09-09T09:00:00+09:00`
- channel: `store` / sku: `PEN-BK` / status: `fulfilled`
- qty: `5` / unit_amount_jpy: `120`
- 分類: `fulfilled`
- 載っている要約行: L01, L02, L03, L04, L09
- note: 合成・店頭

### ROW-W37-007 · L8

- CSV: [行 8](../fixtures/inbound-ops-synthetic-w37.csv#L8)
- occurred_at: `2026-09-09T13:33:00+09:00`
- channel: `wholesale` / sku: `CLIP-20` / status: `fulfilled`
- qty: `10` / unit_amount_jpy: `180`
- 分類: `fulfilled`
- 載っている要約行: L01, L02, L03, L07, L10
- note: 合成・卸単価

### ROW-W37-008 · L9

- CSV: [行 9](../fixtures/inbound-ops-synthetic-w37.csv#L9)
- occurred_at: `2026-09-10T08:50:00+09:00`
- channel: `web` / sku: `PEN-BK` / status: `fulfilled`
- qty: `2` / unit_amount_jpy: `120`
- 分類: `fulfilled`
- 載っている要約行: L01, L02, L03, L05, L09
- note: 合成・Web

### ROW-W37-009 · L10

- CSV: [行 10](../fixtures/inbound-ops-synthetic-w37.csv#L10)
- occurred_at: `2026-09-10T12:15:00+09:00`
- channel: `store` / sku: `NB-A5` / status: `fulfilled`
- qty: `1` / unit_amount_jpy: `480`
- 分類: `fulfilled`
- 載っている要約行: L01, L02, L03, L04, L08
- note: 合成・店頭

### ROW-W37-010 · L11

- CSV: [行 11](../fixtures/inbound-ops-synthetic-w37.csv#L11)
- occurred_at: `2026-09-11T15:40:00+09:00`
- channel: `phone` / sku: `CLIP-20` / status: `fulfilled`
- qty: `2` / unit_amount_jpy: `200`
- 分類: `fulfilled`
- 載っている要約行: L01, L02, L03, L06, L10
- note: 合成・電話

### ROW-W37-011 · L12

- CSV: [行 12](../fixtures/inbound-ops-synthetic-w37.csv#L12)
- occurred_at: `2026-09-12T10:05:00+09:00`
- channel: `web` / sku: `NB-A5` / status: `fulfilled`
- qty: `2` / unit_amount_jpy: `480`
- 分類: `fulfilled`
- 載っている要約行: L01, L02, L03, L05, L08
- note: 合成・Web

### ROW-W37-012 · L13

- CSV: [行 13](../fixtures/inbound-ops-synthetic-w37.csv#L13)
- occurred_at: `2026-09-13T17:20:00+09:00`
- channel: `store` / sku: `PEN-BK` / status: `fulfilled`
- qty: `1` / unit_amount_jpy: `120`
- 分類: `fulfilled`
- 載っている要約行: L01, L02, L03, L04, L09
- note: 合成・店頭

### ROW-W37-013 · L14

- CSV: [行 14](../fixtures/inbound-ops-synthetic-w37.csv#L14)
- occurred_at: `2026-09-13T18:00:00+09:00`
- channel: `web` / sku: `CLIP-20` / status: `fulfilled`
- qty: `3` / unit_amount_jpy: `200`
- 分類: `fulfilled`
- 載っている要約行: L01, L02, L03, L05, L10
- note: 合成・Web

### ROW-W37-014 · L15

- CSV: [行 15](../fixtures/inbound-ops-synthetic-w37.csv#L15)
- occurred_at: `2026-09-08T11:00:00+09:00`
- channel: `store` / sku: `NB-A5` / status: `fulfilled`
- qty: `0` / unit_amount_jpy: `480`
- 分類: `exception` / 理由: `zero_qty`
- 載っている要約行: L15
- note: 合成・数量0

### ROW-W37-015 · L16

- CSV: [行 16](../fixtures/inbound-ops-synthetic-w37.csv#L16)
- occurred_at: `2026-09-08T19:00:00+09:00`
- channel: `web` / sku: `NB-A5` / status: `cancelled`
- qty: `1` / unit_amount_jpy: `480`
- 分類: `cancelled`
- 載っている要約行: L11, L12
- note: 合成・キャンセル

### ROW-W37-016 · L17

- CSV: [行 17](../fixtures/inbound-ops-synthetic-w37.csv#L17)
- occurred_at: `2026-09-11T09:30:00+09:00`
- channel: `phone` / sku: `PEN-BK` / status: `cancelled`
- qty: `2` / unit_amount_jpy: `120`
- 分類: `cancelled`
- 載っている要約行: L11, L12
- note: 合成・キャンセル

### ROW-W37-017 · L18

- CSV: [行 18](../fixtures/inbound-ops-synthetic-w37.csv#L18)
- occurred_at: `2026-09-09T18:45:00+09:00`
- channel: `wholesale` / sku: `NB-A5` / status: `hold`
- qty: `20` / unit_amount_jpy: `400`
- 分類: `hold`
- 載っている要約行: L13, L14
- note: 合成・確認待ち

### ROW-W37-018 · L19

- CSV: [行 19](../fixtures/inbound-ops-synthetic-w37.csv#L19)
- occurred_at: `2026-09-12T14:10:00+09:00`
- channel: `store` / sku: `CLIP-20` / status: `hold`
- qty: `1` / unit_amount_jpy: `200`
- 分類: `hold`
- 載っている要約行: L13, L14
- note: 合成・確認待ち

### ROW-W37-019 · L20

- CSV: [行 20](../fixtures/inbound-ops-synthetic-w37.csv#L20)
- occurred_at: `2026-09-06T16:00:00+09:00`
- channel: `store` / sku: `PEN-BK` / status: `fulfilled`
- qty: `1` / unit_amount_jpy: `120`
- 分類: `exception` / 理由: `out_of_week`
- 載っている要約行: L15
- note: 合成・週前

### ROW-W37-020 · L21

- CSV: [行 21](../fixtures/inbound-ops-synthetic-w37.csv#L21)
- occurred_at: `2026-09-14T09:10:00+09:00`
- channel: `web` / sku: `NB-A5` / status: `fulfilled`
- qty: `1` / unit_amount_jpy: `480`
- 分類: `exception` / 理由: `out_of_week`
- 載っている要約行: L15
- note: 合成・週後

### ROW-W37-021 · L22

- CSV: [行 22](../fixtures/inbound-ops-synthetic-w37.csv#L22)
- occurred_at: `2026-09-10T11:00:00+09:00`
- channel: `store` / sku: `` / status: `fulfilled`
- qty: `1` / unit_amount_jpy: `480`
- 分類: `exception` / 理由: `missing_sku`
- 載っている要約行: L15
- note: 合成・SKU欠落

### ROW-W37-022 · L23

- CSV: [行 23](../fixtures/inbound-ops-synthetic-w37.csv#L23)
- occurred_at: `2026-09-10T11:05:00+09:00`
- channel: `store` / sku: `NB-A5` / status: `fulfilled`
- qty: `-1` / unit_amount_jpy: `480`
- 分類: `exception` / 理由: `negative_qty`
- 載っている要約行: L15
- note: 合成・負数

### ROW-W37-023 · L24

- CSV: [行 24](../fixtures/inbound-ops-synthetic-w37.csv#L24)
- occurred_at: `2026-09-10T11:10:00+09:00`
- channel: `mystery` / sku: `NB-A5` / status: `fulfilled`
- qty: `1` / unit_amount_jpy: `480`
- 分類: `exception` / 理由: `unknown_channel`
- 載っている要約行: L15
- note: 合成・不明チャネル

### ROW-W37-024 · L25

- CSV: [行 25](../fixtures/inbound-ops-synthetic-w37.csv#L25)
- occurred_at: `2026-09-10T11:15:00+09:00`
- channel: `store` / sku: `NB-A5` / status: `exploded`
- qty: `1` / unit_amount_jpy: `480`
- 分類: `exception` / 理由: `unknown_status`
- 載っている要約行: L15
- note: 合成・不明ステータス

### ROW-W37-DUP · L26

- CSV: [行 26](../fixtures/inbound-ops-synthetic-w37.csv#L26)
- occurred_at: `2026-09-10T12:00:00+09:00`
- channel: `store` / sku: `NB-A5` / status: `fulfilled`
- qty: `9` / unit_amount_jpy: `480`
- 分類: `exception` / 理由: `id_collision`
- 載っている要約行: L15
- note: 合成・ID衝突A

### ROW-W37-DUP · L27

- CSV: [行 27](../fixtures/inbound-ops-synthetic-w37.csv#L27)
- occurred_at: `2026-09-10T12:01:00+09:00`
- channel: `store` / sku: `NB-A5` / status: `fulfilled`
- qty: `1` / unit_amount_jpy: `480`
- 分類: `exception` / 理由: `id_collision`
- 載っている要約行: L15
- note: 合成・ID衝突B

### ROW-W37-025 · L28

- CSV: [行 28](../fixtures/inbound-ops-synthetic-w37.csv#L28)
- occurred_at: `2026-09-09T10:00:00+09:00`
- channel: `web` / sku: `PEN-BK` / status: `fulfilled`
- qty: `2` / unit_amount_jpy: `abc`
- 分類: `exception` / 理由: `bad_unit_amount`
- 載っている要約行: L15
- note: 合成・金額不正

### ROW-W37-026 · L29

- CSV: [行 29](../fixtures/inbound-ops-synthetic-w37.csv#L29)
- occurred_at: `(empty)`
- channel: `store` / sku: `CLIP-20` / status: `fulfilled`
- qty: `1` / unit_amount_jpy: `200`
- 分類: `exception` / 理由: `missing_or_bad_occurred_at`
- 載っている要約行: L15
- note: 合成・日時欠落

### ROW-W37-027 · L30

- CSV: [行 30](../fixtures/inbound-ops-synthetic-w37.csv#L30)
- occurred_at: `2026-09-11T10:00:00+09:00`
- channel: `store` / sku: `NB-A5` / status: `fulfilled`
- qty: `1` / unit_amount_jpy: `480`
- 分類: `fulfilled`
- 載っている要約行: L01, L02, L03, L04, L08
- note: 合成・店頭

## このファイルが主張しないこと

- 販売者（石田祐太 / yutalab）の実売上、実顧客、時短率、精度
- n8n Partner / Expert などのバッジ
- 本番シート・本番メール・公開済み運用

再現手順は `README.md`。完了条件は `DOD.md`。言ってよい事実だけ `FACTS.md`。
