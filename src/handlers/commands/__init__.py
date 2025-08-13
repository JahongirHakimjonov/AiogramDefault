from aiogram import Dispatcher

from .start import router as start_router


def setup(dp: Dispatcher) -> None:
    dp.include_router(start_router)
