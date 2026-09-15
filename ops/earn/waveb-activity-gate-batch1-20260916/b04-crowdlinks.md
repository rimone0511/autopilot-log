# B04 — クラウドリンクス (CrowdLinks)

**DRAFT_ONLY.** Logged out. Did not register. Did not apply. No secrets.

```
date (JST): 2026-09-16
desk: CrowdLinks / クラウドリンクス
official_url: https://crowdlinks.jp/  (marketing https://start.crowdlinks.jp/)
public_pages_opened: yes
logged_in: no
signup_path: Official worker JS — 「Googleで登録する」 and 「メールアドレスで登録する」. Login JS — 「Googleでログイン」 / Facebook.
fee_notes: User FAQ — worker use is free; listed pay is not commission-cut. TOS defines 無料会員 vs 有料会員 with no yen table on pages opened.
cu_tip: Worker /signup/ only. Prefer Google (FAQ: cannot switch Google account). Do not buy 有料会員. Do not apply. 2-year experience: do not invent years.
gate: needs_check
published: no
```

## Official URL

- Marketing: https://crowdlinks.jp/ → 200 redirect to https://start.crowdlinks.jp/ (title「クラウドリンクス - ハイクラス副業マッチングサイト」)
- Worker signup: https://crowdlinks.jp/worker/signup/ — 200, title「新規登録【クラウドリンクス】」
- Login: https://crowdlinks.jp/login/ → `/worker/login/` — 200
- Listing (current app): https://crowdlinks.jp/worker/projects/ — 200, title「プロジェクト一覧【クラウドリンクス】」
- Listing (older shell): https://crowdlinks.jp/projects — 200
- Help: https://help.crowdlinks.jp/
- User FAQ: https://help.crowdlinks.jp/0029649d31534622a6d95ffe53df18dd
- Terms: https://crowdlinks.jp/terms
- Do **not** use `/client/` company tools

## Public jobs / dates — what this GET actually saw

`/worker/projects/` logged-out HTML shows filters (募集中のみ表示, 職種, 稼働時間, リモート可否) and sort labels **おすすめ順 / 新着順**. **No project cards and no dates** in the HTML. Next data is empty `pageProps`.

`/projects` (non-worker) visible text includes:「ご登録いただくと、プロジェクトのすべての情報をご覧いただけます。」「登録してプロジェクトの詳細を確認する」. Still **no cards**.

Sitemap https://crowdlinks.jp/sitemap.xml : **299** `/projects/{id}` locs, `changefreq` weekly, **no `<lastmod>`**. URL count is not traffic.

Individual public project pages return **titles** without login. This GET sampled 35 sitemap URLs. Every sample contained embedded fields in page HTML:

- `publishedDateTime` from **2026-03-31T02:23:26.63Z** through **2026-05-21T14:13:10.514Z**
- matching `publishedEndDate` from **2026-05-22** through **2026-07-17**

Examples (title + those two fields only):

| Title (trimmed) | publishedDateTime | publishedEndDate |
|---|---|---|
| （ID1056）SharePoint社内ポータルのUI/UX設計・実装パートナー | 2026-05-21T01:46:09.004Z | 2026-06-19 |
| 【RAG／LLM／PM／フルリモート】生成AI・LLM活用PaaSプロジェクトマネージャー | 2026-04-10T01:55:57.534Z | 2026-06-08 |
| 【フルリモート】AI(Claude cowork等)を使った業務改善を手伝ってくださる方大募集! | 2026-05-14T08:40:23.686Z | 2026-05-27 |

On this observation date those `publishedEndDate` values are **already past**. This GET did **not** treat the sitemap sample as a live September board.

Same project HTML also contains AWS signed asset URLs with `X-Amz-Date=20260915T203206Z`. That is a **signature clock**, not a job date. Do not cite it as activity.

Help center **is** recently touched:

- Index https://help.crowdlinks.jp/ : よくある質問（ユーザー向け） **2026/8/1 13:50**
- FAQ article itself: timestamps **2024/7/29 16:18** and **2026/8/3 13:50**

Site maintenance ≠ open-job recency. Gate stays `needs_check` (login-walled listing; sampled public `publishedDateTime` is spring 2026 and sampled end dates have passed). Not `dead`. Not `thin`.

## Signup path

`/worker/signup/` static HTML is a loader. Public signup chunk `signup-654dee2220da40e7.js`:

- **「Googleで登録する」**
- **「メールアドレスで登録する」**

Login chunk `login-d30fd72bc87effc8.js`:

- **「Googleでログイン」**
- **「Facebookでログイン」**
- email / password fields also present in that chunk

FAQ (same article as fees): Google auth **cannot** be moved to another Google account; password login is the suggested alternative if the Google binding is wrong.

This GET did not click Google or submit email. CU: prefer Google on first click, MAIN mailbox only. Do not create Facebook. Do not complete OAuth from an agent session.

## Fee notes (official pages only)

User FAQ https://help.crowdlinks.jp/0029649d31534622a6d95ffe53df18dd :

> クラウドリンクスのサービスはすべて無料でご利用いただけます。 ※募集を掲載している企業より利用料を頂戴しております。

> クラウドリンクスではマッチングした企業様とユーザーが直接契約を結んていただくので、クラウドリンクス内に表示されているお仕事の報酬額から手数料は引かれません。

TOS https://crowdlinks.jp/terms :

- 「無料会員」: 利用料を支払うことなく、当社所定の範囲で利用
- 「有料会員」: 利用料を支払い、当社所定の範囲で利用

**No yen / % table** on the TOS or FAQ pages this GET opened. Do not invent a paid-plan price. If a paid-plan screen appears, stop and do not buy.

FAQ also: ほとんどがフルリモート; 出社 is called out on the project when required.

## CU tip

1. Worker https://crowdlinks.jp/worker/signup/ only.
2. Prefer **Google** (cannot switch later per FAQ). Same MAIN Google as the queue.
3. TOS member conditions include 満18歳, not a student, and **実務経験が2年以上** on the work listed on the profile. If the public record does not support two years, **do not invent years** — park this desk.
4. Profile visibility: keep to クラウドリンクス内 if the control exists. No 一般公開 from this note.
5. Do not 応募 / 話を聞きたい / マッチング報告.
6. Direct contract after match still STOP-KYC (ID / bank).
7. Do not call the desk `alive` until a human sees a **current** listing date (the spring 2026 `publishedDateTime` values are not enough).

## Gate

**needs_check**
