from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    APP_NAME: str = "Company Brochure API"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = False

    OPENAI_API_KEY: str = Field(default="")
    OPENAI_MODEL: str = "gpt-4.1-mini"

    REQUEST_TIMEOUT: int = 20
    MAX_LINKS: int = 5
    MAX_CONCURRENT_REQUESTS: int = 5


@lru_cache
def get_settings() -> Settings:
    """
    Return a cached Settings instance.
    """
    return Settings()


settings = get_settings()