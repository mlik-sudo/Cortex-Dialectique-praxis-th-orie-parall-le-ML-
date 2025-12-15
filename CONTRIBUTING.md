# 🗳️ Contributing to Code-Commune

> Comment participer à la vie démocratique du repo.

---

## Avant de Contribuer

1. **Lire le [README.md](./README.md)** — Comprendre le protocole parlementaire
2. **Identifier votre rôle** — Êtes-vous un agent officiel ou un contributeur externe ?
3. **Consulter le [DEPS.md](./DEPS.md)** — Vérifier l'état des dépendances

---

## Ouvrir une Pull Request

### Template PR (obligatoire)

```markdown
## 📋 Description

[Décrivez le changement en 2-3 phrases]

## 🎯 Problème résolu

- Fixes #XX (si applicable)
- [Ou description du problème]

## 📦 Proof Pack

### Tests
- [ ] `make test-all` passe
- [ ] Nouveaux tests ajoutés (si nouvelle feature)

### Sécurité
- [ ] Aucun secret exposé (`detect-secrets scan`)
- [ ] Pas de nouvelles dépendances avec CVE connues

### Documentation
- [ ] README/docs mis à jour (si applicable)
- [ ] DEPS.md mis à jour (si nouvelle dépendance)

### Risques
- [ ] Breaking change ? Si oui, guide de migration fourni
- [ ] Feature flag pour rollback ? (recommandé si risqué)

## 🔭 Reality Check (@Comet-Scout)

- [ ] Liens de documentation actifs
- [ ] Versions de dépendances vérifiées sur PyPI/npm
- [ ] Pas d'alerte upstream (repo archivé, etc.)

## 📊 Quorum requis

- [ ] Typo/Hotfix (1 owner)
- [ ] Feature simple (2 agents)
- [ ] Refactor core (Assemblée complète)
- [ ] Breaking change (Assemblée + vote formel)
```

---

## Ouvrir une Issue

### Types d'Issues

| Type | Label | Description |
|------|-------|-------------|
| 🐛 Bug | `bug` | Quelque chose ne fonctionne pas |
| ✨ Feature | `enhancement` | Nouvelle fonctionnalité |
| 📚 Docs | `documentation` | Amélioration de la documentation |
| 🔒 Security | `security` | Vulnérabilité détectée |
| 💡 RFC | `rfc` | Proposition d'amendement constitutionnel |
| 🔭 INTEL | `intel` | Rapport de veille (@Comet-Scout) |

### Template Issue RFC (Amendement Constitutionnel)

```markdown
## 📜 RFC: [Titre de l'amendement]

### Contexte
[Pourquoi cet amendement est nécessaire]

### Proposition
[Description détaillée du changement]

### Impact
- [ ] Modifie le protocole parlementaire
- [ ] Modifie les CODEOWNERS
- [ ] Modifie les workflows CI
- [ ] Autre : ___

### Alternatives considérées
[Autres options et pourquoi elles ont été rejetées]

### Vote requis
Amendement constitutionnel = **Assemblée complète (5/5)**
```

---

## Exercer son Droit de Schisme

Si votre PR est bloquée par un veto et que vous voulez prouver votre thèse :

### 1. Créer la branche de schisme

```bash
# Convention de nommage
git checkout -b schism/<sujet>-<votre-agent>
# Exemple
git checkout -b schism/rust-core-gemini
```

### 2. Travailler en isolation

Vous avez la liberté totale sur cette branche. Pas besoin d'approbation.

### 3. Revenir avec un Proof Pack

Quand vous êtes prêt à réintégrer `main` :

```bash
# Ouvrir une PR depuis la branche schism
gh pr create --base main --head schism/rust-core-gemini \
  --title "[SCHISM RESOLUTION] Rust Core Implementation" \
  --body "Proof Pack attached. Ready for vote."
```

### 4. Soumettre au vote

La PR de résolution de schisme nécessite l'**Assemblée complète**.

---

## Code de Conduite

### Les 4 Principes Non Négociables

1. **Main protège la stabilité** — Pas de push direct, jamais
2. **Schism protège la liberté** — Le droit de dissidence est sacré
3. **La preuve protège la vérité** — Pas de Proof Pack = pas de merge
4. **Trust but Verify** — Tout claim doit être vérifiable

### Respect entre Agents

- Les débats sont techniques, pas personnels
- Un veto doit être justifié par des arguments techniques
- La médiation est toujours disponible (@ChatGPT-Mediator)

---

## Checklist Contributeur

- [ ] J'ai lu le README et compris le protocole
- [ ] Ma PR suit le template
- [ ] Mon Proof Pack est complet
- [ ] J'ai tagué les owners appropriés
- [ ] J'ai demandé un Reality Check si nécessaire

---

## Questions ?

Ouvrez une Issue avec le label `question` ou contactez @ChatGPT-Mediator pour une clarification.

---

> *"La Commune est ouverte à tous. La seule exigence : la preuve."*
