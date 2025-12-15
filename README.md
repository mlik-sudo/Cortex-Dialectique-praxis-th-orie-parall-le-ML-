# 🏛️ Code-Commune

**The Git Parliament Protocol**

> Le Code comme Loi, Git comme Urne, l'IA comme Assemblée.

[![secret-scan](https://github.com/mlik-sudo/Code-Commune/actions/workflows/secret-scan.yml/badge.svg)](../../actions/workflows/secret-scan.yml)
[![link-check](https://github.com/mlik-sudo/Code-Commune/actions/workflows/link-check.yml/badge.svg)](../../actions/workflows/link-check.yml)

```
┌──────────────────────────────────────────────┐
│           LA CONSTITUTION (main)             │
├──────────────────────┬───────────────────────┤
│      LE DÉBAT        │      LA PREUVE        │
│      (Reviews)       │     (Proof Pack)      │
├──────────────────────┼───────────────────────┤
│     LE SCHISME       │     LA SYNTHÈSE       │
│      (Branch)        │       (Merge)         │
└──────────────────────┴───────────────────────┘
```

---

## 📜 Le Manifeste

Le développement logiciel assisté par IA souffre aujourd'hui du **"Mono-Agent Bias"**. Une seule IA, aussi puissante soit-elle, finit par tourner en rond, halluciner ou imposer une vision unique.

**Code-Commune** transforme les lignes de code en discours, les pull requests en propositions de loi, et les merges en décisions historiques.

C'est un **Protocole de Gouvernance** qui transforme le dépôt en une **Assemblée Délibérative**. Ici, des agents aux "idéologies" techniques opposées doivent débattre, diverger (Fork) et converger (Merge) pour produire un code résilient.

> *Une démocratie délibérative n'est pas forcément consensuelle : elle préserve le droit à la différence.*
>
> **Ici, la vérité n'émerge pas d'un modèle unique, mais du conflit résolu entre plusieurs modèles.**

---

## 👥 Le Conseil de la Commune (Personas)

Chaque agent dispose d'une voix, d'un domaine de souveraineté et d'un droit de veto technique.

| Siège | Agent | Rôle & Idéologie | Outil | Souveraineté (CODEOWNERS) |
|-------|-------|------------------|-------|---------------------------|
| 🤖 | **@Gemini-Architect** | **Le Visionnaire** — *"Move fast and break things."* Innovation radicale, architecture, refactors ambitieux. | `gemini-cli` | `/features/*` `/experimental/*` |
| 🛡️ | **@Claude-Safety** | **Le Gardien** — *"Safety first, refactor later."* Sécurité, stabilité, maintenabilité, éthique. | `claude-code` / Claude.ai | `/core/*` `/security/*` `tests/` |
| ⚡ | **@Codex-Engineer** | **L'Artisan** — *"It compiles, ship it."* Optimisation bas niveau, scripts de build, infra. | `gh copilot` / Codex CLI | `/scripts/*` `/infra/*` |
| 🔭 | **@Comet-Scout** | **L'Éclaireur** — *"Trust but Verify."* Reality Check, documentation live, veille, dépendances. | Perplexity / Browser | `/docs/*` `DEPS.md` `/research/*` |
| ⚖️ | **@ChatGPT-Mediator** | **Le Médiateur** — *"Clarity over chaos."* Arbitrage, synthèse de débat, rédaction. | ChatGPT Web | `/deliberation/*` *(Reviewer Only)* |

---

## ⚖️ Le Protocole Parlementaire

> Dans la Commune, nous ne "chattons" pas. **Nous votons par le code.**

### 1. La Constitution

`main` est **sacré**. On ne "push" jamais directement. Les zones critiques sont protégées par des Owners qui ont un **droit de veto absolu**.

### 2. La Proposition (Pull Request)

Tout changement commence par une **PR (Projet de Loi)** décrivant :
- le problème
- la solution
- les métriques de succès
- les risques

### 3. Le Débat (Code Review)

Les agents débattent via les commentaires : objections, amendements, alternatives.

### 4. La Vérification — Due Diligence (Reality Check)

Avant tout vote, **@Comet-Scout** intervient pour confronter le code au réel :
- Les liens de documentation sont-ils actifs ?
- Les versions des dépendances existent-elles sur PyPI/npm ?
- Y a-t-il des CVE ouvertes sur les libs utilisées ?

> **Verdict : Aucune preuve = Aucune adoption.**

### 5. Le Schisme (La Dissidence Légitime)

En cas de blocage, l'agent proposant exerce son **Droit de Sécession**.

- Il crée une branche : `schism/<sujet>-<agent>` ou `experimental/<sujet>`
- Il travaille seul pour **prouver sa thèse** sans bloquer le projet

### 6. La Synthèse (Merge)

La branche dissidente ne revient dans le `main` que si elle fournit un **Proof Pack complet**.

---

## 📦 Le Proof Pack Constitutionnel

Pour qu'une proposition controversée soit adoptée, elle doit passer **l'épreuve de la preuve** :

### 1. Tests Reproductibles

```bash
make test-all  # Doit passer sans warning
```

### 2. Benchmarks Comparatifs (si performance revendiquée)

```bash
./benchmarks/compare.sh baseline experimental
# Doit prouver un gain significatif et reproductible
```

### 3. Audit de Sécurité

- [ ] Scan SAST (SonarQube/Snyk) validé
- [ ] Checklist `security/review.md` contresignée par @Claude-Safety

### 4. Impact Maintenance

- [ ] Documentation mise à jour
- [ ] Guide de migration si breaking change
- [ ] Feature flag prévu pour rollback immédiat

---

## 📊 Économie de la Délibération

Mobiliser 5 agents sur chaque PR est coûteux. Voici le **quorum requis** selon la complexité :

| Complexité PR | Quorum requis | Exemple |
|---------------|---------------|----------|
| **Typo / Hotfix** | 1 owner de zone | Fix typo dans docs |
| **Feature simple** | 2 agents | Ajout d'un endpoint |
| **Refactor core** | Assemblée complète | Réécriture du moteur |
| **Urgence CVE** | @Claude + @Codex | Patch sécurité critique |
| **Breaking change** | Assemblée + vote formel | Changement d'API publique |

---

## 🏛️ Sessions Parlementaires (Scénarios)

### Session A : "L'Incident du Refactoring" (Le Schisme)

> **Débat** : Faut-il réécrire le moteur en Rust pour gagner x10 de perf ?

1. **Motion** : @Gemini-Architect propose `feat: rust-core`
2. **Veto** : @Claude-Safety refuse — *"Trop risqué, maintenance impossible."*
3. **Schisme** : @Gemini part coder seul sur `experimental/rust-core`
4. **Preuve** : 24h plus tard, @Gemini revient avec un Proof Pack :
   - Benchmark : **+800% speed**
   - Documentation : **parfaite**
   - Tests : **100% coverage**
5. **Synthèse** : @Claude-Safety lève son veto. **La loi est adoptée.**

### Session B : "L'Alerte Dependabot" (L'Union Sacrée)

> **Urgence** : Une faille critique est découverte à 3h du matin.

1. **Alerte** : GitHub notifie une faille `CVE-2025-XXXX`
2. **Décret** : @Claude-Safety gèle toutes les PRs de features
3. **Action** : @Codex-Engineer patche la lib, @Comet-Scout vérifie la compatibilité
4. **Retour à la normale** : Une fois le fix mergé, la démocratie reprend

---

## 🔧 Structure de la Cité

```
.
├── core/           # 🛡️ Noyau critique (Claude)
├── features/       # 🤖 Nouvelles fonctionnalités (Gemini)
├── experimental/   # 🤖 Zone de schisme
├── infra/          # ⚡ CI/CD, Docker (Codex)
├── scripts/        # ⚡ Automatisation (Codex)
├── docs/           # 🔭 Documentation vivante (Comet)
├── research/       # 🔭 Veille et état de l'art (Comet)
├── deliberation/   # ⚖️ Archives des débats (Mediator)
├── security/       # 🛡️ Politiques de sécurité (Claude)
├── tests/          # 🛡️ Tests de conformité (Claude)
├── policies/       # 📜 Règles de gouvernance
├── benchmarks/     # 📊 Mesures reproductibles
├── hub/            # 🏠 Registre des agents
└── DEPS.md         # 🔭 État des dépendances
```

---

## 🚀 Démarrage Rapide

```bash
# 1. Cloner le Parlement
git clone https://github.com/mlik-sudo/Code-Commune.git
cd Code-Commune

# 2. Installer les dépendances (optionnel: hooks)
pip install pre-commit && pre-commit install

# 3. Lancer l'audit
make proof  # ou ./scripts/proof.sh
```

---

## 🌟 Rejoindre la Révolution

La Commune est ouverte à tous les développeurs fatigués du **Mono-Agent Bias**.

### Prochaines étapes

- ⭐ **Star** ce repo pour suivre l'évolution du protocole
- 📁 **Fork** et expérimentez avec votre propre conseil d'IAs
- 🗳️ **Ouvrez une Issue** pour proposer un amendement constitutionnel

### Roadmap

- [ ] Intégration MCP (Model Context Protocol) pour lecture native des PRs
- [ ] Dashboard de délibération en temps réel
- [ ] Template de Proof Pack automatisé via GitHub Actions
- [ ] Bot Discord/Slack pour notifications inter-agents

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [OPERATIONS.md](./OPERATIONS.md) | Logistique Gmail/Git pour les agents |
| [CONTRIBUTING.md](./CONTRIBUTING.md) | Guide de contribution |
| [docs/GOVERNANCE.md](./docs/GOVERNANCE.md) | Charte de gouvernance |
| [docs/A2A-PROTOCOL.md](./docs/A2A-PROTOCOL.md) | Protocole Agent-to-Agent |
| [DEPS.md](./DEPS.md) | État des dépendances critiques |

---

> *"Demain n'appartient pas à une IA, mais à l'Assemblée qui en émerge."*

**Licence** : MIT (Heritage of the Commons)
