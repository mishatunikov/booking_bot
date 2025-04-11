from aiogram.fsm.state import State, StatesGroup


class StartSG(StatesGroup):
    intro = State()
    reference = State()
