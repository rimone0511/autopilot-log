# ACTIVITY-GATE — Wave D-early desks D01–D10

観測日: **2026-09-16 JST**  
方法: 公開 URL の GET。ログインなし。登録なし。有料なし。  
フォルダ: `earn-activity-gate-wave-d-early-20260916/`

QUEUE の売り手入口と、今回実際に開いた公開 URL が違う場合は **開いた URL を正** とし、QUEUE 側はメモする。

数値を作らない。公式が出していない件数・GMV・成約率・「月収」を書かない。`unknown` は不合格（登録しない）。

## チェックリスト（コピー元）

各机の [records/](records/) は次の欄だけ埋める。観測テキスト以外を足さない。

```
signup_open:
fee_page:
open_jobs_heuristic:
last_blog_news:
fit_still_ok:
gate_result: alive | thin | dead | needs_check
action:
```

---

## Summary

| # | 机 | 公式（開いた URL） | signup_open | 活動の目視 | Gate |
|---|---|---|---|---|---|
| D01 | Shufti | https://app.shufti.jp/ | `/signup` 200 シェル | 仕事検索は SPA 空。ヘルプに 2026 シルバーウィーク | **needs_check** |
| D02 | カイコク | https://kaikoku.blam.co.jp/ | 「無料登録で案件をみる」→ `/user/register/before` | 案件事例のみ。日付付き公開ボードなし | **needs_check** |
| D03 | note | https://note.com/ | `/signup` タイトル「会員登録」 | トップ HTML の公開ノート `publishAt` 2026-09-14 / 15 | **alive** |
| D04 | Braintrust | https://www.usebraintrust.com/for-talent | Join / Create Your Profile | `/jobs` に役割カード。ブログ 2026-09-14 | **alive** |
| D05 | Twine | https://www.twine.net/jobs | `/signup` 200 | 直投稿 Remote「Posted 4 days ago」 | **alive** |
| D06 | Fastwork | https://fastwork.co/en | `/en/signup` はこの環境で 404（SPA） | `/en/ai-automation` に n8n/make パック | **alive** |
| D07 | Twago | https://www.twago.com/ | 公開フリーランス登録面なし | ドメインは Talent-Pool 企業向け。仕事ボードなし | **dead** |
| D08 | 99freelas | https://www.99freelas.com.br/projects | トップ「Crie o seu perfil。É grátis」。`/register/freelancer` は CF 403 | 公開プロジェクト見出し（Laravel 12 等） | **alive** |
| D09 | Gulp | https://www.gulp.de/freelancing/projekte | `/registrieren` Freelancer 枠 | 「NEU」カード、Start ab 2026-09 / 2026-11 | **alive** |
| D10 | Xing Projects | https://www.xing.com/projects | 専用机なし | **404**。現行 XING は jobs network | **dead** |

`keep_queue` (`alive`): **6**  
`skip_log` (`dead`): **2**  
`needs_check`: **2**  
`thin`: **0**

---

## 机ごとの証拠（短文）

マーケの「○万人／○件」は活動証明に使わない。以下は **この観測で画面または公式 HTML に出たもの**。

### D01 Shufti — needs_check

- アプリ https://app.shufti.jp/signup ・ `/jobs/search` は SPA シェル。仕事名は未読。
- ヘルプ「2026年シルバーウィークの営業について」（変更日 8月31日）。休業 9/19–9/23、9/18 は通常営業の案内。
- ヘルプ「手数料一覧」変更日 2025-11-05。振込手数料 330円、組戻 33円、最低振込 363円（**件数ではない**）。
- 本人確認ヘルプあり。**提出しない。**
- 先行 PR（Wave B / Wave D Fit-Med）と同じくカード未読なので SKIP thin にしない。

### D02 カイコク — needs_check

- LP: 「マーケティング人材・デザイナーのための複業（副業）支援サービス」。フロー 1 が「無料登録で案件をみる」。
- 登録 https://app.kaikoku.blam.co.jp/user/register/before タイトル「会員登録前」。完走していない。
- 「案件事例のご紹介」は職種例（運用型広告、CRM、オウンドメディア）。**公開日なし。**
- 登録者数・累計掲載数はマーケ。使わない。
- 公開ジョブボードの日付が無いので `alive` にしない。閉鎖証拠でもない。

### D03 note — alive

- https://note.com/signup 「会員登録｜note（ノート）」。Google ボタンはこの HTML では未確定（analytics 文字列のみ）。
- トップ埋め込みノートに `publishAt` **2026-09-14** / **2026-09-15**（JST）。件数は数えない。
- `/help` に有料記事・有料マガジン・メンバーシップ・定期購読の活用案内。料率表は help-note.com がこのIPで Cloudflare 403。率は書かない。
- 親キュー Wave C（日本語デジタル販売）。下書きのみ。公開しない。

### D04 Braintrust — alive

- 評価SaaS ではなく https://www.usebraintrust.com/ 。Talent 面「$0 fees for talent」「Keep 100% of your earnings」。
- https://www.usebraintrust.com/jobs に役割カード。例: 「Senior Full-Stack Engineer $150–200/hr」。カテゴリ合計の数字はマーケなので使わない。投稿日は未表示。
- ブログ「What Is AI Interview Software? … (2026)」見出し日付 **Sep 14, 2026**。
- 公式コピーに ID-verified / screening。**画面が出たら STOP。** 応募しない。

### D05 Twine — alive

- https://www.twine.net/jobs : 「Jobs posted directly onto the Twine platform」。例: Old School Adventure Game、Remote、$2,500、「Posted **4 days ago**」。
- 同ページ下段 Ari は他社求人の束ね。**使わない。** 直投稿があるので机全体は aggregator にしない。
- `/pricing` Standard **$0.00 per month**、「Service fee from 5%」（発注側の成功報酬コピー）。`/signup` 200。
- ブログ「7 Smart Side Hustles…」**August 21, 2026**。

### D06 Fastwork — alive

- https://fastwork.co/en : TH のフリーランス机。オンラインと対面が混在。対面カテゴリは触らない。
- https://fastwork.co/en/ai-automation : 「AI Automation / n8n / make.com」。開始価格の表示あり（見積の下限であり GMV ではない）。
- コピー: フリーランスは雇う前にシステム上で本人確認。確認画面が出たら停止。
- `/en/signup` はこの環境で 404（SPA）。売り手入口は人がトップから辿る。
- ブログ索引タイトルに「年 2026」。個別記事日付の新しい例は 17/11/2025（SEO 記事、最初の HTML）。

### D07 Twago — dead

- https://www.twago.com/ と `/jobs` は https://www.talent-pool.com/ へ。見出し「We are a complete Talent Pool solution」。企業向けホワイトラベル。公開フリーランス仕事一覧なし。
- https://www.twago.de/ 404。
- 公開売り手登録面なし。SKIP。

### D08 99freelas — dead ではない / alive

- https://www.99freelas.com.br/projects に公開見出し。例: 「Assumir plataforma SaaS em produção com Laravel 12 e Vue 3/Inertia」「Sistemas e agentes de IA para logística」。`Publicado:` ラベルは静的 HTML では空。
- `/como-funciona` : 登録は無料。「taxa de 5% a 20%（R$ 10,00 no mínimo）」。プレミアムは買わない。
- `/register/freelancer` はこのIPで Cloudflare 403。トップと How it works に「É grátis」。
- ブログ https://blog.99freelas.com.br/ 200。索引に個別投稿日は出ていない。

### D09 Gulp — alive

- ブランドは Randstad Professional（vormals GULP）。https://www.gulp.de/registrieren に Freelancer 枠「Projekte für Freelancer」。
- https://www.gulp.de/freelancing/projekte カード例: 「PKI-Architekt / PKI-Engineer … **NEU**」、Start ab asap / **02.11.2026** / **14.09.2026**。「Cloud & Automation Engineering … Start ab **01.09.2026**」。
- トップ: GULP Direkt は「Nutzung … komplett kostenlos - **7 Euro Servicegebühr** pro Freelancer-Stunde fallen erst bei Beauftragung an」（発注側）。Freelancer は「kostenloses Profil」。
- 現地スイス／常駐カードが混在。**現地カードは応募しない。** 机全体はシフトバイト専用ではない。

### D10 Xing Projects — dead

- https://www.xing.com/projects → **404 - Not Found | XING**。
- https://www.xing.com/en は 「XING - The jobs network」。Freelance jobs は希望条件のチップ。Projects 専用マーケットではない。
- SKIP。現行 XING 求人ボードには逃げない（寄せ集め／求人クラス）。

---

## 認証・停止（全机共通）

1. MAIN Google のみ。別アカウントを作らない。Google が無ければ MAIN Google のメール。
2. パスポート／免許／マイナンバー／顔写真／口座が出たら **アップロードせず停止**。
3. PayPal / Stripe 接続で身分証明が出たら同じ。接続しない。
4. 有料会員・優先掲載・審査スキップは買わない。
5. プロフィール公開・出品公開・応募はしない。
6. 公開一覧が読めなければ `needs_check` のまま。数字を埋めない。

## オペレーター順（このゲートのあと）

1. **keep_queue かつ 親キューが Wave C**: note → Braintrust（ID 画面で停止）
2. **keep_queue マーケット**: Twine（Ari 以外）→ Fastwork（雇前 KYC で停止）→ 99freelas → Gulp（現地カード回避）
3. **needs_check**: シュフティ、カイコク — 人が公開一覧の日付を 1 画面
4. **SKIP**: Twago、Xing Projects
