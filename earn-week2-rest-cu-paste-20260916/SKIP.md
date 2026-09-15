# SKIP.md — Week2-rest CU-23–CU-28

観測: 2026-09-16 JST。公開 GET のみ。登録なし。

薄い／閉鎖と判定した机は、ここに理由を書いてパック本文を書かない。生きていると捏造しない。

## この回の結果

**SKIP 0件。** CU-23–CU-28 の6机は、公開ページが生きている。カタログが読めない机は `needs_check` にしてパックは残す（PR#12 と同じ。見えないことを薄いと決めない）。

| 机 | CU | 公開 GET | SKIP? | 理由 |
|---|---|---|---|---|
| Freelancermap | CU-23 | `https://www.freelancermap.com/` 200。`/projects` 200。埋め込み `created` が **2026-09-15T19:36:50+02:00** ほか同日。`/registration` 200（Freelancer / Project provider） | **no** | 売り手登録面と当日の案件タイムスタンプがある |
| YOUTRUST | CU-24 | `https://youtrust.jp/` → `/lp` 200。`/recruitment_posts` 200（SPA。カード日付なし）。ヘルプ 200 | **no** | 製品は生きている。カード未読なので薄いとしない。ゲートは `needs_check` |
| Offers | CU-25 | `https://offers.jp/` 200。`/jobs/engineer/side-job` 200。業務委託カードの更新日 **2026-09-10**。`/worker/signup` に「Google で登録する」 | **no** | 転職コピーが強いが、Jobs の業務委託が残っている |
| AI CrowdWorks | CU-26 | `https://ai.crowdworks.jp/` 200。ニュース正式リリース **2026-08-20**。人材登録 URL 200（この環境は JS 必須でフォーム本文は未描画）。`/projects/` は「読み込み中」 | **no** | 事前登録 LP は終了コピーだが、正式リリース後の机。公開ボードが読めないので `needs_check`。SKIP thin にしない |
| Skill Shift | CU-27 | QUEUE `https://skillshift.jp/` は **DNS 失敗**。公式 `https://www.skill-shift.com/` 200。公開 `GET /api/jobs` の先頭行 `created_at` **2026-09-14 … 2026-09-08**、`is_recruiting: true`。オンライン／リモートの行あり | **no** | 誤ドメインであり閉鎖ではない。現場ミックスの行はあるが机全体を現地労働 SKIP にしない |
| ITプロパートナーズ | CU-28 | `https://itpropartners.com/` 200。`/register` 200（職種選択）。`/job/sale-4` に最終更新日 **2026/09/08** の業務委託カード | **no** | エージェント型だが自前カードがある。寄せ集め専用ではない |

## 誤URL（机の SKIP ではない）

| 書いたURL | 結果 | 扱い |
|---|---|---|
| `https://skillshift.jp/`（QUEUE B16） | `curl: (6) Could not resolve host` | 公式を `https://www.skill-shift.com/` に読み替える。SKIP 行は作らない |
| `https://www.freelancermap.com/register` と `/signup` | HTTP 404 | 正は `/registration`。机は生きている |
| `https://youtrust.jp/signup` と `/register` | HTTP 404。`/users/sign_up` は `/lp` へ 302 | 登録ボタンは LP 上で人が目視。机は生きている |
| `https://itpropartners.com/signup` と `/entry`（PR#12） | 404 | 正は `/register` |

## SKIP しないもの（再掲）

- SPA でカードが空に見える → `needs_check`
- WAF / JS 必須でフォームが読めない → `needs_check`
- マーケの「○万人／○件」だけ → 活動証明に使わない。SKIP 根拠にもしない
- 現場案件が混在 → その行に応募しない。机全体は現地労働 SKIP にしない（Skill Shift）

薄いと後で分かったら、日付・URL・見たものをこのファイルへ 1 行足し、該当パック先頭に `thin_site_skip: true` を人が書く。エージェントはこの回では書かない。
