from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.methods import AnswerCallbackQuery

from buttons import ButtonData, build_buttons
from schemas import GameButtons
from keyboards import get_reply_markup, Buttons
from models import methods_game, methods_free
from utils import (
     analysis_game_state, 
     clear_data, 
     double_send,
     edit_inline_button,
     double_delete
)



callback_router = Router(name=__name__)



@callback_router.callback_query(ButtonData.filter(F.smile == '🟥'))
async def callback_query_handler(
     query: CallbackQuery, 
     callback_data: ButtonData
) -> AnswerCallbackQuery | None:
     btn_data = GameButtons(**callback_data.model_dump())
     game = methods_game.get_data_about_game(btn_data.game_id)
     
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
     gamer_two = methods_free.check_gamer(query.from_user.id)
     
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
     
     winner = await analysis_game_state(
          game_state=game.game_state,
          who_play_who=game.who_plays_who
     )
     if winner:
          await double_delete(
               players_id=list(game.players.keys())
          )
          
          text = f'Игра закончилась в ничью!'
          if isinstance(winner, str):
               text = f'Игра закончилась! Победил {game.players[winner]["name"]}'
          
          await double_send(
               reply_text=text,
               players_id=list(game.players.keys()),
               reply_markup=get_reply_markup(Buttons.START_GAME_BUTTON)
          )
          return await clear_data(
               players_id=list(game.players.keys()),
               game_id=game.game_id
          )
     