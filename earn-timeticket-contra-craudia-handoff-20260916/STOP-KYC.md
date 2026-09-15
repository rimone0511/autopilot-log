# STOP before KYC — morning user only

Pack date: 2026-09-16  
Mode: **DRAFT_ONLY**. Agents and CU **do not upload**.  
Audience: 朝の本人（祐太）。1机ずつ。3つやったら休憩。

Sibling 1枚: `earn-kyc-morning-checklist-20260916/`（Wave A 全体）。このファイルは **CU-07 / CU-08 / CU-09 だけ** のパスメモ。

## 5つの止め（全部の机）

1. ファイル選択ダイアログを開かない。カメラ権限を KYC に渡さない。
2. マイナンバー **番号面 / 裏面**、保険証の番号、口座番号を撮らない・貼らない。
3. git / チャット / セッションログに書類写真・顔・OTP・電話の実値を残さない。
4. 有料の本人確認ブースター（Contra Pro で Discover を買う、等）を KYC の代わりにしない。
5. 画面がパックと違う → **画面を正とする**。推測で別書類を足さない。

## 朝メモの型（秘密なし）

```
date:
desk:
screen:
saved_draft: yes/no/unknown
kyc_shown: yes/no
upload: none
next: morning-user | park | next-desk
```

## CU-07 TimeTicket

| | |
|---|---|
| 入口 | [identifications/edit](https://www.timeticket.jp/users/identifications/edit) |
| 公式 | [本人確認資料の提出](https://help.timeticket.jp/articles/19398) |
| いつ | 公開説明では **販売の前** に確認完了が要ることがある。下書き保存まで ID 必須なら **チケットは作らない** |
| 出すもの（本人だけ） | 免許 **表面**（国際免許不可）/ 日本国パスポート顔写真ページ / マイナ **表面**（裏面の個人番号は出さない）/ 住民票はマイナ記載なし・本籍等は隠す |
| エージェント | アップロードしない。発行完了も押さない |
| 朝メモに書いてよいこと | `desk: TimeTicket` / `screen: identifications/edit` / チケット下書きの有無 |

番号面禁止。チケットは下書きのまま。

## CU-08 Contra

| | |
|---|---|
| 入口 | Wallet → **Add account** / Verify Your Identity |
| 公式 | [How to Verify Your Identity](https://help.contra.com/en/articles/9322955-how-to-verify-your-identity-on-contra) |
| いつ | **出金ウォレット作成時**。Independent ページの下書きには不要。Discover 完成チェックの最後が wallet ならそこで止める |
| 出すもの（本人だけ） | Persona。政府ID。国は **発行国**（今住んでいる国ではない） |
| 同時に出やすいもの | Stripe 条項、税番号、銀行 / Airwallex。口座は後回し可 — 今は全部閉じる |
| エージェント | Persona にリダイレクトされたら戻る。Pro を買わない |
| 朝メモ | `desk: Contra` / `screen: Wallet Add account / Persona` |

## CU-09 クラウディア

| | |
|---|---|
| 入口 | ログイン後 **マイページ設定 → 本人確認** |
| 公式 | [提出方法](https://www.craudia.com/app/faq/contents/93) / [登録に必要なもの](https://www.craudia.com/app/faq/contents/103) |
| いつ | **バッジ・出金・一部取引**。登録完了には不要（メールがあれば足りる） |
| 出すもの（本人だけ） | 日本の顔付き公的書類いずれか **+ 自撮り必須**。目安 3営業日 |
| エージェント | 画面の種類をメモして閉じる。自撮りを代行しない |
| 朝メモ | `desk: Craudia` / `screen: マイページ設定 → 本人確認` / `selfie: required-when-user-does-it` |

海外在住の追加証明は今の想定外。出たら止める。

## やってよいこと（KYC ではない）

- MAIN Google ログイン
- 親 Gmail のメール OTP（コードを git に書かない）
- プロフィール下書き、Contra Independent **Free**、TimeTicket の **メッセージ** チケット下書き保存（できるとき）
- SMS が「下書き保存」までを止めるとき: ユーザーチャットで待つ。ID 付きなら KYC 扱い

## やらないこと

- 朝の本人以外が書類を上げる
- 3机の KYC を先回りで全部開く
- 本人確認済みバッジのために今すぐ出す
