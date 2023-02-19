from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsAdmin(BoundFilter):
    async def check(self, message: types.Message):
        return message.from_user.id in message.bot.config.admins
