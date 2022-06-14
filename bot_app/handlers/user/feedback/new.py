import asyncio
import random

import aiogram.types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ParseMode

from bot_app import markup, utils, db
from bot_app.misc import bot, dp
from bot_app.state.user import User


@dp.message_handler(text='Задать вопрос')
async def user_feedback_start(message: Message, state: FSMContext):
    await state.set_state(User.SupportMessage.message_text)
    await bot.send_message(message.from_user.id,
                           'Пожалуйста отправьте вопрос который хотите задать: ',
                           parse_mode=ParseMode.HTML,
                           reply_markup=markup.base.cancel_menu())


@dp.message_handler(text='Отмена', state=User.SupportMessage.message_text)
async def cancel_user_feedback(message: Message, state: FSMContext):
    await state.finish()
    await bot.send_message(message.from_user.id,
                           'Создание нового запроса в тех поддержку успешно отменено!',
                           reply_markup=markup.user_m.main_menu())


@dp.message_handler(content_types=aiogram.types.ContentType.TEXT, state=User.SupportMessage.message_text)
async def get_user_feedback(message: Message, state: FSMContext):
    await state.finish()
    await bot.send_message(message.from_user.id,
                           'Ваше сообщение было успешно доставлено администратором, ожидайте вам скоро ответят!',
                           reply_markup=markup.user_m.main_menu())
    bot_data = await bot.get_me()
    target_user_id = bot_data.id
    await db.message.new_user_message(message, target_user_id)
    await asyncio.sleep(random.randint(1, 5))
    await utils.bot_answer.send_answer(message.from_user.id)


@dp.message_handler(content_types=aiogram.types.ContentType.ANY, state=User.SupportMessage.message_text)
async def user_feedback_error(message: Message, state: FSMContext):
    await bot.send_message(message.from_user.id,
                           f'Пока что бот принимает только текстовые сообщения!',
                           reply_markup=markup.base.cancel_menu())
