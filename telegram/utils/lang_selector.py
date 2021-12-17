from client.texts.phrases import phrase_api
from typing import List


class LanguagesSelector:
    """Class for choosing phrases by users' language"""
    def __init__(self):
        # Dict of all phrases
        self.__phrases: dict = {}
        # Dict with phrases from main keyboard buttons
        self.__hotkey_keyboard_phrases: dict = {}

    async def update(self) -> None:
        """Get all phrases from backend"""
        phrases = {}
        for phrase in await phrase_api.get_list():
            phrases.update({phrase['code']: phrase['text']})
        self.__phrases = phrases
        menu = {}
        for code in [
            'main_btn_recommendations', 'main_btn_activate_code',
            'main_btn_settings', 'send_phone_refuse', 'main_btn_search'
        ]:
            menu.update({
                code: await self.say(code)
            })
        self.__hotkey_keyboard_phrases = menu

    def get_hot_keyboard_phrases_by_code(self, code: str):
        """Get list of phrases on any language by phrase code"""
        return self.__hotkey_keyboard_phrases[code]

    async def get_button_texts(self, codes: List[str]) -> List[str]:
        """Get list of phrases."""
        return [await self.say(code) for code in codes]

    async def say(self, code: str) -> (str, str):
        """Get one phrase by code and lang"""
        if code in self.__phrases.keys():
            return self.__phrases[code]
        else:
            return '???'

    async def format(self, code: str, **kwargs) -> (str, str):
        """Formatting template phrase by yours params"""
        text = await self.say(code)
        answer = []
        for row in text.split('\n'):
            value_is_null = True
            for key, value in kwargs.items():
                placeholder = '{' + f'{key}' + '}'
                if row.find(placeholder) != -1:
                    if row.startswith('???') and value is None:
                        continue
                    row = row.replace(placeholder, f'{value}')
                    value_is_null = False
            if row.startswith('???') and value_is_null:
                continue
            elif row.startswith('???'):
                row = row.replace('???', '')
            answer.append(row)
        return '\n'.join(answer)


lang_selector = LanguagesSelector()
