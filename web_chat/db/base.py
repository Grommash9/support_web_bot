from aiomysql import connect, Connection, Cursor, DictCursor

from bot_app.config import MYSQL


async def create_con():
    con: Connection = await connect(**MYSQL)
    cur: Cursor = await con.cursor()
    return con, cur


async def create_dict_con():
    con: Connection = await connect(**MYSQL)
    cur: DictCursor = await con.cursor(DictCursor)
    return con, cur
