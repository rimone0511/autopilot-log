# Wave B ALIVE handoff sample — CU-ready DRAFT profile packs (2026-09-16)

状態: **DRAFT_ONLY**  
対象: Wave B のうち **よくあるセルフサーブ** 5机だけ。  
このフォルダは Computer Use（CU）へ渡す **サンプル手渡し**。パック本文は下書き。**このPRでは登録しない。**

禁止: 秘密、ブラウザ登録、公開、応募、出品、KYCアップロード、有料プラン、件数・GMV・「稼げる額」の創作。

兄弟資料（本文は複製しない）:

- 活動ゲート: `earn-activity-gate-waveB-20260916/`（PR#12）
- JP Week2 登録パック: `earn-register-packs-jp-20260916/`（PR#3）
- CU直列索引: `earn-register-pack-index-20260916/INDEX.md`（PR#8）
- 朝の本人確認: `earn-kyc-morning-checklist-20260916/`（PR#4）

## 5机

| 在庫 | 机 | INDEX CU | activity_gate | Google | このサンプルでの扱い |
|---|---|---|---|---|---|
| [01-sokudan.md](01-sokudan.md) | SOKUDAN | CU-13 | **pass** | PREFER_GOOGLE（登録HTMLに `/users/auth/google`） | 唯一 pass。サンプル直列の先頭 |
| [02-fukugyo-cloud.md](02-fukugyo-cloud.md) | 複業クラウド | CU-12 | **needs_check** | **needs_check**（人材トップはSPA。ボタン未描画） | 人材ドメインだけ。企業コンソール禁止 |
| [03-anycrew.md](03-anycrew.md) | Anycrew | CU-15 | **needs_check** | PREFER_GOOGLE（「Googleでログイン」公開面） | `/offers` はSPA空。案件日付は人の1画面 |
| [04-menta.md](04-menta.md) | MENTA | CU-16 | **needs_check** | PREFER_GOOGLE（`register/choose` に Google OAuth） | プラン公開は出品。プロフィール保存まで |
| [05-street-academy.md](05-street-academy.md) | ストアカ | CU-17 | **needs_check** | **NOT_OFFERED_OAUTH**（公式ヘルプ: LINE / Facebook / メール） | この環境の www は WAF。ヘルプ再読 |

含めない（このサンプルの外）: Workship（CU-11。Googleアイコン目視）、CrowdLinks（実務2年条件）、Shufti（Wave D gate）、Skill Shift / ITプロパートナーズ / Offers / YOUTRUST（エージェント寄り）。

## ラベル

| ラベル | 意味 |
|---|---|
| `pass` | 公開ページに新しさの手がかりがある。下書き登録の検討可。公開しない |
| `needs_check` | 公開情報が足りない（SPA / WAF / 日付なし / 手数料ページがこの環境で読めない）。推測で pass にしない |
| `cu_ready` | Field map と貼る文がある。**登録済みではない** |
| `self_serve` | 公開フローが Web プロフィール型（面談必須と書いていない）。エージェント机ではない |

`thin_site_skip` は全5件 **false**。読めない ≠ 死んでいる。

## CU 共通（全パック）

1. Wave A の `next` が全部 `done-draft` になるまで、本番直列では Week2 を開かない（INDEX どおり）。このフォルダは **手渡しサンプル**。
2. 1机ずつ。人材／売り手入口だけ。企業コンソールなら閉じる。
3. MAIN Google のみ。メールは `{{EMAIL}}`。別アカウント禁止。
4. プロフィール・自己紹介は **下書き保存**。公開・応募・プラン出品・講座公開はしない。
5. Gmail OTP は親（Gmail MCP）。CU ブラウザで Gmail を開かない。
6. SMS が要る画面はユーザーチャット待ち。不在なら park して次へ。
7. KYC（身分証・顔・マイナンバー・口座・Stripe本人確認）が出たらアップロードせず停止。朝の本人へ机名と画面の種類だけ。
8. 画面のラベルがパックと違うときは **画面を正** とする。
9. 値はプレースホルダのまま。実メール・電話・パスワード・身分証を git に書かない。

## 観測

公開 GET / 公式ヘルプのみ。ログインしていない。登録していない。有料を開いていない。  
詳細: [METHOD.md](METHOD.md) / 貼る順: [INDEX.md](INDEX.md)
