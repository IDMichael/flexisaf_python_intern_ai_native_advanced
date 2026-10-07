# Advanced Week 2 — LLM APIs, Prompt Design & Output Contracts

## Purpose

This repository implements the Week 2 curriculum requirement: a reusable Python model-integration layer with configuration, prompt design, typed outputs, retries, rate-limit handling, token budgets, fallback models, streaming, tests, and an AI usage log.

## Structure

```text
app/config.py
app/models.py
app/prompts.py
app/llm_client.py
tests/test_llm_client.py
docs/specification.md
docs/acceptance_tests.md
docs/decisions.md
AGENTS.md
AI_USAGE_LOG.md
.env.example
.gitignore
pyproject.toml
requirements.txt
README.md
```

## Setup

```bash
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
cp .env.example .env
```

Edit `.env` and set `OPENAI_API_KEY` locally. Never commit `.env`.

### Configuration

| Variable | Purpose | Template value |
|---|---|---|
| `OPENAI_API_KEY` | Provider API key (required) | placeholder |
| `OPENAI_BASE_URL` | OpenAI-compatible endpoint | `https://api.groq.com/openai/v1` |
| `OPENAI_MODEL` | Primary model | `openai/gpt-oss-20b` |
| `OPENAI_FALLBACK_MODEL` | Explicit fallback model | blank (none) |
| `OPENAI_MAX_RETRIES` | Bounded retries on transient errors (0-5) | `2` |
| `OPENAI_MAX_OUTPUT_TOKENS` | Output-token budget | `500` |
| `OPENAI_TIMEOUT_SECONDS` | Request timeout | `30` |

The template targets Groq. To use OpenAI instead, leave `OPENAI_BASE_URL` blank and set `OPENAI_MODEL` to an OpenAI model name.

## Tests

```bash
pytest -v
git diff --check
```

Tests mock provider calls and do not require a live API key. `pyproject.toml` sets `pythonpath = ["."]` so `app` imports resolve when pytest runs from the repository root.

## Example

Run from the repository root with `.env` configured:

```python
from app.llm_client import LLMClient

client = LLMClient()
result = client.generate_summary("FastAPI is a Python framework for APIs.")
print(result.summary)
```

`result` is a validated `SummaryResult` with `summary` and `key_points` fields.

## Workflow

```text
Configuration → Prompt Contract → Typed Output → Provider Request
→ Retry/Rate Limit Handling → Model Fallback → Validation → Observability
```

## Security

Credentials are environment-based. Secrets are not logged or committed. Model output is treated as untrusted data and validated against an explicit Pydantic contract.

## Scope

RAG, embeddings, tools, autonomous agents, multi-agent orchestration, deployment, and persistent memory are out of scope for Week 2 and belong to later curriculum modules.

## Submission

The Week 2 submission consists of:

- The GitHub repository link.
- A short demo recording showing the deliverable running (`pytest -v` passing and the live call output), since this is a script/library rather than a deployed service.
- The AI usage log (`AI_USAGE_LOG.md`).