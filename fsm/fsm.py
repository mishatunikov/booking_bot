from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.base import DefaultKeyBuilder
from redis.asyncio import Redis
from aiogram.fsm.storage.redis import RedisStorage


redis = Redis(host='localhost')
storage = RedisStorage(
    redis=redis, key_builder=DefaultKeyBuilder(with_destiny=True)
)
