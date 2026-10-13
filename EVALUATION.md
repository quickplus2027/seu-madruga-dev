# Benchmark protocol
Status: methodology defined; **no measured benchmark results** included. Baseline and Skill must use same model snapshot/settings, repo snapshot, task, permissions and test harness. Randomize order across repeats. Record costs/tokens only when measured, include unsuccessful completions, evaluate solved task correctness independently. Report uncertainty and limitations.

Data template: `tests/benchmark_template.csv`. The first goal is a pre-registered benchmark suite of at least 8 diverse tasks, 5+ repetitions each subject to resource feasibility; this is a target, not a claim of completion.

Quality gates: correctness at least baseline within uncertainty, security not degraded, no lost user edits, no bypassed CI, and a reproducible net cost/time improvement before saying it *saves* tokens.
