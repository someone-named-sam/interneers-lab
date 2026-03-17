from typing import List, Optional
from pydantic import BaseModel, Field

# Product data model
class Product(BaseModel):
    id: int
    name: str = Field(..., min_length=1)
    description: Optional[str] = None
    category: str
    price: float = Field(..., gt=0)
    brand: Optional[str] = None
    quantity: int = Field(..., ge=0)

# In-memory product store
products: List[Product] = []
next_id = 1

# CRUD operations
def create_product(data: dict) -> Product:
    global next_id
    product = Product(id=next_id, **data)
    products.append(product)
    next_id += 1
    return product

def get_product(product_id: int) -> Optional[Product]:
    for p in products:
        if p.id == product_id:
            return p
    return None

def list_products() -> List[Product]:
    return products

def update_product(product_id: int, data: dict) -> Optional[Product]:
    product = get_product(product_id)
    if not product:
        return None
    updated = product.copy(update=data)
    # Replace in the list
    index = products.index(product)
    products[index] = updated
    return updated

def delete_product(product_id: int) -> bool:
    product = get_product(product_id)
    if not product:
        return False
    products.remove(product)
    return True