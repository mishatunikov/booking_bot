from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from dialogs.starting_dialog.states import StartSG

router = Router()


@router.message(CommandStart())
async def command_start(
    message: Message,
    dialog_manager: DialogManager,
):
    await dialog_manager.start(
        state=StartSG.intro,
        mode=StartMode.RESET_STACK,
        data={'first_open': True},
    )
