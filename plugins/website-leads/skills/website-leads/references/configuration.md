# Portable configuration

Create a per-user configuration outside the plugin source, for example `website-leads-config.json`. Never commit credentials, reports, screenshots, or a registry to the plugin repository.

```json
{
  "default_country": null,
  "default_target": 15,
  "max_target_per_run": 50,
  "max_candidates_per_run": 250,
  "max_pages_per_source": 25,
  "retention_days": 90,
  "persistence": {"mode": "local", "registry_path": "<user-selected-private-path>/website-leads.jsonl"},
  "phone_normalization": {"mode": "conservative", "default_region": null},
  "web_research": {"enabled": true, "respect_robots_and_terms": true, "max_requests_per_host_per_minute": 12}
}
```

Validate numeric limits as positive. A target above `max_target_per_run`, missing remote configuration, unavailable browser, blocked source, or invalid persistence path is an actionable error: explain it, preserve the queue/checkpoint, and either use the permitted fallback or stop. Never bypass access restrictions or retry aggressively.

Default limits are guardrails, not a promise of results. Browser-unavailable runs may qualify `No Website` only when its enhanced absence evidence is met; all visual or interaction claims need browser evidence and belong in review otherwise.

