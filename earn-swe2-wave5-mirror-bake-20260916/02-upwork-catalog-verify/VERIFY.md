> DRAFT_ONLY. No Catalog Submit. No Connects. Prices stay `{{TIER_*_USD}}`.

# Verify notes — Upwork Project Catalog

Mirror-bake: 2026-09-16.

## Length verify (this tree, no live box)

| Artifact | Rule (sibling + Upwork resources) | Measured here |
|---|---|---|
| Overview fence in `overview-en-800.md` | 800 **words** working copy | **800 words** / 4519 characters |
| Catalog summary fence in `CATALOG-PASTE.md` (last long block) | 121–1,200 **characters** | **800 characters** / 135 words |
| Title after “You will get” | max 75 characters; do not type those three words | `a production n8n workflow plus operator docs you can rerun` = **58** |
| Starter / Standard / Advanced package titles | short labels | 39 / 44 / 45 characters |

Counts are `split()` on the fenced bodies. Live UI may count differently (newlines, CJK). Devin re-counts in the box.

## Public GET this bake

| URL | Result |
|---|---|
| https://www.upwork.com/catalog | **403** |
| https://support.upwork.com/hc/en-us/articles/360057397533-Create-a-project | **403** |
| https://support.upwork.com/hc/en-us/articles/360016252373-How-to-build-your-freelancer-profile-the-essentials | **403** |

Help URLs in `CATALOG-PASTE.md` stay as **citations**, not re-proven HTML. Do not replace them with guessed 2026 picker IDs.

## LIVE_DEVIN_NEEDED

1. Open Find Work → Your services → Create Project **without Submit**.
2. Confirm category: try Development & IT → Scripts & Utilities → Scripting & Automation; closer Automation/n8n specialty if listed.
3. Standardized search tags (max 5): `n8n`, `automation`, `API`, `documentation`, `SOP` — nearest official token if missing.
4. Image rules: no client PII, no other-company logos. Skip if the uploader is an ID flow.
5. If a price field is required and `{{TIER_*_USD}}` is still empty locally: park `rate_required`. Do not invent USD.
6. **Do not click Submit / send for review.**

## Still STOP

Government ID, Visual, address, tax, payout, identity badge (35 Connects), Freelancer Plus. [STOP-AT-KYC.md](STOP-AT-KYC.md).
