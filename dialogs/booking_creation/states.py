from aiogram.fsm.state import State, StatesGroup


class BookingCreationSG(StatesGroup):
    main_page = State()
