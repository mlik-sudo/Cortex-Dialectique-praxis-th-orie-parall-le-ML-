#!/usr/bin/env bash
# 🔭 @Comet-Scout - Vérification des dépendances
set -euo pipefail

echo "  📋 Lecture de DEPS.md..."

if [ ! -f DEPS.md ]; then
    echo "  ❌ DEPS.md non trouvé!"
    exit 1
fi

# Compte les dépendances documentées
DEP_COUNT=$(grep -c "^|" DEPS.md 2>/dev/null || echo "0")
echo "  📦 $DEP_COUNT entrées dans DEPS.md"

# Vérifie que requirements existe si mentionné
if [ -f requirements.txt ] || [ -f requirements-dev.txt ]; then
    echo "  ✅ Fichiers requirements présents"
else
    echo "  ℹ️  Pas de requirements.txt (normal si pas de Python)"
fi

echo "  ✅ Vérification des dépendances terminée"
