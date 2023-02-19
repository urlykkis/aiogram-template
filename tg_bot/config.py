from dataclasses import dataclass

from environs import Env

env = Env()
env.read_env(".env")


@dataclass
class Database:
    host: str
    port: int
    user: str
    password: str
    name: str
    db_uri: str


@dataclass
class Redis:
    host: str
    port: str
    password: str | None


@dataclass
class Bot:
    token: str
    tag: str


@dataclass
class Config:
    tgbot: Bot
    db: Database
    redis: Redis

    admins: list


try:
    admins = list(map(int, env.str("ADMINS").split(",")))
except ValueError:
    admins = [int(x) for x in env.str("ADMINS").split(",") if x]

db_uri = f"postgresql+asyncpg://" \
         f"{env.str('DB_USER')}:{env.str('DB_PASSWORD')}@" \
         f"{env.str('DB_HOST')}:{env.int('DB_PORT')}" \
         f"/{env.str('DB_NAME')}"

config = Config(
    tgbot=Bot(
        token=env.str("BOT_TOKEN"),
        tag=env.str("BOT_TAG"),
    ),
    db=Database(
        host=env.str("DB_HOST"),
        port=env.int("DB_PORT"),
        user=env.str("DB_USER"),
        password=env.str("DB_PASSWORD"),
        name=env.str("DB_NAME"),
        db_uri=db_uri,
    ),
    redis=Redis(
        host=env.str("REDIS_HOST"),
        port=env.int("REDIS_PORT"),
        password=env.str("REDIS_PASSWORD")
    ),
    admins=admins
)
