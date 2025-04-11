from aiogram.types import User
from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

from dialogs.consts import TIME_CLOSE, TIME_OPEN


async def introduction_getter(
    dialog_manager: DialogManager,
    event_from_user: User,
    i18n: TranslatorRunner,
    **kwargs,
):
    text_selection = int(bool(dialog_manager.start_data))
    if dialog_manager.start_data:
        dialog_manager.start_data.clear()

    menu_text = i18n.main.menu(
        start_data=text_selection,
        name=event_from_user.first_name,
    )

    return {
        'menu_text': menu_text,
        'booking_check_button': i18n.start.booking.check(),
        'booking_creation_button': i18n.start.booking.creation(),
        'reference_button': i18n.reference.button(),
    }


async def reference_getter(
    i18n: TranslatorRunner,
    **kwargs,
):
    return {
        'reference_text': i18n.reference(
            time_open=TIME_OPEN, time_close=TIME_CLOSE
        ),
        'back_to_main_menu': i18n.back.to.main.menu(),
    }
