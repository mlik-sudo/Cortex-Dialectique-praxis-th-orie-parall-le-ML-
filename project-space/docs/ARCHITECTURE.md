# Architecture Overview

## Control Plane
- Policies, governance, and routing rules stored under `project-space/policies`.
- Observability assets collected in `project-space/dashboards`.

## Data Plane
- CLI agents orchestrated via the multi-driver router (see ADR-0001).
- Benchmarks and telemetry recorded in `project-space/benchmarks`.

## Security Envelope
- Local policies and hook configurations under `project-space/security`.
- Detect-secrets baseline enforces zero-secret discipline.
