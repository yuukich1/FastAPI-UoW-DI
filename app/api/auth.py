from fastapi import APIRouter, HTTPException, Form, Response
from app.schemas.users import UserBase
from app.api.dependency import UOWdep
from app.service.user import UserService
from typing import Annotated
from datetime import datetime, timezone
import logging

auth_router = APIRouter(prefix='/auth', tags=['Authorization'])


@auth_router.post('/registration', status_code=201)
async def registraion(user: UserBase, uow: UOWdep):
    user = await UserService().add_user(uow=uow, user=user)
    if not user:
        raise HTTPException(status_code=400, detail='registration is falled')
    return user

@auth_router.post('/login')
async def login(response: Response, uow: UOWdep, username: str = Form(...), password: str = Form(...)):
    try:
        access_token, refresh_token, exp_refresh = await UserService().login(uow, username, password)
        utc_timezone = timezone.utc
        expires_utc = datetime.now(tz=utc_timezone) + exp_refresh
        response.set_cookie('refresh_token', refresh_token, expires=expires_utc, httponly=True)
        return {'type': 'bearer', 'access_token': access_token}
    except ValueError as ve:
        raise HTTPException(status_code=401, detail=str(ve))
    except Exception as e:
        logging.critical(f'Exception: f{e}')
        raise HTTPException(status_code=500)