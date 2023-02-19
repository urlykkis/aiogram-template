from aiogram import Dispatcher, executor

from tg_bot.loader import scheduler
from tg_bot.db_api.schemas.models import create_db_and_tables
from tg_bot.handlers import dp
from tg_bot.middleware import setup_middlewares
from tg_bot.utils.logger import setup_logger
from tg_bot.utils.misc.set_bot_commands import set_commands


async def on_startup(dp: Dispatcher):
    await create_db_and_tables()
    await set_commands(dp, dp.bot.config.admins)
    setup_middlewares(dp, scheduler)


def start_bot():
    setup_logger("INFO", ["aiogram.bot.api"])

    scheduler.start()
    executor.start_polling(dp, on_startup=on_startup, skip_updates=False)
