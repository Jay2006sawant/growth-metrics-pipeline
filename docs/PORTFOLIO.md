# Portfolio proof (recruiters)

Use these links on your resume or application.

| Proof | URL |
|-------|-----|
| **Live chart preview** | https://jay2006sawant.github.io/growth-metrics-pipeline/ (after GitHub Pages is enabled; see below) |
| **Written insights** | [business_insights.md](business_insights.md) |
| **Looker Studio** | Publish using [looker_studio_setup.md](looker_studio_setup.md), then paste your report URL in the repo README under *Live demos*. |

## Enable GitHub Pages (one time)

1. Repo **Settings → Pages → Build and deployment**: Source = **GitHub Actions**.
2. Push to `main`. The `pages` workflow deploys `docs/dashboard/`.
3. Wait 2–5 minutes, then open the live preview URL above.

## Refresh numbers

```bash
make all
python python/generate_insights.py
git add docs/dashboard/summary.json docs/business_insights.md
git commit -m "refresh dashboard summary"
git push
```

The Pages workflow runs on push; re-run it if only JSON changed and Pages did not update.
