from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsNumber(BoundFilter):
    async def check(self, message: types.Message):
        try:
            float(message.text)
            return True
        except ValueError:
            return False
