# Router Stub (v2)

This directory will host the multi-driver router responsible for resolving skills
to drivers while respecting routing preferences, budgets, and local execution
timeouts.

## TODO
- Flesh out driver registry hydration in `router.py`.
- Implement budget ledger persistence across runs.
- Add instrumentation hooks to feed benchmark metrics back into `benchmarks/results`.

## References
- Policies: `project-space/policies/`
- Security envelope: `project-space/security/`
