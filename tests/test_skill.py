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
if __name__=='__main__': unittest.main()
