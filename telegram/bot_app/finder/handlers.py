from bot_app.bot_init import *
from bot_app.base.keyboards import main_keyboard
from ..base.auth import is_user_with_phone
from .keyboards import *
from client.base import basic_get


@dp.message_handler(
    lambda message: message.text == lang_selector.get_hot_keyboard_phrases_by_code('main_btn_search'),
    state='*'
)
@is_user_with_phone
async def open_finder_menu(message: types.Message, state: FSMContext, db_user: UserData):
    await send_message(db_user.id, 'finder_title', await finder_keyboard())


@dp.callback_query_handler(finder_cb.filter(action=Action.choose_products))
async def finder_products_categories(message: types.Message, state: FSMContext, db_user: UserData):
    categories = await basic_get('/storage/categories')
    await send_message(
        db_user.id, 'finder_category',
        await categories_keyboard(action=Action.choose_products, categories=categories)
    )


@dp.callback_query_handler(categories_cb.filter(action=Action.choose_products))
async def finder_products(message: types.Message, state: FSMContext, db_user: UserData):
    categories = await basic_get('/storage/categories')
    await send_message(
        db_user.id, 'finder_category',
        await categories_keyboard(action=Action.choose_products, categories=categories)
    )