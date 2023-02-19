from aiogram import Dispatcher
from apscheduler_di import ContextSchedulerDecorator

from .apscheduler import SchedulerMiddleware
from .db import DBMiddleware
from .throttling import ThrottlingMiddleware


def setup_middlewares(dp: Dispatcher, scheduler: ContextSchedulerDecorator):
    dp.setup_middleware(SchedulerMiddleware(scheduler))
    dp.setup_middleware(DBMiddleware())
    dp.setup_middleware(ThrottlingMiddleware())
