


combinations = [
     [0, 0, 0],
     [1, 1, 1],
     [2, 2, 2],
     [0, 1, 2],
     [2, 1, 0]
]


async def analysis_game_state(
     game_state: list,
     who_play_who: dict
) -> str | None:
     who = {}
     for key, value in who_play_who.items():
          who[value] = key
          
     new = []     
     winner = None
     for comba in combinations:
          new.append([game_state[0][comba[0]], game_state[1][comba[1]], game_state[2][comba[2]]])
     new += game_state
     
     count = 0
     for comba in new:
          if len(set(comba)) == 1:
               winner = comba[0]
          
          if None not in comba:
               count += 1
     
     if count == len(new):
          return True
     return who.get(winner) if who.get(winner) else None