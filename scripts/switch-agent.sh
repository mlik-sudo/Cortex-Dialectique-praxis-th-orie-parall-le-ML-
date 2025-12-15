#!/bin/bash
# 🏛️ Code-Commune — Agent Identity Switcher
# Usage: ./scripts/switch-agent.sh gemini|claude|codex|comet|mediator
# 
# Permet de changer l'identité Git pour simuler différents agents.

set -e

DOMAIN="codecommune.gov"

case $1 in
  gemini)
    git config user.name "Gemini-Architect"
    git config user.email "${DOMAIN}+gemini@gmail.com"
    echo "🤖 Switched to Gemini-Architect"
    echo "   Role: Le Visionnaire — \"Move fast and break things.\""
    echo "   Zone: /features/* /experimental/*"
    ;;
  claude)
    git config user.name "Claude-Safety"
    git config user.email "${DOMAIN}+claude@gmail.com"
    echo "🛡️ Switched to Claude-Safety"
    echo "   Role: Le Gardien — \"Safety first, refactor later.\""
    echo "   Zone: /core/* /security/* tests/"
    ;;
  codex)
    git config user.name "Codex-Engineer"
    git config user.email "${DOMAIN}+codex@gmail.com"
    echo "⚡ Switched to Codex-Engineer"
    echo "   Role: L'Artisan — \"It compiles, ship it.\""
    echo "   Zone: /scripts/* /infra/*"
    ;;
  comet)
    git config user.name "Comet-Scout"
    git config user.email "${DOMAIN}+comet@gmail.com"
    echo "🔭 Switched to Comet-Scout"
    echo "   Role: L'Éclaireur — \"Trust but Verify.\""
    echo "   Zone: /docs/* DEPS.md /research/*"
    ;;
  mediator)
    git config user.name "ChatGPT-Mediator"
    git config user.email "${DOMAIN}+mediator@gmail.com"
    echo "⚖️ Switched to ChatGPT-Mediator"
    echo "   Role: Le Médiateur — \"Clarity over chaos.\""
    echo "   Zone: /deliberation/* (Reviewer Only)"
    ;;
  status|whoami)
    echo "🏛️ Current Agent Identity:"
    echo "   Name:  $(git config user.name)"
    echo "   Email: $(git config user.email)"
    ;;
  *)
    echo "🏛️ Code-Commune — Agent Identity Switcher"
    echo ""
    echo "Usage: $0 {gemini|claude|codex|comet|mediator|status}"
    echo ""
    echo "Agents:"
    echo "  gemini   - 🤖 Gemini-Architect (Vision, Innovation)"
    echo "  claude   - 🛡️ Claude-Safety (Sécurité, Stabilité)"
    echo "  codex    - ⚡ Codex-Engineer (Scripts, Infra)"
    echo "  comet    - 🔭 Comet-Scout (Docs, Reality Check)"
    echo "  mediator - ⚖️ ChatGPT-Mediator (Arbitrage)"
    echo "  status   - Show current identity"
    exit 1
    ;;
esac
