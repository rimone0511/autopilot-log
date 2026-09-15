# B16 / CU-27 — Skill Shift（スキルシフト）CU desk

Desk: Skill Shift  
Official host: **`www.skill-shift.com`**（`skillshift.jp` は 2026-09-16 DNS 失敗。使わない）  
CU serial: **CU-27**（INDEX）。この deep pack では先頭  
Checked: 2026-09-16（公開 HTML / 規約 / 公開 `app.js` ラベル / 公開 `GET /api/jobs`）  
Mode: **DRAFT ONLY** — fill, save, **never apply**  
Language: **日本語**  
Google: **NOT_OFFERED_OAUTH** → メール = MAIN Gmail  
OTP: 仮登録メール → **Gmail parent**. SMS → **user chat**（携帯連絡先が OTP なら）  
activity_gate: **pass**（PR#12）

Operator（規約）: 株式会社みらいワークス。個人情報保護方針リンクは `mirai-works.co.jp/aboutus/policy/`（フッター）。  
`skillshift.global` は別法人（NL）。開かない。

---

## 0. How far to go (then stop)

1. Confirmed URL → 個人登録。企業会員・パートナー・資料請求フォームに入らない。
2. メール = `{{EMAIL}}`（MAIN Gmail）。**Facebookで登録する** は使わない。
3. 公開 JS が必須としている欄を貼る（section 3）。パスワードはローカル台帳。git に書かない。
4. 仮登録メール: parent Gmail。本登録 URL を同じプロファイルで開く。
5. 本登録後のプロフィール編集で 200/800 と公開 URL。**応募しない。**
6. **STOP** at 本人確認サービス / 審査書類 / 口座。[STOP-KYC.md](STOP-KYC.md)。
7. Success line (section 6). Then SOKUDAN.

現場のみ・常駐のみの求人行は見ても応募しない（ゲート: 机全体は現地労働 SKIP にしないが、行単位で避ける）。

Timebox: 15–25 minutes. Stuck > 10 minutes: park, next.

---

## 1. URLs

### Confirmed (use these)

| What | URL |
|---|---|
| Home | https://www.skill-shift.com/ |
| 個人登録 | https://www.skill-shift.com/sign-up |
| Login | https://www.skill-shift.com/login |
| 利用規約 | https://www.skill-shift.com/terms-of-service |
| 公開求人 API（ログイン不要。件数は書かない） | https://www.skill-shift.com/api/jobs |

### Guess only

```
{{URL_GUESS_SKILLSHIFT_PROFILE_EDIT}}   # 公開 JS: 本登録後「プロフィール編集画面へ」。ライブメニューを正とする
{{SIGNUP_URL_GUESS_SKILLSHIFT_GOOGLE}}  # UNCONFIRMED — 公開 JS に Google OAuth 無し。発明しない
```

---

## 2. Google MAIN notes (this desk)

公開観測:

- 個人登録コンポーネント `name:"sign-up"`。ラベル **「Facebookで登録する」** あり。
- `oauth` 文字列なし。`beforeRouteEnter` は `provider` クエリで **facebook_id / facebook_token** を埋める。
- Google 文字列は Tag Manager / Maps / Forms のみ。

方針:

1. https://www.skill-shift.com/sign-up
2. **メールアドレスで登録**（ラベルどおり）。メール = `rimone0511@gmail.com`
3. Facebook を新規紐付けしない。Google ボタンが **目視で出たら** そのときだけ PREFER_GOOGLE に上げ、パックを直す。出なければメールのまま。
4. パスワード: 公開ラベル「英大文字、英小文字、記号、数字を含む8文字以上」。値は `{{PASSWORD_DO_NOT_STORE}}`。画面に出しても git に残さない。
5. 同意: 利用規約 + プライバシーポリシー。
6. ボタン「個人登録する」→ 確認「確認して仮登録する」。**この authoring セッションでは押さない。** CU 直列だけ。
7. Press & Hold / WAF: `holdDurationMs: 1800`。

Already a member with MAIN Gmail: ログイン。二件目を作らない（規約第3条6: 原則1アカウント）。

---

## 3. Profile paste fields (JP)

出典: 公開 `app.js` の必須バリデーションと確認画面ラベル（送信していない）。ライブフォームを正とする。

| 画面の項目（公開 JS） | 貼る値 | 必須見込み | メモ |
|---|---|---|---|
| 登録経路 | メール（MAIN Gmail） | 必須 | Google OAuth 未確認 |
| 性（姓） | `{{LEGAL_NAME_KANJI}}` の姓 | 必須 | 公開 JS `lastName` |
| 名 | `{{LEGAL_NAME_KANJI}}` の名 | 必須 | `firstName` |
| セイ | `{{LEGAL_NAME_KANA}}` のセイ | 必須 | |
| メイ | `{{LEGAL_NAME_KANA}}` のメイ | 必須 | |
| 性別 | `{{GENDER_FORM_VALUE}}`（男性/女性） | 必須に近い | 公開デフォルト gender:1。未指定可なら空にしないで画面の任意を正とする |
| 生年月日 | `{{BIRTH_YEAR}}` / `{{BIRTH_MONTH}}` / `{{BIRTH_DAY}}` | 必須 | |
| 現住所 郵便番号 | `{{POSTAL_CODE}}` | 高 | 〒→住所 |
| 都道府県 | `{{PREFECTURE}}` | 必須 | 一覧に「海外」あり |
| 市区町 | `{{CITY}}` | 必須 | |
| 番地・建物 | `{{STREET_ADDRESS}}` | 任意〜高 | 下書きに番地が要らなければ空。git に番地を書かない |
| 出身地 | `{{BIRTHPLACE}}` | 必須 | 公開ラベル「出身地（必須）」 |
| 現在の業務形態 | 画面の最寄り。個人なら「兼業（個人事業主としてのみ活動している方）」。雇用があるなら「副業（雇用契約を締結している法人がある方）」。**未確認なら「その他」** | 必須 | 雇用を創作しない |
| スキル | 少なくとも1つ。IT・業務改善に近い公式チップ + その他スキルに `業務自動化`, `n8n`, `Claude Code`, `公式API` | 必須 | 公開: 「少なくとも１つ以上、選択してください。」その他は Enter 確定 |
| メールアドレス | `{{EMAIL}}` | 必須 | |
| 携帯連絡先 | `{{PHONE}}` | 必須 | 公開注記: 応募時に地方企業へ公開され連絡がスムーズ、とある。**このパックは応募しない。** OTP なら SMS=user |
| パスワード | ローカルのみ | 必須 | |
| お気に入り地域 `fav_area` | `{{FAV_AREA}}` または空 | 任意 | 未確認なら空。現地通勤を約束する文を書かない |
| 職務経歴 `job_histories` | 公開実録の範囲だけ。年数創作禁止 | 本登録後 | `company_name` / `position` / 期間。秘密の社内名は `{{BLOCK_COMPANY_NAMES}}` |
| 顔写真 `avatar` | `{{PHOTO_LOCAL_PATH}}` | 任意 | 身分証禁止 |
| 自己紹介（プロフィール編集） | 下記 200 / 800 | 高 | 公開 JS 本登録後「プロフィールを充実させましょう」 |
| ポートフォリオ | `{{PORTFOLIO_URL}}` `{{GITHUB_REPO_AUTOPILOT}}` | 高 | |
| 応募・メッセージ | やらない | STOP | |

規約の会員連絡先情報: 住所・氏名・電話・メール（第1条11）。だから住所欄は出る。番地まで強制なら埋めるが git には残さない。

スキルの公式チップ例（公開サインアップ面の検索スニペット、2026-09-16）: 商品・サービス企画開発 / 市場調査・ユーザー調査 / ブランド構築・デザイン監修 / 新規顧客開拓・リード獲得 / 取引先・販売チャネル開拓支援。自動化がチップに無いときは **その他のスキル** に書く。未経験を経験と書かない。

### キャッチ（短い欄があれば）

```
AI業務自動化と手順書。公式APIのみ。リモート前提。現地常駐は受けない
```

### JA bio 200

```
石田祐太。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIによる業務自動化の手順・つまずき・確認できた結果を、むずかしい言葉を避けて公開しています。公式APIだけを使う動画アップロード道具も公開中です。ブラウザ自動操作はしません。人が検品できる形で、繰り返し作業を自動化します。リモート可。未確認の数字は書きません。公開は人が決めます。秘密は貼りません。根拠を残す方針です。
```

### JA bio 800

```
石田祐太（Yuta Ishida）です。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIを使って毎日の作業を自動化する手順、つまずいた点、確認できた結果を、むずかしい言葉を避けて公開しています。売り物は「動いたように見える自動化」ではなく、人が検品できる仕組みです。公開している実録と道具を、業務委託の成果物の根拠にします。提供できること：（1）繰り返し作業の自動化設計。目的・範囲・合格条件・停止条件を先に切り、実装後に回帰確認まで残します。（2）Claude CodeやCodexなど、AIに実装を任せるときの指示の書き方、検品、失敗時の切り分け。（3）YouTubeとTikTokへの公式API投稿の仕組みづくり。ブラウザ自動操作とスクレイピングは対象外です。（4）鍵の扱い、公開事故、トークン期限など、自動化が止まりやすい箇所の点検。公開している道具の例：Autopilot Log（https://github.com/rimone0511/autopilot-log）。YouTube Data API v3 と TikTok Content Posting API のみを使い、投稿の門番は壊れても非公開側に倒れます。受けないこと：いいねやフォローの自動化、権利のない投稿代行、本人確認書類・口座・マイナンバーの代理入力、未確認のままの公開。進め方はテキスト中心です。根拠と反証を残し、公開スイッチは依頼者または本人の手に置きます。リモート可。週次の稼働時間は案件ごとに相談します。未確認の件数や年数は書きません。確認できた公開物だけを貼ります。秘密はチャットに出さず、本人の安全な入力経路だけを使います。日本語でのやり取りを標準にします。英語の一次資料は必要なら要約して渡します。契約前に範囲外を一文で確定します。納期は着手前に合意します。作業の記録を残す。
```

Skill Shift 向けの足し（プロフィールに余白があれば。件数は書かない）:

```
地方企業のDX・業務棚卸し・自動化の伴走は、オンライン打ち合わせを前提にします。月1回の現地が必須の行は、応募前に人が判断します。移住前提の約束はしません。独立した個人です。みらいワークスの社員ではありません。
```

---

## 4. Fees — official public pages only

| Claim | Status | Source | Quote / note |
|---|---|---|---|
| 個人の会員登録・提案は無料 | **cited** | 規約第9条 https://www.skill-shift.com/terms-of-service | 「本サイトは、会員登録、個人会員による提案は無料でご利用頂けます。（2020年4月現在）企業会員が利用する場合のみ掲載料をお支払い頂きます。」日付が古い。**料率改定の有無は needs_check**（貼る直前に規約を再読） |
| 個人の成果報酬％ / 仲介マージン | **needs_check** | 同規約に個人向け％なし | 第23条7に「弊社が受領した手数料」とあるが **数字なし**。記憶やブログの％を書かない |
| 企業の掲載料の金額 | **needs_check** | 第9条は「掲載料」のみ | 人材側パックでは触らない |

Do not paste a take-rate into the profile.

---

## 5. Explicit do-not (this desk)

- 求人への応募（規約上の「提案」）
- Facebook 新規登録
- 企業会員登録・お問い合わせ資料請求を個人登録の代わりにする
- 本人確認サービスの資料
- 口座
- 現場常駐のみの行への応募
- `skillshift.jp` / `skillshift.global`

---

## 6. What success looks like **before SOKUDAN**

| Outcome | Meaning |
|---|---|
| `done-draft` | MAIN Gmail で本登録。プロフィール下書き。応募なし。KYC なし |
| `already_member_draft` | 同じメールで既存。プロフィール確認。公開しない |
| `kyc_wait` | 書類画面。閉じて朝へ |
| `sms_wait_user` | 携帯 OTP。ユーザー不在 |
| `otp_missing` | 仮登録メールなし |

```
desk: SkillShift
pack: earn-skillshift-sokudan-menta-deep-20260916/01-skill-shift.md
auth: email-same-mailbox | already_member | blocked
otp: gmail-parent | sms-chat | none | otp_missing | sms_wait_user
kyc: none | wait-morning + type
draft_profile: yes/no
publish: no
apply: no
next: SOKUDAN
```
