# FABLE-INDEPENDENT — 稼ぐ方向とポートフォリオ設計（独立メタ戦略レビュー）

相談ID: `EARN-PORTFOLIO-DESIGN-20260916-FABLE51` / 入力版 v1
レビュアー: Claude Fable 5.1（Cursor Cloud Agent）— 独立見解。ChatGPT Pro の結論は未受領・未参照。
日付: 2026-09-16（JST 基準。レポ観測は 2026-09-15 UTC 時点の枝）
状態: **DRAFT_ONLY**。このレポートは方針文書ではなく提案。運用ポリシーファイルは一切変更していない。
禁止事項の遵守: 秘密・認証情報・私的ファイル・住所は未閲覧。公開・応募・送信・課金・signup・ブラウザ UI 操作は実施していない。

---

## 0. 10行の結論

1. **n8n は wedge のまま。ただし「n8n 自動化」ではなく「送る前に人が止められる n8n（fail-closed 自動化）」を一枚看板にする。** 既存 3 デモ（受付→表→通知 / 分類+未確定ホールド / 承認ゲート）は全部この一本で説明できる。
2. **最大のメタリスクは「登録の量産」ではなく「見せられる成果物がゼロ」であること。** 110 本の open PR、マージ 0、公開 0、送信 0、画像 0、SKU-0 の Content ZIP 0。Coconala の `image_missing`、Gumroad の ZIP 欠落、Contra の実績欄空欄は、すべて同じ 1 つの欠落（共有アセットキット不在）に還元される。
3. **公開証拠と売り物がねじれている。** 公開物は Python の YouTube/TikTok CLI（autopilot-log）と AI 開発ブログ（yutalab.dev）で、**n8n の公開成果物は 1 つも無い**。n8n を売るなら、n8n の実物を公開するのが最初の仕事。
4. **ショーケースは 4 本＋器 1 つ（§3）。** P1 受付スターター（旗艦。Coconala カバー・Gumroad ZIP・Contra 添付の源泉）、P2 分類+ホールド、P3 承認ゲート（差別化の証明）、P4 手順書サンプル（納品物そのものを見せる）、P5 公開ショーケース repo + 実録記事 1 本。
5. **品質バーは「動く・再現できる・嘘がない」を Must、見た目は Should。** 画像は「ノードが読める canvas + 結果の表 + 止まった通知」の 3 枚で足りる。動画は 60–90 秒 1 本。
6. **登録追加は 30 日で最大 2 机、しかも Gate-A（初回公開 or 初回送信の実施）を通過するまで 0。** 1 机 1 CU セッション（45 分）で `draft_saved` に届かなければ 30 日間は永久パーク。
7. **実績ゼロの信用は「実物・失敗カタログ・除外範囲の明示・実録」で作る。** 架空レビュー・件数・精度 % は使わない（既存 FACTS 方針と一致）。
8. **SWE-2 は「作る」（JSON・fixture・スクショ・動画・ZIP 組み立て）、Cursor Grok は「検品・文言・整合」。CU は SWE-2 がローカル n8n の見た目確認に先に使い、Grok は 2 番手、常に 1 本。** Grok Bot は発注・受入・損切りのみ。
9. **早期ゲート: Day 7 に「P1 が import できる + 画像 3 枚 + カバー 1 枚」を満たしたら、その時点で Coconala 公開の GO/NO-GO を本人が判断する。以後の磨きは「公開を止める欠陥」以外は禁止。** 磨き続けるほど機会費用が積み上がる。
10. **最強の代替案は「YouTube/SNS 投稿自動化（公式 API）へ wedge を寄せる」。** 公開証拠が既にあり、Coconala に類似ギグ・依頼が観測されている。30 日で n8n 出品が問い合わせ 0 かつ YouTube 系依頼が継続観測なら切り替える（§9）。

---

## 1. 目標と構造の診断（一般論ではなく、この repo の事実から）

### 1.1 観測した事実（すべて枝上の文書。live 画面は未確認）

| 事実 | 出典 |
|---|---|
| `master` は YouTube/TikTok CLI のみ。earn-ops フォルダは無い | `git ls-tree master`, PR#35 INDEX |
| open PR 110 本（#1–#110）。merged 0、closed 0 | `gh pr list` |
| Coconala サービス 4403529: unpublished、`image_missing`、FAQ 6、見積受付 ON、フォーム価格 10000 観測 | PR#103 STATUS |
| Gumroad SKU-0: `draft_saved`、$39 は「既にあれば維持」、Content ZIP 無し、SKU-0 パック自体が git に無い（SKU-1/2/3 のスタブ JSON はある） | PR#55 GAPS R1–R6, PR#74 STATUS, PR#37/#46/#52 |
| Contra Independent: `draft_saved`、Free、Kent USA のまま、apply 0、提案文 5 本は未送信 | PR#64 STATUS, PR#71 |
| LinkedIn Services: `paste_ready`（`draft_saved` ではない）、Save=viewable の壁 | PR#75 STATUS |
| Freelancer.com: `blocked_signup`（Earn-money spinner）。会員かどうか不明 | PR#93 STATUS |
| Wave B/C/D 登録 CU は cut（register-winddown / jobs-first） | PR#65 NEXT-CU, PR#72 STATUS |
| 3 本のデモ台本（Loom 用、未録画） | PR#78 |
| 4 SKU 価格メニュー（全額プレースホルダ） | PR#82 |
| 板スキャン 20 件: Coconala に YouTube/n8n 系の依頼・ギグ、Upwork に n8n 案件（多くは `needs_check`） | PR#80 SCOREBOARD |
| 画像・動画・PDF などのバイナリ資産は **全枝にゼロ**（非 .md は JSON 9 ファイルのみ） | `find /tmp/src -type f ! -name '*.md'` |
| 公開サイト yutalab.dev は Claude Code / Codex / 自動化 / AI 副業の実録ブログ（n8n 記事は一覧に見当たらない） | 公開 GET 1 回 |

### 1.2 構造の問題（3 つ）

**A. 「制御文書 ≫ 成果物」の逆転。** 110 PR のほぼ全てが登録手順・ゲート・ステータス・貼り付け文。買い手が見る物（画像・動く JSON・動画・手順書サンプル）は 1 つも無い。register wind-down は正しいが、JOBS フェーズも同じ癖（貼り付け文の量産）を引き継いでいる。**次に作るべきは文書ではなく資産。**

**B. 証拠と商品のねじれ。** 公開証拠（Python CLI、AI 開発記事）は「fail-closed の設計思想」と「検品の丁寧さ」を証明するが、**n8n の手が動く証明にはならない**。買い手は「n8n で作れる人か」を 10 秒で判断する。n8n の canvas 画像 1 枚が無い状態で n8n を売るのは、料理写真の無い飲食店。

**C. 公開の意思決定が「全部そろってから」型。** 各 GO ゲートは正しく閉じているが、「何がそろえば開けるか」の最小定義が無いため、際限なく draft が増える。**ゲートは「欠陥ゼロ」ではなく「最小資産セット」で定義し直す**（§8）。

### 1.3 何を捨てるか

- Coconala 出品 03「AI 運用伴走」（PR#79）: 初回納品実績が出るまで **出品しない**。継続契約は実績ゼロでは売れず、審査コストだけ上がる。
- Contra 提案 03「inspectable AI ops」/ 05「sheet sync」: 4 SKU メニュー外。**送らない**（PR#89 の判断を支持）。
- Wave B–D 登録、Fiverr/Lancers/CrowdWorks 再試行、PPH 有料、Contra Pro、LinkedIn Premium: 30 日間 **触らない**。
- Lステップ系依頼（PR#80 #2）: 必須経験が無い限り **見送る**。

---

## 2. 誰に何を売るか（最初の 30 日）

### 2.1 ターゲット顧客（優先順）

| 優先 | 顧客像 | 痛み | 机 | 根拠 |
|---|---|---|---|---|
| 1 | 日本の小規模事業者・一人社長・小規模代理店。問い合わせフォーム/メール/LINE の内容を **手でスプレッドシートに転記し、手で通知** している | 転記漏れ・返信遅れ。ただし「勝手に送られる」のは怖い | Coconala | 板スキャンで自動化系依頼が継続。fail-closed が刺さる層 |
| 2 | 英語圏の小規模 SaaS/エージェンシー運営者。n8n を自分でも触るが、intake→分類→承認の型を早く欲しい | 自前で作る時間が無い。テンプレ + 手順書が欲しい | Gumroad（$39 テンプレ）、Contra | SKU-1/2/3 スタブと EN 提案文が既にある |
| 3 | 既に n8n/Zapier/Make のフローがあり、**手順書が無くて怖い** 人 | 担当者が変わると止まる。再実行の順が分からない | Coconala / Contra（docs SKU） | ブログの「検品 12 項目」と相性が良い。実装より受注しやすい |

**売らない相手:** 企業の承認基盤、スクレイピング・SNS 運用代行、精度保証が要る AI 分類、Lステップ構築。

### 2.2 wedge と隣接サービス

- **wedge = n8n 受付スターター（form → table → notify、送信は人）。** 最短で見せられ、最短で納品でき、P1 の資産がそのまま 3 机で使える。
- **upsell = 承認ゲート（timeout は承認ではない）。** これが差別化。「安全に自動化する人」というブランドの核。
- **隣接（追加するなら 1 つだけ）= 既存フローの検品 + 手順書（docs SKU）。** 新規構築より受注障壁が低く、初回の「本物の納品」を最速で作れる。ブログの検品記事が証拠になる。**「AI 運用伴走」は隣接ではなく別事業なので保留。**

### 2.3 最初の 30 日のオファー構成

| 机 | 出す物 | 価格の扱い |
|---|---|---|
| Coconala | 出品 01（n8n 自動化 + 手順書）のみ公開。02 分類は P2 完成後に追加判断 | フォーム上の 10000 は観測値。この文書は値を決めない（`{{PRICE_YEN}}` 方針を維持） |
| Gumroad | SKU-0 のみ。$39 は既存値なら維持 | ZIP が付くまで unpublished |
| Contra | Service 1 つ（starter intake）+ Job-feed 提案 1 本/週まで | Contact for pricing |
| LinkedIn | Services は `no_draft_path` なら触らない。プロフィール About に公開 repo リンクだけ | — |

---

## 3. ショーケース 4 本 + 器 1 つ

共通ルール: ダミーデータのみ（`EXAMPLE-ONLY`）。全 JSON は `active: false`。秘密はプレースホルダ。n8n/Google/Slack のロゴを自分の物のように使わない。数字の成果（時短・精度）は書かない。

### P1 受付スターター（旗艦）— 「フォーム → 表 → 人へ通知（送信は人）」

| 項目 | 内容 |
|---|---|
| 想定買い手 | §2.1 の 1 と 2 |
| 課題 | 問い合わせの転記漏れ。しかし自動返信は怖い |
| 入力→処理→出力 | n8n Form Trigger（または Webhook POST）→ 正規化 Set → **ローカル CSV 書き出し**（Convert to File + Read/Write Files from Disk。認証不要で再現可）→ 通知は NoOp「operator ping — not sent」。Google Sheets 版はノード 1 個差し替えとして README に図示 |
| 成果物 | `p1-intake-starter.workflow.json`（import 可・inactive）/ `fixtures/inquiries-10.json`（日英ダミー 10 件）/ `README.ja.md` `README.en.md` / 図 1 枚（Mermaid → SVG/PNG）/ スクショ 3 枚（canvas 全体・出力 CSV/表・止まっている通知ノード）/ 動画 60–90 秒（MP4 + GIF）/ カバー画像 1 枚（§5） |
| 現実的データ | 「明日は臨時休業ですか」「請求書の再発行をお願いします」「見積もりの有効期限は」など日英 10 件。個人名・会社名は架空 |
| 工数見込み | SWE-2 3–5 時間（JSON・fixture・README・図）+ CU 1 セッション（スクショ・録画）+ Grok 検品 1 時間 + 本人確認 20 分 |
| チャネル再利用 | Coconala カバー + サービス画像 3 枚 / Gumroad SKU-0 Content ZIP の中身そのもの / Contra Service の添付・Job-feed 提案のリンク / LinkedIn About のリンク |
| DoD（検証可能） | (1) `docker run n8nio/n8n` の固定バージョンで `n8n import:workflow --input=p1-intake-starter.workflow.json` が exit 0。(2) `jq '.active == false and ([.nodes[].parameters | tostring] | join(" ") | test("sk-|xoxb|AIza") | not)'` が true。(3) fixture 10 件を curl で投げ、出力 CSV が 10 行、通知ノードは実送信ゼロ（ログで確認）。(4) 画像 3 枚に webhook path・URL・認証 UI が写っていない（Grok が目視）。(5) README の「含まないもの」節が PR#82 の共通除外と一致 |

### P2 問い合わせ分類 + 未確定ホールド

| 項目 | 内容 |
|---|---|
| 想定買い手 | §2.1 の 2（Gumroad/Contra）、Coconala 02 出品の将来 |
| 課題 | 種別分けを手でやっている。AI に任せると勝手に返信しそうで怖い |
| 入力→処理→出力 | Webhook → 正規化 → ルール分類（billing/support/sales/**uncertain**）→ uncertain は hold キューへ → 人へ通知（NoOp）。LLM ノードは **オフのまま同梱**（差し替え位置だけ示す） |
| 成果物 | PR#37 のスタブ 2 本を **実行可能に昇格**（P1 と同じ CSV 出力型に揃える）/ `fixtures/inquiries-30.csv`（期待ラベル列付き）/ **挙動一覧表**（30 件それぞれの出力ラベル。「精度 %」とは書かず「同梱サンプルでの挙動。保証値ではない」と明記）/ 図 1 枚 / スクショ 2 枚（分類後の表・hold キュー） |
| 工数 | SWE-2 3–4 時間 + CU 0.5 セッション + Grok 1 時間 |
| 再利用 | Gumroad SKU-1 ZIP / Contra Job-feed 02 / Coconala 02（後日） |
| DoD | import exit 0 / fixture 30 件のうち曖昧 5 件が **必ず** uncertain になる（fixture 側で曖昧文を意図的に用意し、テストで固定）/ 自動返信ノードが存在しない（`jq` で `emailSend|slack|gmail` 型ノードが無いこと）/ 挙動一覧が生成スクリプトから再現できる |

### P3 承認ゲート — 「timeout は承認ではない」

| 項目 | 内容 |
|---|---|
| 想定買い手 | §2.1 の 1・2 の upsell。「安全に自動化」を疑う人 |
| 課題 | 下書きはできても、外に出すボタンを機械に持たせたくない |
| 入力→処理→出力 | 下書き投入 → Wait（Webhook resume）→ `approve` / `reject` / 欠落 / timeout を IF で分岐 → **approve 以外は全部「閉じる」**（通知のみ）→ approve 時のみ後段 NoOp「would send」 |
| 成果物 | PR#46 スタブを実行可能に / **失敗カタログ表**（入力 × 結果。timeout 行を太字）/ シーケンス図 1 枚 / 動画 45–60 秒（timeout して送られない所を見せる）/ スクショ 2 枚 |
| 工数 | SWE-2 3–4 時間 + CU 1 セッション（timeout の録画は待ち時間が要るので Wait を 30 秒に短縮した demo 版を別 JSON で用意）+ Grok 1 時間 |
| 再利用 | Gumroad SKU-2 ZIP / Contra Job-feed 04 / Coconala の見積返信での「安全性」説明 / ブログ記事の題材 |
| DoD | import exit 0 / 4 分岐すべてを curl で再現し、approve 以外で後段ノードが実行されないことを execution ログで確認 / 動画に timeout → 「not sent」の表示が入っている / README に「SLA・自動送信は含まない」明記 |

### P4 手順書サンプル（docs SKU の納品物を見せる）

| 項目 | 内容 |
|---|---|
| 想定買い手 | §2.1 の 3。および P1–P3 の購入検討者（「何が届くか」を見たい） |
| 課題 | 買う前に納品物の質が分からない |
| 入力→処理→出力 | P1 を題材に、実際に納品する形式の手順書を書く: 何が起動するか / 直してよい欄と秘密の欄 / 再実行の順 / 失敗 1 件の戻し方 / 変更メモ欄 |
| 成果物 | `RUNBOOK-sample.ja.md` + `.en.md`（PDF 化は Nice）/ 1 ページ目のスクショ 1 枚（Coconala 画像 3 枚目に使える） |
| 工数 | Grok 2 時間（文書主体）+ SWE-2 30 分（PDF 化）+ 本人 15 分 |
| 再利用 | Coconala 01 のサービス画像 / Gumroad ZIP 同梱 / Contra docs Service の添付 / 見積返信の「納品イメージ」リンク |
| DoD | P1 を知らない人（Grok の別セッション）が手順書だけで import→fixture 実行→CSV 確認まで到達できる（再現テスト）/ 秘密欄と編集可欄の表がある / 用語が PR#82 と一致 |

### P5 器 — 公開ショーケース repo + 実録記事 1 本（Should）

| 項目 | 内容 |
|---|---|
| 内容 | `n8n-showcase`（仮）repo に P1–P4 を格納。README トップに「fail-closed 自動化」の 1 段落、3 本の図、各 P の DoD 結果。yutalab.dev に「n8n で受付を自動化して、送る前に止める型を作った実録」1 本（既存ジャンルに合致） |
| 工数 | SWE-2 1 時間（repo 構成・CI で import テスト）+ Grok 2 時間（記事草稿）|
| 再利用 | 全机のリンク先。Contra/LinkedIn の「実績」欄の代替 |
| DoD | CI（GitHub Actions）で docker n8n import テストが緑 / README のリンクが全部生きている / 記事は本人が公開ボタンを押す（GO） |
| 注意 | repo を public にする・記事を公開するのは「公開」なので **本人 GO**。それまでは private/draft で作る |

---

## 4. 品質バー（Must / Should / Nice）

| 観点 | Must | Should | Nice |
|---|---|---|---|
| 見た目 | canvas 全体が 1 画面に収まり、ノード名が読める。ダミー表示。ロゴ流用なし。カバーは文字が 3 行以内 | 配色 2 色 + アクセント 1 色で全机統一。図は Mermaid 由来で再生成可 | 動画に字幕焼き込み。カバーの日英 2 版 |
| 機能の信頼性 | 固定 n8n バージョンで import 成功。fixture 実行で期待出力。実送信ノード無し。`active:false` | CI で import テスト。失敗 1 件（不正 JSON）の挙動も fixture 化 | 複数 n8n バージョンでの import 確認 |
| 説明 | README に「何をする / しない / 差し替え位置 / 秘密の置き場」。90 秒で読める | 図 1 枚で入力→処理→出力。動画 60–90 秒 1 本 | FAQ 5 問（PR#74 FAQ から転用） |
| 再現性 | 認証不要で手元再現できる（CSV 出力型）。手順書だけで第三者が到達 | Google Sheets 版への差し替え手順 | docker-compose 1 ファイルで環境ごと再現 |
| 信用 | 個人出品・非パートナーの明記。除外範囲の明記。公開 repo と実名表記の一致 | 失敗カタログ表。実録記事 1 本 | 第三者（Grok 別セッション）の再現ログを添付 |
| プライバシー | webhook path / URL / 認証 UI / シート ID を画像・動画に出さない。fixture は架空 | 画像に自動マスク工程（スクリプト化） | — |
| 正直な主張 | 件数・GMV・精度 %・時短・レビュー・バッジを **書かない**。「同梱サンプルでの挙動」と限定 | 「初出品です」を隠さない（Coconala は初回購入者への説明として自然） | — |

**「Must が全部緑なら公開判断に進む。Should の未達を理由に公開を延ばさない。」** これがゲートの定義（§8）。

---

## 5. 共有アセットキットと机別の仕立て

### 5.1 キット構成（`assets/kit/` 1 か所に置く）

| 資産 | 仕様（要確認は明記） | 生成方法 |
|---|---|---|
| ワードマーク | 「送る前に、人が止められる自動化」/ EN「Automation that fails closed」。ロゴ画像は作らない（文字のみ） | Grok が候補 3 → 本人が 1 つ選ぶ |
| 配色 | 基調 1・背景 1・アクセント 1。n8n のオレンジは避ける | 定義ファイル `palette.json` |
| 図テンプレ | Mermaid flowchart。左入力・中処理・右出力。「人」アイコンは絵文字でなく四角に「人」 | `scripts/render-diagrams.sh`（mermaid-cli） |
| スクショ規約 | 1600×900、ブラウザ chrome を切る、URL バーを含めない、マスク後に保存 | Playwright（ローカル n8n 対象）または CU |
| カバーテンプレ | 1 枚のマスター（正方形・横長を同一デザインから書き出し）。**Coconala の推奨画像サイズと Gumroad カバー/サムネ推奨サイズは公式ヘルプで直前確認（本文書は数値を断定しない）** | SVG マスター → `scripts/export-covers.sh` |
| 動画 | 60–90 秒。無音でも分かる字幕。MP4（掲載用）+ GIF（README 用） | CU 録画 → ffmpeg |
| 文言ブロック | 「含む / 含まない / 進め方 / 個人出品の注記」の 4 ブロックを 1 ソース（YAML）で管理し、机別に生成 | Grok が `copy.yaml` → 机別 md |

### 5.2 机別の仕立て

| 机 | 使う物 | 変える所 | 変えない所 |
|---|---|---|---|
| Coconala | カバー（正方形）、サービス画像 3 枚（canvas / 出力表 / 手順書 1 頁）、サービス内容 655 字（PR#79 01 のまま） | 縦書き感のある日本語コピー。「手順書つき」を前面 | 除外範囲・非パートナー注記 |
| Gumroad SKU-0 | カバー（横長）、サムネ、Content ZIP = P1 一式 + P4 手順書 + `DRAFT_ONLY` を外した買い手向け README | 英語主体、「What you get」を箱書き | $39 は既存値なら維持 |
| Contra | Service に P1 図 + 動画リンク、Job-feed 提案に P5 repo リンク 1 本 | 提案ごとに `{{ONE_SPECIFIC_DETAIL}}` | 価格は Contact for pricing |
| LinkedIn | About に P5 リンク 1 行のみ | — | Services は `no_draft_path` なら触らない |

**1 ソース多出力** が原則。机ごとに文言を手書きすると整合が崩れる（現状 110 PR 間で既にヒント値の齟齬が複数ある: PR#24 vs #35、#49/#54 vs #64/#93）。

---

## 6. 実績ゼロで信用を作る方法（偽装なし）

1. **実物を触らせる。** 公開 repo で import→実行→結果まで 10 分で再現できる。これは「レビュー 5 件」より強い証拠。
2. **失敗カタログを公開する。** P3 の「reject / 欠落 / timeout → 全部閉じる」表。安全性を語るのではなく見せる。
3. **納品物そのものを見せる。** P4 手順書サンプル。買い手の不安は「何が届くか」。
4. **除外範囲を先に書く。** スクレイピング・自動送信・精度保証をしないと明記。誠実さの信号であり、悪い依頼の事前除去でもある。
5. **実録で語る。** yutalab.dev の既存ジャンル（実録・失敗談）に n8n 記事 1 本。「作った過程と詰まった所」は捏造不可能な証拠。
6. **同一性を揃える。** 表示名・公開 repo・ブログ・各机の一文が一致していること。バラバラだと不信の種。
7. **初出品を隠さない。** 「初出品のため丁寧に対応します」は Coconala では通常の表現。
8. **使わない物:** 架空クライアント、件数、GMV、精度 %、「n8n Expert」、時短時間、ストック写真の顔。

---

## 7. 実装バックログ（SWE-2 / Cursor Grok / Grok Bot）

役割: **SWE-2 = 作る**（コード・JSON・fixture・スクリプト・画像・動画・ZIP）。**Cursor Grok = 検品・文言・整合**（README、机別コピー、DoD 目視、再現テスト）。**Grok Bot = 発注・受入・損切りのみ**（手は動かさない。PR#26 のロック通り）。CU は常に 1 本、SWE-2 優先。

| ID | 担当 | 内容 | 依存 | 並列 | 受入テスト | 損切り |
|---|---|---|---|---|---|---|
| T01 | SWE-2 | `assets/kit/` 骨組み: palette.json、Mermaid テンプレ、render/export スクリプト、docker-compose（n8n 固定版） | — | T02 と並列 | `docker compose up` で n8n が起動、`render-diagrams.sh` が SVG を出す | 2 時間で n8n が立たなければ版を変えて 1 回だけ再試行、以後は本人へ |
| T02 | Grok | `copy.yaml`（含む/含まない/進め方/注記の 4 ブロック、日英）を PR#79 01・#82・#74 から統合 | — | T01 と並列 | 3 出典との差分を表で提示。新しい主張を足していない | — |
| T03 | SWE-2 | P1 workflow JSON + fixture 10 件 + curl スクリプト | T01 | T04 と並列 | §3 P1 DoD (1)(2)(3) | 4 時間超で CSV 出力が動かなければ、Sheets 差し替え案を捨てて CSV 一本に絞る |
| T04 | Grok | P1 README 日英 + 図の文言 | T02 | T03 と並列 | 90 秒で読める（文字数上限を設定）/ 除外節が copy.yaml と一致 | — |
| T05 | SWE-2 (**CU #1**) | ローカル n8n で P1 のスクショ 3 枚 + 録画 60–90 秒。マスク処理まで | T03 | 単独（CU mutex） | 画像に URL/path/認証 UI が無い（T06 で目視）/ 動画長 60–90 秒 | CU 1 セッション（45 分）で撮れなければ Playwright 静止画のみで代替し、動画は後回し |
| T06 | Grok | T05 成果の目視検品 + 再現テスト（README だけで import→実行） | T05 | — | 再現到達 / 漏れ 0 件 | 漏れがあれば T05 に戻す（1 回まで）|
| T07 | SWE-2 | カバー SVG マスター + 机別書き出し（サイズは公式ヘルプ確認値を本人/Grok が渡す） | T01, T02 | T03 と並列 | 書き出しファイルが存在し、文字 3 行以内 | 2 案まで。3 案目は作らない |
| **G-A** | 本人 | **Gate-A: Coconala 公開 GO/NO-GO 判断**（T03–T07 の Must 緑が条件）| T06, T07 | — | GO なら本人が画像添付→公開。NO-GO なら理由を 1 行 | 判断を延ばす場合は「止める欠陥」を 1 行で書く。書けなければ GO |
| T08 | SWE-2 | P4 手順書の PDF 化 + Gumroad Content ZIP 組み立て（P1 一式 + P4 + 買い手 README） | T03, T09 | T10 と並列 | ZIP 展開 → README の手順で再現 / 秘密スキャン 0 件 | — |
| T09 | Grok | P4 手順書 日英 | T03 | T05 と並列 | §3 P4 DoD（別セッション再現） | 2 往復まで |
| T10 | SWE-2 | P2 classifier 昇格 + fixture 30 + 挙動一覧生成スクリプト | T03 | T08 と並列 | §3 P2 DoD | 曖昧 5 件が uncertain にならない場合はルールを直すのでなく fixture の曖昧文を明確化する（過学習禁止）|
| **G-B** | 本人 | **Gate-B: Gumroad SKU-0 Publish GO/NO-GO** | T08 | — | 本人が ZIP 添付→判断 | 同上 |
| T11 | SWE-2 | P3 approval gate 昇格 + demo 版（Wait 30 秒）+ 失敗カタログ生成 | T03 | T10 と並列 | §3 P3 DoD（4 分岐ログ） | — |
| T12 | SWE-2 (**CU #2**) | P3 timeout 録画 45–60 秒 + P2 スクショ 2 枚 | T10, T11 | 単独 | 動画に「not sent」が映る | CU 1 セッション超で静止画代替 |
| T13 | Grok | Contra Job-feed 提案 01 の仕立て（P5 リンク挿入、`{{ONE_SPECIFIC_DETAIL}}` 空欄のまま） | T05 | — | PR#71 01 との差分が「リンク追加」だけ | — |
| **G-C** | 本人 | **Gate-C: Contra 提案 1 本 送信 GO/NO-GO** | T13, 実在の Job-feed 1 件 | — | 本人が detail を埋めて送る or skip | detail が 1 分で埋まらなければ skip（既存ルール）|
| T14 | SWE-2 | P5 repo 構成 + CI import テスト | T03, T10, T11 | — | Actions 緑 | — |
| T15 | Grok | 実録記事草稿 1 本 | T05, T12 | — | 主張が FACTS.md の非事実に触れていない | — |
| T16 | Grok (**CU #3**、Gumroad/Coconala 画面確認が要る時だけ）| 公開後の表示確認（画像崩れ・リンク切れ） | G-A/G-B 後 | 単独 | 崩れ 0 or 修正票 | 見るだけ。触らない |

**並列の型:** SWE-2 1 本（作る）+ Grok 1 本（書く/検品）を常時、CU は SWE-2 → Grok の順で 1 本ずつ。Grok Bot はチケット発注・受入判定・損切り宣言のみ。

**全体の損切り:** T03–T07 の合計が 16 時間（作業時間）を超えて Gate-A に到達しない場合、P2/P3 を止めて P1 だけで Gate-A を強行判断する。**30 日で公開・送信が 1 件も無ければ、§9 の代替案評価を開く。**

---

## 8. 2 週間 / 30 日計画と「磨きすぎ防止ゲート」

前提: 1 日 1 机、1 GO/日、KYC・課金は本人のみ（PR#76 の型を継承）。

### 8.1 2 週間

| 日 | 作る（エージェント） | 判断（本人） |
|---|---|---|
| D1–2 | T01, T02, T07（キット・文言・カバー） | ワードマーク 1 つ選ぶ（5 分） |
| D3–4 | T03, T04（P1 本体・README） | — |
| D5 | T05（CU #1 スクショ・録画）、T09 着手 | — |
| D6 | T06 検品、T07 書き出し確定 | — |
| **D7** | — | **Gate-A: Coconala 公開 GO/NO-GO。** Must 緑なら「止める欠陥を 1 行で書けない限り GO」 |
| D8–9 | T08, T10（ZIP、P2） | Coconala 公開後の見積返信は PR#81 の型で本人 |
| **D10** | — | **Gate-B: Gumroad Publish GO/NO-GO**（ZIP 添付後） |
| D11–12 | T11, T13（P3、Contra 仕立て） | — |
| D13 | T12（CU #2） | — |
| **D14** | 2 週レビュー: 公開数・送信数・問い合わせ数（実数のみ） | **Gate-C: Contra 提案 1 本** |

### 8.2 D15–30

- D15–18: T14, T15（P5 repo、記事草稿）。本人が repo public 化と記事公開の GO。
- D19–25: 問い合わせ対応優先。P2 を Coconala 02 出品に載せるかを **問い合わせ内容を見て** 判断。登録追加は **Gate-A 通過済みかつ問い合わせ 0 の場合のみ** 検討（§8.4）。
- D26–30: 30 日レビュー。§9 のスイッチ条件を照合。

### 8.3 磨きすぎ防止ゲートの定義

- ゲートは **「Must が全部緑」** で開く。Should/Nice の未達は理由にならない。
- NO-GO には「公開を止める欠陥」を **1 行** で書く義務。書けなければ GO。
- 同じ資産の再撮影・再デザインは **各 2 回まで**（T07 損切りと同じ）。
- ゲート通過後の修正は「誤記・リンク切れ・秘密混入」のみ即時。それ以外は週 1 回まとめる。

### 8.4 登録追加のルール（§2 の「登録が目的化しない」担保）

- **前提条件:** Gate-A または Gate-C を 1 つ以上通過している（= 公開か送信が実際に 1 回起きている）。
- **上限:** 30 日で **2 机まで**。候補は fit が高く壁が低い順: (a) Upwork（n8n 需要が最大。ただし Google アクセス遮断が解けている時のみ）、(b) JP Wave B `pass` の 1 机（SOKUDAN または Workship。高単価の業務委託向け）。Fiverr/Lancers/CrowdWorks/Freelancer の再試行はしない。
- **kill rule:** 1 机 1 CU セッション（45 分）で `draft_saved` に届かない、または KYC・captcha 画像・有料壁が出たら **30 日間パーク**。登録 CU の合計は 30 日で 2 セッションまで。
- **理由:** 現状の最短経路は「既に draft がある 3 机で実物を見せる」こと。4 机目は資産ができてからの方が登録の質も上がる。

---

## 9. 最強の代替案とスイッチ条件

### 9.1 代替案 A: wedge を「SNS 投稿自動化（公式 API・Python）」に寄せる

- **根拠:** 公開証拠（autopilot-log: YouTube Data API / TikTok Content Posting API、fail-closed gate、テスト 22 本）が **既に存在**。yutalab.dev の読者層とも一致。板スキャン（PR#80）で Coconala に類似ギグ（4268304 / 4268246）と依頼（5258870）が観測され、需要の存在は確認済み。
- **形:** Coconala に「YouTube 予約投稿を公式 API で自動化（ブラウザ操作なし・公開スイッチは人）」を出品。P1 相当の資産は **repo に既にある**（README・テスト）。不足は画像 3 枚と動画 1 本だけ。
- **弱点:** 買い手の多くは「動画制作〜投稿まで」を望み、投稿部分だけの需要は薄い可能性。TikTok は無人投稿できないと明記する必要があり、期待値管理が重い。
- **スイッチ条件（いずれか）:** (1) 30 日で n8n 出品の問い合わせ 0 件 かつ Coconala で YouTube/SNS 自動化系の依頼が週 1 件以上継続観測。(2) 最初の 3 件の問い合わせのうち 2 件以上が投稿自動化の相談。(3) T03–T07 が損切り（16 時間）に達し n8n 資産が Gate-A に届かない。
- **スイッチ時の再利用:** アセットキット（§5）と品質バー（§4）はそのまま使える。捨てるのは P2/P3 だけ。

### 9.2 代替案 B: docs/検品ファースト（構築を売らない）

- 「既存フローの検品 + 手順書」だけを最初に出す。ブログの検品記事が直接の証拠。納品が文書なので初回実績が最速で作れる。
- **スイッチ条件:** 問い合わせの過半が「今あるフローが怖い/止まる」型で、新規構築の相談が少ない場合。

### 9.3 推奨を維持する条件

n8n 出品公開後 30 日で **問い合わせ 1 件以上**、または Contra 提案への返信 1 件以上。これが出れば wedge は正しい。0 なら §9.1 の評価を開く。

---

## 10. 主要リスク

| リスク | 影響 | 手当 |
|---|---|---|
| 資産づくりも「文書量産」に変質する | 30 日後も画像 0 | チケットの DoD をファイル存在 + コマンド結果で定義（§7）。md だけの成果は受入しない |
| n8n バージョン差で import が壊れる | 買い手の初体験が失敗 | docker 固定版を README に明記。CI で import テスト |
| 画像・動画に秘密が写る | 信用毀損 | マスク工程のスクリプト化 + Grok 二重目視（T06）|
| Coconala/Gumroad の画像仕様を誤る | 公開時に差し戻し | 数値を文書に固定せず、公開直前に公式ヘルプを本人/Grok が確認 |
| Contra の Kent USA / Persona | 日本拠点の表記と矛盾 | 提案文では「Japan」と明記（既存方針）。場所変更は朝の本人判断。稼ぐゲートとは分離 |
| CU 争奪（SWE-2 vs Grok） | 撮影が遅れる | CU 予定は T05 → T12 → T16 の順で固定。Grok は静止画代替を先に受入 |
| 需要の読み違い | 30 日で 0 件 | §9 のスイッチ条件を最初から日付入りで置く |
| 110 PR の未整理 | 参照先が散逸・ヒント値の齟齬 | 本レポートの範囲外。ただし P5 repo 完成後に「資産 PR 数本 + 索引 1 本」への集約を提案（別票）|

---

## 11. 調査した repo ソース / 参照できなかった物

### 11.1 実際に読んだ物（枝を checkout せず `git show` で内容取得）

- `master`: `README.md`、`autopilot_log/`、`tests/`（earn-ops フォルダは無し）
- PR#35 `earn-master-index-refresh-20260916/INDEX.md`（全体地図・open PR 表）
- PR#103 Coconala 4403529 `STATUS.md`（`image_missing`、FAQ 6、価格観測）
- PR#79 Coconala 出品 01 本文（前半 150 行）
- PR#74 Gumroad SKU-0 listing polish `STATUS.md`、PR#55 `GAPS.md`（SKU-0 パック不在 R1–R6）
- PR#37 SKU-1 `BUYER-README.md` とスタブ JSON 冒頭（実行可能スタブの構造確認）
- PR#64 Contra `STATUS.md`（`draft_saved`、Kent USA、apply 0）
- PR#75 LinkedIn Services `STATUS.md`（`paste_ready`）
- PR#93 Freelancer `STATUS.md`（`blocked_signup`）
- PR#65 `NEXT-CU.md`、PR#72 `STATUS.md`（register-winddown / REGISTER-CU-CUT）
- PR#78 デモ台本 `README.md` `FACTS.md`（許される主張の一覧）
- PR#82 `SKU-MENU-JA.md`（4 SKU・除外範囲）
- PR#76 `WEEK.md`、PR#88 `RANKED.md`、PR#89 `ONE-PAGER.md`（JOBS 週次・優先順・売り方）
- PR#80 `SCOREBOARD.md`（前半。板の需要観測）
- PR#40 SWE-2 wave5 mirror `README.md`、PR#26 Grok-head `README.md` `COMMON-THIN.md`（CU/座席のロック）
- `gh pr list`（open 110 / merged 0 / closed 0）、全枝の非 .md ファイル一覧（JSON 9 本のみ）
- 公開 GET: https://yutalab.dev/ トップ 1 回（記事一覧のみ）

### 11.2 参照できなかった / 未検証の物

- ChatGPT Pro の結論（未受領。参照していない）
- Coconala / Gumroad / Contra / LinkedIn / Freelancer の **live 画面**（ログイン不可・意図的に未実施）。ステータスは全て枝上の文書経由
- 実価格（全て `{{PRICE_*}}`。Coconala 10000 と Gumroad $39 は文書上の観測値）
- Coconala サービス画像 / Gumroad カバー・サムネの **公式推奨サイズ**（未確認。公開直前に確認を要求）
- n8n の Data Table 機能など最新ノードの有無（未確認。本文書は認証不要の CSV 出力型を前提にしており、依存しない）
- Freelancer.com にアカウントが存在するか（`blocked_signup` のまま不明）
- LinkedIn の captcha 状態、Contra Job-feed の現在の案件
- 秘密・認証ストア・私的ファイル・住所（方針により未閲覧）
- PR#79 02/03、#71 全文、#7 RUNBOOK 745 行、#83 cold email、#27/#44 X 系: 表題と索引のみ確認、本文未読

### 11.3 このレポートがしていないこと

- 運用ポリシー・ゲート・ステータスファイルの変更
- 兄弟 PR のマージ・draft 解除・書き換え
- 公開・応募・送信・課金・signup・ブラウザ UI 操作
- 価格・件数・GMV・精度の断定
