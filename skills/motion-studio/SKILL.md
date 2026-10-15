---
name: motion-studio
description: Advanced video production guidance for Remotion, HyperFrames, motion graphics, storyboards, style diversity, asset reuse, token-efficient iteration, rendering and quality assurance. Apply when designing, coding, optimizing or reviewing programmatic video.
license: MIT
---
# SeuMadruga Motion Studio | Production Intelligence

**Autor: Rômulo Bezerra** · SeuMadruga Ecosystem 2.0

## Mission
Create **distinctive, production-ready videos with the smallest verified total cost** in tokens, developer time, rendering, and revisions. Quality and faithful creative direction come before token minimization. This skill does not render, install tools, switch models, or guarantee savings by itself.

## Mandatory workflow
1. **Discover, do not dump:** inspect project instructions, package manifest, relevant compositions, assets and current scene only. Never recursively read a full video project by default.
2. **Brief first:** establish audience, objective, narrative, duration, aspect, FPS, CTA, assets, audio, reference, platform, deadline and constraints. Ask only for essential missing inputs.
3. **Avoid clones:** inspect any existing visual identity and prior approved styles, then propose *three genuinely different narrative structures*, not three color variants. Get a direction when ambiguity is meaningful.
4. **Select engine with evidence:** Remotion for a React/TS composition with frame-based animation; HyperFrames for HTML/DOM based workflow when compatible with actual project and supported rendering tools. Follow the selected engine's installed official skills. Never assume cross-engine migration is free or desirable.
5. **Approve cheap artifacts before expensive ones:** concise shot list → timeline/frame map → representative stills → short segment → full draft → final render. Skip checkpoints only when risk and cost are genuinely low.
6. **Edit only relevant files:** reuse existing components, tokenized animation presets, asset manifests and scene interfaces. Preserve existing code and don't rewrite the entire composition to change one shot.
7. **Validate technically and visually:** inspect readable text, safe areas, transitions, rhythm, subtitles, beat sync, clip continuity, sound, export settings and actual outputs. Report what was rendered and what was not.
8. **Handoff the useful state:** capture final direction, scene map, component choices, assets, known issues and next actions. Never store secrets or private media paths in published handoffs.

## Load references *selectively*
- Token economy and project-context strategy: [references/TOKEN_ECONOMY.md](references/TOKEN_ECONOMY.md)
- Remotion implementation patterns: [references/REMOTION_PLAYBOOK.md](references/REMOTION_PLAYBOOK.md)
- HyperFrames skills and workflows: [references/HYPERFRAMES_PLAYBOOK.md](references/HYPERFRAMES_PLAYBOOK.md)
- Art direction, originality and fatigue prevention: [references/CREATIVE_DIRECTION.md](references/CREATIVE_DIRECTION.md)
- Shot workflow, rendering and acceptance: [references/PRODUCTION_PIPELINE.md](references/PRODUCTION_PIPELINE.md)
- Project checklist: [references/CHECKLIST.md](references/CHECKLIST.md)

## Routing rules
- Small typography change? Read affected scene and test relevant frames, not the entire suite.
- New reel? Start with production pipeline + creative direction; load the selected engine reference only after engine decision.
- Performance/token complaint? Load token economy and inspect actual tool usage and repeated actions.
- Existing Remotion code to HyperFrames? Read the official `remotion-to-hyperframes` skill if installed; it is a **porting** workflow, not a generic video generator.
- Do not install external skills, tools, dependencies or run untrusted scripts without necessary approvals.

## Output contract
Report **direction** (why this style), **scope**, **engine**, **assets reused**, **new work**, **preview evidence**, **render evidence**, **tokens/cost measured or unknown**, **PASS/WARN/FAIL/NOT_RUN/NOT_APPLICABLE**, and **what to do next**. No invented benchmarks or claims of automatic compliance.
