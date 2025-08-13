from collections.abc import Awaitable, Callable
from typing import Any

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from infrastructure.database.dao.holder import HolderDao


class HolderMiddleware(BaseMiddleware):
    def __init__(self, pool: async_sessionmaker[AsyncSession]):
        super().__init__()
        self.pool = pool

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        async with self.pool() as session:
            data["dao"] = HolderDao(session=session)
            result = await handler(event, data)
            return result
