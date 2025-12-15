#!/usr/bin/env bash
# 🛡️ @Claude-Safety - Scan de sécurité basique
set -euo pipefail

echo "  🔐 Scan de sécurité en cours..."

# 1. Vérifie les secrets avec detect-secrets si disponible
if command -v detect-secrets >/dev/null 2>&1; then
    echo "  🔍 detect-secrets scan..."
    detect-secrets scan --baseline .secrets.baseline 2>/dev/null || true
fi

# 2. Vérifie les patterns dangereux basiques
echo "  🔍 Recherche de patterns sensibles..."
Dangerous_patterns="password=|api_key=|secret_key=|AWS_SECRET|PRIVATE_KEY"
if grep -rniE "$Dangerous_patterns" --include="*.py" --include="*.js" --include="*.ts" --include="*.env.example" . 2>/dev/null | grep -v node_modules | grep -v ".git" | head -3; then
    echo "  ⚠️  Patterns sensibles détectés (vérifier ci-dessus)"
else
    echo "  ✅ Aucun pattern sensible détecté"
fi

# 3. Vérifie que .gitignore protège les secrets
if [ -f .gitignore ]; then
    if grep -q "\.env" .gitignore; then
        echo "  ✅ .env protégé dans .gitignore"
    else
        echo "  ⚠️  .env n'est pas dans .gitignore!"
    fi
fi

echo "  ✅ Scan de sécurité terminé"
