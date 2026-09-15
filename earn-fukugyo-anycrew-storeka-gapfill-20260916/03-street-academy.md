> DRAFT_ONLY paste stub. NO secrets. NO browser signup from this PR. NO publish.
> Gap-fill for CU-17 where prior packs left www WAF and help-fee 403 as needs_check.
> Agent that wrote this pack did not create an account. Lessons are not published.
> `thin_site_skip: false`. Stop at KYC / eKYC.

# CU-17 GAP-FILL — ストアカ（Street Academy）講師

| キー | 値 |
|---|---|
| cu_serial | CU-17 |
| activity_gate | 一覧 **pass**（`/online/all` に開催日 **2026-09-16** 以降）。個別 `myclass` は AWS WAF **405** → 詳細 **needs_check** |
| self_serve | **yes**（`/register` にメール登録。Google OAuth は見当たらない） |
| cu_ready | **true**（メール経路。講座は作らない） |
| official | https://www.street-academy.com/ |
| register | https://www.street-academy.com/register |
| teach | https://www.street-academy.com/teach |
| fee | https://www.street-academy.com/fee |
| listing | https://www.street-academy.com/online/all |
| help_fee | https://support.street-academy.com/hc/ja/articles/200700579 （this env **403** → **needs_check**） |
| google_signup_preference | **NOT_OFFERED_OAUTH** → Google メールで「メールアドレスで登録」 |
| fee_public | **cited** from `/fee`（下記）。ヘルプ本文は未取得 |
| thin_site_skip | **false** |
| stop_at_kyc | **STOP**（本人確認書類 + 顔撮影画面） |
| draft | true |
| observed | 2026-09-16 公開 GET |

## Gap vs prior packs

| 穴（PR#3 / PR#12 / PR#21 / PR#33） | この GET |
|---|---|
| www / register / teach が AWS WAF **405** | **200**。トップ・登録・講師 LP が読めた。WAF は死滅ではないし、毎回再現するとは限らない |
| 講座開催日未読 | `/online/all` に講座カードと開催日フィルタ（例: `2026-09-16`, `2026-09-17`）。カテゴリ件数は活動証明に使わない |
| 個別講座 | 検索結果の `/myclass/99028?...` を GET すると **405 Human Verification**。**unread WAF = needs_check** |
| 手数料ヘルプ 403 | **再現**（Cloudflare）。料率は公式 **`/fee`** で取得した。ヘルプ本文は needs_check のまま。数字をヘルプから発明しない |
| Google OAuth | `/register` ライブ: LINE / Facebook / **メールアドレスで登録**。Google ボタン無し。再確認 |

個別講座が WAF のときは park。www がまた 405 なら人も解けなければ park。死滅と書かない。

## CU handoff（この机）

やってよい（下書きのみ・後続 CU）:

1. ブラウザで www。WAF が出たら人が解いてから再開。解けなければ park
2. `/register` → **メールアドレスで登録**。メールは `{{EMAIL}}`。パスワードはローカル台帳。このファイルに書かない
3. LINE / Facebook は、Google メール経路が死んでいるときだけ。新規 LINE/Facebook をこの仕事のためだけに作らない
4. 生徒登録のあと、先生プロフィール（名前・顔写真・公開 URL・自己紹介）まで。**講座は作らない。公開申請しない**
5. 本人確認画面は開いたら閉じる

アプリは先生機能なし、と既存ヘルプ。PC ブラウザ。

## Fees — official `/fee` only（創作しない）

出典: [ストアカの利用料について｜先生・主催団体向け](https://www.street-academy.com/fee)  
この環境で HTTP **200**。貼る直前に公式を再読。ヘルプ 403 を根拠にしない。

公開面の文言（要約ではなく、ページに出た区分）:

| 経路（公式 `/fee` の項目名） | 公式ページの率 | Status |
|---|---|---|
| 登録費・掲載費・月額費 | 0 円（「利用料はずっと0円」） | **cited** |
| 自己集客手数料（生徒が初めて。SNS やブログなど自分の集客） | 10% | **cited** |
| ストアカ送客手数料（検索・特集などストアカ内。初めて） | 30%（対面講座は 20%） | **cited** |
| リピート手数料（2 回目以降。経路を問わず） | 10% | **cited** |

同ページの注記（数字の創作ではない）:

- 各手数料には別途消費税
- 未開催・キャンセル時は手数料は発生しない
- 自己集客・ストアカ送客の判定基準はページ内リンク先。**この GET ではリンク先本文を追っていない → 判定ロジックは needs_check**

ヘルプ https://support.street-academy.com/hc/ja/articles/200700579 は this env **403**。同じ 10/30/20 をヘルプ側で再確認できていない。**ヘルプ本文は needs_check**。CU は `/fee` を正とし、矛盾したら空欄。

運用: 自己集客 URL をストアカ内で回して 10% を狙う、と書く必要はない。講座公開はしない。プロフィールに料率を書かない。

## Field map（プレースホルダ）

| 画面の項目（公開ヘルプ / `/register` ベース） | 貼る値 | 必須見込み | メモ |
|---|---|---|---|
| 登録経路 | メールアドレスで登録 | 必須 | NOT_OFFERED_OAUTH。`/register` に submit 値あり |
| メール | `{{EMAIL}}` | 必須 | |
| パスワード | ローカルのみ | 必須 | git に書かない |
| 名前 | 生徒表示 `{{DISPLAY_NAME}}` / 先生は実名 `{{LEGAL_NAME_KANJI}}` | 必須 | |
| 性別 | `{{GENDER_FORM_VALUE}}` | 生徒登録で出る | 未設定可なら空 |
| 地域 | `{{PREFECTURE}}` | 生徒登録で出る | |
| 興味カテゴリ | ビジネス / IT・プログラミングの最寄り | 任意 | |
| 先生: 顔写真 | `{{PHOTO_LOCAL_PATH}}` 本人が特定できる顔 | 必須に近い | 身分証の写真をアイコンにしない |
| 先生: SNS または HP | `{{PORTFOLIO_URL}}` | 必須に近い | 顔が確認できる公開ページ |
| 自己紹介 | 下記 200 / 800 | 高 | |
| 本人確認書類 / eKYC | やらない | STOP | `/teach`: 先生活動には書類提出 |
| 講座ページ | やらない | 出品 STOP | |

共通プレースホルダは [INDEX.md](INDEX.md)。

## JA bio 200（講師向け・200字）

```
石田祐太。個人サイト「ユタラボ」（https://yutalab.dev/）で、AI自動化の手順を初心者向け日本語で公開しています。公式APIの動画投稿も扱います。ブラウザ自動操作は教えません。最初の1回を、人が確認できる形で安全に動かすところまで伴走します。公開スイッチは受講者本人が持ちます。未確認の数字は書きません。リモート可。宿題は小さく先に切ります。秘密は貼りません。必ず根拠だけ教えます。
```

## JA bio 800（講師向け・800字）

```
石田祐太（Yuta Ishida）です。個人サイト「ユタラボ」（https://yutalab.dev/）で、AI自動化の手順を初心者向けの日本語で公開しています。教える範囲は、道具の入れ方から「最初の1回を安全に動かす」までです。専門用語は後回しにし、つまずきやすい場所を先に書きます。教えられること：（1）Claude Code / Codex のはじめ方と、対象ファイル・完成条件・禁止事項を入れた指示の書き方。（2）毎日の作業を自動化してよいかの見分け。秘密・公開・課金が絡む仕事は外す判断。（3）公式APIだけを使う動画投稿の考え方。ブラウザ自動操作やスクレイピングは教えません。（4）動いたあとの検品。仕様、境界値、秘密情報、権限、再現性の順に見ます。公開している教材の土台：ユタラボの実録記事と、Autopilot Log（https://github.com/rimone0511/autopilot-log）。投稿の門番は壊れても非公開側に倒れる設計です。受けないこと：代行ログイン、本人確認の代理、権利のない投稿、未確認の公開、いいね自動化。進め方はチャットまたは非同期テキストです。宿題は小さく切り、合格条件を先に合意します。公開スイッチは受講者本人が持ちます。未確認の受講者数や収益は書きません。公開記事と公開リポジトリを教材の根拠にします。秘密はチャットへ貼らず、本人の画面で入力してもらいます。レッスンはオンライン想定です。録画の外部公開はしません。課題の提出物に秘密を含めないよう、提出前チェックを宿題にします。料金と回数はプラン欄で別途示し、プロフィール本文では約束しません。初回は環境確認から始め、いきなり本番公開へ進みません。止める条件も先に書きます。画面共有なしでも進められます。質問はテキストで残します。未確認の効果は言いません。料金はプラン欄だけに書きます。
```

## STOP-AT-KYC

ここまでやってよい: メール登録、生徒アカウント、先生プロフィール（名前・顔写真・公開 URL・自己紹介）。

ここで止める:

- 本人確認（顔写真付き公的証明書 + 顔撮影）
- 口座
- 講座の公開申請（出品）

`/teach`: 「先生として活動いただくためには、本人確認書類の提出をお願いしています」。提出しない。

## thin_site_skip

false。www / register / teach / fee / online/all は 200。個別講座とヘルプの WAF は死滅証拠ではない。
