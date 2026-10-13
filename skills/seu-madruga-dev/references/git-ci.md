# Repository and CI efficiency
Use narrow diffs; avoid formatting unrelated files. Never overwrite user edits. Inspect git status before and after editing; do not remove untracked files without explicit approval. Commit in coherent task units; don't auto push.

CI: trigger focused jobs by paths when safely possible; retain branch protection, dependency scan, integration and full-suite release gates. Path filtering should not bypass security or deployment validations. Cancel redundant *superseded* CI builds where supported, not required release jobs. Cache versioned dependencies with lockfile keys; beware stale outputs. Benchmark a change before installing a new cache/tool.
