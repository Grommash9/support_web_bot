from pathlib import Path

cwd = Path().cwd()


TOKEN = '5412860565:AAHCWYSoAwDn7yK2vrPqoKcpkba-SMnO9gE'


WEBHOOK_HOST = 'http://142.93.230.250'
WEBHOOK_PATH = f'{cwd.name}'
WEBHOOK_URL = f"{WEBHOOK_HOST}/{WEBHOOK_PATH}/"

BOT_SERVER = {
    'host': '127.0.0.1',
    'port': 2000
}


REDIS = {
    'db': 2,
    'prefix': cwd.name
}


MYSQL = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'root',
    'db': 'support_web_bot',
    # 'unix_socket': '/var/run/mysqld/mysqld.sock'
}


