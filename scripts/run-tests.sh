#!/usr/bin/env bash
set -euo pipefail

# Runs repository tests in a predictable way.
# Intended to be called by `make test-all`.

if ! command -v pytest >/dev/null 2>&1; then
  echo "pytest not found. Install dev deps: pip install -r requirements-dev.txt" >&2
  exit 1
fi

pytest -q tests/
