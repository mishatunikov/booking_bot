from aiogram.types import User
from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner


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
        name=f'<b>{event_from_user.first_name}</b>',
    )

    return {
        'menu_text': menu_text,
        'booking_check_button': i18n.start.booking.check(),
        'booking_creation_button': i18n.start.booking.creation(),
    }
