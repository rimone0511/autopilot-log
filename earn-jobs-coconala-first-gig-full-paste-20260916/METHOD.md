# 観測メモ（方法だけ）

日時: 2026-09-16  
UA: `curl` + 通常ブラウザ相当の GET。ログイン Cookie なし。  
やったこと: 公式の公開 URL に GET。HTML / 公式ニュース / ココナラマグに出た見出し・リンク・ラベルだけ記録。  
やらなかったこと: 会員登録、OAuth 完走、サービス出品 POST、公開、KYC、口座、見積もり送信、パスワード入力。

件数・「○万件」・カテゴリ相場表は活動証明に使わない（ベンダー UI）。  
手数料％は公式ヘルプ本文をこの環境で読めていない。価格欄に書かない。  
字数は公式ニュースに数字があるときだけ **cited**。FAQ/オプション字数は第三者 → **needs_check** + 測済みフェンス。

| URL | HTTP (this env) | メモ |
|---|---|---|
| https://coconala.com/ | **200** | ホーム |
| https://coconala.com/categories/ | **200** | カテゴリ一覧。IT → 業務自動化・効率化支援 → API連携・開発 を確認 |
| https://coconala.com/categories/11 | **200** | 大: IT相談・システム開発 |
| https://coconala.com/categories/230 | **200** | 中: 業務自動化・効率化支援。n8n を題名に含む出品あり。相場表は使わない |
| https://coconala.com/categories/230/739 | **200** | 小: API連携・開発。n8n 連携の出品あり |
| https://coconala.com/services/3695231 | **200** | 公開 n8n 出品の存在確認のみ。文面はコピーしない |
| https://coconala.com/services/add | **202** | 公式マグが新規出品 URL と書く。未ログイン |
| https://coconala.com/mypage/services_lists | **202** | 出品一覧。未ログイン |
| https://coconala.com/news/170 | **200** | タイトル最大25字・ます固定・キャッチ最大30字 |
| https://coconala.com/news/1372 | **200** | 2026-09-01: サービス内容 1500字、お願い 1000字、推奨 600/150、新規は画像1枚以上 |
| https://coconala.com/news/1137 | **200** | ビデオチャット手数料改定。この出品ではビデオを使わない |
| https://mag.coconala.com/articles/knowhow-the-basics-of-service-pages | **200** | 完結取引、提供形式、オプション必須禁止、見積もり必須は推奨しない |
| https://help.coconala.com/hc/ja/articles/230180287 | **403** | 販売時の手数料。Cloudflare。料率は貼る直前に人が読む |

ログイン必須の「書き方ガイド」（ニュース 1372 が案内）は未取得。見出し構成は公開マグ + 通説の ■ 見出し。
