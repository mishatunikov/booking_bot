from aiogram.fsm.storage.base import DefaultKeyBuilder
from redis.asyncio import Redis
from aiogram.fsm.storage.redis import RedisStorage

redis = Redis(host='redis', port=6379)
storage = RedisStorage(
    redis=redis, key_builder=DefaultKeyBuilder(with_destiny=True)
)
