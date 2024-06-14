import pytest
from app.service.user import UserService, UserBase
from app.utils.unitofwork import IUnitOfWork, UnitOfWork
from app.config import fake


uow = UnitOfWork()

@pytest.mark.asyncio
async def test_create_user_service():
    name = fake.user_name()
    email = fake.email()
    user = await UserService().add_user(uow, UserBase(username=name, 
                                                    email=email, 
                                                    password=fake.password()))
    assert user.username == name
    assert user.email == email


@pytest.mark.asyncio
async def test_find_one_user():
    username = 'yuuki'
    user = await UserService().find_one(uow, username=username)
    assert user.username == username




