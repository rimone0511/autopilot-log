# PARALLEL-CAP-PERF 薄い規則（スタブ）

状態: **DRAFT / stub / not production-applied**  
置き場: 観測と突合のメモ。共通指示の厚い本文や APPLY-WINDOW の数字欄ではない。

このファイルは薄い。料金・TTL・キュー長・補充間隔・最適 N を足さない。  
擬似コードの正は [OBSERVER-RECONCILE.md](OBSERVER-RECONCILE.md)。台帳語は [LEDGER.md](LEDGER.md)。

---

## ロック（このスタブが守る）

1. **最適 N は UNKNOWN。** 観測値でも `LEGACY_UNVERIFIED~10` でも最適値にしない。未観測を 0 にも最適値にもしない。
2. **CU = 1。** Computer Use の同時数は 1。`n_observed(CU) > 1` は **HARD**。このスタブは CU を起動しない。
3. **LEGACY_UNVERIFIED~10。** HANDS のソフト暫定 GO（Cursor Grok ~10 + SWE-2 ~10）は、Pro までの仮ヒント。最終キャップではない。APPLY 列へ写さない。検証済みとも書かない。
4. **帯は分類だけ。** GREEN / YELLOW / RED / HARD は台帳の色。本番の cap を焼かない。
5. **observer は書く。reconcile は色を付ける。どちらも apply しない。** refill-on-empty の実行も、空席補充の個数発明もしない。
6. **新しい監視台帳サービスを既定にしない。** 常駐プロセス・専用監視モデル・司令塔は作らない。メモと擬似コードに留める（CLI-CACHE v2.0 / Pro 総点検の「監視台帳を新設しない」と両立）。

---

## 家族（このスタブが見る列）

| family | ロック | 最適 N | 仮ヒント |
|---|---|---|---|
| `cursor_grok` | 難所の実働候補（振り分け順は兄弟 ORCH） | UNKNOWN | LEGACY_UNVERIFIED~10 |
| `swe2` | 通常実働の第一候補（〜2026-10-10） | UNKNOWN | LEGACY_UNVERIFIED~10 |
| `cu` | mutex=1 | UNKNOWN（1 は mutex であり最適並行数ではない） | 無し。1 より上げない |

Grok と SWE-2 を合算して一つの N にしない。CU を Grok/SWE-2 の ~10 に混ぜない。

---

## 帯の薄い意味（閾値を新しく作らない）

既知の定数は **CU=1** と **LEGACY_UNVERIFIED~10** だけ。7 や 15 などの第三の数字を帯の境界にしない。

| 帯 | いつ付けるか（薄い） | 付けてもしてよいこと | 付けてもしてはいけないこと |
|---|---|---|---|
| **GREEN** | CU が 0 または 1、かつ Grok/SWE-2 の `n_observed` が実測であり、LEGACY_UNVERIFIED~10 を超えていない | 次の観測を続ける | 空席補充、キャップ引き上げ、最適 N の宣言 |
| **YELLOW** | 未観測、または観測源が LEGACY_UNVERIFIED、または ~10 の近傍で仮ヒント自身が未検証 | 観測を厚くする。起動を増やさない | 未観測を 0 と読む。~10 を正にする |
| **RED** | Grok または SWE-2 の観測数が LEGACY_UNVERIFIED~10 を**超えた**（ヒントを注意天井として使う。最適値ではない） | 新規起動を止めるメモ。drain | APPLY、refill、CU 追加 |
| **HARD** | CU>1、または最適 N を既知として書いた、またはこのスタブから本番 apply / CU 起動をしようとした | 停止。本人確認。何も焼かない | 自動復旧、数の上書き、HARD を YELLOW に戻す |

`~10` は近似なので、ちょうど 10 は **YELLOW**（仮ヒントそのものが未検証）とし、はっきり超えたときだけ RED。10 を最適値の証明にしない。

---

## この薄い規則がやらないこと

- `{{PRO_NUMBER_*}}` の置換（それは兄弟 APPLY-WINDOW）
- 最適 N の探索実験、負荷試験、15 並行の再証明
- bridge / 憲法 / スキル本体のパッチ
- 秘密・Cookie・トークン・金庫パスの転記
