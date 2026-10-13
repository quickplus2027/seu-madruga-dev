# Targeted testing with risk-based escalation
Goal: shortest **adequate** confidence path. Always obey requested suite and mandatory CI gates.

## Impact map
Identify changed function/module, tests covering that behavior, direct callers, public contracts, data boundaries and shared components. Test in order: static checks (if scoped), changed function/unit test, component/integration tests for affected call chain, then wider checks based on risk.

## When full tests are required
- Public/shared API change or common utility imported widely.
- Dependency, compiler, TypeScript config, routing, build tooling or schema changes.
- Authentication/authorization, cryptography, payments, personal data or security-sensitive flow.
- Global state, database migration, concurrency or release preparation.
- Evidence of unexpected regressions or flaky tests.
- User/CI/repository explicitly requires full suite.

## Examples
JS/TS: `npx vitest run path/to/file.test.ts` (only if Vitest exists); `npx jest path/to/file.test.ts` (only if Jest exists); targeted `npm test -- --runTestsByPath` only when configured. Python: `pytest tests/test_feature.py -q`; expanded `pytest -q`. Detect available scripts first; do not install tools just to run a sample.

Report `PASSED`, `FAILED`, `NOT RUN` separately. Do not call targeted test a full regression guarantee.
