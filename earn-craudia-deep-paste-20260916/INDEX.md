# INDEX — クラウディア worker deep CU

観測: 2026-09-16（公開 GET。登録なし）  
状態: **DRAFT_ONLY** / `cu_ready` はパックがあること。登録済みではない。

本番の Wave A 直列は兄弟 `earn-cu-runbook-20260916/RUNBOOK.md` と `earn-register-pack-index-20260916/` を正とする。  
**このフォルダの貼る順**は深掘り 1 机だけ。A9。

| 順 | Pack | INDEX CU | QUEUE | Google | 止める場所 |
|---|---|---|---|---|---|
| 1 | [01-craudia.md](01-craudia.md) | CU-09 | A9 | **PREFER_GOOGLE**（register-temp の `signin_btn_google.svg` / i2i `auth=3`） | マイページ設定 → 本人確認（書類+**自撮り**）。参加申請。スキル出品。口座・出金 |

## Fee / rate citation rule

| ラベル | 意味 |
|---|---|
| **cited** | 公式の公開ページに数字または「無料」が出た。URL と引用をパックに残した |
| **needs_check** | 公式ページに料率・字数が無い、またはログイン壁（出金の「くわしくはこちら」、本人確認 UI）。創作しない。画面カウンター / 現行手数料ページを正とする |
| **placeholder** | `{{HOURLY_JPY}}`。git に実額なし。空で保存できるなら空 |

机の表は [01-craudia.md](01-craudia.md) と [STOP-KYC.md](STOP-KYC.md) を見よ。

## Bio length rule

| 欄 | 公式に出た上限 | このパックのフェンス |
|---|---|---|
| キャッチ / 短い自己紹介 | **needs_check**（FAQ に字数なし） | **23** 字。画面で切る |
| 自己紹介 | **needs_check**（FAQ 92 / 78 に字数なし） | **200 / 255 / 800**（測済み）。カウンター超過なら短い方へ |
| スキル出品タイトル | **cited 25 文字以内**（出品ガイド） | **使わない。** 出品画面に入らない |
| プロフィール スキル / 得意種別 | **needs_check**（公開一覧は SPA。meta に得意種別の分類あり） | プログラム・開発系 + 実務スキルのみ。未経験を経験と書かない |

## 共通プレースホルダ

実値はローカルの本人台帳だけ。このリポジトリには書かない。README の Shared placeholders と同じ。

公開してよい URL:

- https://yutalab.dev/
- https://github.com/rimone0511
- https://github.com/rimone0511/autopilot-log

## このPRでやらないこと

- アカウント作成
- 本人確認（書類・自撮り）
- 応募・スキル出品・公開・PRO
- 秘密・実メール・実電話のコミット
- 案件数・GMV・登録者数の創作
- 時給円額の創作
