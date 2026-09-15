# 観測メモ（方法だけ）

日時: 2026-09-16  
UA: 通常のブラウザ相当。ログイン Cookie なし。  
やったこと: 公式の公開 URL に GET。HTML / 公式ヘルプに出た見出し・リンク・ラベルだけ記録。  
やらなかったこと: アカウント作成、OAuth 完走、仮登録 POST、有料（Craudia PRO）、KYC、自撮り、応募、スキル出品、パスワード入力。

件数・「○万人」・PRO LP の「時給5,000円以上」例は活動証明に使わない。  
手数料％は公式ページに数字があるときだけ **cited**。無ければ **needs_check**。  
プロフィール字数は公式ヘルプに数字があるときだけ **cited**。自己紹介の字数は FAQ に無い → **needs_check** + 測済みフェンス。  
スキル出品タイトル「25文字以内」は出品ガイドに出るが、このパックは出品しない。

| URL | HTTP (this env) | メモ |
|---|---|---|
| https://www.craudia.com/ | **200** | 「会員登録(無料)」。ワーカーを探す / スキルを探す |
| https://www.craudia.com/worker | **200** | 受注は「公募に応募」「スキルを出品」「オファーを待つ（PRO）」の3系統。このパックはどれも開始しない |
| https://www.craudia.com/app/auth/register-temp | **200** | STEP1 仮登録。メール欄 + 「無料で会員登録する（仮登録）」。SNS: Twitter `auth=1` / Facebook `auth=2` / **Google `auth=3`** / Yahoo `auth=4`。連携先は i2i ID。reCAPTCHA あり。**POST していない** |
| https://www.craudia.com/signup | **404** | 使わない |
| https://www.craudia.com/app/signup | **404** | 使わない |
| https://www.craudia.com/login | **200** → `app.craudia.com/auth/login-form` | メール（i2iID）+ パスワード。同じ Google ボタン |
| https://www.craudia.com/app/faq/contents/151 | **200** | 登録: PCメール **または** Twitter / facebook / Google / Yahoo! |
| https://www.craudia.com/app/faq/contents/103 | **200** | 登録に必要なもの = 連絡の取れる PC メール。**出金**時に本人確認 |
| https://www.craudia.com/app/faq/contents/93 | **200** | マイページ設定 → 本人確認。顔付き公的書類 + **自撮り必須**。目安 3営業日 |
| https://www.craudia.com/app/faq/contents/72 | **200** | 採用時のみ手数料。**5万円まで一律 15%**。詳細は手数料ガイドへ |
| https://www.craudia.com/app/guide/crowdsourcing-price | **200** | クライアント 0円。ワーカー 3〜15%。階段: 〜5万 15% / 5万1円〜10万 10% / 10万1円〜100万 5% / 100万1円〜 3%。時間制 **一律 10%**。税込。四捨五入 |
| https://www.craudia.com/app/guide/skill-price | **200** | スキル販売者も同じ階段。**このパックは出品しない**ので「今払う額」にしない |
| https://www.craudia.com/faq/contents/164 | **200** | 直接取引禁止 |
| https://www.craudia.com/app/faq/contents/140 | **200** | 直接取引・直接連絡の勧誘禁止。サービス外連絡申請はクライアント（案件）またはスキル出品者 |
| https://www.craudia.com/app/faq/contents/89 | **200** | 参加申請 / 「納品する」。**送らない** |
| https://www.craudia.com/app/faq/contents/175 | **200** | スキル出品 = マイページ「スキルを出品する」。ガイド https://app.craudia.com/guide/service/sell |
| https://www.craudia.com/app/guide/service/sell | **200** | タイトル **25文字以内**。ステップ8 **公開**。**開いて公開しない** |
| https://www.craudia.com/app/faq/contents/92 | **200** | プロフィール編集 = マイページ設定メニュー「プロフィール編集」 |
| https://www.craudia.com/app/faq/contents/78 | **200** | ポートフォリオは公開可能な実績。字数なし |
| https://www.craudia.com/app/faq/contents/47 | **200** | 満18歳以上。規約第4条 |
| https://www.craudia.com/app/faq/contents/156 | **200** | 電話認証。失敗時に本人確認を勧める。UI `mypage/setting/person` |
| https://www.craudia.com/app/faq/contents/39 | **200** | 出金振込 **一律 300円**。詳細はログイン後。**出金しない** |
| https://www.craudia.com/app/faq/contents/110 | **200** | 出金 = マイページ＞入出金管理＞振込依頼。**開かない** |
| https://www.craudia.com/app/faq/contents/66 | **200** | 仮払い（エスクロー）。取引しないので触れない |
| https://www.craudia.com/app/agreement | **200** | 運営: 株式会社エムフロ。第10条 登録無料・ワーカー 3〜15%。第12条4–5 直接取引禁止・違約金 |
| https://www.craudia.com/project_guideline | **200** | 連絡先投稿・指定口座・常駐・ステマ・いいね依頼などの NG |
| https://www.craudia.com/app/guide/crowd-sourcing/worker | **200** | 応募とスキル出品の二系統。どちらもこのパックの外 |
| https://www.craudia.com/app/guide/new-user | **200** | 報酬はクラウディア経由。手数料差引 |
| https://www.craudia.com/app/privacy | **200** | 個人情報保護方針 |
| https://www.craudia.com/app/tokushou | **200** | 特定商取引法 |
| https://www.craudia.com/app/lp/professional | **200** | Craudia PRO LP。例の時給はマーケ。**登録しない・買わない** |
| https://www.craudia.com/app/lp/skill | **200** | スキル LP。出品導線。**入らない** |
| https://www.craudia.com/app/user_list | **200** SPA シェル | meta: 得意種別（ライティング系、デザイン・クリエイティブ系、**プログラム・開発系**、事務系、その他） |
| https://www.craudia.com/mypage/setting/person | 未ログイン GET は **トップへ** | FAQ が URL を出す。**STOP 入口**。上げない |

`thin_site_skip: false`。FAQ・手数料ガイド・register-temp が 200。Google 登録を FAQ 151 と登録面のボタンが明記。
