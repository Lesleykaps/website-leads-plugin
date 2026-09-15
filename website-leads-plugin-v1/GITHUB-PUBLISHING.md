# Publish through GitHub Pages

1. Create a new public GitHub repository named `website-leads-plugin` and upload this folder's contents.
2. In GitHub, open **Settings → Pages**, set **Source** to **GitHub Actions**, then push the `main` branch. The included workflow publishes the contents of `site/`.
3. Copy the resulting `https://<account>.github.io/website-leads-plugin/` URL. Set the matching homepage, privacy, and terms URLs in `plugin.json`, then create a release tag such as `v1.0.0`.
4. Before a public plugin submission, replace the contributor placeholder in both manifests with the legal publisher name and a monitored support email.

For a custom domain, connect it in GitHub Pages first, verify its DNS ownership, and then replace the GitHub Pages URLs in the manifest. Do not use a URL you do not control.
