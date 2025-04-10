from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.base import DefaultKeyBuilder
from aiogram.fsm.storage.memory import MemoryStorage
from redis.asyncio import Redis
from aiogram.fsm.storage.redis import RedisStorage

redis = Redis(host='localhost', port=6379)
storage = RedisStorage(
    redis=redis, key_builder=DefaultKeyBuilder(with_destiny=True)
)
