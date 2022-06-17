import asyncio
import datetime
import random

from bot_app import db, config, markup, utils
from bot_app.misc import routes, bot
from starlette.requests import Request


@routes.post('/support_web_bot_api/new_message/')
async def get_handler(request):
    from_user = int(request.query['message_from'])
    to_user = int(request.query['message_to'])
    message_text = str(request.query['message'])
    message_data = await bot.send_message(5271842643,
                           f"Новое сообщение от пользователя {from_user}:\n\n"
                           f"{message_text}",
                           reply_markup=markup.user_m.new_admin_answer_markup(from_user, to_user))
    await bot.send_message(from_user,
                           f'Вы отправили сообщение для {to_user} используя веб версию чата.\n\n'
                           f'Текст сообщения: \n'
                           f'{message_text}',
                           reply_markup=markup.user_m.new_admin_answer_markup(from_user, to_user))
    await db.message.new_web_message(message_data, from_user, to_user)
    await utils.bot_answer.send_answer(from_user)






