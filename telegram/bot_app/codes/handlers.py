from bot_app.bot_init import *
from .services import get_code_or_error_text
from ..base.auth import is_user_with_phone


@dp.message_handler(
    lambda message: message.text in lang_selector.get_hot_keyboard_phrases_by_code('main_btn_activate_code'),
    state='*'
)
@is_user_with_phone
async def get_temporary_code(message: types.Message, state: FSMContext, db_user: UserData):
    text = await get_code_or_error_text(db_user)
    await send_msg_text(db_user.id, text)
