from __future__ import annotations
import time
from collections.abc import Callable, Iterator
from typing import Any
import openai
from openai import OpenAI
from app.config import Settings, get_settings
from app.models import SummaryResult
from app.prompts import DEVELOPER_INSTRUCTIONS, SYSTEM_INSTRUCTIONS, build_user_prompt

ObservabilityHook = Callable[[str, dict[str, Any]], None]


class LLMClient:
    """Reusable model client with typed output, retries, fallback and streaming."""

    def __init__(
        self,
        settings: Settings | None = None,
        *,
        client: OpenAI | None = None,
        sleep_fn: Callable[[float], None] = time.sleep,
        observability_hook: ObservabilityHook | None = None,
    ) -> None:
        self.settings = settings or get_settings()
        self._client = client or OpenAI(
            api_key=self.settings.openai_api_key,
            base_url=self.settings.openai_base_url or None,
            timeout=self.settings.openai_timeout_seconds,
            max_retries=0,
        )
        self._sleep = sleep_fn
        self._observe = observability_hook

    def _emit(self, event: str, **data: Any) -> None:
        if self._observe:
            self._observe(event, data)

    @staticmethod
    def _is_retryable(exc: Exception) -> bool:
        if isinstance(
            exc,
            (openai.APIConnectionError, openai.APITimeoutError, openai.RateLimitError),
        ):
            return True
        if isinstance(exc, openai.APIStatusError):
            return exc.status_code >= 500
        return False

    def _wait(self, attempt: int) -> None:
        self._sleep(0.5 * (2**attempt))

    def generate_summary(self, text: str) -> SummaryResult:
        user_prompt = build_user_prompt(text)
        models = [self.settings.openai_model]
        if self.settings.openai_fallback_model:
            models.append(self.settings.openai_fallback_model)
        last_error: Exception | None = None
        for model_index, model in enumerate(models):
            attempts = self.settings.openai_max_retries + 1
            for attempt in range(attempts):
                self._emit(
                    "request_started",
                    model=model,
                    attempt=attempt + 1,
                    model_index=model_index,
                )
                try:
                    response = self._client.responses.parse(
                        model=model,
                        input=[
                            {"role": "system", "content": SYSTEM_INSTRUCTIONS},
                            {"role": "developer", "content": DEVELOPER_INSTRUCTIONS},
                            {"role": "user", "content": user_prompt},
                        ],
                        text_format=SummaryResult,
                        max_output_tokens=self.settings.openai_max_output_tokens,
                    )
                    if response.output_parsed is None:
                        raise ValueError("Model returned no parsed output")
                    self._emit("request_succeeded", model=model)
                    return response.output_parsed
                except Exception as exc:
                    last_error = exc
                    retryable = self._is_retryable(exc)
                    self._emit(
                        "request_failed",
                        model=model,
                        attempt=attempt + 1,
                        retryable=retryable,
                        error_type=type(exc).__name__,
                    )
                    if not retryable:
                        raise
                    if attempt < attempts - 1:
                        self._wait(attempt)
            if model_index < len(models) - 1:
                self._emit(
                    "model_fallback", from_model=model, to_model=models[model_index + 1]
                )
        assert last_error is not None
        raise last_error

    def stream_text(self, text: str) -> Iterator[str]:
        user_prompt = build_user_prompt(text)
        with self._client.responses.stream(
            model=self.settings.openai_model,
            input=[
                {"role": "system", "content": SYSTEM_INSTRUCTIONS},
                {"role": "developer", "content": DEVELOPER_INSTRUCTIONS},
                {"role": "user", "content": user_prompt},
            ],
            max_output_tokens=self.settings.openai_max_output_tokens,
        ) as stream:
            for event in stream:
                if event.type == "response.output_text.delta":
                    yield event.delta
