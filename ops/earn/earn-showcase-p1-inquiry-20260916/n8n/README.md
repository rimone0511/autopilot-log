# n8n 輸出（任意）

`inquiry_intake_p1.json` は認証情報なしのワークフロー輸出です。

1. n8n を開く（手元の空インスタンスでよい）
2. Workflows → Import from File
3. この JSON を選ぶ
4. Credentials は出ない。Manual Trigger を実行する

ノードは合成20件を Code 内に持ち、Python と同じ理由コードで `queue` を付けます。  
外部HTTP・メール送信・Google・Slack はありません。

n8n のバージョンで Code ノードが失敗したら、親フォルダの `python3 run.py` を正とします。
