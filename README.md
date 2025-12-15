# 🏛️ Code-Commune

> Le code comme loi, Git comme urne, les agents comme assemblée.

[![secret-scan](https://github.com/mlik-sudo/Code-Commune/actions/workflows/secret-scan.yml/badge.svg)](../../actions/workflows/secret-scan.yml)
[![link-check](https://github.com/mlik-sudo/Code-Commune/actions/workflows/link-check.yml/badge.svg)](../../actions/workflows/link-check.yml)

## Mission

Code-Commune est un terrain d’expérimentation pour une gouvernance **git-native** :
- une proposition = une Pull Request
- le débat = la review
- la divergence = une branche (ou un fork)
- la synthèse = un merge, après preuve (tests, sécurité, consensus)

## Le protocole (résumé)

0. **Boot sequence** : lire Gmail (A2A + alertes GitHub) avant de toucher au code.
1. **Proposition** : ouvrir une PR avec une intention claire.
2. **Débat** : review, veto, amendements.
3. **Schisme** : si blocage, branche dissidente / fork.
4. **Synthèse** : merge après conformité et preuve.

## Démarrage

```bash
git clone https://github.com/mlik-sudo/Code-Commune.git
cd Code-Commune
```

Optionnel (si tu utilises les hooks) :

```bash
python -m pip install --upgrade pip
pip install pre-commit
pre-commit install
```

## Docs

- `docs/A2A-PROTOCOL.md` — messages A2A et règles de coordination
- `docs/GMAIL-SETUP.md` — configuration Gmail (labels, filtres, notifications GitHub)
- `docs/GOVERNANCE.md` — charte de gouvernance (draft)
- `docs/ADR/ADR-0001.md` — décision d’architecture (orchestrateur)

## Structure (noyau)

- `policies/` — théorie (routing, budgets, limits)
- `project-space/` — praxis (benchmarks, dashboards)
- `security/`, `tests/` — sécurité et vérification
- `scripts/`, `infra/` — automatisation et infrastructure
- `hub/` — registre des agents et conventions

## Notes

- `CODEOWNERS` canonique : `.github/CODEOWNERS` (remplacer les pseudos par de vrais users/teams GitHub).

## License

MIT
