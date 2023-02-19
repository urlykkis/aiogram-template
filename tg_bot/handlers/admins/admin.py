from aiogram.types import Message, ChatType
from sqlalchemy.ext.asyncio import AsyncSession

from tg_bot.loader import dp
from tg_bot.filters.admin_filter import IsAdmin


@dp.message_handler(IsAdmin(), commands="admin", chat_type=ChatType.PRIVATE)
async def command_start(message: Message, session: AsyncSession):
    await message.answer("Меню администратора")
