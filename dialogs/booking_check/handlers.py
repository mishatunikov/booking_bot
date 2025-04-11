from typing import cast

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button
from fluentogram import TranslatorRunner
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import User, Reserve
from dialogs.booking_check.states import BookingCheckSG


async def change_page(
    callback: CallbackQuery, widget: Button, dialog_manager: DialogManager
):
    change_page_data = {'previous_booking': -1, 'next_booking': 1}
    dialog_manager.start_data['booking_number'] += change_page_data[
        widget.widget_id
    ]


async def booking_cancel(
    callback: CallbackQuery, widget: Button, dialog_manager: DialogManager
):
    await dialog_manager.switch_to(BookingCheckSG.confirm_cancel_booking)


async def confirm_cancel(
    callback: CallbackQuery, widget: Button, dialog_manager: DialogManager
):
    i18n: TranslatorRunner = dialog_manager.middleware_data.get('i18n')
    session: AsyncSession = dialog_manager.middleware_data.get('session')
    user: User = dialog_manager.middleware_data.get('user')
    reserve = await session.get(
        Reserve, dialog_manager.dialog_data.get('selected_reverse_id')
    )
    cast(reserve, Reserve)
    await session.delete(reserve)
    await session.commit()
    await dialog_manager.switch_to(BookingCheckSG.success_cancel_booking)
