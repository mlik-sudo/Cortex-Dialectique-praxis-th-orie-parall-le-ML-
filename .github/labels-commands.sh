#!/usr/bin/env bash
set -e
# Requiert: gh auth login
for L in proposal critique synthesis jules; do
  gh label create "$L" --color FFB000 --description "Cortex debate: $L" || true
done
