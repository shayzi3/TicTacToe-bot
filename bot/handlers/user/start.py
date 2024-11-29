
from aiogram.types import Message
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.methods import SendMessage

from keyboards import Buttons, get_reply_markup
from models import methods_free


start_router = Router(name=__name__)


@start_router.message(CommandStart())
async def start(message: Message) -> SendMessage:
     reply = None
     if not methods_free.free_check(message.from_user.id): # Не находится в поиске или игре
          reply = get_reply_markup(Buttons.START_GAME_BUTTON)
     
     return await message.answer(
          text='Приветвую тебя в боте для игры в Крестики Нолики!',
          reply_markup=reply
     )