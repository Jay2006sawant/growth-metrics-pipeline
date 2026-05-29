#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
python python/export_dashboard.py
echo "Dashboard CSVs ready in dashboard/exports/"
