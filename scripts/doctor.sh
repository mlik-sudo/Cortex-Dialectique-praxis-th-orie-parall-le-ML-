#!/usr/bin/env bash
set -euo pipefail

missing=0
require() {
  if [[ ! -e "$1" ]]; then
    echo "[doctor] missing: $1" >&2
    missing=1
  fi
}

# Structure promised by README
require ".github/workflows"
require ".github/CODEOWNERS"
require "core"
require "security"
require "features"
require "experimental"
require "scripts"
require "infra"
require "tests"
require "docs"
require "hub"
require "deliberation"
require "policies"
require "project-space"

if [[ $missing -ne 0 ]]; then
  echo "[doctor] FAIL" >&2
  exit 1
fi

echo "[doctor] OK"
