from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

from dotenv import load_dotenv
import os

class Settings(BaseSettings):
    app_name: str
    app_version: str

    database_url: str

    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

@lru_cache
def get_settings() -> Settings:
    return Settings()

Settings = get_settings()