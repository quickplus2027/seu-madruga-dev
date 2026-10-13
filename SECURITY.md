# Security policy
For private security reports, contact the repository owner through GitHub's private vulnerability reporting if enabled; otherwise open a GitHub issue **without sensitive exploit details** requesting a secure disclosure route. Do not post credentials or active exploit chains publicly.

Threat model: prompt injection in repository content and fetched skills, unsafe terminal commands, supply-chain scripts, unnecessary filesystem/network privilege and exfiltration. The Skill is a set of instructions with optional local validators; it does not autonomously enforce client sandboxes. Every third-party Skill requires manual inspection. Security guidance is not a security certification.

Do not include API keys, secrets, credentials or personal data in benchmark fixtures, issues or logs. Maintainers review third-party pull requests before merge.
