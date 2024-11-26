
from aiogram.types import Message
from aiogram.methods import SendMessage
from aiogram import Router

from bot.keyboards import Buttons, get_reply_markup
from utils import Queue


echo_router = Router(name=__name__)


@echo_router.message()
async def echo(message: Message) -> None | SendMessage:
     queue = Queue()
     
     if message.text == 'Начать игру':
          if queue.is_empty() is True: # Очередь пуста
               queue.add(message.from_user.id)
               return await message.reply(
                    text='Игра начата. Вы находитесь в очереди...',
                    reply_markup=get_reply_markup(Buttons.QUIT_FROM_QUEUE)
               )
          ... # Некий aункционал
          
          await message.reply(
               text='Игра началась!',
               reply_markup=get_reply_markup(Buttons.END_GAME_BUTTON)
          )
          
     if message.text == 'Завершить игру':
          await message.reply(
               text='Игра была завершена.',
               reply_markup=get_reply_markup(Buttons.START_GAME_BUTTON)
          )
          
     if message.text == 'Выход':
          queue.remove()
          await message.reply(
               text='Вы вышли из очереди.',
               reply_markup=get_reply_markup(Buttons.START_GAME_BUTTON)
          )
          