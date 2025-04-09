from typing import Callable, Awaitable, Dict, Any

from aiogram.types import (
    TelegramObject,
)
from aiogram import BaseMiddleware
from fluentogram import TranslatorHub


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
