from abc import ABC, abstractmethod

class GreetingAPI(ABC):
    @abstractmethod
    def greet(self, name: str, age: int) -> str:
        pass