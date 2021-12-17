from aiogram.utils.callback_data import CallbackData
from ..base.callbacks import BaseAction


finder_cb = CallbackData('finder_cb', 'action')
categories_cb = CallbackData('categories_cb', 'action', 'id')


class Action(BaseAction):
    choose_products = 'choose_products'
    choose_services = 'choose_services'
