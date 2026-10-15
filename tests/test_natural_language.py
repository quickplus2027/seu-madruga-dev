import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class NaturalLanguageTests(unittest.TestCase):
    def test_intent_coverage(self):
        skill=(ROOT/'skills/seu-madruga-dev/SKILL.md').read_text(encoding='utf-8')
        for phrase in ['revise o que mudou', 'prepare este projeto', 'diagnostique', 'model', 'consent']:
            self.assertIn(phrase.casefold(), skill.casefold())
    def test_safe_bootstrap(self):
        rules=(ROOT/'templates/CORE_RULES.pt-BR.md').read_text(encoding='utf-8')
        self.assertIn('prévia',rules)
        self.assertIn('aprovação',rules)
    def test_no_python_quick_start(self):
        readme=(ROOT/'README.md').read_text(encoding='utf-8')
        front=readme.split('## O que é o SeuMadruga.dev?')[0]
        self.assertNotIn('python D:',front)
        self.assertIn('npx skills add',front)
if __name__=='__main__': unittest.main()
