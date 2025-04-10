from aiogram.fsm.state import State, StatesGroup


class BookingCreationSG(StatesGroup):
    select_date = State()
    select_time = State()
    input_name = State()
    select_persons_count = State()
    confirmation = State()
