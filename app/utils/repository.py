from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select, delete, update


class AbstractRepository(ABC):

    @abstractmethod
    async def add_one():
        ...

    @abstractmethod
    async def find_all():
        ...

    @abstractmethod
    async def find_one():
        ...

    @abstractmethod
    async def edit_one():
        ...

    @abstractmethod
    async def delete_one():
        ...


class SQLAlchemyRepository(AbstractRepository):

    model = None

    def __init__(self, session: AsyncSession) -> None:
        self.session = session


    async def add_one(self, data: dict):
        stmt = insert(self.model).values(**data).returning(self.model)
        res = await self.session.execute(stmt)
        return res.scalar_one().to_read_model()
    

    async def find_all(self):
        stmt = select(self.model)
        res = await self.session.execute(stmt)
        res = [row[0].to_read_model() for row in res.all()]
        return res
    
    
    async def find_one(self, **filter_by):
        stmt = select(self.model).filter_by(**filter_by)
        res = await self.session.execute(stmt)
        return res.scalar_one().to_read_model()
    
    
    async def edit_one(self, id: int, data: dict):
        stmt = update(self.model).values(**data).filter_by(id=id).returning(self.model)
        res = await self.session.execute(stmt)
        return res.scalar_one().to_read_model()
    
    
    async def delete_one(self, id: int):
        stmt = delete(self.model).filter_by(id=id)
        res = await self.session.execute(stmt)
        return res