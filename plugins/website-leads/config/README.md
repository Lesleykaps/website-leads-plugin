# Private configuration

Copy `outreach-config.example.json` to a private folder outside this repository, replace the placeholders, and point the skills to that copy when prompted.

Use a local registry by default. A remote registry or sending provider is optional and must be user-authorized. Never put credentials, tokens, personal reports, campaign workbooks, screenshots, or registry data in this plugin repository.

`provider: "none"` is the safe default: the delivery skill will run preflight only. Change it only after connecting a provider through the host's approved account-connection mechanism.
