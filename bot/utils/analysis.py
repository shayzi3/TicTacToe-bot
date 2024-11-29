

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
       
     count = 0
     winner = None   
     for combo in game_state:
          if None not in combo: 
               if len(set(combo)) == 1:
                    winner = combo[0]
                    break
               count += 1
     
     if not winner:
          for combo in combinations:
               state = [game_state[0][combo[0]], game_state[1][combo[1]], game_state[2][combo[2]]]
               
               if None not in state:
                    if len(set(state)) == 1:
                         winner = state[0]
                         break
                    count += 1
     
     if count == len(combinations) + len(game_state):
          return True
     return who.get(winner)