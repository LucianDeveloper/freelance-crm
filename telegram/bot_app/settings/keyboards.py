from aiogram import types
from utils.lang_selector import lang_selector
from .callbacks import settings_cb, Action


async def settings_keyboard():
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(*[
        types.InlineKeyboardButton(
            await lang_selector.say('settings_refresh_phone'),
            callback_data=settings_cb.new(action=Action.edit_phone)
        ),
    ])
    return keyboard
