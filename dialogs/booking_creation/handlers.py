from datetime import datetime

from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Select
from fluentogram import TranslatorRunner
from sqlalchemy.ext.asyncio import AsyncSession

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
    dialog_manager.dialog_data.update({'reserved_date': item_id})
    await dialog_manager.switch_to(BookingCreationSG.select_time)


async def select_time(
    callback: CallbackQuery,
    widget: Select,
    dialog_manager: DialogManager,
    item_id: str,
):
    dialog_manager.dialog_data.update({'reserved_time': item_id})
    await dialog_manager.switch_to(BookingCreationSG.input_name)


async def correct_input(
    message: Message,
    widget: MessageInput,
    dialog_manager: DialogManager,
):
    dialog_manager.dialog_data.update({'reservation_name': message.text})
    await dialog_manager.switch_to(
        BookingCreationSG.select_persons_count,
    )


async def incorrect_input(
    message: Message, widget: MessageInput, dialog_manager: DialogManager
):
    i18n: TranslatorRunner = dialog_manager.middleware_data.get('i18n')
    await message.answer(text=i18n.incorrect.input.name())


async def not_text_input(
    message: Message, widget: MessageInput, dialog_manager: DialogManager
):
    i18n: TranslatorRunner = dialog_manager.middleware_data.get('i18n')
    await message.answer(text=i18n.no.text.inpute)


async def select_person(
    callback: CallbackQuery,
    widget: Select,
    dialog_manager: DialogManager,
    item_id: str,
):
    dialog_manager.dialog_data.update({'person_count': int(item_id)})
    await dialog_manager.switch_to(BookingCreationSG.confirmation)


# async def confirm_booking(
#     callback: CallbackQuery,
#     widget: Button,
#     dialog_manager: DialogManager,
# ):
#     session: AsyncSession = dialog_manager.middleware_data.get('session')
