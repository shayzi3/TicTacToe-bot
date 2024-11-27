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
     