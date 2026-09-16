# Website Leads — V1

## Claude Code compatibility

This package can also be installed in Claude Code. See [CLAUDE-CODE.md](CLAUDE-CODE.md) for installation and use. The Claude and Codex editions share the same Website Leads skill, safeguards, scripts, and reference material.

Website Leads is a research-only plugin for finding businesses that plausibly need a new or improved website. It produces a reviewable Excel report and evidence package, rather than an unverified list. It never sends email, messages, or calls.

## What is included

- Portable `plugin.json`, plus a Codex compatibility manifest.
- One skill with qualification, evidence, scoring, and safety rules.
- Portable configuration, a local/remote deduplication contract, quality checks, and examples.
- Small standard-library helpers for deterministic identity normalisation and pre-export validation.

## Install and test locally

Place this folder at `plugins/website-leads` in a repository, then copy `marketplace.example.json` to `.agents/plugins/marketplace.json` in that repository. Add the marketplace as a local source, restart the desktop app, install the plugin, and test in a new chat. The example path assumes that conventional layout; change only its relative `source.path` if you use another layout.

Use a prompt such as: “Find 10 verified website-improvement leads in [location], across at least four industries, and export the report to Excel.” The skill asks for location and target only when they are not safely inferable.

## Architecture

The skill is usable without a backend if the host provides web search/browser access and an XLSX-capable environment. Local deduplication writes an append-only JSONL registry chosen by the installer. It is private to that user/device unless they deliberately sync it.

A shared team history, cross-device deduplication, managed browser research, or quota enforcement needs an optional remote MCP/backend. That service must implement the contract in `references/persistence-and-backend.md`, authenticate each user, and obtain consent before a read/write action. No MCP server is bundled in V1, so no account is linked or data is transmitted by the plugin itself.

## Privacy and safe use

Research only publicly advertised business contact details. Do not infer personal addresses, collect gated data, bypass access controls, contact a business, or use the output as consent to market. Evidence may contain public contact details and screenshots; keep reports and evidence packages access-controlled, minimise retention, and delete them when no longer needed. See `references/privacy-and-data.md`.

## Before public submission

The publisher, support email, repository, and hosted homepage, privacy policy, and terms URLs are configured. Add final icons/screenshots if desired, complete live-host testing, and submit through the OpenAI plugin submission portal. Do not claim a backend capability until it is deployed, documented, and reviewed.

## License

MIT. See `LICENSE`.

