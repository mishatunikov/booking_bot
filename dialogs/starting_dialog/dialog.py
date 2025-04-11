from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Back, Next
from aiogram_dialog.widgets.text import Format

from dialogs.starting_dialog.getters import (
    introduction_getter,
    reference_getter,
)
from dialogs.starting_dialog.handlers import start_next_dialog
from dialogs.starting_dialog.states import StartSG

starting_dialog = Dialog(
    Window(
        Format('{menu_text}'),
        Button(
            Format('{booking_creation_button}'),
            id='booking_creation',
            on_click=start_next_dialog,
        ),
        Button(
            Format('{booking_check_button}'),
            id='booking_check',
            on_click=start_next_dialog,
        ),
        Next(Format('{reference_button}')),
        state=StartSG.intro,
        getter=introduction_getter,
    ),
    Window(
        Format('{reference_text}'),
        Back(Format('{back_to_main_menu}')),
        getter=reference_getter,
        state=StartSG.reference,
    ),
)
