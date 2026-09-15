# JP WEEK2 INDEX — earn-register-packs-jp-20260916

観測日: 2026-09-15（公開ページの HEAD / 公式ヘルプ。ブラウザ登録はしていない）
状態: **DRAFT-ONLY**
禁止: 秘密の記入、ブラウザ登録、公開、KYC完了、口座登録

## 使い方

1. 現行 Top10（CU-01〜CU-10）が終わるまで、本フォルダは触らない。
2. Top10 の直後から、下の **CU直列** を上から貼る。
3. `thin_site_skip: true` の行はスキップ。いまは 0 件。
4. 各パックの **STOP-AT-KYC** で手を止める。本人確認・Stripe・口座・マイナンバーは出金が必要になるまで進めない。
5. 値はプレースホルダのままコピーし、ローカル台帳で置換する。このPRに実値を足さない。

## 現行 Top10 の直後 — CU直列の推奨

Week1 Top10 の中身はこのフォルダでは再定義しない。番号だけ **CU-11 起算** で続ける。

貼る順は在庫順（01〜08）ではない。AI自動化の売り手（石田祐太 / ユタラボ）との相性、Google登録の通しやすさ、登録時点のKYC摩擦で並べた。

| CU直列 | パック | 優先 | Google登録 | thin_site_skip | 止める場所 | なぜこの順か |
|---|---|---|---|---|---|---|
| CU-11 | [02-workship.md](02-workship.md) | High | PREFER_GOOGLE（SNS。画面でGoogleアイコンを目視） | false | 契約署名・本人確認が出たら止める | Web系業務委託の単価帯が売り物に近い。登録はSNS。KYCは登録直後には出にくい |
| CU-12 | [03-fukugyo-cloud.md](03-fukugyo-cloud.md) | High | PREFER_GOOGLE | false | 本人確認・口座が出たら止める | ワーカー手数料なし。Google / Apple。スカウト型 |
| CU-13 | [01-sokudan.md](01-sokudan.md) | High | PREFER_GOOGLE | false | 審査書類の提出画面で止める | Google / GitHub あり。職歴プロフィール型。書類審査はKYC扱い |
| CU-14 | [04-crowdlinks.md](04-crowdlinks.md) | High | PREFER_GOOGLE | false | 有料会員化・追加書類で止める | CrowdWorks系。Googleあり。規約に実務経験2年の条件。本人が該当するかだけ判断 |
| CU-15 | [05-anycrew.md](05-anycrew.md) | Med-High | PREFER_GOOGLE（主経路） | false | 職務経歴書の提出依頼で止める | 公式が Google / Facebook 登録。書類は一部案件のみ |
| CU-16 | [06-menta.md](06-menta.md) | Med | PREFER_GOOGLE | false | Stripe本人確認・口座の直前 | 教える売り物とユタラボ実録が重なる。出金KYCは後回し |
| CU-17 | [07-street-academy.md](07-street-academy.md) | Med | NOT_OFFERED_OAUTH（Googleメールでメール登録） | false | 顔写真付き証明書の提出画面 | 自己集客10%が本命。OAuthにGoogleは無い。講師KYCは後回し |
| CU-18 | [08-shufti.md](08-shufti.md) | Optional Med | PREFER_GOOGLE | false | 本人確認資料の提出画面 | 在宅ワーク寄りの場。売り物との一致は弱い。Googleは使える |

## 在庫（ファイル順。貼る順ではない）

1. SOKUDAN — `01-sokudan.md`
2. Workship — `02-workship.md`
3. 複業クラウド — `03-fukugyo-cloud.md`
4. CrowdLinks / クラウドリンクス — `04-crowdlinks.md`
5. Anycrew — `05-anycrew.md`
6. MENTA — `06-menta.md`
7. ストアカ — `07-street-academy.md`（自己集客手数料ノート付き）
8. Shufti / シュフティ — `08-shufti.md`（Optional Med）

## 共通プレースホルダ


共通プレースホルダ（実値はローカルの本人台帳だけ。このリポジトリには書かない）:

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


公開してよいURL（秘密ではない）:

- サイト: https://yutalab.dev/
- GitHub: https://github.com/rimone0511
- Autopilot Log: https://github.com/rimone0511/autopilot-log

## thin-site SKIP 判定（2026-09-15）

全8件 `thin_site_skip: false`。公開証拠は「死んでいる」ではなく「生きている」側。

| サイト | 公開証拠 | SKIPしない理由 |
|---|---|---|
| sokudan.work | signup HTTP 200、Google/Facebook ボタンあり | 新規登録面が生きている |
| goworkship.com | signup HTTP 200、公式ヘルプがアカウント作成を案内 | サービス継続 |
| talent.aw-anotherworks.com | HTTP 200、Vercel、2026-09-15 更新 | 複業クラウド個人向けが生きている |
| crowdlinks.jp | worker signup HTTP 200、ヘルプFAQが 2026-08-01 更新 | アプリは生きている。マーケTOPは start.crowdlinks.jp へ飛ぶが死滅ではない |
| app.any-crew.com | HTTP 200、2026-09-15 のオブジェクト | Google/Facebook ログイン面あり |
| menta.work | register HTTP 200、Google OAuth リンクあり | ランサーズ系として継続 |
| street-academy.com | 公式ヘルプが講師手数料・登録を案内。この環境のHTMLはAWS WAFのHuman Verification | WAFは死滅証拠ではない。ヘルプと teach.street-academy.com は生きている |
| app.shufti.jp | signup HTTP 200、Google登録、ヘルプに 2026-07 メンテ告知 | SPAシェルだが更新されている |

## 観測の限界

- 登録フォームの必須項目は、公開ヘルプと第三者解説に依存。画面のラベルが違う場合は画面を正とし、このパックは下書きとして直す。
- Workship の静的HTMLは「SNSで登録」。Googleアイコンのラベルは貼る人が目視する。
- ストアカ公式ヘルプの登録経路は LINE / Facebook / メール。Google OAuth は見当たらない。
- 手数料・規約は公式ページの要約。数字は貼る直前に公式ヘルプで再確認する。

## このPRでやらないこと

- アカウント作成
- 本人確認
- 出品・応募・公開
- 秘密・実メール・実電話のコミット
