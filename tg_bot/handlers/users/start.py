from aiogram.types import Message, ChatType
from sqlalchemy.ext.asyncio import AsyncSession

from tg_bot.loader import dp
from tg_bot.db_api.crud.users import get_user, register_user
from tg_bot.utils.logger import logger


@dp.message_handler(commands="start", chat_type=ChatType.PRIVATE)
async def command_start(message: Message, session: AsyncSession):
    if await get_user(session, message.from_user.id) is None:
        await register_user(session, message.from_user.id,
                            message.from_user.username,
                            message.from_user.full_name)

        logger.success(
            f"New User: {message.from_user.id} | {message.from_user.username}")

    await message.answer("Меню пользователя")
