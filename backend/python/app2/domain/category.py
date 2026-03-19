from pydantic import BaseModel, Field
from typing import Optional

class ProductCategory(BaseModel):
    id: str
    title: str = Field(..., min_length=1)
    description: Optional[str] = None