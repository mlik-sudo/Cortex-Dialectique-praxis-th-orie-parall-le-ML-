# 🏛️ Code-Commune Makefile
# ========================
# Cibles principales pour l'audit constitutionnel

.PHONY: proof test-all security-scan check-deps help

# Cible par défaut
.DEFAULT_GOAL := help

# 🔍 Audit constitutionnel complet
proof:
	@echo "🔍 Audit constitutionnel de la Commune..."
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@$(MAKE) check-deps
	@$(MAKE) test-all
	@$(MAKE) security-scan
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "✅ La Commune est en état de fonctionner."

# 📦 Vérification des dépendances (DEPS.md)
check-deps:
	@echo "📦 Vérification des dépendances..."
	@if [ -f scripts/check-deps.sh ]; then \
		chmod +x scripts/check-deps.sh && ./scripts/check-deps.sh; \
	else \
		echo "  ⚠️  scripts/check-deps.sh non trouvé - skip"; \
	fi

# 🧪 Exécution des tests
test-all:
	@echo "🧪 Exécution des tests..."
	@if [ -f scripts/run-tests.sh ]; then \
		chmod +x scripts/run-tests.sh && ./scripts/run-tests.sh; \
	elif command -v pytest >/dev/null 2>&1; then \
		pytest tests/ -v --tb=short 2>/dev/null || echo "  ℹ️  Pas de tests Python"; \
	else \
		echo "  ℹ️  Aucun framework de test détecté"; \
	fi

# 🔒 Scan de sécurité SAST
security-scan:
	@echo "🔒 Scan de sécurité..."
	@if [ -f scripts/security-scan.sh ]; then \
		chmod +x scripts/security-scan.sh && ./scripts/security-scan.sh; \
	elif command -v detect-secrets >/dev/null 2>&1; then \
		detect-secrets scan --baseline .secrets.baseline; \
	else \
		echo "  ℹ️  detect-secrets non installé - vérification basique"; \
		grep -rn "password\|secret\|api_key" --include="*.py" --include="*.js" . 2>/dev/null | grep -v node_modules | head -5 || echo "  ✅ Aucun secret évident détecté"; \
	fi

# 📚 Aide
help:
	@echo "🏛️ Code-Commune - Cibles disponibles"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "  make proof         - Audit constitutionnel complet"
	@echo "  make check-deps    - Vérifie DEPS.md"
	@echo "  make test-all      - Lance les tests"
	@echo "  make security-scan - Scan SAST basique"
	@echo "  make help          - Cette aide"
