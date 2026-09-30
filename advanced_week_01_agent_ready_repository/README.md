# Advanced Week 1 — AI-Native Engineering Lifecycle & Agent-Ready Repository

## Project

This repository demonstrates an AI-native engineering workflow in which AI is used as a bounded engineering collaborator while human approval, traceability, testing, security review, and release control remain explicit.

The implementation is intentionally small. The main purpose of this Week 1 submission is to demonstrate the engineering lifecycle and repository controls, not to build a large application.

## Week 1 Deliverable

This repository contains:

- Agent-ready repository instructions
- A written project specification
- Acceptance-test plan
- AI workflow policy and usage log
- A reviewed sample code change
- Automated tests
- Engineering decision records
- Reproducible Python project configuration

## Repository Structure

```text
advanced_week_01_agent_ready_repository/
├── app/
│   ├── __init__.py
│   └── main.py
|__ demo/
|   |__ week1_demo_recording.mp4
├── tests/
│   └── test_health.py
├── docs/
│   ├── specification.md
│   ├── acceptance_tests.md
│   └── decisions.md
├── AGENTS.md
├── AI_USAGE_LOG.md
├── README.md
├── pyproject.toml
├── requirements.txt
└── .gitignore
```

## Requirements

- Python 3.11+
- pip
- Git

## Setup

### 1. Create and activate a virtual environment

Git Bash on Windows:

```bash
python -m venv .venv
source .venv/Scripts/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
uvicorn app.main:app --reload
```

The API is available at:

```text
http://127.0.0.1:8000
```

Health endpoint:

```text
GET /health
```

Expected response:

```json
{
  "status": "healthy"
}
```

## Run Tests

```bash
pytest -v
```

## AI-Native Workflow Demonstrated

```text
Specification
    ↓
Acceptance Criteria
    ↓
Bounded AI Task
    ↓
AI-Generated Change
    ↓
Human Review of Diff
    ↓
Automated Tests
    ↓
Security Review
    ↓
Decision Documentation
    ↓
Human Approval
    ↓
Release
```

AI is not treated as the final authority. The human reviewer owns acceptance, permissions, quality gates, and release approval.

## Sample Change

The reviewed sample change is the `/health` endpoint in `app/main.py`.

The change was evaluated against the acceptance criteria in:

```text
docs/acceptance_tests.md
```

The AI interaction and human review are recorded in:

```text
AI_USAGE_LOG.md
```

## Quality Gate

Before release, the following must be true:

- The implementation satisfies the written specification.
- Acceptance tests pass.
- The Git diff has been reviewed by a human.
- No secrets are committed.
- No unnecessary permissions or dependencies are introduced.
- Engineering decisions are documented.
- The AI-generated change is explicitly accepted by the human reviewer.

## Submission

Submit the GitHub repository link as required by the internship curriculum.

If deployed, provide the live URL. If not deployed, provide a short demo recording where applicable.

Also provide the AI usage log as part of the repository evidence.
