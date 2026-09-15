# B08 — DMM生成AI人材バンク

**DRAFT_ONLY.** Logged out. Did not register. Did not submit the form. No secrets.

This-folder ID **B08** ≠ QUEUE **B8** (Guru.com).  
QUEUE: **not listed**. Do not CU-serial this desk from this folder.

```
日付（JST）: 2026-09-16
机: DMM生成AI人材バンク
公式URL: https://algoage.co.jp/jinzaibanktouroku
公開ページを見たか: yes
ログインしたか: no
signup_open: LP 200「無料会員登録フォーム」見出し。静的 HTML に入力欄なし。送信していない
fee_page: FAQ の費用文は依頼者向け。人材の売り手数料 % は未記載 → 書かない
open_jobs_heuristic: 公開案件カードなし。LP がリンクする generative-ai.web-camp.io は DNS fail
last_blog_news: 未使用（マーケ「10,000名+」は活動証明にしない）
fit_still_ok: unknown（エージェント面談型。公開ボード未確認）
1 生きている: yes（登録 LP 200。閉鎖文なし。Copyright 2026）
2 寄せ集めではない: unknown（自前案内。外部ボードへ飛ばす一覧は見ていない）
3 現地だけではない: unknown（案件未読）
4 本人専用ではない: yes（公開 LP）
5 活動の目視: unknown（カード日付なし）
6 KYC: 出ていない（フォーム未描画）
7 本線: unknown（人材マッチ vs 法人向け伴走支援が FAQ 上で混在）
gate_result: needs_check
action: park. 送信しない. QUEUE に足さない.
公開したか: no
Google: 登録 HTML の Google は Tag Manager のみ。OAuth ボタンなし
有料: 人材 % 未記載。依頼者「初回相談・お見積りは無料」を売り手数料と混ぜない
SKIP thin: no（見えない机を薄いにしない）
```

## Official URL

Opened because they were already on a 200 page or linked from that page. Unused `dmm.com/...` paths were **not** invented.

| What | URL | This GET |
|---|---|---|
| Talent register LP | https://algoage.co.jp/jinzaibanktouroku | 200. Title「DMM生成AI人材バンク会員登録ページ」 |
| Algoage origin | https://algoage.co.jp/ | **404** |
| Operator / 私たちについて | https://dmm-businessai.com/about-us/ | 200. 会社名 **株式会社DMMビジネスAI** |
| FAQ | https://dmm-businessai.com/faq/ | 200. 人材バンク節は依頼者向け |
| Privacy | https://dmm-businessai.com/privacy-policy/ | 200. 共同: Algoage / DMM.com / インフラトップ |
| Linked talent list (href on LP) | https://generative-ai.web-camp.io/bank/talents/ | **DNS fail** |
| Linked TOS (href on LP) | https://generative-ai.web-camp.io/terms/resources/ | **DNS fail** |
| Guessed `/jinzaibank/` | https://dmm-businessai.com/jinzaibank/ | **404** — not a board |

Sibling PR#19 already had the Algoage register URL. This GET re-opened it. It does not copy that NOTES body.

## Public jobs / dates — what this GET actually saw

Logged-out register HTML is a **Peraichi** landing page. Visible copy (plain text after stripping tags):

- 「DMM 生成AI 人材バンクの無料会員登録フォームになります。」
- 「当サービスでは副業・フリーランス（業務委託）など、幅広い雇用形態へのサポートを行っております。」
- 「会員登録をいただき、ご面談後、ご経歴・ご希望を元にキャリアドバイザーから求人のご提案をいたします。」
- 対象コピー: 生成AIエンジニア・生成AIコンサルタントがメイン。営業・マーケ案件も案内しうる。合う求人が無いと面談できない場合がある。
- 事前に利用規約・プライバシーポリシーへ同意してから回答、とある。
- Footer: **Copyright 2026 DMM生成AI人材バンク**

Static HTML has **no `<input>` / `<select>` / `<textarea>`**. There is a Peraichi `b-html-code` embed block; the live widget was **not** painted in this GET. Form fields are unread.

No public job titles. No `created_at` / 掲載日.

The LP links `generative-ai.web-camp.io/bank/talents/` as if a talent surface exists. This environment: **Name or service not known**. Unreadable ≠ dead. Unreadable ≠ a dated catalog.

`dmm-businessai.com` home/about/FAQ are **法人向け** (研修 / エンジニアリング / パートナーズ). About-us「10,000名+ デジタル人材の育成実績」is vendor marketing — **not** activity proof.

FAQ section「DMM生成AI人材バンクについて」describes **client consulting** (ヒアリング、PoC、RAG、マニュアル整備、定着支援). That is a different surface from the talent-register LP. Do not merge them into one “job board.”

Gate stays **`needs_check`** (not `alive`/`pass`, not `dead`, not `thin`).

## Signup path

- Public LP says 無料会員登録フォーム. **Do not submit.**
- Google / Apple / Facebook **OAuth buttons: not in this HTML.** GTM snippets only.
- Prefer MAIN Google mailbox **if** a later human sees an email field. Do not mint a new SNS account.
- If Google is missing at click-time, park rather than inventing a path.
- TOS body lives on `generative-ai.web-camp.io/terms/resources/` — **unread this GET**. Human opens it before any submit.

## Fee notes (official pages only)

Cited from https://dmm-businessai.com/faq/ Q「生成AI人材バンクの費用はどのくらいですか？」:

> ご支援内容によりますが、スポット対応から継続支援まで柔軟に対応可能です。初回相談・お見積りは無料です。

That answer sits under **依頼者 / 法人** FAQ. It is **not** a worker success-fee %. Do not copy into a talent fee cell.

Worker %: **not on any 200 page this GET opened** → leave unstated.

Register heading「無料会員登録」is a form title, not a proof that placement is free for talent.

## CU tip

1. **Do not open this desk this pass.** Gate is `needs_check`. Not in QUEUE.
2. Human decides: 人材マッチ（面談必須）vs 法人伴走支援. Interview-mandatory agent desks are morning-operator, not CU.
3. If a later pass continues: do not submit from an agent. Stop at KYC / 職務経歴書ファイル / My Number / 顔写真.
4. Do not buy a client consulting package from the talent desk.
5. Do not promote to `pass` until a human sees **one dated public listing** or writes “紹介型・ボード無し” and chooses SKIP / Wave D.
6. Do not add a QUEUE row from this INDEX.

## Gate

**needs_check**

Sibling: [PR#19](https://github.com/rimone0511/autopilot-log/pull/19) catalog-gap notes (body not copied).
