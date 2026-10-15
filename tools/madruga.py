#!/usr/bin/env python3
"""SeuMadruga.dev maintenance CLI. Offline, stdlib only. No network or Git changes."""
import argparse
import sys
from pathlib import Path

START='<!-- SEUMADRUGA:START -->'
END='<!-- SEUMADRUGA:END -->'
BASE=Path(__file__).resolve().parents[1]
RULES=(BASE/'templates/CORE_RULES.pt-BR.md').read_text(encoding='utf-8')
MANAGED=START+'\n'+RULES.rstrip()+'\n'+END+'\n'
FILES=('AGENTS.md','CLAUDE.md')

def bootstrap(project:Path,apply:bool):
    if not project.is_dir():
        print('ERROR: project directory does not exist',file=sys.stderr); return 2
    for filename in FILES:
        dest=project/filename
        old=dest.read_text(encoding='utf-8-sig') if dest.exists() else ''
        if (START in old) != (END in old):
            print(f'ERROR: incomplete marker in {dest}; no files changed',file=sys.stderr);return 2
        if START in old and old.index(START)>old.index(END):
            print(f'ERROR: reversed markers in {dest}; no files changed',file=sys.stderr);return 2
    # Validate all backup destinations before the first write.
    if apply:
        for filename in FILES:
            dest=project/filename
            if dest.exists() and dest.with_name(dest.name+'.seumadruga.bak').exists():
                old=dest.read_text(encoding='utf-8-sig')
                if START in old:
                    a=old.index(START);b=old.index(END)+len(END)
                    candidate=old[:a]+MANAGED.rstrip()+old[b:]
                else:
                    candidate=old.rstrip()+ ('\n\n' if old.strip() else '')+MANAGED
                if candidate != old:
                    print(f'ERROR: backup exists for {dest}; no files changed',file=sys.stderr);return 2
    for filename in FILES:
        dest=project/filename
        old=dest.read_text(encoding='utf-8-sig') if dest.exists() else ''
        if START in old:
            a=old.index(START);b=old.index(END)+len(END)
            new=old[:a]+MANAGED.rstrip()+old[b:]
            action='update managed block'
        else:
            new=old.rstrip()+ ('\n\n' if old.strip() else '')+MANAGED
            action='append managed block' if old else 'create file'
        if old==new:
            print(f'UNCHANGED {dest}');continue
        print(f'{"APPLY" if apply else "PREVIEW"} {action}: {dest}')
        if apply:
            if dest.exists():
                backup=dest.with_name(dest.name+'.seumadruga.bak')
                if backup.exists():
                    print(f'ERROR: backup exists {backup}; stop to avoid overwrite',file=sys.stderr);return 2
                backup.write_bytes(dest.read_bytes())
            dest.write_text(new,encoding='utf-8',newline='\n')
    return 0

def doctor(project:Path):
    print('SeuMadruga.dev doctor (offline; no runtime activation guarantee)')
    print('Skill manifest:', 'OK' if (BASE/'skills/seu-madruga-dev/SKILL.md').is_file() else 'MISSING')
    problem=False
    for name in FILES:
        f=project/name
        ok=f.exists() and START in f.read_text(encoding='utf-8-sig') and END in f.read_text(encoding='utf-8-sig')
        print(f'{name}:', 'managed rules present' if ok else 'MISSING (run bootstrap)')
        problem|=not ok
    print('NOTE: agent may still ignore instructions; test in a new session and inspect actual behavior.')
    return 1 if problem else 0

def lint(paths):
    failures=0
    for raw in paths:
        path=Path(raw)
        if not path.exists():
            print('MISSING',path);failures+=1;continue
        if path.is_dir():
            print('SKIP directory (select individual prose files):',path);continue
        if path.suffix.lower() not in ('.md','.txt','.mdx'):
            print('SKIP non-prose:',path);continue
        in_fence=False
        for index,line in enumerate(path.read_text(encoding='utf-8-sig').splitlines(),1):
            if line.lstrip().startswith(('```','~~~')):
                in_fence=not in_fence;continue
            if not in_fence and '—' in line:
                print(f'{path}:{index}: em dash found (review manually)');failures+=1
    return 1 if failures else 0

def hooks(project:Path,apply:bool):
    """Claude project-local, opt-in advisory hooks. Do not overwrite settings."""
    import json
    import subprocess
    config=project/'.claude/settings.local.json'
    if not project.is_dir(): print('ERROR project missing');return 2
    if config.exists():
        print(f'EXISTS {config}. Merge manually after inspection; no changes made.')
        return 2
    cli=(BASE/'tools/quality_gates.py').resolve()
    # shell quoting for paths; Python can be resolved from PATH in the client environment
    from shlex import quote
    import os
    import shutil
    python=shutil.which('python3') or shutil.which('python')
    if not python: print('ERROR Python not found');return 2
    command_prefix=f'"{python}" "{cli}"'
    config_data={'hooks':{
        'SessionStart':[{'hooks':[{'type':'command','command':command_prefix+' hook-session','timeout':10}]}],
        'PostToolUse':[{'matcher':'Edit|Write', 'hooks':[{'type':'command','command':command_prefix+' hook-edit','timeout':10}]}]
    }}
    print(f'{"INSTALL" if apply else "PREVIEW"} Claude project-local advisory hooks in {config}')
    print(json.dumps(config_data,indent=2,ensure_ascii=False))
    if apply:
        config.parent.mkdir(parents=True,exist_ok=True)
        with config.open('x',encoding='utf-8') as stream:json.dump(config_data,stream,ensure_ascii=False,indent=2)
        print('Installed; check /hooks in Claude Code. Remove settings.local.json to uninstall only if you created it here.')
    return 0

def main():
    a=argparse.ArgumentParser(description='Offline project rules bootstrap and audit')
    sub=a.add_subparsers(dest='command',required=True)
    b=sub.add_parser('bootstrap');b.add_argument('--project',type=Path,required=True);b.add_argument('--apply',action='store_true',help='explicitly write files; previews by default')
    d=sub.add_parser('doctor');d.add_argument('--project',type=Path,required=True)
    l=sub.add_parser('lint-prose');l.add_argument('paths',nargs='+')
    h=sub.add_parser('hooks-claude');h.add_argument('--project',type=Path,required=True);h.add_argument('--apply',action='store_true')
    args=a.parse_args()
    if args.command=='bootstrap':return bootstrap(args.project.resolve(),args.apply)
    if args.command=='doctor':return doctor(args.project.resolve())
    if args.command=='hooks-claude':return hooks(args.project.resolve(),args.apply)
    return lint(args.paths)
if __name__=='__main__':sys.exit(main())
