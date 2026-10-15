# Remotion Production Playbook

Official sources: https://www.remotion.dev/docs/terminology/composition and https://www.remotion.dev/docs/render

## When to choose
Use for an existing React/TypeScript video project or when component reuse, typed props, frame-driven visuals, reproducible renders and React ecosystem integration are natural fits. Confirm locally installed Remotion version before using version-specific APIs.

## Architecture
- Register explicit Composition(s): id, React component, width, height, fps and durationInFrames.
- Use Sequence for time placement; share scene interfaces like `startFrame`, `durationFrames`, `assets`, `brand`, `copy`.
- Animation must be a deterministic function of frame, FPS and props, not wall-clock timers. Think in **frames**, not only seconds.
- Avoid duplicated magic numbers: establish central duration and motion design tokens.
- Keep text and assets data-driven where useful, separate narrative data from scene logic.

## Key animation patterns
- `useCurrentFrame()` and `useVideoConfig()`: read frame and FPS.
- `interpolate(frame, inputRange, outputRange, options)`: precise controlled changes (e.g., opacity and position). Clamp extrapolation when desired.
- `spring({frame, fps, config})`: natural motion, parameterized, with scene-specific purpose.
- Keep entrance/exit distinct from camera motion. Avoid using identical `spring` configuration on every title.
- Use deliberate rests, contrast, negative space, speed variation and cuts, not continuous motion everywhere.

Example:
```tsx
import {AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig} from 'remotion';

export const Headline = ({text}: {text: string}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const reveal = spring({frame, fps, config: {damping: 16, stiffness: 95}});
  const opacity = interpolate(frame, [0, 12], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  return (
    <AbsoluteFill style={{justifyContent: 'center', alignItems: 'center'}}>
      <h1 style={{opacity, transform: `translateY(${(1 - reveal) * 70}px)`}}>{text}</h1>
    </AbsoluteFill>
  );
};
```
Only an illustration: preview against actual FPS and duration; accessible contrast, font loading and scene semantics still need validation.

## Minimize wasted renders
- Inspect composition metadata and available CLI options first.
- Render stills at selected frames to check typography/composition.
- Render only changed frame ranges for localized motion issues when CLI version supports `--frames`.
- Render a draft with scaled/lower-cost settings before the final full-quality encode when acceptable.
- Verify overlays, audio, font assets, media decode and safe areas in real output.

## Shot acceptance
Review frame 0, first readable frame, title peak, main cut boundaries, dominant motion peak, CTA arrival and last frame. Verify correct aspect (9:16, 1:1, 16:9 etc.), subtitles, motion continuity and music sync.

## Anti-patterns
Full video rerender after every one-line edit; copying huge source trees into agent context; timing driven by setTimeout/Date.now; identical titles and transitions in every campaign; unrelated dependencies installed to solve a small animation.
