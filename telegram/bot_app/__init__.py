from .bot_init import types, FSMContext, UserData, send_message
from .base.auth import is_user_with_phone
from .start.handlers import dp, main_keyboard
from .codes.handlers import dp
from .settings.handlers import dp
from .finder.handlers import dp
from aiogram.utils.exceptions import (
    TelegramAPIError,
    MessageNotModified,
    CantParseEntities
)
from config import logger


@dp.message_handler(content_types=types.ContentTypes.ANY)
@is_user_with_phone
async def get_any_useless_content(message: types.Message, state: FSMContext, db_user: UserData):
    """Send to user message, if user writes something unuseful or if he use old keyboards"""
    await send_message(db_user.id, 'for_useless_content', await main_keyboard(db_user))


@dp.errors_handler()
async def errors_handler(update, exception):
    """Logging of telegrams' API errors"""
    if isinstance(exception, MessageNotModified):
        logger.exception('Message is not modified')
        return True

    if isinstance(exception, CantParseEntities):
        logger.error(f'CantParseEntities: {exception} \nUpdate: {update}')
        return True

    if isinstance(exception, TelegramAPIError):
        logger.error(f'TelegramAPIError: {exception} \nUpdate: {update}')
        return True

    logger.error(f'Update: {update} \n{exception}')


# Import all from this module
__all__ = ['dp']
