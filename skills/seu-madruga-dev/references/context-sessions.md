# Context engineering and session hygiene
Context includes instructions, messages, file reads, tool outputs and history. Long sessions amplify repeated cost and can dilute relevant signals. Preserve *decisions*, not raw transcripts.

## Claude Code
- `/clear`: start unrelated work with fresh chat after a concise saved handoff.
- `/compact`: compress when continuing the same extensive task.
- `/context`: inspect context usage **if exposed by current installed version**; never infer exact percentage without telemetry.
- Plan Mode: use the UI/command available in current installation, not a guessed universal slash command.

## Codex
Use a new thread/session to separate unrelated work; use built-in context or compaction controls only if confirmed in active version. No assumption that Claude slash commands exist in Codex.

## Routine
On task switch: checkpoint modified files, test results, known failures, exact next step. Don't put secrets in a handoff. Prefer `docs/HANDOFF.md` or short session note. Avoid permanent logs of irrelevant tool output. Summarize facts with paths and specific symbols.

## Heuristic checks, not universal thresholds
After broad file exploration, high output volume, repeated corrections or loss of coherence, consider compacting/fresh session; do not rely on an arbitrary 70/80% threshold. Avoid compacting mid-critical tool transaction if it may lose state.
