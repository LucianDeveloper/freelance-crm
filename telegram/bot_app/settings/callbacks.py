from aiogram.utils.callback_data import CallbackData
from ..base.callbacks import BaseAction


settings_cb = CallbackData('settings_cb', 'action')


class Action(BaseAction):
    edit_phone = 'edit_phone'
