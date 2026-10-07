from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )
    openai_api_key: str = Field(min_length=1)
    openai_model: str = "gpt-5.6-luna"
    openai_base_url: str | None = None
    openai_fallback_model: str | None = None
    openai_max_retries: int = Field(default=2, ge=0, le=5)
    openai_max_output_tokens: int = Field(default=500, ge=1, le=10000)
    openai_timeout_seconds: float = Field(default=30.0, gt=0, le=300)


def get_settings() -> Settings:
    return Settings()
