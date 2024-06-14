from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from app.config import DATABASE_URL
async_engine = create_async_engine(f'{DATABASE_URL}')

async_session_maker = async_sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)
