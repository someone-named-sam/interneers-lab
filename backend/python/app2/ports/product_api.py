from abc import ABC, abstractmethod

class ProductAPI(ABC):
    @abstractmethod
    def create(self, data: dict):
        pass

    @abstractmethod
    def get(self, product_id: int):
        pass

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def update(self, product_id: int, data: dict):
        pass

    @abstractmethod
    def delete(self, product_id: int):
        pass