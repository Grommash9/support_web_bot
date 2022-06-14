from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ChatType
from bot_app import db, markup
from bot_app.misc import bot, dp


@dp.message_handler(chat_type=ChatType.PRIVATE, commands=['start'], state='*')
async def process_start(message: Message):
    await db.user.create(message.from_user)
    await bot.send_message(message.from_user.id,
                           f"Бот создан для демонстрации веб интерфейса для тех поддержки или переписки между пользователями.\n"
                           f"Исходный код открыт и доступен https://github.com/Grommash9/support_web_bot\n\n"
                           f"По любым вопросам - @grommash9",
                           reply_markup=markup.user_m.main_menu())

