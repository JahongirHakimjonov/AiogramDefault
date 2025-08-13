from aiogram import Dispatcher
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from middlewares.database import HolderMiddleware


def setup(dp: Dispatcher, pool: async_sessionmaker[AsyncSession]) -> None:
    dp.update.middleware(HolderMiddleware(pool=pool))
