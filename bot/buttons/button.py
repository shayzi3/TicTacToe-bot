
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup



class ButtonData(CallbackData, prefix='game'):
     game_id: str
     position_list: int
     position_index: int
     
     
     
def build_buttons(
     game_state: list,
     game_id: str
) -> InlineKeyboardMarkup:
     builder = InlineKeyboardBuilder()
     
     for state_index in range(3):
          for item_index in range(3):
               item = game_state[state_index][item_index]
               text = '🟥' if item is None else item
               builder.button(
                    text=text,
                    callback_data=ButtonData(
                         game_id=game_id,
                         position_list=state_index,
                         position_index=item_index
                    ).pack()
               )
     builder.adjust(3)
     return builder.as_markup()