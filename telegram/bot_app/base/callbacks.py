from aiogram.utils.callback_data import CallbackData


close_cb = CallbackData('close', 'action')


class BaseAction:
    close = 'close'
    choose = 'choose'
