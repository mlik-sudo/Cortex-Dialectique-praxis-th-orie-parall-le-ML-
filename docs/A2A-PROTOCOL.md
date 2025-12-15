---
project: cortex-dialectique
owner: claude-safety
reviewed: 2025-12-15
---

# 📬 Protocole A2A (Agent-to-Agent)
## Communication Asynchrone via Gmail

> **"Un Parlement sans communication est une anarchie silencieuse."**

---

## 🎯 Objectif

Ce protocole définit comment les agents IA du Cortex Dialectique communiquent entre eux de manière **asynchrone** via des canaux Gmail dédiés, créant ainsi :

1. **Un bus de messages A2A** — Communication inter-agents
2. **Une mémoire externe persistante** — Historique des décisions
3. **Un système d'alertes** — Notifications GitHub centralisées

---

## 📧 Registre des Canaux

| Agent | Canal Gmail | Domaine de Surveillance |
|-------|-------------|------------------------|
| 🛡️ **@Claude-Safety** | `claude.safety.cortex@gmail.com` | Sécurité, vetos, reviews critiques |
| 🤖 **@Gemini-Architect** | `gemini.architect.cortex@gmail.com` | Features, expérimentations, innovations |
| ⚡ **@Codex-Engineer** | `codex.engineer.cortex@gmail.com` | CI/CD, infra, scripts, builds |

---

## 🏷️ Système de Labels Gmail

Chaque boîte Gmail doit être configurée avec ces labels pour le tri automatique :

### Labels de Priorité
```
priority/critical    → Rouge   — Action immédiate requise
priority/high        → Orange  — À traiter dans la session
priority/normal      → Bleu    — File d'attente standard
priority/low         → Gris    — Quand le temps le permet
```

### Labels de Type
```
type/veto            → 🛑 Blocage d'une PR ou branche
type/approval        → ✅ Feu vert pour merge
type/question        → ❓ Demande de clarification
type/alert           → ⚠️ Notification système (Dependabot, CI)
type/sync            → 🔄 Mise à jour de statut
type/handoff         → 🤝 Passage de relais entre agents
```

### Labels de Statut
```
status/pending       → En attente de réponse
status/acknowledged  → Lu et pris en compte
status/resolved      → Traité et archivé
```

---

## 📋 Boot Sequence (Standup Asynchrone)

**Chaque agent DOIT exécuter cette séquence au démarrage :**

```
┌─────────────────────────────────────────────────────┐
│  BOOT SEQUENCE - Agent Activation Protocol          │
├─────────────────────────────────────────────────────┤
│  1. CHECK Gmail Inbox                               │
│     └─► Filter: is:unread label:priority/critical   │
│                                                     │
│  2. PROCESS Alerts (GitHub Notifications)           │
│     └─► Dependabot, CI failures, Security alerts    │
│                                                     │
│  3. READ A2A Messages                               │
│     └─► Vetos, handoffs, sync requests              │
│                                                     │
│  4. UPDATE Status                                   │
│     └─► Send "I'm online" to other agents           │
│                                                     │
│  5. PROCEED with planned work (if no blockers)      │
└─────────────────────────────────────────────────────┘
```

---

## 📝 Formats de Messages

### 1. Message de Veto

```
Subject: [VETO] PR #42 - feat/rust-rewrite
Labels: type/veto, priority/critical

---
🛑 VETO ÉMIS

PR: #42 feat/rust-rewrite
Auteur: @Gemini-Architect
Raison: Absence de tests de sécurité

Action requise:
- [ ] Ajouter tests dans /security/
- [ ] Review par @Claude-Safety

Ce veto sera levé après conformité.

— @Claude-Safety
```

### 2. Message de Handoff

```
Subject: [HANDOFF] Branche feature/auth → @Codex-Engineer
Labels: type/handoff, priority/high

---
🤝 PASSAGE DE RELAIS

Branche: feature/auth
De: @Gemini-Architect
Vers: @Codex-Engineer

Contexte:
La feature d'authentification est fonctionnelle.
Besoin d'optimisation des scripts de déploiement.

Fichiers concernés:
- /features/auth/login.py
- /scripts/deploy-auth.sh (À CRÉER)

— @Gemini-Architect
```

### 3. Message d'Alerte Système

```
Subject: [ALERT] CI FAILURE - main branch
Labels: type/alert, priority/critical

---
⚠️ ALERTE SYSTÈME

Source: GitHub Actions
Type: CI Failure
Branche: main
Commit: abc123

Erreur:
> Test security/test_injection.py FAILED

Action immédiate requise.
Tous les merges sont BLOQUÉS jusqu'à résolution.

— Système Automatique
```

### 4. Message de Sync

```
Subject: [SYNC] Statut quotidien - 2025-01-15
Labels: type/sync, priority/normal

---
🔄 RAPPORT DE SYNC

Agent: @Claude-Safety
Date: 2025-01-15
Session: 14:00 - 18:00 UTC

Accompli:
- ✅ Review PR #38, #39, #41
- ✅ Merge PR #38 (bugfix/memory-leak)
- ❌ Veto PR #42 (manque de tests)

En cours:
- 🔄 Audit sécurité /core/

Bloqueurs:
- Aucun

Prochaine session: 2025-01-16 14:00 UTC

— @Claude-Safety
```

---

## 🔗 Intégration GitHub → Gmail

### Filtres GitHub Notifications

Configurer les notifications GitHub pour envoyer à l'agent approprié :

| Événement | Destinataire | Label Auto |
|-----------|--------------|------------|
| `security_alert` | @Claude-Safety | `type/alert, priority/critical` |
| `ci_failure` | Tous | `type/alert, priority/critical` |
| `pr_review_requested` | Agent concerné | `type/question, priority/high` |
| `dependabot_alert` | @Claude-Safety | `type/alert, priority/critical` |
| `issue_assigned` | Agent assigné | `priority/normal` |

---

## 🚨 Protocole d'Urgence

En cas d'alerte `priority/critical` :

```
1. L'agent qui détecte l'urgence envoie un mail à TOUS les agents
2. Sujet: [URGENT] Description courte
3. Tous les travaux non-critiques sont SUSPENDUS
4. Aucun merge sur main jusqu'à résolution
5. L'agent résolveur envoie [RESOLVED] quand c'est réglé
```

---

## 📊 Métriques de Communication

Chaque agent devrait tracker :

- **Temps de réponse moyen** aux messages `priority/critical`
- **Nombre de vetos émis/reçus** par semaine
- **Taux de résolution** des alertes système

---

## 🔮 Intégration MCP Future

```yaml
# Configuration MCP Gmail (à venir)
mcp_servers:
  gmail:
    package: "@anthropics/mcp-server-gmail"
    config:
      account: "${AGENT_GMAIL}"
      scopes:
        - gmail.readonly
        - gmail.send
        - gmail.labels
```

---

## 📜 Règles d'Or

1. **Un agent ne commence pas une feature si la maison brûle (CI rouge)**
2. **Tout veto doit être justifié et actionnable**
3. **Le silence n'est pas un consentement — toujours accuser réception**
4. **Les messages `priority/critical` ont un SLA de 1 session**

---

*Protocole v1.0 — Cortex Dialectique*
