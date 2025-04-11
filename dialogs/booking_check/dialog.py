from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Back, Button, Cancel, Row
from aiogram_dialog.widgets.text import Format

from dialogs.booking_check.getters import (confirm_cancel_getter,
                                           main_page_getter,
                                           success_cancel_getter)
from dialogs.booking_check.handlers import (booking_cancel, change_page,
                                            confirm_cancel, update_booking)
from dialogs.booking_check.states import BookingCheckSG

booking_check = Dialog(
    Window(
        Format('{booking_detail_info}'),
        Row(
            Button(
                Format('{previous}'),
                on_click=change_page,
                id='previous_booking',
                when='have_previous',
            ),
            Button(
                Format('{cancel}'),
                id='booking_cancel',
                on_click=booking_cancel,
                when='booking_exist',
            ),
            Button(
                Format('{next}'),
                on_click=change_page,
                id='next_booking',
                when='have_next',
            ),
        ),
        Button(
            Format('{update_booking}'),
            id='update_booking',
            on_click=update_booking,
            when='booking_exist',
        ),
        Cancel(Format('{back}'), id='back_to_main_menu'),
        state=BookingCheckSG.main_page,
        getter=main_page_getter,
    ),
    Window(
        Format('{cancel_confirmation_text}'),
        Button(
            Format('{confirm_cancel}'),
            id='confirm_cancel',
            on_click=confirm_cancel,
        ),
        Back(Format('{not_confirm_cancel}'), id='back_to_booking'),
        state=BookingCheckSG.confirm_cancel_booking,
        getter=confirm_cancel_getter,
    ),
    Window(
        Format('{success_cancel_booking}'),
        Cancel(Format('{back_to_main_menu}'), id='back_to_main_menu'),
        state=BookingCheckSG.success_cancel_booking,
        getter=success_cancel_getter,
    ),
)
