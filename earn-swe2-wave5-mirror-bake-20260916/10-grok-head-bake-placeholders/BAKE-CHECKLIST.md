# BAKE-CHECKLIST — GROK-HEAD-THIN-HANDS

状態: **BLOCKED until Pro reply**  
対象フォルダ: `ops-grok-head-thin-hands-bake-skeleton-20260916/`  
本番へ焼く前に全部を満たす。一つでも欠ければ APPLY しない。

---

## 0. 停止条件（今はここで止まる）

- [ ] Pro 回答が着いている（GROK-FOUNDATION-COST / MAIN 6 Pro 未回収のまま進めない）
- [ ] このフォルダの `{{PRO_RULE}}` 残数が **0**
- [ ] 残数確認コマンドを実行した: `rg -n '\{\{PRO_RULE\}\}' ops-grok-head-thin-hands-bake-skeleton-20260916/`
- [ ] 本人が「この文面で焼け」と明示している

今の残数は 0 ではない。**未着のまま焼かない。**

---

## 1. ロック4点が原文のまま残っている

言い換え・吸収・削除をしない。チェックは照合であり、新しい文面を足す作業ではない。

- [ ] **Effort max = GrokBOT本体**（**NOT Cursor Grok 4.6**）
- [ ] WINDOW card の Effort max 行が GrokBOT本体を指し、Cursor Grok 4.6 を指していない
- [ ] COMMON thin が Cursor Grok 4.6 へ Effort max を焼いていない
- [ ] **Instruct THICK**（COMMON 薄層へ厚い本文を移していない）
- [ ] **Hands→others ~0**
- [ ] **Receive FULL for important**（ロック句を言い換えていない）

---

## 2. 骨格の穴を Pro 原文で埋めた

- [ ] [COMMON-THIN.md](COMMON-THIN.md) の各 `{{PRO_RULE}}` が Pro 原文に置換されている
- [ ] [WINDOW-CARD.md](WINDOW-CARD.md) の各 `{{PRO_RULE}}` が Pro 原文に置換されている
- [ ] Pro に無い数字・手順・コマンド・例外を足していない
- [ ] 別枝の下書き APPLY を、未着 Pro の代用にしていない

---

## 3. 焼かない面（このチェックが終わるまで）

- [ ] 憲法・CLI 共通指示・スキル本体をこの PR で書き換えない
- [ ] GrokBOT desired-state をこの PR で書き換えない
- [ ] Computer Use を起動しない
- [ ] 公開・課金・解約・削除・権限変更をしない
- [ ] 秘密・トークン・Cookie・Drive ID・金庫の値を成果物へ書かない

---

## 4. APPLY 直前（Pro 着後のみ）

- [ ] WINDOW の対象座席が **GrokBOT本体** である
- [ ] 焼き先が **Cursor Grok 4.6** になっていない
- [ ] COMMON は薄層、Instruct THICK は WINDOW
- [ ] Hands→others が ~0 のまま
- [ ] important の Receive が FULL のまま
- [ ] 差分を本人が読める短い一覧にした
- [ ] 本番適用の記録は「適用した／していない」を混ぜない

---

## 5. このチェックリスト自体

- [ ] ロック4点以外の「完成ルール本文」をこのファイルへ足していない
- [ ] 未観測の Effort を埋めていない
