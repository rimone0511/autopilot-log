# APPLY-WINDOW（下書き）並列キャップ — 適応設計

状態: **DRAFT / not production-applied / PARALLEL-CAP-PERF recovered**  
ロック日の目印: 2026-09-16 HANDS。数字の正は回収した Pro `PARALLEL-CAP-PERF`。

APPLY-WINDOW とは「次に本番へ焼くときの並列キャップの正」であり、この PR では窓へ書いただけ。実行・配備・Bot 設定変更は含まない。

**固定の 10/10 を max として焼かない。** 最適数はライブ観測まで `{{UNKNOWN}}`。

---

## 0. 回収後の状態

| 項目 | 状態 |
|---|---|
| Pro 案件 **PARALLEL-CAP-PERF** | **回収済み**（HANDS 2026-09-16）。全文は貼らない |
| 旧ソフト暫定 GO ~10/~10 | `{{LEGACY_UNVERIFIED}}` — 移行境界のみ。証明済み maxima ではない |
| 最適並行数 | `{{UNKNOWN}}` — ライブ観測が着くまで不明 |
| 増減 | `{{ADAPTIVE}}` — GREEN / YELLOW / RED / HARD |
| CU | **1 always**（兄弟 ORCH mutex=1 と一致。上げない） |
| 本番適用 | していない |

`{{PRO_NUMBER_*}}` は使わない。残っていたら未完。

---

## 1. 窓の APPLY 値

| つまみ | APPLY 値 | Pro が言ったこと | 焼かないこと |
|---|---|---|---|
| **shared cap**（Grok と SWE-2 を横断） | `{{UNKNOWN}}` | 共有のクロスモデル・キャップ。最適数はライブ観測まで UNKNOWN | モデル別に 10 と 10 を独立 max にする |
| **max Cursor Grok** | `{{UNKNOWN}}`（shared に従う） | 単独の証明済み上限はない | `{{LEGACY_UNVERIFIED}}` の ~10 を Grok max にする |
| **max SWE-2** | `{{UNKNOWN}}`（shared に従う） | 単独の証明済み上限はない | `{{LEGACY_UNVERIFIED}}` の ~10 を SWE-2 max にする |
| **legacy 境界** | `{{LEGACY_UNVERIFIED}}` | ~10/~10 は移行境界のみ。証明済み maxima ではない | 現行の認可上限、観測済み Effort |
| **CU** | **1** | always。並列 CU を焼かない | `{{ADAPTIVE}}` の +1 を CU に掛ける |
| **refill-on-empty** | `{{ADAPTIVE}}` | 固定補充数ではない。空席は reconcile 1 本。GREEN のときだけ trial +1 を**試してよい** | 空席を ~10 まで埋める。待ち専用 Pro を足す |
| **増減コントローラ** | `{{ADAPTIVE}}` | §3 の GREEN / YELLOW / RED / HARD | 固定ステップ幅の発明（RED の下げ幅など） |

トークン:

- `{{LEGACY_UNVERIFIED}}` — 旧 ~10/~10 の移行境界。max ではない
- `{{UNKNOWN}}` — 最適並行数。ライブ観測まで不明
- `{{ADAPTIVE}}` — レーンと refill。固定人数ではない

---

## 2. `{{LEGACY_UNVERIFIED}}`（~10/~10）

旧ソフト暫定 GO の **Cursor Grok ~10 / SWE-2 ~10** は、Pro により:

- 移行境界（migration boundary）だけ
- **証明済み maxima ではない**
- この窓の APPLY max 列へ写さない
- G1 の「15 並行の証明」の代用でもない

移行時にその近傍の運用が見えても、検証済み上限としては扱わない。`{{UNKNOWN}}` のまま観測する。

---

## 3. `{{ADAPTIVE}}` レーン

Pro の条件だけ書く。計測コマンド・実装名は足さない。

| レーン | 条件（原文の範囲） | してよいこと | CU |
|---|---|---|---|
| **GREEN** | time ratio **<= 1.10** かつ quality pass かつ RL / stall / resource / acceptance の劣化なし | shared cap を **trial +1** してよい（必須ではない） | 1 のまま。+1 しない |
| **YELLOW** | （GREEN を満たさない成長停止側。Pro: stop growth） | **成長を止める**。trial +1 しない | 1 のまま |
| **RED** | （影響資源が劣化したとき。Pro: lower affected resource cap） | **影響している資源のキャップを下げる**。下げ幅は文面に無いので発明しない | 1 のまま（CU を 0 にする指示はこの文面に無い） |
| **HARD** | （閉じる側。Pro: close affected op） | **影響している op を閉じる** | 1 のまま。CU 自体を増やす指示は無い |

GREEN の time ratio 1.10 はレーン条件であり、並行数の max ではない。

ライブ観測が無い間、最適数は `{{UNKNOWN}}`。未観測を 0 にも 10 にもしない。

---

## 4. 共有キャップと reconcile

Pro:

- **shared cross-model caps** — Grok 枠と SWE-2 枠を別々の確定 max に割らない
- **one reconcile function** — desired と actual の突合は関数 1 本。第二の並行台帳を足さない
- **no wait-only Pro workers** — 席を埋めるためだけの待ち専用 Pro を立てない
- **no duplicate fake parallelism** — 待ち・遊休・重複起動を「並行している」と数えない

reconcile の関数名、ファイルパス、キュー長はこの下書きでは増やさない。要件だけ残す。

振り分け順（SWE-2 第一候補、Grok は難所）は兄弟 ORCH の正。この窓は**数とレーン**だけ。

---

## 5. refill-on-empty = `{{ADAPTIVE}}`

固定の「空席 1 につき N」は Pro に無い。空席時:

1. 共有キャップを **one reconcile function** で合わせる
2. wait-only Pro worker を足して枠を見せない
3. 偽の並行（重複・待ちの二重計上）を作らない
4. 成長してよいのは **GREEN** のときだけ **trial +1**
5. CU は対象外（always 1）

YELLOW では補充で成長しない。RED では影響資源のキャップを下げる。HARD では影響 op を閉じる。

---

## 6. 兄弟パックとの境界

`ops-bake-orch-cli-20260916/`（下書き）と矛盾させない。

| 兄弟側（ORCH / CLI / Head） | この窓 |
|---|---|
| 実働順: SWE-2 Max → Cursor Grok → Sol または親 Astra | 並行**数**とレーンだけ。振り分け順は再定義しない |
| CU mutex=1。並列 CU を焼かない | CU = **1 always**。`{{ADAPTIVE}}` +1 を CU に掛けない |
| Effort は requested / resolved / observed。未観測を 0 にしない | 最適数は `{{UNKNOWN}}`。~10 を観測値にしない |
| G1 は 15 並行を証明しない | 15 も 10 もキャップ候補にしない |
| Hands~0 | 手元操作を増やさない。この PR で CU を起動しない |

---

## 7. この下書きがやらないこと

- `{{UNKNOWN}}` を 10/10 や 0 で置換する
- `{{LEGACY_UNVERIFIED}}` を現行 max として焼く
- RED の下げ幅、HARD の実装、reconcile のコードを発明する
- 振り分け表の新しい TTL・料金を足す
- bridge / 憲法 / スキル本体のパッチ
- 「適用済み」「実機合格」のスタンプ
- 秘密・Cookie・トークン・Drive ファイル ID の転記
