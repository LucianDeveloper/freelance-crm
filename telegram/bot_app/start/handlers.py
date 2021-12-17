from bot_app.bot_init import *
from bot_app.base.keyboards import main_keyboard
from client.persons.users import users_api
from re import sub
from .states import StateRegistrationForm
from .keyboards import *


@dp.message_handler(commands=['start'], chat_type=types.ChatType.PRIVATE, state='*')
async def start(message: types.Message, state: FSMContext, db_user: UserData):
    """Here creating new users in system"""
    if state is not None:
        await state.finish()
    if not db_user.exists():
        user = await users_api.create(
            id=message.chat.id,
            username=message.chat.username,
            first_name=message.chat.first_name,
            last_name=message.chat.last_name,
        )
        await db_user.reload(user['id'])
        await start_wait_phone(db_user)
    else:
        if db_user.phone is not None:
            await send_message(db_user.id, 'welcome', await main_keyboard(db_user))
        else:
            await start_wait_phone(db_user)


@dp.message_handler(content_types=types.ContentTypes.CONTACT, state=StateRegistrationForm.phone)
async def get_phone(message: types.Message, state: FSMContext, db_user: UserData):
    """Receiving users' phone number"""
    if message.contact.user_id == db_user.id:
        clean_phone = sub(r'[^\d]', '', message.contact.phone_number)
        if db_user.phone != clean_phone:
            await db_user.update(
                phone=clean_phone,
                token=None
            )
        await send_message(db_user.id, 'welcome_new_user', await main_keyboard(db_user))
        await state.finish()
    else:
        await send_message(db_user.id, 'its_not_your_phone')


async def start_wait_phone(db_user: UserData):
    """Sending request for getting phone number"""
    await StateRegistrationForm.phone.set()
    await send_message(
        db_user.id, 'request_phone',
        keyboard=await get_phone_keyboard()
    )


@dp.message_handler(content_types=types.ContentTypes.ANY, state=StateRegistrationForm.phone)
async def get_phone(message: types.Message, state: FSMContext, db_user: UserData):
    """Getting wrong data instead users' phone"""
    await send_message(
        db_user.id, 'its_not_phone',
        keyboard=await get_phone_keyboard()
    )


async def send_not_auth(db_user: UserData):
    """Send to users, when they not authenticated in bot"""
    await send_message(db_user.id, 'not_auth_user', await main_keyboard(db_user))
