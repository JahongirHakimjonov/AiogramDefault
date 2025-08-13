from aiogram import Dispatcher

from handlers import commands


def setup(dp: Dispatcher) -> None:
    commands.setup(dp)
