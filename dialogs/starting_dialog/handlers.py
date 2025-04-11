from datetime import datetime

from aiogram.types import CallbackQuery
from aiogram_dialog import Dialog, DialogManager
from aiogram_dialog.widgets.kbd import Button

from dialogs.booking_creation.states import BookingCreationSG
from dialogs.booking_check.states import BookingCheckSG


async def start_next_dialog(
    callback: CallbackQuery, widget: Button, dialog_manager: DialogManager
):
    id_next_sg = {
        'booking_creation': BookingCreationSG.select_date,
        'booking_check': BookingCheckSG.main_page,
    }
    start_data = {
        'booking_creation': {'dates_page': 0, 'times_page': 0},
        'booking_check': {'booking_number': 0},
    }
    await dialog_manager.start(
        state=id_next_sg.get(widget.widget_id),
        data=start_data.get(widget.widget_id),
    )
