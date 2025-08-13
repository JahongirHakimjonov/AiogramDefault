from datetime import datetime

from sqlalchemy import BigInteger, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


metadata = Base.metadata


class BaseModel(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(
        BigInteger,
        autoincrement=True,
        primary_key=True,
    )
    created_at: Mapped[datetime] = mapped_column(DateTime(True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(True),
        default=func.now(),
        onupdate=func.now(),
        server_default=func.now(),
    )


__all__ = ["BaseModel", "Base", "metadata"]
