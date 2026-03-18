from typing import List, Optional
from app2.domain.product import Product

class InMemoryProductRepository:

    def __init__(self):
        self.products: List[Product] = []
        self.next_id = 1

    def create(self, data: dict) -> Product:
        product = Product(id=self.next_id, **data)
        self.products.append(product)
        self.next_id += 1
        return product

    def get(self, product_id: int) -> Optional[Product]:
        for p in self.products:
            if p.id == product_id:
                return p
        return None

    def list(self) -> List[Product]:
        return self.products

    def update(self, product_id: int, data: dict) -> Optional[Product]:
        product = self.get(product_id)
        if not product:
            return None

        updated = product.copy(update=data)
        index = self.products.index(product)
        self.products[index] = updated
        return updated

    def delete(self, product_id: int) -> bool:
        product = self.get(product_id)
        if not product:
            return False

        self.products.remove(product)
        return True