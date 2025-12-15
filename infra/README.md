# ⚡ /infra/ — Domaine de @Codex-Engineer

> "It compiles, ship it."

## Souveraineté

Ce dossier contient l'**infrastructure** et la configuration de déploiement.

Toute modification passe par **@Codex-Engineer**, le Pragmatique.

## Contenu

- `docker/` - Images et Compose files
- `k8s/` - Manifests Kubernetes
- `terraform/` - Infrastructure as Code
- `ci/` - Pipelines CI/CD

## Principes

1. **Reproductibilité** - Même config = même résultat
2. **Idempotence** - Réexécuter ne casse rien
3. **Secrets isolés** - Jamais en dur
4. **Logs structurés** - JSON, pas de printf

## Processus

1. Créer une PR avec le prefix `infra:`
2. Tests en staging obligatoires
3. Rollback documenté pour chaque changement
