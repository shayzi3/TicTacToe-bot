import os

from aiogram import Bot
from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, CallbackQuery
from utils import HashMessageID
          
     


async def double_send(
     players_id: list[int],
     reply_text: str,
     reply_markup: ReplyKeyboardMarkup,
     inline_text: str | None = None,
     inline_markup: InlineKeyboardMarkup | None = None,
     game_who: dict | None = None
) -> None:
     hash_id = HashMessageID()
     
     async with Bot(os.environ.get('TOKEN')) as bot:
          for user_id in players_id:
               await bot.send_message(
                    chat_id=user_id,
                    text=reply_text + f' Вы играете за {game_who.get(str(user_id))}' if game_who else reply_text,
                    reply_markup=reply_markup
               )
               if inline_markup:
                    inline = await bot.send_message(
                         chat_id=user_id,
                         text=inline_text,
                         reply_markup=inline_markup
                    )
                    hash_id.update({str(user_id): inline.message_id})
                    
async def edit_inline_button(
     text: str,
     players_id: list[int],
     inline_markup: InlineKeyboardMarkup,
) -> None:
     hash_id = HashMessageID()
     
     async with Bot(os.environ.get('TOKEN')) as bot:
          for user_id in players_id:
               await bot.edit_message_text(
                    text=text,
                    chat_id=int(user_id),
                    message_id=hash_id.get(user_id),
                    reply_markup=inline_markup
               )