from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


def main_menu():
    m = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    m.insert(KeyboardButton('Купить'))
    m.insert(KeyboardButton('Мой профиль'))
    m.insert(KeyboardButton('Задать вопрос'))
    return m


def new_admin_answer_markup(user_id):
    m = InlineKeyboardMarkup()
    m.insert(InlineKeyboardButton('Веб версия', url='https://www.binance.com/en'))
    m.insert(InlineKeyboardButton('Ответить', callback_data='user-feedback_'))
    return m