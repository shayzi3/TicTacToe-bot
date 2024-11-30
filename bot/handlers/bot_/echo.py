
from loguru import logger
from aiogram.types import Message
from aiogram.methods import SendMessage
from aiogram import Router

from keyboards import Buttons, get_reply_markup
from buttons import build_buttons
from utils import Queue, double_send, clear_data
from models import methods_game, methods_free



echo_router = Router(name=__name__)



@echo_router.message()
async def echo(message: Message) -> None | SendMessage:
     queue = Queue()
     
     if message.text == 'Начать игру':
          methods_free.free_update(message.from_user.id)
          
          if queue.is_empty() is True: # Очередь пуста
               queue.add((message.from_user.id, message.from_user.full_name)) # Добавляю в очередь
               return await message.reply(
                    text='Игра начата. Вы находитесь в очереди...',
                    reply_markup=get_reply_markup(Buttons.QUIT_FROM_QUEUE)
               )
               
          player_id, player_name = queue.remove() # Очищаю очередь
          
          logger.info(
              f'User {message.from_user.id}-{message.from_user.full_name} started game with {player_id}-{player_name}'
          )
          
          # Добавляю игроков в словарь геймеров чтобы пользовать этим при завершении игры
          methods_free.update_gamers(
               first_id=message.from_user.id,
               second_id=player_id
          )
          # Сохраняю данные о игре
          data = methods_game.insert_data(
               first=message.from_user.id,
               first_name=message.from_user.full_name,
               second=player_id,
               second_name=player_name
          )  
          
          # inline_buttons = data.game_state, data.game_id # Генерирую кнопки
          await double_send(
               players_id=[message.from_user.id, player_id],
               reply_text='Игра началась!',
               reply_markup=get_reply_markup(Buttons.END_GAME_BUTTON),
               inline_text=f'Начинает {message.from_user.full_name}.',
               inline_markup=build_buttons(game_state=data.game_state, game_id=data.game_id),
               game_who=data.who_plays_who
          )  # Отправляю сообщение обоим игрокам о том за кого кого они играют и кто первый ходит
          
     if message.text == 'Завершить игру':
          gamer_two = methods_free.check_gamer(message.from_user.id)  # Достаю id второго игрока
          game_id = methods_game.get_game_id(message.from_user.id)
          
          logger.info(
               f'User {message.from_user.id}-{message.from_user.full_name} finished game-{game_id}'
          )
          
          methods_free.free_update(
               id=[message.from_user.id, gamer_two], 
               mode='remove'
          )  # Удаляю игроков онлайна
          methods_free.update_gamers(
               first_id=message.from_user.id,
               second_id=gamer_two,
               mode='remove'
          ) # Удаляю игроков из словаря геймеров
          await clear_data(
               players_id=[message.from_user.id, gamer_two],
               game_id=game_id
          )  # Очищаю данных о игре
          
          await double_send(
               players_id=[message.from_user.id, gamer_two],
               reply_text=f'Игра завершена досрочно игроком {message.from_user.full_name}.',
               reply_markup=get_reply_markup(Buttons.START_GAME_BUTTON)
          )
          
     if message.text == 'Выход':
          player_id, _ = queue.remove()  # Удаляю игрока из очереди
          methods_free.free_update(
               id=player_id,
               mode='remove'
          ) # Удаляю из онлайна
          
          await message.reply(
               text='Вы вышли из очереди.',
               reply_markup=get_reply_markup(Buttons.START_GAME_BUTTON)
          )
          
          