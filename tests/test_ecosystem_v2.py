import json
import unittest
from pathlib import Path
from tools.skill_router import recommend

ROOT = Path(__file__).resolve().parents[1]

class EcosystemTest(unittest.TestCase):
    def test_motion(self):
        self.assertEqual(recommend("Criar reels com Remotion")["selected"][0]["skill"], "motion-studio")
    def test_security(self):
        self.assertIn("cybersecurity", [item["skill"] for item in recommend("Avalie segurança, autenticação e LGPD")["selected"]])
    def test_fallback(self):
        self.assertEqual(recommend("uma tarefa sem keyword")["selected"][0]["skill"], "seu-madruga-core")
    def test_all_skills(self):
        registry = json.loads((ROOT / "core/skill-registry.json").read_text(encoding="utf-8"))
        self.assertEqual(len(registry["skills"]), 9)
        for item in registry["skills"]:
            self.assertTrue((ROOT / item["path"]).is_file())
            skill = (ROOT / item["path"]).read_text(encoding="utf-8")
            self.assertTrue(skill.startswith("---\nname: "))

if __name__ == "__main__":
    unittest.main()
