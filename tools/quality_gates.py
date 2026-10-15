#!/usr/bin/env python3
"""Optional offline checks. Stdlib only. Does not change files or execute app scripts."""
import argparse
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

class A11yParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.issues=[]; self.stack=[]; self.line=0
    def handle_starttag(self,tag,attrs):
        d=dict(attrs); line=self.getpos()[0]
        if tag=='img' and ('alt' not in d): self.issues.append((line,'IMG_ALT','image missing alt attribute'))
        if tag=='html' and not d.get('lang'): self.issues.append((line,'HTML_LANG','root html missing lang'))
        if tag=='input' and d.get('type','').lower() not in ('hidden','submit','button','reset','image') and not (d.get('aria-label') or d.get('aria-labelledby') or d.get('id')): self.issues.append((line,'INPUT_LABEL','input has no label reference; inspect associated label'))
        if tag=='button' and not (d.get('aria-label') or d.get('aria-labelledby') or d.get('title')): self.stack.append((tag,line,[]))
    def handle_data(self,data):
        if self.stack: self.stack[-1][2].append(data)
    def handle_endtag(self,tag):
        if tag=='button' and self.stack:
            _,line,parts=self.stack.pop()
            if not ''.join(parts).strip(): self.issues.append((line,'BUTTON_NAME','button may have no accessible name; inspect nested content'))

def inspect_file(path, editorial=False):
    """Heuristics, NOT full WCAG or runtime assurance."""
    suffix=path.suffix.lower()
    if suffix not in ('.html','.htm','.md','.mdx','.txt','.jsx','.tsx','.vue'):
        return []
    try: content=path.read_text(encoding='utf-8-sig')
    except (OSError,UnicodeError) as e:return [(0,'READ_ERROR',str(e))]
    issues=[]
    if editorial and suffix in ('.md','.mdx','.txt'):
        fenced=False
        for num,line in enumerate(content.splitlines(),1):
            if line.lstrip().startswith(('```','~~~')): fenced=not fenced;continue
            if not fenced and '\u2014' in line: issues.append((num,'EDITORIAL_DASH','review em dash in original prose'))
    if suffix in ('.html','.htm'):
        parser=A11yParser()
        try: parser.feed(content);issues+=parser.issues
        except Exception as e:issues.append((0,'PARSE',str(e)))
    return issues

def changed_files(project):
    """Read-only Git; avoid expensive whole-repo test discovery."""
    import subprocess
    try:
        r=subprocess.run(['git','-C',str(project),'status','--porcelain','-z','--untracked-files=normal'],capture_output=True,timeout=10)
        if r.returncode:return []
        results=[]
        for item in r.stdout.decode('utf-8','replace').split('\0'):
            if len(item)<4:continue
            name=item[3:]
            if name.startswith(('"','\'')):name=name.strip('"')
            f=(project/name).resolve()
            if f.is_file() and f.is_relative_to(project.resolve()):results.append(f)
        return results
    except (OSError,subprocess.TimeoutExpired):return []

def scan(paths,editorial=False):
    count=0
    for path in paths:
        if not path.is_file():continue
        for lineno,code,message in inspect_file(path,editorial):
            print(f'{path}:{lineno}: {code}: {message}');count+=1
    print(f'GATES: {len(paths)} file(s) checked, {count} finding(s). Static heuristics only.')
    return 1 if count else 0

def hook_session():
    print('SeuMadruga.dev: avalie risco, modelo e contexto; em UI aplique Visual Excellence; preserve dados e execute testes afetados. Hooks não substituem aprovação humana.')
    return 0

def hook_edit():
    # Claude delivers JSON on stdin. Never block an edit based on static heuristics.
    try:
        data=json.loads(sys.stdin.read(250000) or '{}')
        tool=data.get('tool_input') or {}
        filename=tool.get('file_path') or tool.get('path')
        if filename:
            p=Path(filename)
            if p.is_file():
                issues=inspect_file(p,editorial=False)
                if issues:
                    print(f'SeuMadruga quality advisory: {len(issues)} potential accessibility issue(s) in {p.name}. Run quality-gates for details.')
    except (ValueError,OSError,TypeError):pass
    return 0

def main(argv=None):
    p=argparse.ArgumentParser(description='SeuMadruga.dev offline quality checks')
    sub=p.add_subparsers(dest='cmd',required=True)
    q=sub.add_parser('check');q.add_argument('--project',type=Path,required=True);q.add_argument('--changed',action='store_true');q.add_argument('--editorial',action='store_true');q.add_argument('files',nargs='*')
    sub.add_parser('hook-session');sub.add_parser('hook-edit')
    a=p.parse_args(argv)
    if a.cmd=='hook-session':return hook_session()
    if a.cmd=='hook-edit':return hook_edit()
    project=a.project.resolve()
    if not project.is_dir():print('ERROR project missing');return 2
    paths=changed_files(project) if a.changed else [project/f for f in a.files]
    if not a.changed and not paths:
        print('ERROR specify --changed or paths; no automatic full-repository scan');return 2
    for f in paths:
        if not f.resolve().is_relative_to(project):print(f'ERROR outside project: {f}');return 2
    return scan(paths,a.editorial)
if __name__=='__main__':sys.exit(main())
