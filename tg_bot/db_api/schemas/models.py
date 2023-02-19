from datetime import datetime

from sqlalchemy import Boolean, Column, BigInteger, String, DateTime

from .session import Base, engine


class User(Base):
    __tablename__ = "users"

    user_id = Column(BigInteger, primary_key=True, index=True, nullable=False)
    username = Column(String, index=True, nullable=True)
    full_name = Column(String, nullable=True)
    registration_date = Column(DateTime, default=datetime.now)
    ban = Column(Boolean, default=False, nullable=False)


async def create_db_and_tables():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
    except:
        pass
