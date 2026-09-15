# FIELD-MAP — SOKUDAN 人材 下書き（safe JA paste）

> **DRAFT_ONLY.** Paste-ready JA. No secrets. Live form wins.  
> **REGISTER-CU-CUT.** Do not open SOKUDAN to paste these now. Prefer JOBS. See [STATUS.md](STATUS.md).  
> Seller-brand = 石田祐太 / ユタラボ / 公式APIのみ / 人が検品できる仕組み。  
> **生年月日と電話番号は創作しない。このファイルに実値を書かない。CU は打たない。**  
> 実パスワード・OTP・番地・口座・身分証番号も **このリポジトリに書かない**。

CU 手順: [CHECKLIST.md](CHECKLIST.md)  
Desk box: [STATUS.md](STATUS.md)

公式の自己紹介字数は公開 FAQ に無い（**needs_check**）。超過したら短いフェンスへ降りる。URL も字数に含む。

---

## Shared placeholders

Replace locally. Never commit filled private values.

```
{{FULL_LEGAL_NAME}}
{{LEGAL_NAME_KANJI}}
{{LEGAL_NAME_KANA}}
{{DISPLAY_NAME}}
{{EMAIL}}
{{GOOGLE_ACCOUNT_EMAIL}}
{{PASSWORD_DO_NOT_STORE}}
{{COUNTRY}}
{{PREFECTURE}}
{{CITY}}
{{PHONE}}                 # EMPTY — do not paste. required → phone_required_stop
{{BIRTH_YEAR}}            # EMPTY — do not paste. required → dob_required_stop
{{BIRTH_MONTH}}
{{BIRTH_DAY}}
{{PHOTO_LOCAL_PATH}}
{{PORTFOLIO_URL}}
{{GITHUB_URL}}
{{GITHUB_REPO_AUTOPILOT}}
{{YEARS_AUTOMATION_PUBLIC}}
{{HOURLY_JPY}}
{{INVITE_CODE}}
```

Public defaults（ログイン識別と公開 URL だけ。受信箱の中身は秘密）:

| Token | Public default |
|---|---|
| `{{GOOGLE_ACCOUNT_EMAIL}}` / `{{EMAIL}}` | `rimone0511@gmail.com` |
| `{{DISPLAY_NAME}}` | `石田祐太` |
| `{{COUNTRY}}` | `Japan` |
| `{{PORTFOLIO_URL}}` | `https://yutalab.dev/` |
| `{{GITHUB_URL}}` | `https://github.com/rimone0511` |
| `{{GITHUB_REPO_AUTOPILOT}}` | `https://github.com/rimone0511/autopilot-log` |
| `{{HOURLY_JPY}}` | **empty** — 円額を創作しない |
| `{{YEARS_AUTOMATION_PUBLIC}}` | **empty** — 未確認なら空 |
| `{{INVITE_CODE}}` | **empty** |
| `{{PHONE}}` | **empty — do not invent, do not type** |
| `{{BIRTH_YEAR}}` `{{BIRTH_MONTH}}` `{{BIRTH_DAY}}` | **empty — do not invent, do not type** |

Sibling thick pack ([PR#33](https://github.com/rimone0511/autopilot-log/pull/33)) maps phone/DOB as 「高」必須見込み. **This live checklist overrides that for CU:** leave blank; if the live form blocks save, park instead of filling.

---

## One-liners（brand）

キャッチ（**30** 字。計測 2026-09-16）:

```
AI業務自動化と手順書。公式APIのみ。ブラウザ自動操作なし
```

短い欄（**12** 字）:

```
公式API自動化と手順書
```

連絡先・「リモート92%」・仲介手数料ゼロ・マッチング日数を足さない。

---

## A. Signup（公開面 — 観測済み）

出典: https://sokudan.work/signup/pro GET 200（2026-09-16）。POST していない。

| 画面の項目 | 貼る値 | 必須 | Evidence |
|---|---|---|---|
| 経路 | **Google で登録** | このパックでは必須 | `alt="Google で登録"` `/users/auth/google?category=signup&usage_type_id=1` |
| Facebook で無料登録 推奨 | **skip** | — | 推奨バッジあり。使わない |
| LinkedIn / X / GitHub | **skip** | — | 新規身分にしない |
| メールアドレス | `{{EMAIL}}` | メール経路のみ | `#user_email` placeholder `メールアドレス` |
| パスワード | `{{PASSWORD_DO_NOT_STORE}}` | メール経路のみ | 英数含む8文字以上。git に書かない |
| メールで無料登録 | メール経路の submit | メール経路 | `form action="/signup"`。authoring は押さない |
| `user[usage_type_id]=1` | 触らない | 人材面がセット | hidden |
| 利用規約 / プライバシー | 人が読む | 同意みなし文言あり | `/pages/terms` `/pages/policy`。「上記に同意してご利用ください」 |
| reCAPTCHA | 人待ち | メール経路 | 登録面にウィジェット。sitekey をコミットしない |
| 電話 | **この画面に無い** | — | 公開 STEP に `input` 電話なし |
| 生年月日 | **この画面に無い** | — | 公開 STEP に DOB なし |

ログイン面（既存会員）: https://sokudan.work/login — **Google でログイン** `/users/auth/google?category=login`。見出し「全ユーザー共通」。

---

## B. After login — プロフィール（未観測ラベル + 取得しうる種類）

ログイン後フォームは壁の向こう → **needs_check**。下表はプライバシー第2条の **種類** と公開コピーからの見込み。ライブラベルが違えば画面を正とする。

プライバシー（https://sokudan.work/pages/policy 第2条）が取得しうると書くもの: 氏名、性別、**生年月日**、住所、メールアドレス、**電話番号**、就業形態、就業先及び役職、紹介文（プロフィール画像、職歴、自己PR、SNS、表彰、資格等）、クレジットカード、パスワード。これは **必須チェックリストではない**。

| 画面の項目（見込み） | 貼る値 | 必須見込み | メモ |
|---|---|---|---|
| 氏名 | `{{LEGAL_NAME_KANJI}}` | 高 | 実名。書類は上げない |
| 氏名カナ | `{{LEGAL_NAME_KANA}}` | needs_check | 無ければ skip |
| 表示名 | `{{DISPLAY_NAME}}` = `石田祐太` | 高 | |
| 性別 | ライブ必須だけ | needs_check | 空可なら空 |
| **生年月日 / 生年月** | **空** | 任意=skip / 必須=`dob_required_stop` | **打たない。創作しない** |
| 居住地 | `{{PREFECTURE}}` `{{CITY}}` | 高 | 番地は出さない |
| **電話番号** | **空** | 任意=skip / 必須=`phone_required_stop` | **打たない。SMS しない** |
| 職種 | エンジニア / 自動化 / 業務改善の最寄りチップ | 高 | 「AI」だけにしない |
| 所有スキル | 下記リスト | 高 | チップが無ければ書かない |
| 経験年数 | 空 | 高〜任意 | `{{YEARS_AUTOMATION_PUBLIC}}` empty |
| キャッチ | 上記 30 / 12 | 任意〜高 | |
| 自己紹介 / 自己PR | 下記 200（既定）/ 800 | 高 | AI生成（規約第7条）を使うなら保存前に人が直す |
| 職歴 | 公開実録だけ。年数創作禁止 | 任意 | |
| 資格 | 空（未確認） | 任意 | 持っていない資格を書かない |
| ポートフォリオ / SNS | 公開 URL 3つ | 任意〜高 | yutalab / github / autopilot-log |
| プロフィール画像 | `{{PHOTO_LOCAL_PATH}}` | 任意 | KYC 自撮りは不可。コミット禁止 |
| 稼働条件 | リモート可。週次は要相談 | 高 | |
| 招待コード | 空 | 任意 | |
| 所属企業名 | 人が決める。git に書かない | 任意 | FAQ: 同じ会社名同士は互いに見えない |
| 公開設定 | 非公開 / 下書き | あれば必須 | |
| 応募 | やらない | STOP | [CHECKLIST.md](CHECKLIST.md) §7 |
| 審査書類 | やらない | STOP | 規約第4条・第14条 |
| 発注機能 | やらない | STOP | `business.sokudan.work` |
| クレジットカード | やらない | STOP | ポリシー記載 ≠ 今入力 |

---

## C. Paste — 自己紹介（URL あり。自己紹介が URL を受け付けるときの既定）

計測は UTF-8 文字数（2026-09-16）。電話番号・生年月日・社名・秘密は含まない。

### JA bio 200（既定。**200** 字）

```
石田祐太。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIによる業務自動化の手順・つまずき・確認できた結果を、むずかしい言葉を避けて公開しています。公式APIだけを使う動画アップロード道具も公開中です。ブラウザ自動操作はしません。人が検品できる形で、繰り返し作業を自動化します。リモート可。未確認の数字は書きません。公開は人が決めます。秘密は貼りません。根拠を残す方針です。
```

### JA bio 800（カウンターがそれ以上のときだけ。切って使う。**800** 字）

```
石田祐太（Yuta Ishida）です。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIを使って毎日の作業を自動化する手順、つまずいた点、確認できた結果を、むずかしい言葉を避けて公開しています。売り物は「動いたように見える自動化」ではなく、人が検品できる仕組みです。公開している実録と道具を、業務委託の成果物の根拠にします。提供できること：（1）繰り返し作業の自動化設計。目的・範囲・合格条件・停止条件を先に切り、実装後に回帰確認まで残します。（2）Claude CodeやCodexなど、AIに実装を任せるときの指示の書き方、検品、失敗時の切り分け。（3）YouTubeとTikTokへの公式API投稿の仕組みづくり。ブラウザ自動操作とスクレイピングは対象外です。（4）鍵の扱い、公開事故、トークン期限など、自動化が止まりやすい箇所の点検。公開している道具の例：Autopilot Log（https://github.com/rimone0511/autopilot-log）。YouTube Data API v3 と TikTok Content Posting API のみを使い、投稿の門番は壊れても非公開側に倒れます。受けないこと：いいねやフォローの自動化、権利のない投稿代行、本人確認書類・口座・マイナンバーの代理入力、未確認のままの公開。進め方はテキスト中心です。根拠と反証を残し、公開スイッチは依頼者または本人の手に置きます。リモート可。週次の稼働時間は案件ごとに相談します。未確認の件数や年数は書きません。確認できた公開物だけを貼ります。秘密はチャットに出さず、本人の安全な入力経路だけを使います。日本語でのやり取りを標準にします。英語の一次資料は必要なら要約して渡します。契約前に範囲外を一文で確定します。納期は着手前に合意します。作業の記録を残す。
```

---

## D. Paste — URL 無し（自己紹介が URL を弾くとき）

公開 URL はポートフォリオ欄へ。

### JA bio nourl（**185** 字）

```
石田祐太。個人サイト「ユタラボ」で、AIによる業務自動化の手順・つまずき・確認できた結果を、むずかしい言葉を避けて公開しています。公式APIだけを使う動画アップロード道具も公開中です。ブラウザ自動操作はしません。人が検品できる形で、繰り返し作業を自動化します。リモート可。未確認の数字は書きません。公開は人が決めます。秘密は貼りません。公開URLはポートフォリオ欄です。
```

---

## E. Skills（プロフィール欄のみ。案件応募ではない）

画面がチップ選択なら **存在するチップだけ**。自由記述なら 1行ずつ。無いものは書かない。未経験を経験と書かない。

```
業務自動化
n8n
Python
Claude Code
Codex
YouTube Data API v3
TikTok Content Posting API
手順書
公式API
```

職種チップの最寄り: エンジニア / 自動化 / 業務改善 / バックエンド などライブにあるもの。FAQ「AIエンジニアやAIコンサルタント…CXO」は **マーケ**。自分の肩書に CXO を足さない。

---

## F. Fees — official public pages only（フォームに貼らない）

| Claim | Status | Source | Quote / note |
|---|---|---|---|
| 人材側の利用は無料 | **cited** | トップ FAQ「サービスを利用するのに、費用はかかりますか？」 https://sokudan.work/ | 「すべて無料でご利用いただけます。採用担当者としてご利用する場合は、こちらからお問い合わせください。」 |
| 登録面の「無料新規登録」 | **cited** | https://sokudan.work/signup/pro | 見出し「無料新規登録」／「メールで無料登録」 |
| 仲介マージン％ | **needs_check** | 規約第10条 https://sokudan.work/pages/terms | 「本サービス利用料」「委託料に含まれる当社の手数料の料率」とあるが **％は未記載**。創作しない |
| メタ / トップ「リモート案件 92%」 | **do not cite as personal proof** | トップ・description | 自己紹介にコピーしない |
| FAQ「２-3週間程度で決定」 | **do not paste** | トップ FAQ | 自分の実績にしない |
| 規約第24条 違約金（50万円 / 200万円） | **cited unused** | `/pages/terms` | 直接契約禁止の話。bio に書かない。今は取引しない |

Do not type CrowdWorks / Lancers % onto this desk. `{{HOURLY_JPY}}` stays empty.

---

## G. Do not paste (this pack)

- 生年月日・生年月・年齢の数字
- 電話番号・SMS コード
- 番地・マイナンバー・口座・カード番号
- 「リモート92%」「仲介手数料ゼロ」「1,000名突破」を実績のように見せる文
- 連絡先（メール / LINE / 携帯）を自己紹介本文へ
- 応募文・スカウト返信
- 社名（就業規則は人が確認。git に書かない）
