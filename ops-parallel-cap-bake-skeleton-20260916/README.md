# ops-bake 並列キャップ骨格（下書き）

案件: 並列キャップ APPLY-WINDOW の骨格  
版: 2026-09-16 DRAFT  
枝: `ops-parallel-cap-bake-skeleton-20260916/`

**これは骨格だけです。本番の憲法・CLI・Bot・スキルへは適用していません。**  
**最終数字は焼かない。Pro `PARALLEL-CAP-PERF` の回答が来るまで `{{PRO_NUMBER}}` のまま残す。**

リポジトリに既存の並列キャップ APPLY 原文は無かった。HANDS が渡した窓の形と、照合できたロック（CU mutex）だけを薄く残す。無い数字・手順・コマンドは作らない。

## このフォルダ

| ファイル | 中身 |
|---|---|
| [APPLY-WINDOW.md](APPLY-WINDOW.md) | 並列キャップの窓。max Cursor Grok / SWE-2 / CU / refill-on-empty はプレースホルダ |
| [BAKE-CHECKLIST.md](BAKE-CHECKLIST.md) | Pro 回答が着いてから数字を焼く手順。今は全部未完 |
| [SOURCES.md](SOURCES.md) | 照合した原典。秘密・認証・Drive ID は書かない |

## 状態

| 項目 | 今 |
|---|---|
| APPLY-WINDOW | 骨格。`{{PRO_NUMBER_*}}` 未置換 |
| Pro `PARALLEL-CAP-PERF` | **未回収**。MAIN Pro 枠 残り 0% の記録あり |
| ソフト暫定 GO | Cursor Grok **~10** + SWE-2 **~10**。Pro までの仮。最終値ではない |
| CU | 兄弟パック ORCH が mutex=**1** をロック。この窓でも上げない |
| 本番適用 | していない |

## まだ本番にしないこと

- `{{PRO_NUMBER_*}}` を推測で埋めない。~10 を正として焼かない
- 憲法・CLI・desired-state の実書き換え
- Computer Use の起動、並列 CU の焼き込み
- 未回収 Pro の想像復元
- 公開・課金・解約・秘密の転記

## 検証

Markdown の下書きだけ。Python ゲート試験は変更していない。実機 APPLY はしていない。
