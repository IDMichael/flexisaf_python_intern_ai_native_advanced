# Engineering Decisions

## Decision 001 — Use FastAPI for the Sample Backend

**Status:** Accepted

**Decision:**

Use FastAPI for the minimal backend service.

**Reason:**

The Week 1 objective is to demonstrate the AI-native engineering lifecycle rather than spend most of the week building complex application functionality. FastAPI allows a small HTTP endpoint and automated test to demonstrate the workflow clearly.

---

## Decision 002 — Keep the Sample Change Small

**Status:** Accepted

**Decision:**

Use a single `/health` endpoint as the reviewed sample change.

**Reason:**

A bounded change makes it easier to demonstrate specification, acceptance criteria, AI delegation, diff inspection, testing, security review, and human approval without unrelated application complexity.

---

## Decision 003 — Use Pytest for Automated Verification

**Status:** Accepted

**Decision:**

Use pytest for the acceptance test.

**Reason:**

The test can directly verify the endpoint behavior and provide a repeatable quality gate.

---

## Decision 004 — Keep Dependencies Minimal

**Status:** Accepted

**Decision:**

Use only FastAPI, Uvicorn, and pytest for this Week 1 demonstration.

**Reason:**

The task focuses on engineering workflow and repository readiness. Additional frameworks, databases, and external services would add complexity without being required by the Week 1 deliverable.
