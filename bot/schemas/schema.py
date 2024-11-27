from dataclasses import dataclass


@dataclass
class GameObject:
     game_id: str
     players: list[int]
     game_state: list[list[int]]
     queue: int
     who_plys_who: dict[str, str]