> **DRAFT_ONLY. DO NOT SEND.**  
> This folder is copy text for a human. It is not a mailer, sequencer, or Gmail bot.

# HANDS + ToS — cold email to SMBs (no automation)

**HANDS** means: you read **this** public page, you rewrite the one specific line, you (later, only after a GO outside this repo) paste in **your** mail client, **you** decide whether the legal basis is real. A computer must not be the thing that sends.

This pack does **not** certify that a cold advertising email is lawful for a given address. Japan’s default for advertising mail is **opt-in**. US CAN-SPAM is not a permission slip to harvest lists. Read the live official pages before arguing with a composer.

## Forbidden in this pack (do not add later either)

Do **not** write or run:

- SMTP / Gmail API / n8n / Zapier / Make send from this folder
- Sequencers, “unlimited inboxes”, domain-warming farms, or purchased mailbox pools
- Harvested, scraped, or purchased lists; dictionary attacks; scraped WHOIS
- BCC blasts, CSV imports, or “just 10 SMBs as a test”
- A second Gmail / domain to dodge reputation or a prior opt-out
- Fake From names, spoofed domains, or misleading subjects
- Invented case studies, fake metrics, or partner badges
- Calendar links, WhatsApp, phone, or “text me” in the first note
- Live USD/JPY in git
- Filling `{{RECIPIENT_EMAIL}}` or `{{POSTAL_ADDRESS}}` in a commit

## Official lines this pack is obeying (re-check live)

### United States — CAN-SPAM (B2B is covered)

FTC compliance guide (retrieved 2026-09-15):  
https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business

The guide states, among other rules:

1. Accurate From / To / Reply-To / domain — identify the initiator.
2. Subject must match the body (no deceptive subjects).
3. Identify the message as an advertisement.
4. Include a valid physical postal address (street, USPS PO box, or CMRA box — **Japan-based seller: use a real address you are allowed to publish; do not invent a US box in git**).
5. Clear opt-out; honor within **10 business days**; keep the mechanism working at least **30 days** after send.
6. No exception that “it is B2B so CAN-SPAM does not apply.”
7. You cannot contract away compliance if someone else hits Send for you.
8. Harvesting / dictionary attacks are aggravated.

This pack’s fenced footers are **templates** for those disclosures. They are not a completed legal footer until `{{POSTAL_ADDRESS}}` and `{{OPT_OUT_CONTACT}}` are real — which this git copy does not fill.

### Japan — 特定電子メール法 (advertising email)

MIC overview (retrieved 2026-09-15):  
https://www.soumu.go.jp/main_sosiki/joho_tsusin/d_syohi/m_mail.html  

Guideline PDF (MIC):  
https://www.soumu.go.jp/main_sosiki/joho_tsusin/d_syohi/pdf/m_mail_081114_1.pdf  

Pamphlet (MIC, 表示義務 / 受信拒否):  
https://www.soumu.go.jp/main_sosiki/joho_tsusin/d_syohi/pdf/m_mail_pamphlet.pdf  

Re-check the live statute on e-Gov before send; this pack cites MIC materials that were fetchable on 2026-09-15 rather than a brittle e-Gov permalink.

Facts used here (re-read the live text; this is not legal advice):

- Advertising / solicitation email is **特定電子メール**. Default is **opt-in** (Art. 3): do not send without prior consent, with listed exceptions in the statute and ordinance (including, among others, a party in an existing business relationship, and certain **published** addresses of organizations or individuals who operate a business).
- An exception is **not** “every contact@ on a corporate site is a blast target.” The operator must be able to name the exception for **this** address without stretching. If they cannot, **skip**.
- Do not falsify sender information (Art. 5).
- Display duties (Art. 4 + ordinance): sender name, a working opt-out address or URL, and other prescribed items (MIC materials include **address** among display items). Honor a refusal; do not send again.
- Consent records, when consent is the basis, must be kept as the ordinance requires.

**This pack does not decide that Art. 3(1)(iv) or any other exception applies.** Skip unless a human can point at the live statute/guideline and the live public page together.

### Japan — 特定商取引法 (email ads)

If the note is an email advertisement for a mail-order / service offer, 特商法 email-ad rules may also apply. This pack is not a 特商法 filing and does not invent a registration number. If the live form or counsel says stop, stop.

### n8n / APIs

- n8n export/import: https://docs.n8n.io/build/manage-workflows/export-and-import/
- Offer official connectors and documented APIs only. No “we will log into the admin UI for you with a bot.”

## Allowed (this pack)

- Draft in git with placeholders
- One human-personalized first note **per** public page, only with a real public hook
- Declining scraping, engagement fraud, ungated send/publish, or KYC-by-proxy
- Linking **public** portfolio / GitHub
- Stopping at send, mailbox-draft creation, list import, or legal uncertainty

## Theme-specific declines (do not stretch the paste)

| Theme | Take | Decline |
|---|---|---|
| n8n workflow | Official API / documented connector + SOP + failure alert | Browser bots, unofficial scrapers, partner-badge impersonation |
| AI ops | Draft / inspect / human approve before send | Fully autonomous outbound, invented citations, KYC-by-proxy |
| lead classify | Tags + route + human review of the unsure bucket | Auto-spam sequences, scraped contact lists, fake intent scores |

If the public page is a job ad, a “do not contact vendors” notice, or a personal mailbox, skip.
