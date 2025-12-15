# 🔭 Comet Report — State of the Art (2025)

> Objectif: documenter des **best practices vérifiées** (liens, versions, activité upstream) pour la stack de Code-Commune.
>
> Règle: chaque affirmation importante doit pointer vers une source (release notes, docs officielles, changelog, issue GitHub, PyPI/npm).

## 1) Stack actuelle (à confirmer)

- CI: GitHub Actions (`actions/checkout@v5`, CodeQL, secret-scan, pre-commit)
- Python: workflows en `3.x` / `3.12` (tests, hooks)
- Secrets: `detect-secrets` + `gitleaks`
- Lint YAML: `actionlint`, `yamllint`

## 2) Best practices 2025 — checklist

### Dépendances & supply chain
- [ ] Pinning (commit SHA ou tags majeurs) pour actions critiques
- [ ] Politique de mise à jour (Dependabot + fenêtre de merge)
- [ ] Vérification de l’activité (commits récents, releases, issues critiques)

### CI (GitHub Actions)
- [ ] Permissions minimales par job
- [ ] Concurrency / cancel-in-progress
- [ ] Caches raisonnables (pip)

### Sécurité
- [ ] Secret scanning + baseline disciplinée
- [ ] Code scanning (CodeQL) activé et maintenu

### Documentation “vivante”
- [ ] Liens vérifiés (pas de 404)
- [ ] Pages de référence courtes: `README.md`, `DEPS.md`

## 3) Reality Check — template

Pour chaque outil / lib proposé:

- Nom:
- Usage dans le repo (fichier/ligne):
- Source officielle:
- Dernière release:
- Dernier commit:
- Statut (active / deprecated / archived):
- Issues critiques ouvertes:
- Verdict Comet: ✅ OK / ⚠️ Prudence / ❌ Rejet
- Action proposée (amendement PR / alternative):

## 4) Notes

Ce fichier est un **point d’entrée**: le détail peut être split par rapports datés dans `research/`.
