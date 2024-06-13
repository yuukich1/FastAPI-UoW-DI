from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession

async_engine = create_async_engine('driver://user:password@host:port/db')

async_session_maker = async_sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)
