

from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.methods import AnswerCallbackQuery

from bot.buttons import ButtonData, build_buttons
from bot.schemas import GameButtons
from models import methods_game, methods_free
from utils import edit_inline_button



callback_router = Router(name=__name__)



@callback_router.callback_query(ButtonData.filter())
async def callback_query_handler(
     query: CallbackQuery, 
     callback_data: ButtonData
) -> AnswerCallbackQuery | None:
     btn_data = GameButtons(**callback_data.model_dump())
     game = methods_game.get_data_about_game(btn_data.game_id)
     gamer_two = methods_free.check_gamer(query.from_user.id)
     
     if not game.game_id:
          return AnswerCallbackQuery(
               callback_query_id=query.id,
               text='Эта игра была закончена.'
          )
     # game expired
     if game.queue != query.from_user.id:
          return AnswerCallbackQuery(
               callback_query_id=query.id,
               text='Сейчас не ваша очередь!'
          )
     
     game.game_state[btn_data.position_list][btn_data.position_index] = game.who_plays_who[str(query.from_user.id)]
     text = f'Теперь ход совершает {game.players[str(gamer_two)]["name"]}'
     
     methods_game.update_game(
          game_id=game.game_id,
          game_state=game.game_state,
          queue=gamer_two
     )
     await edit_inline_button(
          text=text,
          inline_markup=build_buttons(game.game_state, game.game_id),
          players_id=list(game.players.keys())
     )
     