---
name: craft-website-outreach
description: Create review-ready, evidence-grounded website outreach drafts from a Website Leads report. Use after research; this skill never sends or schedules messages.
---

# Craft Website Outreach

Turn a verified Website Leads report into a reviewable outreach campaign. Draft only: never send, schedule, authenticate an email account, or treat a public contact as consent.

## Start safely

Read `../../config/outreach-config.example.json` as the configuration contract. The user must provide their own private data directory and sender identity; never assume a drive path, repository, email address, telephone number, country, or offer. Do not request or store passwords, API keys, or OAuth tokens.

Accept only the Qualified Leads and Evidence sheets from a Website Leads XLSX report (or equivalent structured data). Keep every source Lead ID. Before drafting, use the configured local registry or an explicitly configured authenticated team backend to exclude prior outreach, active drafts, opt-outs, do-not-contact records, and unresolved identity matches. If no registry is available, label the output `no historical deduplication` and require the user to approve proceeding.

## Eligibility and drafting

1. Exclude a lead without a verified public business contact, contact-source URL, evidence-backed website issue, or Medium/High confidence. Keep exclusions in a separate sheet.
2. For each eligible lead, find one truthful, public, business-specific personalization fact independent of the website issue. Save its source URL. Do not use generic industry or location facts.
3. Select one evidence-backed issue, one relevant service, and one cautious business outcome. Distinguish observation from inference. Never claim losses, rankings, security issues, ownership, budgets, or decision-maker status without evidence.
4. Draft an initial email and two follow-ups. Use one clear CTA. Only draft WhatsApp copy when the source explicitly advertises WhatsApp; a phone number alone is insufficient.
5. Do not quote prices, promise results, offer a discount, or create an attachment unless the user has supplied a current approved offer and the source evidence supports the attachment.

## Required outputs

Create a UTF-8 campaign CSV and an XLSX approval workbook containing `Campaign Review`, `Message Drafts`, `Excluded Leads`, and `Campaign Summary`. Each campaign row must include: campaign ID, Lead ID, verified observation and URL, contact source URL, personalization fact and URL, channel, subject/body/follow-ups, approval status `Pending`, outreach status `Ready for review`, and deduplication result.

Validate that every personalization fact is business-specific, every factual claim maps to evidence, every Lead ID is retained, and no row is marked approved merely because it was requested. Record warnings and missing configuration in Campaign Summary. Return the workbook, CSV, exclusions, and validation summary, then stop before delivery.

## Boundaries

- Do not contact a business or connect to a mailbox.
- Do not create one generic message by replacing only names.
- Do not use screenshots, scores, scraping, or internal research process in outreach copy.
- Do not draft for opt-outs, do-not-contact records, or existing active sequences.
- Public contact details are evidence, not permission. The user remains responsible for consent and applicable marketing law.
