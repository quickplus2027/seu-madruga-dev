# Environment Efficiency & Profile Protection

**Scope:** Apply when agent tasks create or manage builds, dependencies, temporary files, traces, caches, downloaded artifacts or substantial workspace data, or when troubleshooting performance. Do not load for unrelated tasks. This document provides recommendations, not permission to change system configuration.

## Golden rule
Optimize **total resources to a correct, verified result**: tokens, time, disk I/O, storage, memory, CPU, GPU and reliability. Never save tokens by damaging the machine, breaking another project, weakening security, or hiding necessary tests.

## Scope-first discovery (read-only)
1. Confirm OS and the current project root. Use the existing project and user instructions; respect existing workspace conventions.
2. If relevant, identify available disks, free space and project-local build paths. Do not assume a `D:` drive exists. Ask before choosing an alternate volume.
3. Read relevant package manager/build configuration before proposing cache changes. Find out whether paths are global, per-user, per-repo or shared.
4. Determine **evidence of a problem** (large file counts, disk exhaustion, prolonged scans, slow builds, memory pressure); do not claim that a cache causes OS startup delays without measurements.
5. Scope tool searches: exclude `.git`, `node_modules`, `.next`, `dist`, `build`, coverage and caches when content is not needed, but do not blindly ignore those paths for security or dependency investigations.

## Defaults for all platforms
- Keep source, outputs, temp files and disposable test artifacts inside dedicated project-controlled paths when tooling allows it, and exclude generated outputs from Git.
- Prefer project-local `TMP`, `TEMP`, `TMPDIR` or tool-specific path overrides **only for a particular command/process**, where supported. Do not change global environment variables reflexively.
- Prefer reuse of safe verified caches to repeated downloads; weigh cache relocation against broken symlinks, permissions, disk wear, portability and tool compatibility.
- Avoid duplicate checkout copies and broad recursive scans of the entire home/profile directory; inspect targeted paths and cap log output.
- Never delete/move/rename user files, caches, SSH keys, credentials, shell profiles, IDE settings, `.git`, `.claude`, `.codex`, `.vscode`, package manager directories, cloud-synced folders or OS paths without explicit, specific authorization and backup/rollback plan.
- Never disable antivirus, security protections or logging to improve speed. Do not elevate privileges unless indispensable and approved.
- For concurrent builds and tests, bound worker count according to available RAM and CPU; avoid repeated full-suite runs when scoped tests suffice, but retain CI/release/security gates.

## Windows profile protection
- `%USERPROFILE%`, `%APPDATA%`, `%LOCALAPPDATA%`, `%TEMP%`, `%USERPROFILE%\.ssh`, `%USERPROFILE%\.claude`, and configuration files require careful handling. Windows and installed tools legitimately rely on these locations.
- Avoid placing repositories and huge generated trees inside Desktop, Downloads, OneDrive or roaming profile locations when a safer user-approved workspace exists.
- If the user already chose `D:\DEV` for repositories, respect it; suggest (not silently create) project caches under a suitable workspace or an approved alternate drive.
- Prefer overrides scoped to the current PowerShell process or project scripts, only after verifying the tool honors the variable; global `npm`, `pnpm`, Python, compiler or Windows temp relocation may affect unrelated repositories.
- A delay observed during Windows startup, logon or profile loading is **not by itself proof** that `node_modules`, caches or temporary files caused it. Measure and isolate contributing factors first.
- Do not automatically use junctions, symlinks, registry edits, `setx`, User Profile migration, cleanup commands, or bulk deletion. Request approval after explaining side effects.

## Linux and macOS
- Respect `$HOME`, XDG base directories, `$TMPDIR`, filesystem mount and permission constraints. Do not assume Windows conventions or move `/tmp`, global package caches or home directories automatically.
- Avoid privileged cleanup, global shell profile changes, or moving application support directories unless reviewed with the user.

## Safe decision flow
1. **Identify:** What generates the bytes/CPU/RAM cost? Which project and tool own it? Is there direct evidence?
2. **Estimate:** Expected benefit and risk; include disk usage, reproducibility, effect on other projects, cross-platform behavior.
3. **Plan:** Propose a reversible *per-project* change first. Identify exact paths, backup, validation, rollback, and whether the change affects multiple projects.
4. **Approve:** Ask for explicit confirmation before any deletion, relocation, global setting, or shared-cache mutation.
5. **Verify:** Measure before/after for build time, disk size, relevant resource usage, behavior, and regression tests. Report measurements as measurements, not assumptions.

## Examples
- **Good:** A Next.js app builds huge `.next` artifacts on its project drive. Inspect `next.config`, location and free space, then propose an appropriate project-scoped build artifact path if supported; verify build and deploy compatibility.
- **Good:** A test runner floods the system temp directory. Check whether it supports project-level output and cleanup, propose a small isolated fix, validate it, and request approval before deleting existing files.
- **Avoid:** Repointing global `TEMP/TMP` or `npm`/`pnpm` caches without user consent, or deleting all `%LOCALAPPDATA%` to 'speed up Windows'.

## Minimal report
`SCOPE | EVIDENCE | PROPOSED PATH | GLOBAL IMPACT? | APPROVAL | VALIDATION | ROLLBACK`
Omit this report when nothing about environment resources is relevant to the task.
