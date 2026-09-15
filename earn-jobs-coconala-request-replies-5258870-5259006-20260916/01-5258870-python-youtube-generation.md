> **DRAFT_ONLY. DO NOT SEND.**  
> 実在の鍵・円・勝率禁止。金額は `{{PRICE_YEN}}`。エージェントは応募しない。

# CN-REQ-5258870 — ココナラ募集：Python YouTube 生成（stretch）

## Fact table (operator; do not paste)

| key | value |
|---|---|
| pack | earn-jobs-coconala-request-replies-5258870-5259006-20260916 |
| id | CN-REQ-5258870 |
| desk | ココナラ募集（単発） |
| url | https://coconala.com/requests/5258870 |
| status_this_fetch | **OPEN** — recheck [STATUS.md](STATUS.md) |
| apply_deadline_on_page | 2026-09-22 |
| delivery_hope_on_page | 2026-10-04（希望。完了予定日にコピーしない） |
| pay_on_page | 見積り希望 / `pay_not_on_page` |
| fit | **stretch** |
| send | **禁止** |
| chars_preview | 88 |
| chars_short | 694 |
| chars_standard | 988 |

募集の核（公開文）: 台本または音声 → Whisper（タイムスタンプ）→ Claude API（claude-3-7-sonnet、テロップ整形）→ ローカル VOICEVOX API `localhost:5021` → FFmpeg で背景＋音声＋字幕の mp4（1080×1920 または 1920×1080）。納品は Python 一式（または Claude Code 用リポジトリ）、`.bat` 等の起動、Python / FFmpeg / VOICEVOX の手順書。

公開している Autopilot Log は **公式 API での投稿**（非公開デフォルト、門番）。**動画生成パイプラインそのものではない。** 隣接（Python・手順・公式呼び出し）だが stretch。n8n は起動と失敗通知に使える。テロップ描画と音声合成の本体にはならない。

---

## 画面の別欄（ココナラ募集・応募）

| 欄 | 貼る値 |
|---|---|
| 提案内容 | 下の標準文（短い募集なら短文） |
| 提案額 | `{{PRICE_YEN}}`（空なら応募しない） |
| 完了予定日 | `{{LEAD_TIME_DRAFT}}`（納品希望日をそのまま打たない） |

他応募者の円がページに見えてもコピーしない。見積り希望なので、円は本人台帳だけ。この PR は打たない。

---

## 送信ゲート

- [ ] https://coconala.com/requests/5258870 がまだ OPEN
- [ ] `{{ONE_SPECIFIC_DETAIL}}` がこの募集（Whisper 時刻・VOICEVOX `:5021`・縦横 mp4・`.bat` / 手順書）から取れている
- [ ] n8n だけで「完成動画工場」と書いていない
- [ ] Autopilot Log を動画生成成果物だと書いていない
- [ ] 提案額は `{{PRICE_YEN}}`。本文に円なし
- [ ] 応募するは自分が押す — **この PR からは押さない**

---

## 正直な範囲（オペレータ用。フェンスには短く入れる）

**できる（条件付き）**

- 依頼者 PC 上の Python パッケージ。入力（テキスト台本 / 音声ファイル）→ 公開ドキュメントどおり Whisper / Claude / VOICEVOX HTTP / FFmpeg を呼ぶスクリプト
- Whisper は募集どおり API **または** ローカル。GPU が無い PC でのローカル速度は保証しない。選ばせる
- Claude は依頼者キー。モデル名は募集の claude-3-7-sonnet を初期値にし、キー側で使えるか先に確認
- VOICEVOX は依頼者が既に `localhost:5021` で立てる前提。こちらはクライアントと手順。ホスティングしない
- FFmpeg は依頼者が入れたバイナリ。背景は依頼者指定の画像/動画。権利のない素材は扱わない
- 最初の1本は解像度どちらか一方。もう一方は同じ経路の確認あと
- `.bat`（または同等の起動）と、Python / FFmpeg / VOICEVOX の手順書
- 任意: フォルダ監視や失敗通知を n8n 公式コネクタで足す（**生成の代わりではない**）
- 投稿（YouTube Data API）はこの募集文に無い。必要なら **別見積・公式 API のみ・門番は人**

**できない / 約束しない**

- どの Windows でもワンクリックで同じ画質、という未確認保証
- 字幕の精度％、再生数、時短分数
- ブラウザで YouTube Studio を操作する投稿
- n8n だけで Whisper 時刻付き字幕と VOICEVOX 波形を合成すること
- こちらが VOICEVOX / GPU / Claude キーを預かること
- 希望日 2026-10-04 までの全入力×両解像度×初心者ゼロ失敗を、未計測のまま確約すること → 先に1本の経路

---

## 一覧・通知で先に見える一文（ここを先に直す）

```
募集 5258870 を拝見しました。{{ONE_SPECIFIC_DETAIL}} を、依頼者マシンの Python 1本として切り、n8n は起動と失敗通知までにします。
```

---

## 短文

```
https://coconala.com/requests/5258870 を拝見しました。{{ONE_SPECIFIC_DETAIL}}

{{DISPLAY_NAME}}です。公開メモ: {{PORTFOLIO_URL}}。公開の Python 例は投稿用 CLI（公式 API・壊れたら非公開側へ倒す門番）{{GITHUB_REPO_AUTOPILOT}} で、Whisper／VOICEVOX／FFmpeg の完成品工場ではありません。隣接する仕事として、募集の流れ（台本または音声 → 時刻付き文字起こし → Claude でテロップ整形 → 依頼者の VOICEVOX localhost:5021 → FFmpeg で mp4）を、依頼者 PC 上のスクリプトと .bat と手順書に落とす案です。

n8n でできること: フォルダや手動トリガからそのスクリプトを起動し、失敗を人へ戻すこと。n8n だけでは字幕同期の mp4 は出せません。ブラウザで YouTube を操作する投稿、コメント自動化、鍵の預かりはお受けできません。字幕の精度や再生数は保証しません。

最初の納品は、指定の入力1系統と解像度1つで「同じ手順でもう1本出せる」ところまでです。縦と横の両方、音声入力とテキスト入力の全部を同日に約束はしません。投稿 API が必要なら別見積です（公式のみ）。

確認: {{QUESTION_1}}
料金 {{PRICE_YEN}}、完了予定日 {{LEAD_TIME_DRAFT}} は応募欄へ。未記入のまま送りません。この文は下書きです。送信しません。
```

---

## 標準文

```
https://coconala.com/requests/5258870 を拝見しました。{{ONE_SPECIFIC_DETAIL}}。{{SCOPE_ONE_LINER}}

{{DISPLAY_NAME}}（{{PORTFOLIO_URL}}）です。公開の Autopilot Log（{{GITHUB_REPO_AUTOPILOT}}）は公式 API の投稿と、公開スイッチを人に残す門番です。募集は mp4 生成までで、投稿はその文にありません。生成側は stretch です。既製の Whisper＋VOICEVOX 工場を持っている、とは書きません。募集の流れに沿い、依頼者 PC で動く Python を書く提案です。

【切る範囲】台本または音声の一方を先に通す。Whisper は API かローカル（GPU 無しの遅さは未保証）。Claude は依頼者キー、初期値は募集の claude-3-7-sonnet（使えなければ確認して落とす）。VOICEVOX は依頼者の localhost:5021。FFmpeg で指定背景＋WAV＋時刻字幕。mp4 は 1080×1920 か 1920×1080 の片方から。納品はソース、.bat 等、手順書。鍵の値は書かない。

【n8n / 手順書】足りる: 起動、失敗時の再実行、任意で n8n から同じ CLI を叩くこと。足りない: n8n だけで字幕同期 mp4 を出すこと。手順書だけで GPU や FFmpeg が揃うこと。

【しないこと】ブラウザ操作、スクレイピング、コメントや再生の自動化、権利のない素材、鍵の預かり、精度％・時短・再生数の保証、サイト外連絡・支払い。投稿が必要なら公式 Data API の別見積だけです。全入力×両解像度を未計測の希望日で確約しません。

確認: {{QUESTION_1}} / {{QUESTION_2}} / Whisper は API かローカルか / VOICEVOX は既に 5021 か / 先に通す解像度は縦か横か。

料金 {{PRICE_YEN}}、完了予定日 {{LEAD_TIME_DRAFT}} は応募の別欄です。手数料は {{PLATFORM_FEE_NOTE}}。連絡はココナラ内だけです。この文は下書きです。送信しません。
```

---

## この募集向けの記入（公開ページから。送信は別）

- `{{ONE_SPECIFIC_DETAIL}}` 例: `VOICEVOX を localhost:5021 で鳴らし、Whisper の時刻で FFmpeg 字幕を乗せ、縦 1080×1920 か横 1920×1080 の mp4 と .bat と手順書が欲しい`
- `{{SCOPE_ONE_LINER}}` 例: `生成は依頼者 PC の Python 1経路。n8n は起動と失敗通知まで。投稿 API はこの募集には含めない、という理解です。`
- `{{QUESTION_1}}` 例: `最初に通す入力は台本テキストですか、音声ファイルですか。`
- `{{QUESTION_2}}` 例: `VOICEVOX は既に 5021 で起動できますか。こちらでサーバを預かりはしません。`

募集者の表示名や、他応募者の本文・円は git に残さない。

---

## STOP

- 応募するボタンは押さない
- 閉じていたら CLOSED にして止める。文を他 ID へ使わない
- Autopilot Log＝動画自動生成、と書かない
- n8n＝FFmpeg の代替、と書かない
- 本文に円を書かない。`{{PRICE_YEN}}` は欄だけ
