
from loguru import logger
from models import methods_game
from .deck import HashMessageID



async def clear_data(
     players_id: list[int],
     game_id: str
) -> None:
     hash_message = HashMessageID()
     methods_game.delete_game(game_id)
     for user_id in players_id:
          hash_message.delete(user_id)
     
     logger.debug(f'delete game data about game-{game_id} and users from cache {players_id}')
     