from sqlalchemy.ext.asyncio import AsyncSession
from tg_bot.db_api.schemas.session import SessionLocal
from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware


class DBMiddleware(LifetimeControllerMiddleware):
    skip_patterns = ['error', 'update']

    # инициализация
    def __init__(self):
        super().__init__()
        self.data = {}

    async def pre_process(self, obj, data, *args):
        async with SessionLocal() as session:
            data["session"]: AsyncSession = session

    # после исполнения хендлера удаляем объект
    async def post_process(self, obj, data, *args):
        session: AsyncSession = data['session']
        await session.close()
        del data['session']
