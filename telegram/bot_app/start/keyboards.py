from aiogram import types
from utils.lang_selector import lang_selector


async def get_phone_keyboard(can_refuse: bool = False):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.InlineKeyboardButton(
        await lang_selector.say('send_phone'), request_contact=True,
    ))
    if can_refuse:
        keyboard.add(types.InlineKeyboardButton(
            await lang_selector.say('send_phone_refuse')
        ))
    return keyboard
