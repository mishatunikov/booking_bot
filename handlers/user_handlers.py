from aiogram import Router
from aiogram.filters import CommandStart
from aiogram_dialog import DialogManager, StartMode

router = Router()


@router.message(CommandStart())
async def command_start(
    dialog_manager: DialogManager,
):
    await dialog_manager.start(state=..., mode=StartMode.RESET_STACK)
