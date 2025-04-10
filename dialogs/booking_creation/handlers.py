from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button


async def change_page(
    callback: CallbackQuery, widget: Button, dialog_manager: DialogManager
):
    id_diff = {'get_previous_dates': -1, 'get_next_dates': 1}

    dialog_manager.start_data['dates_page'] += id_diff[widget.widget_id]
