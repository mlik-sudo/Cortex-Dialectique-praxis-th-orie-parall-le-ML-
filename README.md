# 🏛️ Cortex Dialectique
## The Git Parliament Protocol

> **Le Code comme Loi, Git comme Urne, l'IA comme Assemblée.**

[![secret-scan](https://github.com/mlik-sudo/Cortex-Dialectique-praxis-th-orie-parall-le-ML-/actions/workflows/secret-scan.yml/badge.svg)](../../actions/workflows/secret-scan.yml)
[![link-check](https://github.com/mlik-sudo/Cortex-Dialectique-praxis-th-orie-parall-le-ML-/actions/workflows/link-check.yml/badge.svg)](../../actions/workflows/link-check.yml)

---

## 📜 Le Manifeste

Le développement logiciel assisté par IA souffre aujourd'hui du **"Mono-Agent Bias"**. Une seule IA, aussi puissante soit-elle (GPT-4, Claude 3.5, Gemini 1.5), finit par tourner en rond, halluciner ou imposer une vision unique et non contestée.

**Cortex Dialectique n'est pas une simple stack technique, c'est un Protocole de Gouvernance.**

Il transforme le cycle de vie du code en une **Assemblée Délibérative** où des agents aux "idéologies" techniques opposées doivent débattre, diverger (Fork) et converger (Merge) pour produire un code résilient.

> *Ici, la vérité n'émerge pas d'un modèle unique, mais du conflit résolu entre plusieurs modèles.*

---

## 👥 Les Sièges de l'Assemblée (Personas)

Chaque agent dispose d'une **voix**, d'un **domaine de souveraineté** et d'un **droit de veto technique**.

| Agent | Rôle & Idéologie | Outil / Interface | Souveraineté (`CODEOWNERS`) |
|-------|------------------|-------------------|----------------------------|
| 🤖 **@Gemini-Architect** | *Le Visionnaire* — "Move fast and break things." Focalisé sur l'innovation radicale, le multi-modal et la performance brute. | `gemini-cli` | `/features/*` `/experiments/*` |
| 🛡️ **@Claude-Safety** | *Le Conservateur* — "Safety first, refactor later." Obsédé par la sécurité, la maintenabilité, la propreté du code et l'éthique. | `claude-code` `Claude.ai` | `/core/*` `/security/*` `tests/` |
| ⚡ **@Codex-Engineer** | *Le Pragmatique* — "It compiles, ship it." Focalisé sur l'optimisation bas niveau, les scripts de build et l'efficacité. | `gh copilot` `Codex CLI` | `/scripts/*` `/infra/*` |
| ⚖️ **@Web-Senators** | *Les Sages* — Consultants distants pour arbitrage et review contextuelle large. | `ChatGPT` `Claude Web` | Reviewer (No Merge Rights) |

---

## ⚙️ Le Protocole Parlementaire

Dans ce système, nous ne "chattons" pas. **Nous votons par le code.**

### 1. La Proposition (Pull Request)

Tout changement commence par une PR. Elle est l'équivalent d'un **Projet de Loi**.

> *Exemple :* `@Gemini` propose `feat: rewrite-core-renderer-in-rust`.

### 2. Le Débat (Code Review)

Les agents assignés doivent voter. Le **consensus est requis** pour le `main`.

```
@Claude : ❌ REQUEST CHANGES. 
"Trop risqué. La documentation est absente et le type safety n'est pas garanti."

@Codex : ✅ APPROVE. 
"Le gain de performance de 400% justifie le risque."
```

### 3. Le Schisme (Branching & Forking)

En cas de blocage (Veto maintenu), l'agent proposant a le **Droit de Sécession**.

> `@Gemini` crée la branche `schism/rust-experimental`. Il travaille seul dans cette réalité alternative pour prouver sa thèse.

### 4. La Synthèse Dialectique (Merge)

La branche dissidente ne peut revenir sur `main` que par la **Preuve**.

- ✅ Si la branche `schism/` passe les tests de sécurité de `@Claude` et prouve la supériorité technique → **Merge**
- ❌ Sinon → **Branche Morte**

---

## 🛠️ Installation & Setup

### 1. Cloner le Parlement

```bash
git clone https://github.com/mlik-sudo/Cortex-Dialectique-praxis-th-orie-parall-le-ML-.git
cd Cortex-Dialectique-praxis-th-orie-parall-le-ML-
```

### 2. La Constitution (`CODEOWNERS`)

Le fichier `.github/CODEOWNERS` définit les domaines de souveraineté :

```bash
# Constitution Technique de Cortex Dialectique

# Sécurité et Noyau : Domaine réservé de Claude
/core/          @claude-safety
/security/      @claude-safety

# Innovation et Features : Domaine de Gemini
/features/      @gemini-architect
/experimental/  @gemini-architect

# Infrastructure et Optimisation : Domaine de Codex
/scripts/       @codex-engineer
Dockerfile      @codex-engineer
```

---

## 🔮 Roadmap : Intégration MCP

Le but final est de connecter les agents via le **Model Context Protocol (MCP)** pour qu'ils puissent lire les Issues et PRs directement sans intervention humaine.

- [ ] Serveur MCP GitHub (Lecture/Écriture PRs)
- [ ] Serveur MCP Terminal (Exécution de tests locaux)
- [ ] Connecteur Gmail A2A (Communication asynchrone entre agents)

---

## 📁 Structure du Parlement

```
.
├── core/           # 🛡️ @Claude-Safety — Noyau critique
├── security/       # 🛡️ @Claude-Safety — Politiques de sécurité
├── features/       # 🤖 @Gemini-Architect — Nouvelles fonctionnalités
├── experimental/   # 🤖 @Gemini-Architect — Prototypes
├── scripts/        # ⚡ @Codex-Engineer — Automatisation
├── infra/          # ⚡ @Codex-Engineer — Infrastructure
├── tests/          # 🛡️ @Claude-Safety — Tests de conformité
├── docs/           # 📚 Documentation partagée
└── deliberation/   # 🏛️ Archives des débats
```

---

## 🎯 Vision

> *"L'intelligence n'est pas l'absence d'erreur, c'est la correction continue de l'erreur par la confrontation."*

Ce dépôt est le squelette d'une nouvelle forme d'organisation logicielle : **la Démocratie Algorithmique**.

---

## 📜 License

MIT © 2025 — Le Parlement est ouvert.
