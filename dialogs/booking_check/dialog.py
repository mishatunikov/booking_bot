from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Format
from aiogram_dialog.widgets.kbd import Row, Button, Cancel

from dialogs.booking_check.getters import main_page_getter
from dialogs.booking_check.handlers import change_page

from dialogs.booking_check.states import BookingCheckSG
from dialogs.booking_check.handlers import change_page

booking_check = Dialog(
    Window(
        Format('{booking_info}', when='booking_exist'),
        Format('{booking_not_exist_text}', when='booking_not_exist'),
        Row(
            Button(
                Format('{previous}'),
                on_click=change_page,
                id='previous_booking',
                when='have_previous',
            ),
            Button(
                Format('{cancel}', when='booking_exist'), id='booking_cancel'
            ),
            Button(
                Format('{next}'),
                on_click=change_page,
                id='next_booking',
                when='have_next',
            ),
        ),
        Cancel(Format('{back}'), id='back_to_main_menu'),
        state=BookingCheckSG.main_page,
        getter=main_page_getter,
    )
)
