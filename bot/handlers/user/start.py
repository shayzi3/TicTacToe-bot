
from aiogram.types import Message
from aiogram import Router
from aiogram.filters import CommandStart

from bot.keyboards import reply_start_button


start_router = Router(name=__name__)


@start_router.message(CommandStart())
async def start(message: Message) -> None:
     await message.answer(
          text="Приветвую тебя в боте для игры в Крестики Нолики!",
          reply_markup=reply_start_button
     )