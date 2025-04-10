from aiogram.fsm.state import State, StatesGroup


class BookingCreationSG(StatesGroup):
    select_date = State()
    select_time = State()
