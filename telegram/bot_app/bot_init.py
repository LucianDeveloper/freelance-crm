from config import TOKEN
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.lang_selector import lang_selector
from aiogram.dispatcher.storage import FSMContext
from middlewares.user_database.check_user import UserData
from client.persons.users import users_api
from .base.states import get_data, update_data, get_data_dict


# Init of telegram bot
bot = Bot(TOKEN, parse_mode='HTML')


# Storage for FSMContext and another inner and temp data
storage = MemoryStorage()

# Dispatcher, for creating handlers
dp = Dispatcher(bot, storage=storage)


async def send_message(user_id: int, code: str, keyboard=None):
    """Sending message to user by `user_id`, with text by phrase code and `lang_id`"""
    text = await lang_selector.say(code)
    return await send_msg_text(user_id, text, keyboard)


async def send_msg_text(user_id: int, text: str, keyboard=None):
    """Send to user message with text"""
    return await bot.send_message(user_id, text, reply_markup=keyboard, disable_web_page_preview=True)


async def edit_message(message: types.Message, code: str, keyboard=None):
    """Edit message with another text or keyboard"""
    text = await lang_selector.say(code)
    return await message.edit_text(text, reply_markup=keyboard)
