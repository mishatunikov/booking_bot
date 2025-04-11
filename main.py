import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram_dialog import setup_dialogs
from fluentogram import TranslatorHub
from sqlalchemy.ext.asyncio import async_sessionmaker

from config_data.config import Config, load_config
from db.connection import engine
from db.models.base import Base
from dialogs.booking_check.dialog import booking_check
from dialogs.booking_creation import booking_creation
from dialogs.booking_update import booking_update
from dialogs.starting_dialog import starting_dialog
from fsm import storage
from handlers.user_handlers import router as user_router
from middlewares.outer import (
    DbSessionMiddleware,
    TrackUserMiddleware,
    TranslatorRunnerMiddleware,
)
from utils.i18n import create_translator_hub

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
        '[%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('Starting bot')

    config: Config = load_config()
    bot = Bot(
        token=config.bot.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    logger.info('Создаем таблицы в БД.')
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

    session_generator = async_sessionmaker(
        engine, autoflush=True, expire_on_commit=False
    )
    dp = Dispatcher(storage=storage)

    translator_hub: TranslatorHub = create_translator_hub()
    dp.workflow_data.update(
        {'config': config, '_translator_hub': translator_hub}
    )

    logger.info('Подключаем роутеры')
    dp.include_routers(
        user_router,
        starting_dialog,
        booking_creation,
        booking_check,
        booking_update,
    )
    setup_dialogs(dp)

    logger.info('Подключаем миддлвари')
    dp.update.middleware(TranslatorRunnerMiddleware())
    dp.update.middleware(DbSessionMiddleware(session_generator))
    dp.message.outer_middleware(TrackUserMiddleware())
    dp.callback_query.outer_middleware(TrackUserMiddleware())

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
