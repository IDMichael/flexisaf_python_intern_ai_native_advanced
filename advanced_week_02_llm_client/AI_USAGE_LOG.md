# AI Usage Log

## Purpose
Records AI-assisted engineering work for Advanced Week 2. AI is a bounded collaborator; human review, testing, security review, and release approval remain mandatory.

---

## Change W02-001: LLM client implementation

### Task
Build a reusable Python LLM client with configuration, prompt design, typed outputs, retries, rate-limit handling, token budgets, fallback, streaming, tests, and usage traceability.

### Human-Defined Acceptance Criteria
1. Environment-based configuration.
2. No hard-coded API key.
3. Separate system/developer/user instructions.
4. Pydantic typed output.
5. Structured parsing.
6. Bounded retry behavior.
7. Rate-limit/transient error handling.
8. Explicit fallback model.
9. Output-token budget.
10. Streaming helper.
11. Safe observability hook.
12. Offline unit tests.
13. AI usage recorded.

### AI Assistance
Repository architecture, client implementation, Pydantic models, prompts, tests, and retry/security considerations.

### Human Review
Reviewed scope, API contract, configuration safety, retry/fallback behavior, error handling, test coverage, dependency necessity, and secret handling. Human retained final acceptance authority.

### Verification
```bash
pytest -v
git diff --check
git diff
```
Result: 6 tests passed. Tests use mocked provider responses and need no real API key.

### Final Disposition
**ACCEPTED FOR SUBMISSION** after human review and verification.

---

## Change W02-002: Documentation

### Task
Document the specification, acceptance tests, engineering decisions, and agent rules.

### AI Assistance
Documentation drafts (`docs/`, `README.md`, `AGENTS.md`).

### Human Review
Checked documentation against the Week 2 requirements and the implementation.

### Final Disposition
**ACCEPTED FOR SUBMISSION**

---

## Change W02-003: Test import fix and provider base URL

### Task
Fix the pytest `ModuleNotFoundError: app` error and allow the client to target an OpenAI-compatible provider.

### AI Assistance
- Suggested `pythonpath = ["."]` under `[tool.pytest.ini_options]` in `pyproject.toml`.
- Suggested an optional `openai_base_url` setting in `app/config.py`, passed as `base_url` in `app/llm_client.py`.

### Human Review
Applied the edits manually, confirmed `OPENAI_BASE_URL` is optional and blank by default (OpenAI behavior unchanged), and kept all keys in `.env` only.

### Verification
- `pytest -v`: 6 passed.
- Live call to OpenAI: `429 insufficient_quota` (account had no credit). The client surfaced the provider error as designed.
- Live call to Groq: <record the real result here: success, or the error you got>.

### Security Review
- API key hard-coded: none
- `.env` committed: no (`.gitignore` excludes it; confirmed with `git status`)
- Secrets in tests/logs: none
- A partially masked key appeared in a terminal traceback; the key was revoked and replaced.
- Unbounded retry: none
- Automatic retry of consumed streams: none

### Final Disposition
**ACCEPTED FOR SUBMISSION** after human review and verification.