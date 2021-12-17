from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware
from .user_database.check_user import UserData, users_api, user_storage


class UserDatabaseMiddleware(LifetimeControllerMiddleware):
    def __init__(self):
        super().__init__()

    async def pre_process(self, obj, data, *args):
        if hasattr(obj, "update_id"):
            data['db_user'] = UserData(data=None)
            return
        user_id = obj['from']['id']
        user = await user_storage.get(user_id)
        if user is None:
            # If we can get users' info - then we get information about current user and
            # send to handlers like UserData object
            user = UserData(data=await users_api.get(user_id))
            if user.exists():
                await user_storage.update(user)
        data['db_user'] = user

    async def post_process(self, obj, data, *args):
        if 'db_user' in data.keys():
            del data["db_user"]
