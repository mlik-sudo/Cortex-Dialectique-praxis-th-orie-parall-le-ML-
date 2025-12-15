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

> 📋 **Voir le [Registre des Agents](hub/AGENT-REGISTRY.md)** pour les fiches complètes et contacts.

---

## ⚙️ Le Protocole Parlementaire

Dans ce système, nous ne "chattons" pas. **Nous votons par le code.**

### 0. Le Standup Asynchrone (Boot Sequence)

Avant toute interaction avec le code, l'agent **DOIT** consulter son canal Gmail dédié.

1. **Sync Camarades (A2A)** : Lire les directives ou vetos posés par les autres agents durant la période d'inactivité.
   - *Exemple : "Gemini, j'ai lu ton mail sur Rust, je prépare une contre-proposition."*
2. **Sync Infrastructure (GitHub Notifications)** : Priorité absolue aux alertes `security` et `ci-failure`.
   - *Règle d'Or :* "Un agent ne commence pas une feature si la maison brûle (CI rouge)."

> 📬 **Voir le [Protocole A2A](docs/A2A-PROTOCOL.md)** pour les formats de messages et labels.

#### 🚀 Scénario : "L'Alerte Dependabot"

Imaginez la scène :

- **3h00 (Matin)** : GitHub détecte une faille critique dans une librairie Python. Il envoie un mail.
- **8h00** : Vous activez `@Claude-Safety`.
- **Boot Sequence** : Claude checke Gmail. Il voit "Critical Severity" (Dependabot).
- **Action Immédiate** : Au lieu de travailler sur sa tâche prévue, il ouvre une Issue : `HOTFIX: Update pandas immediately`.
- **Communication A2A** : Il envoie un mail à `@Gemini` :

> *"Arrête tes devs sur la branche features. Je dois update les dépendances. Ne pushez rien avant mon feu vert."*

**C'est vivant. C'est coordonné. C'est pro.**

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

Le fichier `.github/CODEOWNERS` définit les domaines de souveraineté.

> Note: `CODEOWNERS` doit référencer des comptes/teams GitHub réels. Les noms d'agents ci-dessus sont des personas.

```bash
# Constitution Technique de Cortex Dialectique (exemple)

# Sécurité et Noyau : Domaine "Claude"
/core/          @mlik-sudo
/security/      @mlik-sudo

# Innovation et Features : Domaine "Gemini"
/features/      @mlik-sudo
/experimental/  @mlik-sudo

# Infrastructure et Optimisation : Domaine "Codex"
/scripts/       @mlik-sudo
/infra/         @mlik-sudo
Dockerfile      @mlik-sudo
```

### 3. Configuration Gmail (Canaux A2A)

> 📧 **Voir le [Guide Setup Gmail](docs/GMAIL-SETUP.md)** pour la configuration complète.

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [Protocole A2A](docs/A2A-PROTOCOL.md) | Communication asynchrone entre agents via Gmail |
| [Guide Setup Gmail](docs/GMAIL-SETUP.md) | Configuration des comptes et filtres Gmail |
| [Registre des Agents](hub/AGENT-REGISTRY.md) | Fiches complètes des agents et contacts |
| [CODEOWNERS](.github/CODEOWNERS) | Constitution technique (domaines de souveraineté) |
| [Policies](policies/README.md) | Règles (routing/budgets/limits) |

---

## 🔮 Roadmap : Intégration MCP

Le but final est de connecter les agents via le **Model Context Protocol (MCP)** pour qu'ils puissent lire les Issues et PRs directement sans intervention humaine.

- [ ] Serveur MCP GitHub (Lecture/Écriture PRs)
- [ ] Serveur MCP Terminal (Exécution de tests locaux)
- [x] Connecteur Gmail A2A (Communication asynchrone entre agents) — *Documenté*

---

## 📁 Structure du Parlement

```
.
├── core/           # 🛡️ @Claude-Safety — Noyau critique
├── security/       # 🛡️ @Claude-Safety — Politiques de sécurité
├── policies/       # 📜 Théorie — rules/routing/budgets
├── features/       # 🤖 @Gemini-Architect — Nouvelles fonctionnalités
├── experimental/   # 🤖 @Gemini-Architect — Prototypes
├── scripts/        # ⚡ @Codex-Engineer — Automatisation locale
├── infra/          # ⚡ @Codex-Engineer — Infrastructure
├── tests/          # 🛡️ @Claude-Safety — Tests de conformité
├── docs/           # 📚 Documentation (A2A, Gmail, etc.)
├── hub/            # 🏛️ Registre des agents et outils partagés
├── project-space/  # 🧪 Praxis — benchmarks, dashboards, résultats
└── deliberation/   # 🗳️ Archives des débats
```

---

## 🎯 Vision

> *"L'intelligence n'est pas l'absence d'erreur, c'est la correction continue de l'erreur par la confrontation."*

Ce dépôt est le squelette d'une nouvelle forme d'organisation logicielle : **la Démocratie Algorithmique**.

---

## 📜 License

MIT © 2025 — Le Parlement est ouvert.
