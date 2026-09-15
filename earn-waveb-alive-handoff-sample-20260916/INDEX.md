# INDEX — Wave B ALIVE handoff sample (5 packs)

観測: 2026-09-16（公開 GET。登録なし）  
状態: **DRAFT_ONLY** / `cu_ready` はパックがあること。登録済みではない。

## このサンプルの貼る順（pass を先に）

JP-WEEK2-INDEX の CU-12→CU-13 とは違う。ここは **activity_gate=pass を先頭** にした5机の手渡し順。  
本番の Week2 直列は INDEX CU-11 Workship 起算のまま。Workship / CrowdLinks を飛ばす命令ではない。

| 順 | 在庫 | CU（INDEX） | 机 | activity_gate | Pack | 止める場所 |
|---|---|---|---|---|---|---|
| 1 | [01-sokudan.md](01-sokudan.md) | CU-13 | SOKUDAN | pass | cu_ready | 審査書類・身分証 |
| 2 | [03-anycrew.md](03-anycrew.md) | CU-15 | Anycrew | needs_check | cu_ready | 公開設定を公開にしない。職務経歴書必須画面 |
| 3 | [02-fukugyo-cloud.md](02-fukugyo-cloud.md) | CU-12 | 複業クラウド | needs_check | cu_ready | Googleボタン目視。本人確認・口座 |
| 4 | [04-menta.md](04-menta.md) | CU-16 | MENTA | needs_check | cu_ready | Stripe本人確認・口座・プラン公開 |
| 5 | [05-street-academy.md](05-street-academy.md) | CU-17 | ストアカ | needs_check | cu_ready | 顔写真付き証明書・講座公開 |

`needs_check` の机は、人が公開一覧の日付（または登録面が開くこと）を1画面見てから CU を進める。見えないまま pass 扱いにしない。

## 共通プレースホルダ

実値はローカルの本人台帳だけ。このリポジトリには書かない。

- `{{LEGAL_NAME_KANJI}}` 戸籍上の氏名（漢字）
- `{{LEGAL_NAME_KANA}}` 氏名カナ
- `{{DISPLAY_NAME}}` 表示名。推奨: `石田祐太`
- `{{EMAIL}}` Googleメール（ログイン用）
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
- `{{GENDER_FORM_VALUE}}` 性別フォーム。未設定可なら空

## このPRでやらないこと

- アカウント作成
- 本人確認
- 出品・応募・公開
- 秘密・実メール・実電話のコミット
- 案件数・GMV・登録者数の創作
