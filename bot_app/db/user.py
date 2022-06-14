from aiogram.types import User

from bot_app.db.base import create_dict_con


def user_name_formatter(user_data: User):
    if user_data.username:
        return f"@{user_data.username}"
    return None


async def create(from_user: User):
    con, cur = await create_dict_con()
    await cur.execute('insert ignore into user (user_id, user_name, first_name) '
                      'values (%s, %s, %s)',
                      (from_user.id, user_name_formatter(from_user), from_user.first_name))
    await con.commit()
    await con.ensure_closed()
