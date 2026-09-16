# Website Leads Suite — V1.1

## Claude Code compatibility

This package can also be installed in Claude Code. See [CLAUDE-CODE.md](CLAUDE-CODE.md) for installation and use. The Claude and Codex editions share the same Website Leads skill, safeguards, scripts, and reference material.

## npm installer

After the npm package is published, users will be able to install the supported host with one explicit command:

```text
npx @ciphertechnologies/website-leads codex
npx @ciphertechnologies/website-leads claude
```

The installer asks for confirmation before changing a marketplace or installing a plugin. Its source and publishing notes are in [`npm/website-leads-installer`](../../npm/website-leads-installer).

Website Leads Suite is a three-stage plugin for finding businesses that may need a new or improved website, preparing evidence-grounded outreach for review, and optionally delivering explicitly approved email campaigns through the installer's own authorized provider.

## What is included

- Portable `plugin.json`, plus a Codex compatibility manifest.
- Three connected skills: research, draft outreach, and approval-gated delivery.
- Portable configuration, a local/remote deduplication contract, quality checks, and examples.
- Small standard-library helpers for deterministic identity normalisation and pre-export validation.

## The three-stage workflow

1. `$website-leads:website-leads` researches public business information and produces the four-sheet evidence-backed XLSX report.
2. `$website-leads:craft-website-outreach` turns eligible report rows into a review workbook and drafts. It never sends.
3. `$website-leads:send-website-outreach` performs preflight and can deliver only rows marked exactly `Approved`, only through an email provider the installer has connected and authorized.

Copy `config/outreach-config.example.json` to a private, user-controlled location and complete it before drafting or delivery. Never commit the completed file, reports, registries, or credentials.

## Install and test locally

Place this folder at `plugins/website-leads` in a repository, then copy `marketplace.example.json` to `.agents/plugins/marketplace.json` in that repository. Add the marketplace as a local source, restart the desktop app, install the plugin, and test in a new chat. The example path assumes that conventional layout; change only its relative `source.path` if you use another layout.

Use a prompt such as: “Find 10 verified website-improvement leads in [location], across at least four industries, and export the report to Excel.” The skill asks for location and target only when they are not safely inferable.

## Architecture

The research and drafting stages are usable without a backend if the host provides web search/browser access and an XLSX-capable environment. Local deduplication writes an append-only JSONL registry chosen by the installer. It is private to that user/device unless they deliberately sync it.

A shared team history, cross-device deduplication, managed browser research, or live delivery needs an optional remote MCP/backend or host-authorized email provider. No sending connector is bundled in V1.1: without one, the delivery skill produces preflight output only and never sends.

## Privacy and safe use

Research only publicly advertised business contact details. Do not infer personal addresses, collect gated data, bypass access controls, or use the output as consent to market. Drafting does not contact anyone. Live delivery requires explicit approval for each row, the installer's own authorized provider, and compliance with applicable law. Evidence may contain public contact details and screenshots; keep reports and evidence packages access-controlled, minimise retention, and delete them when no longer needed. See `references/privacy-and-data.md`.

## Before public submission

The publisher, support email, repository, and hosted homepage, privacy policy, and terms URLs are configured. Add final icons/screenshots if desired, complete live-host testing, and submit through the OpenAI plugin submission portal. Do not claim a backend capability until it is deployed, documented, and reviewed.

## License

MIT. See `LICENSE`.

