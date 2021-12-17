from aiogram import types
from utils.lang_selector import lang_selector
from .callbacks import finder_cb, categories_cb, Action


async def finder_keyboard():
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(*[
        types.InlineKeyboardButton(
            await lang_selector.say('finder_products'),
            callback_data=finder_cb.new(action=Action.choose_products)
        ),
        types.InlineKeyboardButton(
            await lang_selector.say('finder_services'),
            callback_data=finder_cb.new(action=Action.choose_services)
        ),
    ])
    return keyboard


async def categories_keyboard(action, categories):
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(*[
        types.InlineKeyboardButton(
            x['name'],
            callback_data=categories_cb.new(
                action=action, id=x['id']
            )
        )
        for x in list(sorted(categories, key=lambda x: x['name']))
    ])
    return keyboard
