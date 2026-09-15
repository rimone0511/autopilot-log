> DRAFT_ONLY paste stub. NO secrets. NO browser signup from this PR. NO publish.
> Gap-fill for CU-12 where prior packs left Google button / worker % / listing dates as needs_check.
> Agent that wrote this pack did not create an account.
> `thin_site_skip: false`. Stop at KYC.

# CU-12 GAP-FILL — 複業クラウド（旧 Another Works）

| キー | 値 |
|---|---|
| cu_serial | CU-12 |
| activity_gate | **needs_check**（個別求人タイトルは出る。本文ローダー。新着日付なし。pass にしない） |
| self_serve | **yes**（人材ドメイン。面談必須と公開トップに書いていない） |
| cu_ready | **true**（スタブあり。登録済みではない） |
| talent | https://talent.aw-anotherworks.com/ |
| sign_up | https://talent.aw-anotherworks.com/sign_up （200。タイトル「新規登録」） |
| login | https://talent.aw-anotherworks.com/login （200。タイトル「サインイン」） |
| company | https://anotherworks.co.jp/ |
| tos | https://cl.aw-anotherworks.com/user_tos |
| privacy | https://anotherworks.co.jp/user_privacy |
| google_signup_preference | **PREFER_GOOGLE** |
| worker_fee_public | **cited**: TOS 第2.1条1「本サービスを無料で利用することができます」（登録タレント）。人材の成果報酬％は TOS に無し → **needs_check**。作らない |
| thin_site_skip | **false** |
| stop_at_kyc | **STOP** |
| draft | true |
| observed | 2026-09-16 公開 GET |

## Gap vs prior packs

| 穴（PR#12 / PR#21） | この GET |
|---|---|
| 人材トップ SPA。Google ボタン未描画 | `/sign_up` `/login` を確認。静的 HTML は未描画のまま。公開 JS `2ft1bogak3uo6.js` に `handleClickGoogle` / `signInGoogle` / ラベル **「Googleでサインイン」**。Apple / Facebook も同ファイル |
| ワーカー手数料％が TOS から取れない | ％はまだ無い。第2.1条1 の **タレント無料** は cited。第3.2条は **事業者** プラン料金。企業 LP の「採用手数料 0 円」は事業者向けコピーであり、人材％に転記しない |
| 案件日付 | `/projects/91374` タイトルのみ。本文ローダー。**needs_check のまま** |

人が公開案件の日付を 1 画面見てから CU を進める。見えないまま pass にしない。

## CU handoff（この机）

やってよい（下書きのみ・後続 CU）:

1. **人材** https://talent.aw-anotherworks.com/ だけ。`cl.aw-anotherworks.com` の企業デモ・資料は閉じる
2. `/sign_up` で **Googleでサインイン** が見えたら Google。`rimone0511@gmail.com` only。初回と違う SNS で入らない
3. Google が死んでいたら park（メール欄の有無はライブで `needs_check`。無い SNS を新規作成しない）
4. プロフィール下書き。TOS 第2.1条2 は一部項目が登録事業者へ公開されると書く。追加の公開トグルがあればオフ
5. エントリーしない

使わない: 企業向け「無料で人材データベースを見てみる」。法人デモ。

## Field map（プレースホルダ）

| 画面の項目（公開情報ベース） | 貼る値 | 必須見込み | メモ |
|---|---|---|---|
| 登録経路 | Google（目視できれば） | 必須 | 公開 JS ラベル「Googleでサインイン」 |
| メール | `{{EMAIL}}` | 高 | |
| 氏名 | `{{LEGAL_NAME_KANJI}}` | 高 | |
| ニックネーム | `{{DISPLAY_NAME}}` | 画面による | |
| 自己紹介 | 下記 200 / 800 | 高 | |
| 職種・経験 | 業務自動化 / エンジニア寄り | 高 | |
| スキル | Claude Code, Codex, Python, API, 技術記事, 自動化設計 | 高 | |
| 希望単価 | 空または要相談 | 任意 | 未確認の月額を書かない |
| 稼働 | リモート、週次は要相談 | 任意 | |
| 顔写真 | `{{PHOTO_LOCAL_PATH}}` | 任意 | |
| ポートフォリオ | `{{PORTFOLIO_URL}}` `{{GITHUB_REPO_AUTOPILOT}}` | 任意〜高 | |
| 居住地 | `{{PREFECTURE}}` | 任意 | |
| 転職意向 | 複業・業務委託（転職ではない） | 任意 | 画面の選択肢に合わせる |
| 非表示企業 | `{{BLOCK_COMPANY_NAMES}}` | 任意 | 実名をこの PR に書かない |

共通プレースホルダは [INDEX.md](INDEX.md)。

## JA bio 200（200字）

```
石田祐太。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIによる業務自動化の手順・つまずき・確認できた結果を、むずかしい言葉を避けて公開しています。公式APIだけを使う動画アップロード道具も公開中です。ブラウザ自動操作はしません。人が検品できる形で、繰り返し作業を自動化します。リモート可。未確認の数字は書きません。公開は人が決めます。秘密は貼りません。根拠を残す方針です。
```

## JA bio 800（800字）

```
石田祐太（Yuta Ishida）です。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIを使って毎日の作業を自動化する手順、つまずいた点、確認できた結果を、むずかしい言葉を避けて公開しています。売り物は「動いたように見える自動化」ではなく、人が検品できる仕組みです。公開している実録と道具を、業務委託の成果物の根拠にします。提供できること：（1）繰り返し作業の自動化設計。目的・範囲・合格条件・停止条件を先に切り、実装後に回帰確認まで残します。（2）Claude CodeやCodexなど、AIに実装を任せるときの指示の書き方、検品、失敗時の切り分け。（3）YouTubeとTikTokへの公式API投稿の仕組みづくり。ブラウザ自動操作とスクレイピングは対象外です。（4）鍵の扱い、公開事故、トークン期限など、自動化が止まりやすい箇所の点検。公開している道具の例：Autopilot Log（https://github.com/rimone0511/autopilot-log）。YouTube Data API v3 と TikTok Content Posting API のみを使い、投稿の門番は壊れても非公開側に倒れます。受けないこと：いいねやフォローの自動化、権利のない投稿代行、本人確認書類・口座・マイナンバーの代理入力、未確認のままの公開。進め方はテキスト中心です。根拠と反証を残し、公開スイッチは依頼者または本人の手に置きます。リモート可。週次の稼働時間は案件ごとに相談します。未確認の件数や年数は書きません。確認できた公開物だけを貼ります。秘密はチャットに出さず、本人の安全な入力経路だけを使います。日本語でのやり取りを標準にします。英語の一次資料は必要なら要約して渡します。契約前に範囲外を一文で確定します。納期は着手前に合意します。作業の記録を残す。
```

## Fees — official public pages only

| Claim | Status | Source | Quote / note |
|---|---|---|---|
| 登録タレントは無料で利用 | **cited** | TOS 第2.1条1 https://cl.aw-anotherworks.com/user_tos | 「登録タレントは、タレント利用契約の有効期間中、本規約に従って、…本サービスを無料で利用することができます。」 |
| 事業者の利用料金 | **cited（％なし）** | TOS 第3.2条 | プランに従って事業者が支払う。料率は「当社が別途定める」。**人材プロフィールに転記しない** |
| 成功報酬無料（採用） | **cited — 事業者定義** | TOS 第1.2条(16)(18) | 登録事業者が人材にアプローチした上での採用コピー。**ワーカー成果報酬％ではない** |
| 人材の成果報酬％ | **needs_check** | 公開 TOS に％なし | ブログ / Play の「無料」を確定値にしない |

## STOP-AT-KYC

ここまでやってよい: 人材側の登録、プロフィール下書き、ブロック企業、ポートフォリオ URL。

ここで止める:

- 身分証アップロード
- 口座
- 源泉・マイナンバー
- TOS 第1.3条7 の資料提出
- 企業からの契約書で本人確認が必須になった時点
- 案件エントリー

マッチング後の直接契約でも、発注者の本人確認は STOP。

## thin_site_skip

false。2026-09-16 に talent `/sign_up` HTTP 200。企業 TOS 公開中。SPA で日付が読めないだけ。
