import tempfile
import unittest
from pathlib import Path
from tools.quality_gates import inspect_file, scan
from tools.madruga import hooks

class QualityGateTests(unittest.TestCase):
    def test_html_a11y_heuristics(self):
        with tempfile.TemporaryDirectory() as temp:
            f=Path(temp)/'index.html';f.write_text('<html><body><img src="x"><button></button></body></html>',encoding='utf-8')
            codes=[item[1] for item in inspect_file(f)]
            self.assertIn('HTML_LANG',codes)
            self.assertIn('IMG_ALT',codes)
            self.assertIn('BUTTON_NAME',codes)
    def test_editorial_opt_in(self):
        with tempfile.TemporaryDirectory() as temp:
            f=Path(temp)/'note.md';f.write_text('Esse texto — viola a regra.\n```\ncode — ignored\n```',encoding='utf-8')
            self.assertEqual(1,len(inspect_file(f,editorial=True)))
            self.assertEqual(0,len(inspect_file(f,editorial=False)))
    def test_hook_preview_and_safe_existing(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            self.assertEqual(0,hooks(root,False))
            self.assertFalse((root/'.claude/settings.local.json').exists())
            self.assertEqual(0,hooks(root,True))
            self.assertEqual(2,hooks(root,True))
    def test_empty_scan_passes(self):
        self.assertEqual(0,scan([]))
if __name__=='__main__':unittest.main()
