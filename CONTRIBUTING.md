# Contributing
Original author: **Rômulo Bezerra**. Contributions welcome under MIT license.

1. Open an issue describing problem and expected impact. Avoid claims of measured improvement without baseline.
2. Keep `SKILL.md` short. Add one focused reference for material that is task-dependent. Remove duplication.
3. No executable installer scripts or external network calls without dedicated security review.
4. Add/update tests or benchmarks when modifying routing heuristics.
5. Run `python tests/validate_skill.py` and `python -m unittest discover -s tests -p 'test_*.py'`.
6. Never include keys or user-private material. Document compatibility differences explicitly.
7. Submit focused PR with change summary, validation evidence and possible regressions. Attribution of others should be maintained alongside original author credit.
