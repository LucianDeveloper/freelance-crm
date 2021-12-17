from src.languages.models import Phrase


class JSONPhrase:
    def __init__(self, code: str, text: str):
        self.code = code
        self.text = text

    def to_dict(self):
        return {'code': self.code, 'text': self.text}


async def init_russian_phrases():
    phrases = [
        JSONPhrase(code='send_phone', text='📱 Поделиться телефоном'),
        JSONPhrase(code='send_phone_refuse', text='☎️Отменить'),
        JSONPhrase(code='refuse', text='Отменено'),
        JSONPhrase(
            code='request_phone',
            text='📲 Для получения полного доступа вам необходимо предоставить номер телефона'
        ),
        JSONPhrase(
            code='its_not_your_phone',
            text='Это не ваш телефон! Отправьте контакт, принадлежащий вашему аккаунту'
        ),
        JSONPhrase(
            code='its_not_phone', text='Пожалуйста, нажмите на кнопку "Поделиться телефоном"'
        ),
        JSONPhrase(code='welcome_new_user', text='✨ Добро пожаловать!'),
        JSONPhrase(code='welcome', text='✨ С возвращением!'),
        JSONPhrase(code='main_btn_settings', text='⚙ Настройки'),
        JSONPhrase(code='main_btn_search', text='🔍 Найти'),
        JSONPhrase(code='settings_success_update', text='✅ Настройки успешно изменены'),
        JSONPhrase(code='settings_refresh_phone', text='Изменить телефон'),
        JSONPhrase(code='main_btn_activate_code', text='✉️Код подтверждения'),
        JSONPhrase(code='main_btn_recommendations', text='📰 Рекомендации'),

        JSONPhrase(code='support_thx_for_request', text='Спасибо за ваше обращение!'),
        JSONPhrase(code='send_code_to_user', text='🔐 Ваш код: {user_code}'),
        JSONPhrase(code='send_code_to_user_not_found', text='Активный код не найден'),

        JSONPhrase(code='auth_user_not_found', text='⛔️Пользователя с таким номером телефона не найдено'),
        JSONPhrase(
            code='auth_user_success',
            text='✅ Регистрация прошла успешно! Добро пожаловать, {first_name} {last_name}'
        ),
        JSONPhrase(
            code='auth_user_backend_error',
            text='❌ Приносим свои извинения, но к сожалению на стороне сервера произошла ошибка. '
                 'Пожалуйста, повторите попытку позже'
        ),
        JSONPhrase(
            code='auth_user_unknown_error',
            text='❌ Приносим свои извинения, но к сожалению произошла неизвестная ошибка. '
                 'Пожалуйста, повторите попытку позже'
        ),
        JSONPhrase(code='not_auth_user', text='⛔ Вы не прошли авторизацию!'),

        JSONPhrase(code='for_useless_content', text='Простите, я вас не понял'),

        JSONPhrase(code='finder_title', text='Выберите, что хотите найти'),
        JSONPhrase(code='finder_products', text='Товары'),
        JSONPhrase(code='finder_services', text='Услуги'),
        JSONPhrase(code='finder_category', text='Выберите интересующую вас категорию'),
    ]
    old_phrase = [x.code for x in await Phrase.all()]
    for phrase in phrases:
        if phrase.code not in old_phrase:
            try:
                await Phrase.create(**phrase.to_dict())
            except:
                pass
