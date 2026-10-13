# Model routing and Plan approvals
Use **capability tiers, not fixed vendor equivalence**. Opus and Sonnet are Anthropic product names; Codex model offerings and reasoning effort change. For complicated architecture/security/migrations, propose a high-capability model or increased reasoning. For bounded implementation and mechanical updates, use a cost-efficient capable option. Escalate if repeated failures, uncertainty or regression risk; de-escalate after architecture has been decided. Higher-tier planning may cost more than it saves for small tasks.

## Approval contract
For high-impact tasks deliver: objective, files/domains, options and tradeoffs, ordered steps, migration/rollback, test strategy, risks, approvals needed. Wait for user approval before editing. Always clarify whether plan mode is available rather than claiming to have switched. Do not ask for redundant approval if a concrete plan was already authorized, except for new irreversible actions.

## Stop conditions
- Unknown business requirement affecting correctness: ask a narrow question or state assumption.
- Security-critical change and insufficient evidence: no speculative patch.
- Multiple new dependencies: justify why native stack is inadequate.
- Plan consumes more than fix: scale planning to task.

Do not automatically route all planning to a premium model. Measure quality and cost by task class.
