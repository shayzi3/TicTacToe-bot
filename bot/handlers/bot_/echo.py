import os

from aiogram.types import Message
from aiogram.methods import SendMessage
from aiogram import Router, Bot
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup

from bot.keyboards import Buttons, get_reply_markup
from utils import Queue
from models import methods_game, methods_free


echo_router = Router(name=__name__)



async def double_send(
     players_id: list[int],
     reply_text: str,
     reply_markup: ReplyKeyboardMarkup,
     inline_text: str | None = None,
     inline_markup: InlineKeyboardMarkup | None = None,
     game_who: dict | None = None
) -> None:
     
     async with Bot(os.environ.get('TOKEN')) as bot:
          for user_id in players_id:
               await bot.send_message(
                    chat_id=user_id,
                    text=reply_text + f' Вы играете за {game_who.get(str(user_id))}' if game_who else reply_text,
                    reply_markup=reply_markup
               )
               if inline_markup:
                    await bot.send_message(
                         chat_id=user_id,
                         text=inline_text,
                         reply_markup=None
                    )



@echo_router.message()
async def echo(message: Message) -> None | SendMessage:
     queue = Queue()
     
     if message.text == 'Начать игру':
          methods_free.free_update(message.from_user.id)
          
          if queue.is_empty() is True: # Очередь пуста
               queue.add((message.from_user.id, message.from_user.full_name))
               return await message.reply(
                    text='Игра начата. Вы находитесь в очереди...',
                    reply_markup=get_reply_markup(Buttons.QUIT_FROM_QUEUE)
               )
               
          player_id, player_name = queue.remove()
          methods_free.update_gamers(
               first_id=message.from_user.id,
               second_id=player_id
          )
          data = methods_game.insert_data(
               first=message.from_user.id,
               first_name=message.from_user.full_name,
               second=player_id,
               second_name=player_name
          )
          # inline_buttons = data.game_state, data.game_id
          await double_send(
               players_id=[message.from_user.id, player_id],
               reply_text='Игра началась!',
               reply_markup=get_reply_markup(Buttons.END_GAME_BUTTON),
               inline_text=f'Начинает {message.from_user.full_name}.',
               inline_markup=1,
               game_who=data.who_plays_who
          )
          
     if message.text == 'Завершить игру':
          gamer_two = methods_free.check_gamer(message.from_user.id)
          
          methods_free.free_update(
               id=[message.from_user.id, gamer_two], 
               mode='remove'
          )
          methods_free.update_gamers(
               first_id=message.from_user.id,
               second_id=gamer_two,
               mode='remove'
          )
          await double_send(
               players_id=[message.from_user.id, gamer_two],
               reply_text=f'Игра завершена досрочно игроком {message.from_user.full_name}.',
               reply_markup=get_reply_markup(Buttons.START_GAME_BUTTON)
          )
          
     if message.text == 'Выход':
          queue.remove()
          await message.reply(
               text='Вы вышли из очереди.',
               reply_markup=get_reply_markup(Buttons.START_GAME_BUTTON)
          )
          
          