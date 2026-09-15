> DRAFT_ONLY field map. NO login in the authoring session. NO secrets. NO invented credentials.  
> Paste values for CU. Stops: [STOP.md](STOP.md). Step order: [PLAYBOOK.md](PLAYBOOK.md).  
> Labels come from **public signup JS** + **CrowdLinks Help / TOS / プロフィール記入サンプル** (2026-09-16 GET). Live wizard wins.

# FIELD-MAP — CrowdLinks worker / B04

Desk: クラウドリンクス / CrowdLinks B04 / QUEUE Wave B / CU-14  
Livecheck: 2026-09-16 JST, public help + TOS + https://crowdlinks.jp/worker/signup/ (no account created)

`required_guess` is **not** a logged-in required-field dump. Values:

| Token | Meaning |
|---|---|
| `required (docs)` | Help, TOS, or public signup JS names the control as part of creating the worker account |
| `high` | Help / 記入サンプル lists it on プロフィール; draft save may still work without it |
| `optional (docs)` | Help documents skip / later / 任意 |
| `needs_check` | Help is silent or the live widget was not opened logged-in |
| `STOP` | Do not fill. Not a paste target |

Placeholders stay empty of secrets in git. Fill only from the operator’s local ledger at paste time.

**Paste default for this desk:** n8n / AI automation **日本語**. Safe paste = **URL 無し**. Public URLs go to ポートフォリオ. Character counts below are committed Japanese counts (no secrets).

---

## A. Sign up (public JS + FAQ)

Public signup (https://crowdlinks.jp/worker/signup/, retrieved 2026-09-16): title **新規登録【クラウドリンクス】**. Static HTML is a loader. Chunk `signup-654dee2220da40e7.js` this GET:

- **Googleで登録する**
- **Facebookで登録する**
- **メールアドレスで登録する** / **メールアドレスを入力**
- 利用規約 (`/worker/terms/`) および 個人情報の取り扱い (`https://crowdworks.co.jp/privacy_policy/01/`) について同意します
- **同意して会員登録する**
- Password validation copy: **半角の英字、数字、記号を含む8文字以上**

Static HTML does **not** print “Google”. **Click-time: the button must say Googleで登録する.** Else email fallback.

| UI label (help / public JS) | `required_guess` | DRAFT_ONLY paste | Cite / gap |
|---|---|---|---|
| Googleで登録する | preferred path | MAIN `{{GOOGLE_ACCOUNT_EMAIL}}` only. Same Google every later login | Signup JS. FAQ: Google認証の付け替え **不可** |
| Facebookで登録する | `STOP` as new identity | Do not bind a new Facebook | Signup JS `alt:"facebook"` |
| メールアドレスで登録する | fallback `required (docs)` on email path | Same MAIN `{{EMAIL}}`. No new mailbox | Signup JS. FAQ: 連絡用とログイン用が分かれうる → 両方 MAIN で揃える |
| パスワード | email path | `{{PASSWORD_DO_NOT_STORE}}`. Never in git | Signup JS regex copy. FAQ also lists allowed symbols; **do not copy a sample password** |
| 利用規約 / 個人情報の取り扱い について同意します | `required (docs)` on email path | Human reads. Live CU may tick after GO | `/worker/terms/` · `https://crowdworks.co.jp/privacy_policy/01/` |
| 同意して会員登録する | control | Email path only. Google path uses OAuth | Signup JS |
| すでに登録済みの方はログイン | control | If MAIN already has CrowdLinks → login. No second account | Signup JS · [login-how](https://help.crowdlinks.jp/login-how-w) 二重アカウント |
| Googleでログイン / Facebookでログイン | control | Login page. Facebook still not a new identity | Login JS `login-d30fd72bc87effc8.js` |
| `/client/` | `STOP` | Close | https://crowdlinks.jp/client/ |

Google / email / password values are **never** committed. Do not write a sample password. Do not record CSRF, OAuth tokens, or AWS signed URLs.

氏名 / 生年月日 / 電話 are **not** in public signup JS this GET → post-OAuth wizard = `needs_check`. Live form wins.

---

## B. Profile after account (help + 記入サンプル)

### B1. Identity (not bank)

| Help label | `required_guess` | DRAFT_ONLY paste | Cite |
|---|---|---|---|
| 氏名 | `high` (help: 本名必須ではないが推奨) | `{{LEGAL_NAME_KANJI}}`. Display `{{DISPLAY_NAME}}` only if the form splits | [User FAQ 本名](https://help.crowdlinks.jp/0029649d31534622a6d95ffe53df18dd) · [写真/氏名](https://help.crowdlinks.jp/15c33f48ad3041ce9a0975ba863b6c32) · `.../profiles/edit/base/` |
| 通称 / 屋号 only | skip unless form splits and 登録名 is already 本名 | Do not replace 氏名 with a brand to hide 副業 | FAQ 本名推奨 |
| 生年月日 | `needs_check` (TOS 満18歳; not on public signup JS) | `{{BIRTH_YEAR}}-{{BIRTH_MONTH}}-{{BIRTH_DAY}}` if asked. Do not invent | TOS 第3条2(1) |
| 学生ではない | `required (docs)` as eligibility, not a paste box | If a checkbox appears, only tick if true | TOS 第3条2(2) · [応募ガイドライン](https://help.crowdlinks.jp/entry_guidelines) |
| 実務経験2年以上（記載する業務） | `required (docs)` as eligibility | **Not a number to invent.** Empty `{{YEARS_AUTOMATION_PUBLIC}}` → `years_empty_park` | TOS 第3条2(3) |
| 所属組織の規則に反していない | `required (docs)` as eligibility | Human owns 副業可否. CU does not attest | TOS 第3条2(9) |
| メール | account field | MAIN only. 連絡用 = ログイン用 = same mailbox | FAQ アカウント |
| 電話番号（アカウント設定・連絡先） | `needs_check` / often `STOP` this pass | `{{PHONE}}` only if **draft save** blocks. User-chat wait. If ID/selfie → KYC STOP | [change-mail-tel](https://help.crowdlinks.jp/change-mail-tel) · `.../user/account_setting/` |
| プロフィール画像 | `optional (docs)` | `{{PHOTO_LOCAL_PATH}}` local face photo. Not an ID | [写真](https://help.crowdlinks.jp/15c33f48ad3041ce9a0975ba863b6c32) |
| 公開範囲 | `high` if control visible | **クラウドリンクス内で公開**. Not 一般公開. 限定公開 = 有料プラン契約企業のみ（FAQ）— still not 一般公開 | User FAQ プロフィール |
| 特定の企業をブロック | `optional (docs)` | `{{BLOCK_COMPANY_NAMES}}` from ledger. **Names off git**. Help: 正式名称（株式会社も含めて） | [corporate_block](https://help.crowdlinks.jp/corporate_block) |

### B2. プロフィール本文 (this pass)

Official sample headings ([resume-sample](https://help.crowdlinks.jp/guide/resume-sample)): **キャリアの概要・略歴**, **課題解決できること**, plus FAQ **経歴・実績** (1+ required) and help **スキルタグ**.

| Help / sample label | `required_guess` | DRAFT_ONLY paste | Cite |
|---|---|---|---|
| キャリアの概要・略歴 | `high` | Fence **n8n 200** below. URL `.../profiles/edit/self_introduction/` | 記入サンプル 「キャリアの概要の更新はこちらから」 |
| 課題解決できること | `high` | Fence **capability** (short) or **n8n 800** if the box is long. URL `.../profiles/edit/capability/` | 記入サンプル |
| 経歴・実績 | `required (docs)` 1+ | Public facts only. Empty years if ledger empty. FAQ: 1件しか無いと削除ボタン非表示 | User FAQ |
| スキルタグ | `high` | Existing chips only. Then **経験年数** 1年未満 / 1年以上 / 2年以上 / 3〜5年 / 5年以上. Ledger or **skip chip** | [スキルタグ](https://help.crowdlinks.jp/642ef850db334df8a4ee93a2f330a09a) · `.../profiles/edit/skill_tag/` |
| ポートフォリオ / URL | `high` | Public URLs only | Live form. Not in signup JS |
| 希望単価 / 報酬 | `needs_check` | `{{HOURLY_YEN_DRAFT}}` or empty. Else `rate_empty` | Live form. Do not invent 円 |
| 希望職種 / ワークスタイル / 稼働時間 | `needs_check` | If shown: existing chips only. リモート / 週次は要相談. Third-party blogs name these; **official sample this GET does not** | Live form |
| 自己紹介 (if a third box appears) | `needs_check` | Same n8n 200 / 800. Live label wins | Live form |

Help/sample note: 記入サンプル uses 〇件 / 〇％ as **blanks**. Do not fill those with invented volume.

### B3. Apply / money — not paste targets

| Help label | `required_guess` | DRAFT_ONLY paste | Cite |
|---|---|---|---|
| 応募フォームへ | **STOP** | Current user FAQ + sampled project HTML this GET | [FAQ 応募](https://help.crowdlinks.jp/0029649d31534622a6d95ffe53df18dd) |
| 話を聞きたい | **STOP** | Older faq-worker wording. Same stop | [faq-worker](https://help.crowdlinks.jp/faq-worker) |
| スカウトに返信 | **STOP** | FAQ encourages reply; this pack does not | User FAQ スカウト |
| マッチング報告 / 報告する | **STOP** | Direct contract path | User FAQ 外部やり取り |
| 有料会員 | **STOP** | TOS 第4条 審査・追加書類・利用料. **金額未記載 → 作らない** | [terms](https://crowdlinks.jp/terms) |
| 追加の書類等の提出 | **STOP** | TOS 第3条4 (無料会員の審査でも求め得ると書く) | Same |
| 口座 / マイナンバー / 身分証 | **STOP** | Direct contract after match is still STOP | FAQ 契約は企業と直接 |
| 案件応募そのもの | **STOP** | Guideline repeats TOS eligibility | [entry_guidelines](https://help.crowdlinks.jp/entry_guidelines) |

---

## Placeholders (empty in git)

Same family as Week2 / Workship packs. Values live only in the operator ledger.

- `{{GOOGLE_ACCOUNT_EMAIL}}` / `{{EMAIL}}` MAIN Google mailbox
- `{{PASSWORD_DO_NOT_STORE}}` email path only
- `{{LEGAL_NAME_KANJI}}` 戸籍上の氏名（漢字）
- `{{LEGAL_NAME_KANA}}` 氏名カナ if asked
- `{{DISPLAY_NAME}}` 表示名。推奨: `石田祐太` (only if the form is not the contract 氏名)
- `{{PHONE}}` 日本の携帯電話 — only if draft save blocks
- `{{PREFECTURE}}` / `{{CITY}}` 住所を求められたとき。番地は git に書かない
- `{{BIRTH_YEAR}}` / `{{BIRTH_MONTH}}` / `{{BIRTH_DAY}}`
- `{{PORTFOLIO_URL}}` 推奨公開: `https://yutalab.dev/`
- `{{GITHUB_URL}}` 推奨公開: `https://github.com/rimone0511`
- `{{GITHUB_REPO_AUTOPILOT}}` `https://github.com/rimone0511/autopilot-log`
- `{{PHOTO_LOCAL_PATH}}` 顔写真のローカルパス（コミット禁止）
- `{{HOURLY_YEN_DRAFT}}` 空なら空 / `rate_empty`
- `{{YEARS_AUTOMATION_PUBLIC}}` 空なら年数を作らない（TOS 2年を満たすために盛らない）
- `{{BLOCK_COMPANY_NAMES}}` 実名を git に書かない

---

## Paste fences — 石田祐太 / n8n / AI automation / JP

Recount after placeholder fill. Counts below are committed Japanese character counts (no secrets).

**Default = URL 無し.** 公開URLはポートフォリオ欄. 画面がURLを受け、カウンターが足りるときだけ「URL あり」の PR#30 同文を使う.

Do not claim TikTok posting from Autopilot Log is unattended. Do not write unverified 件数 / 年数. Do not 応募 in the bio.

### キャリアの概要 — n8n 200（200字・URL無し・この机の既定）

```
石田祐太。n8nとAIで、人が検品できる業務自動化を作ります。公式コネクタと公開APIのみ。ブラウザ自動操作・スクレイピング・いいね自動化はしません。手順とつまずきは個人サイトで公開。リモート可。未確認の件数や年数は書きません。秘密は貼りません。公開は人が決めます。応募はこの下書きではしません。根拠を残す方針です。公開スイッチは人手側に置きます。下書き保存まで。連絡先は本文に書きません。保存のみ。
```

### 課題解決できること — short

```
n8nの公式コネクタと公開APIで、繰り返し作業を人が検品できる形にします。フォーム→表→通知、分類、承認待ち。ブラウザ自動操作・スクレイピング・いいね自動化はしません。未確認の件数は書きません。応募はこの下書きではしません。
```

### 課題解決できること / 長い自己紹介 — n8n 800（800字・URL無し）

```
石田祐太（Yuta Ishida）です。n8nとAIを使い、人が検品できる業務自動化を設計・実装します。売り物は「動いたように見える自動化」ではなく、目的・範囲・合格条件・停止条件を先に切り、動いたあとに回帰確認まで残す仕組みです。使う道具はn8nの公式コネクタと、公開されているAPIです。ブラウザ自動操作・スクレイピング・いいねやフォローの自動化はしません。提供できること：（1）フォーム到着→表への記録→通知、分類、承認待ちといった繰り返し作業の自動化設計。（2）Claude CodeやCodexなど、AIに実装を任せるときの指示の書き方、検品、失敗時の切り分け。（3）鍵の扱い、公開事故、トークン期限など、自動化が止まりやすい箇所の点検。（4）公式APIだけを使う投稿導線の仕組みづくり。公開している実録の場は個人サイト「ユタラボ」です。受けないこと：権利のない投稿代行、本人確認書類・口座・マイナンバーの代理入力、未確認のままの公開。進め方はテキスト中心です。根拠と反証を残し、公開スイッチは依頼者または本人の手に置きます。リモート可。週次の稼働時間は案件ごとに相談します。未確認の件数や年数は書きません。確認できた公開物だけを貼ります。秘密はチャットに出さず、本人の安全な入力経路だけを使います。日本語でのやり取りを標準にします。英語の一次資料は必要なら要約して渡します。契約前に範囲外を一文で確定します。納期は着手前に合意します。応募とスカウト返信はこの下書きではしません。公開URLはポートフォリオ欄にだけ置きます。自己紹介欄には貼りません。スキルの経験年数は台帳に無いなら空のままにし、2年とは書きません。現職の社名は一般公開しません。有料会員化と応募はこのパックではしません。作業の記録を残します。確認できた公開物だけを根拠にします。公開は人手。下書き保存までです。人手側です。
```

### URL あり（ポートフォリオ欄 / URLを受け付ける欄だけ。PR#30 同文・200/800）

自己紹介で弾かれたら使わない。測済み **200** / **800**.

```
石田祐太。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIによる業務自動化の手順・つまずき・確認できた結果を、むずかしい言葉を避けて公開しています。公式APIだけを使う動画アップロード道具も公開中です。ブラウザ自動操作はしません。人が検品できる形で、繰り返し作業を自動化します。リモート可。未確認の数字は書きません。公開は人が決めます。秘密は貼りません。根拠を残す方針です。
```

```
石田祐太（Yuta Ishida）です。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIを使って毎日の作業を自動化する手順、つまずいた点、確認できた結果を、むずかしい言葉を避けて公開しています。売り物は「動いたように見える自動化」ではなく、人が検品できる仕組みです。公開している実録と道具を、業務委託の成果物の根拠にします。提供できること：（1）繰り返し作業の自動化設計。目的・範囲・合格条件・停止条件を先に切り、実装後に回帰確認まで残します。（2）Claude CodeやCodexなど、AIに実装を任せるときの指示の書き方、検品、失敗時の切り分け。（3）YouTubeとTikTokへの公式API投稿の仕組みづくり。ブラウザ自動操作とスクレイピングは対象外です。（4）鍵の扱い、公開事故、トークン期限など、自動化が止まりやすい箇所の点検。公開している道具の例：Autopilot Log（https://github.com/rimone0511/autopilot-log）。YouTube Data API v3 と TikTok Content Posting API のみを使い、投稿の門番は壊れても非公開側に倒れます。受けないこと：いいねやフォローの自動化、権利のない投稿代行、本人確認書類・口座・マイナンバーの代理入力、未確認のままの公開。進め方はテキスト中心です。根拠と反証を残し、公開スイッチは依頼者または本人の手に置きます。リモート可。週次の稼働時間は案件ごとに相談します。未確認の件数や年数は書きません。確認できた公開物だけを貼ります。秘密はチャットに出さず、本人の安全な入力経路だけを使います。日本語でのやり取りを標準にします。英語の一次資料は必要なら要約して渡します。契約前に範囲外を一文で確定します。納期は着手前に合意します。作業の記録を残す。
```

### スキルタグ (pick live matches only)

`n8n` · `業務自動化` · `Python` · `API` · `Claude Code` · `Codex` · `技術執筆`

If a chip is missing from the DB: **skip**. Do not file a new tag this pass.

経験年数: ledger value mapped onto **1年未満 / 1年以上 / 2年以上 / 3〜5年 / 5年以上**, or skip. Empty ledger → skip (do not pick 2年以上).

### ポートフォリオ rows

| Title (public) | URL |
|---|---|
| ユタラボ | `{{PORTFOLIO_URL}}` → https://yutalab.dev/ |
| Autopilot Log | `{{GITHUB_REPO_AUTOPILOT}}` → https://github.com/rimone0511/autopilot-log |

---

## Sources (public)

- Signup UI JS: https://crowdlinks.jp/worker/signup/ (`Googleで登録する` / `メールアドレスで登録する`)
- Login UI JS: https://crowdlinks.jp/worker/login/ (`Googleでログイン`; Facebook = not a new identity)
- User FAQ: https://help.crowdlinks.jp/0029649d31534622a6d95ffe53df18dd
- 記入サンプル: https://help.crowdlinks.jp/guide/resume-sample
- スキルタグ: https://help.crowdlinks.jp/642ef850db334df8a4ee93a2f330a09a
- TOS: https://crowdlinks.jp/terms
- STOP URLs: listed in [STOP.md](STOP.md)
