from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from bot_app import config


def main_menu():
    m = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    m.insert(KeyboardButton('Купить'))
    m.insert(KeyboardButton('Мой профиль'))
    m.insert(KeyboardButton('Задать вопрос'))
    return m


def new_admin_answer_markup(user_id, target_user_url):
    m = InlineKeyboardMarkup()
    m.insert(InlineKeyboardButton('История чата', url=f'{config.SERVER_URL}/chat/{user_id}/{target_user_url}'))
    m.insert(InlineKeyboardButton('Ответить', callback_data='user-feedback_'))
    return m