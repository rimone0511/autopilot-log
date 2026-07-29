# Autopilot Log

Unattended, auditable uploading to YouTube and TikTok from a script — no browser, no UI
automation, no scraping. It talks only to the **YouTube Data API v3** and TikTok's
**Content Posting API**.

It exists because a one-person studio cannot open a browser ten times a day, and because
almost every "how to automate YouTube" article on the web is quietly out of date.

> ### YouTube and TikTok are not the same story here — please read this before judging the name
>
> **YouTube** is the unattended part: you authorise your own channel once with your own
> Google credentials, and after that the command runs on a timer without you.
>
> **TikTok is not unattended.** By default this CLI only performs an **inbox upload**: the
> video lands in your TikTok inbox and *you* review it and press post inside the TikTok
> app. Direct posting exists as a separate subcommand, it is off unless a posting-gate file
> explicitly allows it, and it only works if **you** hold your own TikTok client
> credentials that **you** have had audited. This repository is a self-hosted tool, so
> every copy is its own API client running under its operator's own key.
>
> If you are looking for the hosted product — a web app where a person chooses the privacy
> level and every other setting and presses Post themselves — that is
> **[Autopilot Log Studio](https://yutalab.dev/autopilot-log/studio/)**, and it is a
> different, separately reviewed API client from this CLI.
>
> The name is just a name. Nothing in this repository operates TikTok through a browser,
> and nothing posts to TikTok on a schedule.

```bash
python -m autopilot_log.youtube upload \
  --shelf main --file today.mp4 --title "Today's short" --privacy private

python -m autopilot_log.tiktok upload \
  --shelf main --file today.mp4
# lands in your TikTok inbox; you review and post it yourself in the TikTok app
```

---

## What it does

| | |
|---|---|
| Uploads a video file | resumable upload, so a large file survives a flaky connection |
| Handles OAuth | one browser click per channel, once, ever — then it runs unattended |
| Holds many channels | each channel gets a nickname (`--shelf main`, `--shelf en`, …) |
| Keeps secrets out of the repo | pluggable keystore, nothing is ever printed or logged |
| Refuses to publish by accident | a posting gate file must explicitly allow public uploads |

## What it deliberately does **not** do

- No browser automation and no scraping of any platform. If a platform has no API for
  something, this tool does not do that something.
- No engagement automation — it does not like, follow, comment, or view.
- No uploading of content you do not own the rights to. That is on you.
- TikTok posting uses the official Content Posting API only. Browser automation remains
  out of scope. An unaudited client is restricted to `SELF_ONLY`, posting accounts must
  be private, and no more than five users may post through that client in a 24-hour
  period. TikTok's [getting-started guide][tiktok-start] and [content-sharing
  guidelines][tiktok-guidelines] describe these limits.

---

## Four things Google's documentation says that surprise most people

These are the reason this tool exists in this shape. All four are from Google's own pages.

1. **Uploads through an unaudited Cloud project are locked to private, forever.**
   Every video uploaded via `videos.insert` from an API project created after 28 July 2020
   is restricted to private viewing, and that lock cannot be lifted by hand or appealed.
   The fix is the free [YouTube API compliance audit][audit].
   **A successful upload is not a published video.** This tool prints a loud warning when
   YouTube overrides the privacy you asked for.
2. **An OAuth app left in "Testing" hands out refresh tokens that expire in 7 days.**
   Unattended posting will die every single week until the app is published to production.
   ([OAuth 2.0 docs][oauth])
3. **Service accounts cannot upload to YouTube.** They have no channel, so the API answers
   `NoLinkedYouTubeAccount`. There is no fully human-free path: each channel needs exactly
   **one** consent click, once. ([Authentication docs][auth])
4. **`videos.insert` costs 1 of 100 uploads per day**, on a budget separate from the
   10,000-unit daily quota. The widely copied "1,600 units per upload, so 6 videos a day"
   figure is out of date. ([Quota costs][quota])

[audit]: https://developers.google.com/youtube/v3/guides/quota_and_compliance_audits
[oauth]: https://developers.google.com/identity/protocols/oauth2
[auth]: https://developers.google.com/youtube/v3/guides/authentication
[quota]: https://developers.google.com/youtube/v3/determine_quota_cost

---

## Three things TikTok's documentation says that surprise most people

These constraints are why the TikTok module has separate inbox and direct-post commands.

1. **An unaudited client can direct-post only to `SELF_ONLY`.**
   The restriction is removed through TikTok's audit process; until then, posting
   accounts must also be private and the client is limited to five users in 24 hours.
   ([Content Posting API getting started][tiktok-start])
2. **A refresh token rotates whenever it is used.**
   The old value can stop working, so this tool saves the newly returned refresh token
   before using the accompanying access token. ([OAuth token management][tiktok-token])
3. **An unspecified posting mode means `MEDIA_UPLOAD`, not a direct post.**
   That sends media to the creator's inbox for a final action. This tool always sends an
   explicit `post_mode`: `MEDIA_UPLOAD` for `upload`, or `DIRECT_POST` for `publish`.
   ([Content Posting API reference][tiktok-start])

[tiktok-start]: https://developers.tiktok.com/doc/content-posting-api-get-started
[tiktok-guidelines]: https://developers.tiktok.com/doc/content-sharing-guidelines
[tiktok-token]: https://developers.tiktok.com/doc/oauth-user-access-token-management

---

## Install

Python 3.9+ and one dependency.

```bash
git clone https://github.com/rimone0511/autopilot-log.git
cd autopilot-log
pip install requests
```

## Get a key

1. Create a project in the [Google Cloud console](https://console.cloud.google.com/).
2. Enable **YouTube Data API v3**.
3. Configure the OAuth consent screen (external user type).
4. Create an **OAuth client ID** of type **Desktop app**. Copy the client secret — Google
   shows it once. If you lose it, add a new secret from the client's detail page.
5. **Publish the app to production.** Skipping this is failure mode #2 above.

Store the client:

```bash
python -m autopilot_log.youtube set-client --client-id XXX --client-secret YYY
python -m autopilot_log.youtube where     # confirms where it landed; prints no secret
```

## Connect a channel (one click, once)

```bash
python -m autopilot_log.youtube auth --shelf main
```

It prints a consent URL and waits on `http://localhost:8765/`. Open the URL in a browser
signed in to the channel you want, press **Allow**, and the refresh token is saved. If the
machine has no browser, use `auth-url` on that machine and `exchange --code ...` afterwards.

```bash
python -m autopilot_log.youtube whoami --shelf main
```

## Upload

```bash
# safe by default: private
python -m autopilot_log.youtube upload --shelf main --file clip.mp4 --title "Test"

# see the request without sending it
python -m autopilot_log.youtube upload --shelf main --file clip.mp4 --title "Test" --dry-run

# scheduled publish (requires the gate to be open)
python -m autopilot_log.youtube upload --shelf main --file clip.mp4 \
  --title "Tomorrow" --publish-at 2026-07-26T09:00:00Z
```

---

## The posting gate

Anything other than `--privacy private` is refused unless a gate file says otherwise.
Default location: `./posting-gate.json`, override with `AUTOPILOT_LOG_GATE`.

```json
{ "channels": { "youtube": { "allowed": false } } }
```

It **fails closed**: a missing, unreadable, or malformed gate means private-only. The point
is that "the automation is running" and "the automation may publish" are two separate
switches, and the second one is a deliberate human act.

The gate is covered by tests, because it is the only thing standing between "the automation
is running" and "something went public that should not have":

```bash
python tests/test_gate.py
```

## Bring your own keystore

Set `AUTOPILOT_LOG_KEYSTORE`:

| value | where secrets live |
|---|---|
| `file` (default) | `~/.autopilot-log/keys.json`, owner-only permissions. Override with `AUTOPILOT_LOG_KEYFILE`. |
| `env` | read-only, from `AUTOPILOT_LOG_<SERVICE>_<FIELD>` variables — for CI and container secrets |
| `dpapi` | Windows: shells out to a PowerShell script pointed at by `AUTOPILOT_LOG_DPAPI_SHELF`, so keys sit in a DPAPI-encrypted store rather than a JSON file. The script must accept `-Get <name> [-Field <f>]` and `-Set <name> -FromFile <path> -RemoveSource -Note <text>`, where the file holds `KEY=VALUE` lines. Values are passed by file, never as arguments, so they never appear in a command line or a process listing. |

No backend ever prints a secret. `where` shows the location; `keystore.redact()` shows only
the last four characters of a value.

---

## Data this tool touches

- **Your Google OAuth refresh token and channel id**, stored by your chosen keystore on your
  own machine. They are sent only to `oauth2.googleapis.com` and `googleapis.com`.
- **The video file and metadata you name on the command line.**

Nothing is sent anywhere else. There is no telemetry, no analytics, and no server operated
by this project. Revoke access any time at
[myaccount.google.com/permissions](https://myaccount.google.com/permissions).

Use of the YouTube API is subject to the [YouTube Terms of Service](https://www.youtube.com/t/terms),
the [YouTube API Services Terms of Service](https://developers.google.com/youtube/terms/api-services-terms-of-service),
and the [Google Privacy Policy](https://policies.google.com/privacy).

---

## 日本語(かんたんな説明)

**これは何?** — 動画を「ブラウザを開かずに」YouTubeやTikTokへ上げるための小さな道具です。
毎日ショート動画を出したいけれど、人が10回もアップロード画面を開くのは無理、という
ところから生まれました。

**たとえ話**: YouTubeの投稿画面が「窓口に並んで手渡しする」だとすると、この道具は
「**専用の宅配便の伝票を書いて出す**」やり方です。窓口に並ばなくていい代わりに、
最初に一度だけ「この宅配業者を使っていいですよ」と許可のハンコ(=許可ボタン)を押します。
ハンコはチャンネル1つにつき生涯1回だけ。あとは全部機械がやります。

**気をつける点が4つ**(全部Googleの公式ドキュメントに書いてあります):

1. **審査に通るまで、上げた動画は全部「非公開」で固定されます。** 手で公開に戻すことも、
   異議を出すこともできません。無料の審査に通すのが唯一の解除方法です。
   → だから「アップロード成功」と「公開できた」は別物です。この道具は、YouTube側に
   privacy を書き換えられたとき大きな警告を出します。
2. **アプリを「テスト中」のままにすると、機械が使う合鍵が7日で失効します。** 毎週止まります。
   必ず「本番公開」に切り替えてください。
3. **完全に人の手をゼロにはできません。** サービスアカウント(人が触らない鍵)はYouTubeでは
   使えないので、チャンネルごとに1回だけ許可のクリックが要ります。
4. **1日100本まで上げられます。** ネットに多い「1日6本まで」は古い情報です。

**安全のしくみ**: 既定は必ず「非公開」で上げます。公開したいときは `posting-gate.json` という
別のファイルで明示的に許可する必要があり、そのファイルが無い・壊れている場合は自動的に
「非公開のみ」に倒れます(=事故で公開されない側に倒れる作り)。
鍵は画面にもログにも一切出しません。

**やらないこと**: ブラウザの自動操作・スクレイピング・いいね/フォローの自動化。
TikTokは公式Content Posting APIだけを使い、未審査クライアントの制限を回避しません。

---

## License

MIT — see [LICENSE](LICENSE).

This project is not affiliated with, endorsed by, or sponsored by Google or YouTube.
YouTube is a trademark of Google LLC.
