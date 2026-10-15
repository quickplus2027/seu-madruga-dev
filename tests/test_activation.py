import tempfile
import unittest
from pathlib import Path
from tools.madruga import bootstrap, doctor, START, END

class TestActivation(unittest.TestCase):
    def test_bootstrap_safe_and_idempotent(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); f=root/'AGENTS.md'; f.write_text('Existing instructions\n',encoding='utf-8')
            self.assertEqual(bootstrap(root,False),0)
            self.assertNotIn(START,f.read_text())
            self.assertEqual(bootstrap(root,True),0)
            self.assertEqual(doctor(root),0)
            self.assertTrue((root/'AGENTS.md.seumadruga.bak').exists())
            self.assertEqual(bootstrap(root,True),0)
            self.assertEqual(f.read_text().count(START),1)
            self.assertEqual(f.read_text().count(END),1)
    def test_refuse_broken_marker(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); f=root/'CLAUDE.md';f.write_text(START)
            self.assertEqual(bootstrap(root,True),2)
            self.assertFalse((root/'AGENTS.md').exists())
