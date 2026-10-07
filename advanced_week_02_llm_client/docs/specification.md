# Week 2 Specification — Reusable LLM Client

## Objective
Create a reliable model-integration layer with explicit inputs, outputs, errors, limits, and observability hooks.

## Required Capabilities
- Environment-based API key and model configuration.
- Separate system, developer, and user instructions.
- Pydantic typed output contract.
- Structured output parsing.
- Bounded retry handling for transient failures and rate limits.
- Explicit model fallback.
- Configurable maximum output-token budget.
- Streaming helper.
- Safe observability callback.

## Security
No hard-coded keys, committed `.env`, secrets in logs/tests, or unbounded retries.

## Testing
Tests cover successful typed output, retry, fallback, token budget, observability, and input validation without a live API.

## Out of Scope
RAG, embeddings, tool calling, autonomous agents, multi-agent orchestration, deployment, and persistent memory.

## Acceptance Authority
The human maintainer decides whether the implementation satisfies the acceptance criteria.
