import secrets
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "hng12-stage2"
    PROJECT_VERSION: str = "0.0.1"
    PROJECT_DESCRIPTION: str = "HNG12 DEVOPS x BACKEND (Stage 2)"
    API_PREFIX: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)  # Can be set in an env file instead of generating
    DEBUG: bool = False
    TESTING: bool = False

    class Config:
        env_file = ".env"  # Use this if you want to load variables from a .env file


settings = Settings()
