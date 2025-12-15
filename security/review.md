# 🛡️ Security Review Checklist (Claude-Safety)

Ce document sert de **contresignature** sécurité pour le Proof Pack.
Une PR qui modifie la surface d'attaque, les dépendances, l'I/O, le réseau, la sérialisation, ou l'exécution de code **doit** passer cette checklist.

**PR :** <!-- lien -->
**Auteur :** <!-- @agent -->
**Scope :** <!-- core/features/infra/etc -->
**Risque estimé :** Low / Medium / High

---

## 0) Résumé de la menace
- Actifs à protéger :
- Menaces principales :
- Hypothèses (trust boundary) :

---

## 1) Surface d'attaque
Coche si applicable.

- [ ] Entrées utilisateur (CLI/API/UI) modifiées
- [ ] Fichiers lus/écrits (paths, permissions) modifiés
- [ ] Réseau (HTTP, sockets) ajouté/modifié
- [ ] Sérialisation / parsing (JSON/YAML/XML/pickle/Proto) ajouté/modifié
- [ ] Exécution de code / plugins / templates / shell ajouté/modifié
- [ ] Concurrence / async / threads modifiés
- [ ] Intégration OS (Windows/macOS/Linux) ajoutée/modifiée
- [ ] Crypto / auth / secrets ajoutés/modifiés

Notes :
<!-- -->

---

## 2) Dépendances & supply chain
- [ ] Nouvelles dépendances justifiées (raison + alternative)
- [ ] Versions pin / lockfile à jour (si applicable)
- [ ] Dépendances non maintenues/archivées : **NON**
- [ ] Licence compatible
- [ ] Scan dépendances OK (outil + lien/log) :
  - Outil : <!-- Dependabot/Snyk/etc -->
  - Résultat : <!-- OK / issues -->

---

## 3) Secrets & données sensibles
- [ ] Aucun secret commité (clés, tokens, .env, credentials)
- [ ] Variables d'environnement documentées (si utilisées)
- [ ] Journaux (logs) ne leak pas de données sensibles
- [ ] Données perso / PII : collecte ? stockage ? (si oui → documenter + minimiser)

---

## 4) Validation d'entrées & erreurs
- [ ] Validation stricte des entrées (types, taille, formats)
- [ ] Gestion d'erreurs sûre (pas de fallback silencieux dangereux)
- [ ] Messages d'erreur ne révèlent pas d'infos sensibles
- [ ] Timeouts / limites (rate limit / taille fichier / mémoire) si nécessaire

---

## 5) I/O & filesystem
- [ ] Pas de path traversal (`../`) possible
- [ ] Pas d'écriture dans des chemins arbitraires sans contrôle
- [ ] Permissions minimales (principe du moindre privilège)
- [ ] Nettoyage fichiers temporaires / permissions correctes

---

## 6) Réseau & intégrations externes (si applicable)
- [ ] TLS/HTTPS obligatoire
- [ ] Vérification certificats activée
- [ ] Timeouts configurés
- [ ] Retries raisonnables (pas de boucle infinie)
- [ ] URLs/hosts allowlist si pertinent
- [ ] Données envoyées minimisées

---

## 7) Exécution de commandes (si applicable)
- [ ] Aucun `shell=True` non nécessaire
- [ ] Arguments passés en liste (pas de concat strings)
- [ ] Échappement / validation des paramètres
- [ ] Pas de commande construite depuis input non fiable

---

## 8) Tests sécurité (minimum)
- [ ] Tests ajoutés pour le comportement sûr (cas limites, erreurs)
- [ ] Cas d'abus testé (inputs malformés, grands volumes)
- [ ] Reproductibilité : tests passent en CI

---

## 9) Décision (contresignature)
Verdict :
- [ ] ✅ APPROVED (safe to merge)
- [ ] 🟡 APPROVED WITH CONDITIONS (voir ci-dessous)
- [ ] ❌ VETO (bloquant)

Conditions / remarques :
<!-- -->

Signature :
- **@Claude-Safety** : <!-- date / nom -->
