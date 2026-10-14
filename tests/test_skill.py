import unittest
from pathlib import Path
from validate_skill import validate, ROOT
class TestSkill(unittest.TestCase):
 def test_structure(self): self.assertEqual(validate(),[])
 def test_human_approval(self):
  txt=(ROOT/'skills/seu-madruga-dev/SKILL.md').read_text(encoding='utf-8')
  self.assertIn('approval',txt.lower())
 def test_all_references_nonempty(self):
  refs=list((ROOT/'skills/seu-madruga-dev/references').glob('*.md'))
  self.assertGreaterEqual(len(refs),10)
  self.assertTrue(all(f.stat().st_size>100 for f in refs))
 def test_environment_protection(self):
  skill=(ROOT/'skills/seu-madruga-dev/SKILL.md').read_text(encoding='utf-8')
  doc=(ROOT/'skills/seu-madruga-dev/references/environment-efficiency.md').read_text(encoding='utf-8')
  self.assertIn('references/environment-efficiency.md',skill)
  for phrase in ['per-project', 'explicit', 'rollback', 'Windows', 'Linux', 'macOS']:
   self.assertIn(phrase,doc)
 def test_orchestration_is_on_demand_and_safe(self):
  skill=(ROOT/'skills/seu-madruga-dev/SKILL.md').read_text(encoding='utf-8')
  doc=(ROOT/'skills/seu-madruga-dev/references/orchestration.md').read_text(encoding='utf-8')
  self.assertIn('references/orchestration.md',skill)
  for phrase in ['1 — Simples','5 — Estratégico','até 4','não uma obrigação' if False else 'não metas','aprovação','Não pressupor `D:`']:
   self.assertIn(phrase,doc)
 def test_visual_excellence_on_demand(self):
  skill=(ROOT/'skills/seu-madruga-dev/SKILL.md').read_text(encoding='utf-8')
  visual=(ROOT/'skills/seu-madruga-dev/references/visual-excellence.md').read_text(encoding='utf-8')
  self.assertIn('references/visual-excellence.md',skill)
  for phrase in ['VISUAL INNOVATION FIRST','prefers-reduced-motion','Do not load for backend-only','data visualization']:
   self.assertIn(phrase,visual)
 def test_visual_modules_comprehensive(self):
  required=['visual-design-system.md','visual-ux-interactions.md','visual-motion.md','visual-3d-immersive.md','visual-data-geospatial.md','visual-performance-quality.md']
  for filename in required:
   path=ROOT/'skills/seu-madruga-dev/references'/filename
   self.assertTrue(path.is_file(), filename)
   self.assertGreater(path.stat().st_size, 1000)
  master=(ROOT/'skills/seu-madruga-dev/references/visual-excellence.md').read_text(encoding='utf-8')
  for filename in required: self.assertIn(filename,master)
if __name__=='__main__': unittest.main()
