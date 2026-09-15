# TITLE-FIX — do not save doubled ます

Listing: Coconala **4403529** (unpublished)  
Canonical title (ますあり, 15):

```
n8n自動化と手順書を作ります
```

Coconala news 170: 提供内容は最大 25 字、語尾は「ます」固定.  
Cite: https://coconala.com/news/170  
[#87](https://github.com/rimone0511/autopilot-log/pull/87) §1.1: if the form **auto-appends** ます, paste **without** ます.

---

## What can go wrong

The title **field** may already hold `n8n自動化と手順書を作ります` while the **preview / heading** adds another ます:

| Where | String | Count |
|---|---|---|
| Wanted display | `n8n自動化と手順書を作ります` | 15 |
| Bad display | `n8n自動化と手順書を作りますます` | 17 |

Do not save the bad string. Do not “fix” by adding a third ます.

---

## If you reopen the title field

Live counter wins. One of:

1. **Form does not auto-append ます** — keep / paste:

   ```
   n8n自動化と手順書を作ります
   ```

2. **Form auto-appends ます** (preview already ends in ます while the box does not) — paste **ますなし** (13):

   ```
   n8n自動化と手順書を作り
   ```

   Displayed result should be `n8n自動化と手順書を作ります`.

3. **Box already contains `…作りますます`** — delete the extra ます until the **displayed** title is exactly `n8n自動化と手順書を作ります`. Then **下書きで保存する**. Not 公開する.

Do not keyword-stuff (`n8n AI エージェント 公式パートナー` など). Do not create a second listing to “fix the title.”

---

## After a title edit

- [ ] Displayed title = `n8n自動化と手順書を作ります` (one ます)
- [ ] Counter ≤ 25
- [ ] Still unpublished
- [ ] Cover still required before GO ([OPERATOR-NEXT.md](OPERATOR-NEXT.md))
