

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


button = [
     [
          KeyboardButton(text='Начать игру!')
     ]
]

reply_start_button = ReplyKeyboardMarkup(
     keyboard=button,
     resize_keyboard=True,
     one_time_keyboard=False
)