# B5 / CU-15 — Anycrew（エニィクルー）CU desk

Desk: Anycrew  
CU serial: **CU-15**  
Checked: 2026-09-16（`app.any-crew.com` 公開 HTML、www 規約・プライバシー）  
Mode: **DRAFT ONLY**  
Language: **日本語**  
Google: **PREFER_GOOGLE**  
OTP: 確認メールがあれば **Gmail parent**  
activity_gate: **needs_check**（`/offers` は SPA 空。人が 1 画面見てから）  
Operator: エニィクルー株式会社（規約）

**人材側だけ。** `biz.any-crew.com` は閉じる。

---

## 0. How far to go (then stop)

1. Human: 公開の求人カードまたは登録面が開くことを 1 回見る（ゲート needs_check）。見えなければ park。
2. https://app.any-crew.com/ → **Googleでログイン** / 利用登録。
3. 登録ユーザー（仕事を受ける側）。求人事業者にしない。
4. プロフィール下書き。公開トグルがあれば非公開。
5. 職務経歴書が必須なら後回し。身分証なら STOP。
6. 応募しない。
7. Success line. Then MENTA.

Timebox: 15–25 minutes.

---

## 1. URLs

### Confirmed

| What | URL |
|---|---|
| 人材アプリ | https://app.any-crew.com/ |
| マーケ | https://www.any-crew.com/ |
| 利用規約 | https://www.any-crew.com/terms （2024-11-14 改訂が公開面に出ている） |
| プライバシー | https://www.any-crew.com/privacy |
| 企業コンソール | https://biz.any-crew.com/ — **使わない** |

### Guess only

```
{{URL_GUESS_ANYCREW_PROFILE}}
{{URL_GUESS_ANYCREW_GOOGLE_OAUTH}}   # ボタンは確認。deep link は発明しない
```

`https://www.any-crew.com/faq` は 2026-09-16 に **404**。FAQ 本文はアプリトップを正とする。

---

## 2. Google MAIN notes (this desk)

公開アプリ HTML:

- 「FacebookかGoogleのアカウントで利用登録」
- モーダル「Googleでログイン」
- メール + パスワード欄もある（「メールアドレスとパスワードを入力してください」）

規約第3条1: **登録には外部 SNS サービスで登録されたアカウントを使用**。第2条(11) の例示は Facebook「その他当社が定めるもの」。公開面は Google を明示。

方針:

1. **Googleでログイン** を押す。`rimone0511@gmail.com` only.
2. Facebook を新規作成・新規紐付けしない。Google が失敗したら **park**（メール欄があっても、規約が SNS 登録を主経路と書く。メールだけで通るかは `needs_check`）。
3. 同意は profile/email。Drive 等は拒否。
4. 既登録ならログイン。二件目禁止。
5. Hold: `holdDurationMs: 1800`.

---

## 3. Profile paste fields (JP)

プライバシーポリシーの収集項目（登録ユーザー）: 氏名、メールアドレス、所属企業・団体、過去の職歴、職業、転職・就職活動の意向、生年月日等。外部 SNS のメール。

| 画面の項目（公開情報ベース） | 貼る値 | 必須見込み | メモ |
|---|---|---|---|
| 登録経路 | Google | 必須 | |
| 氏名 | `{{LEGAL_NAME_KANJI}}` | 高 | |
| メール | `{{EMAIL}}` | 高 | Google から来る。確認リンクは親が CU へ渡す |
| 生年月日 | `{{BIRTH_YEAR}}-{{BIRTH_MONTH}}-{{BIRTH_DAY}}` | 任意〜高 | ポリシーに生年月日 |
| 所属・職歴 | 公開実録の範囲 | 高 | 公式 FAQ: 通常は職務経歴書不要 |
| 職業 | 業務自動化 / エンジニア | 高 | |
| 転職意向 | **複業・業務委託**（転職エージェント化しない） | 任意 | ポリシーに「転職・就職活動の意向」 |
| 自己紹介 | 下記 200 / 800 | 高 | |
| ポートフォリオ | `{{PORTFOLIO_URL}}` `{{GITHUB_REPO_AUTOPILOT}}` | 任意 | |
| 職務経歴書アップロード | スキップ | 任意 | エージェント案件で必須なら STOP-lite（応募しないので通常出ない） |
| 公開範囲 | 非公開 / 下書き | 高 | |

公式 FAQ（アプリ）: 「Web上でプロフィールを入力頂くだけで、面談や職務経歴書は不要です。ただし、エージェントが仲介をする一部の案件では応募時に、面談や職務経歴書が必要になります。」  
このパックは応募しないので、仲介案件の書類は触らない。

### キャッチ

```
AI業務自動化と手順書。公式APIのみ。ブラウザ自動操作なし
```

### JA bio 200

```
石田祐太。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIによる業務自動化の手順・つまずき・確認できた結果を、むずかしい言葉を避けて公開しています。公式APIだけを使う動画アップロード道具も公開中です。ブラウザ自動操作はしません。人が検品できる形で、繰り返し作業を自動化します。リモート可。未確認の数字は書きません。公開は人が決めます。秘密は貼りません。根拠を残す方針です。
```

### JA bio 800

```
石田祐太（Yuta Ishida）です。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIを使って毎日の作業を自動化する手順、つまずいた点、確認できた結果を、むずかしい言葉を避けて公開しています。売り物は「動いたように見える自動化」ではなく、人が検品できる仕組みです。公開している実録と道具を、業務委託の成果物の根拠にします。提供できること：（1）繰り返し作業の自動化設計。目的・範囲・合格条件・停止条件を先に切り、実装後に回帰確認まで残します。（2）Claude CodeやCodexなど、AIに実装を任せるときの指示の書き方、検品、失敗時の切り分け。（3）YouTubeとTikTokへの公式API投稿の仕組みづくり。ブラウザ自動操作とスクレイピングは対象外です。（4）鍵の扱い、公開事故、トークン期限など、自動化が止まりやすい箇所の点検。公開している道具の例：Autopilot Log（https://github.com/rimone0511/autopilot-log）。YouTube Data API v3 と TikTok Content Posting API のみを使い、投稿の門番は壊れても非公開側に倒れます。受けないこと：いいねやフォローの自動化、権利のない投稿代行、本人確認書類・口座・マイナンバーの代理入力、未確認のままの公開。進め方はテキスト中心です。根拠と反証を残し、公開スイッチは依頼者または本人の手に置きます。リモート可。週次の稼働時間は案件ごとに相談します。未確認の件数や年数は書きません。確認できた公開物だけを貼ります。秘密はチャットに出さず、本人の安全な入力経路だけを使います。日本語でのやり取りを標準にします。英語の一次資料は必要なら要約して渡します。契約前に範囲外を一文で確定します。納期は着手前に合意します。作業の記録を残す。
```

---

## 4. Fees — official public pages only

| Claim | Status | Source | Quote / note |
|---|---|---|---|
| 仕事を受ける側は費用なし | **cited** | https://app.any-crew.com/ FAQ | 「仕事を受けるフリーランス・副業人材の方には一切費用はかかりません。」 |
| 基本無料 | **cited** | 規約第5条 https://www.any-crew.com/terms | 「利用者は、本サービスを基本的に無料で利用することが出来ます。」求人事業者は希望により有料プラン |
| 人材側の成果報酬％ | **needs_check** | 公開規約・人材 FAQ に％なし | 企業向けエージェントは成功報酬と biz 面が書く。**人材プロフィールに転記しない** |

---

## 5. Explicit do-not

- biz コンソール
- 求人への応募
- Facebook だけの新規身分
- 職務経歴書必須の仲介フローを完走する
- 身分証・口座
- 有料プラン（人材側に出ても買わない）

---

## 6. Success before MENTA

```
desk: Anycrew
pack: earn-skillshift-sokudan-menta-deep-20260916/03-anycrew.md
auth: google-main | already_member | blocked
otp: gmail-parent | none | otp_missing
kyc: none | wait-morning + type
draft_profile: yes/no
publish: no
apply: no
next: MENTA
```
