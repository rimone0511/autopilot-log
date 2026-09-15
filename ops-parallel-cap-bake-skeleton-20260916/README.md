# ops-bake 並列キャップ骨格（下書き）

案件: 並列キャップ APPLY-WINDOW（適応設計）  
版: 2026-09-16 DRAFT  
枝: `ops-parallel-cap-bake-skeleton-20260916/`

**これは下書き APPLY です。本番の憲法・CLI・Bot・スキルへは適用していません。**  
**固定の 10/10 max は焼かない。** 最適数はライブ観測まで `{{UNKNOWN}}`。

回収した Pro `PARALLEL-CAP-PERF` で、骨格の `{{PRO_NUMBER}}` を適応トークンへ置き換えた。無い観測・下げ幅・関数実装は作らない。

## このフォルダ

| ファイル | 中身 |
|---|---|
| [APPLY-WINDOW.md](APPLY-WINDOW.md) | 共有キャップ `{{UNKNOWN}}`、旧 ~10/~10 は `{{LEGACY_UNVERIFIED}}`、増減は `{{ADAPTIVE}}`、CU=1 |
| [BAKE-CHECKLIST.md](BAKE-CHECKLIST.md) | 既知項目はチェック済み。ライブ観測と本番パッチは未 |
| [SOURCES.md](SOURCES.md) | 照合した原典。秘密・認証・Drive ID は書かない |

## 状態

| 項目 | 今 |
|---|---|
| APPLY-WINDOW | 適応設計。`{{LEGACY_UNVERIFIED}}` / `{{UNKNOWN}}` / `{{ADAPTIVE}}` / CU=1 |
| Pro `PARALLEL-CAP-PERF` | **回収済み**（HANDS 2026-09-16） |
| 旧 ~10/~10 | 移行境界のみ。証明済み maxima ではない |
| CU | **1 always** |
| 最適並行数 | `{{UNKNOWN}}`（ライブ観測待ち） |
| 本番適用 | していない |

## まだ本番にしないこと

- `{{UNKNOWN}}` を 10/10 で埋める。`{{LEGACY_UNVERIFIED}}` を現行 max にする
- 憲法・CLI・desired-state の実書き換え
- Computer Use の起動、並列 CU の焼き込み
- wait-only Pro worker、偽の並行の実装コードをこの PR で足す
- 公開・課金・解約・秘密の転記

## 検証

Markdown の下書きだけ。Python ゲート試験は変更していない。実機 APPLY はしていない。
