from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, AmqpDsn
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

HEADERS = {
    "User-Agent": "MyProject/1.0 (+https://example.com/contact; email: your_email@example.com)",
}


class DBConfig(BaseModel):

    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_port: int
    postgres_db: str
    echo: bool = False

    @property
    def dsn(self) -> str:
        return (
            f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}@"
            f"{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_prefix="APP_CONFIG__",
        env_nested_delimiter="__",
        case_sensitive=False,
    )

    db: DBConfig


settings = Settings()
