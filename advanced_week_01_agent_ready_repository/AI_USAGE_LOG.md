# AI Usage Log

## Purpose

This log provides traceability for AI-assisted engineering work performed in this repository.

The log records the requested task, AI assistance, human review, verification, and final disposition.

## Workflow Policy

AI may assist with:

- Understanding requirements
- Proposing implementation approaches
- Drafting code
- Drafting tests
- Drafting documentation
- Reviewing bounded changes for obvious issues

Human control is required for:

- Defining or approving acceptance criteria
- Granting permissions
- Reviewing generated diffs
- Running and evaluating tests
- Security review
- Approving changes
- Approving release

## Sample Change Log

### Change ID

`W01-001`

### Task

Implement a minimal health-check endpoint for the backend service.

### Human-Defined Acceptance Criteria

1. `GET /health` must exist.
2. The endpoint must return HTTP 200.
3. The response must contain `status` with the value `healthy`.
4. An automated test must verify the endpoint.
5. The change must not introduce secrets or unnecessary dependencies.

### AI Assistance Requested

The AI was asked to propose a minimal FastAPI health-check implementation and a pytest test.

### AI-Generated Change

The resulting change added:

- `app/main.py`
- `tests/test_health.py`

The endpoint implementation is intentionally small and contains no authentication, database, external service, or secret handling.

### Human Review

The human reviewer inspected the Git diff and checked:

- Scope was limited to the requested health-check behavior.
- The endpoint matched the specification.
- The test verified the expected response.
- No credentials or secrets were introduced.
- No unnecessary dependency was added.
- The implementation was readable and maintainable.

### Verification

Command:

```bash
pytest -v
```

Expected result:

```text
1 passed
```

### Security Review

Checked for:

- Hard-coded secrets: none
- Credentials: none
- Unsafe file/system operations: none
- External network calls: none
- Excessive permissions: none
- Unnecessary dependencies: none

### Final Disposition

`ACCEPTED FOR SUBMISSION`

The human reviewer approved the sample change after reviewing the diff and verification results.

## AI Usage Rule

Future AI-assisted changes must be recorded in this file with:

- Change ID
- Task
- Acceptance criteria
- AI assistance
- Generated change
- Human review
- Verification
- Security review
- Final disposition
