from faker import Faker
from dotenv import load_dotenv
import os

fake = Faker()

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
SECRET_KET = os.getenv('SECRET_KET')
ALGORITHM = os.getenv('ALGORITHM')
REDIS_URL = os.getenv('REDIS_URL')
