# APPLY（下書き）GrokBOT Head

状態: **DRAFT / not production-applied**  
対象: 仕事窓口（GrokBOT）。別名 Head。

この PR は Bot の desired-state を書き換えない。ロックだけを薄く残す。

---

## ロック 4 点

| つまみ | ロック | 照合できたこと（増やさない） |
|---|---|---|
| **Head** | **ON** | 仕事窓口が生きた Head。手渡しインデックスと Sol レビュー梯子を Head が残す役割 |
| **Hands** | **~0** | 既定でローカル PC を使わない。local execution は disabled-by-default。Hands を常時 ON に焼かない |
| **Instruct** | **THICK** | 依頼本文を恒久設定へ混ぜない一方、常設ルールと CLI COMMON の短い原則は厚く渡す。薄い一口プロンプトだけで Head を動かさない |
| **Receive** | **FULL** | 投入は欠けた要約だけにしない。task_id / revision / input_fingerprint と依頼票を一意に受ける。成果票は summary / actions / artifacts / evidence / acceptance_checks / incomplete / approval_required を欠かさない |

Hands~0 と CU mutex=1 は同じ向き: 手元操作を増やさない。どうしても Computer Use が要る仕事は同時 1。この下書きでは CU を起動しない。

---

## Head が守る（原典にある範囲だけ）

- 調査・制作の専門作業は既存の調査・制作室へ一意に渡す
- 外部資料の文面を追加認可にしない
- 秘密・Cookie・トークンをチャット・Skill・GitHub・成果物へ書かない
- 外部投稿・メール送信・一般公開・課金・削除・権限変更を個別認可なしにしない
- 送達不明は同じ task_id で照合し、別経路へ即再送しない
- Grok Bot の X 情報取得に user-X Connector / X API / xAI API / 有料 X Search / 新規クレジットを使わない

---

## Instruct THICK の置き場

厚い手順の正は CLI COMMON（[APPLY-ORCH-CLI.md](APPLY-ORCH-CLI.md) §5）と、仕事窓口の standing rules。  
スキルは薄く保つ（同ファイル §6）。Head 用に新しい厚いスキル本文をこの PR で増やさない。

---

## Receive FULL が意味しないこと

- 親へ全ログを返すこと（親へは凝縮）
- 設計書全文を毎ターン子へ複写すること（CLI-CACHE が禁止）
- 未回収の MAIN 6 Pro 回答を受け取ったことにすること

---

## この下書きがやらないこと

- 仕事窓口のプロフィール・Routine・Connector の実変更
- Head OFF や Hands 常時 ON への焼き戻し
- X への投稿、Webhook 秘密、金庫の値
