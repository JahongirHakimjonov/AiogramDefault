from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.database.models.base import BaseModel


class User(BaseModel):
    __tablename__ = "custom_user"

    telegram_id: Mapped[int] = mapped_column(BigInteger)
    full_name: Mapped[str] = mapped_column(String)
    username: Mapped[str] = mapped_column(String, nullable=True)


__all__ = ["User"]
