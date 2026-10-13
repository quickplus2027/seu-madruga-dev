# Lean retrieval and tool orchestration
1. `git status --short` and project manifests before deciding scope (only if needed).
2. Prefer narrow glob / `rg -n 'symbol' src/path` over recursive full dumps.
3. Read exact line neighborhoods and relevant call sites; inspect one dependency hop at a time.
4. Batch logically related low-cost searches. Avoid repeating identical failed commands.
5. Prefer local docs, lockfiles, existing tests, types and implementation over uncontrolled internet search; verify fast-changing external APIs against official documentation.
6. Cache discoveries as compact paths/symbol references, not pasted full source files. Re-open only when source changes.
7. In tool output, truncate by intent; do not silently truncate evidence of security or failure. Use focused summaries of tests.
8. Parallelize *independent* safe investigations when platform supports it; avoid duplicated agents that read the same repo and produce overlapping answers.
9. Keep skill search opt-in or task-driven. Prioritize official sources and demonstrable maintenance, not popularity.
10. No access? State limitation instead of inventing results.

**Token equation:** total work = input + output + tool results + repeated context + retries. Optimizing one term cannot justify lowering success rate.
