from pydantic import BaseModel
from datetime import datetime


class StatusOrderBase(BaseModel):
    name: str


class StatusOrderScheme(StatusOrderBase):
    id: int


class OrderBase(BaseModel):
    item_id: int


class OrderScheme(OrderBase):
    id: int
    user_id: int
    item_id: int
    date_order: datetime
    status_id: int