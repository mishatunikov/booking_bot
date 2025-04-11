from aiogram.types import BotCommand
from aiogram import Bot


async def set_menu(bot: Bot):
    commands = [
        BotCommand(command=cmd, description=desc)
        for cmd, desc in [('/start', 'Запустить бота'), ('/help', 'Справка')]
    ]

    await bot.set_my_commands(commands)
