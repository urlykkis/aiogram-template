from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler_di import ContextSchedulerDecorator

from tg_bot.config import config


storage = RedisStorage2(config.redis.host, config.redis.port,
                        db=5, pool_size=10, prefix='bot_fsm')
jobstores = {
    'default': RedisJobStore(jobs_key="dispatched_trips_jobs",
                             run_times_key="dispatched_trips_running",
                             host=config.redis.host,
                             db=2,
                             port=config.redis.port)
}

bot = Bot(config.tgbot.token, parse_mode="HTML")
dp = Dispatcher(bot, storage=storage)

scheduler = ContextSchedulerDecorator(
    AsyncIOScheduler(timezone="Europe/Moscow", jobstores=jobstores)
)
scheduler.ctx.add_instance(bot, declared_class=Bot)
bot.config = config
