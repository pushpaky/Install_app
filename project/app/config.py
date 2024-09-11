import os
import logging

from pydantic_settings import BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = "dev"
    testing: bool = bool(0)
    db_uri: str = os.getenv("AQUESA_DB_DEV_URI")
    db_name: str = os.getenv("AQUESA_DB_NAME")


def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()
