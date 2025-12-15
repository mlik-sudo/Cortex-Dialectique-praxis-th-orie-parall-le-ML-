# 🔧 Operations Manual

> Logistique technique pour faire fonctionner la Commune.

Ce document couvre la configuration pratique des agents. Pour la philosophie et le protocole, voir [README.md](./README.md).

---

## 👤 Identité des Agents (Git Config)

Nous utilisons la stratégie **Compte Maître + Alias** pour simuler l'indépendance des agents tout en conservant un historique Git traçable.

### Configuration par Agent

```bash
# Pour @Gemini-Architect
git config user.name "Gemini-Architect"
git config user.email "codecommune.gov+gemini@gmail.com"

# Pour @Claude-Safety
git config user.name "Claude-Safety"
git config user.email "codecommune.gov+claude@gmail.com"

# Pour @Codex-Engineer
git config user.name "Codex-Engineer"
git config user.email "codecommune.gov+codex@gmail.com"

# Pour @Comet-Scout
git config user.name "Comet-Scout"
git config user.email "codecommune.gov+comet@gmail.com"

# Pour @ChatGPT-Mediator
git config user.name "ChatGPT-Mediator"
git config user.email "codecommune.gov+mediator@gmail.com"
```

### Vérification

```bash
git config user.name   # Doit afficher l'agent actif
git config user.email  # Doit afficher l'alias correspondant
```

---

## 📧 Configuration Gmail

### Structure des Alias

Un seul compte Gmail (`codecommune.gov@gmail.com`) avec des alias :

| Agent | Alias Email |
|-------|-------------|
| @Gemini-Architect | `codecommune.gov+gemini@gmail.com` |
| @Claude-Safety | `codecommune.gov+claude@gmail.com` |
| @Codex-Engineer | `codecommune.gov+codex@gmail.com` |
| @Comet-Scout | `codecommune.gov+comet@gmail.com` |
| @ChatGPT-Mediator | `codecommune.gov+mediator@gmail.com` |

### Filtres Gmail (Labels)

Créer un filtre pour chaque alias :

1. **Gemini** : `to:codecommune.gov+gemini@gmail.com` → Label `🤖 Gemini`
2. **Claude** : `to:codecommune.gov+claude@gmail.com` → Label `🛡️ Claude`
3. **Codex** : `to:codecommune.gov+codex@gmail.com` → Label `⚡ Codex`
4. **Comet** : `to:codecommune.gov+comet@gmail.com` → Label `🔭 Comet`
5. **Mediator** : `to:codecommune.gov+mediator@gmail.com` → Label `⚖️ Mediator`

### Boot Sequence (Routine Quotidienne)

Chaque agent, avant de coder, doit :

1. **Consulter son label Gmail** — Notifications GitHub, A2A messages
2. **Lire les PRs assignées** — Via GitHub ou MCP
3. **Vérifier les alertes Dependabot** — Priorité si CVE

---

## 🔐 GitHub Configuration

### Branch Protection Rules (main)

```yaml
# Settings > Branches > main
require_pull_request_reviews:
  required_approving_review_count: 2
  require_code_owner_reviews: true
  dismiss_stale_reviews: true

require_status_checks:
  strict: true
  contexts:
    - secret-scan
    - link-check
    - test-suite

restrictions:
  users: []  # Personne ne push directement
  teams: []
```

### CODEOWNERS (.github/CODEOWNERS)

```
# Constitution Technique de Code-Commune

# Sécurité et Noyau : Domaine de @Claude-Safety
/core/          @mlik-sudo
/security/      @mlik-sudo
/tests/         @mlik-sudo

# Innovation et Features : Domaine de @Gemini-Architect
/features/      @mlik-sudo
/experimental/  @mlik-sudo

# Infrastructure : Domaine de @Codex-Engineer
/scripts/       @mlik-sudo
/infra/         @mlik-sudo
Dockerfile      @mlik-sudo

# Documentation et Veille : Domaine de @Comet-Scout
/docs/          @mlik-sudo
/research/      @mlik-sudo
DEPS.md         @mlik-sudo

# Délibération : Domaine de @ChatGPT-Mediator
/deliberation/  @mlik-sudo
```

> **Note** : Remplacer `@mlik-sudo` par les vrais comptes GitHub des agents quand disponibles.

---

## 🛠️ Scripts Utilitaires

### Switch d'Agent

Créer un script `scripts/switch-agent.sh` :

```bash
#!/bin/bash
# Usage: ./scripts/switch-agent.sh gemini|claude|codex|comet|mediator

case $1 in
  gemini)
    git config user.name "Gemini-Architect"
    git config user.email "codecommune.gov+gemini@gmail.com"
    echo "🤖 Switched to Gemini-Architect"
    ;;
  claude)
    git config user.name "Claude-Safety"
    git config user.email "codecommune.gov+claude@gmail.com"
    echo "🛡️ Switched to Claude-Safety"
    ;;
  codex)
    git config user.name "Codex-Engineer"
    git config user.email "codecommune.gov+codex@gmail.com"
    echo "⚡ Switched to Codex-Engineer"
    ;;
  comet)
    git config user.name "Comet-Scout"
    git config user.email "codecommune.gov+comet@gmail.com"
    echo "🔭 Switched to Comet-Scout"
    ;;
  mediator)
    git config user.name "ChatGPT-Mediator"
    git config user.email "codecommune.gov+mediator@gmail.com"
    echo "⚖️ Switched to ChatGPT-Mediator"
    ;;
  *)
    echo "Usage: $0 {gemini|claude|codex|comet|mediator}"
    exit 1
    ;;
esac
```

### Proof Pack Check

Créer un script `scripts/proof.sh` :

```bash
#!/bin/bash
# Vérifie qu'une PR a un Proof Pack complet

echo "📦 Proof Pack Verification"
echo "=========================="

# 1. Tests
echo -n "✓ Tests: "
if make test-all 2>/dev/null; then
  echo "PASS"
else
  echo "FAIL"
  exit 1
fi

# 2. Linting
echo -n "✓ Lint: "
if pre-commit run --all-files 2>/dev/null; then
  echo "PASS"
else
  echo "FAIL"
  exit 1
fi

# 3. Security scan
echo -n "✓ Security: "
if detect-secrets scan --baseline .secrets.baseline 2>/dev/null; then
  echo "PASS"
else
  echo "WARN - Review manually"
fi

echo ""
echo "✅ Proof Pack COMPLETE"
```

---

## 📊 Monitoring

### Métriques à Suivre

| Métrique | Outil | Seuil d'Alerte |
|----------|-------|----------------|
| PRs ouvertes > 7 jours | GitHub API | > 5 PRs |
| CVE non patchées | Dependabot | > 0 critical |
| Coverage tests | Codecov | < 80% |
| Temps review moyen | GitHub Insights | > 48h |

### Dashboard (optionnel)

Voir `dashboards/grafana.json` pour un dashboard Grafana pré-configuré.

---

## 🚨 Procédures d'Urgence

### CVE Critique Détectée

1. @Claude-Safety **gèle** toutes les PRs features
2. @Codex-Engineer **prépare** le patch
3. @Comet-Scout **vérifie** la compatibilité upstream
4. PR de hotfix avec quorum réduit (2 agents)
5. Merge + déploiement immédiat
6. Post-mortem dans `/deliberation/`

### Schisme Non Résolu > 7 Jours

1. @ChatGPT-Mediator **convoque** une session de médiation
2. Les deux parties présentent leurs Proof Packs
3. Vote formel de l'Assemblée complète
4. La majorité l'emporte (3/5 minimum)

---

*Voir [CONTRIBUTING.md](./CONTRIBUTING.md) pour le guide de contribution.*
