from bot_app.bot_init import *
from bot_app.base.callbacks import close_cb, BaseAction
from bot_app.base.keyboards import main_keyboard
from typing import Optional


@dp.callback_query_handler(close_cb.filter(action=BaseAction.close), state='*')
async def close(
        query: types.CallbackQuery,
        db_user: UserData,
        state: Optional[FSMContext] = None
):
    await state.finish()
    await send_message(db_user.id, 'OK', await main_keyboard(db_user))
    await query.message.delete()
