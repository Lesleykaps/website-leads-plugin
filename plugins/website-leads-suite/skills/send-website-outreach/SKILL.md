---
name: send-website-outreach
description: Preflight and deliver explicitly approved website-outreach campaigns through a user-authorized email provider. Use only after craft-website-outreach and explicit human approval.
---

# Send Website Outreach

Deliver only explicitly approved campaign rows through a user-authorized sending provider. This skill never researches leads, changes campaign copy, guesses approvals, creates credentials, or sends WhatsApp messages.

## Configuration and capability gate

Read `../../config/outreach-config.example.json` as the configuration contract. The user must configure their own sender identity, private registry, timezone, and a supported provider outside this plugin. Credentials and OAuth tokens must remain in that provider or host connection; never ask the user to paste them into chat or save them in the plugin.

If `delivery.provider` is `none`, an approved email connection is unavailable, or the host has no authorized delivery tool, do preflight only: produce a delivery manifest and clear setup instructions. Do not simulate a successful send.

## Preflight before every delivery

1. Read the latest configured registry and campaign workbook. A row is eligible only when its approval cell is exactly `Approved` and it has a verified public business contact, Lead ID, and evidence URL.
2. Exclude and report any row already sent, replied, bounced, opted out, unsubscribed, do-not-contact, missing approval, or unresolved duplicate.
3. Reconfirm that the configured sender identity and approved provider match the user’s intent. Default to dry-run; live delivery needs a direct, current user instruction naming the campaign ID.
4. Enforce the configured weekday cap (default 10 initial messages) and allowed days. Never send on a disallowed day. Send no more than one initial message to the same lead/contact.

## Delivery and follow-ups

For a live run, send only eligible initial emails using the approved copy. Attach only files mapped to that Lead ID; follow-ups must be plain email. Record provider message/thread IDs and update the registry after each confirmed provider result.

Follow up only after the configured intervals and only if the same thread has no reply, bounce, unsubscribe, opt-out, or do-not-contact state. Stop immediately after any such state. If the registry update or provider confirmation fails, stop the run and report the unknown outcome rather than retrying and risking duplicates.

Return a run summary with sent, skipped, follow-up, reply, bounce, opt-out, error, and unresolved counts. Never silently schedule background sending; scheduling requires a separate user-configured backend and a fresh approval gate.

## Boundaries

- Never send drafts, Pending, Rejected, or missing-approval rows.
- Never alter messages or approvals during delivery.
- Never send WhatsApp, SMS, calls, or social messages.
- Never bypass provider limits, consent rules, source terms, or applicable law.
