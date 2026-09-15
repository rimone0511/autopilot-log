# STATUS — CrowdLinks (B04) CU handoff

Snapshot: **2026-09-16** (folder stamp; authoring GET ~2026-09-15 21:00 UTC / 2026-09-16 JST)  
Folder: `ops/earn/earn-crowdlinks-cu-handoff-20260916/`  
State: **DRAFT_ONLY**

This file is the desk box for **B04 / QUEUE Wave B / CU-14 クラウドリンクス (CrowdLinks)**. It is not a signup log and **does not claim an account exists**.

Authoring session: public CrowdLinks HTML + Help Center + TOS only. **No login. No 同意して会員登録する. No credentials invented or stored.**

---

## Desk hint

| Field | Value |
|---|---|
| Desk | CrowdLinks worker（クラウドリンクス） |
| IDs | **B04** · QUEUE **Wave B** · **CU-14** |
| Not | CrowdWorks.jp · `/client/` 契約企業 |
| CU hint | `pending` — pack ready; live CU has **not** run this folder |
| Activity gate | **needs_check** ([PR#12](https://github.com/rimone0511/autopilot-log/pull/12) · [PR#62](https://github.com/rimone0511/autopilot-log/pull/62)). This GET did **not** upgrade it to `alive` |
| Google | MAIN only (`Googleで登録する` in signup JS; icon/label **at click-time**. Static HTML has no “Google”) |
| Plan | 無料会員 only ([FAQ](https://help.crowdlinks.jp/0029649d31534622a6d95ffe53df18dd) qualitative free / no commission-cut. **No yen table**) |
| Stop | **応募 / 話を聞きたい** + KYC/phone/paid — [STOP.md](STOP.md) |
| Runner | [PLAYBOOK.md](PLAYBOOK.md) · [FIELD-MAP.md](FIELD-MAP.md) |
| Paste | 石田祐太 n8n / AI automation JP — FIELD-MAP fences (200 / 800 counted) |

Sibling paste (bodies not merged here except n8n fences already in FIELD-MAP):

| Pack | PR |
|---|---|
| Thick CU-14 | [#30](https://github.com/rimone0511/autopilot-log/pull/30) |
| Thin Week2 | [#3](https://github.com/rimone0511/autopilot-log/pull/3) |
| Gate record | [#12](https://github.com/rimone0511/autopilot-log/pull/12) |
| Gate note batch1 | [#62](https://github.com/rimone0511/autopilot-log/pull/62) |

---

## Public livecheck (authoring, 2026-09-16 JST, no login, no POST)

| URL | HTTP | Result used |
|---|---|---|
| https://crowdlinks.jp/ | 302→200 | Final https://start.crowdlinks.jp/ title **クラウドリンクス - ハイクラス副業マッチングサイト** |
| https://start.crowdlinks.jp/ | 200 | Same marketing home |
| https://crowdlinks.jp/worker/signup/ | 200 | Title **新規登録【クラウドリンクス】**. Loader HTML. Chunk `signup-654dee2220da40e7.js` |
| signup JS (same host, GET) | 200 | **Googleで登録する** / **Facebookで登録する** / **メールアドレスで登録する** / 利用規約+個人情報の取り扱い同意 / **同意して会員登録する** / password copy 半角英字・数字・記号を含む8文字以上 |
| https://crowdlinks.jp/worker/login/ | 200 | `/login/` 301/308 → here |
| login JS `login-d30fd72bc87effc8.js` | 200 | **Googleでログイン** / **Facebookでログイン** / メール / パスワード |
| https://crowdlinks.jp/worker/projects/ | 200 | Title プロジェクト一覧. `pageProps` empty. JS labels: 募集中のみ表示 / 職種 / 稼働時間 / リモート可否 / おすすめ順 / 新着順. **No cards** |
| https://crowdlinks.jp/projects | 200 | Older shell. Not used as a live board |
| https://crowdlinks.jp/sitemap.xml | 200 | **299** `/projects/{id}` locs. **0** `<lastmod>`. Count ≠ traffic |
| https://crowdlinks.jp/projects/mUCkNAz6f6WxisGMnzzG | 200 | Title ID1056 SharePoint… `publishedDateTime` 2026-05-21T01:46:09.004Z · `publishedEndDate` 2026-06-19 · CTA 応募フォーム. `X-Amz-Date=20260915T210830Z` = signature clock **not** a job date |
| https://crowdlinks.jp/projects/cU1XcGkZuiKMM1J1Wqyp | 200 | ID1055 BPO… same spring dates / end 2026-06-19 |
| https://crowdlinks.jp/projects/2ohybl2MyHPftkRSo2U6 | 200 | 社長秘書… `publishedDateTime` 2026-05-19T06:53:18.737Z · end 2026-06-17 |
| https://crowdlinks.jp/terms | 200 | 無料会員条件: 満18歳 / 学生でない / **記載業務の実務経験2年以上** / 所属規則に反していない. 第3条4 追加書類. 第4条 有料会員. **No yen table** |
| https://crowdlinks.jp/worker/terms/ | 200 | Signup-linked TOS |
| https://crowdworks.co.jp/privacy_policy/01/ | 200 | Signup-linked 個人情報の取り扱い |
| https://help.crowdlinks.jp/ | 200 | Worker FAQ heading timestamp **2026/8/1 13:50** (index) |
| https://help.crowdlinks.jp/0029649d31534622a6d95ffe53df18dd | 200 | User FAQ. Timestamps **2024/7/29** and **2026/8/3**. Free / no commission-cut / 本名推奨 / 経歴1+ / 応募フォームへ / Google付け替え不可 |
| https://help.crowdlinks.jp/guide | 200 | Link to プロフィール記入サンプル |
| https://help.crowdlinks.jp/guide/resume-sample | 200 | Headings キャリアの概要・略歴 / 課題解決できること. Edit URLs self_introduction + capability |
| https://help.crowdlinks.jp/642ef850db334df8a4ee93a2f330a09a | 200 | スキルタグ + 経験年数 5 bins. URL `.../profiles/edit/skill_tag/` |
| https://help.crowdlinks.jp/corporate_block | 200 | 企業ブロック。正式名称 |
| https://help.crowdlinks.jp/15c33f48ad3041ce9a0975ba863b6c32 | 200 | 写真・氏名。`.../profiles/edit/base/` |
| https://help.crowdlinks.jp/change-mail-tel | 200 | 電話・メールはアカウント設定の連絡先。**STOP unless draft-blocked** |
| https://help.crowdlinks.jp/entry_guidelines | 200 | 応募ガイドライン = TOS eligibility restate. **Do not 応募** |
| https://help.crowdlinks.jp/login-how-w | 200 | Googleログインのみの場合あり。二重アカウント注意 |
| https://crowdlinks.jp/client/ | 200 | 契約企業 LP — **close**. Marketing has 実名登録・現職記載; not a worker how-to |
| https://crowdlinks.jp/worker/profiles/edit/base/ | 200 | SPA title プロフィール編集. Logged-out loader. **Not** a completed profile |
| https://crowdlinks.jp/privacy | 404 | Use CrowdWorks privacy URL from signup JS instead |

CSRF tokens, OAuth client secrets, and AWS signed asset URLs are **not** recorded here.

`thin_site_skip: false`.  
`gate: needs_check` (login-walled listing; sampled public `publishedEndDate` already past; help recently touched ≠ live September board).

**No invented volume. No invented 手数料％ / 円.**

---

## Live CU outcome (empty until a human/CU runs the playbook)

Do not pre-fill success. Valid later values match PLAYBOOK:

```
desk: CrowdLinks
pack: ops/earn/earn-crowdlinks-cu-handoff-20260916/
ids: B04 / QUEUE-Wave-B / CU-14
auth:
otp:
kyc:
draft_profile:
entry: no
scout_reply: no
matching_report: no
publish: no
visibility:
plan: free
paid: no
bank: no
phone:
rate:
years:
next: stop
```

Current: **not run**.

---

## This PR does not

- Create or log into a CrowdLinks account
- Invent or commit Google / email / password / OTP / phone / bank / My Number
- Press **応募フォームへ** or **話を聞きたい**
- Reply to スカウト or マッチング報告
- Open 有料会員 / 追加書類 / 口座
- Fill 電話 SMS unless a later live run is draft-blocked (then user-chat only)
- Invent worker 手数料％, 会員数, or open-job volume
- Invent 実務経験2年
- 一般公開 a profile
- Mix CrowdLinks with CrowdWorks
- Merge sibling pack folders
- Change Python posting-gate tests
