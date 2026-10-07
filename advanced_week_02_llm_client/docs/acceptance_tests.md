# Week 2 Acceptance-Test Plan

- **AT-01 Configuration:** settings load and validate API/model/retry/token/timeout values.
- **AT-02 Secret Protection:** no API key is hard-coded; `.env` is ignored.
- **AT-03 Typed Output:** mocked valid output becomes `SummaryResult`.
- **AT-04 Prompt Contract:** system/developer/user instructions are distinct.
- **AT-05 Retry:** a retryable failure is retried within the configured limit.
- **AT-06 Rate Limit:** rate-limit errors are treated as retryable.
- **AT-07 Fallback:** the fallback model is attempted after exhausted primary retries.
- **AT-08 Token Budget:** `max_output_tokens` is passed to the provider.
- **AT-09 Observability:** lifecycle events are emitted without the API key.
- **AT-10 Streaming:** a streaming helper is exposed.
- **AT-11 Offline Tests:** tests run without a real API key.
- **AT-12 Documentation:** README, AGENTS, AI log, specification, acceptance tests, and decisions exist.

Final acceptance requires implementation, tests, security review, diff review, and human approval.
