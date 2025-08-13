import asyncio
import sys

from aiogram import Dispatcher
from loguru import logger

import handlers
import middlewares
from bot import bot
from config import load_config
from infrastructure.database.factory import create_pool, make_connection_string

dp = Dispatcher()


async def main() -> None:
    config = load_config()
    logger.remove()
    logger.add(
        sys.stdout,
        level="DEBUG" if config.project.debug else "INFO",
        colorize=True,
    )
    pool = create_pool(url=make_connection_string(config))
    middlewares.setup(dp, pool=pool)
    handlers.setup(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logger.info("Starting bot...")
    asyncio.run(main())
    logger.info("Bot stopped.")
