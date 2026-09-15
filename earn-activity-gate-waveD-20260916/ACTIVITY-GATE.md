# ACTIVITY-GATE — Wave D Fit-Med desks

観測日: **2026-09-16 JST**  
方法: 公開 URL の GET。ログインなし。登録なし。有料なし。  
フォルダ: `earn-activity-gate-waveD-20260916/`

QUEUE の売り手入口と、今回実際に開いた公開 URL が違う場合は **開いた URL を正** とし、QUEUE 側はメモする。

数値を作らない。公式が出していない件数・GMV・成約率・「月収」を書かない。`unknown` は不合格（登録しない）。

---

## Summary

| # | 机 | 公式（開いた URL） | 活動の目視 | Google | 無料の売り手入口 | Gate |
|---|---|---|---|---|---|---|
| 1 | SKIMA | https://skima.jp/ | トップに価格付きコミッション／opt。`/guide/sell` に出品手順。一覧に「新着」コピー | `/entry` に「Googleで登録」 | `/entry` メールまたは SNS。出品無料のガイド | **pass** |
| 2 | Payhip | ヘルプ（トップはこのIPで 403） | 公式ヘルプ: デジタル商品＋ **Invisible / Unlisted / Visible**。Visibility 記事の最終更新 **November 6, 2025** | 未確認 | 売り手はヘルプ上「Add Digital Product」。接続は PayPal/Stripe | **pass**（店頭は未読。下書き=Invisible） |
| 3 | Ko-fi | https://ko-fi.com/ | トップ: tips / memberships / shop。クリエイター例。FAQ「0–5% fee」「no monthly fee」。`/shop` はこのIPで CF | 未確認 | 「Create a free account」。支払いは PayPal/Stripe 直接 | **pass** |
| 4 | Dribbble | https://dribbble.com/services | 価格付きサービスカード。例: Product Design (Web, Mobile, Ai Agents)。`/jobs` は求人（使わない） | サービス面に Google サインイン用 JS | `/signup/new` 200 | **pass**（Services のみ） |
| 5 | Fastwork | https://fastwork.co/en | `/en/ai-automation` に n8n / make.com のパック説明。開始価格表示あり（マーケ合計ではない） | 公開HTMLでは未確認 | 売り手 signup URL はこの環境で 404（SPA）。トップにフリーランス本人確認コピー | **pass**（オンラインカテゴリのみ。雇前KYCで停止） |
| 6 | Truelancer | https://www.truelancer.com/freelance-jobs | 見出し「September 2026」。カード例「Posted: 2 hours ago」。低額カードと開発カードが混在 | signup はこのIPで Vercel 429 | 仕事ボードは公開。登録面は人が辿る | **pass**（スパムだけではない） |
| 7 | Twine | https://www.twine.net/jobs | 「Jobs posted directly onto the Twine platform」＋ Remote「Posted 4 days ago」。下段は Ari の他社求人 | `/signup`。状態に Google OAuth | Sign Up to Twine。完走していない | **pass**（Ari は使わない） |
| 8 | ワークシフト | https://workshift-sol.com/ | トップに案件カード。例 公開日 **2026-09-11**。規約改定 **2026年4月11日**。`/job/search` は 404（正: `/jobs/search`） | 未確認（メール／FB／LinkedIn／GitHub） | `/registration/mail_start`「completely free」 | **pass**（現地カードは応募しない） |
| 9 | ママワークス | https://mamaworks.jp/ | 在宅カード。期間例 **2026/09/09**、**2026/09/11**、**2026/09/14**。SEO／SNS 制作あり | 未確認 | `/entry` メール仮登録 | **pass**（応募型。出品カタログではない） |
| 10 | 99designs | https://99designs.com/how-it-works | 机は生きている。Hire a designer と contest が並ぶ。トップはコンテスト寄り | 未確認 | Become a designer / Designers | **fail-thin** |
| 11 | シュフティ | https://app.shufti.jp/jobs/search | 検索は SPA 空。ヘルプに「2026年シルバーウィークの営業」「【9/11】生成AI入門」。仕事カード未読 | パックは Google。このHTMLでは未描画 | `/signup` 200 シェル | **needs_check** |
| 12 | Wellfound | https://wellfound.com/ | スタートアップ求人＋AI採用。候補者無料・求人投稿無料の FAQ。ギグ出品なし | 求人面に Sign up 文字列 | 人材は求職プロフィール。売り手机ではない | **fail-aggregator** |

`fail-closed`: **0**  
`fail-local` / `fail-identity`: **0**（そのクラスは12に入れていない）  
`blocked_paid_plan`: **0**（公開面では課金必須を見ていない）

---

## 机ごとの証拠（短文）

マーケの「○万人／○件」は活動証明に使わない。以下は **この観測で画面または公式 HTML に出たもの**。

### SKIMA — pass

- https://skima.jp/ に価格付きカード。例: 「イラスト制作します！ ¥5,000～」「1枚絵イラスト制作 ¥20,000～」。
- https://skima.jp/guide/sell : イラスト特化のオーダーメイド。コミッション／opt。出品完了で SKIMA 上に表示。受付休止可。手数料は販売総額に応ずる（率は書かない）。
- 新規登録 https://skima.jp/entry 「Googleで登録」「メールアドレスで登録」。
- カードの「○時間前」は未確認。カタログが並び、ガイドに新着表示があるので活動ありとする。

### Payhip — pass

- https://payhip.com/ と `/discover` はこのIPで Cloudflare。店頭カードは未読。
- https://help.payhip.com/article/164-how-to-sell-your-first-product-on-payhip : デジタル／物理／サブスク／コーチ／コース。先に PayPal または Stripe。
- デジタル商品は **Invisible**（自分だけ）→ Unlisted（リンク）→ Visible。コースは Draft / Preorder / Published。https://help.payhip.com/article/351-product-visibility Last updated **November 6, 2025**。
- 登録はしていない。支払接続・KYC は停止。商品は Invisible のまま。

### Ko-fi — pass

- WebFetch の https://ko-fi.com/ : tips・memberships・「sell your work」。FAQ: 月額課金なし、手数料 0–5%、PayPal または Stripe へ直接。
- クリエイター名の例がトップに並ぶ（支持者数はマーケなので活動件数に使わない）。
- curl の `/shop` `/pricing` と help.ko-fi.com はこのIPで Cloudflare。店の商品グリッドは未読。トップ本文で机は生きている。

### Dribbble Services — pass

- https://dribbble.com/services に価格付きパック。例: Website Design + Development、Product Design (Web, Mobile, Ai Agents) $12,000、Custom Vector Illustration $150。
- https://dribbble.com/jobs は求人ボード（「Posted about 6 hours ago」など）。**活動の証明には使えるが、売り手路ではない。** QUEUE は Services。
- `/signup/new` 200。Google ボタンはこの観測では未クリック。

### Fastwork — pass

- https://fastwork.co/en : TH/SEA のフリーランス机。オンラインと対面（マッサージ、家政など）が混在。対面カテゴリは触らない。
- https://fastwork.co/en/ai-automation : 「AI Automation / n8n / make.com」。開始価格の表示あり（見積の下限であり GMV ではない）。
- コピー: フリーランスは雇う前にシステム上で本人確認。**登録直後でなくても、確認画面が出たら停止。**
- `/en/start-earning` `/en/signup` はこの環境で 404（SPA）。売り手入口は人がトップから辿る。

### Truelancer — pass

- https://www.truelancer.com/freelance-jobs 見出し「Best Freelance Jobs Online in **September 2026**」。
- カード例: Video Editor「Posted: **2 hours ago**」、CAD「3 hours ago」、Next.js Developer「12 hours ago」。$5 固定の短文カードもある。**複製だけが本線、ではない。**
- 詐欺注意の公式コピーあり（プラットフォーム外のデポジット要求）。外払いしない。
- トップの「2M+ Freelancers」はマーケ。使わない。signup は Vercel 429。

### Twine — pass

- https://www.twine.net/jobs : 「Jobs posted directly onto the Twine platform」。例: Old School Adventure Game、Remote、$2,500、「Posted **4 days ago**」。Character Design も Remote。
- 同ページ下段は Ari（「searches hundreds of sources」「company careers pages」）。**寄せ集め路。使わない。** 直投稿があるので机全体は aggregator にしない。
- `/signup` 「Sign Up to Twine」。フロント状態に Google OAuth。完走していない。

### ワークシフト — pass

- https://workshift-sol.com/ : 海外人材マッチング。コピー「アクセスの難しい日本企業の案件にオンラインで応募できます。」IT・デザイン枠あり。
- トップカード例: `/jobs/view/13758` 公開日 **2026-09-11**（SIAL Paris 現地通訳。**応募しない**）、`/jobs/view/13757` モンゴル現地営業、`/jobs/view/13756` スリランカ現地営業。現地カードがあっても、机全体はシフトバイト専用ではない。
- 会員登録 https://workshift-sol.com/registration/mail_start : Email または Facebook。無料。ログインに LinkedIn / GitHub。**Google ボタンは未確認。**
- 利用規約 https://workshift-sol.com/pages/term : **2026年4月11日改定**。
- `/job/search` は 404。検索は `/jobs/search`（CAPTCHA あり。一覧本文はこの観測では未描画）。

### ママワークス — pass

- https://mamaworks.jp/ 在宅・業務委託カード。例: SEOライター期間 **2026/09/09〜2027/09/30**、SNS運用・クリエイティブ **2026/09/09〜**、オンライン商談 **2026/09/11〜**、コール **2026/09/14〜2026/09/25**。
- フローは会員登録 → 求人に応募。**カタログ出品ではない。** 制作・SNS カードがあるので本線とゼロではない。
- https://mamaworks.jp/entry メール仮登録。`/register` はこの観測で 500。入口は `/entry`。
- 応募・面接はしない。プロフィール下書きまで。

### 99designs — fail-thin

- 机は生きている。https://99designs.com/how-it-works で 1-to-1 と contest が両方ある。
- トップと How it works の主語はデザインコンテスト／ロゴ。自動化・デジタル配布の置き机ではない。
- 閉鎖でも寄せ集めでも現地でもない。**薄い（本線不一致）** で SKIP。

### シュフティ — needs_check

- https://www.shufti.jp/ と https://app.shufti.jp/jobs/search は SPA シェル。仕事名は未読。
- https://help.shufti.jp/ は生きている。索引に「2026年シルバーウィークの営業について」「【9/11】ゼロから始める生成AI入門」。本人確認のヘルプ項目あり（**提出しない**）。
- 製品は在宅タスク寄り。カードを見ていないので SKIP thin にしない。JP Wave B と同じ `needs_check`。
- `/signup` 200。Google はこの HTML では未描画。

### Wellfound — fail-aggregator

- https://wellfound.com/ : スタートアップの求人・AI 採用。FAQ「Creating a profile and applying to jobs is always free for candidates」「Post jobs free」。
- `/jobs` タイトル「Find Startup Jobs」。売り手サービス／ギグカタログは無い。
- LinkedIn Jobs と同じクラス。SKIP aggregators。

---

## 認証・停止（全机共通）

1. MAIN Google のみ。別アカウントを作らない。Google が無ければ MAIN Google のメール。
2. パスポート／免許／マイナンバー／顔写真／口座が出たら **アップロードせず停止**。
3. PayPal / Stripe 接続で身分証明が出たら同じ。接続しない。
4. 有料会員・優先掲載・審査スキップは買わない。
5. プロフィール公開・出品公開・応募・コンテスト投稿はしない。
6. 公開一覧が読めなければ `needs_check` のまま。数字を埋めない。

## オペレーター順（このゲートのあと）

1. **プロダクト化 pass**: SKIMA → Payhip（Invisible）→ Ko-fi → Dribbble Services
2. **マーケット pass**: Fastwork（雇前KYCで停止）→ Truelancer → Twine（Ari 以外）
3. **JP マッチング pass**: ワークシフト（メール・現地カード回避）→ ママワークス（応募しない）
4. **needs_check**: シュフティ — 人が仕事一覧の日付を1画面
5. **SKIP**: 99designs、Wellfound
