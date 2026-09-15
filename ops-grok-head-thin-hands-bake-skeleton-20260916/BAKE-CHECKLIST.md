# BAKE-CHECKLIST — GROK-HEAD-THIN-HANDS

状態: **DRAFT BAKE / Pro recovered / production APPLY still blocked**  
対象フォルダ: `ops-grok-head-thin-hands-bake-skeleton-20260916/`  
プレースホルダ埋めは回収 Pro で行った。**本番 APPLY はまだしない。**

確認コマンド（COMMON と WINDOW に未埋めスロットが残っていないこと）:

```bash
rg -n '\{\{PRO_RULE\}\}' \
  ops-grok-head-thin-hands-bake-skeleton-20260916/COMMON-THIN.md \
  ops-grok-head-thin-hands-bake-skeleton-20260916/WINDOW-CARD.md
```

期待: マッチなし。

---

## 0. Pro 回収（下書き焼き）

- [x] GROK-HEAD-THIN-HANDS の Pro 回答が着いている（HANDS 回収。GrokBOT本体。NOT Cursor Grok 4.6）
- [x] [COMMON-THIN.md](COMMON-THIN.md) と [WINDOW-CARD.md](WINDOW-CARD.md) に `{{PRO_RULE}}` スロットが残っていない
- [ ] 本人が「この文面で本番へ焼け」と明示している
- [ ] 本番 APPLY 済み、とは書かない

今は下書き焼きまで。**本番へ焼かない。**

---

## 1. ロックが原文のまま残っている

言い換え・吸収・削除をしない。チェックは照合。

- [x] 対象座席は **GrokBOT本体**（**NOT Cursor Grok 4.6**）
- [x] WINDOW が Cursor Grok 4.6 を Head にしていない
- [x] COMMON thin が Cursor Grok 4.6 へ Effort max を焼いていない
- [x] **Head ON:** purpose / auth / dispatch / thick instruct / accept-reject / inspect / losscut
- [x] **Instruct THICK**（COMMON 薄層へ厚い本文を移していない）
- [x] **Hands ~0 at window**（exploration / long browser / production / impl / debug / mass screenshot / repetitive clicks → other workers）
- [x] **Important Receive FULL**（required return fields を省略しない。evidence 欠けるとき ACCEPT しない）
- [x] **Control:** order / cancel / status / record / evidence only。dedupe only
- [x] **Effort max を証拠なしに適用済みと書いていない**
- [x] **トークン節約のパーセントを発明していない**

---

## 2. 骨格の穴を回収 Pro で埋めた

- [x] [COMMON-THIN.md](COMMON-THIN.md) のプレースホルダを回収 Pro で置換した
- [x] [WINDOW-CARD.md](WINDOW-CARD.md) のプレースホルダを回収 Pro で置換した
- [x] Pro に無い数字・手順・コマンド・例外を足していない
- [x] 別枝の下書き APPLY を、この回収 Pro の代用にしていない
- [x] required return fields の一覧を、回収文に無いのに発明していない

---

## 3. 焼かない面（本番 APPLY まで）

- [x] 憲法・CLI 共通指示・スキル本体をこの PR で書き換えない
- [x] GrokBOT desired-state をこの PR で書き換えない
- [x] Computer Use を起動しない
- [x] 公開・課金・解約・削除・権限変更をしない
- [x] 秘密・トークン・Cookie・Drive ID・金庫の値を成果物へ書かない

---

## 4. 本番 APPLY 直前（まだやらない）

- [ ] 本人が本番適用を明示した
- [ ] WINDOW の対象座席が **GrokBOT本体** である
- [ ] 焼き先が **Cursor Grok 4.6** になっていない
- [ ] COMMON は薄層、Instruct THICK は WINDOW
- [ ] Hands ~0 at window のまま
- [ ] important の Receive が FULL のまま
- [ ] Effort max を証拠なしに適用済みと書いていない
- [ ] トークン節約パーセントが無い
- [ ] 差分を本人が読める短い一覧にした
- [ ] 本番適用の記録は「適用した／していない」を混ぜない

---

## 5. このチェックリスト自体

- [x] 完成ルール本文の正は COMMON と WINDOW に置き、ここへ複製して肥大化していない
- [x] 未観測の Effort を適用済みにしていない
- [x] トークン節約パーセントを書いていない
