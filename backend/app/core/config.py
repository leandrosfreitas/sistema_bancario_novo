from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Ambiente
    DEBUG: bool = True

    # Banco de dados
    DATABASE_URL: str

    # Segurança
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
