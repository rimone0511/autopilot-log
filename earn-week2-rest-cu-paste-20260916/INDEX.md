# INDEX — Week2-rest CU-23–CU-28

観測日: 2026-09-16 JST（公開 GET。ブラウザ登録はしていない）  
状態: **DRAFT-ONLY**  
禁止: 秘密の記入、ブラウザ登録、公開、KYC完了、有料プラン加入

MASTER INDEX（PR#14）と CU serial INDEX（PR#8）で **Week2 残り = QUEUE B12–B17** が `unknown · no PR` だった。このフォルダがその空き。

貼る順は在庫ファイル名の番号と一致する（JP Week2 の Workship 起算とは違う）。QUEUE の B12→B17 が CU-23→CU-28。

Wave A の `next`（CU-02→CU-10）が全部 `done-draft` になるまで、このフォルダは触らない（PR#3 INDEX / PR#8 と同じ）。

## CU直列（この空き）

| CU直列 | QUEUE | パック | Google登録 | activity_gate | thin_site_skip | 止める場所 |
|---|---|---|---|---|---|---|
| CU-23 | B12 | [01-freelancermap.md](01-freelancermap.md) | **NOT_OFFERED_OAUTH**（公開登録面に Google ボタンなし。メールで登録） | **pass**（`/projects` に 2026-09-15 の `created`） | false | Profile verification / Premium / 応募 |
| CU-24 | B13 | [02-youtrust.md](02-youtrust.md) | **PREFER_GOOGLE**（ヘルプ「Googleアカウント連携」。サインアップURLは LP へ飛ぶ → クリック時にボタン目視） | **needs_check**（ジョブカード日付は未読） | false | 身分証、実名SNSの強制、プロフィール公開、応募 |
| CU-25 | B14 | [03-offers.md](03-offers.md) | **PREFER_GOOGLE**（`/oauth/worker_signup/google`） | **pass**（Jobs 業務委託カード 更新日 2026-09-10） | false | 応募、「話を聞きたい」、有料ブース、身分証 |
| CU-26 | B15 | [04-ai-crowdworks.md](04-ai-crowdworks.md) | **EMAIL_ONLY**（公開面に Google ボタン未確認。メール登録 URL は 200） | **needs_check**（仕事一覧は「読み込み中」） | false | 事前登録は閉じた。案件ボードが見えるまで登録しない。KYC・応募 |
| CU-27 | B16 | [05-skill-shift.md](05-skill-shift.md) | **NOT_OFFERED_OAUTH**（公開 JS に Google 登録ボタンなし。メール必須。Facebook は新規作成しない） | **pass**（公開 `/api/jobs` の `created_at` 2026-09-08〜14） | false | 身分証、現場のみの行への応募、企業コンソール |
| CU-28 | B17 | [06-itpropartners.md](06-itpropartners.md) | **NOT_OFFERED_OAUTH**（`/register` 初面は職種選択。Google なし） | **pass**（案件カード 最終更新日 2026/09/08） | false | 面談で身分証、エージェント契約、応募 |

`activity_gate=pass` でもこのパックは下書きまで。公開・応募はしない。

## 在庫（ファイル順 = 貼る順）

1. Freelancermap — `01-freelancermap.md`
2. YOUTRUST — `02-youtrust.md`
3. Offers — `03-offers.md`
4. AI CrowdWorks — `04-ai-crowdworks.md`
5. Skill Shift — `05-skill-shift.md`
6. ITプロパートナーズ — `06-itpropartners.md`

## 共通プレースホルダ

実値はローカルの本人台帳だけ。このリポジトリには書かない。

- `{{LEGAL_NAME_KANJI}}` 戸籍上の氏名（漢字）
- `{{LEGAL_NAME_KANA}}` 氏名カナ
- `{{DISPLAY_NAME}}` 表示名。推奨: `石田祐太`
- `{{FULL_LEGAL_NAME}}` ローマ字フルネーム（Freelancermap 等 EN 机）
- `{{EMAIL}}` Googleメール（ログイン用）
- `{{PHONE}}` 日本の携帯電話
- `{{POSTAL_CODE}}` 郵便番号
- `{{PREFECTURE}}` 都道府県
- `{{CITY}}` 市区町村以下
- `{{COUNTRY}}` 国。正直に Japan。偽の US/EU 住所は作らない
- `{{TIMEZONE}}` 例: Asia/Tokyo
- `{{BIRTH_YEAR}}` / `{{BIRTH_MONTH}}` / `{{BIRTH_DAY}}` 生年月日
- `{{PORTFOLIO_URL}}` 推奨公開: `https://yutalab.dev/`
- `{{GITHUB_URL}}` 推奨公開: `https://github.com/rimone0511`
- `{{GITHUB_REPO_AUTOPILOT}}` `https://github.com/rimone0511/autopilot-log`
- `{{PHOTO_LOCAL_PATH}}` 顔写真のローカルパス（コミット禁止）
- `{{INVITE_CODE}}` 招待コード。無ければ空
- `{{YEARS_AUTOMATION_PUBLIC}}` 公開実録の期間だけ。未確認なら空
- `{{HOURLY_RATE_EUR}}` / `{{DAILY_RATE_EUR}}` レート。未確認なら空。このPRに実額を書かない
- `{{PASSWORD_DO_NOT_STORE}}` メール登録パス。リポジトリに書かない

公開してよいURL（秘密ではない）:

- サイト: https://yutalab.dev/
- GitHub: https://github.com/rimone0511
- Autopilot Log: https://github.com/rimone0511/autopilot-log

## thin-site SKIP（2026-09-16）

全6件 `thin_site_skip: false`。詳細は [SKIP.md](SKIP.md)。この回に SKIP した机は **0**。

QUEUE の `https://skillshift.jp/` は DNS 失敗。机が死んでいるのではなく、公式ドメインが `https://www.skill-shift.com/`。SKIP にしない。

## 観測の限界

- 登録フォームの必須項目は、公開ヘルプと公開 HTML に依存。画面のラベルが違う場合は画面を正とする。
- SPA / WAF / JS 必須の面は、カードが読めなければ `needs_check` のまま。数字を埋めない。
- Freelancermap のマーケ「14,600 open projects」等は活動証明に使わない。使ったのは `/projects` 埋め込み JSON の `created` タイムスタンプ。
- Skill Shift の `pagination.total` は書かない（PR#12 と同じ）。

## このPRでやらないこと

- アカウント作成
- 本人確認
- 出品・応募・公開
- 秘密・実メール・実電話のコミット
