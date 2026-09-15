# Catalog-gap — Skill Shift

日付（観測）: 2026-09-15 UTC  
机: Skill Shift  
QUEUE: Wave B16。QUEUE URL は `https://skillshift.jp/`  
このフォルダの判定: **needs_check**（カタログ／登録パック／Google／手数料が未確認。活動ゲートの `pass` を登録許可にしない）  
ログインしたか: no  
登録したか: no  
Pack: INDEX では `earn-packs/skill-shift/` が `unknown`

## URL（捏造しない）

| 何 | URL | この環境 |
|---|---|---|
| QUEUE の売り手入口 | https://skillshift.jp/ | **接続失敗**（DNS。ホスト解決できず） |
| 開いた公式トップ | https://www.skill-shift.com/ | HTTP 200。タイトル「【Skill Shift】地方副業で貢献を｜地域企業✕副業プロジェクト」。HTML はシェルが短い（SPA） |
| 求人 HTML | https://www.skill-shift.com/jobs | HTTP 200。本文はシェル |
| 公開 jobs API（サイトが使うもの） | https://www.skill-shift.com/api/jobs | HTTP 200。JSON |

人材登録のパス（`/signup` など）は **HTML から確定していない。捏造しない。** CU はトップから「個人／副業人材」を辿る。

## 公開 API で見えた日付（件数は書かない）

`data` 先頭行の `created_at`（この GET）: **2026-09-14, 2026-09-13, 2026-09-12, 2026-09-11**。`is_recruiting: true` の行あり。

`side_job_style` の例（見出しを活動証明にしない。働き方の混在だけ）:

- 「基本的にオンラインでの打ち合わせを想定しています。」
- 「オンライン中心」
- 「相談の上決定しましょう！」

対面／現地ミックスがあり得る。**現場のみと分かった行は応募しない。** 机全体を現地労働 SKIP には、この NOTES では落とさない。

`meta` の件数・pagination.total は **書かない**。

## 兄弟 activity-gate（参考）

JP Wave B は公式ドメイン読み替えのうえ活動 `pass`。Google は未確認。ここは **catalog-gap** なので `needs_check`。

## 手数料

**書かない。** 公開 GET では料金表を確定していない。CU 前にライブの人材手数料・紹介料・有料会員を人が見る。無ければ空欄のまま。

## CU の前に確認すること

- [ ] ブラウザで `skill-shift.com` が公式か（証明書・会社名・QUEUE メモ）。`skillshift.jp` は使わない
- [ ] 個人／副業人材の登録ボタンがある。企業の求人掲載コンソールに入らない
- [ ] Google があるか。無ければメール（MAIN Google のメール）。新規 SNS 禁止
- [ ] KYC・顔写真身分証・口座が初画面に出ないか
- [ ] 有料壁（優先表示、紹介料前払い）が無いか。あったら額を invent せず止める
- [ ] 公開一覧または API 相当で、今週〜数日の `created_at` / 更新表示がまだあるか
- [ ] 本線（AI／業務効率化のリモート行）が残っているか。現場シフトばかりなら人が SKIP 現地労働
- [ ] パック未作成。プロフィール文は別途。この NOTES で登録完了にしない

次: URL 読み替えを QUEUE 側に人が書くのは別 PR。この PR では登録しない。
