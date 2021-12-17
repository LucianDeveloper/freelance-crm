from client.persons.users import users_api
from typing import Dict, Optional
from datetime import datetime, timedelta


class UserData:
    """Class provides methods for manipulating users' data and access to any users' params"""
    def __init__(self, data: dict):
        self.data = data

    def __repr__(self):
        return str(self.data)

    async def reload(self, pk: Optional[int] = None):
        json = await users_api.get(self.id if pk is None else pk)
        if json is not None:
            self.data = json
            await user_storage.update(self)
            return True
        return False

    async def update(self, **kwargs) -> bool:
        """Updating users' data"""
        json = await users_api.update(self.id, old_json=self.data, **kwargs)
        if json is not None:
            self.data = json
            await user_storage.update(self)
            return True
        return False

    def to_dict(self):
        return self.data

    def exists(self) -> bool:
        return self.data is not None

    @property
    def id(self):
        return self.data['id']

    @property
    def username(self):
        return self.data['username']

    @property
    def full_name(self):
        answer = (f'{self.first_name if self.first_name is not None else ""} '
                  f'{self.last_name if self.last_name is not None else ""}')
        return answer

    @property
    def first_name(self):
        return self.data['first_name']

    @property
    def last_name(self):
        return self.data['last_name']

    @property
    def token(self):
        return self.data['token']

    @property
    def phone(self):
        return self.data['phone']


class UserStorage:
    """Class for hashing users information on bot side"""
    def __init__(self):
        self.__users: Dict[int, (datetime, UserData)] = {}

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(cls.__class__, cls).__new__(cls)
        return cls.instance

    async def update(self, db_user: UserData):
        self.__users.update({db_user.id: (datetime.now(), db_user)})

    async def get(self, user_id: int) -> Optional[UserData]:
        try:
            time, user = self.__users[user_id]
            if time + timedelta(minutes=1) < datetime.now():
                return None
            return user
        except:
            return None


user_storage = UserStorage()
