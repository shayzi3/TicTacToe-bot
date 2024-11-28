from typing import Any



def hashing(class_: type):
     hashed_class = {}
     
     def wrapper(*args, **kwargs):
          if class_.__name__ not in hashed_class:
               hashed_class[class_.__name__] = class_(*args, **kwargs)
          return hashed_class[class_.__name__]
     return wrapper


@hashing
class Queue:
     def __init__(self) -> None:
          self.queue: list[Any] = []
          
     def add(self, id: tuple[Any]) -> None:
          self.queue.append(id)
          
     def remove(self) -> tuple[Any]:
          if self.queue:
               return self.queue.pop(0)
          return None, None
     
     def is_empty(self) -> bool:
          return not self.queue
     
     def __str__(self) -> str:
          return f'Queue({" ".join(str(element) for element in self.queue).strip()})'
     
     
@hashing  
class HashMessageID:
     def __init__(self) -> None:
          self.messages = {}
          
          
     def get(self, user_id: int) -> int:
          return self.messages.get(str(user_id))
     
     
     def delete(self, user_id: int) -> None:
          try:
               del self.messages[str(user_id)]
          except KeyError:
               return None
          
     def update(self, users: dict[str, int]) -> None:
          # user_id - {'123': 87, '345': 431}
          # key - user id; value - message id
          
          for key, value in users.items():
               self.messages[key] = value
               
          