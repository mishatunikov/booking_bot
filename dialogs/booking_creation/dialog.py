from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import SwitchTo, Back
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import (
    Button,
    Row,
    SwitchTo,
    Cancel,
    Select,
    Group,
)

from dialogs.booking_creation.filters import CorrectInput
from dialogs.booking_creation.getters import (
    select_date_getter,
    select_time_getter,
    ask_name_getter,
)
from dialogs.booking_creation.handlers import (
    change_page,
    confirm_booking,
    correct_input,
    incorrect_input,
    not_text_input,
)
from dialogs.booking_creation.states import BookingCreationSG
from dialogs.booking_creation.handlers import select_date, select_time
from dialogs.booking_creation import consts

booking_creation = Dialog(
    Window(
        Format(
            '{select_date_text}',
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
                on_click=select_date,
            ),
            Button(
                Format('{next}'),
                on_click=change_page,
                when='have_next',
                id='get_next_dates',
            ),
        ),
        Cancel(Format('{main_menu}'), id='back_to_main_menu'),
        state=BookingCreationSG.select_date,
        getter=select_date_getter,
    ),
    Window(
        Format('{select_time_text}'),
        Group(
            Select(
                Format('{item[0]}'),
                id='dates',
                item_id_getter=lambda x: x[1],
                items='times_for_booking',
                on_click=select_time,
            ),
            width=consts.WIDTH_TIME_BUTTONS,
        ),
        Button(
            Format('{previous}'),
            on_click=change_page,
            when='have_previous',
            id='get_previous_times',
        ),
        Button(
            Format('{next}'),
            on_click=change_page,
            when='have_next',
            id='get_next_times',
        ),
        Back(Format('{back}')),
        state=BookingCreationSG.select_time,
        getter=select_time_getter,
    ),
    Window(
        Format('{ask_name}'),
        MessageInput(
            func=correct_input,
            content_types=ContentType.TEXT,
            filter=CorrectInput(),
        ),
        MessageInput(func=incorrect_input, content_types=ContentType.TEXT),
        MessageInput(func=not_text_input, content_types=ContentType.ANY),
        SwitchTo(
            Format('{back}'),
            state=BookingCreationSG.select_time,
            id='cancel_input_name',
        ),
        getter=ask_name_getter,
        state=BookingCreationSG.input_name,
    ),
    # Window(
    #     Format('{confirm_booking_text}'),
    #     Button(Format('{confirm}'), on_click=confirm_booking, id='click_yes'),
    #     SwitchTo(
    #         Format('{not_confirm}'),
    #         state=BookingCreationSG.select_time,
    #         id='click_not',
    #     ),
    #     state=BookingCreationSG.confirmation,
    # ),
)
