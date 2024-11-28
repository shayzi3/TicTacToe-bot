from orm_json import JsonOrm, Column, Insert



class Game(JsonOrm):
     game_id: Column
     players: Column
     game_state: Column
     queue: Column
     who_plays_who: Column
     
     class Data:
          tablename = 'game'
          primary = 'game_id'
          path = '/data/games.json'
          
          
class Free(JsonOrm):
     players_in_online: Column
     gamers: Column
     
     class Data:
          tablename = 'free'
          path = '/data/games.json'
          free = True
          
          
def function_main():
     JsonOrm.create_tables()
     
     Insert(Free).values(
          players_in_online = [],
          gamers = {}
     )
          
if __name__ == '__main__':
     function_main()
          