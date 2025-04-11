from aiogram.fsm.state import State, StatesGroup


class BookingUpdateSG(StatesGroup):
    main_page = State()
    update_date = State()
    update_time = State()
    update_name = State()
    update_count_person = State()
    confirmation_update = State()
    success_update = State()
