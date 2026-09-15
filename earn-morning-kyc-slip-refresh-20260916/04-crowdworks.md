# Slip — クラウドワークス CrowdWorks

**DRAFT_ONLY.** ワーカープロフィールは下書き。**応募しない。**  
**エージェントは signup しない。アップロードしない。403 を再試行しない。**

| | |
|---|---|
| Desk | クラウドワークス CrowdWorks（Wave A4 / CU-04） |
| CU hint | `blocked_skip` **403** |
| Who | **祐太だけ** |
| 入口 | ログイン後「名前 → 本人確認書類提出」（ライブメニューを正） |
| いつ | 出金の必須、と案内。出金も応募も今朝はやらない |

---

## この机のいま

live box から homepage / signup が **403 Forbidden**（[PR#35](https://github.com/rimone0511/autopilot-log/pull/35)）。  
エージェント・この環境から **再GETしない。signup しない。**  
[PR#24](https://github.com/rimone0511/autopilot-log/pull/24) の「CW next」は古い。Upwork も `blocked_skip`（Google SSO）。**次の CU は LinkedIn profile draft**（Services は GO-gated / 開かない）。

人が **自分の回線・自分のブラウザ** で開いて、本人確認の画面が出たときだけこのスリップ。403 のままなら `blocked_skipのまま`。AI CrowdWorks（B15）と PARK（`park.jp`）は開かない。

---

## 上げるもの（サイトの画面にだけ）

どれか（個人・ワーカー）:

- 運転免許証 **表裏**
- マイナンバーカード **表面だけ**（番号面・通知カードは公式対象外）
- **デジタル認証アプリ**（マイナカード + デジタル庁アプリ。氏名・住所・生年月日だけ渡る、と公式。番号は渡らない、と書くが **番号はメモしない**）

保険証は **2026-07-27 以降の新規は不可**、という既存朝チェックのメモ。画面が保険証だけ出したら **閉じる**（新しい案内があれば画面を正）。

ヘルプ:  
https://blog.crowdworks.jp/archives/5685/  
https://blog.crowdworks.jp/archives/6465/  
https://crowdworks-help.zendesk.com/hc/ja/sections/4987979705374  
規約の本人確認: https://crowdworks.jp/pages/agreement

ラベル確認だけなら開いてすぐ閉じる。ファイルは選ばない。

---

## 上げない / やらない

- [ ] この環境 / エージェントから 403 を再試行する、会員登録を完了する
- [ ] 応募する / 提案送信 / コンペ提出 / タスク開始
- [ ] マイナンバー **番号面**、通知カード、番号のメモ
- [ ] 振込先口座・ゆうちょ・個人口座を今入れる
- [ ] インボイス登録番号を git に書く
- [ ] 法人本人確認。個人のまま
- [ ] クライアントダッシュボードに留まる。ワーカーへ戻れなければ閉じる
- [ ] 書類を git / チャット / エージェントへ

---

## DRAFT_ONLY reminder

403 は「書類が足りない」ではない。**回線側の門**。門が開いてから本人確認。  
プロフィールが既に下書きなら、公開も応募もしない。

状態: `なし` / `上げた` / `待ち` / `詰まった` / `blocked_skipのまま`
