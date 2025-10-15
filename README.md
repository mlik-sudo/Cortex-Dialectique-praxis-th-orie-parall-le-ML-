# Cortex Dialectique — théorie ↔ praxis (agents CLI)

[![secret-scan](https://github.com/mlik-sudo/Cortex-Dialectique-praxis-th-orie-parall-le-ML-/actions/workflows/secret-scan.yml/badge.svg)](../../actions/workflows/secret-scan.yml)
[![link-check](https://github.com/mlik-sudo/Cortex-Dialectique-praxis-th-orie-parall-le-ML-/actions/workflows/link-check.yml/badge.svg)](../../actions/workflows/link-check.yml)
[![nightly-bench](https://github.com/mlik-sudo/Cortex-Dialectique-praxis-th-orie-parall-le-ML-/actions/workflows/nightly-bench.yml/badge.svg)](../../actions/workflows/nightly-bench.yml)

> De la théorie à l'expérience et de l'expérience à la théorie — en boucle.
![nightly](project-space/dashboards/badges/nightly.svg) ![secret-scan](project-space/dashboards/badges/secret-scan.svg)
![Smoke](project-space/dashboards/badges/smoke.svg)

## Vision

Orchestrateur multi-drivers (Codex, Jules, Gemini CLI, Claude Code, ChatGPT-5, Comet) avec quotas, sécurité, observabilité.

## Arborescence (extrait)

- `.github/workflows/` — CI sécurité, nightly-bench, link-check, codeql
- `project-space/agents/` — {jules, gemini-cli, codex-cli, claude-code}
- `project-space/a2a/` — router v2 (policies, budgets, drivers, cards)
- `project-space/benchmarks/` — scenarios, harness, results
- `project-space/dashboards/` — prometheus_rules.yml, grafana.json, badges
- `project-space/docs/` — ARCHITECTURE.md, GOVERNANCE.md, ADR/
