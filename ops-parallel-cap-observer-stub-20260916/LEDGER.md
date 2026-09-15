# 台帳状態（スタブ）

状態: **DRAFT / stub / not a live ledger**  
実ファイル・DB・常駐サービスは作らない。下表は観測メモの語彙。

1 行 = 1 family（`cursor_grok` / `swe2` / `cu`）。合算行を正にしない。

---

## 列

| 列 | 値 | 発明しないこと |
|---|---|---|
| `family` | `cursor_grok` \| `swe2` \| `cu` | 別名の新ファミリー |
| `n_observed` | 非負整数 **または** `UNOBSERVED` | 未観測を `0` にする |
| `n_optimal` | 常に `UNKNOWN` | 数字、~10、1 |
| `n_legacy_hint` | Grok/SWE-2 は `LEGACY_UNVERIFIED~10`。CU は `-` | ヒントを観測値へ写す |
| `ledger_state` | 下の状態語 | 新しい司令塔用の状態機械 |
| `band` | `GREEN` \| `YELLOW` \| `RED` \| `HARD` | 帯を cap 数値に変換 |
| `apply` | 常に `no` | `yes` / `baked` |

---

## 状態語（ledger_state）

| 状態 | 意味 |
|---|---|
| `UNOBSERVED` | この周期に数が無い。0 ではない。帯の既定は YELLOW |
| `OBSERVED` | 名付けた源から数を取った。源の題名だけ残す（秘密なし） |
| `LEGACY_UNVERIFIED` | 数が仮ヒント ~10 由来。観測の代用ではない |
| `MUTEX_CU_1` | CU 枠を 1 つ持っている。合法。GREEN になり得る |
| `MUTEX_VIOLATION` | CU が 1 を超えた、または超えようとした。HARD |
| `DRAIN` | 新規起動を止めるメモ。RED のあと。実際の kill はしない |
| `STUB_ONLY` | このパックはメモ。本番台帳ではない |

同時に持てる組み合わせの例:

- Grok: `OBSERVED` + GREEN（実測が ~10 を超えていない）
- SWE-2: `UNOBSERVED` + YELLOW
- CU: `MUTEX_CU_1` + GREEN、または `UNOBSERVED` + YELLOW、または `MUTEX_VIOLATION` + HARD

`LEGACY_UNVERIFIED` と `OBSERVED` を同一 family で同時に正としない。ヒントは `n_legacy_hint` 列だけ。

---

## 空の初期行（数字を埋めない）

| family | n_observed | n_optimal | n_legacy_hint | ledger_state | band | apply |
|---|---|---|---|---|---|---|
| cursor_grok | UNOBSERVED | UNKNOWN | LEGACY_UNVERIFIED~10 | UNOBSERVED | YELLOW | no |
| swe2 | UNOBSERVED | UNKNOWN | LEGACY_UNVERIFIED~10 | UNOBSERVED | YELLOW | no |
| cu | UNOBSERVED | UNKNOWN | - | UNOBSERVED | YELLOW | no |

この表を「現在 0 稼働」と読まない。初期は未観測。

---

## HARD のとき台帳がすること

- `apply` を `no` のまま固定する
- CU 起動・並列 CU・refill の擬似コード経路を進まない
- 最適 N の欄を数字で上書きしない
- 本人確認が無い自動クリアをしない

---

## やらないこと

- JSON/SQLite の実台帳ファイルをリポジトリへ足す
- Drive ID・座席 Cookie・API トークンをセルへ書く
- 兄弟 APPLY-WINDOW の `{{PRO_NUMBER_*}}` をここへ写して「観測済み」にする
