from aiogram.fsm.state import State, StatesGroup 


class WaitLinkState(StatesGroup):
    link = State()