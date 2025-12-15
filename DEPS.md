# DEPS (overview)

Objectif: une page courte pour aider `@Comet-Scout` à faire la due diligence.

## GitHub Actions

- `actions/checkout@v5`
- `actions/setup-python@v5`
- `actions/upload-artifact@v4`
- `github/codeql-action@v4`
- `gitleaks/gitleaks-action@v2`
- `peter-evans/create-pull-request@v7`
- `lycheeverse/lychee-action@v2.0.2`
- `raven-actions/actionlint@v2`
- `ibiqlik/action-yamllint@v3`

## Python (dev)

- `pre-commit`
- `detect-secrets==1.5.0`

## Règle Comet

Avant d’adopter une nouvelle dépendance:
- vérifier la doc officielle et sa fraîcheur
- vérifier que la version existe réellement (PyPI/npm, tags GitHub)
- vérifier l’activité du projet (releases, commits, issues)
