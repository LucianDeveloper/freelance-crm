from aiogram.dispatcher.filters.state import State, StatesGroup


class StateRegistrationForm(StatesGroup):
    phone = State()
