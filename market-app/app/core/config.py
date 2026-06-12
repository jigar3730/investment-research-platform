from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Investment Research Platform"
    DATABASE_PATH: str = "/app/data/platform.db"
    OLLAMA_HOST: str = "http://ollama:11434"

    class Config:
        env_file = ".env"

settings = Settings()