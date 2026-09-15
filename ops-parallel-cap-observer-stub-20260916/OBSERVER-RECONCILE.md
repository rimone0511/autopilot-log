# observer / reconcile 擬似コード（スタブ）

状態: **DRAFT / not executable / not production-applied**  
言語はメモ用。ランナーもロックファイルも作らない。

入力は「今見えた並行数」。出力は台帳行と帯。**APPLY しない。CU を起動しない。最適 N を返さない。**

規則の正は [THIN-RULES.md](THIN-RULES.md)。語彙は [LEDGER.md](LEDGER.md)。

---

## 0. 共通の約束

```
N_OPTIMAL := UNKNOWN          # 永久。計算しない
LEGACY_HINT_GROK := ~10       # LEGACY_UNVERIFIED。キャップではない
LEGACY_HINT_SWE2 := ~10       # 同上
CU_MUTEX := 1                 # 超えたら HARD
APPLY := no                   # このスタブでは常に no
```

未観測は `UNOBSERVED`。`0` に折らない。  
Grok と SWE-2 と CU は別行。合算 N を最適値にしない。

---

## 1. observer（書くだけ）

観測源の題名と日付だけ残す。本文・秘密・ID は残さない。

```
function observe(family, source_title, source_date, count_or_none):
    row = ledger[family]
    row.n_optimal = UNKNOWN
    row.apply = no

    if family in {cursor_grok, swe2}:
        row.n_legacy_hint = LEGACY_UNVERIFIED~10
    else if family == cu:
        row.n_legacy_hint = -

    if count_or_none is missing:
        row.n_observed = UNOBSERVED
        row.ledger_state = UNOBSERVED
        # 帯は reconcile が付ける
        return row

    # count は非負整数。推定・四捨五入・合算をここでしない
    row.n_observed = count_or_none
    row.ledger_state = OBSERVED
    row.source = {title: source_title, date: source_date}  # 題名だけ
    return row
```

observer は帯を付けない。色は reconcile の仕事。  
observer はプロセスを増やさない。空席があっても refill しない。

---

## 2. reconcile（色を付ける。止めメモまで）

```
function clearly_beyond_legacy_hint(n, hint_approx_10):
    # ~10 は近似。境界の 10 は超えたことにしない
    return (n is a number) and (n > 10)

function at_or_near_legacy_hint(n):
    return (n is a number) and (n == 10)

function classify_cu(n):
    if n is UNOBSERVED: return YELLOW, UNOBSERVED
    if n == 0:          return GREEN, OBSERVED
    if n == CU_MUTEX:   return GREEN, MUTEX_CU_1
    if n > CU_MUTEX:    return HARD, MUTEX_VIOLATION
    # n が負など不正
    return HARD, MUTEX_VIOLATION

function classify_agent_family(n):
    # n_optimal を数字にした時点で HARD（発明）
    if n is UNOBSERVED:
        return YELLOW, UNOBSERVED
    if clearly_beyond_legacy_hint(n, ~10):
        return RED, DRAIN
    if at_or_near_legacy_hint(n):
        return YELLOW, LEGACY_UNVERIFIED   # ヒント自身が未検証
    # 実測あり、かつ ~10 を超えていない
    return GREEN, OBSERVED

function reconcile(ledger):
    # 先に HARD 条件（家族を問わず）
    if any row.n_optimal != UNKNOWN:
        mark_all HARD
        stop_without_apply("invented optimal N")
        return ledger

    if any attempted_apply or attempted_cu_launch or attempted_refill:
        mark_all HARD
        stop_without_apply("stub does not apply")
        return ledger

    for family in {cursor_grok, swe2, cu}:
        row = ledger[family]
        if family == cu:
            row.band, row.ledger_state = classify_cu(row.n_observed)
        else:
            row.band, row.ledger_state = classify_agent_family(row.n_observed)
        row.n_optimal = UNKNOWN
        row.apply = no

    # CU HARD は他家族より優先して残す（mutex 破壊）
    if ledger.cu.band == HARD:
        ledger.cu.ledger_state = MUTEX_VIOLATION
        # Grok/SWE-2 の帯は消さない。CU 行だけ HARD
        stop_without_apply("CU mutex > 1")

    if any family in {cursor_grok, swe2} has band == RED:
        that_row.ledger_state = DRAIN
        # 新規起動を止めるメモ。kill しない。APPLY しない

    return ledger
```

`stop_without_apply` はログ用の語。実装の raise でも Bot 停止でもない。  
この関数の戻り値に cap 数字を載せない。

---

## 3. 動かない経路（意図的に空）

```
function apply_window(...):
    HARD
    return  # 兄弟 APPLY-WINDOW のトークン置換も、憲法パッチもしない

function launch_cu(...):
    HARD
    return

function refill_on_empty(...):
    HARD
    return  # {{PRO_NUMBER_REFILL_ON_EMPTY}} は未着。個数を作らない

function invent_optimal_n(observed):
    HARD
    return UNKNOWN
```

---

## 4. 一周期の順

1. family ごとに `observe`（無いなら UNOBSERVED のまま）
2. `reconcile`
3. 帯をメモする
4. **終わる。** desired-state を書き換えない

Hands~0 と両立: 手元操作を増やさない。CU を使う場合でも mutex=1 は兄弟 ORCH のロックであり、このスタブは CU を使わない。

---

## 5. やらないこと

- この擬似コードを `.py` / CLI / cron に落とすこと（別案件。この PR の外）
- 観測数から最適 N を回帰すること
- `LEGACY_UNVERIFIED~10` を `n_observed` にコピーすること
- 「GREEN だから補充してよい」と APPLY すること
