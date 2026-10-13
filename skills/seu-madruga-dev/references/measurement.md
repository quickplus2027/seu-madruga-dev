# Evaluation methodology: real economy, not marketing numbers
Primary metric: **cost per verified successful task**. Secondary: input tokens, output tokens, cached token metrics if provided, tool calls, re-reads, wall time, retries, tests passed, success ratio, unresolved defects.

## Controlled A/B protocol
Select representative benchmark tasks: local bug, refactor, UI, code search, multi-module architecture, flaky tests, security patch, and documentation. Create immutable repo fixture and task brief. Run baseline and with Skill on the **same model/version/settings** and same environment; repeat randomized ordering to limit variance. Capture actual telemetry, not guesses; if cost unavailable use tokens but label limitation. Blind-evaluate correctness using deterministic tests and reviewer rubric. Track p50/p90, failures, and completion quality; include unsuccessful attempts in cost.

## Honest reporting
Do not publish savings percentages until data exist. Small N is exploratory, not statistically conclusive. Avoid cherry-picking. Report raw anonymized metrics without secrets and runtime versions, hashes, limitations and seeds where applicable. Savings = `(baseline - skill)/baseline * 100` only if comparable baseline > 0. Prefer confidence intervals with sufficient repeated samples.

`tests/benchmark_template.csv` is a schema, not measured data.
