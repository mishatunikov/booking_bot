from dataclasses import dataclass

from environs import Env


@dataclass
class TgBot:
    """
    Класс представляющий бота.

    Attributes:
        bot_token: str,
    """

    bot_token: str


@dataclass
class DataBase:
    """
    Класс DataBase. Содержит конфигурационные данные для работы с бд.

    Attributes:
        database_url: str
    """

    database_url: str


@dataclass
class Config:
    """
    Класс Config. Содержит конфигурационные данные для работы проекта.

    Attributes:
        bot: TgBot,
        database: DataBase.
    """

    bot: TgBot
    database: DataBase


def load_config() -> Config:
    """
    Функция загружает данные из переменных окружения и возвращает
    объект Config.
    Return:
        Config
    """

    env = Env()
    env.read_env()
    return Config(
        bot=TgBot(bot_token=env('BOT_TOKEN')),
        database=DataBase(database_url=env('DATABASE_URL')),
    )
