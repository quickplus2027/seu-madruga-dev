# HyperFrames Production Playbook

Official source: https://github.com/heygen-com/hyperframes

## What it is
HyperFrames is an HTML-based video creation/rendering framework with a set of specialized agent skills. It is a distinct engine, not a synonym for Remotion. Follow current documentation and the exact installed version.

## Install and route *official* skills responsibly
The upstream repository documents `npx hyperframes skills update` for the core skill set and `npx hyperframes skills` for all published skills. Installation executes external tooling: review source and request necessary approval. Do not run either as an unnoticed side effect.

Read the official `/hyperframes` router first when available. It helps select a creation workflow (e.g., general-video, motion-graphics, music-to-video, talking-head editing) and domain skills. Do **not** force-load all 21 skills for each task; choose one entry workflow and targeted capabilities.

## Remotion vs HyperFrames
| Criteria | Remotion | HyperFrames |
| --- | --- | --- |
| Existing code | React/TS composition | HTML/DOM-based composition |
| Primary motion model | Frame functions and sequences | Framework timing and seekable animation |
| Existing asset ecosystem | Reuse React video scene utilities | Reuse web layouts, animations and HyperFrames scene contracts |
| Agent integration | Remotion conventions and plugins | /hyperframes router and domain skills |
| Recommended next step | Read local composition source | Read local composition + official HyperFrames core skill |

Do not migrate just for fashion. For an existing video, compare feature parity, render constraints, media support, visual fidelity, learning cost and rollback.

## Motion practices
- Model scene timings so they can be sought and rendered at arbitrary timestamps/frames.
- Follow the official composition contract and `data-*` timing conventions of your installed HyperFrames version.
- Use GSAP, Lottie, Three.js, WAAPI or other runtimes **only if** supported by the project, motion requirement and official workflow; avoid stacking libraries automatically.
- Separate source content, typography, transition tokens and media track metadata.
- Capture stills at turning points, short scene snippets and final output for visual acceptance.

## Efficient workflow
1. Discover installed HyperFrames version, available CLI commands and skills. Never invent syntax.
2. Use official router to select relevant creation workflow.
3. Approve three distinct concept routes before implementation when style is uncertain.
4. Implement a signature scene; validate determinism at key timestamps and check renders.
5. Expand to remaining timeline; inspect rhythm, safe areas, effects, caption alignment and audio.
6. Save a concise handoff with the selected workflow, skill versions, render commands actually used and known problems.

## Special case: remotion-to-hyperframes
This is a **one-way migration of existing Remotion compositions**. It is not the proper primary workflow for authoring a new video from scratch. Avoid assuming byte-exact output parity; compare rendered scenes and note discrepancies.
