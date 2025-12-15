#!/usr/bin/env bash
set -euo pipefail

cat <<'EOF'
BOOT SEQUENCE (Cortex Dialectique)

1) CHECK Gmail Inbox (agent channel)
   - priority/critical
   - type/alert
   - type/veto

2) CHECK GitHub notifications
   - security alerts
   - CI failures on main

3) ACK A2A messages (handoff/veto/sync)

4) Only then: start coding (PR-first)
EOF
