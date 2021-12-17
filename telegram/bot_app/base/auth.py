from aiogram import types
from bot_app.start.handlers import start, start_wait_phone
from aiogram.dispatcher import FSMContext
from middlewares.user_database.check_user import UserData


def is_user_with_phone(func):
    """Decorator for handlers. Here we check that the user has a phone"""
    async def decorator(message: types.Message, state: FSMContext, db_user: UserData):
        if state is not None:
            await state.finish()
        if db_user.data is None:
            return await start(message, state, db_user)
        elif db_user.phone is None:
            return await start_wait_phone(db_user)
        if db_user.username != message.from_user.username:
            await db_user.update(username=message.from_user.username)
        return await func(message, state, db_user)
    return decorator
