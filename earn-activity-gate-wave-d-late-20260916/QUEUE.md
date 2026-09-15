# QUEUE-ready — Wave D late 活動ゲート

案件: earn-ops Wave D late（D11–D20）  
観測: 2026-09-16 JST  
枝: `earn-activity-gate-wave-d-late-20260916/`

親キュー: `earn-register-expand-20260916/QUEUE.md`（Wave D は D1–D8 のみ。`needs_activity_check` のまま登録禁止）。  
**QUEUE に D-late 行は無い。** この表はゲート結果の skip だけ。昇格なし。Wave A には上げない。公開しない。

認証: MAIN Google のみ（メール登録なら MAIN Google のメール）。別アカウントを作らない。  
KYC: 免許・パスポート・顔写真・住所証明が出たらアップロードせず停止。朝の本人。

## 状態記号

| 記号 | 意味 | 次の手 |
|---|---|---|
| `week-2` 後 | ゲート合格。A/B と既存 C の後ろ | この観測では **行が無い** |
| `gate` | 公開一覧が未読 | この観測では **行が無い** |
| `skip` | やらない | [SKIP.md](SKIP.md) |

---

## 合格 → Wave C 末尾 Med

**なし。** keep 0。

---

## gate のまま（登録しない）

**なし。** `needs_check` 0。

---

## SKIP（QUEUE に戻さない）

| # | 机 | 判定 | SKIP節 |
|---|---|---|---|
| D11 | Comet | `fail-closed` | 閉じた机（freelance ダッシュボード閉鎖。LP はコンサル） |
| D12 | Replit Bounties | `fail-closed` | 閉じた机（Contra へ 301。Contra は Wave A） |
| D13 | Superpeer | `fail-closed` | 閉じた机（スタンドアロン sunset 2024-12-31。Skillshare へ 301） |
| D14 | We Work Remotely | `fail-aggregator` | 寄せ集め専用（リモート求人ボード） |
| D15 | Remote OK | `fail-aggregator` | 寄せ集め専用（リモート求人ボード） |
| D16 | Himalayas | `fail-aggregator` | 寄せ集め専用（リモート求人ボード） |
| D17 | ココナラテック | `skip-agent` | 面接エージェント専用 |
| D18 | Findy Freelance | `skip-agent` | 面接エージェント専用 |
| D19 | PRONI アイミツ | `fail-thin` | 薄い机（企業向け一括見積・有料掲載） |
| D20 | 比較ビズ | `fail-thin` | 薄い机（企業・専門家の掲載。個人カタログではない） |

詳細は [SKIP.md](SKIP.md) と [SUMMARY.md](SUMMARY.md)。

---

## 親 QUEUE 対照

| 元 | このゲート |
|---|---|
| Wave D D1–D8 | 対象外（PR#13 側） |
| Wave D D-late 行 | **QUEUE に無い。追加していない** |
| Wave C LATE C-L1–C-L4 | 対象外（Zapier / Make / n8n / Toptal。再ゲートしない） |
| オペレーター指定 D11–D20 | このフォルダ。全部 skip |

---

## やらないこと

- 出品公開、プロフィール公開、CV 送信、パートナー掲載申込
- KYC 書類のアップロード
- 秘密のコミット
- ゲート不合格机の先回り登録
- 案件数・GMV・「稼げる額」の創作
- Contra / Skillshare をこのゲートから新規キューに足すこと
