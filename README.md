# Cortex — Dialectique *praxis* ↔ *théorie* (parallèle ML)

> De la **théorie** à l’**expérience** et de l’**expérience** à la **théorie** — en boucle. Ici, « théorie » = **policies/ADR/hypothèses**, « praxis » = **exécution par les agents CLI**.

---

## 1) Mapping conceptuel (raccourci)

| Dialectique ML                | Cortex (Control Plane)                                            | Data Plane / Agents                       |
| ----------------------------- | ----------------------------------------------------------------- | ----------------------------------------- |
| **Théorie**                   | Policies, ADR, hypothèses, objectifs, critères                    | —                                         |
| **Praxis**                    | —                                                                 | Exécution (Gemini, Codex, Claude, Jules)  |
| **Contradictions**            | Conflits métriques (coût vs latence, qualité vs quota), incidents | Erreurs, flakiness, limites contextuelles |
| **Critique / autocritique**   | Revue de résultats, post‑mortems, HITL, débats                    | Logs/artefacts comme preuves              |
| **Synthèse**                  | Mise à jour `routing.yaml`, `budgets.yaml`, choix de drivers, ADR | —                                         |
| **Planification**             | Roadmap, seuils SLO, règles d’escalade/fallback                   | Cron, GH Actions, plan de runs            |
| **Forces productives**        | GPU/CPU/tokens, extensions, MCPs                                  | Capacités des agents                      |
| **Rapports sociaux de prod.** | Gouvernance/RACI, RBAC, conventions                               | Collaboration humano‑agent                |
| **Superstructure**            | Docs, scorecards, dashboards, normes de revue                     | —                                         |

---

## 2) Boucle dialectique de Cortex (7 étapes)

1. **Formuler l’hypothèse** (théorie) : but, métriques cibles, contraintes, risques.
2. **Planifier la praxis** : scénarios/skills, budgets, timebox, seeds, seuils.
3. **Exécuter** (data plane) : dispatch vers agents choisis, collecte artefacts.
4. **Mesurer** : success/p95/cost/retries/flaky, diffs vs baseline.
5. **Critiquer** : revue HITL, objections argumentées, analyse des contradictions.
6. **Synthétiser** : décision **Adopt/Hold/Retire**, MAJ policies/budgets/scorecards.
7. **Institutionnaliser** : ADR + badges + dashboards, et retour à (1).

```mermaid
flowchart LR
  T[Théorie\n(Policies/ADR/Hypothèses)] --> P[Praxis\n(Dispatch vers Agents)] --> M[Mesure\n(Métriques/Artefacts)] --> C[Critique\n(HITL, post‑mortems)] --> S[Synthèse\n(MAJ Policies/ADR)] --> T
```

---

## 3) Protocoles minimaux (pour rester « evidence‑based »)

* **Chaque proposition** doit inclure : hypothèse, métriques d’acceptation, budget/timeout, risques, plan de rollback.
* **Chaque critique** : objection **référencée** (logs, métriques, texte/commit), alternative testable.
* **Chaque synthèse** : décision + **∆** mesuré (avant/après) + MAJ explicites des fichiers (`policies/*`, scorecards, ADR).

**Checklist** (à coller dans les issues/PR) :

* [ ] Hypothèse & succès mesurable
* [ ] Plan d’essai (scénarios/skills)
* [ ] Budget/timeout & risques
* [ ] Résultats vs baseline
* [ ] Décision + ADR + MAJ policies
* [ ] Badges/Dashboards mis à jour

---

## 4) Anti‑patterns (à éviter)

* **Dogmatisme** : changer policies sans preuve empirique (∆ non mesuré).
* **Sur‑adaptation locale** : optimiser un skill au détriment des autres (déplacer le problème).
* **Churn de policies** : réécrire trop souvent sans consolidation (instabilité).
* **HITL opaque** : overrides non tracés → pas de reproductibilité.

---

## 5) Garde‑fous (conception)

* **Policy‑as‑code** versionné + contrôle de changements (2 reviewers : Owner + SecEng).
* **Seuils de preuve** : tailles d’effet min., niveaux de confiance, paliers d’adoption.
* **Canary & rollback** systématiques pour décisions à large impact.
* **Observabilité** : métriques uniformes, badges auto, exports Prometheus.

---

## 6) Glossaire pont

* **Praxis** → exécution mesurée par les agents.
* **Théorie** → policies/ADR définissant le « pourquoi/comment ».
* **Contradiction** → tension métrique (qualité vs coût, latence vs budget).
* **Synthèse** → nouvelle politique qui réconcilie la tension **avec preuve**.

---

## 7) Taglines candidates

* *De la théorie à la praxis — et retour (en preuves).*
* *Observe • Débat • Synthétise • Agit • Apprend.*
* *Dialectic Control Plane for Multi‑Agent Workflows.*

---

## 8) Dashboards & Badges

| Service           | Status                                                                    |
| ----------------- | ------------------------------------------------------------------------- |
| **Nightly Bench** | ![Nightly Benchmark Status](dashboards/badges/nightly_status.svg) |
