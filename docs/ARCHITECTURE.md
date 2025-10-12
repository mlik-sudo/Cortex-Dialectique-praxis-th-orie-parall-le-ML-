---
project: cortex-dialectique-ml
owner: codex-cli
title: "Architecture Overview"
status: "draft"
updated: "2025-10-12"
reviewed: 2025-10-12
---

# Architecture Overview

## Control Plane
- Policies, governance, and routing rules stored under `project-space/policies`.
- Observability assets collected in `project-space/dashboards`.

## Data Plane
- CLI agents orchestrated via the multi-driver router (see ADR-0001).
- Benchmarks and telemetry recorded in `project-space/benchmarks`.

## Security Envelope
- Local policies and hook configurations maintained in `security/`.
- Detect-secrets baseline enforces zero-secret discipline.
