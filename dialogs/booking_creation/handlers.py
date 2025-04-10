from datetime import datetime

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button, Select

from dialogs.booking_creation.states import BookingCreationSG


async def change_page(
    callback: CallbackQuery, widget: Button, dialog_manager: DialogManager
):
    if widget.widget_id in (
        change_page_data := {'get_previous_dates': -1, 'get_next_dates': 1}
    ):
        dialog_manager.start_data['dates_page'] += change_page_data[
            widget.widget_id
        ]

    elif widget.widget_id in (
        change_page_data := {'get_previous_times': -1, 'get_next_times': 1}
    ):
        dialog_manager.start_data['times_page'] += change_page_data[
            widget.widget_id
        ]


async def select_date(
    callback: CallbackQuery,
    widget: Select,
    dialog_manager: DialogManager,
    item_id: str,
):
    await dialog_manager.update({'selected_date': item_id})
    await dialog_manager.switch_to(BookingCreationSG.select_time)


async def select_time(
    callback: CallbackQuery,
    widget: Select,
    dialog_manager: DialogManager,
    item_id: str,
):
    pass
