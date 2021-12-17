from os import environ, listdir, mkdir, path
from typing import List


class DBPaths:
    base = ['src.base.models']
    users = ['src.users.models']
    languages = ['src.languages.models']
    telegram = ['src.telegram.models']
    storage = ['src.storage.models']
    clients = ['src.clients.models']
    schedule = ['src.schedule.models']
    notifications = ['src.notifications.models']
    broadcast = ['src.broadcast.models']

    @property
    def all_paths(self) -> List[str]:
        result = []
        for attr in filter(
            lambda key: not key.startswith('__') and key != 'all_paths',
            self.__dir__()
        ):
            result.extend(self.__getattribute__(attr))
        return result


class MediaPath:
    root = 'media'

    sub_dirs = {}

    @staticmethod
    def init_dirs():
        if MediaPath.root not in listdir():
            mkdir(MediaPath.root)
        for sub_root, sub_paths in MediaPath.sub_dirs.items():
            if not path.isdir(sub_root):
                try:
                    mkdir(f'{sub_root}')
                except:
                    pass
            for s_path in sub_paths:
                try:
                    mkdir(s_path)
                except:
                    pass


MediaPath().init_dirs()
db_paths = DBPaths()


DB_URL = environ.get('DB_URL', "sqlite://sql_app.db")
URL = environ.get('URL', "http://127.0.0.1:8000/api")
TOKEN_TG = environ.get('TOKEN_TG', '1971498893:AAFEYk6hTFUHNC5FDI7uqZEaF4-g-JORR2U')
ALLOW_CORS = environ.get('ALLOW_CORS', 'http://192.168.1.123:3000')

SECRET = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
