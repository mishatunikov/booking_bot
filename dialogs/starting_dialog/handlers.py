from aiogram.types import CallbackQuery
from aiogram_dialog import Dialog, DialogManager
from aiogram_dialog.widgets.kbd import Button

from dialogs.booking_creation.states import BookingCreationSG
from dialogs.booking_check.states import BookingCheckSG


async def start_next_dialog(
    callback: CallbackQuery, widget: Button, dialog_manager: DialogManager
):
    id_next_sg = {
        'booking_creation': BookingCreationSG,
        'booking_check': BookingCheckSG,
    }
    state_group = id_next_sg.get(callback.id)
    await dialog_manager.start(state_group.main_page)
