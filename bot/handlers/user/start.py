
from aiogram.types import Message
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.methods import SendMessage

from bot.keyboards import Buttons, get_reply_markup


start_router = Router(name=__name__)


@start_router.message(CommandStart())
async def start(message: Message) -> SendMessage:
     return await message.answer(
          text="Приветвую тебя в боте для игры в Крестики Нолики!",
          reply_markup=get_reply_markup(Buttons.START_GAME_BUTTON)
     )