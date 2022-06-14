from aiogram.types import Message

from bot_app.db.base import create_dict_con


async def new_user_message(message: Message, target_user_id):
    con, cur = await create_dict_con()
    await cur.execute('insert into message (message_from, message_to, message_id, message_text, date) '
                      'values (%s, %s, %s, %s, %s)',
                      (message.from_user.id, target_user_id, message.message_id, message.text, message.date))
    await con.commit()
    await con.ensure_closed()


async def new_bot_message(message: Message):
    con, cur = await create_dict_con()
    await cur.execute('insert into message (message_from, message_to, message_id, message_text, date) '
                      'values (%s, %s, %s, %s, %s)',
                      (message.from_user.id, message.chat.id, message.message_id, message.text, message.date))
    await con.commit()
    await con.ensure_closed()
