from client.base import BaseAPI, Urls


class UsersAPI(BaseAPI):
    def __init__(self):
        super(UsersAPI, self).__init__()
        self._URL += Urls.tg_users


users_api = UsersAPI()
