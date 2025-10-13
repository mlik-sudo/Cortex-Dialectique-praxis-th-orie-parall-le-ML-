# Cortex Dialectique — théorie ↔ praxis (agents CLI)

> De la théorie à l'expérience et de l'expérience à la théorie — en boucle.

![nightly](project-space/dashboards/badges/nightly.svg) ![secret-scan](project-space/dashboards/badges/secret-scan.svg)

## Vision
Orchestrateur multi-drivers (Codex, Jules, Gemini CLI, Claude Code, ChatGPT-5, Comet) avec quotas, sécurité, observabilité.

## Arborescence (extrait)
- `.github/workflows/` — CI sécurité, nightly-bench, link-check, codeql
- `project-space/agents/` — {jules, gemini-cli, codex-cli, claude-code}
- `project-space/a2a/` — router v2 (policies, budgets, drivers, cards)
- `project-space/benchmarks/` — scenarios, harness, results
- `project-space/dashboards/` — prometheus_rules.yml, grafana.json, badges
- `project-space/docs/` — ARCHITECTURE.md, GOVERNANCE.md, ADR/
- `project-space/security/` — pre-commit, secret policies

## Workflows CI
- **secret-scan.yml** (bloquant PR)
- **nightly-bench.yml** (export → badges)
- **link-check.yml** (liens)
- **codeql.yml** (code scanning)

## Sécurité & Gouvernance
MIT · branch protection (checks Required) · secrets hors VCS · logs redacted · front-matter requis.

## Observabilité
Prometheus (task_duration_seconds…) + Grafana (stubs).

## Roadmap
J+0 skeleton+sécurité · J+1 CI+badges · J+2 router v2 + scénarios.

## Contribuer
Conventional Commits + footer `Project: cortex-dialectique-ml`.