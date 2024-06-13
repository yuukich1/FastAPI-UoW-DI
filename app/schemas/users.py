from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class RoleBase(BaseModel):
    name: str

class RoleScheme(RoleBase):
    id: int


class UserBase(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserScheme(UserBase):
    id: int
    active: bool
    date_registration: datetime
    role_id: int


