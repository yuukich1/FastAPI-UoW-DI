from app.schemas.users import UserBase
from app.utils.unitofwork import IUnitOfWork
from passlib.hash import pbkdf2_sha256
import jwt 
from datetime import timedelta, datetime
from app.config import ALGORITHM, SECRET_KET
import logging


class UserService:

    
    async def add_user(self, uow: IUnitOfWork, user: UserBase):
        user.password = pbkdf2_sha256.hash(user.password)
        user_dict = user.model_dump()
        async with uow:
            user = await uow.user.add_one(user_dict)
            await uow.commit()
            return user


    async def generate_jwt(self, payload: dict):
        token = jwt.encode(payload=payload, key=SECRET_KET, algorithm=ALGORITHM)
        return token
    
    async def find_one(self, uow: IUnitOfWork, **filter_by):
        async with uow:
            user = await uow.user.find_one(**filter_by)
            if not user:
                return None
            return user

    async def login(self, uow: IUnitOfWork, username: str, password: str):
        logging.info(f'Attempt to login **{username}**')
        async with uow:
            user = await uow.user.find_one(username=username)
            if not user or not pbkdf2_sha256.verify(password, user.password):
                logging.warning(f'**{user.username}** failed password verification') if user else logging.warning(f'User **{username}** does not exist')
                raise ValueError('invalid username or password')
            exp, exp_refresh = timedelta(minutes=30), timedelta(days=30)
            access_token = await self.generate_jwt({'user_id': user.id, 'exp': exp+datetime.now()})
            refresh_token = await self.generate_jwt({'user_id': user.id, 'exp': exp_refresh+datetime.now()})
            await uow.redis.set(refresh_token, user.id, ex=int(exp_refresh.total_seconds()))
            logging.info(f'Added refresh_token to Redis for **{username}**')
            return access_token, refresh_token, exp_refresh