from unittest.mock import Mock
import openai
import pytest
from app.config import Settings
from app.llm_client import LLMClient
from app.models import SummaryResult

def make_settings(**overrides) -> Settings:
    values = {"openai_api_key":"test-key","openai_model":"primary-model","openai_max_retries":1,
              "openai_max_output_tokens":250,"openai_timeout_seconds":10}
    values.update(overrides)
    return Settings(**values)

def parsed_response() -> Mock:
    response = Mock()
    response.output_parsed = SummaryResult(summary="Python is used to build APIs.", key_points=["Python", "APIs"])
    return response

def test_generate_summary_returns_typed_output():
    provider = Mock(); provider.responses.parse.return_value = parsed_response()
    result = LLMClient(make_settings(), client=provider).generate_summary("Python is used to build APIs.")
    assert isinstance(result, SummaryResult)
    provider.responses.parse.assert_called_once()

def test_retryable_error_is_retried():
    provider = Mock(); provider.responses.parse.side_effect = [openai.APITimeoutError(request=Mock()), parsed_response()]
    sleeps = Mock()
    result = LLMClient(make_settings(), client=provider, sleep_fn=sleeps).generate_summary("Retry this request.")
    assert isinstance(result, SummaryResult); assert provider.responses.parse.call_count == 2
    sleeps.assert_called_once_with(0.5)

def test_fallback_model_is_used_after_primary_failure():
    provider = Mock(); provider.responses.parse.side_effect = [openai.APITimeoutError(request=Mock()), parsed_response()]
    result = LLMClient(make_settings(openai_max_retries=0, openai_fallback_model="fallback-model"), client=provider).generate_summary("Use a fallback.")
    assert isinstance(result, SummaryResult)
    assert provider.responses.parse.call_args_list[0].kwargs["model"] == "primary-model"
    assert provider.responses.parse.call_args_list[1].kwargs["model"] == "fallback-model"

def test_token_budget_is_sent_to_provider():
    provider = Mock(); provider.responses.parse.return_value = parsed_response()
    LLMClient(make_settings(openai_max_output_tokens=123), client=provider).generate_summary("Check token budget.")
    assert provider.responses.parse.call_args.kwargs["max_output_tokens"] == 123

def test_observability_does_not_receive_api_key():
    provider = Mock(); provider.responses.parse.return_value = parsed_response(); events=[]
    def observe(event, data): events.append((event, data))
    LLMClient(make_settings(), client=provider, observability_hook=observe).generate_summary("Observe safely.")
    assert "test-key" not in repr(events)
    assert any(event == "request_started" for event, _ in events)
    assert any(event == "request_succeeded" for event, _ in events)

def test_empty_user_input_is_rejected_before_api_call():
    provider = Mock(); client = LLMClient(make_settings(), client=provider)
    with pytest.raises(ValueError, match="must not be empty"):
        client.generate_summary("   ")
    provider.responses.parse.assert_not_called()
