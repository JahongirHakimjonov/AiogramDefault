from pydantic import Field

from dto.base import Base


class User(Base):
    telegram_id: int
    full_name: str
    username: str | None = Field(default=None)


__all__ = ["User"]
