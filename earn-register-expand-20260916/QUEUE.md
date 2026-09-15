# 登録キュー（expanded）

案件: earn-ops マーケット登録  
版: 2026-09-16 GO（Top10 + 第2波 + High/Med ALIVE のみ。薄い机は切る）  
枝: `earn-register-expand-20260916/`

## 運用ルール（先に読む）

- **認証**: MAIN Google のみ。別アカウントを増やさない。
- **下書きのみ**: プロフィール／出品／サービス文は draft。公開・申請・出品公開はしない。
- **KYC**: 本人確認（免許・マイナンバー・顔写真・住所証明）が出たら **即停止**。朝に本人へ渡す。エージェントは進めない。
- **秘密を書かない**: メール全文、トークン、口座、本人確認画像、パスワードはリポジトリに置かない。
- **公開しない**: このキューは作業順。マーケットへ投稿しない。PR も「下書きパック」まで。
- **薄い机を切る**: 案件が見えない・売り手登録がない・閉じている・寄せ集め専用は [SKIP.md](SKIP.md) へ。数字の捏造は禁止。
- **Wave D はゲート必須**: `needs_activity_check` は [ACTIVITY-GATE.md](ACTIVITY-GATE.md) を通すまで登録しない。

## 状態記号

| 記号 | 意味 | 次の手 |
|---|---|---|
| `done-draft` | 下書きまで確認 | 公開しない。次の机へ |
| `next` | いま登録する | MAIN Google → 下書き → 停止 |
| `week-2` | 第2波 | Wave A の next が終わってから |
| `late` | 後回し | パートナー審査・KYC・実績ゲートが重い |
| `gate` | 活動確認待ち | ACTIVITY-GATE 合格後に昇格 |
| `skip` | やらない | SKIP.md |

---

## Wave A — Top10 + Gumroad

順序どおり。**次に手を付けるのは最初の `next`。**

| # | 机 | URL（売り手入口） | 状態 | 認証 | KYC | いまやること |
|---|---|---|---|---|---|---|
| A1 | ココナラ Coconala | https://coconala.com/ | `done-draft` | MAIN Google（2026-09-16 JST ログイン確認） | 朝停止 | 出品は下書きのまま。公開しない |
| A2 | Fiverr | https://www.fiverr.com/ | `next` | MAIN Google | 朝停止 | 売り手登録 → プロフィール下書き → ギグ非公開 |
| A3 | ランサーズ Lancers | https://www.lancers.jp/ | `next` | MAIN Google | 朝停止 | ランサー登録 → プロフィール下書き |
| A4 | クラウドワークス CrowdWorks | https://crowdworks.jp/ | `next` | MAIN Google | 朝停止 | ワーカー登録 → プロフィール下書き |
| A5 | Upwork | https://www.upwork.com/ | `next` | MAIN Google | 朝停止 | Freelancer 登録。本人確認が出たら停止 |
| A6 | LinkedIn Services | https://www.linkedin.com/services | `next` | MAIN Google（既存 LinkedIn と同じ） | 朝停止 | Services 出品は下書き。求人ボードに逃げない |
| A7 | TimeTicket | https://www.timeticket.jp/ | `next` | MAIN Google | 朝停止 | 出品者登録 → チケット下書き |
| A8 | Contra | https://contra.com/ | `next` | MAIN Google | 朝停止 | Independent プロフィール下書き |
| A9 | クラウディア Craudia | https://www.craudia.com/ | `next` | MAIN Google | 朝停止 | ワーカー登録 → プロフィール下書き |
| A10 | Freelancer.com | https://www.freelancer.com/ | `next` | MAIN Google | 朝停止 | Freelancer 登録。KYC が出たら停止 |
| A+ | Gumroad | https://gumroad.com/ | `done-draft` | MAIN Google（2026-09-16 JST ログイン確認） | 朝停止 | 商品は下書きのまま。公開しない |

Wave A の残り（A2→A10）が全部 `done-draft` になってから Wave B。

**パック置き場（他エージェントが埋める）**: `earn-packs/fiverr/` など。このキューは順だけ決める。パックが無くても登録順は変えない。

---

## Wave B — Week-2（第2波）

Fit は高いが Top10 の直後。**日本の机を先に、英語圏は後半。** AI CrowdWorks は売り手入口が開いているかを登録前に目視。

| # | 机 | URL（売り手入口） | 状態 | いまやること |
|---|---|---|---|---|
| B1 | SOKUDAN | https://sokudan.work/ | `week-2` | 人材登録。首都圏寄りでもリモート可の案件があるか目視してから下書き |
| B2 | Workship | https://goworkship.com/ | `week-2` | フリーランス登録 → プロフィール下書き |
| B3 | 複業クラウド | 人材 https://talent.aw-anotherworks.com/ ／案内 https://cl.aw-anotherworks.com/ | `week-2` | **人材側**で登録。企業向け画面に入らない |
| B4 | CrowdLinks | https://crowdlinks.jp/ | `week-2` | ワーカー実名登録。企業ページ（`/client/`）は使わない |
| B5 | Anycrew | 人材 https://www.any-crew.com/ ／企業 https://biz.any-crew.com/ | `week-2` | **人材側**。企業コンソールはスキップ |
| B6 | MENTA | https://menta.work/ | `week-2` | メンター登録 → プラン下書き。公開しない |
| B7 | ストアカ | https://www.street-academy.com/ | `week-2` | 講師登録 → 講座下書き |
| B8 | Guru | https://www.guru.com/ | `week-2` | Freelancer 登録 → プロフィール下書き |
| B9 | PeoplePerHour | https://www.peopleperhour.com/ | `week-2` | Freelancer 登録。本人確認が出たら停止 |
| B10 | Malt | https://www.malt.com/ | `week-2` | Freelance 登録。EU 偏りなら ACTIVITY-GATE の言語欄に記録 |
| B11 | Workana | https://www.workana.com/ | `week-2` | Freelancer 登録。LATAM 偏りなら記録して続行可否を本人へ |
| B12 | Freelancermap | https://www.freelancermap.com/ | `week-2` | Freelancer 登録。DE/EU 偏りなら記録 |
| B13 | YOUTRUST | https://youtrust.jp/ | `week-2` | プロフィール下書き。SNS 実名連携を求められたら記録。KYC なら停止 |
| B14 | Offers | https://offers.jp/ | `week-2` | 副業・業務委託の人材側。転職導線だけならゲート再判定 |
| B15 | AI CrowdWorks | 案内は CrowdWorks 公式ニュース。入口は登録時に公式から辿る | `week-2` | **売り手事前登録が開いているか**を先に目視。閉じていたら `gate` に落とす。数値は書かない |
| B16 | Skill Shift | https://skillshift.jp/ | `week-2` | 複業人材登録。地域案件が現場のみなら SKIP の現地労働へ |
| B17 | ITプロパートナーズ | https://itpropartners.com/ | `week-2` | フリーランス登録 → プロフィール下書き |

Wave B 完了後に Wave C。パートナー系は Wave C の LATE 枠。

---

## Wave C — Fit High の残り（ALIVE のみ）

Top10 と Week-2 に入っていない **High 机**。薄い・閉じた・寄せ集めは載せない。  
**Zapier / Make / n8n パートナーは LATE**（実績・審査が重い。朝の本人作業）。

### C1. いまの残り High（パートナー以外）

登録は Wave B の後。いずれも下書きのみ。KYC で停止。

| # | 机 | URL | なぜ残り High か | 状態 | いまやること |
|---|---|---|---|---|---|
| C1 | ビザスク | https://visasq.co.jp/ | スポット知見。AI／自動化の実務相談と合う | `week-2` 後 | アドバイザー登録 → プロフィール下書き |
| C2 | クラウドテック | https://crowdtech.jp/ | CrowdWorks 系の高スキル業務委託 | `week-2` 後 | フリーランス登録。エージェント面談が必須なら `late` |
| C3 | レバテックフリーランス | https://freelance.levtech.jp/ | IT 業務委託の本線。机は厚い | `week-2` 後 | 登録。営業担当が付くなら下書きプロフィールまでで止める |
| C4 | note | https://note.com/ | 日本語のデジタル販売（Gumroad の JP 補完） | `week-2` 後 | 有料記事・メンバーシップは **下書き**。公開しない |
| C5 | BOOTH | https://booth.pm/ | 日本語デジタル配布。Gumroad と役割が近い | `week-2` 後 | 商品下書き。公開しない |
| C6 | Kwork | https://kwork.com/ | カタログ型ギグ。Fiverr の補完 | `week-2` 後 | 売り手登録 → サービス下書き |
| C7 | Codementor | https://www.codementor.io/ | ライブ助言・短い実装。自動化相談と合う | `week-2` 後 | Mentor 登録 → プロフィール下書き |
| C8 | Braintrust | https://www.usebraintrust.com/ | 高単価ネットワーク。評価SaaS の Braintrust ではない | `week-2` 後 | Talent 登録。審査が本人確認なら停止 |

これ以外の「High では？」は **新規机を増やさない**。ACTIVITY-GATE に通し、合格したらこの表へ 1 行追加する。不合格は SKIP。

### C2. LATE — 自動化パートナー（Wave C の末尾）

実績・審査・公開ディレクトリ掲載が前提。**朝の本人**。エージェントは申請を送らない。

| # | 机 | URL | 状態 | いまやること |
|---|---|---|---|---|
| C-L1 | Zapier Solution Partners | https://zapier.com/partnerdirectory | `late` | ディレクトリを目視。申請は本人。下書き経歴だけ用意 |
| C-L2 | Make Partners | https://www.make.com/en/partners | `late` | 同上 |
| C-L3 | n8n Experts / Creators | https://n8n.io/ （公式の Experts/Creators 入口をその場で辿る） | `late` | 入口がコミュニティ投稿だけなら `gate`。パートナー申請は本人 |
| C-L4 | Toptal | https://www.toptal.com/ | `late` | スクリーニング＋KYC が重い。朝の本人。今は登録しない |

---

## Wave D — Fit Med（`needs_activity_check`）

**登録禁止。** チェックリスト合格後にだけ「薄い Med を切る／残す」を決める。  
合格しても Wave A/B より後ろ。不合格・薄い・寄せ集めは SKIP。

| # | 机 | URL | タグ | ゲート |
|---|---|---|---|---|
| D1 | シュフティ | https://www.shufti.jp/ | `needs_activity_check` | 在宅案件が今も出ているか。主婦特化で机が薄いなら SKIP |
| D2 | ママワークス | https://mamaworks.jp/ | `needs_activity_check` | 売り手入口と最近の募集の有無 |
| D3 | Twine | https://www.twine.net/ | `needs_activity_check` | クリエイティブ案件の新しさ |
| D4 | 99designs | https://99designs.com/ | `needs_activity_check` | コンテスト中心なら本線と合わない → SKIP thin |
| D5 | Truelancer | https://www.truelancer.com/ | `needs_activity_check` | スパム机になっていないか |
| D6 | Fastwork | https://www.fastwork.co/ | `needs_activity_check` | TH/SEA 偏り。日本語客が無ければ SKIP thin |
| D7 | Dribbble | https://dribbble.com/ | `needs_activity_check` | ポートフォリオ寄せ集めなら SKIP aggregators |
| D8 | Wellfound | https://wellfound.com/ | `needs_activity_check` | 求人ボードだけなら SKIP aggregators。Services 相当が無ければ切る |

ゲート結果の書き方（数字を作らない）:

```
日付:
机:
公式URL:
結果: pass / fail-closed / fail-thin / fail-aggregator / fail-local / fail-kyc-stop
見たもの: （例: 募集カードの日付表示、売り手登録ボタン、閉鎖文）
次: QUEUE昇格 / SKIPへ移動 / 本人の朝
```

---

## 1回の作業（15–25分）

1. このファイルで最初の `next`（無ければ最初の `week-2`）を1つだけ開く。
2. MAIN Google で入る。別アカウントを作らない。
3. 売り手／人材側か確認。企業コンソールなら閉じる。
4. KYC が出たら保存せず閉じる。朝の本人へ机名と画面の種類だけ伝える。
5. プロフィールまたは商品を **下書き**。公開トグルは触らない。
6. 状態を `done-draft` に変え、次の机へ。秘密は書かない。

## やらないこと

- 出品公開、プロフィール公開、パートナー申請の送信
- KYC 書類のアップロード
- 秘密のコミット
- Wave D の先回り登録
- 案件数・GMV・「稼げる額」の創作
