from client.base import raw_post, api
from bot_app.bot_init import lang_selector
import json


async def get_code_for_user(phone: str):
    return await raw_post(api.get_url(f'/persons/tg/code'), json={
        "phone": phone,
    })


async def get_code_or_error_text(db_user):
    response = await get_code_for_user(db_user.phone)
    if response.ok:
        schema = json.loads(await response.read())
        text = await lang_selector.format('send_code_to_user', user_code=schema['code'], )
    else:
        text = await lang_selector.say('send_code_to_user_not_found')
    return text
