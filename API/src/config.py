from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):

    calculator_url: str
    database: SecretStr


settings = Settings()
