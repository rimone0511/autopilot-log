# 観測メモ（方法だけ）

日時: 2026-09-16  
UA: 通常のブラウザ相当。ログイン Cookie なし。  
やったこと: 公式の公開 URL に GET。HTML / 公式ヘルプに出た見出し・リンク・ラベルだけ記録。  
やらなかったこと: アカウント作成、OAuth 完走、有料（Contra Pro）、KYC、チケット発行完了、応募、パスワード入力。

件数・「○万人」・Contra pricing の `$100K+ earned` 引用は活動証明に使わない。  
手数料％は公式ページに数字があるときだけ **cited**。無ければ **needs_check**。  
プロフィール字数は公式ヘルプに数字があるときだけ **cited**（Contra bio = 400）。TimeTicket 字数はヘルプに無い → **needs_check** + 測済みフェンス。

| URL | HTTP (this env) | メモ |
|---|---|---|
| https://www.timeticket.jp/ | **202** 0 bytes（curl）。WebFetch は本文あり | トップ特徴「誰でも無料でチケット発行」「会員登録料・月会費はかかりません」。ランキング期間 2026/09/09〜09/16。死滅ではない |
| https://www.timeticket.jp/categories/ | **202** 0 bytes。WebFetch 本文あり | `IT/プログラミング` 配下に `エンジニアのメンタリング` / `その他IT/プログラミング` / `AI/機械学習/ディープラーニング` |
| https://www.timeticket.jp/terms | **202** 0 bytes。WebFetch 本文あり | 第8条1: プロフィールは設定を変えない限り公開。第9条4: 複数会員登録禁止 |
| https://www.timeticket.jp/privacy | **200** | 本文あり。KYC 提出先の参照用 |
| https://www.timeticket.jp/users/sign_up | **202** 0 bytes | Google ボタンの有無は **needs_check**（目視）。EMAIL = MAIN Gmail を既定にする |
| https://www.timeticket.jp/users/sign_in | **202** 0 bytes | 同上 |
| https://www.timeticket.jp/users/identifications/edit | **202** 0 bytes | ヘルプ 19398 がこの URL を出す。未ログイン空は想定内。**STOP 入口** |
| https://help.timeticket.jp/articles/19374 | **200** | 通常チケット。形式 = 対面 / オンライン / 電話 / **メッセージ**。価格「カテゴリ最低〜1,000,000円」。発行完了ボタン名あり |
| https://help.timeticket.jp/articles/19386 | **200** | ホスト手数料（2025-08-01 以降の購入申込）: 5万以下 25%+税 / 5–10万 20%+税 / 10万超 15%+税 |
| https://help.timeticket.jp/articles/19387 | **200** | 売る流れ。承認後はダイレクトメッセージ。このパックは発行完了前に止まる |
| https://help.timeticket.jp/articles/19398 | **200** | 本人確認資料。マイナは裏面（個人番号）提出お控え。国際免許不可 |
| https://help.timeticket.jp/articles/19400 | **200** | ホスト禁止: 中抜き・現金・連絡先・同一内容の複数発行 |
| https://help.timeticket.jp/articles/19461 | **200** | 最低価格。`IT/プログラミング` は ¥500（時間単価30分 / 定価とも） |
| https://help.timeticket.jp/articles/113228 | **200** | **電話相談チケット**。アプリ通話。対象カテゴリに IT は無い。**作らない** |
| https://help.timeticket.jp/articles/19376 | **200** | 出金。口座登録 URL と振込手数料 300円。**開かない** |
| https://contra.com/ | **200** | Independent / Hire の分岐はオンボーディングヘルプを正とする |
| https://contra.com/how-it-works/independents | **200** | FAQ: profile is free。Pro は premium features。commission-free の文言あり |
| https://contra.com/pricing | **200** | Join / Get started for free。Pro `$29 / month` または `$199 / year`。このパックは買わない |
| https://contra.com/policies/terms | **200** | Direct engagement。Rate Limits and Automated Outreach（複数アカウント・自動ツール禁止） |
| https://contra.com/independent/wallet | **200** 公開シェル | `googleSigninClientId` がフロントに出る（PREFER_GOOGLE の傍証）。**Add account しない** |
| https://help.contra.com/en/articles/9322381-onboarding-and-completing-your-profile | **200** | Share work。Free **or** Pro。Discoverable 完成に wallet を含む |
| https://help.contra.com/en/articles/9322675-writing-your-one-liner-on-contra | **200** | one-liner は brief。**字数数字なし** → needs_check |
| https://help.contra.com/en/articles/9322626-bios-on-contra | **200** | 「there is a **400-character** limit」 |
| https://help.contra.com/en/articles/9322955-how-to-verify-your-identity-on-contra | **200** | Wallet → Add account → 発行国 → Persona |
| https://help.contra.com/en/articles/9322950-your-contra-wallet | **200** | Add an account。ID 発行国。パートナーサイトで ID |
| https://help.contra.com/en/articles/9322763-paid-projects | **200** | Non-Pro 手数料表（$2…$29）。このパックは請求しないので「今払う額」にしない |

TimeTicket の www がこの環境で 202 空でも、help.timeticket.jp が 200 でカテゴリ WebFetch が生きているので **thin_site_skip: false**。signup の Google 有無だけ人/CU が 1 画面確認する。
