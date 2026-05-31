# Portfolio proof (recruiters)

Use these links on your resume or application.

| Proof | URL |
|-------|-----|
| **Live chart preview** | https://jay2006sawant.github.io/growth-metrics-pipeline/ (after GitHub Pages is enabled; see below) |
| **Written insights** | [business_insights.md](business_insights.md) |
| **Looker Studio** | Publish using [looker_studio_setup.md](looker_studio_setup.md), then paste your report URL in the repo README under *Live demos*. |

## Enable GitHub Pages (one time)

If the **github-pages** deployment shows a red X, the repo is usually not set to Actions yet.

1. Open **Settings → Pages**.
2. Under **Build and deployment**, set **Source** to **GitHub Actions** (not “Deploy from a branch”).
3. Go to **Actions**, open the latest **pages** workflow run, and click **Re-run all jobs** (or push any commit to `main`).
4. Wait 2–5 minutes, then open https://jay2006sawant.github.io/growth-metrics-pipeline/

The site is static HTML in `docs/dashboard/` (includes `.nojekyll` so Jekyll is skipped).

## Refresh numbers

```bash
make all
python python/generate_insights.py
git add docs/dashboard/summary.json docs/business_insights.md
git commit -m "refresh dashboard summary"
git push
```

The Pages workflow runs on push; re-run it if only JSON changed and Pages did not update.
