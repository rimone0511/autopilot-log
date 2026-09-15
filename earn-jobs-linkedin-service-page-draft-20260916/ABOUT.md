# About — LinkedIn Service Page (JOBS DRAFT)

Desk: LinkedIn **Services** on the existing recovered **personal** profile  
Mode: **`DRAFT_ONLY`** — paste then **do not Save** if Save publishes ([STOP-AT-SAVE.md](STOP-AT-SAVE.md))

Official help: About is **optional**; fill it ([a569554](https://www.linkedin.com/help/linkedin/answer/a569554)). **Live character limit wins.** Third-party writeups often cite ~500 characters. This fence is **362 characters** so it should fit. If the box is shorter, cut from the pricing sentence first, then the location sentence.

Aligned with sibling Wave A6 paste (PR [#16](https://github.com/rimone0511/autopilot-log/pull/16)). Replace `{{CITY}}` / `{{COUNTRY}}` locally. Recount after fill.

## Paste (About)

```
I build n8n workflows and the operator docs a non-engineer can rerun. Official APIs, webhooks, and first-party connectors only. No scraping, no likes or follows, no publishing to your social accounts. English, async, remote from {{CITY}}, {{COUNTRY}}. Work stays on LinkedIn until a contract exists. Pricing: Contact for pricing — not a public guaranteed hourly.
```

| Check | This commit |
|---|---|
| Characters in fence | 362 |
| Email / phone / WhatsApp | none |
| Live USD/JPY | none — Contact for pricing named in prose |
| Employment / Expert / client-count claims | none |

Do not put `{{GOOGLE_ACCOUNT_EMAIL}}`, `{{PHONE_E164}}`, WhatsApp, Telegram, or “email me at.” Inbound LinkedIn messages are enough.

Do not claim xAI / Grok employment, n8n Expert, or invented years / client counts.

## Location (same editor, not About prose)

| UI field | Value |
|---|---|
| Work location | `{{CITY}}`, `{{COUNTRY}}` (honest Japan location) |
| Open to remote work | **On** |
| Service area / radius | confirm live; do not claim “United States only” |

Do not spoof a US city to chase US buyers.

## Optional headline (not a feed post)

If the Services flow also offers a profile headline edit, paste **only if** it does not auto-share:

```
n8n automation with operator docs
```

33 characters. Do **not** click Share to feed, Notify network, or Create a post about services.
