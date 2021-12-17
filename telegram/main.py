from aiogram import executor
import asyncio
from time import sleep
from bot_app import *
from schedules import scheduler

from middlewares.user_database_middleware import UserDatabaseMiddleware

from client.base import api
from config import logger


async def on_startup(_):
    """This method startup first"""
    await api.initial()
    asyncio.create_task(scheduler())


if __name__ == '__main__':
    while True:
        try:
            # Adding middleware to system
            dp.middleware.setup(UserDatabaseMiddleware())
            # Starting pooling updates
            executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
        except Exception as e:
            logger.error(e)
            sleep(10)
