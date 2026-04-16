from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ENVIRONMENT: str = "development"

    # NEW: frontend origin for CORS
    FRONTEND_ORIGIN: str = "http://localhost:5173"

    model_config = ConfigDict(env_file=".env")


settings = Settings()