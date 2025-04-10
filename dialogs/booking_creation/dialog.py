from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import SwitchTo
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import Button, Row, SwitchTo, Cancel, Select

from dialogs.booking_creation.getters import main_page_getter
from dialogs.booking_creation.handlers import change_page
from dialogs.booking_creation.states import BookingCreationSG

booking_creation = Dialog(
    Window(
        Format(
            '{main_page_text}',
        ),
        Row(
            Button(
                Format('{previous}'),
                on_click=change_page,
                when='have_previous',
                id='get_previous_dates',
            ),
            Select(
                Format('{item[0]}'),
                id='dates',
                item_id_getter=lambda x: x[1],
                items='days_for_booking',
            ),
            Button(
                Format('{next}'),
                on_click=change_page,
                when='have_next',
                id='get_next_dates',
            ),
        ),
        Cancel(Format('{main_menu}'), id='back_to_main_menu'),
        state=BookingCreationSG.main_page,
    ),
    getter=main_page_getter,
)
