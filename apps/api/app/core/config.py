from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Comprehensive ISP Accounting API"
    api_prefix: str = "/api/v1"
    database_url: str = "sqlite+aiosqlite:///./accounting_dev.db"
    seed_demo_data: bool = True

    model_config = SettingsConfigDict(env_file=".env", env_prefix="ACCOUNTING_")


@lru_cache
def get_settings() -> Settings:
    return Settings()

