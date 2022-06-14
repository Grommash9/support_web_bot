from aiogram.dispatcher.filters.state import StatesGroup, State

class User:

    class SupportMessage(StatesGroup):
        message_text = State()
