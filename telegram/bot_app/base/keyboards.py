from aiogram import types
from bot_app.base.callbacks import close_cb, BaseAction
from utils.lang_selector import lang_selector
from middlewares.user_database.check_user import UserData


async def add_close_btn(keyboard, lang_id: int):
    keyboard.add(types.InlineKeyboardButton(
        await lang_selector.say('btn_back', lang_id=lang_id),
        callback_data=close_cb.new(action=BaseAction.close)
    ))
    return keyboard


async def main_keyboard(db_user: UserData, was_auth: bool = False):
    """Main menu keyboard with main buttons"""
    # There is different keyboard for authenticated user and user without token
    codes = [
        'main_btn_search', 'main_btn_recommendations',
        'main_btn_activate_code', 'main_btn_settings'
    ]
    phrases = await lang_selector.get_button_texts(codes)
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(*[types.InlineKeyboardButton(phrase) for phrase in phrases])
    return keyboard


async def url_keyboard(title: str, url: str):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text=title, url=url))
    return keyboard
