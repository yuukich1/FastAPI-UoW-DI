from fastapi import FastAPI
from app.api.auth import auth_router
import logging

from app.utils.loger import setup_loger

app = FastAPI()

setup_loger()

async def logginig_start_application():
    logging.info('App startup')

app.add_event_handler('startup', logginig_start_application)

app.include_router(auth_router)