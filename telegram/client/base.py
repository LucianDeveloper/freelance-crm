import io
from time import sleep
import json
from os import environ
import aiohttp
from config import URL_BACKEND, logger


class Urls:
    api = f''
    jwt = f"{api}/auth/jwt"
    auth = f"{api}/auth"
    users = f"{api}/users"

    login = f'{jwt}/login'
    refresh = f'{jwt}/refresh'

    persons = f'{api}/persons'
    tg_users = f'{persons}/tg'

    texts = f'{api}/langs'
    languages = f'{texts}/langs'
    phrases = f'{texts}/phrases'


class ConfigAPI:
    URL = URL_BACKEND
    LOGIN_URL = Urls.login
    REFRESH_URL = Urls.refresh

    API_LOGIN = environ.get('API_LOGIN', 'e@e.e')
    API_PASS = environ.get('API_PASS', 'e')

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ConfigAPI, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        # Just wait before startup backend
        sleep(15)
        jar = aiohttp.CookieJar(unsafe=True, quote_cookie=False)
        self.session = aiohttp.ClientSession(cookie_jar=jar)

    def __del__(self):
        self.session.close()

    def get_url(self, url: str):
        return f'{self.URL}{url}'

    async def initial(self):
        await self.refresh_login()

    async def refresh_login(self):
        while True:
            async with self.session.post(self.get_url(ConfigAPI.LOGIN_URL), data={
                'username': ConfigAPI.API_LOGIN, 'password': ConfigAPI.API_PASS
            }) as response:
                if response.ok:
                    logger.error('CLIENT WAS INIT')
                    logger.error(f'{await response.read()}')
                    return


api = ConfigAPI()


class BaseAPI:
    URL = ''

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(cls.__class__, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self._URL = api.get_url(self.URL)

    async def create(self, **kwargs):
        response = await api.session.post(f'{self._URL}/', json=kwargs)
        return json.loads(await response.read()) if response.ok else None

    async def get_list(self, **kwargs):
        response = await api.session.get(f'{self._URL}/?{"&".join([f"{k}={v}" for k, v in kwargs.items()])}')
        return json.loads(await response.read()) if response.ok else []

    async def get(self, unique_id):
        response = await api.session.get(self._URL + f'/{unique_id}')
        return json.loads(await response.read()) if response.ok else None

    async def update(self, unique_id, old_json: dict, **kwargs):
        for key, param in kwargs.items():
            old_json.update({key: param})
        response = await api.session.put(self._URL + f'/{unique_id}', json=old_json)
        return json.loads(await response.read()) if response.ok else None

    async def delete(self, unique_id: int):
        response = await api.session.delete(self._URL + f'/{unique_id}')
        return json.loads(await response.read()) if response.ok else None


async def raw_get(url: str, **kwargs):
    params = "&".join([f"{k}={v}" for k, v in kwargs.items()])
    return await api.session.get(
        f'{url}?{params}'
    )


async def basic_get(url: str, **kwargs):
    response = await raw_get(api.get_url(url), **kwargs)
    return json.loads(await response.read()) if response.ok else None


async def raw_post(url: str, json):
    return await api.session.post(url, json=json)


async def basic_post_form(url: str, data: dict):
    return await api.session.post(api.get_url(url), data=data)


async def basic_post(url: str, **send_json):
    response = await raw_post(f'{api.get_url(url)}', json=send_json)
    return json.loads(await response.read()) if response.ok else None


async def get_file_content(url: str) -> io.BytesIO:
    resp = await api.session.get(url)
    if not resp.ok:
        return None
    return io.BytesIO(await resp.read())
