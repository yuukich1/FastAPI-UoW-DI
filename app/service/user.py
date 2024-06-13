from app.schemas.users import UserBase
from app.utils.unitofwork import IUnitOfWork
from passlib.hash import pbkdf2_sha256

class UserService:

    
    async def add_user(self, uow: IUnitOfWork, user: UserBase):
        user.password = pbkdf2_sha256.hash(user.password)
        user_dict = user.model_dump()
        async with uow:
            user = await uow.user.add_one(user_dict)
            await uow.commit()
            return user