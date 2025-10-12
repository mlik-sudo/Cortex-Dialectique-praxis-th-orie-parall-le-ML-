# Cortex Dialectique — Observatoire Poly-Agents

## Vision
Construire un observatoire local où la théorie (policies, ADR) et la praxis (agents CLI) s’enrichissent en boucle mesurable, avec sécurité par défaut et instrumentation continue.

## Périmètre
- **Project-space** : espace de travail versionné pour agents et maintainers.
- **Policies** : routage, budgets et limites pour piloter les drivers.
- **Security** : hooks pré-commit/pré-push et règles de gestion des secrets.
- **Benchmarks** : scénarios, harnais et résultats de mesure codex.

## Roadmap
- **J+0** : Arborescence minimale, policies v0, hooks de sécurité et premiers artefacts de mesure.
- **J+1** : Instrumenter les workflows critiques, ajouter scénarios de benchmarks et premières dashboards réelles.
- **J+2** : Activer la boucle complète théorie ↔ praxis avec revues régulières et badges automatisés.

## Démarrer
1. Installer les hooks pré-commit (`pre-commit install && pre-commit install --hook-type pre-push`).
2. Consulter `docs/ARCHITECTURE.md` pour la vue d’ensemble.
3. Examiner `project-space/policies/routing.yaml` et `budgets.yaml` avant tout run.
4. Collecter les métriques dans `project-space/benchmarks/results` après chaque session.

### CI & observabilité
- **pre-commit** : exécute les hooks `detect-secrets`, `gitleaks` et front-matter sur chaque PR vers `main`.
- **secret-scan** : rejoue les scans de secrets (baseline + gitleaks) sur `push`/`PR` et chaque nuit (`05:00 UTC`).
- **nightly-bench** : exporte les résultats en `JSONL`/`CSV`, génère les badges et publie les artefacts chaque nuit.
- En environnement hors-ligne, utiliser `PATH=$PWD/tools/offline:$PATH pre-commit run --all-files --config security/pre-commit-config.yaml` pour rejouer les contrôles essentiels.

## Liens utiles
- [Architecture](docs/ARCHITECTURE.md)
- [Governance](docs/GOVERNANCE.md)
- [ADR-0001](docs/ADR/ADR-0001.md)
- [Security Policies](security/policies.md)
- [Benchmarks](project-space/benchmarks)

---

> De la théorie à la praxis, puis retour — à chaque boucle, des preuves.
