> DRAFT_ONLY field map. NO login in the authoring session. NO secrets. NO invented credentials.  
> Paste values for CU. Stops: [STOP.md](STOP.md). Step order: [PLAYBOOK.md](PLAYBOOK.md).  
> Labels come from **Intercom Help** (this GET 200) + sibling public HTML on `register/choose` (this origin GET was **WAF 202**). Live wizard wins.

# FIELD-MAP — MENTA mentor / B11

Desk: MENTA（メンター） B11 / QUEUE B6 / CU-16  
Livecheck: 2026-09-16. Intercom Help readable. `menta.work` this GET = AWS WAF **challenge** (no logged-in required-field dump).

`required_guess` is **not** a logged-in required-field dump. Values:

| Token | Meaning |
|---|---|
| `required (docs)` | Help names it as part of メンタープラン編集 / 新規メンター |
| `high` | Help lists it on the mentor listing; draft save may still work without it |
| `optional (docs)` | Help documents skip / 画像なしでも登録可 / later |
| `needs_check` | Help is silent or the live widget was not opened (WAF / not logged in) |
| `STOP` | Do not fill. Not a paste target |

Placeholders stay empty of secrets in git. Fill only from the operator’s local ledger at paste time.

**Shape:** this is a **mentor listing** (タイトル + できること + プラン行). It is **not** a CrowdWorks 提案 and **not** a Coconala gig with a price. 金額 stays empty. **提出** is not a save control — see [PLAYBOOK.md](PLAYBOOK.md) §0.

---

## A. Sign up (public choose + help)

Sibling GET 2026-09-16 (PR#33 / #61): https://menta.work/index.php/register/choose — 「メールアドレスで登録する」「**Googleアカウントで登録する**」（class note in thick pack: `m-button__text google`）plus X / Facebook / Apple / Lancers. OAuth: `/index.php/oauth/google`.

This authoring GET: the same URLs returned **HTTP 202** `x-amzn-waf-action: challenge`. **Re-read labels at click-time.**

| UI label (help / sibling HTML) | `required_guess` | DRAFT_ONLY paste | Cite / gap |
|---|---|---|---|
| Googleアカウントで登録する | preferred path | MAIN `{{GOOGLE_ACCOUNT_EMAIL}}` only. Same Google every later login | Sibling `/register/choose` 200. This GET WAF. Click-time **`needs_check` until the challenge clears** |
| メールアドレスで登録する | fallback | Same MAIN `{{EMAIL}}`. No new mailbox | Sibling choose page |
| パスワード | email path | `{{PASSWORD_DO_NOT_STORE}}`. Never in git | Sibling choose page |
| X / Facebook / Apple | `STOP` (new identity) | Do not use | Sibling choose page |
| Lancers アカウントで登録する | `STOP` | Separate identity. Close | Sibling choose page |
| 招待コード | `optional (docs)` / `needs_check` | `{{INVITE_CODE}}` empty unless ledger has one | Live form |
| 利用規約 / プライバシー 同意 | `required (docs)` if shown | Human reads. Live CU may tick after GO | Live form |
| Google OAuth start | control | Human MAIN only. Authoring agent does not follow into Google | `/index.php/oauth/google` |
| WAF challenge / press-and-hold | gate | Wait. `holdDurationMs` 1800 / retry 2500. Then park | This GET 202. **Do not copy challenge keys / cookies into git** |

Google / email / password values are **never** committed. Do not write a sample password. Do not record CSRF or WAF tokens.

Already a member: login with the same MAIN Google. No second account.

---

## B. After account — メンタープラン編集

Help path: ログイン後、メニューから「メンター」→「メンタープラン編集」 ([メンターとして登録したい](https://intercom.help/mentajp/ja/articles/3025349), 2021-05-22).

Help order on that page: **1 タイトル → 2 メインイメージ → 3 カテゴリとタグ → 4 できること → 5 プラン（名 / 金額 / 内容）→ 6 ステータス・契約承認 → 7 提出**. This pack uses 1–6 as paste targets and treats **7 as STOP**.

### B1. Identity (not bank)

| Help / likely label | `required_guess` | DRAFT_ONLY paste | Cite |
|---|---|---|---|
| ユーザーネーム | `high` (提出審査でも見られる) | `{{DISPLAY_NAME}}` 推奨 **石田祐太**. Live charset (英数制限) wins | [提出について](https://intercom.help/mentajp/ja/articles/5252569) プロフィールやユーザーネームも確認対象 |
| アイコン | `optional (docs)` | `{{PHOTO_LOCAL_PATH}}` 顔写真. 身分証禁止 | Same. Help メインイメージは「設定しなくても登録できます」 |
| メール | account field | MAIN only. Confirm = parent Gmail | Live account |
| 生年月日 / 住所 / 電話 | `needs_check` | Ledger placeholders only if **draft save** blocks. Street not in git. If ID/selfie → KYC STOP | Live form |
| Lancers 連携 | `STOP` | Do not bind a second identity | Choose-page sibling |

### B2. Listing + profile paste (石田祐太 / AI自動化)

| Help label | `required_guess` | DRAFT_ONLY paste | Cite |
|---|---|---|---|
| タイトル | `required (docs)` step 1 | Course **タイトル** fence below | [登録したい](https://intercom.help/mentajp/ja/articles/3025349) 「どんなプランを提供するのかが一目でわかる」 |
| メインイメージ / サブ画像 | `optional (docs)` | Skip, or non-ID photo. Not required to register | Same, step 2 |
| カテゴリ | `high` | Nearest **existing** chip (プログラミング / 業務効率化 / AI 系 if listed). Live list wins | Same, step 3 |
| タグ | `optional (docs)` | Up to **5**. Existing / short: `AI` `自動化` `Claude Code` `API` `検品` — skip if the chip DB rejects | Same 「5つまで」 |
| できること | `required (docs)` step 4 | Fence **200** or **800** below. Help: プロフィール・経歴・実績。markdown 可 | Same. 具体プランは step 5 |
| 経歴・実績 | `high` (inside できること) | Public articles + public repo only. **No invented 指導件数** | [スクールガイド](https://intercom.help/mentajp/ja/articles/6591930) は「指導経験●件」例を出すが **数字は作らない** |

### B3. Course / plan row (draft — 金額 empty)

Help step 5: 「プラン名、金額、内容を入力します」「月契約」（既定・自動更新）と「単発」チェック ([登録したい](https://intercom.help/mentajp/ja/articles/3025349)).

| Help label | `required_guess` | DRAFT_ONLY paste | Cite |
|---|---|---|---|
| プラン名 | `high` if a row is opened | Course **プラン名** fence. One row only this pass | Same |
| 内容 | `high` if a row is opened | Course **プラン内容** fence. No 円. No 受講者数 | Same. スクールガイド is tips, not a GO |
| 金額 | **STOP** this pass | Leave empty. `{{PLAN_PRICE_YEN}}` stays blank. If the widget refuses empty → **skip the row** (`rate_empty` / `plan_skipped`). Do **not** type 10000 / 1.4万 / sibling SKU | Help examples use 10,000円 only as a **fee illustration**. Not a paste price |
| 月契約 / 単発 | `needs_check` | Do not enable a **priced** 月契約 (auto-renew). Prefer untouched + empty 金額 | Same 「デフォルトでは月契約」「単発にしたい場合は左下チェック」 |
| プランを増やす | skip | One draft row max. Prefer zero rows if 金額 blocks | Same |
| 中止 | n/a this pass | Only relevant if already 出品中 — then the desk already went too far | [出品中の中止](https://intercom.help/mentajp/ja/articles/3025564) |

If the live page has a **保存 / 更新** that is **not** 提出: allowed. If the only control is **提出**: do not press (`no_draft_path`).

### B4. Status / submit / money — not paste targets (except 表示しない)

| Help label | `required_guess` | DRAFT_ONLY paste | Cite |
|---|---|---|---|
| ステータス **表示しない** | `high` if filling a listing | Prefer this. 一覧に出ず契約不可 | [ステータス](https://intercom.help/mentajp/ja/articles/3751409) |
| ステータス **今、忙しいです** | skip | Still **表示はされる**. Not this pass | Same |
| ステータス **相談できます** | **STOP** | 契約が可能な状態 | Same |
| 契約承認 承認有り | `optional (docs)` | Not a substitute for skipping 提出 | [登録したい](https://intercom.help/mentajp/ja/articles/3025349) step 6 |
| **提出** / 提出する | **STOP** | 運営確認のあと **一般に公開**. 新規メンターは提出必須・**提出自体は無料** — still do not | [提出について](https://intercom.help/mentajp/ja/articles/5252569) |
| 本人確認ページ (Stripe) | **STOP** | 設定メニュー. 支払いに必要 | [本人確認](https://intercom.help/mentajp/ja/articles/3025561) |
| 口座 / 出金 | **STOP** | 売上 1,000円超かつ入金から30日 + 本人確認・口座 | [出金](https://intercom.help/mentajp/ja/articles/3025575) |
| プラン値上げウィザード | **STOP** | Needs an already-live plan | [値上げ](https://intercom.help/mentajp/ja/articles/3135613) |
| 運営と一緒に企画 | skip | スクールガイド CTA. Do not inquire this pass | [スクールガイド](https://intercom.help/mentajp/ja/articles/6591930) |

---

## Placeholders (empty in git)

Same family as Week2 packs. Values live only in the operator ledger.

- `{{GOOGLE_ACCOUNT_EMAIL}}` / `{{EMAIL}}` MAIN Google mailbox
- `{{PASSWORD_DO_NOT_STORE}}` email path only
- `{{INVITE_CODE}}` empty OK
- `{{LEGAL_NAME_KANJI}}` 戸籍上の氏名（漢字）— only if a legal-name field appears
- `{{LEGAL_NAME_KANA}}` 氏名カナ if asked
- `{{DISPLAY_NAME}}` 表示名。推奨: `石田祐太`
- `{{PHONE}}` 日本の携帯電話 — only if draft save blocks
- `{{PREFECTURE}}` / `{{CITY}}` 住所を求められたとき。番地は git に書かない
- `{{BIRTH_YEAR}}` / `{{BIRTH_MONTH}}` / `{{BIRTH_DAY}}`
- `{{PORTFOLIO_URL}}` 推奨公開: `https://yutalab.dev/`
- `{{GITHUB_URL}}` 推奨公開: `https://github.com/rimone0511`
- `{{GITHUB_REPO_AUTOPILOT}}` `https://github.com/rimone0511/autopilot-log`
- `{{PHOTO_LOCAL_PATH}}` 顔写真のローカルパス（コミット禁止）
- `{{PLAN_PRICE_YEN}}` **always empty this pass**
- `{{YEARS_AUTOMATION_PUBLIC}}` 空なら年数を作らない

---

## Paste fences

Recount after placeholder fill. Counts below are committed Japanese character counts (no secrets). Profile 200 / 800 match sibling [#33](https://github.com/rimone0511/autopilot-log/pull/33) mentor bios.

Do not put 手数料％, 円額, or unverified 受講者数 in any fence.

### できること / 自己紹介 200（200字）

```
石田祐太。個人サイト「ユタラボ」（https://yutalab.dev/）で、AI自動化の手順を初心者向け日本語で公開しています。公式APIの動画投稿も扱います。ブラウザ自動操作は教えません。最初の1回を、人が確認できる形で安全に動かすところまで伴走します。公開スイッチは受講者本人が持ちます。未確認の数字は書きません。リモート可。宿題は小さく先に切ります。秘密は貼りません。必ず根拠だけ教えます。
```

### できること / 自己紹介 800（800字）

```
石田祐太（Yuta Ishida）です。個人サイト「ユタラボ」（https://yutalab.dev/）で、AI自動化の手順を初心者向けの日本語で公開しています。教える範囲は、道具の入れ方から「最初の1回を安全に動かす」までです。専門用語は後回しにし、つまずきやすい場所を先に書きます。教えられること：（1）Claude Code / Codex のはじめ方と、対象ファイル・完成条件・禁止事項を入れた指示の書き方。（2）毎日の作業を自動化してよいかの見分け。秘密・公開・課金が絡む仕事は外す判断。（3）公式APIだけを使う動画投稿の考え方。ブラウザ自動操作やスクレイピングは教えません。（4）動いたあとの検品。仕様、境界値、秘密情報、権限、再現性の順に見ます。公開している教材の土台：ユタラボの実録記事と、Autopilot Log（https://github.com/rimone0511/autopilot-log）。投稿の門番は壊れても非公開側に倒れる設計です。受けないこと：代行ログイン、本人確認の代理、権利のない投稿、未確認の公開、いいね自動化。進め方はチャットまたは非同期テキストです。宿題は小さく切り、合格条件を先に合意します。公開スイッチは受講者本人が持ちます。未確認の受講者数や収益は書きません。公開記事と公開リポジトリを教材の根拠にします。秘密はチャットへ貼らず、本人の画面で入力してもらいます。レッスンはオンライン想定です。録画の外部公開はしません。課題の提出物に秘密を含めないよう、提出前チェックを宿題にします。料金と回数はプラン欄で別途示し、プロフィール本文では約束しません。初回は環境確認から始め、いきなり本番公開へ進みません。止める条件も先に書きます。画面共有なしでも進められます。質問はテキストで残します。未確認の効果は言いません。料金はプラン欄だけに書きます。
```

This pack leaves プラン欄 **empty of yen**, so the last sentences are a promise **not** to put a price in the bio — they are not a GO to fill 金額.

### タイトル（listing・25字）

```
AI自動化のはじめ方｜公式APIと検品（石田祐太）
```

### プラン名（one row, unpublished・16字）

```
AI自動化 伴走（チャット中心）
```

### プラン内容（draft — no 円・558字）

```
このプランは「最初の1回を、人が確認できる形で安全に動かす」ところまでを、チャット中心で伴走します。ゴール（公開できる範囲）: Claude Code / Codex で対象ファイル・完成条件・禁止事項を書いた指示が自分で書ける。毎日の作業を自動化してよいかを自分で見分けられる（秘密・公開・課金が絡む仕事は外す）。公式APIだけを使う動画投稿の考え方を理解する（ブラウザ自動操作は対象外）。動いたあとに仕様・境界値・秘密・権限・再現性の順で検品できる。進め方: テキスト中心（非同期可）。宿題は小さく切り、合格条件を先に合意します。初回は環境確認から。いきなり本番公開へ進みません。公開スイッチは受講者本人が持ちます。秘密はチャットへ貼らず、本人の画面で入力します。教材の根拠（公開物のみ）: ユタラボ https://yutalab.dev/ と Autopilot Log https://github.com/rimone0511/autopilot-log 。受けないこと: 代行ログイン、本人確認の代理、権利のない投稿、未確認の公開、ブラウザ自動操作・スクレイピング・いいね自動化。未確認の受講者数・収益・稼げる額は約束しません。料金・回数はこの下書きでは空欄のままにします。提出（公開審査）はしません。
```

### タグ (pick live matches only; max 5)

`AI` · `自動化` · `Claude Code` · `API` · `検品`

If a chip is missing from the DB: **skip**. Do not invent a tag taxonomy.

### ポートフォリオ URLs (inside できること or a URL field)

| Title (public) | URL |
|---|---|
| ユタラボ | `{{PORTFOLIO_URL}}` → https://yutalab.dev/ |
| Autopilot Log | `{{GITHUB_REPO_AUTOPILOT}}` → https://github.com/rimone0511/autopilot-log |

Do not claim TikTok posting from this repo is unattended.

---

## Sources (public)

- Signup UI (sibling, not this WAF GET): https://menta.work/index.php/register/choose
- Mentor edit steps: https://intercom.help/mentajp/ja/articles/3025349
- 提出 = 公開審査: https://intercom.help/mentajp/ja/articles/5252569
- ステータス: https://intercom.help/mentajp/ja/articles/3751409
- 手数料: https://intercom.help/mentajp/ja/articles/3025582
- Stripe 本人確認: https://intercom.help/mentajp/ja/articles/3025561
- 出金: https://intercom.help/mentajp/ja/articles/3025575
- MENTAとは: https://intercom.help/mentajp/ja/articles/3025296
- STOP URLs: listed in [STOP.md](STOP.md)
