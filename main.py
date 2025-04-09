import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram_dialog import setup_dialogs
from fluentogram import TranslatorHub

from config_data.config import Config, load_config
from fsm import storage
from middlewares.outer import TranslatorRunnerMiddleware
from utils.i18n import create_translator_hub
from handlers.user_handlers import router as user_router
from dialogs.booking_creation import booking_creation

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
    dp = Dispatcher(storage=storage)

    translator_hub: TranslatorHub = create_translator_hub()
    dp.workflow_data.update(
        {'config': config, '_translator_hub': translator_hub}
    )

    logger.info('Подключаем роутеры')
    dp.include_routers(user_router, booking_creation)
    setup_dialogs(dp)

    logger.info('Подключаем миддлвари')
    dp.update.middleware(TranslatorRunnerMiddleware())

    await dp.start_polling(bot)


asyncio.run(main())
