> **MAIN Google only.** Public GET does not log in. No OAuth completion.
> **DRAFT_ONLY.** These rows are URL confirmation, not accounts.
> **STOP-KYC.** No identity pages were submitted.
> **No secrets.** Response bodies were not saved as cookies or tokens. CSRF hidden fields from HTML are **not** copied here.
> **No invented fees.** HTTP codes and visible headings / quotes only. Marketing totals are not activity proof.
> **No publish. No signup.** No forms were posted.

# 観測メモ（この PR の公開 GET）

日時: 2026-09-16  
UA: 通常のブラウザ相当。ログイン Cookie なし。  
やったこと: 公式の公開 URL に GET。見出し・リンク・FAQ・案件カードの日付だけ記録。  
やらなかったこと: アカウント作成、OAuth 完走、有料、KYC、応募、出品、企業コンソール、POST。

件数見出し・「登録 35,000 人」・「リモート案件 92%」は **活動証明に使わない**。

先パックの METHOD（PR#12 / PR#21 / PR#30 / PR#33 / PR#34）は本文複製しない。下表は **この著者の GET**。

## Workship

| URL | HTTP | この GET で見えたこと |
|---|---|---|
| https://goworkship.com/ | 200 | タイトル「フリーランス・副業向けマッチングサービス」。見出しに「SNSで登録」 |
| https://goworkship.com/signup | 200 | タイトル「フリーランス登録をする」。`SNSで登録` + `#firebaseui-auth-container`。静的 HTML に Google ボタン文字列は無い（Tag Manager / recaptcha のみ）。メールフォームも同じページ。**CSRF トークンは記録しない** |
| https://goworkship.com/portal/search | 200 | タイトル「フリーランス・業務委託案件」。フィルタ「リモート可」「フルリモートOK」。カード例: 「【基本リモ/週20h～相談可】財務BI導入…」「【一部リモ可】SAP導入…」。件数見出しの数字は活動証明に使わない |
| https://goworkship.com/help/how_to/44 | 200 | 「アカウントを新規登録したい」。SNS のアイコン。確認 URL **24時間** |
| https://goworkship.com/help/agreement/95 | 200 | 前払いオプション。「本人確認が必要です」。手数料は「手数料・利用規約を確認の上」— **％なし → 作らない** |

## SOKUDAN

| URL | HTTP | この GET で見えたこと |
|---|---|---|
| https://sokudan.work/ | 200 | タイトルにフリーランス・副業案件。公開 HTML に案件カード（例 alt: 「【フルリモ／週10h〜】TikTok Shop…」「【週2～】Claude×Figma MCP…」）。埋め込み JSON に `contractType":"outsourcing"` かつ `createdAt` **2026-09-15** のカードあり。FAQ: 人材側「すべて無料でご利用いただけます」。マーケ「92%」は活動証明に使わない。ブログ日付例 2026.09.03 は告知であり件数ではない |
| https://sokudan.work/signup/pro | 200 | 見出し「無料新規登録」。`alt="Google で登録"` → `/users/auth/google?category=signup&usage_type_id=1`。Facebook「推奨」+ LinkedIn / X / GitHub / 「メールで無料登録」もあり。**Google を選ぶ** |
| https://sokudan.work/login | 200 | ログイン面。Google 経路あり（この GET は押していない） |
| https://sokudan.work/pages/terms | 200 | 第4条: 審査に必要な書類の提出を求めることがある。代理人による会員登録は認めない。第10条付近に「手数料の料率」という語 — **％は未記載 → needs_check** |

## Offers

| URL | HTTP | この GET で見えたこと |
|---|---|---|
| https://offers.jp/ | 200 | タイトル「ハイクラスエンジニア**転職**」。ヘッダに `/worker/signup`。メタの「登録35,000人」はマーケ → 活動証明に使わない |
| https://offers.jp/worker/signup | 200 | `data-testid="auth-google"`。「**Google**で登録する」。`/oauth/worker_signup/google`。GitHub / X / LinkedIn / 「メールアドレスで登録する」もあり。**Google を選ぶ**。企業側は使わない |
| https://offers.jp/jobs/engineer/side-job | 200 | タイトル「副業・業務委託可」。カード「【フルリモート】AI×FDE｜…」。公開 HTML の日付文字列に **2026-09-10**（更新日）ほか 2026-08-19〜2026-09-10。時給レンジは **その求人の提示** でありプロフィール単価にコピーしない |
| https://offers.jp/terms | 200 | 第12条 マッチング成功報酬はクライアントが支払う。**％なし → 作らない**。マッチング対象に業務委託と求職の両方 |
| https://offers.jp/signup | **404** | 入口は `/worker/signup` のまま |

## やらない解釈

- FirebaseUI が空に見える ≠ Google が無い。Workship はヘルプが SNS アイコン、signup はコンテナ。**クリック時に Google ラベルを目視**。
- Offers トップが転職コピー ≠ 業務委託が死んでいる。Jobs の日付カードが pass 根拠（PR#12 と同じ種類の手がかり。この GET でも 2026-09-10）。
- 公開 JSON の `workerCount` などはスキルカタログであり GMV ではない。書かない。
