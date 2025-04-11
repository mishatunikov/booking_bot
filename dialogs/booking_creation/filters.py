from aiogram.filters import BaseFilter
from aiogram.types import Message

from dialogs.booking_creation.consts import MAX_NAME_LENGTH


class CorrectInput(BaseFilter):

    async def __call__(self, message: Message):

        if any(char.isdigit() for char in message.text):
            return False

        if len(message.text) > MAX_NAME_LENGTH:
            return False

        return True
