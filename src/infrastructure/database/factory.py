from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from config import Settings


def make_connection_string(settings: Settings) -> str:
    url = (
        f"postgresql+asyncpg://{settings.db.user}:{settings.db.password}"
        f"@{settings.db.host}/{settings.db.name}"
        f"?async_fallback=True"
    )
    return url


def create_pool(url: str) -> async_sessionmaker[AsyncSession]:
    engine = create_async_engine(url, echo=False)
    return async_sessionmaker(
        bind=engine,
        expire_on_commit=False,
        class_=AsyncSession,
        autoflush=False,
    )


__all__ = ["make_connection_string", "create_pool"]
