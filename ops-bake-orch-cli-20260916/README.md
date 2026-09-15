# ops-bake ORCH + CLI + GrokBOT Head（下書き）

案件: 運用焼き込み（オーケストレーション・CLI共通・仕事窓口）  
版: 2026-09-16 DRAFT  
枝: `ops-bake-orch-cli-20260916/`

**これは下書き APPLY です。本番の憲法・CLI・Bot・スキルへは適用していません。**

リポジトリ内に既存の APPLY 原文は無かった。HANDS 指示のロック決定と、照合できた Pro / 本人決定だけを薄く焼く。無い数字・手順・コマンドは作らない。

## このフォルダ

| ファイル | 中身 |
|---|---|
| [APPLY-ORCH-CLI.md](APPLY-ORCH-CLI.md) | 振り分け順、CU mutex=1、SWE-2優先、Effortは観測、CLI COMMON、skills thin、Gemini Flash JP は一度、G1–G4 |
| [APPLY-GROKBOT.md](APPLY-GROKBOT.md) | Head ON / Hands~0 / Instruct THICK / Receive FULL |
| [SOURCES.md](SOURCES.md) | 照合した原典。秘密・認証・Drive ID は書かない |

## まだ本番にしないこと

- Codex / Claude Code / Cursor の共通指示やスキルをこの PR で書き換えない
- GrokBOT の desired-state をこの PR で書き換えない
- Computer Use を起動しない
- MAIN 6 Pro（GROK-FOUNDATION-COST）の再送結果は未回収。枠 0% の記録がある。未回収分を想像で埋めない
- 公開・課金・解約・秘密の転記をしない

## 検証

Markdown の下書きだけ。Python ゲート試験は変更していない。実機 APPLY はしていない。
