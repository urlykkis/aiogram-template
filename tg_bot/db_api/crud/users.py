from sqlalchemy import select
from sqlalchemy.sql import text
from sqlalchemy.ext.asyncio import AsyncSession

from tg_bot.db_api.schemas.models import User


async def get_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).filter(User.user_id == user_id))
    return result.scalar()


async def register_user(db: AsyncSession, user_id: int,
                        username: str | None, full_name: str | None):
    user = User(user_id=user_id, username=username, full_name=full_name)

    try:
        db.add(user)
        await db.commit()
    except Exception as e:
        print(e)


async def get_users(db: AsyncSession):
    result = await db.execute(select(User))
    total = await db.execute(text(f"select count(*) from users"))
    return total.scalar(), result.scalars()
