# Orchestrateur A2A — Router v2 (stub)

Sélection par `skill`, `size`, `context_tokens`, avec **policies/budgets**.

## Règles v0
- run_and_fix_locally → driver_codex_cli (fallback: jules)
- generate_tests (large) → jules → gemini_cli
- watch + needs_fresh_web:true → comet → gemini_cli
- défaut → gemini_cli

## Budgets (extrait)
jules, gemini, codex, comet … (voir policies/*)

## Sécurité
écriture limitée au workdir; logs redacted.

## Fichiers
policies/{routing.yaml,budgets.yaml} · a2a/cards/*
