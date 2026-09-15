# STATUS — Coconala publish-ready checklist

Snapshot: **2026-09-16**  
Folder: `earn-jobs-coconala-publish-ready-checklist-20260916/`  
State: **DRAFT_ONLY**  
Authoring: public GET / sibling PR paths only. **No Coconala login. No 公開する. No 見積もり送信.**

This file is a desk box for **A1 / CU-01**. It does not rewrite QUEUE. It does not claim a live service URL.

Forbidden: secrets, filled yen, KYC files, live `coconala.com/services/<id>`, invented GMV.

---

## Verdict

| Item | Status |
|---|---|
| This checklist pack | **ready · draft** (markdown only) |
| Live fill (fields / images / price / FAQ) | **not run** from this agent |
| Profile | sibling boxes: **`draft_saved`** — not re-verified live here |
| Listing public | **no** (this agent) |
| HUMAN-GO `coconala_publish_listing` | **false** |

---

## CU / JOBS hint (this desk)

| Hint | Meaning here |
|---|---|
| `draft_saved` | Profile (and possibly a listing) parked unpublished — Wave A start |
| `pack_ready` | This 5-file checklist is field-ordered. Operator may fill under CHECKLIST rules |
| `publish_ready_unpublished` | Fields + images + price + FAQ saved as 下書き. **公開する still off** |
| `images_missing` / `rate_empty` | Draft saved or not; GO-blocked |
| `listing_draft_no_save_path` | Form had only 公開する. Left without clicking |
| `already_published` | Live listing public. Agent does not unpublish |
| `blocked_skip` | Login/captcha. Do not retry from this pack |
| `kyc_wait` | 本人確認 / 口座. Morning slip. No upload |

Current row (authoring time):

| # | desk | hint | reason | next action |
|---|---|---|---|---|
| A1 / CU-01 | ココナラ Coconala | `pack_ready` + profile `draft_saved` | Checklist written. No login from this agent | Human: CHECKLIST against PR#87 SERVICE-PASTE. 下書き保存. HUMAN-GO stays false |

---

## Complement (bodies not copied)

| PR | Folder | Relation |
|---|---|---|
| [#87](https://github.com/rimone0511/autopilot-log/pull/87) | `earn-jobs-coconala-first-gig-full-paste-20260916/` | **First-gig paste** (`SERVICE-PASTE.md`). This pack points; does not copy fences |
| [#79](https://github.com/rimone0511/autopilot-log/pull/79) | `earn-jobs-coconala-service-drafts-20260916/` | x3 listings. `01` is same first-gig family as #87 — do not dual-list |
| [#82](https://github.com/rimone0511/autopilot-log/pull/82) | `earn-jobs-pricing-menu-20260916/` | Price tokens / overlay. Not a second first-gig body |
| [#11](https://github.com/rimone0511/autopilot-log/pull/11) | `earn-jp-proposal-drafts-20260916/` | 見積もり。出品 1000 字ではない |
| [#28](https://github.com/rimone0511/autopilot-log/pull/28) | `earn-jp-proposal-wave2-20260916/` | Wave 2 応募文 |
| [#81](https://github.com/rimone0511/autopilot-log/pull/81) | `earn-jobs-coconala-proposal-replies-20260916/` | Inquiry/custom replies. Do not send from this pack |
| [#76](https://github.com/rimone0511/autopilot-log/pull/76) | `earn-jobs-weekly-earn-plan-20260916/` | Week calendar. Day 2 look. Its “listing pack missing” predates #79 / #87 |
| [#43](https://github.com/rimone0511/autopilot-log/pull/43) | `earn-morning-kyc-slip-refresh-20260916/01-coconala.md` | KYC slip. Not listing GO |
| [#1](https://github.com/rimone0511/autopilot-log/pull/1) | `earn-register-expand-20260916/QUEUE.md` | A1 `done-draft` |
| [#54](https://github.com/rimone0511/autopilot-log/pull/54) | `ops/earn/register-wave-a-status-20260916/` | `draft_saved` |
| [#8](https://github.com/rimone0511/autopilot-log/pull/8) | INDEX | `earn-packs/coconala/` still `unknown` |

---

## Public GET (this authoring session)

`thin_site_skip: false` for coconala.com / mag (help.zendesk 403 from this egress).

| URL | HTTP | Note |
|---|---|---|
| https://coconala.com/pages/guide_sell | 200 | 通常サービス steps. キャッチ 30 字. 価格 500円〜 ※カテゴリ. 画像ステップ. 公開. 手数料 22% cited unused in paste |
| https://coconala.com/pages/guide_rule | 200 | 同一サービス複数出品禁止、外部決済禁止 |
| https://coconala.com/news/170 | 200 | タイトル 25 字・ます / キャッチ 30 字 |
| https://coconala.com/news/1220 | 200 | 通常 1000 字 |
| https://coconala.com/news/1372 | 200 | 2026-09-01 案内（#87 引用。画像1枚以上は公開時。ライブを正） |
| https://coconala.com/categories/ | 200 | Live tree wins |
| https://coconala.com/services/add | 202 | Challenge without session. Logged-in form wins |
| https://mag.coconala.com/articles/knowhow-the-basics-of-service-pages | 200 | FAQ + 画像は必ず設定 |
| https://mag.coconala.com/articles/knowhow-list-to-improve-service-pages | 200 | できること／できないこと |
| https://mag.coconala.com/articles/knowhow-rules-about-selling | 200 | 景品表示法 |
| https://help.coconala.com/hc/ja/articles/360020963554 | 403 | Category minimum. Cite; re-read at paste |
| https://help.coconala.com/hc/ja/articles/9517249749017 | 403 | 出品禁止一覧 |
| https://help.coconala.com/hc/ja/articles/218832717 | 403 | 本人確認. Do not open this pack |

**POST / login: none.**

---

## After live operator pass (leave blank until a run)

```
desk: Coconala
pack: earn-jobs-coconala-publish-ready-checklist-20260916/
profile:
listing:
listing_id_in_git: none
first_gig_source:
fields:
images:
price:
faq:
save:
publish_clicked: no
estimate_sent: no
kyc_opened: no
human_go_coconala_publish_listing: false
next: stop
```

Outcome so far: **not run**.

---

## Next (human)

1. Keep this PR **draft**. Do not merge until Yuta reviews.
2. Open PR#87 `SERVICE-PASTE.md` + `DRAFT_ONLY.md`. Do not also create #79 `01` as a second listing.
3. Run [CHECKLIST.md](CHECKLIST.md). **下書きで保存する.**
4. Leave [HUMAN-GO.md](HUMAN-GO.md) all `false` unless 祐太 decides a later morning.
5. Do not send estimates. Do not announce.

---

## This PR / pack will not

- Copy first-gig fences into this folder or `earn-packs/coconala/`
- Log in to Coconala from the authoring agent
- Click 公開する / 見積もり送信
- Upload ID / bank / images
- Invent yen rates or freeze fee %
- Flip HUMAN-GO rows to `true`
- Change Python posting-gate tests
