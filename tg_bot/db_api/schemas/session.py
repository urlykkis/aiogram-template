from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from tg_bot.config import config

engine = create_async_engine(config.db.db_uri, pool_pre_ping=True)
SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False,
                            autocommit=False, autoflush=False,)
Base = declarative_base()
