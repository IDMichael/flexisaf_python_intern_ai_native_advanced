# Acceptance-Test Plan

## Acceptance Criteria

### AT-01 — Health Endpoint Exists

**Given:** the application is running.

**When:** a client sends:

```http
GET /health
```

**Then:** the server responds successfully.

Expected status:

```text
200 OK
```

---

### AT-02 — Health Response Contract

**Given:** the `/health` endpoint is called.

**Then:** the response is JSON containing:

```json
{
  "status": "healthy"
}
```

---

### AT-03 — Automated Verification

The repository must contain an automated test covering the health endpoint.

Command:

```bash
pytest -v
```

Expected result:

```text
1 passed
```

---

### AT-04 — Agent Instructions

The repository must contain `AGENTS.md`.

It must define:

- repository context;
- bounded AI work;
- testing expectations;
- security expectations;
- human review and approval.

---

### AT-05 — AI Traceability

The repository must contain `AI_USAGE_LOG.md`.

The log must record the sample change, acceptance criteria, human review, verification, security review, and final disposition.

---

### AT-06 — Specification Traceability

The repository must contain:

```text
docs/specification.md
```

The specification must describe the intended outcome and the `/health` requirement.

---

### AT-07 — Decision Traceability

The repository must contain:

```text
docs/decisions.md
```

Significant implementation choices must have a documented reason.

---

### AT-08 — Secret Protection

The repository must not contain committed secrets.

`.gitignore` must exclude:

```text
.env
.venv/
__pycache__/
.pytest_cache/
```

---

### AT-09 — Human Review Gate

Before the change is considered accepted:

1. The Git diff must be inspected.
2. Tests must be run.
3. Security checks must be performed.
4. The human reviewer must record the final disposition.

## Acceptance Summary

The Week 1 submission is acceptable when the repository demonstrates the complete workflow:

```text
Specification
→ Acceptance Tests
→ Bounded AI Task
→ Implementation
→ Diff Review
→ Testing
→ Security Review
→ Documentation
→ Human Approval
```
