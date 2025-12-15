---
project: code-commune
owner: claude-safety
reviewed: 2025-12-15
---

# 📧 Guide de Configuration Gmail
## Setup des Canaux Agents

> **Checklist complète pour créer et configurer les boîtes Gmail de la Commune.**

---

## 🎯 Vue d'Ensemble

Chaque agent IA dispose de son propre canal Gmail qui sert de :
- **Boîte de réception A2A** — Messages des autres agents
- **Hub de notifications** — Alertes GitHub
- **Mémoire externe** — Archive des décisions

---

## 📋 Étape 1 : Création des Comptes

### Comptes à Créer

| Agent | Email Suggéré | Mot de passe |
|-------|---------------|--------------|
| 🛡️ Claude-Safety | `claude.safety.codecommune@gmail.com` | Stocker dans gestionnaire sécurisé |
| 🤖 Gemini-Architect | `gemini.architect.codecommune@gmail.com` | Stocker dans gestionnaire sécurisé |
| ⚡ Codex-Engineer | `codex.engineer.codecommune@gmail.com` | Stocker dans gestionnaire sécurisé |

### Informations de Profil

Pour chaque compte :
```
Prénom: [Nom de l'Agent]
Nom: Code-Commune
Photo: Avatar distinctif par agent (optionnel)
```

---

## 🏷️ Étape 2 : Configuration des Labels

### Créer ces labels dans chaque compte :

```
📁 Labels Gmail à créer
│
├── priority/
│   ├── critical    (Rouge)
│   ├── high        (Orange)
│   ├── normal      (Bleu)
│   └── low         (Gris)
│
├── type/
│   ├── veto        (Rouge foncé)
│   ├── approval    (Vert)
│   ├── question    (Violet)
│   ├── alert       (Jaune)
│   ├── sync        (Cyan)
│   └── handoff     (Bleu foncé)
│
├── status/
│   ├── pending     (Orange clair)
│   ├── acknowledged (Bleu clair)
│   └── resolved    (Vert clair)
│
├── source/
│   ├── github      (Noir)
│   ├── agent-claude (Violet)
│   ├── agent-gemini (Bleu)
│   └── agent-codex  (Vert)
│
└── archive/
    └── decisions   (Gris)
```

---

## 🔧 Étape 3 : Filtres Automatiques

### Filtre 1 : Alertes GitHub Critiques

```
Correspond à: from:(notifications@github.com) ("security" OR "critical" OR "failure")
Action:
  - Appliquer le label: priority/critical
  - Appliquer le label: type/alert
  - Appliquer le label: source/github
  - Ne jamais envoyer dans les spams
  - Toujours marquer comme important
```

### Filtre 2 : Messages Veto

```
Correspond à: subject:([VETO])
Action:
  - Appliquer le label: type/veto
  - Appliquer le label: priority/critical
  - Marquer comme important
```

### Filtre 3 : Messages des Autres Agents

```
# Pour le compte de Claude :
Correspond à: from:(gemini.architect.codecommune@gmail.com OR codex.engineer.codecommune@gmail.com)
Action:
  - Appliquer le label: source/agent-gemini OU source/agent-codex
  - Ne jamais envoyer dans les spams

# Répéter pour chaque agent avec les bons expéditeurs
```

### Filtre 4 : CI Failures

```
Correspond à: from:(notifications@github.com) subject:(failed OR failure)
Action:
  - Appliquer le label: priority/critical
  - Appliquer le label: type/alert
```

### Filtre 5 : Dependabot

```
Correspond à: from:(dependabot) OR subject:(dependabot)
Action:
  - Appliquer le label: type/alert
  - Appliquer le label: source/github
```

---

## 🔔 Étape 4 : Configuration GitHub Notifications

### Dans GitHub → Settings → Notifications :

1. **Email notifications** : Activer
2. **Email address** : Mettre l'email de l'agent concerné
3. **Watching** : Notifications pour le repo Code-Commune

### Notifications par CODEOWNERS :

| Domaine | Agent notifié |
|---------|---------------|
| `/core/*`, `/security/*`, `tests/` | claude.safety.codecommune@gmail.com |
| `/features/*`, `/experimental/*` | gemini.architect.codecommune@gmail.com |
| `/scripts/*`, `/infra/*` | codex.engineer.codecommune@gmail.com |

---

## 🔐 Étape 5 : Sécurité & Accès API

### Activer l'accès API (pour MCP futur)

1. Aller dans **Google Cloud Console**
2. Créer un projet `code-commune-agents`
3. Activer **Gmail API**
4. Créer des **OAuth 2.0 credentials**
5. Télécharger le fichier `credentials.json`

### Stocker les credentials

```bash
# Structure recommandée (NE PAS COMMIT)
~/.code-commune-secrets/
├── claude-safety/
│   ├── credentials.json
│   └── token.json
├── gemini-architect/
│   ├── credentials.json
│   └── token.json
└── codex-engineer/
    ├── credentials.json
    └── token.json
```

### Variables d'environnement

```bash
# .env (NE PAS COMMIT)
CLAUDE_GMAIL_CREDENTIALS=~/.code-commune-secrets/claude-safety/credentials.json
GEMINI_GMAIL_CREDENTIALS=~/.code-commune-secrets/gemini-architect/credentials.json
CODEX_GMAIL_CREDENTIALS=~/.code-commune-secrets/codex-engineer/credentials.json
```

---

## ✅ Étape 6 : Vérification

### Checklist Post-Setup

Pour chaque compte Gmail :

- [ ] Compte créé et accessible
- [ ] Labels créés avec les bonnes couleurs
- [ ] Filtres configurés et testés
- [ ] Notifications GitHub redirigées
- [ ] 2FA activé
- [ ] Accès API configuré (si MCP prévu)
- [ ] Mot de passe stocké de manière sécurisée

### Test de Communication

1. Envoyer un mail test de `claude.safety.codecommune` vers `gemini.architect.codecommune`
2. Vérifier que les labels s'appliquent correctement
3. Vérifier que le mail n'est pas dans les spams

---

## 📊 Maintenance

### Hebdomadaire
- Vérifier les mails non lus `priority/critical`
- Archiver les messages `status/resolved` de plus de 7 jours

### Mensuelle
- Revoir les filtres et ajuster si nécessaire
- Vérifier les quotas API Gmail
- Backup des archives importantes

---

## 🔗 Liens Utiles

- [Gmail API Documentation](https://developers.google.com/gmail/api)
- [MCP Server Gmail](https://github.com/modelcontextprotocol/servers) (quand disponible)- [Google Cloud Console](https://console.cloud.google.com/)

---

*Guide v1.0 — Code-Commune*
