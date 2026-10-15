# Token Economy for Video Production

**Goal:** save the total cost of reaching an approved final video, not maximize token savings at the expense of creativity.

## 1. Context reconnaissance
- Read project-local AGENTS.md/CLAUDE.md and only package/config files needed to establish engine.
- Search paths for `Composition`, `Sequence`, scene IDs, media assets, timing tokens and animation utilities before opening large files.
- Open only 1-3 relevant scene files initially; widen scope on dependency evidence.
- Keep an asset index with filename, role, duration, orientation, license and reuse status; avoid uploading/embedding binary or frame dumps into context.
- Use filenames and short descriptions for stills; inspect actual representative images only when making visual decisions.
- Do not re-read unchanged outputs; maintain a working facts ledger with source paths.

## 2. The three-gate iteration
**Gate A, concept (text cheap):** one-page brief, three distinct concepts, selected idea, shot list and timing table. No full source code before direction is fixed.
**Gate B, visual (renders cheap):** still at opening, hero reveal, midpoint, CTA; one 2-4s motion sample only if needed. Resolve legibility, contrast, camera and choreography.
**Gate C, final (render expensive):** implement remaining scenes, render a low-cost review and then final full-quality export. Do not repeat full renders for text alignment fixes when a still will answer the question.

## 3. Change classification
| Task | Read | Edit | Verify |
| --- | --- | --- | --- |
| Fix typo | affected component | one string | still of affected frame |
| Re-time cut | timeline + adjacent scenes | frame mapping | short excerpt at cut |
| Rebrand fonts | typography tokens and key scenes | theme tokens | stills across formats |
| Add scene | scene contract + neighboring sequence | new scene and timeline | sample then integration |
| Change engine | manifests, dependencies, source design | approved migration plan | cross-engine parity frames |

## 4. Reuse without visual sameness
Reuse infrastructure: media loader, interpolation helpers, typography, transitions API, timing calculations, safe-area overlays, render scripts and test fixtures.
**Do not blindly reuse** the same hook, composition, camera path, kinetic type treatment, CTA transition and pacing across every project. Keep a **creative signature** per campaign with opening mechanism, shot grammar, motion curve family, tempo and contrast approach.

## 5. Working notes and handoff
Maintain a short local `VIDEO_HANDOFF.md` when needed:
```text
GOAL / PLATFORM / FORMAT / FPS / DEADLINE
CHOSEN CONCEPT / DIFFERENTIATING FEATURE / REFERENCES
SCENES: ids, in/out frames, content, assets
FILES TO EDIT / VERIFIED ENGINE / INSTALLED SKILLS
APPROVED STILLS / RENDER PATHS / OPEN ISSUES
NEXT ACTION / TEST NEEDED / STATUS
```
Do not create this file or store media details without the project's authorization; treat this as a template.

## 6. Token budgets: practices, not arbitrary promises
- Before a long operation, state its expected value and decide whether file search, code edit, still render or full render is the least expensive proof.
- Batch compatible file/path inspections, but avoid massive tool transcript dumps.
- Prefer exact line-range reads and scoped diffs over repeating whole files.
- Stop after repeated failed attempts; summarize errors and revise hypothesis rather than retrying the same render unchanged.
- Track where possible: model tokens, tool calls, renders attempted, render duration, changes requested after review, number of scenes approved on first pass.
- Compare like-for-like tasks and track **quality + elapsed time + revisions + token count**. Never claim a percentage saving without actual telemetry.

## 7. Example budget-sensitive sequence
For a 30s vertical reel: find existing assets, pick art direction, define timeline at chosen FPS, build a 3s signature opening, render two or three stills, approve visual language, build remaining scenes, inspect critical cuts, render full draft, then final. If the audience already approved a reliable style, shorten the concept step rather than recycling shots blindly.
