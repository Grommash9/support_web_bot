from aiogram.types import Message

from bot_app.db.base import create_dict_con


async def get_correspondence(message_from, message_to):
    con, cur = await create_dict_con()
    await cur.execute('select * from message where message_from = %s and message_to = %s', (message_from, message_to, ))
    messages_from: list = await cur.fetchall()
    await cur.execute('select * from message where message_from = %s and message_to = %s', (message_to, message_from,))
    messages_to: list = await cur.fetchall()
    await con.ensure_closed()
    return sorted(messages_from + messages_to, key=lambda x: x['date'])
