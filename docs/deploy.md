# Deploy (GitHub Pages)

The `pages` workflow publishes `docs/dashboard/` (static HTML + `summary.json`) to GitHub Pages.

Repository setting: **Pages → Build and deployment → Source: GitHub Actions**.

Workflow uses `actions/configure-pages@v5` with `enablement: true` so the Pages site is created on first deploy.

Public URL: https://jay2006sawant.github.io/growth-metrics-pipeline/
