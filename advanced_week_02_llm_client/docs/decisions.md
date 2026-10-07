# Engineering Decisions

## 001 — OpenAI Python SDK
The curriculum identifies the OpenAI Python Library as the Week 2 resource, so the official SDK is used.

## 002 — Pydantic Output Contract
Pydantic provides an explicit, validated Python type for model output.

## 003 — Responses API
The client uses the Responses API for model interaction and structured output parsing.

## 004 — Application-Level Retry
SDK retries are disabled in the client so this repository can explicitly demonstrate and test its own bounded retry/fallback policy.

## 005 — Mocked Unit Tests
Tests do not depend on a live API key, network, account balance, or model availability.

## 006 — Separate Streaming Helper
Complete typed responses and incremental streaming are exposed as separate operations.

## 007 — Safe Observability
Observability receives lifecycle metadata, not credentials or raw sensitive content.
