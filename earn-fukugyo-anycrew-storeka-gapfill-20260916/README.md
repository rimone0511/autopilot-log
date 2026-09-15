# Gap-fill CU notes — 複業クラウド / Anycrew / ストアカ (2026-09-16)

状態: **DRAFT_ONLY**  
対象: 先行パックが **`needs_check`** のまま残した 3 机（CU-12 / CU-15 / CU-17）。  
このフォルダは Computer Use（CU）へ渡す **ギャップ埋め + 貼り付けスタブ**。アカウントではない。**この PR では登録しない。**

禁止: 秘密、ブラウザ登録、公開、応募、出品、KYC アップロード、有料プラン、件数・GMV・「稼げる額」の創作、手数料％の発明。

観測: **公開 GET のみ**（ログイン Cookie なし）。WAF / Cloudflare で本文が読めない URL は **`needs_check` のまま**。死滅とはしない。

## この GET で埋まった穴 / 残る穴

| 机 | INDEX CU | 先行 activity_gate | このフォルダ | Google | 手数料 |
|---|---|---|---|---|---|
| [01-fukugyo-cloud.md](01-fukugyo-cloud.md) | CU-12 | needs_check（SPA・日付未読） | **needs_check**（案件本文・新着日は未読） | **PREFER_GOOGLE**（`/sign_up` 公開 JS に「Googleでサインイン」） | タレント「無料で利用」**cited**（TOS 第2.1条1）。人材％は TOS に無し → **needs_check** |
| [02-anycrew.md](02-anycrew.md) | CU-15 | needs_check（`/offers` SPA 空） | **needs_check**（案件カード未読） | **PREFER_GOOGLE**（アプリ HTML「Googleでログイン」） | 人材「一切費用はかかりません」**cited**。人材％なし → **needs_check** |
| [03-street-academy.md](03-street-academy.md) | CU-17 | needs_check（www WAF・ヘルプ 403） | 一覧は **pass**（`/online/all` に 2026-09-16 以降の開催日）。個別講座・ヘルプは WAF **needs_check** | **NOT_OFFERED_OAUTH**（`/register` に LINE / Facebook / メール。Google ボタン無し） | 公式 `/fee` の 10 / 30（対面 20）/ リピート 10 **cited**。ヘルプ本文 403 は **needs_check** |

`thin_site_skip`: 3 机とも **false**。読めない ≠ 死んでいる。

## 兄弟（本文は複製しない）

- 活動ゲート: `earn-activity-gate-waveB-20260916/`（PR#12）— この PR は上書きしない
- JP Week2 薄パック: `earn-register-packs-jp-20260916/`（PR#3）
- Wave B サンプル: `earn-waveb-alive-handoff-sample-20260916/`（PR#21）
- 深掘り（Anycrew / ストアカ含む）: `earn-skillshift-sokudan-menta-deep-20260916/`（PR#33）
- CU 直列索引: `earn-register-pack-index-20260916/INDEX.md`（PR#8）

本番直列は **CU-11 Workship から**。このフォルダはギャップ埋めであり、Workship / CrowdLinks を飛ばす合図ではない。

## CU 共通

1. 1 机ずつ。人材／売り手入口だけ。企業コンソールなら閉じる。
2. MAIN Google のみ。メールは `{{EMAIL}}`。別アカウント禁止。
3. プロフィール・自己紹介は **下書き保存**。公開・応募・講座公開はしない。
4. Gmail OTP は親（Gmail MCP）。CU ブラウザで Gmail を開かない。
5. SMS が要る画面はユーザーチャット待ち。不在なら park。
6. KYC が出たらアップロードせず停止。[STOP-KYC.md](STOP-KYC.md)
7. 画面のラベルがパックと違うときは **画面を正** とする。
8. 値はプレースホルダのまま。実メール・電話・パスワード・身分証を git に書かない。
9. **`needs_check` の机は、人が公開一覧を 1 画面見るまで登録しない。** ストアカの個別講座が WAF なら park。ヘルプ 403 を料率の根拠にしない（`/fee` を正とする）。

観測の生ログ: [METHOD.md](METHOD.md)  
貼る順: [INDEX.md](INDEX.md)  
後続 CU スタブ: [CU-PROMPT.md](CU-PROMPT.md)
