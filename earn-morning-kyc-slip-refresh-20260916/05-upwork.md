# Slip — Upwork

**DRAFT_ONLY.** プロフィールは下書き。Catalog は **Submit しない**。0 Connects。  
**エージェントは signup を完了しない。アップロードしない。Google SSO を再試行しない。**

| | |
|---|---|
| Desk | Upwork（Wave A5 / CU-05） |
| CU hint | `blocked_skip` **Google SSO** |
| Who | **祐太だけ** |
| 入口 | Settings → Identity Verification（ライブメニューを正）。**SSO が通るまで開かない** |
| いつ | 求められたとき。通知のあと目安7日、と公式FAQ。先回り可だが **Submit の口実にしない** |

---

## この机のいま

live: MAIN Google で入ろうとして **Your Google account cannot be accessed at this time**。  
これは本人確認不足ではない。**SSO の門**。エージェント・この環境から **再試行しない。別 Google を作らない。**

[PR#35](https://github.com/rimone0511/autopilot-log/pull/35) の「Upwork next」は古い。  
LinkedIn（A6）も `blocked_skip` **reCAPTCHA**（login）。**next にしない。** 開かない。再試行しない。Services は GO-gated / not enabled。  
**次の CU は TimeTicket（A7, in progress）** → Contra → Craudia → Freelancer。handoff [PR#16](https://github.com/rimone0511/autopilot-log/pull/16) は置いたまま。

人が自分の端末で MAIN Google に入れるようになってから、ID 画面が出たらこのスリップ。SSO のままなら `blocked_skipのまま`。

www / signup の 403（field map [PR#32](https://github.com/rimone0511/autopilot-log/pull/32)）も再GETしない。ウィザードのラベルは画面を正。

---

## 上げるもの（サイトの画面にだけ。SSO が通ったあと）

- 顔付きの **政府発行ID**（免許 / パスポート。プロフィール写真と同一人物）
- 国は **発行国 = プロフィールの国**（Japan でよい。US に偽らない）
- 住所がIDと違うときだけ、画面が求めた公共料金など。求められなければ上げない

学生証は不可、と既存朝チェック。画面が拒んだら別の政府ID。

ヘルプ:  
https://support.upwork.com/hc/en-us/articles/360001176427-How-to-verify-your-identity-as-a-freelancer  
https://support.upwork.com/hc/en-us/articles/34397755511955-Identity-verification-Frequently-asked-questions  
https://support.upwork.com/hc/en-us/articles/360000563227-How-to-verify-your-identity-with-a-government-ID

---

## 上げない / やらない

- [ ] Google SSO（“cannot be accessed at this time”）をエージェントから再試行する
- [ ] 2つ目の Google / 2つ目の Upwork を作って門を迂回する
- [ ] Catalog **Submit** / Boost / キーワード購入
- [ ] **Connects を買う**（任意バッジ 35 Connects も含む）
- [ ] 提案送信、Boosted Proposal、Easy Apply、Auto-bid
- [ ] Agency を作る
- [ ] W-8BEN / 税フォームにマイナンバーや在留カード画像を載せる（今朝はやらない。画面だけ見て閉じる）
- [ ] 出金（銀行 / Payoneer / Wise）を今入れる
- [ ] プロフィールに電話・メール・「contact me」URL を書く
- [ ] 名前を ID に合わせて偽の英語名にする。不一致は朝に記録するだけ
- [ ] 書類を git / チャット / エージェントへ
- [ ] LinkedIn に進む / login reCAPTCHA を再試行する / Services を開く・Save する

Phone SMS / 通話コードは「アカウント作成のコード」と「ID検証の一種」が公式に並ぶ。下書き保存のため人が SMS するのは可。ID / 自撮り / 有料バッジに繋がったら **止める**。

---

## DRAFT_ONLY reminder

SSO skip は Escalate の対象であって、Catalog 公開の許可ではない。  
本人確認は **SSO が通ったあとの朝**。Submit は人が別の朝に決める。

状態: `なし` / `上げた` / `待ち` / `詰まった` / `blocked_skipのまま`
