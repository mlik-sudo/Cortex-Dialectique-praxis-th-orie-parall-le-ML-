# 🛡️ Security Review Checklist (Claude-Safety)

Ce document sert de **contresignature sécurité** pour le Proof Pack.
Toute PR qui modifie la surface d'attaque, les dépendances, l'I/O, le réseau, la sérialisation, ou l'exécution de code **doit** passer cette checklist.

**PR :** <!-- lien -->
**Auteur :** <!-- @agent -->
**Reviewers (sécurité) :** <!-- @Claude-Safety, etc -->
**Scope :** <!-- core/features/infra/etc -->
**Risque estimé :** Low / Medium / High
**Date :** <!-- YYYY-MM-DD -->

---

## 0) Résumé de la menace
- Actifs à protéger :
- Menaces principales :
- Hypothèses / trust boundaries :
- Dépendances externes (services, APIs, OS) :

**Evidence (obligatoire) :**
- Lien PR + description du changement :
- Lien CI (run) :

---

## 1) Surface d'attaque
Coche si applicable.

- [ ] Entrées utilisateur (CLI/API/UI) ajoutées/modifiées
- [ ] Fichiers lus/écrits (paths, permissions) ajoutés/modifiés
- [ ] Réseau (HTTP, sockets) ajouté/modifié
- [ ] Sérialisation / parsing (JSON/YAML/XML/pickle/Proto) ajouté/modifié
- [ ] Exécution de code / plugins / templates / shell ajouté/modifié
- [ ] Concurrence / async / threads modifiés
- [ ] Intégration OS (Windows/macOS/Linux) ajoutée/modifiée
- [ ] Crypto / auth / secrets ajoutés/modifiés

**Notes :**
<!-- -->

**Evidence (si coché) :**
- Entrées / endpoints / flags impactés :
- Exemple d'inputs (valide + malformé) :
- Chemins/URLs touchés :

---

## 2) Dépendances & supply chain
- [ ] Nouvelles dépendances justifiées (raison + alternative)
- [ ] Versions pin / lockfile à jour (si applicable)
- [ ] Dépendances non maintenues/archivées : **NON**
- [ ] Licence compatible
- [ ] Scan dépendances OK (outil + lien/log) :
  - Outil : <!-- Dependabot/Snyk/etc -->
  - Résultat : <!-- OK / issues -->
- [ ] Actions GitHub utilisées : versions contrôlées (au minimum major pin, idéalement SHA)

**Evidence :**
- Diff `requirements*.txt` / `pyproject.toml` / lockfile (si applicable) :
- Lien Dependabot (si applicable) :
- Lien scan (log/rapport) :

---

## 3) Secrets & données sensibles
- [ ] Aucun secret commité (clés, tokens, .env, credentials)
- [ ] Variables d'environnement documentées (si utilisées)
- [ ] Journaux (logs) ne leak pas de données sensibles (redaction obligatoire avant archivage)
- [ ] Données perso / PII : collecte ? stockage ? (si oui → documenter + minimiser)

**Evidence :**
- Résultats `detect-secrets` / `gitleaks` (lien CI) :
- Exemple de logs vérifiés (ou justification) :

---

## 4) Validation d'entrées & erreurs
- [ ] Validation stricte des entrées (types, taille, formats)
- [ ] Gestion d'erreurs sûre (pas de fallback silencieux dangereux)
- [ ] Messages d'erreur ne révèlent pas d'infos sensibles
- [ ] Timeouts / limites (rate limit / taille fichier / mémoire) si nécessaire

**Evidence :**
- Tests ajoutés (cas limites) :
- Stratégie de timeouts/limites (où ? valeur ?) :

---

## 5) I/O & filesystem
- [ ] Pas de path traversal (`../`) possible
- [ ] Pas d'écriture dans des chemins arbitraires sans contrôle
- [ ] Permissions minimales (principe du moindre privilège)
- [ ] Nettoyage fichiers temporaires / permissions correctes

**Evidence :**
- Liste des chemins autorisés (si applicable) :
- Tests/contrôles contre traversal :

---

## 6) Réseau & intégrations externes (si applicable)
- [ ] TLS/HTTPS obligatoire
- [ ] Vérification certificats activée
- [ ] Timeouts configurés
- [ ] Retries raisonnables (pas de boucle infinie)
- [ ] URLs/hosts allowlist si pertinent
- [ ] Données envoyées minimisées

**Evidence :**
- Hosts/URLs contactés :
- Timeouts/retries configurés :

---

## 7) Exécution de commandes (si applicable)
- [ ] Aucun `shell=True` non nécessaire
- [ ] Arguments passés en liste (pas de concat strings)
- [ ] Échappement / validation des paramètres
- [ ] Pas de commande construite depuis input non fiable

**Evidence :**
- Appels `subprocess`/shell identifiés :
- Exemple d'input non-fiable neutralisé :

---

## 8) CI / GitHub Actions (si la PR touche `.github/workflows/*` ou scripts CI)
- [ ] Permissions minimales (`permissions:` explicite, pas de `write` par défaut)
- [ ] Pas d'usage de `pull_request_target` (sauf justification + durcissement)
- [ ] Pas d'exécution de code non-fiable sur PRs externes
- [ ] Actions tierces : versions contrôlées + revue

**Evidence :**
- Lien vers le workflow modifié + justification des permissions :

---

## 9) Agents / LLM (si applicable)
- [ ] Frontières de confiance explicites entre agents (pas de “zero trust” implicite)
- [ ] Protection contre prompt injection (entrées non-fiables, contenu externe)
- [ ] Aucune exfiltration de secrets via logs/artefacts/outputs

**Evidence :**
- Sources non-fiables identifiées (URLs, issues, PR body, fichiers) :
- Mesures de mitigation :

---

## 10) Tests sécurité (minimum)
- [ ] Tests ajoutés pour le comportement sûr (cas limites, erreurs)
- [ ] Cas d'abus testé (inputs malformés, grands volumes)
- [ ] Reproductibilité : tests passent en CI

**Evidence :**
- Commandes + lien CI :

---

## 11) Décision (contresignature)
Verdict :
- [ ] ✅ APPROVED (safe to merge)
- [ ] 🟡 APPROVED WITH CONDITIONS (voir ci-dessous)
- [ ] ❌ VETO (bloquant)

Conditions / remarques :
<!-- -->

Signature :
- **@Claude-Safety** : <!-- date / nom -->
