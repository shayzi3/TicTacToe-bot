import random

from string import (
     ascii_letters,
     digits,
     ascii_uppercase
)
from orm_json import (
     Select,
     Delete,
     Update,
     Insert,
     custom_option
)
from .models import Game, Free


class MethodsForGame:
     
     @staticmethod
     def __generate_game_id() -> str:
          letters = ascii_letters + digits + ascii_uppercase
          return ''.join([random.choice(letters) for _ in range(8)])
     
     def insert_data(
          self, 
          first: int, 
          first_name: str, 
          second: int, 
          second_name: str
     ) -> Game:
          players = {
               str(first): {
                    'id': first,
                    'name': first_name
                    
               },
               str(second): {
                    'id': second,
                    'name': second_name
               }
          }
          who_plays_who = {
               str(first): '⭕',
               str(second): '❌'
          }
          game_state = [
               [None, None, None],
               [None, None, None],
               [None, None, None],
          ]
          return Insert(Game).values(
               queue=first,
               game_state=game_state,
               game_id=self.__generate_game_id(),
               who_plays_who=who_plays_who,
               players=players
          )
          
     @staticmethod
     def get_data_about_game(game_id: str) -> Game:
          return Select(Game).where(game_id=game_id).one()
          
          
     @staticmethod
     def update_game(game_id: str, game_state: list, queue: int) -> None:
          return Update(Game).where(game_id=game_id).values(game_state=game_state, queue=queue)
     
     @staticmethod
     def delete_game(game_id: str) -> None:
          return Delete(Game).drop_one_data(game_id=game_id)
     
     
     @staticmethod
     def get_game_id(player: int) -> str:
          
          @custom_option(model=Game)
          def check_game_id(players) -> bool:
               return str(player) in players.keys()
          
          return Select(Game).custom_options(check_game_id).one().game_id
          
          
class MethodsForFree:
     
     @staticmethod
     def free_check(id: int) -> None:
          return id in Select(Free).where().one().players_in_online
     
     @staticmethod
     def check_gamer(id: int) -> int:
          return Select(Free).where().one().gamers.get(str(id))
     
     @staticmethod
     def free_update(id: int | list[int], mode: str = 'append') -> None:
          free: list[int] = Select(Free).where().one().players_in_online
          if isinstance(id, int):
               id = [id]
          
          if mode == 'append':
               for _id in id:
                    free.append(_id)
          else:
               try:
                    for _id in id:
                         free.remove(_id)
               except:
                    return None
          return Update(Free).values(players_in_online=free)
     
     
     @staticmethod
     def update_gamers(
          first_id: int,
          second_id: int,
          mode: str = 'append'
     ) -> None:
          free = Select(Free).where().one().gamers
          
          if mode == 'append':
               free.update({
                    str(first_id): second_id,
                    str(second_id): first_id
               })
          else:
               try:
                    del free[str(first_id)]
                    del free[str(second_id)]
               except KeyError:
                    return None
          return Update(Free).values(gamers=free)
     
     
methods_game = MethodsForGame()
methods_free = MethodsForFree()