# AI Coding Agent Instructions

## Purpose

This repository is an agent-ready repository for Advanced Week 1.

AI coding agents may assist with bounded engineering work, but all generated changes require human review and approval before release.

## Repository Context

This is a small Python backend service used to demonstrate an AI-native engineering lifecycle.

Primary application code:

```text
app/
```

Automated tests:

```text
tests/
```

Specifications and engineering records:

```text
docs/
```

## Required Workflow

Before changing code:

1. Read `README.md`.
2. Read `docs/specification.md`.
3. Read `docs/acceptance_tests.md`.
4. Check relevant tests.
5. Understand the requested scope.

After changing code:

1. Inspect the complete Git diff.
2. Run the automated tests.
3. Check for security issues.
4. Confirm that the change satisfies the acceptance criteria.
5. Document significant decisions.
6. Record the AI interaction in `AI_USAGE_LOG.md`.

## Scope Control

Agents must:

- Work only on the task explicitly assigned.
- Avoid unrelated refactoring.
- Avoid changing dependencies unless required.
- Avoid changing public behavior outside the requested scope.
- Never commit secrets.
- Never expose environment variables, credentials, tokens, private keys, or passwords.
- Never disable tests simply to make a task pass.
- Never claim that a change is approved by a human.
- Never merge or release code without explicit human approval.

## Code Standards

- Use clear Python naming.
- Prefer small, readable functions.
- Add type hints where useful.
- Keep API behavior explicit.
- Do not add unnecessary abstractions.
- Keep dependencies minimal.

## Testing Standards

Every behavior change should have an automated test where practical.

A successful task is not established by generated code alone. The implementation must pass the relevant tests and satisfy the written acceptance criteria.

## Human Approval Gate

The final decision to accept, merge, or release an AI-generated change belongs to the human maintainer.

The human reviewer must inspect the diff and test results before approval.
