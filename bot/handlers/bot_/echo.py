
from aiogram.types import Message
from aiogram import Router
from aiogram.types import ReplyKeyboardRemove

from bot.keyboards import Buttons, get_reply_markup


echo_router = Router(name=__name__)


@echo_router.message()
async def echo(message: Message) -> None:
     
     if message.text == 'Начать игру':
          await message.reply(
               text='Игра началась!',
               reply_markup=get_reply_markup(Buttons.END_GAME_BUTTON)
          )
          
     if message.text == 'Завершить игру':
          await message.reply(
               text='Игра была завершена.',
               reply_markup=get_reply_markup(Buttons.START_GAME_BUTTON)
          )
          