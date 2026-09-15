# CTA — LinkedIn Service Page (JOBS DRAFT)

Desk: LinkedIn **Services** on the existing recovered **personal** profile  
Mode: **`DRAFT_ONLY`** — set pricing/toggles; **do not Save** if Save publishes ([STOP-AT-SAVE.md](STOP-AT-SAVE.md))

This file is the Service Page **call to action**: how buyers see price and how they reach you. It is not a feed post, not InMail, and not a Company Page button.

## 1. Pricing CTA (required stance)

Official personal help ([a569554](https://www.linkedin.com/help/linkedin/answer/a569554)): starting hourly is a **minimum shown to buyers, not a guarantee**. You may choose **Contact for pricing**.

| Field | This pack |
|---|---|
| Starting hourly rate | **Do not fill** unless `{{STARTING_HOURLY_USD}}` was supplied **locally** by the operator for this session |
| **Contact for pricing** | **Select this** |

`{{STARTING_HOURLY_USD}}` is empty in git. Do not invent USD/JPY/EUR.

If the form **requires** a number and Contact-for-pricing is missing: park `rate_required`. Do not type a guessed amount. Do not Save to dismiss the wall.

About prose already names Contact for pricing ([ABOUT.md](ABOUT.md)). Keep the form control and the About sentence consistent.

## 2. Request services / Showcase (Premium — leave off)

Official help: with Premium Business, Sales Navigator, or Recruiter Lite, the profile can show Services Showcase and a **Request services** button. Without that subscription, members see a **preview of the services description** only ([a569554](https://www.linkedin.com/help/linkedin/answer/a569554)).

| Control | This pack |
|---|---|
| Buy Premium / start trial to unlock Request services | **No** |
| Media (documents, photos, videos, websites) on the Service Page | **Skip** (Premium-only) |
| Request services button | Not this pack’s CTA. Do not pay to turn it on |

## 3. Company Page custom CTA (not this desk)

Company Pages can set **Request Services** as the Page custom call-to-action ([a7433052](https://www.linkedin.com/help/linkedin/answer/a7433052)). Freelancer = **personal** profile. Do not choose Company Page / ユタラボ Page. That choice is **not currently reversible**.

## 4. Message / consult toggles (confirm live labels)

| Control | Draft stance |
|---|---|
| Allow messages from people outside your network (if shown **inside** the Services editor) | May leave **on** only if it does **not** require Save-to-publish. If it is bundled with Save = viewable, **do not Save**. |
| Provide free consultation / Request services button | **Off** unless the operator later GO’s inbound lead forms. Do not advertise a free consult you have not staffed. |
| Custom CTA on a Company Page | N/A |

## 5. What buyers should do (no off-platform CTA)

Allowed implied CTA: **message on LinkedIn** and **Contact for pricing**.

Do not paste:

- email, phone, WhatsApp, Telegram, Slack, Discord
- calendar links
- “DM me @…” on another network
- a public guaranteed hourly

Inbound Services **proposal replies** are sibling PR [#38](https://github.com/rimone0511/autopilot-log/pull/38) and still **do not send** from that pack.
