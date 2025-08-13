from pydantic_settings import (
    BaseSettings,
)


class TgBot(BaseSettings):
    token: str


class DB(BaseSettings):
    host: str
    port: int | None = None
    name: str
    user: str
    password: str


class ProjectSettings(BaseSettings):
    project_name: str = "aiogram-template"
    debug: bool = False


class SettingsExtractor(BaseSettings):
    BOT_TOKEN: str = ""
    PROJECT_NAME: str = ""
    DEBUG: bool = False

    POSTGRES_HOST: str = ""
    POSTGRES_PORT: int | None = None
    POSTGRES_DB: str = ""
    POSTGRES_USER: str = ""
    POSTGRES_PASSWORD: str = ""

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class Settings(BaseSettings):
    tgbot: TgBot
    db: DB
    project: ProjectSettings


def load_config() -> Settings:
    settings = SettingsExtractor()

    return Settings(
        tgbot=TgBot(token=settings.BOT_TOKEN),
        db=DB(
            host=settings.POSTGRES_HOST,
            port=settings.POSTGRES_PORT,
            name=settings.POSTGRES_DB,
            user=settings.POSTGRES_USER,
            password=settings.POSTGRES_PASSWORD,
        ),
        project=ProjectSettings(
            project_name=settings.PROJECT_NAME,
            debug=settings.DEBUG,
        ),
    )
