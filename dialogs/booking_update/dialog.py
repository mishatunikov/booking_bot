from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.kbd import Row, Button, SwitchTo, Cancel
from aiogram_dialog.widgets.text import Format

from dialogs.booking_update.getters import update_booking_getter
from dialogs.booking_update.states import BookingUpdateSG

booking_update = Dialog(
    Window(
        Format('{update_booking_text}'),
        Row(
            Button(Format('{update_date}'), id='update_date'),
            Button(Format('{update_time}'), id='update_time'),
        ),
        Button(
            Format('{update_persons_count}'),
            id='update_persons_count',
        ),
        Button(Format('{update_name}'), id='update_name'),
        Cancel(
            Format('{cancel_update}'),
            id='cancel_update',
        ),
        state=BookingUpdateSG.main_page,
        getter=update_booking_getter,
    ),
)
