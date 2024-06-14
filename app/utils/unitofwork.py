from abc import ABC, abstractmethod
from typing import Type
from redis import asyncio as aioredis
from app.db import async_session_maker
from app.repositories.category import CategoryRepository
from app.repositories.order import OrderRepository
from app.repositories.product import ProductRepository
from app.repositories.product_image import ProductImageRepository
from app.repositories.role import RolesRepository
from app.repositories.status_order import StatusOrderRepository
from app.repositories.user import UserRepository
from app.config import REDIS_URL


class IUnitOfWork(ABC):
    category: Type[CategoryRepository]
    order: Type[OrderRepository]
    product: Type[ProductRepository]
    product_image: Type[ProductImageRepository]
    role: Type[RolesRepository]
    status_order: Type[StatusOrderRepository]
    user: Type[UserRepository]
    redis: aioredis.Redis


    @abstractmethod
    def __init__(self):
        ...


    @abstractmethod
    async def __aenter__(self):
        ...


    @abstractmethod
    async def __aexit__(self, *args):
        ...

    
    @abstractmethod
    async def commit(self):
        ...


    @abstractmethod
    async def rollback(self):
        ...


class UnitOfWork:
    def __init__(self) -> None:
        self.session_factory = async_session_maker
        

    async def __aenter__(self):
        self.session = self.session_factory()
        self.redis = aioredis.from_url(REDIS_URL)
        self.category = CategoryRepository(self.session)
        self.order = OrderRepository(self.session)
        self.product = ProductRepository(self.session)
        self.product_image = ProductImageRepository(self.session)
        self.role = RolesRepository(self.session)
        self.status_order = StatusOrderRepository(self.session)
        self.user = UserRepository(self.session)
        return self

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()
        await self.redis.aclose()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
