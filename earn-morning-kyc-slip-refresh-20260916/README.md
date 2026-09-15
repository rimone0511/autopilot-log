# 朝の本人確認スリップ refresh — 2026-09-16

案件: earn-ops 朝の本人確認  
版: 2026-09-16 GO **refresh**（机の状態が動いたあとの6枚）  
枝: `earn-morning-kyc-slip-refresh-20260916/`  
誰: **祐太だけ**（エージェントは上げない・登録しない）  
認証: **MAIN Google だけ**。別アカウントを作らない。

> **DRAFT_ONLY.** 出品・プロフィール・商品は下書きのまま。公開しない。秘密なし。エージェントからの signup なし。

これは [PR#4](https://github.com/rimone0511/autopilot-log/pull/4) `earn-kyc-morning-checklist-20260916/` の **全机1枚** を置き換えない。  
いま `blocked_skip` か `draft_saved` の机だけを **1机1スリップ** にする（Upwork 含む。live: Google SSO skip）。LinkedIn も `blocked_skip`（login reCAPTCHA）だが、このフォルダにスリップは置かない。

TimeTicket / Contra / クラウディア / Freelancer.com の **本人確認文** はまだ PR#4。Wave B–D も対象外。CU の次机だけ下のポインタを正とする。

---

## このフォルダ

| File | Desk | CU hint（この refresh の正） |
|---|---|---|
| [01-coconala.md](01-coconala.md) | ココナラ Coconala | `draft_saved` |
| [02-fiverr.md](02-fiverr.md) | Fiverr | `blocked_skip` **hold** |
| [03-lancers.md](03-lancers.md) | ランサーズ Lancers | `blocked_skip` **captcha** |
| [04-crowdworks.md](04-crowdworks.md) | クラウドワークス CrowdWorks | `blocked_skip` **403** |
| [05-upwork.md](05-upwork.md) | Upwork | `blocked_skip` **Google SSO** |
| [06-gumroad.md](06-gumroad.md) | Gumroad | `draft_saved` |

### CU ポインタ（この refresh の正。LinkedIn を next にしない）

| Desk | CU hint | このフォルダ |
|---|---|---|
| LinkedIn（A6） | `blocked_skip` **reCAPTCHA**（login） | スリップなし。next にしない。Services は GO-gated / not enabled — 開かない |
| **TimeTicket（A7）** | **in progress（いま開く CU）** | スリップなし。KYC は PR#4 |
| Contra（A8） | after TimeTicket | スリップなし。KYC は PR#4 |
| クラウディア Craudia（A9） | after Contra | スリップなし。KYC は PR#4 |
| Freelancer.com（A10） | after Craudia | スリップなし。KYC は PR#4 |

順: **TimeTicket → Contra → Craudia → Freelancer**。LinkedIn login の reCAPTCHA はエージェントから再試行しない。2つ目の LinkedIn を作らない。

CU ポインタの出典: live box（Upwork Google SSO skip + LinkedIn reCAPTCHA skip）が [PR#35 MASTER INDEX](https://github.com/rimone0511/autopilot-log/pull/35) の「Upwork next」より新しい。Fiverr hold / Lancers captcha / CW 403 は同じ。  
ココナラと Gumroad の `draft_saved` は [PR#1 QUEUE](https://github.com/rimone0511/autopilot-log/pull/1) の `done-draft`（公開しない）。  
[PR#24 REGISTER-BOARD](https://github.com/rimone0511/autopilot-log/pull/24) の「CW next」と PR#35 の「Upwork next」は古い。パック本文は複製しない。

---

## 机の上（揃うまでサイトを開かない）

- [ ] 運転免許証（表・裏）**実物**
- [ ] マイナンバーカード **表面だけ**（番号の面は伏せる）
- [ ] パスポート（英語サイト用。ある人）
- [ ] スマホ（カメラ・SMS。**VPNオフ**）
- [ ] 明るい場所（自撮り）

番号・口座・パスワードは、紙にも git にもチャットにも書かない。書類写真も置かない。

---

## 5つの止め（全スリップ共通）

1. **同時に2サイト開かない。** 1スリップ終わるまで次を触らない。
2. **出品・プロフィール・商品を公開しない。** 本人確認だけ。`draft_saved` を公開にしない。
3. **書類写真を git / チャット / 共有フォルダに置かない。** サイトの画面にだけ上げる。
4. **有料は一呼吸。** Fiverr 手数料・Seller Plus・Connects・Gumroad boost は、迷ったら閉じる。
5. **詰まったら閉じる。** 同じ机を3回叩かない。`blocked_skip` の原因（hold / captcha / 403 / Google SSO / LinkedIn reCAPTCHA）をエージェントから再試行しない。

状態の書き方（机の名前だけ）: `なし` / `上げた` / `待ち` / `詰まった` / `draft_savedのまま` / `blocked_skipのまま`

---

## エージェントがやってはいけないこと

- マーケットへ **signup / 会員登録を完了しない**
- 本人確認・税・口座の **アップロードをしない**
- 出品公開、Catalog Submit、応募、提案送信をしない
- hold / captcha / **403** / Upwork **Google SSO** / LinkedIn **reCAPTCHA** を再試行しない
- 秘密（OTP、口座、マイナンバー、ID画像）をログや git に残さない

エージェントが KYC 画面を見たら: 机名と画面の種類だけ書いて **閉じる**。このフォルダを朝の本人へ渡す。

---

## 朝の順（目安。全部やらなくていい）

`draft_saved` は **公開しに戻らない**。画面が出たときだけスリップを開く。

1. ココナラ — 振込・NDAの画面が出たときだけ
2. Gumroad — 出金（Stripe）の画面が出たときだけ。商品は unpublished のまま
3. Fiverr — **hold のまま**。人が hold を外したあと、ID が出たらこのスリップ
4. ランサーズ — **captcha は人**。エージェントは叩かない。ID が出たらこのスリップ
5. クラウドワークス — **403 は再試行しない**。自分の回線で開いて ID が出たらこのスリップ
6. Upwork — **Google SSO skip のまま**。人が MAIN Google に入れるようになったあと、ID が出たらこのスリップ。Connects を買わない。LinkedIn は **reCAPTCHA skip**（next にしない）。次の CU は **TimeTicket**（in progress）→ Contra → Craudia → Freelancer

3つやったら休憩。

---

## 朝が終わったら（机の名前だけ）

- 上げた:
- 待ち:
- なし:
- 詰まった:
- `draft_saved` のまま（公開していない）:
- `blocked_skip` のまま（再試行していない）:

根拠は各社の公開ヘルプ（観測 2026-09-15〜16）。**画面と違うときは画面を正** とする。
