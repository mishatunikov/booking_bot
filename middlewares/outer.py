from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject
from cachetools import TTLCache
from fluentogram import TranslatorHub
from sqlalchemy.ext.asyncio import async_sessionmaker

from db.crud import create_or_update_user
from db.models.models import User


class TranslatorRunnerMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ):
        hub: TranslatorHub = data.get('_translator_hub')
        data['i18n'] = hub.get_translator_by_locale(locale='ru')

        return await handler(event, data)


class DbSessionMiddleware(BaseMiddleware):

    def __init__(self, session_pool: async_sessionmaker):
        self.session_pool = session_pool

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ):
        async with self.session_pool() as session:
            data['session'] = session
            return await handler(event, data)


class TrackUserMiddleware(BaseMiddleware):

    def __init__(self):
        super().__init__()
        self.cache = TTLCache(maxsize=1000, ttl=60 * 60 * 6)

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ):
        user_id = event.from_user.id
        session = data['session']

        if user_id not in self.cache:
            user, _ = await create_or_update_user(
                session,
                user_id,
                event.from_user.first_name,
                event.from_user.last_name,
                event.from_user.username,
            )
            self.cache[user_id] = None

        else:
            user = await session.get(User, user_id)

        data['user'] = user

        return await handler(event, data)
