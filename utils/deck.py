from typing import Any, Callable




class Queue:
     queue: list[Any] = []
          
     @classmethod
     def add(cls, id: Any) -> None:
          cls.queue.append(id)
          
          
     @classmethod
     def remove(cls) -> Any:
          return cls.queue.pop(0)
     
     
     @classmethod
     def is_empty(cls) -> bool:
          return not cls.queue
     
     @classmethod
     def __str__(cls) -> str:
          return f'Queue({" ".join(str(element) for element in cls.queue).strip()})'
     