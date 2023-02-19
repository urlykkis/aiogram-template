from aiogram.dispatcher import Dispatcher
from aiogram.types import BotCommand, BotCommandScope, BotCommandScopeType, \
    BotCommandScopeDefault, BotCommandScopeChatAdministrators, \
    BotCommandScopeAllGroupChats, BotCommandScopeChat, BotCommandScopeChatMember

from tg_bot.utils.logger import logger


async def set_commands(dp: Dispatcher, admins: list[int]) -> None:

    default_commands = [
        BotCommand("start", "Запустить бота"),
    ]

    admin_commands = [
        BotCommand("admin", "Админ-Меню"),
    ]

    await dp.bot.set_my_commands(default_commands, scope=BotCommandScopeDefault())

    for admin_id in admins:
        try:
            await dp.bot.set_my_commands(admin_commands + default_commands,
                                         scope=BotCommandScopeChat(admin_id))
        except:
            logger.error(f"{admin_id}: Commands are not installed.")
