from typing import List, Optional
from pydantic import BaseModel, Field

# Product data model
class Product(BaseModel):
    id: str
    category_id: str #new changes added
    name: str = Field(..., min_length=1)
    description: Optional[str] = None
    category: str
    price: float = Field(..., gt=0)
    brand: Optional[str] = None
    quantity: int = Field(..., ge=0)
