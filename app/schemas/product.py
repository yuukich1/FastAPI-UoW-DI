from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    name: str
    description: Optional[str]
    category_id: Optional[int]


class ProductScheme(ProductBase):
    id: int


class ProductImageScheme(BaseModel):
    id: int
    image: str
    product_id: int