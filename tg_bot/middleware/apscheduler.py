from aiogram.contrib.middlewares.environment import BaseMiddleware
from apscheduler_di import ContextSchedulerDecorator

from typing import Callable, Any, Dict, Awaitable
from aiogram.types.base import TelegramObject


class SchedulerMiddleware(BaseMiddleware):
    def __init__(self, scheduler: ContextSchedulerDecorator):
        self.scheduler = scheduler
        super().__init__()

    async def __call__(self,
                       handler: Callable[
                           [TelegramObject, Dict[str, Any]], Awaitable[Any]
                       ],
                       event: TelegramObject,
                       data: Dict[str, Any]) -> Any:
        data['apscheduler'] = self.scheduler
        return await handler(event, data)
