
from loguru import logger
from models import methods_game
from .deck import HashMessageID
from models import methods_free



async def clear_data(
     players_id: list[int],
     game_id: str
) -> None:
     hash_message = HashMessageID()
     methods_game.delete_game(game_id)
     for user_id in players_id:
          hash_message.delete(user_id)
     
     logger.debug(f'delete game data about game-{game_id} and users from cache {players_id}')
     
     

async def clear_users_update(
     players_id: list[int],
     game_id: str
) -> None:
     methods_free.free_update(
          id=players_id, 
          mode='remove'
     )  # Удаляю игроков онлайна
     methods_free.update_gamers(
          players_id=players_id,
          mode='remove'
     ) # Удаляю игроков из словаря геймеров
     return await clear_data(
          players_id=players_id,
          game_id=game_id
     )  # Очищаю данные о игре