from pydantic import BaseModel
from typing import Optional

class CategoryBase(BaseModel):
    name: str
    description: str


class CategoryScheme(CategoryBase):
    id: int
    image: str