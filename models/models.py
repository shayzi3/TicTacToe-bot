from orm_json import JsonOrm, Column, DataArgs



class Game(JsonOrm):
     game_id: Column
     players: Column
     game_state: Column
     queue: Column
     who_plys_who: Column
     
     class Data(DataArgs):
          tablename = 'game'
          primary = 'game_id'
          path = 'data/games.json'
          
          
if __name__ == '__main__':
     JsonOrm.create_tables()
          