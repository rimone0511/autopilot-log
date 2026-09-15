# ops 並列キャップ observer / reconcile スタブ（下書き）

案件: PARALLEL-CAP-PERF の **薄い規則** を、観測と突合のメモとして残す  
版: 2026-09-16 DRAFT  
枝: `ops-parallel-cap-observer-stub-20260916/`

**これはスタブです。本番の憲法・CLI・Bot・スキルへは適用していません。**  
**擬似コードと Markdown だけ。実行しない。配備しない。Computer Use を起動しない。**

最適並行数 **N は UNKNOWN**。`~10` を最適値にも APPLY 値にもしない。  
CU は mutex=**1**。秘密・トークン・Drive ID は書かない。

兄弟の APPLY-WINDOW 骨格（`ops-parallel-cap-bake-skeleton-20260916/`）は数字の正を待つ窓。  
このパックは窓を焼かず、**観察と台帳の突合**だけを薄く書く。

## このフォルダ

| ファイル | 中身 |
|---|---|
| [THIN-RULES.md](THIN-RULES.md) | PARALLEL-CAP-PERF の薄い規則（CU=1 / LEGACY_UNVERIFIED~10 / N=UNKNOWN） |
| [LEDGER.md](LEDGER.md) | 台帳の状態語。GREEN / YELLOW / RED / HARD |
| [OBSERVER-RECONCILE.md](OBSERVER-RECONCILE.md) | 観測と突合の擬似コード。適用手順は無い |
| [SOURCES.md](SOURCES.md) | 照合した題名と日付だけ |

## 状態

| 項目 | 今 |
|---|---|
| 最適 N | **UNKNOWN**。発明しない |
| LEGACY_UNVERIFIED | Cursor Grok **~10** と SWE-2 **~10**。仮ヒント。未検証 |
| CU | **1**。並列 CU を焼かない・起動しない |
| 帯 | GREEN / YELLOW / RED / HARD は分類語。APPLY 値ではない |
| 本番適用 | していない |

## まだ本番にしないこと

- 最適 N の推定、~10 の焼き込み、15 並行の証明扱い
- 憲法・CLI・desired-state の実書き換え
- Computer Use の起動、並列 CU
- 常駐の監視サービスや新しい司令塔の実装
- 公開・課金・解約・秘密の転記

## 検証

Markdown と擬似コードの下書きだけ。Python ゲート試験は変更していない。実機 APPLY はしていない。
