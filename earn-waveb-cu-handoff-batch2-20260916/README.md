> **MAIN Google only.** Same mailbox as QUEUE / CU runbook. Placeholder `{{EMAIL}}` / `{{GOOGLE_ACCOUNT_EMAIL}}`. No second account, no `+desk@`, no LINE / Apple / Facebook / Yahoo / X just for this GO.
> **DRAFT_ONLY.** Profile save only. No publish, 応募, エントリー, 話を聞きたい, ジョブ投稿, スカウト返信.
> **STOP-KYC.** No ID, My Number reverse, selfie-with-ID, bank, Stripe, 印鑑証明. See [STOP-KYC.md](STOP-KYC.md).
> **No secrets.** No passwords, OTP, phone digits, ID images, account numbers in git or session logs.
> **No invented fees.** Cite official public pages only. Missing % → `needs_check`. No GMV / 登録者数 as activity proof.
> **No publish.** This folder is not a live listing. The agent that wrote it did not sign up.

# Wave B CU-ready DRAFT profile packs — batch 2 (2026-09-16)

状態: **DRAFT_ONLY** / `cu_ready` はパックがあること。**登録済みではない。**  
対象: PR#21 ALIVE サンプルが **含めないと書いた** 5机。  
このフォルダは Computer Use（CU）へ渡す **手渡し**。パック本文は下書き。**このPRでは登録しない。**

観測: 2026-09-16 公開 GET のみ。ログイン Cookie なし。詳細は [METHOD.md](METHOD.md)。

兄弟資料（本文は複製しない）:

- 活動ゲート: `earn-activity-gate-waveB-20260916/`（PR#12）
- JP Week2 薄い登録パック: `earn-register-packs-jp-20260916/`（PR#3。Workship / CrowdLinks の在庫）
- Wave B ALIVE サンプル（別5机）: `earn-waveb-alive-handoff-sample-20260916/`（PR#21）
- CU直列索引: `earn-register-pack-index-20260916/INDEX.md`（PR#8）
- QUEUE: `earn-register-expand-20260916/QUEUE.md`（PR#1）
- 朝の本人確認: `earn-kyc-morning-checklist-20260916/`（PR#4）

INDEX の `earn-packs/youtrust/` などへは複製しない。

## このフォルダの貼る順（pass を先に）

本番の Week2 直列は INDEX **CU-11 Workship 起算**のまま。ここは **この5机だけ**の手渡し順。  
`needs_check` の机は、人が公開一覧の日付（または登録面が開くこと）を1画面見てから CU を進める。見えないまま pass 扱いにしない。

Wave A の `next` が全部 `done-draft` になるまで、**本番直列では** Week2 を開かない（INDEX / QUEUE どおり）。このフォルダはパック用意。

| 順 | 在庫 | INDEX CU | 机 | activity_gate | Google | 止める場所 |
|---|---|---|---|---|---|---|
| 1 | [01-workship.md](01-workship.md) | CU-11 | Workship | **pass** | PREFER_GOOGLE（SNS。アイコンの Google ラベルは貼る人が目視） | 契約署名・前払いの本人確認・口座 |
| 2 | [03-itpropartners.md](03-itpropartners.md) | CU-28 | ITプロパートナーズ | **pass** | **NOT_OFFERED_OAUTH** → MAIN Google メールでフォーム | エージェント面談で身分証。登録完了の先の営業電話は本人 |
| 3 | [04-offers.md](04-offers.md) | CU-25 | Offers | **pass** | PREFER_GOOGLE（`/worker/signup` に「Google で登録する」） | 応募・有料ブース・転職エージェント面談のID |
| 4 | [02-crowdlinks.md](02-crowdlinks.md) | CU-14 | クラウドリンクス | **needs_check** | PREFER_GOOGLE（FAQ: Google認証。登録SPAはクリック時） | 有料会員化・追加書類・口座。応募しない |
| 5 | [05-youtrust.md](05-youtrust.md) | CU-24 | YOUTRUST | **needs_check** | PREFER_GOOGLE（公式ヘルプ: Googleアカウント連携。`/sign_in` はSPA） | 話を聞きたい / ジョブ投稿 / 公式リクルーター有料 / Google連絡先インポート |

## 本番 INDEX 直列（この5机の番号だけ。飛ばす命令ではない）

PR#8 の CU 正本:

1. **CU-11** Workship（このフォルダ 01）
2. （間に CU-12〜CU-13 / CU-15〜CU-23 がある。このPRの対象外）
3. **CU-14** クラウドリンクス（このフォルダ 02）
4. **CU-24** YOUTRUST（このフォルダ 05）
5. **CU-25** Offers（このフォルダ 04）
6. **CU-28** ITプロパートナーズ（このフォルダ 03）

PR#3 の薄い `02-workship.md` / `04-crowdlinks.md` より、**このフォルダを後続CUの正**とする（Field map と STOP が厚い）。画面ラベルが違うときは **画面を正**。

## CU 共通（全パック）

1. 1机ずつ。人材／売り手入口だけ。企業コンソールなら閉じる。
2. **MAIN Google のみ。** メールは `{{EMAIL}}`。別アカウント禁止。
3. プロフィール・自己紹介は **下書き保存**。公開トグル、応募、スカウト返信、ジョブ投稿はしない。
4. Gmail OTP は親（Gmail MCP）。CU ブラウザで Gmail を開かない。
5. SMS が要る画面はユーザーチャット待ち。不在なら park して次へ。
6. KYC が出たらアップロードせず停止。朝の本人へ机名と画面の種類だけ。
7. 手数料％が公式ページに無いなら空 / `needs_check`。第三者ブログの「10〜25%」を貼らない。
8. 値はプレースホルダのまま。実メール・電話・パスワード・身分証を git に書かない。
9. Press & Hold がある画面は `holdDurationMs`（目安 1800、再試行 2500）。スキーマに無ければセッション停止。

## 共通プレースホルダ

実値はローカルの本人台帳だけ。このリポジトリには書かない。

- `{{GOOGLE_ACCOUNT_EMAIL}}` / `{{EMAIL}}` MAIN Google（同じ値）
- `{{LEGAL_NAME_KANJI}}` 戸籍上の氏名（漢字）
- `{{LEGAL_NAME_KANA}}` 氏名カナ
- `{{DISPLAY_NAME}}` 表示名。推奨: `石田祐太`
- `{{PHONE}}` 日本の携帯電話
- `{{POSTAL_CODE}}` 郵便番号
- `{{PREFECTURE}}` 都道府県
- `{{CITY}}` 市区町村以下
- `{{BIRTH_YEAR}}` / `{{BIRTH_MONTH}}` / `{{BIRTH_DAY}}` 生年月日
- `{{PORTFOLIO_URL}}` 推奨公開: `https://yutalab.dev/`
- `{{GITHUB_URL}}` 推奨公開: `https://github.com/rimone0511`
- `{{GITHUB_REPO_AUTOPILOT}}` `https://github.com/rimone0511/autopilot-log`
- `{{PHOTO_LOCAL_PATH}}` 顔写真のローカルパス（コミット禁止）
- `{{INVITE_CODE}}` 招待コード。無ければ空
- `{{YEARS_AUTOMATION_PUBLIC}}` 公開実録の期間だけ。未確認なら空
- `{{BLOCK_COMPANY_NAMES}}` 非表示企業。無ければ空。実名をこのPRに書かない
- `{{HOURLY_YEN_DRAFT}}` / `{{PRICE_YEN_DRAFT}}` 空のまま。未確認の時給を書かない

公開してよいURL（秘密ではない）:

- サイト: https://yutalab.dev/
- GitHub: https://github.com/rimone0511
- Autopilot Log: https://github.com/rimone0511/autopilot-log

## ラベル

| ラベル | 意味 |
|---|---|
| `pass` | 公開ページに新しさの手がかりがある。下書き登録の検討可。公開しない |
| `needs_check` | 公開情報が足りない（SPA / 未ログイン / 日付なし）。推測で pass にしない |
| `cu_ready` | Field map と貼る文がある。**登録済みではない** |
| `NOT_OFFERED_OAUTH` | 公開面に Google ボタンが無い。MAIN Google の **メール** で登録する |

`thin_site_skip` は全5件 **false**。読めない ≠ 死んでいる。

## このPRでやらないこと

- アカウント作成、OAuth 完走、OTP 入力
- 本人確認アップロード
- 出品・応募・公開・有料プラン
- 秘密・実メール・実電話のコミット
- 案件数・GMV・「稼げる額」・未確認マージン％の創作
- Python 投稿ゲート試験の変更
