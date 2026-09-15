# 観測メモ（方法だけ）

日時: 2026-09-16  
UA: 通常のブラウザ相当。ログイン Cookie なし。

やったこと: 公式の公開 URL に GET。HTML に出た見出し・リンク・FAQ だけ記録。  
やらなかったこと: アカウント作成、OAuth 完走、有料、KYC、応募、出品。

件数・「○万人」・ホームページのマーケ％（例: SOKUDAN「リモート案件 92%」）は活動証明に使わない。

| URL | HTTP | メモ |
|---|---|---|
| https://sokudan.work/ | 200 | 案件カードあり。FAQ「すべて無料」。Google / Facebook / GitHub / X / LinkedIn / メール |
| https://sokudan.work/signup/pro | 200 | 「無料新規登録」。`/users/auth/google?category=signup&usage_type_id=1`（alt「Google で登録」） |
| https://sokudan.work/login | 200 | 「Google で ログイン」 |
| https://sokudan.work/pages/terms | 200 | CAMELORS。第4条に審査書類 |
| https://sokudan.work/pages/faq | 200 | この環境では Notion シェル。FAQ本文はトップHTML側を正とする |
| https://talent.aw-anotherworks.com/ | 200 | タイトルのみ。SPA。Googleボタン未描画 |
| https://cl.aw-anotherworks.com/user_tos | 200 | 事業者の利用料金条。ワーカー手数料の％は未記載 |
| https://app.any-crew.com/ | 200 | 「FacebookかGoogle」「Googleでログイン」。人材FAQ「一切費用はかかりません」。`/offers` `/login` は SPA 429B |
| https://www.any-crew.com/terms | 200 | 基本無料。求人事業者の有料プラン条あり |
| https://menta.work/ | 200 | 無料登録。メンター募集導線 |
| https://menta.work/index.php/register/choose | 200 | 「Googleアカウントで登録する」→ `/index.php/oauth/google`（同日の活動ゲートは登録面 WAF の記録あり。環境差） |
| https://menta.work/tokutei | 200 | メンター手数料20％税別（15+5）。振込都度300円 |
| https://intercom.help/mentajp/ja/articles/3025561 | 200 | 出金に Stripe 本人確認 |
| https://intercom.help/mentajp/ja/articles/3025582 | 200 | 運用案内は「手数料22%（20%+消費税10%）」— 特商法の20％税別と併記。貼る直前に再読 |
| https://www.street-academy.com/ | 405 | AWS WAF Human Verification |
| https://www.street-academy.com/register | 405 | 同上 |
| https://www.street-academy.com/teach | 405 | 同上 |
| https://support.street-academy.com/hc/ja/articles/200700579 | 403 | Cloudflare challenge。手数料％はこのGETでは未取得 |
| https://teach.street-academy.com/ | 200 | 講師向けメディア。登録フォームではない |
