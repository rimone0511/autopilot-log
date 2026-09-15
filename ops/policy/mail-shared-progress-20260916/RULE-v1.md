# メール仕分け共通進捗（shared-progress）RULE-v1

日付: 2026-09-16  
きっかけ: 手動「メール仕分け」直後と朝の秘書便が同じ内容を本人に繰り返した。

## 正本
- Box: `/workspace/grok-operations/ops/mail/shared-progress.json`
- GitHub: `autopilot-log` の `ops/mail/shared-progress.json`（クラウド／PC／他モデルが同じ続きを見る）
- 台帳 Windows 正本は別物。これは「報告・仕分けの現在地」用。

## いつ更新するか
1. 本人依頼のメール仕分けスキル実行後（必須）
2. 朝・昼・夕のメール便／秘書便の仕分け後（必須）
3. Devin / Cursor Grok / Codex / Claude が仕分けを代行した直後（必須）

## 報告ルール（重複防止）
- 開始前に必ず `shared-progress.json` を読む。
- `reported_open_items[].fingerprint` が前回と同じなら、本人向け本文の「いま動くこと／本人判断」に再掲しない（result に「変化なし」）。
- 再掲してよい条件: 新着、状態変化、金額・期限変化、期限が今日／超過で未完、本人が再依頼。
- 報告済み ≠ 決着済み。

## 禁止
- 秘密（パスワード、OTP、カード番号全文、住所本文）を書かない。
- このファイルだけで台帳決着を断定しない。
