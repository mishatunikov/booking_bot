from aiogram.fsm.state import State, StatesGroup


class BookingCheckSG(StatesGroup):
    main_page = State()
