> DRAFT_ONLY paste pack. NO secrets. NO browser signup from this PR. NO publish.
> CU-ready field map for a later human/CU session. Agent that wrote this pack did not create an account.
> `thin_site_skip: false` unless public evidence shows the product is dead.
> Stop at KYC: do not upload ID, My Number, bank, Stripe identity, or e-sign identity contracts.

# CU-17 PACK — ストアカ（Street Academy）講師

| キー | 値 |
|---|---|
| sample_inventory | 05 |
| cu_serial | CU-17 |
| activity_gate | **needs_check**（www は WAF。講座開催日未読。ヘルプは Cloudflare 403） |
| self_serve | **yes**（公式ヘルプ: 会員登録のあと先生プロフィール。Google OAuth は見当たらない） |
| cu_ready | **true**（メール経路の手順あり。ライブフォームはこの環境で未取得） |
| official | https://www.street-academy.com/ |
| register | https://www.street-academy.com/register |
| teach | https://www.street-academy.com/teach |
| help_register | https://support.street-academy.com/hc/ja/articles/360011723660 |
| help_fee | https://support.street-academy.com/hc/ja/articles/200700579 |
| google_signup_preference | **NOT_OFFERED_OAUTH** → Googleメールで「メールアドレスで登録」 |
| fee_public | **needs_check（このGETではヘルプ本文未取得）**。公式ヘルプURLは上。数字は貼る直前に公式を再読。ここへ％を確定値として書かない |
| thin_site_skip | **false** |
| stop_at_kyc | **STOP**（顔写真付き公的証明書の提出画面） |
| draft | true |
| observed | 2026-09-16 公開 GET |

## needs_check

1. **活動** — www / register / teach はこの環境で AWS WAF **405**。講座カードの日付なし
2. **手数料％** — 公式ヘルプ https://support.street-academy.com/hc/ja/articles/200700579 はこの環境で **403**。自己集客10%／ストアカ送客30%（対面20%）／リピーター10% は **公開ヘルプの既存要約**であり、この観測では本文を再取得できていない。**CUは貼る直前に公式を開いて確認。確認できないなら空欄**
3. **Google OAuth** — 公式ヘルプ（PC/スマホ）の新規登録は **LINE / Facebook / メールアドレス**。Googleボタンは見当たらない。クリック時に Google が出ても、このパックはメール経路を正とする
4. teach.street-academy.com は講師メディア（2026.06.18 などの記事日付あり）。登録フォームではない

WAF は死滅証拠ではない。人がブラウザで登録面を開けないときだけ `thin_site_skip` を true に上げる。

## CU handoff（この机）

やってよい（下書きのみ・後続CU）:

1. ブラウザで www（アプリの先生機能なし、公式ヘルプ）。WAF が出たら人が解いてから再開。解けなければ park
2. 「メールアドレスで登録」。メールは `{{EMAIL}}`。パスワードはローカル台帳。このファイルに書かない
3. LINE / Facebook は、Googleメール経路が死んでいるときだけ
4. 生徒登録のあと、先生プロフィール（名前・顔写真・公開URL・自己紹介）まで。**講座は作らない。公開申請しない**
5. 本人確認画面は開いたら閉じる

## 自己集客手数料ノート（公式ヘルプ — 要再読）

出典: [ストアカの手数料・利用料はいくらですか？](https://support.street-academy.com/hc/ja/articles/200700579)  
**この環境では本文 GET が 403。** 下の表は既存公開ヘルプの要約であり、確定観測ではない。`needs_check`。貼る直前に公式を開く。開けなければ表を使わない。

| 経路（公式ヘルプの項目名） | 公開ヘルプに書かれている率（要再読） |
|---|---|
| 自己集客（自己集客URL経由） | 10% |
| ストアカ送客・オンライン | 30% |
| ストアカ送客・対面講座 | 20% |
| 2回目以降 | 経路を問わず 10%（公式Q&A） |

運用メモ（確認できたあとでも、講座公開は本人判断）:

- 自己集客10%は **自己集客URL** 経由に限る、とヘルプにある
- 自己集客URLをストアカ内やストアカユーザーへ送って送客手数料を避けることは、公式が禁止している、とヘルプにある
- 登録後に URL 発行だけ見るのは可。講座公開はしない

初期費用・月額は、この観測では公式HTMLから取れていない → 書かない。

## Field map（プレースホルダ）

| 画面の項目（公開情報ベース） | 貼る値 | 必須見込み | メモ |
|---|---|---|---|
| 登録経路 | メールアドレスで登録 | 必須 | Google OAuthなし |
| メール | `{{EMAIL}}` | 必須 | |
| パスワード | ローカルのみ | 必須 | git に書かない |
| 名前 | `{{DISPLAY_NAME}}` / 先生登録は実名 `{{LEGAL_NAME_KANJI}}` | 必須 | |
| 性別 | `{{GENDER_FORM_VALUE}}` | 生徒登録で出る | 未設定可なら空 |
| 地域 | `{{PREFECTURE}}` | 生徒登録で出る | |
| 興味カテゴリ | ビジネス / IT・プログラミング の最寄り | 任意 | |
| 先生登録: 顔写真 | `{{PHOTO_LOCAL_PATH}}` 本人が特定できる顔 | 必須に近い | コミット禁止 |
| 先生登録: SNSまたはHP | `{{PORTFOLIO_URL}}` | 必須に近い | 顔が確認できる公開ページ |
| 自己紹介 | 下記 200 / 800 | 高 | |
| 本人確認書類 | やらない | STOP | |
| 講座ページ | やらない | 出品STOP | |

公式ヘルプ: 講座作成の前にプロフィール、本人確認、先生ページ。このパックはプロフィール更新まで。

共通プレースホルダは [INDEX.md](INDEX.md)。

## JA bio 200（200字）

```
石田祐太。個人サイト「ユタラボ」（https://yutalab.dev/）で、AI自動化の手順を初心者向け日本語で公開しています。公式APIの動画投稿も扱います。ブラウザ自動操作は教えません。最初の1回を、人が確認できる形で安全に動かすところまで伴走します。公開スイッチは受講者本人が持ちます。未確認の数字は書きません。リモート可。宿題は小さく先に切ります。秘密は貼りません。必ず根拠だけ教えます。
```

## JA bio 800（800字）

```
石田祐太（Yuta Ishida）です。個人サイト「ユタラボ」（https://yutalab.dev/）で、AI自動化の手順を初心者向けの日本語で公開しています。教える範囲は、道具の入れ方から「最初の1回を安全に動かす」までです。専門用語は後回しにし、つまずきやすい場所を先に書きます。教えられること：（1）Claude Code / Codex のはじめ方と、対象ファイル・完成条件・禁止事項を入れた指示の書き方。（2）毎日の作業を自動化してよいかの見分け。秘密・公開・課金が絡む仕事は外す判断。（3）公式APIだけを使う動画投稿の考え方。ブラウザ自動操作やスクレイピングは教えません。（4）動いたあとの検品。仕様、境界値、秘密情報、権限、再現性の順に見ます。公開している教材の土台：ユタラボの実録記事と、Autopilot Log（https://github.com/rimone0511/autopilot-log）。投稿の門番は壊れても非公開側に倒れる設計です。受けないこと：代行ログイン、本人確認の代理、権利のない投稿、未確認の公開、いいね自動化。進め方はチャットまたは非同期テキストです。宿題は小さく切り、合格条件を先に合意します。公開スイッチは受講者本人が持ちます。未確認の受講者数や収益は書きません。公開記事と公開リポジトリを教材の根拠にします。秘密はチャットへ貼らず、本人の画面で入力してもらいます。レッスンはオンライン想定です。録画の外部公開はしません。課題の提出物に秘密を含めないよう、提出前チェックを宿題にします。料金と回数はプラン欄で別途示し、プロフィール本文では約束しません。初回は環境確認から始め、いきなり本番公開へ進みません。止める条件も先に書きます。画面共有なしでも進められます。質問はテキストで残します。未確認の効果は言いません。料金はプラン欄だけに書きます。
```

## STOP-AT-KYC

ここまでやってよい: メール登録、生徒アカウント、先生プロフィール（名前・顔写真・公開URL・自己紹介）。

ここで止める:

- 本人確認（顔写真付き公的証明書 + 顔撮影）
- 口座
- 講座の公開申請（出品）

登録パックは書類を提出しない。

## thin_site_skip

false。www の WAF とヘルプ 403 は死滅証拠ではない。公式ヘルプURLと講師メディアは公開されている。
