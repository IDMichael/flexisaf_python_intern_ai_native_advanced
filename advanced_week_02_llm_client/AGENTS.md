# AI Coding Agent Instructions

## Before changes
Read `README.md`, `docs/specification.md`, `docs/acceptance_tests.md`, and `docs/decisions.md`.

## Scope
- Work only on the assigned scope.
- Avoid unnecessary dependencies and refactors.
- Week 2 excludes RAG, embeddings, tools, agents, multi-agent orchestration, deployment, and persistent memory.

## Security
- Never hard-code or expose secrets; keep credentials in `.env`, which is never committed.
- Treat LLM output as untrusted data and validate it against the Pydantic contract.
- Keep retry limits finite and model fallback explicit.
- Do not automatically retry partially consumed streams.

## Testing
- Never disable or weaken tests.
- Unit tests must not require a real API key.

## After changes
1. Inspect `git diff`.
2. Run `pytest -v` and `git diff --check`.
3. Review security and verify acceptance criteria.
4. Update `AI_USAGE_LOG.md`.
5. Obtain human approval.

## Authority
Agents must never claim human approval or release authority.