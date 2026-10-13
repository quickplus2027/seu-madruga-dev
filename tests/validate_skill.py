#!/usr/bin/env python3
"""Offline, standard-library-only structural validation; not a security certification."""
from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[1]
SKILL=ROOT/'skills'/'seu-madruga-dev'/'SKILL.md'
def validate():
 errors=[]
 if not SKILL.is_file(): return ['Missing SKILL.md']
 txt=SKILL.read_text(encoding='utf-8')
 m=re.match(r'\A---\n(.*?)\n---\n',txt,re.S)
 if not m: return ['Missing YAML frontmatter']
 fm=m.group(1)
 fields={k.strip():v.strip() for k,v in (line.split(':',1) for line in fm.splitlines() if ':' in line)}
 name=fields.get('name',''); desc=fields.get('description','')
 if name!='seu-madruga-dev' or not re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',name): errors.append('Invalid skill name')
 if not (1<=len(desc)<=1024): errors.append('Description outside allowed length')
 if len(txt.splitlines())>500: errors.append('SKILL.md exceeds 500 lines')
 for path in re.findall(r'\]\((references/[^)# ]+|assets/[^)# ]+)\)',txt):
  if not (SKILL.parent/path).is_file():errors.append('Missing referenced file: '+path)
 for path in ['README.md','SECURITY.md','CONTRIBUTING.md','EVALUATION.md','LICENSE','docs/GITHUB_PASSO_A_PASSO.md']:
  if not (ROOT/path).is_file():errors.append('Missing repo file: '+path)
 return errors
if __name__=='__main__':
 errors=validate()
 if errors:
  for x in errors:print('ERROR:',x)
  sys.exit(1)
 print('PASS: offline structural checks; this is not security or runtime certification.')
