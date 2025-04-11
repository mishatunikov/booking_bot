from aiogram.filters import BaseFilter
from aiogram.types import Message

from dialogs.booking_creation.consts import MAX_NAME_LENGTH, MIN_NAME_LENGTH


class CorrectInput(BaseFilter):

    async def __call__(self, message: Message):

        if not all(char.isalpha() for char in message.text):
            return False

        if len(message.text) not in range(
            MIN_NAME_LENGTH, MAX_NAME_LENGTH + 1
        ):
            return False

        return True
