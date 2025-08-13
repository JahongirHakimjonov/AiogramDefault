from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

from infrastructure.database.dao.holder import HolderDao

router = Router()


@router.message(CommandStart())
async def on_cmd_start(message: types.Message, dao: HolderDao) -> None:
    if message.from_user is not None:
        await dao.user.add_user_or_update(
            telegram_id=message.from_user.id,
            username=message.from_user.username,
            full_name=f"{message.from_user.first_name} {message.from_user.last_name}",
        )
    await message.answer(
        "Xush kelibsiz! Ilovani ochish uchun pastga bosing."
    )
