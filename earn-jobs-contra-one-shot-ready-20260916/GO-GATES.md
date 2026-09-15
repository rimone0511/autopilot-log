> **STOP. Gate is closed.**  
> Missing, unread, or half-filled = do not Apply, do not Submit, do not send a proposal.  
> This file is **not** a SEND GO. **GO is false.**

# GO-GATES — Contra JOBS one-shot ready (style 01)

Mirror of the Autopilot Log posting gate: **fail closed**.  
“Paste is ready in git” is not “Contra may receive an application.”

This file is the switch. [OPERATOR-CARD.md](OPERATOR-CARD.md) is the one-shot serial. [PR#86](https://github.com/rimone0511/autopilot-log/pull/86) is the LOOK / PREP playbook. None of those is a GO until 祐太 writes a **dated SEND GO outside this folder** **and** clicks the live control.

Default (commit this way):

```
contra_one_shot_ready_gate:
  pack: earn-jobs-contra-one-shot-ready-20260916
  phase: JOBS
  draft_only: true
  style: 01-n8n-inbound-path
  existing_draft_saved_independent_only: true
  contra_apply_opportunity: false
  contra_submit_application: false
  contra_send_paid_project_proposal: false
  contra_send_inquiry_reply: false
  contra_publish_feed: false
  contra_discoverable_on: false
  contra_buy_pro: false
  contra_buy_max: false
  contra_refer_earn: false
  contra_labs_or_expert: false
  contra_job_network_video: false
  contra_persona_wallet: false
  contra_change_location: false
  contra_second_account: false
  auto_apply: false
  send_go: false
  apply: no
```

If this file is deleted, treat every row as `false`. Do not infer permission from a merged PR, from “#71 is paste-ready”, from “#86 LOOK passed”, or from JOBS week Rank 2.

Sibling gates (do not copy, still closed):

- [#71](https://github.com/rimone0511/autopilot-log/pull/71) — send **forbidden** on all five styles
- [#86](https://github.com/rimone0511/autopilot-log/pull/86) `GO-GATES.md` — SEND default **FALSE**
- [#64](https://github.com/rimone0511/autopilot-log/pull/64) — live box **`apply: no`**
- [#88](https://github.com/rimone0511/autopilot-log/pull/88) — `contra_apply_opportunity: false`

This pack does not flip those files.

---

## What “GO” means here

| Gate set | Unlocks | This pack |
|---|---|---|
| **LOOK** | May sign in the existing Independent and **browse** the Job feed | Not granted here. Use [PR#86 LOOK](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-jobs-contra-apply-playbook-7732/earn-jobs-contra-apply-playbook-20260916/GO-GATES.md). Still **do-not-send**. |
| **PREP** | May rewrite **this** style-01 paste for **one** posting, locally | Not granted here. Use PR#86 PREP. Still **do-not-send**. |
| **SEND** | May click **Apply** on **that one** listing | **`false`.** Needs a later dated human SEND GO. **This folder is not that GO.** |

Passing LOOK + PREP + a filled `{{ONE_SPECIFIC_DETAIL}}` is the expected success: `prepped_not_sent`. It is **not** Apply.

---

## UI labels that mean send / publish (stop)

Do not click. Log `stopped_at_apply` / `stopped_at_publish` locally. Leave.

**Apply / proposal**

- **Apply** / **Submit** / **Submit application** on a Job-feed posting
- **Send proposal** / **Create proposal** / paid-project **Send** from this pack
- **Reply** / **Send** on an inbound Contra inquiry (not this one-shot)

**Publish / growth**

- **Publish** / **Make discoverable** / feed publish
- **Get Pro** / **Get Max** / **Upgrade** / add a card
- **Refer & Earn**
- Labs / Expert program / Discover boost
- Job Network **video** / **Loom** submit

**Identity / wallet / location**

- Wallet / Add account / payout
- Persona / Verify identity / government photo ID / selfie
- Change location Kent, USA → Japan

**All**

- Any second Google / second Contra
- Any auto-apply extension, scraper, or “apply to more”

---

## What DRAFT work is allowed without flipping a row

1. Do **not** require a live Contra session from **this** authoring PR.
2. Later human: follow [PR#86](https://github.com/rimone0511/autopilot-log/pull/86) on the **existing** Free Independent (MAIN Google).
3. LOOK the official Job feed. **Dismiss** / skip freely.
4. If **one** posting is an inbound n8n / official-API path: PREP [PASTE.md](PASTE.md) in a **local** editor, or into a composer you will **clear**.
5. Fill `{{ONE_SPECIFIC_DETAIL}}` from **that** posting. Skip if it will not fill in about a minute.
6. Watch the character counter.
7. Close. Do not click Apply.

If the field cannot be cleared safely, do not paste into Contra. Keep the draft in this folder.

A true unpublished composer, if visible, still does **not** authorize Apply from this PR.

---

## One-listing rule (Apply — still off)

Skip the posting if any box is false. Even after a later GO, still **one** listing of style 01, then stop.

- [ ] I opened **this** job on **contra.com** (not a scraper, not a third-party apply tool).
- [ ] This GO-GATES file is still all `false` unless 祐太 flipped **`contra_apply_opportunity`** for **this** click in a dated note **outside** this folder.
- [ ] I replaced `{{ONE_SPECIFIC_DETAIL}}` with a fact from **this** posting. Empty → skip.
- [ ] The ask matches style **01** (inbound path + failure alert + SOP). Classify / AI-ops / gate / sheet-only → skip this pack.
- [ ] I am not using style 01 on a second listing this wave.
- [ ] Leftover placeholders and `[FICTION]` / `Client A` are gone.
- [ ] No email, phone, WhatsApp, Telegram, Slack, Discord in the paste.
- [ ] No off-platform payment. No live USD in git.
- [ ] No Pro / wallet / Persona / card wall on the Apply control.
- [ ] I will click **Apply** myself only after a GO **outside** this folder. Nothing here submits.

---

## Paid / boost (always false this pack)

Do not buy to “become apply-ready”:

- Contra Pro / Max
- Discover boost / paid highlighting
- Expert program / Contra Labs
- Wallet funding “to verify”
- Refer & Earn

Pricing page (do not buy; do not copy list prices into git): https://contra.com/pricing

---

## KYC / wallet / location

`contra_persona_wallet` and `contra_change_location` stay **`false`**.  
Kent, USA is an intentional STOP, not a jobs-phase fix. If Persona, wallet, or a country-change proof screen appears: close the picker **without a file**. Hand desk + screen type to morning. Documents stay on the **site screen**. Not in git. Not in chat. Not in an agent.

---

## Gate → outcome

| If | Outcome code | Send? |
|---|---|---|
| Playbook LOOK false | `look_blocked` / STOP code | no |
| Feed walled | `pro_wall` `card_wall` `wallet_wall` `persona_wall` `kyc_wall` `job_network_wall` `labs_or_expert_wall` | no |
| Posting is not inbound-path | `style_skipped` | no |
| `{{ONE_SPECIFIC_DETAIL}}` empty | `detail_empty` | no |
| Style 01 already used this wave | `style_already_used` | no |
| PREP true, SEND GO absent | `prepped_not_sent` (**normal**) | **no** |
| Live rate required, ledger empty | `rate_required` | no |
| Agent / script would submit | `auto_apply_forbidden` | **no** |
| SEND GO present + `contra_apply_opportunity: true` | later human may Apply **once** | only then |

`prepped_not_sent` is a **successful** one-shot. It is not a failed apply.

---

## What is never a GO

- This folder existing (`one_shot_ready` is not sent)
- PR#71 existing (drafts are copy text)
- PR#86 existing (LOOK/PREP only; SEND still false)
- PR#88 Rank 2 (“prepare one Job-feed text”)
- First-client help Step 5 “make applying a habit”
- Contra marketing about Job feed / Pro / Expert badges
- A computer-use agent finishing the serial
- “The composer already has text in it”
- Fictional `Client A` / `[FICTION]` fills
- Filling every placeholder except a later human SEND GO

---

## Fail-closed test (operator)

Ask: “Did a human outside this repo write a dated GO that **this** Job-feed listing may receive Apply, using style 01?”  
If the answer is no, missing, or “the PR is merged so it must be OK” → **do not Apply**.
