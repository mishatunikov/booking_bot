from aiogram.fsm.state import State, StatesGroup


class BookingCheckSG(StatesGroup):
    main_page = State()
    confirm_cancel_booking = State()
    success_cancel_booking = State()
