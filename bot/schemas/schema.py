from dataclasses import dataclass


@dataclass
class GameObject:
     game_id: str
     players: list[int]
     game_state: list[list[int]]
     queue: int
     who_plys_who: dict[str, str]
     
     
@dataclass
class GameButtons:
     smile: str
     game_id: str
     position_list: int
     position_index: int