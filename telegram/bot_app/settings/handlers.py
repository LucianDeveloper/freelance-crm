from bot_app.bot_init import *
from bot_app.base.keyboards import main_keyboard
from ..base.auth import is_user_with_phone
from .keyboards import *
from ..start.keyboards import get_phone_keyboard
from ..start.states import StateRegistrationForm


@dp.message_handler(
    lambda message: message.text in lang_selector.get_hot_keyboard_phrases_by_code('main_btn_settings'),
    state='*'
)
@is_user_with_phone
async def open_settings_menu(message: types.Message, state: FSMContext, db_user: UserData):
    await send_message(db_user.id, 'main_btn_settings', await settings_keyboard())


@dp.callback_query_handler(settings_cb.filter(action=Action.edit_phone))
async def send_editor_for_phone(query: types.CallbackQuery, db_user: UserData):
    await send_message(
        db_user.id, 'request_phone',
        keyboard=await get_phone_keyboard(can_refuse=True)
    )
    await StateRegistrationForm.phone.set()


@dp.message_handler(
    lambda message: message.text in lang_selector.get_hot_keyboard_phrases_by_code('send_phone_refuse'),
    state='*'
)
@is_user_with_phone
async def refuse_sending_phone(message: types.Message, state: FSMContext, db_user: UserData):
    await send_message(db_user.id, 'refuse', await main_keyboard(db_user))
