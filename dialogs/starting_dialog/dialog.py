from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import Row, Button

from dialogs.starting_dialog.states import StartSG
from dialogs.starting_dialog.handlers import start_next_dialog
from dialogs.starting_dialog.getters import introduction_getter


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
        state=StartSG.intro,
        getter=introduction_getter,
    ),
)
