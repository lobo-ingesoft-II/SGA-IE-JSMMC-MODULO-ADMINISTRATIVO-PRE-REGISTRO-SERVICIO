
import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    # Pydantic leerá MONGO_URI de las env vars
    mongo_uri: str = Field(..., env="MONGO_URI")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"

# Instancia global para quien importe `settings`
settings = Settings()

# Constante para quien prefiera no usar Pydantic
MONGO_URI = settings.mongo_uri
print(MONGO_URI)