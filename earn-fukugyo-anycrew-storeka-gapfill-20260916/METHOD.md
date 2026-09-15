# 観測メモ（方法だけ）

日時: 2026-09-16 JST（GET は 2026-09-15 20:1x UTC）  
UA: 通常のブラウザ相当。ログイン Cookie なし。

やったこと: 公式の公開 URL に GET。HTML / 公開 JS ラベル / 公式 `/fee` に出た見出し・数字だけ記録。  
やらなかったこと: アカウント作成、OAuth 完走、フォーム送信、有料、KYC、応募、出品、パスワード入力。

件数・「○万人」・カテゴリ件数（例: オンライン「すべてのカテゴリー (37,014)」）は活動証明に使わない。  
手数料％は公式ページに数字があるときだけ **cited**。WAF で本文未取得なら **needs_check**。創作しない。

| URL | HTTP | メモ |
|---|---|---|
| https://talent.aw-anotherworks.com/ | 200 | SPA シェル。案件日付なし |
| https://talent.aw-anotherworks.com/sign_up | 200 | タイトル「新規登録」。静的 HTML にボタン未描画 |
| https://talent.aw-anotherworks.com/login | 200 | タイトル「サインイン」 |
| https://talent.aw-anotherworks.com/_next/static/chunks/2ft1bogak3uo6.js | 200 | 公開 JS。`signInGoogle` / ラベル「Googleでサインイン」。Apple / Facebook も同ファイル |
| https://talent.aw-anotherworks.com/projects/91374 | 200 | タイトル「法人SNS運用ディレクター募集」。本文はローダー |
| https://talent.aw-anotherworks.com/signup | 404 | `/sign_up` が正 |
| https://cl.aw-anotherworks.com/user_tos | 200 | 第2.1条1 タレントは無料。第3.2条は事業者プラン料金（％なし） |
| https://anotherworks.co.jp/user_privacy | 200 | 会社プライバシー。本文はシェル寄り |
| https://help.aw-anotherworks.com/ | DNS fail | 使わない |
| https://app.any-crew.com/ | 200 | 「Googleでログイン」「一切費用はかかりません」。表示範囲は非公開／公開 |
| https://app.any-crew.com/offers | 200 | React 空シェル 429B。カード未読 |
| https://www.any-crew.com/terms | 200 | 第5条 基本無料。求人事業者の有料プラン |
| https://www.any-crew.com/privacy | 200 | 氏名・メール・職歴・生年月日等 |
| https://www.any-crew.com/faq | 404 | FAQ はアプリトップを正とする |
| https://www.street-academy.com/ | 200 | 先行パックの www **405 WAF は、この GET では再現せず** |
| https://www.street-academy.com/register | 200 | LINE / Facebook / 「メールアドレスで登録」。Google ボタン無し |
| https://www.street-academy.com/teach | 200 | 「無料ではじめられる」。本人確認書類は先生活動に必要、と画面 |
| https://www.street-academy.com/fee | 200 | 自己集客 10% / 送客 30%（対面 20%）/ リピート 10%。登録費・月額 0 円 |
| https://www.street-academy.com/online/all | 200 | 公開講座カード。開催日フィルタに **2026-09-16** 以降 |
| https://www.street-academy.com/myclass/99028?sessiondetailid=22764089 | **405** | AWS WAF Human Verification。**needs_check**（一覧は読めた。詳細は未読） |
| https://support.street-academy.com/hc/ja/articles/200700579 | **403** | Cloudflare challenge。ヘルプ本文 **needs_check**。料率は `/fee` を正とする |
| https://support.street-academy.com/hc/ja | **403** | 同上 |
| https://teach.street-academy.com/ | 200 | 講師メディア。登録フォームではない |

WAF / Cloudflare で開けなかった URL を pass の根拠にしない。ストアカ www が 200 でも、個別 `myclass` とヘルプは未読のまま。
