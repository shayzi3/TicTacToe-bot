
from enum import Enum
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


start_game_button = [
     [KeyboardButton(text='Начать игру')]
]
end_game_button = [
     [KeyboardButton(text='Завершить игру')]
]
quit_from_queue = [
     [KeyboardButton(text='Выход')]
]

class Buttons(Enum):
     START_GAME_BUTTON = start_game_button
     END_GAME_BUTTON = end_game_button
     QUIT_FROM_QUEUE = quit_from_queue



def get_reply_markup(keyboard: Buttons) -> ReplyKeyboardMarkup:
     return ReplyKeyboardMarkup(
          keyboard=keyboard.value,
          resize_keyboard=True,
          one_time_keyboard=False
     )