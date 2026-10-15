#!/usr/bin/env python3
"""Roteador indicativo e determinístico; não ativa skills automaticamente."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def recommend(query, registry_path=None, max_skills=3):
    path = Path(registry_path) if registry_path is not None else ROOT / "core" / "skill-registry.json"
    registry = json.loads(path.read_text(encoding="utf-8"))
    text = query.casefold()
    candidates = []
    for item in registry["skills"]:
        matches = [word for word in item["keywords"] if re.search(r"(?<!\\w)" + re.escape(word.casefold()) + r"(?!\\w)", text)]
        if matches:
            candidates.append((len(matches), item["id"], matches))
    candidates.sort(key=lambda item: (-item[0], item[1]))
    selected = [{"skill":skill, "matched_keywords":words} for _, skill, words in candidates if skill != "seu-madruga-core"][:max(1, max_skills)]
    if not selected:
        selected = [{"skill":"seu-madruga-core", "matched_keywords":[]}]
    return {"selected":selected,"advisory_only":True,"context_policy":"load only selected skills and relevant references"}


def main():
    parser = argparse.ArgumentParser(description="SeuMadruga: recomenda skills sem ativá-las")
    parser.add_argument("request", help="Descrição da tarefa")
    parser.add_argument("--max-skills", type=int, default=3)
    args = parser.parse_args()
    print(json.dumps(recommend(args.request, max_skills=args.max_skills), ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
