# CU-07 — TimeTicket（タイムチケット）host desk

Desk: TimeTicket  
Role: **ホスト / チケット販売側**。ゲスト専用で終わらない  
Official: https://www.timeticket.jp/  
CU serial: **CU-07**（QUEUE **A7**。INDEX を正とする）  
Checked: 2026-09-16（公開ヘルプ HTTP 200。www は this env curl **202 空**、WebFetch は本文あり。**登録していない**）  
Mode: **DRAFT_ONLY** — fill, save, **never 発行完了**  
Language: **日本語**  
Google: **EMAIL = MAIN Gmail**（OAuth は this env 未確認）  
OTP: 確認メール → **Gmail parent**. SMS → **user chat**  
ticket_mode: **async 優先 = メッセージ**。対面・電話・オンライン・**電話相談チケットは作らない**  
`thin_site_skip: false`

---

## 0. How far to go (then stop)

1. Confirmed URL → ホスト側のユーザー登録。ゲスト専用で止まらない。
2. メール = `{{EMAIL}}`（MAIN Gmail）。LINE / Apple / Facebook を新規紐付けしない。Google ボタンが **目視できたら** PREFER_GOOGLE。
3. プロフィールを field map で埋める。規約第8条: 設定を変えないと公開 → **非公開があればオフ**。
4. キャッチは 23 字。自己紹介は画面カウンターを見て **200 / 255 / 800** から選ぶ。
5. 本人確認（`identifications/edit`）が出たら **アップロードしない**。[STOP-KYC.md](STOP-KYC.md)。
6. 通常チケット下書き。形式は **メッセージのみ**。エリアは **インターネット**。価格は `{{TICKET_PRICE_JPY}}`（空なら `rate_empty`）。
7. **発行して予約可能日時の登録へ** と **チケット発行手続きを完了する** は押さない。下書き保存があればそれを使う。無ければチケットは作らずプロフィールで完了。
8. チケット作成が本人確認必須ならチケットは作らない。プロフィールのみ。

やらない: SNS シェア、LINE 公式連携、予約枠の公開カレンダー、同じ内容の複数発行（ホスト禁止行為）、電話相談チケット。

Timebox: 15–25 minutes. Stuck > 10 minutes: park, next (Contra).

---

## 1. URLs

### Confirmed (use these)

| What | URL |
|---|---|
| Home | https://www.timeticket.jp/ |
| カテゴリー一覧 | https://www.timeticket.jp/categories/ |
| ユーザー登録 | https://www.timeticket.jp/users/sign_up |
| ログイン | https://www.timeticket.jp/users/sign_in |
| 利用規約 | https://www.timeticket.jp/terms |
| 通常チケット | https://help.timeticket.jp/articles/19374 |
| 手数料 | https://help.timeticket.jp/articles/19386 |
| 売る流れ（DM） | https://help.timeticket.jp/articles/19387 |
| 本人確認 | https://help.timeticket.jp/articles/19398 |
| ホスト禁止 | https://help.timeticket.jp/articles/19400 |
| 最低価格 | https://help.timeticket.jp/articles/19461 |
| 電話相談チケット（作らない） | https://help.timeticket.jp/articles/113228 |
| 出金（開かない） | https://help.timeticket.jp/articles/19376 |

### Guess only

```
{{URL_GUESS_TIMETICKET_GOOGLE_OAUTH}}   # UNCONFIRMED — this env signup GET 202 空。発明しない
{{URL_GUESS_TIMETICKET_PROFILE_EDIT}}   # ログイン後メニューを正とする
{{URL_GUESS_TIMETICKET_TICKET_DRAFT}}   # 「チケットを売る」→ 通常チケット。電話相談を選ばない
```

---

## 2. Google MAIN notes (this desk)

公開観測:

- 登録 URL `https://www.timeticket.jp/users/sign_up` は公式導線（トップ「ユーザー登録（無料）」）。this env GET は **202 空**なので、Google / LINE / Apple / メールの並びは **ライブ画面**。
- Google OAuth コールバックをこのパックに書かない。

方針:

1. https://www.timeticket.jp/users/sign_up
2. Google が見えたら MAIN Google。見えなければ **メールアドレスで登録**。メール = `rimone0511@gmail.com`
3. LINE / Apple / Facebook を新規身分にしない。LINE しか無くメールが不可能なら STOP。
4. パスワード: `{{PASSWORD_DO_NOT_STORE}}`。git に残さない。
5. **この authoring セッションでは登録ボタンを押さない。** CU 直列だけ。
6. Press & Hold / 202 壁: `holdDurationMs: 1800`。
7. Already a member with MAIN Gmail: ログイン。二件目を作らない（規約第9条4）。

---

## 3. Profile paste fields (JP)

出典: 公開ヘルプ + 規約。**カウンターと必須マークは画面を正とする**。第三者ブログの「キャッチ 18 字」は **cited しない**（`needs_check`）。

| 画面の項目 | 貼る値 | 必須見込み | メモ |
|---|---|---|---|
| 登録経路 | メール（Google ボタンがあれば Google） | 必須 | MAIN のみ |
| メール | `{{GOOGLE_ACCOUNT_EMAIL}}` | 必須 | |
| パスワード | `{{PASSWORD_DO_NOT_STORE}}` | メール経路 | git に書かない |
| 氏名 / 名前 | `{{LEGAL_NAME_KANJI}}` | 高 | 公開名が分かれるなら表示は `{{DISPLAY_NAME}}` |
| ハンドル / ユーザーネーム | `{{DISPLAY_NAME}}` または `{{HANDLE}}` | 高 | |
| ユーザーURL / ユーザーID | `{{HANDLE}}`（英数。空きを画面で確認） | 高 | 他人の URL を奪わない |
| 生年月日 | `{{BIRTH_YEAR}}` / `{{BIRTH_MONTH}}` / `{{BIRTH_DAY}}` | 高 | |
| 性別 | 画面の選択肢。未設定可なら空 | 任意 | 創作しない |
| 都道府県 | `{{PREFECTURE}}` | 高 | 番地は出さない |
| よくいるエリア | **インターネット** 相当 | 高 | 対面用の駅名を書かない |
| キャッチフレーズ | 下記 short（23 字） | 任意〜高 | 画面上限が短ければ切る |
| 自己紹介 | 下記 200。カウンターが 255 なら 255。それ以上なら 800 を切る | 任意〜高 | 公式字数 **needs_check** |
| 興味カテゴリ | `IT/プログラミング`（カテゴリ一覧に実在） | 任意 | 恋愛 / 占い / インフルエンサートークは選ばない |
| SNS / LINE | 空 | STOP | チケット本文にも書かない |
| 公開設定 | 非公開 / 非表示 | 必須（あれば） | 規約第8条: 未設定だと公開 |
| 本人確認 | やらない | STOP | |

### 通常チケット（下書き。async）

公式: [通常チケットとは？](https://help.timeticket.jp/articles/19374)。カテゴリは [カテゴリー一覧](https://www.timeticket.jp/categories/)。

| 画面の項目 | 貼る値 | 必須見込み | メモ |
|---|---|---|---|
| チケット種別 | **通常チケット** | 必須 | **電話相談チケットは作らない**（ヘルプ 113228。アプリ通話・IT カテゴリ対象外） |
| カテゴリー | `IT/プログラミング` | 必須 | 一覧に実在 |
| サブ（あれば） | `エンジニアのメンタリング` が最寄り。無ければ `その他IT/プログラミング` | 高 | `AI/機械学習/ディープラーニング` は未確認実績を名乗らないなら使わない |
| タイトル | 下記 Title（32 字） | 必須 | 返金文言・連絡先・他チケットの盗用禁止（ホスト禁止） |
| 詳しい説明 | 下記 Body | 必須 | メール・電話・LINE・住所を書かない。カウンターで切る |
| タグ | `自動化`, `公式API`, `n8n`, `手順書`, `非同期` から画面が許す範囲 | 任意 | 存在しないタグを量産しない |
| やり取り形式 | **メッセージ** のみ | 必須 | ヘルプ: 対面 / オンライン / 電話 / メッセージ。このパックはメッセージだけ |
| 開催場所 / エリア | **インターネット** | 必須 | 公式: オンライン・電話・メッセージはインターネット |
| 販売形式 | 時間単価 **または** 定価。画面の既存から選ぶ | 必須 | |
| 価格 | `{{TICKET_PRICE_JPY}}` | 必須になり得る | **実額を git に書かない。** 空で保存可なら空。必須で台帳が空なら `rate_empty` |
| 1回あたり上限 | 空（制限しない） | 任意 | 公式: 未設定時は最大 8 時間。数字を創作して狭めない |
| カバー画像 | フリー素材から無難なもの。自作はローカルのみ | 任意 | 顔・身分証・秘密画面は不可 |
| 公開チェック | **オフ** | 必須 | |
| 予約可能日時 | 登録しない | STOP | 発行フローに入らない |
| 発行完了 | 押さない | STOP | ヘルプ ◇10 / ◇12 のボタン名 |

---

## 4. Paste — bio lengths（測済み）

公式ヘルプに自己紹介の最大字数は無い（**needs_check**）。CU は画面カウンターを正とする。超過したら短いフェンスへ降りる。URL も字数に含む。

### キャッチ（23 字。短い欄）

```
公式APIの自動化を、非同期テキストで切ります
```

### JA bio 200（自己紹介の既定）

```
石田祐太。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIによる業務自動化の手順と確認できた結果を日本語で公開しています。公式APIだけを使う動画アップロードの道具も公開中です。ブラウザ自動操作・スクレイピング・いいね自動化はしません。やりとりはタイムチケットのメッセージ（非同期）です。対面・電話はしません。未確認の数字は書きません。公開は人が決めます。検品できる形です。
```

### JA bio 255（カウンターが 255 前後のとき）

```
石田祐太。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIによる業務自動化の手順と、確認できた結果を日本語で公開しています。公式APIだけを使う動画アップロードの道具も公開中です。ブラウザ自動操作・スクレイピング・いいね自動化はしません。やりとりはタイムチケットのメッセージ（非同期）を使います。対面・電話は提供しません。未確認の数字は書きません。公開スイッチは相手が持ちます。秘密は貼りません。中抜きとサイト外支払いはしません。Zoomは使いません。作業の記録を残します。方針です。
```

### JA bio 800（カウンターがそれ以上のときだけ。切って使う）

```
石田祐太（Yuta Ishida）です。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIを使って毎日の作業を自動化する手順、つまずいた点、確認できた結果を、むずかしい言葉を避けて公開しています。売り物は「動いたように見える自動化」ではなく、人が検品できる仕組みです。公開している実録と道具を、業務委託の成果物の根拠にします。提供できること：（1）繰り返し作業の自動化設計。目的・範囲・合格条件・停止条件を先に切り、実装後に回帰確認まで残します。（2）Claude CodeやCodexなど、AIに実装を任せるときの指示の書き方、検品、失敗時の切り分け。（3）YouTubeとTikTokへの公式API投稿の仕組みづくり。ブラウザ自動操作とスクレイピングは対象外です。（4）鍵の扱い、公開事故、トークン期限など、自動化が止まりやすい箇所の点検。公開している道具の例：Autopilot Log（https://github.com/rimone0511/autopilot-log）。YouTube Data API v3 と TikTok Content Posting API のみを使い、投稿の門番は壊れても非公開側に倒れます。受けないこと：いいねやフォローの自動化、権利のない投稿代行、本人確認書類・口座・マイナンバーの代理入力、未確認のままの公開。この机ではタイムチケットのメッセージ（非同期）だけを使います。Zoom・電話・対面・電話相談チケットは使いません。根拠と反証を残し、公開スイッチは依頼者または本人の手に置きます。未確認の件数や年数は書きません。確認できた公開物だけを貼ります。秘密はチャットに出さず、本人の安全な入力経路だけを使います。日本語でのやり取りを標準にします。契約前に範囲外を一文で確定します。納期は着手前に合意します。中抜きはいたしません。
```

### チケット Title（32 字）

```
公式APIの自動化相談（非同期メッセージ。手順と停止条件を切る）
```

### チケット Body

メール・電話・LINE・外部決済を書かない。中抜きしない。画面カウンターで切る。

```
提供すること
- 毎日のコピー作業を、公式のAPIや n8n のような公式連携で自動化していいかの切り分け
- 目的・範囲・合格条件・止める条件を先に短く切ること
- 実装後の検品の見方（仕様、境界、秘密、権限、再現）
- 公開している実録: https://yutalab.dev/
- 公開している道具の例: https://github.com/rimone0511/autopilot-log （YouTube Data API v3 と TikTok Content Posting API。投稿の門番は壊れても非公開側）

やらないこと
- ブラウザ自動操作、スクレイピング、いいね/フォローの自動化
- 権利のない投稿代行
- 本人確認・口座の代理
- タイムチケット外の現金・振込・外部メッセンジャーでの契約

進め方
- このチケットはメッセージ（非同期）だけです。Zoom・電話・対面は使いません
- 申込の承認後も、場所やツールの話はタイムチケットのダイレクトメッセージに残します
- 秘密はメッセージに貼らず、相手の画面で入力してもらいます

価格と時間は画面の設定に従います。ここに金額や「必ず稼げる」は書きません。
```

---

## 5. Fees and rate placeholders — official public pages only

価格欄に入れるのは **`{{TICKET_PRICE_JPY}}` だけ**。推奨時給をこのパックが決めてはいけない。

| Claim | Status | Source | Quote / note |
|---|---|---|---|
| チケット発行は無料。会員登録料・月会費なし。手数料は支払確定時のみ | **cited** | トップ（WebFetch 2026-09-16）https://www.timeticket.jp/ | 「誰でも無料でチケット発行」「会員登録料・月会費はかかりません。手数料が発生するのは、チケット支払が確定したときのみです。」 |
| ホスト手数料％（2025-08-01 以降の購入申込） | **cited** | https://help.timeticket.jp/articles/19386 | 5万円以下 25%（+税）。5万超10万以下 20%（+税）。10万超 15%（+税）。**プロフィールに貼らない。販売しないので入力不要** |
| `IT/プログラミング` の最低価格 | **cited** | https://help.timeticket.jp/articles/19461 | 時間単価（30分）¥500 / 定価 ¥500。※2023-06-05 一部変更。**下限であり推奨額ではない** |
| 販売価格の上限 | **cited** | https://help.timeticket.jp/articles/19374 | 「カテゴリ最低販売価格 〜 1,000,000円」 |
| 未設定時の 1 回上限 | **cited** | 同 19374 | 設定しない場合最大 8 時間 |
| 電話相談の分単価 | **cited but unused** | https://help.timeticket.jp/articles/113228 | 180円/3分 〜 1,500円/3分。**電話相談を作らないので使わない** |
| 出金の振込手数料 300円 | **cited but unused** | https://help.timeticket.jp/articles/19376 | 出金しない |
| ゲストに見せる販売円額 | **placeholder** | 画面 | `{{TICKET_PRICE_JPY}}`。空で保存。必須ならローカル台帳。台帳が空なら **`rate_empty` で停止**（¥500 を「おすすめ」として埋め込まない） |

Do not paste a take-rate into the profile or ticket body.

---

## 6. Explicit do-not (this desk)

- 電話相談チケット（ヘルプ 113228。アプリ通話。対象は占い / 悩み / フリートーク / インフルエンサー / サブカル）
- 通常チケットに 対面 / 電話 / オンライン（Zoom）を付けること
- 「発行して予約可能日時の登録へ」「チケット発行手続きを完了する」
- 本人確認アップロード、マイナ裏面、出金口座
- LINE / メール / 電話を本文に書くこと
- 同じ内容の複数発行
- 恋愛・占い・お金/副業カテゴリ（最低価格も違う。このパックの仕事ではない）
- `{{TICKET_PRICE_JPY}}` を数字で埋めてコミットすること

---

## 7. What success looks like **before Contra**

| Outcome | Meaning |
|---|---|
| `done-draft` | MAIN Gmail で登録またはログイン。プロフィール下書き。非公開。チケットはメッセージ下書きのみ、またはプロフィールのみ。発行なし。KYC なし |
| `already_member_draft` | 同じメールで既存。プロフィール確認。公開しない |
| `kyc_wait` | identifications/edit。閉じて朝へ |
| `rate_empty` | 価格必須で台帳が空。円額を創作せず停止 |
| `sms_wait_user` | 携帯 OTP。ユーザー不在 |
| `otp_missing` | 確認メールなし |

```
desk: TimeTicket
pack: earn-contra-timeticket-deep-paste-20260916/01-timeticket.md
auth: email-same-mailbox | google-main | already_member | blocked
otp: gmail-parent | sms-chat | none | otp_missing | sms_wait_user
kyc: none | wait-morning + identifications/edit
draft_profile: yes/no
ticket_or_page: tt-message-draft | tt-profile-only | none
async_only: yes
publish: no
apply: no
rate: empty | placeholder-from-ledger | rate_empty
next: Contra
```
